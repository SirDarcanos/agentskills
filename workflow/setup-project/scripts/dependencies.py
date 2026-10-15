#!/usr/bin/env python3
"""Inspect or add approved native GitHub blockers; read-only unless --apply."""

import argparse
import json
import re
import subprocess
import sys
from collections import deque
from pathlib import Path

MAX_ISSUES = 500


class Blocked(ValueError):
    """The intended graph cannot be safely established or verified."""


def require(condition, message):
    if not condition:
        raise Blocked(message)


def positive_int(value):
    return type(value) is int and value > 0


def parse_plan(plan):
    require(isinstance(plan, dict) and set(plan) == {"repository", "dependencies"},
            "Plan requires only repository and dependencies")
    repo = plan["repository"]
    require(isinstance(repo, str) and re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*", repo),
        "repository must be OWNER/REPO")
    require(isinstance(plan["dependencies"], list), "dependencies must be an array")
    edges = set()
    for edge in plan["dependencies"]:
        require(isinstance(edge, dict) and set(edge) == {"blocked", "by"},
                "Each dependency requires only blocked and by")
        a, b = edge["blocked"], edge["by"]
        require(positive_int(a) and positive_int(b) and a != b,
                "Use distinct positive issue numbers, not IDs or self-links")
        edges.add((a, b))
    require(len({n for edge in edges for n in edge}) <= MAX_ISSUES,
            "Plan exceeds bounded graph scope; inspect manually")
    return repo, sorted(edges)


class GitHub:
    """Fixed github.com transport; never print credentials or retry writes."""

    def __init__(self, repository):
        self.repository = repository

    def request(self, suffix, method="GET", payload=None, paginated=False):
        args = ["gh", "api", "--hostname", "github.com", "--method", method,
                f"repos/{self.repository}/issues/{suffix}",
                "-H", "Accept: application/vnd.github+json"]
        if paginated:
            args += ["--paginate", "--slurp"]
        if payload is not None:
            args += ["--input", "-"]
        try:
            result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                                    text=True, capture_output=True, timeout=60, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise Blocked(f"{method} {suffix}: {type(exc).__name__}; inspect state before retry") from exc
        require(result.returncode == 0,
                f"{method} {suffix} failed (gh exit {result.returncode}); check access/API availability; no fallback")
        try:
            data = json.loads(result.stdout)
        except ValueError as exc:
            raise Blocked(f"{method} {suffix}: invalid JSON; inspect state before retry") from exc
        if paginated:
            require(isinstance(data, list) and all(isinstance(page, list) for page in data),
                    f"GET {suffix}: expected complete array pages")
            return [item for page in data for item in page]
        return data


def issue_number(issue, repository):
    require(isinstance(issue, dict), "Expected an issue object")
    location = issue.get("repository_url")
    require(isinstance(location, str) and location.lower() ==
            f"https://api.github.com/repos/{repository}".lower(),
            "Cross-repository or unknown issue identity: helper cannot verify this graph scope")
    require(positive_int(issue.get("number")) and positive_int(issue.get("id")),
            "Issue response lacks valid number/database ID")
    require("pull_request" not in issue, "Pull requests are not supported dependency nodes")
    return issue["number"]


def issue_set(items, repository):
    require(isinstance(items, list), "Expected an issue array")
    return {issue_number(item, repository) for item in items}


def check_acyclic(graph):
    # Iterative topological elimination avoids recursion limits on long chains.
    degree = {node: 0 for node in graph}
    for targets in graph.values():
        for target in targets:
            require(target in degree, "Incomplete reachable graph")
            degree[target] += 1
    ready = deque(node for node, count in degree.items() if count == 0)
    visited = 0
    while ready:
        node = ready.popleft()
        visited += 1
        for target in graph[node]:
            degree[target] -= 1
            if degree[target] == 0:
                ready.append(target)
    require(visited == len(graph), "Dependency cycle in existing-plus-planned graph; inspect execution progress")


def inspect(repository, edges, api):
    pending = deque(sorted({n for edge in edges for n in edge}))
    graph, ids = {}, {}
    while pending:
        number = pending.popleft()
        if number in graph:
            continue
        require(len(graph) < MAX_ISSUES, "Reachable graph exceeds helper limit; inspect manually")
        issue = api.request(str(number))
        require(issue_number(issue, repository) == number, "Issue lookup identity mismatch")
        ids[number] = issue["id"]
        blockers = issue_set(api.request(f"{number}/dependencies/blocked_by", paginated=True), repository)
        graph[number] = blockers
        pending.extend(sorted(blockers - graph.keys()))
    # Reverse endpoints can expose unsupported scope or permissions too. Inspect
    # them before writing, not only when verifying an already-created edge.
    reverse = {b: issue_set(api.request(f"{b}/dependencies/blocking", paginated=True), repository)
               for b in sorted({b for _, b in edges})}
    for a, b in edges:
        require((b in graph[a]) == (a in reverse[b]),
                f"Existing relationship mismatch for #{a} blocked by #{b}; reconcile before writing")
    additions = [(a, b) for a, b in edges if b not in graph[a]]
    combined = {node: set(targets) for node, targets in graph.items()}
    for a, b in edges:
        combined[a].add(b)
    check_acyclic(combined)
    return additions, ids


def reconcile(plan, api=None, apply=False, emit=lambda event: None):
    repository, edges = parse_plan(plan)
    api = api or GitHub(repository)
    additions, ids = inspect(repository, edges, api)
    for a, b in edges:
        if (a, b) not in additions:
            verify_edge(repository, api, a, b, ids)
    if not apply:
        return {"status": "planned", "repository": repository,
                "additions": [{"blocked": a, "by": b} for a, b in additions],
                "already_present": len(edges) - len(additions)}
    for a, b in additions:
        # Record the attempted operation before sending; a failed response may hide a successful write.
        emit({"status": "attempting", "blocked": a, "by": b})
        api.request(f"{a}/dependencies/blocked_by", method="POST", payload={"issue_id": ids[b]})
        verify_edge(repository, api, a, b, ids)
        emit({"status": "verified", "blocked": a, "by": b})
    # Recheck the whole requested graph, including previously present edges.
    for a, b in edges:
        verify_edge(repository, api, a, b, ids)
    # Detect a concurrent graph change that invalidated the cycle check.
    remaining, _ = inspect(repository, edges, api)
    require(not remaining, "Graph changed during verification; stop dispatch and reconcile")
    return {"status": "verified", "repository": repository,
            "added": len(additions), "edges": len(edges)}


def verify_edge(repository, api, blocked, blocker, ids):
    forward_items = api.request(f"{blocked}/dependencies/blocked_by", paginated=True)
    reverse_items = api.request(f"{blocker}/dependencies/blocking", paginated=True)
    forward = issue_set(forward_items, repository)
    reverse = issue_set(reverse_items, repository)
    require(blocker in forward and blocked in reverse,
            f"Read-back mismatch for #{blocked} blocked by #{blocker}; stop dispatch, preserve partial work")
    for items, number in [(forward_items, blocker), (reverse_items, blocked)]:
        require(all(item["id"] == ids[number] for item in items if item["number"] == number),
                f"Database ID mismatch for #{number}; stop dispatch, preserve partial work")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--apply", action="store_true", help="add only explicitly approved edges; never delete")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text())
        report = reconcile(plan, apply=args.apply,
                           emit=lambda event: print(json.dumps(event), flush=True))
        print(json.dumps(report))
        return 0
    except (Blocked, OSError, ValueError) as exc:
        print(json.dumps({"status": "blocked", "error": str(exc),
                          "next": "inspect actual state before retry; earlier attempted writes may have succeeded"}),
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
