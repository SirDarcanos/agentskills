"""Source-only caller/isolation checks; no agent execution or host mutations."""
import importlib.util
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "packages", ROOT / "docs/validation/delivery-coverage/check_packages.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def main():
    notice = (ROOT / "LICENSE").read_bytes()
    for name in ("setup-project", "write-tickets", "write-spec", "work-on", "work-on-spec"):
        source = ROOT / "workflow" / name
        checks.check_package(source, name, name == "setup-project", notice)
        with tempfile.TemporaryDirectory(prefix="native-library-") as directory:
            copied = Path(directory) / "unrelated-catalog" / name
            shutil.copytree(source, copied, symlinks=True)
            checks.check_package(copied, name, name == "setup-project", notice)
            assert not (copied / ".git").exists()
            assert (copied / "LICENSE").read_bytes() == (source / "LICENSE").read_bytes()
            if name == "setup-project":
                library = (copied / "references/native-tracker.md").read_text()
                assert "without reading `SKILL.md` or the label audit" in library
                assert "scripts/dependencies.py" in library
    # Actual incoming runtime callers, not just the measured selected path.
    for relative in (
        "write-tickets/SKILL.md", "write-spec/references/publication.md",
        "work-on/SKILL.md", "work-on/references/contracts.md",
        "work-on-spec/SKILL.md", "work-on-spec/references/dispatch.md",
    ):
        text = (ROOT / "workflow" / relative).read_text()
        assert "references/native-tracker.md" in text, relative
        assert "without" in text or "not its setup entry" in text or "not the setup entry" in text
        assert "references/issue-tracker.md" not in text, relative
    assert checks.check_links([ROOT / "docs/agents/issue-tracker.md"], ROOT)
    print("Direct library routes, unchanged notices and isolated package links passed.")
    print("Static inspection only; no agent trial, live API or installed migration.")


if __name__ == "__main__":
    main()
