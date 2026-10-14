"""Replay #70's authored local tracker/check operations, not an agent runtime.

Python 3.9+. No network; explicit output directory must not exist. The instruction
walkthrough is recorded separately. Imports existing fixtures/helper, not copies
of their procedures. Assertions verify artifacts and persisted fixture effects.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def run(output):
    output.mkdir(parents=True, exist_ok=False)
    baseline = REPO / "docs/validation/shape-work/reading_list.py"
    protected = baseline.read_bytes(), baseline.stat().st_mode
    source_paths = [baseline, REPO / "setup-project/scripts/dependencies.py",
                    REPO / "docs/validation/write-tickets/tracker_fixture.py"]
    source_paths += [REPO / name / "SKILL.md" for name in (
        "shape-work", "write-spec", "write-tickets", "analyze", "research",
        "domain-modeling", "setup-project", "tdd")]
    source_paths += [HERE / name for name in (
        "input.md", "brief.md", "spec.md", "technical.md", "tickets.json", "run_fixture.py")]
    identities = {str(p.relative_to(REPO)): digest(p) for p in source_paths}
    baseline_run = subprocess.run([sys.executable, "-B", str(baseline)],
                                  capture_output=True, text=True, check=False)
    (output / "baseline.txt").write_text(baseline_run.stdout + baseline_run.stderr)
    assert baseline_run.returncode == 0
    fixture = module("ticket_fixture", REPO / "docs/validation/write-tickets/tracker_fixture.py")
    helper = module("dependencies", REPO / "setup-project/scripts/dependencies.py")
    plan = json.loads((HERE / "tickets.json").read_text())
    assert plan["repository"] == fixture.FakeTracker.repository
    bodies = {"SPEC": (HERE / plan["spec"]["body_file"]).read_text()}
    assert all(cid in bodies["SPEC"] for cid in ("P1", "P2", "P3"))
    assert all(all(cid in t["body"] for cid in ("P1", "P2", "P3")) for t in plan["tickets"])
    events = []
    with tempfile.TemporaryDirectory() as tmp:
        api = fixture.FakeTracker(Path(tmp) / "graph.json")
        assert api.load() == {"issues": [], "parents": {}, "blockers": {}}
        # Exact authored fixture approval: input.md; a credential is never used.
        parent = api.create(plan["spec"]["title"], bodies["SPEC"], plan["spec"]["labels"])
        assert api.request(str(parent["number"])) == parent
        spec_only = api.load()
        assert len(spec_only["issues"]) == 1 and not spec_only["parents"] and not spec_only["blockers"]
        write_json(output / "spec-only.json", spec_only)
        events.append({"phase": "write-spec", "status": "complete", "stop": "one mirror, no tickets/graph"})
        bindings = {"SPEC": parent}
        # Separate subsequent Write Tickets request; no automatic phase advance.
        for ticket in plan["tickets"]:
            bindings[ticket["key"]] = api.create(ticket["title"], ticket["body"], ticket["labels"])
        for key, issue in bindings.items():
            expected = plan["spec"] if key == "SPEC" else next(t for t in plan["tickets"] if t["key"] == key)
            read = api.request(str(issue["number"]))
            assert read["title"] == expected["title"] and read["labels"] == expected["labels"]
            assert read["body"] == (bodies["SPEC"] if key == "SPEC" else expected["body"])
            assert "ready-for-agent" not in read["labels"]
            assert not ({"spec", "implementation-step"} <= set(read["labels"]))
        native = {"repository": plan["repository"], "dependencies": [
            {"blocked": bindings[e["blocked"]]["number"], "by": bindings[e["by"]]["number"]}
            for e in plan["dependencies"]]}
        # Missing edge permission: actual helper inspection only; no writes.
        before = api.path.read_bytes()
        api.calls.clear()
        proposed = helper.reconcile(native, api, apply=False)
        assert proposed["status"] == "planned" and len(proposed["additions"]) == 1
        assert api.path.read_bytes() == before and not any(c[1] == "POST" for c in api.calls)
        events.append({"case": "permission absent", "status": "plan-only", "graph_writes": 0})
        # Missing native read capability: explicit failure, not absent blockers.
        api.fail = f'{bindings["VERIFY"]["number"]}/dependencies/blocked_by'
        try:
            helper.reconcile(native, api, apply=True)
        except RuntimeError as exc:
            events.append({"case": "native capability unavailable", "status": "blocked", "error": str(exc)})
        else:
            raise AssertionError("unavailable endpoint was not blocked")
        assert api.path.read_bytes() == before
        api.fail = None
        # Fresh parent inspection and server conflict protection; empty parentage
        # was observed, no removals/reparenting or prose fallback is authorized.
        for edge in plan["parents"]:
            p, child = bindings[edge["parent"]], bindings[edge["child"]]
            assert api.request(f'{p["number"]}/parent') is None
            assert api.request(f'{child["number"]}/parent') is None
            api.request(f'{p["number"]}/sub_issues', "POST", {"sub_issue_id": child["id"]})
        applied = helper.reconcile(native, api, apply=True, emit=events.append)
        assert applied == {"status": "verified", "repository": plan["repository"], "added": 1, "edges": 1}
        # Reopen disk; inspect both graphs using actual IDs and complete pages.
        reopened = fixture.FakeTracker(api.path)
        children = reopened.request(f'{parent["number"]}/sub_issues', paginated=True)
        assert {i["id"] for i in children} == {bindings[k]["id"] for k in ("PIN", "VERIFY")}
        for key in ("PIN", "VERIFY"):
            assert reopened.request(f'{bindings[key]["number"]}/parent')["id"] == parent["id"]
        pin, verify = bindings["PIN"], bindings["VERIFY"]
        assert reopened.request(f'{verify["number"]}/dependencies/blocked_by', paginated=True) == [pin]
        assert reopened.request(f'{pin["number"]}/dependencies/blocking', paginated=True) == [verify]
        assert (f'{parent["number"]}/sub_issues', 2) in reopened.pages
        before_rerun = api.path.read_bytes()
        rerun = helper.reconcile(native, reopened, apply=True)
        assert rerun["added"] == 0 and api.path.read_bytes() == before_rerun
        assert not any(c[1] == "POST" for c in reopened.calls)
        # Actual duplicate inspection: content+role+identity match; no recreation.
        assert len([i for i in reopened.load()["issues"] if i["title"] == pin["title"]
                    and i["body"] == pin["body"] and i["labels"] == pin["labels"]]) == 1
        write_json(output / "graph.json", reopened.load())
        write_json(output / "readback.json", {"bindings": bindings, "children": children,
                   "blocker_report": applied, "rerun": rerun, "pages": reopened.pages,
                   "requests": api.calls + reopened.calls})
        events.append({"phase": "write-tickets", "status": "verified", "stop": "no scheduling/build"})
        # Controlled deciding-caller change; preserve service/intent evidence.
        old_source = baseline.read_text()
        old = module("old_reading", baseline)
        changed_path = Path(tmp) / "changed_reading.py"
        changed_path.write_text(old_source.replace('"titles": visible_books(books, reader)',
                                                   '"books": visible_books(books, reader)', 1))
        changed = module("changed_reading", changed_path)
        books = [{"reader": "A", "title": "Own"}, {"reader": "B", "title": "Other"}]
        assert old.visible_books(books, "A") == changed.visible_books(books, "A") == ["Own"]
        assert old.reading_page(books, "A") != changed.reading_page(books, "A")
        write_json(output / "freshness.json", {
            "old_source": digest(baseline), "changed_caller_source": digest(changed_path),
            "old_page": old.reading_page(books, "A"), "changed_page": changed.reading_page(books, "A"),
            "service_result_unchanged": ["Own"],
            "disposition": "caller output-shape support stale; reader filter/order and P1–P3 intent retained; old caller compatibility cannot be relied on"})
    assert protected == (baseline.read_bytes(), baseline.stat().st_mode)
    assert identities == {str(p.relative_to(REPO)): digest(p) for p in source_paths}
    write_json(output / "execution.json", {"python": platform.python_version(),
               "platform": platform.system(), "input_revision": subprocess.check_output(
                   ["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip(),
               "identities": identities, "events": events, "baseline_exit": baseline_run.returncode,
               "protected_baseline_bytes_and_mode": "unchanged",
               "limits": "authored fixture operations and direct author walkthrough; no autonomous compliance or live API proof"})
    print("PASS: artifact fidelity, spec stop, plan-only zero writes, unavailable native read blocked, "
          "persisted graph/roles/both directions/pagination, no-op rerun, targeted caller invalidation, protected source")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new evidence directory (never overwritten)")
    run(parser.parse_args().output)
