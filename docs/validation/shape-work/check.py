"""Offline source/isolated-package checks, not an agent conversation runner.

Run from the repository root with Python 3.9+. Reuses the maintained Markdown
checker; only disposable copies are written. No installed discovery or network.
"""
import hashlib
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[3]
CHECKER = REPO / "docs/validation/delivery-coverage/check_packages.py"
spec = importlib.util.spec_from_file_location("package_checks", CHECKER)
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    notice = (REPO / "LICENSE").read_bytes()
    for name, command_only in (("shape-work", False), ("work-on", False)):
        source = REPO / 'workflow' / name
        checks.check_package(source, name, command_only, notice)
        if name == "shape-work":
            assert (source / "LICENSE").read_bytes() == notice
        with tempfile.TemporaryDirectory(prefix="shape-package-check-") as temp:
            isolated = Path(temp) / "catalog" / "unrelated-location"
            shutil.copytree(source, isolated, symlinks=True)
            checks.check_package(isolated, name, command_only, notice)
    paths = [REPO / "README.md", REPO / "CHANGELOG.md"]
    paths += list(Path(__file__).parent.glob("*.md"))
    print("Root/evidence links:", checks.check_links(paths, REPO))
    fixture = Path(__file__).parent / "reading_list.py"
    before = digest(fixture)
    subprocess.run([sys.executable, "-B", str(fixture)], check=True)
    assert digest(fixture) == before
    print("Settled-case deciding source remains unchanged:", before)
    print("Offline structural checks and baseline tests only; no autonomous routing assertion.")


if __name__ == "__main__":
    main()
