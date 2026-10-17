"""Disposable JSON tracker with native parent/blocker state; no network or policy.

Fixture server conflict checks are synthetic, not a new graph service. Callers own
approval, deduplication, readiness and complete read-back. Python 3.9+.
"""
import json


class FakeTracker:
    repository = "example/project"

    def __init__(self, path):
        self.path = path
        self.calls = []
        self.pages = []
        self.fail = None
        self.wrong_id = None
        self.timeout_after_write = False
        if not path.exists():
            self.save({"issues": [], "parents": {}, "blockers": {}})

    def load(self):
        return json.loads(self.path.read_text())

    def save(self, state):
        self.path.write_text(json.dumps(state, indent=2) + "\n")

    def create(self, title, body, labels):
        state = self.load()
        number = len(state["issues"]) + 1
        issue = {"number": number, "id": 9000 + number, "title": title,
                 "body": body, "labels": labels,
                 "repository_url": "https://api.github.com/repos/" + self.repository}
        state["issues"].append(issue)
        self.save(state)
        if self.timeout_after_write:
            raise RuntimeError("timeout after persisted creation")
        return issue

    def request(self, suffix, method="GET", payload=None, paginated=False):
        self.calls.append((suffix, method, payload, paginated))
        if suffix == self.fail:
            raise RuntimeError("read unavailable")
        state = self.load()
        parts = suffix.split("/")
        number = int(parts[0])
        issues = {i["number"]: i for i in state["issues"]}
        issue = issues[number]
        relation = "/".join(parts[1:])
        parents, blockers = state["parents"], state["blockers"]
        if method == "PATCH" and not relation:
            # Fixture CRUD only: the authored caller supplies the approved delta.
            issue["labels"] = payload["labels"]
            self.save(state)
            if self.timeout_after_write:
                raise RuntimeError("timeout after persisted labels")
            return issue
        if method == "POST":
            field = "sub_issue_id" if relation == "sub_issues" else "issue_id"
            target = next((i["number"] for i in issues.values()
                           if i["id"] == payload[field]), None)
            if target is None:
                raise ValueError("unknown database ID")
            if relation == "sub_issues":
                existing = parents.get(str(target))
                if existing is not None and existing != number:
                    raise ValueError("conflicting parent")
                ancestor = number
                while ancestor is not None:
                    if ancestor == target:
                        raise ValueError("hierarchy cycle")
                    ancestor = parents.get(str(ancestor))
                parents[str(target)] = number
            elif relation == "dependencies/blocked_by":
                edges = blockers.setdefault(str(number), [])
                if target not in edges:
                    edges.append(target)
            else:
                raise ValueError("unsupported write")
            self.save(state)
            if self.timeout_after_write:
                raise RuntimeError("timeout after persisted relationship")
            return issue
        if not relation:
            return issue
        if relation == "parent":
            parent = parents.get(str(number))
            return issues[parent] if parent is not None else None
        if relation == "sub_issues":
            result = [issues[int(n)] for n, p in parents.items() if p == number]
        elif relation == "dependencies/blocked_by":
            result = [issues[n] for n in blockers.get(str(number), [])]
        elif relation == "dependencies/blocking":
            result = [issues[int(n)] for n, bs in blockers.items() if number in bs]
        else:
            raise ValueError("unsupported read")
        # Page size one ensures callers must consume all pages even in tiny graphs.
        pages = [result[i:i + 1] for i in range(len(result))] or [[]]
        if paginated:
            self.pages.extend((suffix, n + 1) for n in range(len(pages)))
            result = [i for page in pages for i in page]
        else:
            result = pages[0]
        if suffix == self.wrong_id:
            result = [dict(i, id=i["id"] + 50000) for i in result]
        return result
