"""Create a retained synthetic target for the separately authorized reviewer trial.

Uses the offline test fixture; does not launch agents or change the caller's repo.
The caller owns retention/cleanup of the printed temporary directory.
"""
import hashlib
import json
from pathlib import Path
import runpy
import shutil
import subprocess
import tempfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    package = Path(__file__).resolve().parents[1]
    tests = runpy.run_path(str(package / "scripts/test_snapshot.py"))
    fixture = tests["SnapshotTests"]()
    fixture.setUp()
    trial = Path(tempfile.mkdtemp(prefix="review-delivery-trial-"))
    target = trial / "target"
    try:
        shutil.copytree(fixture.root, target, symlinks=True)
        base = fixture.base
        paths = fixture.paths + ["AGENTS.md", "brief.md"]
    finally:
        fixture.doCleanups()
    (target / "AGENTS.md").write_text(
        "# Synthetic target instructions\n\n"
        "S1: formatter.py is the sole owner of heading normalization. Consumers "
        "must reuse its heading function rather than implement normalization.\n"
        "S2: Preserve unrelated staged, unstaged and untracked work.\n"
        "Review is read-only; no delegation, writes, shell or network by reviewers.\n"
        "No changelog, release, domain or ADR policy applies to this fixture.\n"
    )
    (target / "brief.md").write_text(
        "# Approved synthetic brief\n\n"
        "F1: heading(text) trims outer whitespace while preserving the case and "
        "words of string input. Internal whitespace normalization is excluded.\n"
        "F2: Keep one owner for heading behavior and preserve unrelated work.\n"
        "Non-string input, publication, deployment and release are excluded.\n"
        "Review the delivered change, including relevant uncommitted files.\n"
    )
    procedure = trial / "procedure"
    (procedure / "references").mkdir(parents=True)
    # Maintenance validation/test expectations stay outside the review packet;
    # SKILL.md's conditional validation pointer is not part of a review run.
    procedure_paths = ["SKILL.md", "references/handoff.md", "references/scope.md",
                       "references/report.md"]
    for name in procedure_paths:
        shutil.copyfile(package / name, procedure / name)
    evidence = trial / "evidence"
    evidence.mkdir()
    capture = runpy.run_path(str(package / "scripts/snapshot.py"))["capture"]
    state = capture(target, base, paths)
    (evidence / "scope-before.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    commands = {
        "committed.patch": ["diff", "--no-ext-diff", "--no-textconv", "--binary", base,
                            "HEAD", "--", *paths],
        "staged.patch": ["diff", "--no-ext-diff", "--no-textconv", "--binary", "--cached",
                         "HEAD", "--", *paths],
        "unstaged.patch": ["diff", "--no-ext-diff", "--no-textconv", "--binary", "--", *paths],
        "status-before.bin": ["status", "--porcelain=v1", "-z", "--untracked-files=all"],
        "index-before.bin": ["ls-files", "--stage", "-z"],
        "history-before.txt": ["rev-list", "HEAD"],
    }
    for name, args in commands.items():
        data = subprocess.check_output(["git", "--literal-pathspecs", "-c",
                                        "core.fsmonitor=false", "-C", str(target), *args])
        (evidence / name).write_bytes(data)
    protected = {name: sha((target / name).read_bytes())
                 for name in ["protected.txt", "private-note.txt"]}
    procedure_hashes = {name: sha((procedure / name).read_bytes())
                        for name in procedure_paths}
    metadata = {"trial": str(trial), "target": str(target), "base": base,
                "head": state["head"], "paths": paths, "protected": protected,
                "procedure_sha256": procedure_hashes}
    (trial / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True))
    print(json.dumps(metadata, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
