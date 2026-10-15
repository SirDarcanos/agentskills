"""Offline evidence checks/replay for #29; this does not execute Work On agents."""

import difflib
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from capture import manifest

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
CHANGES = {"file_types.py", "test_file_types.py", "README.md"}


def check_records():
    baseline = manifest(ROOT / "fixture/baseline")
    delivered = manifest(ROOT / "fixture/delivered")
    records = {name: json.loads((ROOT / f"evidence/{name}.json").read_text())
               for name in ("baseline", "red", "green", "integrated")}
    assert records["baseline"]["before"] == baseline
    assert records["green"]["before"] == delivered
    assert records["integrated"]["before"] == delivered
    for name, record in records.items():
        assert record["before"] == record["after"], name
        assert record["command"] == "python3 -B -m unittest -v"
        assert record["python"] == "3.14.7"
        assert record["exit_code"] == (1 if name == "red" else 0), name
    assert set(baseline) == set(delivered)
    changed = {name for name in baseline if baseline[name] != delivered[name]}
    assert changed == CHANGES, changed
    for name in ("AGENTS.md", "REQUEST.md", "unrelated-note.txt", "note-link"):
        assert baseline[name] == delivered[name], name
    red = dict(baseline)
    red["test_file_types.py"] = delivered["test_file_types.py"]
    assert records["red"]["before"] == red
    assert "AssertionError: False is not true" in records["red"]["output"]
    assert "['plain.md'] != ['B.MD', 'a.mD', 'B.MD', 'plain.md']" in records["red"]["output"]
    return baseline, delivered


def support():
    files = [ROOT / name for name in ("plan.md", "scope.md", "capture.py", "verify.py", "delivered.diff")]
    files += list((ROOT / "evidence").glob("*.json"))
    for package in ("work-on", "review-delivery"):
        files += [p for p in (REPO / 'workflow' / package).rglob("*")
                  if p.is_file() and p.suffix in (".md", ".py")]
    files += [REPO / name for name in (
        "AGENTS.md", "CONTEXT.md", "docs/agents/project.md", "docs/agents/workflow.md",
        "docs/agents/issue-tracker.md", "docs/agents/triage-labels.md",
        "docs/design/delivery-workflow.md", "docs/design/delivery-workflow-inventory.md",
        "docs/design/delivery-workflow-validation.md")]
    return {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(files)}


def snapshot():
    return {"baseline": manifest(ROOT / "fixture/baseline"),
            "delivered": manifest(ROOT / "fixture/delivered"), "support": support()}


def replay():
    with tempfile.TemporaryDirectory(prefix="small-change-replay-") as directory:
        project = Path(directory) / "project"
        for state, expected in (("baseline", 0), ("red", 1), ("delivered", 0)):
            source = "baseline" if state == "red" else state
            if project.exists():
                shutil.rmtree(project)
            shutil.copytree(ROOT / f"fixture/{source}", project, symlinks=True)
            if state == "red":
                shutil.copyfile(ROOT / "fixture/delivered/test_file_types.py",
                                project / "test_file_types.py")
            result = subprocess.run([sys.executable, "-B", "-m", "unittest", "-v"],
                                    cwd=project, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, check=False)
            assert result.returncode == expected, result.stdout
            if state == "red":
                assert "AssertionError: False is not true" in result.stdout
                assert "FAILED (failures=4)" in result.stdout
            print(f"Script replay {state}: check exit {result.returncode} (expected {expected})")


def main():
    check_records()
    pin = ROOT / "scope.json"
    if sys.argv[1:] == ["--pin"]:
        if pin.exists():
            raise ValueError("Refusing to overwrite a pinned review snapshot")
        patches = []
        for name in sorted(CHANGES):
            before = (ROOT / "fixture/baseline" / name).read_text().splitlines(True)
            after = (ROOT / "fixture/delivered" / name).read_text().splitlines(True)
            patches.extend(difflib.unified_diff(before, after,
                           fromfile=f"baseline/{name}", tofile=f"delivered/{name}"))
        (ROOT / "delivered.diff").write_text("".join(patches))
        pin.write_text(json.dumps(snapshot(), indent=2, sort_keys=True) + "\n")
        print("Pinned non-Git manifests and supporting inputs; F4 preserved")
    elif sys.argv[1:] in ([], ["--replay"]):
        assert json.loads(pin.read_text()) == snapshot(), "Stale scope or new input"
        print("Current scope matches pin; path inventory, support and F4 preserved")
        if sys.argv[1:] == ["--replay"]:
            replay()
    else:
        raise ValueError("Usage: verify.py [--pin|--replay]")


if __name__ == "__main__":
    main()
