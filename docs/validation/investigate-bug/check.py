"""Offline package isolation checks; no discovery runner or diagnosis agent."""
import ast
import importlib.util
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "package_checks", ROOT / "docs/validation/delivery-coverage/check_packages.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def main():
    notice = (ROOT / "LICENSE").read_bytes()
    assert (ROOT / "workflow/investigate-bug/LICENSE").read_bytes() == notice
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    package = ROOT / "workflow/investigate-bug"
    checks.check_package(package, "investigate-bug", False, notice)
    # Structural regression guards only: authored fixture traces do not execute
    # the instruction workflow. Inspect the changed entry as well as toy results.
    entry = (package / "SKILL.md").read_text()
    assert "Supported diagnosis can complete in conversation without tracker access" in entry
    assert "`write-tickets` is conditional on an explicitly selected ticket stage" in entry
    assert "diagnosis complete — implementation-ready" in entry
    assert "partial/blocked — investigation-only" in entry
    assert "without requiring a ticket or another user command" in entry
    assert "Findings alone do not satisfy this checkpoint" not in entry
    assert "authorized publication/reconciliation and verified ticket read-back" not in entry
    # The whole shipped maintenance procedure must work without this checkout.
    maintenance = (package / "references/validation.md").read_text()
    assert "docs/validation/" not in maintenance
    assert "Repository-only offline checks" not in maintenance
    with tempfile.TemporaryDirectory(prefix="investigation-isolation-") as temp:
        isolated = Path(temp) / "catalog" / "non-sibling-package"
        shutil.copytree(ROOT / "workflow/investigate-bug", isolated, symlinks=True)
        checks.check_package(isolated, "investigate-bug", False, notice)
    print("Root/evidence links:", checks.check_links(
        [ROOT / "README.md", ROOT / "CHANGELOG.md", *HERE.glob("*.md")], ROOT))
    print("Package/isolated checks passed; companion resolution inspected separately.")


if __name__ == "__main__":
    main()
