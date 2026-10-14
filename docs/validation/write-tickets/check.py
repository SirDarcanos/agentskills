"""Offline links/frontmatter/license/isolation checks; no agent runner."""
import ast
import importlib.util
from pathlib import Path
import shutil
import tempfile

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "package_checks", REPO / "docs/validation/delivery-coverage/check_packages.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def main():
    notice = (REPO / "LICENSE").read_bytes()
    expected = notice.replace(b"Copyright (c) 2026 Nicola Mustone",
                              b"Copyright (c) 2026 Matt Pocock\nCopyright (c) 2026 Nicola Mustone")
    assert (REPO / "write-tickets/LICENSE").read_bytes() == expected
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    for name, command_only in (("write-tickets", False), ("work-on", True)):
        checks.check_package(REPO / name, name, command_only, notice)
        with tempfile.TemporaryDirectory(prefix="tickets-isolation-") as temp:
            isolated = Path(temp) / "catalog" / "non-sibling-package"
            shutil.copytree(REPO / name, isolated, symlinks=True)
            checks.check_package(isolated, name, command_only, notice)
    print("Root/evidence links:", checks.check_links(
        [REPO / "README.md", REPO / "CHANGELOG.md", *HERE.glob("*.md")], REPO))
    adapter = (REPO / "work-on/references/ticketing.md").read_text()
    assert "write-tickets" in adapter and "### Reconciliation algorithm" not in adapter
    assert "## 2. Inspect and propose cohesive tickets" not in adapter
    print("Offline checks passed; no remote, model, installed mutation or agent trial.")


if __name__ == "__main__":
    main()
