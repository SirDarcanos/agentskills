"""Offline package/link and tracker-fixture mechanics checks, Python 3.9+.

No agent runner: decisions in these checks are authored by the lead. Fixture
persistence does not prove instruction-following or live GitHub behavior.
"""
import ast
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "package_checks", REPO / "docs/validation/delivery-coverage/check_packages.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def main():
    notice = (REPO / "LICENSE").read_bytes()
    assert (REPO / "write-spec/LICENSE").read_bytes() == notice
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    for name, command_only in (("write-spec", False), ("work-on", True), ("shape-work", False)):
        checks.check_package(REPO / name, name, command_only, notice)
        with tempfile.TemporaryDirectory(prefix="spec-isolation-") as temp:
            isolated = Path(temp) / "catalog" / "not-a-sibling"
            shutil.copytree(REPO / name, isolated, symlinks=True)
            checks.check_package(isolated, name, command_only, notice)
    print("Root/evidence links:", checks.check_links(
        [REPO / "README.md", REPO / "CHANGELOG.md", *HERE.glob("*.md")], REPO))
    with tempfile.TemporaryDirectory(prefix="spec-tracker-") as temp:
        store = Path(temp) / "tracker.json"

        def operation(*args, ok=True):
            run = subprocess.run([sys.executable, "-B", str(HERE / "tracker_fixture.py"),
                                  str(store), *args], text=True, capture_output=True)
            assert (run.returncode == 0) == ok, run.stderr
            return json.loads(run.stdout) if run.returncode == 0 else run.stderr.strip()

        assert operation("list") == []
        issue = operation("create", "--title", "Proposal: Export the filtered reading list",
                          "--body", str(HERE / "spec.md"), "--labels", "product-agreement", "feature")
        actual = operation("read", "--number", "1")
        assert actual == issue and actual["body"] == (HERE / "spec.md").read_text()
        assert actual["labels"] == ["product-agreement", "feature"]
        print("Authorized approved-but-design-unready publication/read-back: issue 1, revision 1")
        matches = operation("list")
        assert len(matches) == 1 and matches[0]["number"] == 1
        # Caller reuses existing identity; fixture does not deduplicate automatically.
        before = store.read_bytes()
        assert operation("read", "--number", "1") == actual
        assert store.read_bytes() == before
        print("Existing identity reused without mutation: one spec, zero tickets/relationships")
        timeout = operation("update", "--number", "1", "--body", str(HERE / "spec.md"),
                            "--timeout-after-write", ok=False)
        assert "timeout" in timeout
        actual = operation("read", "--number", "1")
        assert actual["revision"] == 2 and len(operation("list")) == 1
        assert actual["relationships"] == [] and actual["labels"] == issue["labels"]
        print("Timeout inspected before retry: persisted revision 2, no second create")
        assert "unavailable" in operation("read", "--number", "1", "--fail-read", ok=False)
        assert store.read_bytes() != before  # Only the earlier update changed revision.
        print("Unavailable read reported as failure, not verified publication")
    print("Offline checks passed; no model, installed mutation, public fixture or agent trial.")


if __name__ == "__main__":
    main()
