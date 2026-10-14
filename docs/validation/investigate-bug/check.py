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
    assert (ROOT / "investigate-bug/LICENSE").read_bytes() == notice
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    checks.check_package(ROOT / "investigate-bug", "investigate-bug", False, notice)
    with tempfile.TemporaryDirectory(prefix="investigation-isolation-") as temp:
        isolated = Path(temp) / "catalog" / "non-sibling-package"
        shutil.copytree(ROOT / "investigate-bug", isolated, symlinks=True)
        checks.check_package(isolated, "investigate-bug", False, notice)
    print("Root/evidence links:", checks.check_links(
        [ROOT / "README.md", ROOT / "CHANGELOG.md", *HERE.glob("*.md")], ROOT))
    print("Package/isolated checks passed; companion resolution inspected separately.")


if __name__ == "__main__":
    main()
