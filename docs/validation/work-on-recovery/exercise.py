#!/usr/bin/env python3
"""Disposable local facts for a direct recovery walkthrough; not a recovery engine."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def run(root, *args, expected=0):
    result = subprocess.run(args, cwd=root, text=True, capture_output=True)
    assert result.returncode == expected, (args, result.stdout, result.stderr)
    return result.stdout.strip()


def git(root, *args, expected=0):
    return run(root, "git", *args, expected=expected)


def commit(root, message):
    git(root, "add", "core.py")
    git(root, "commit", "--only", "-m", message, "--", "core.py")
    return git(root, "rev-parse", "HEAD")


def protected(root):
    return {
        "index": git(root, "diff", "--cached", "--", "unrelated.txt"),
        "unstaged": git(root, "diff", "--", "unrelated.txt"),
        "bytes": (root / "unrelated.txt").read_bytes().hex(),
        "mode": (root / "unrelated.txt").stat().st_mode,
        "note": (root / "note.txt").read_bytes().hex(),
        "link": os.readlink(root / "note-link"),
        "status": git(root, "status", "--porcelain", "--", "unrelated.txt", "note.txt", "note-link"),
    }


def check(root, value):
    return run(root, "python3", "-B", "-c", "from core import value; assert value() == %s" % value)


with tempfile.TemporaryDirectory(prefix="recovery-fixture-") as tmp:
    root = Path(tmp)
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Synthetic Fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    (root / "core.py").write_text("def value(): return 1\n")
    (root / "unrelated.txt").write_text("original\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "baseline")
    baseline = git(root, "rev-parse", "HEAD")
    check(root, 1)
    old_evidence = {"revision": baseline, "content": hashlib.sha256((root / "core.py").read_bytes()).hexdigest()}
    git(root, "switch", "-c", "source")
    (root / "core.py").write_text("def value(): return 2\n")
    source = commit(root, "delivered change")
    git(root, "switch", "main")
    (root / "unrelated.txt").write_text("staged sentinel\n")
    git(root, "add", "unrelated.txt")
    (root / "unrelated.txt").write_text("unstaged sentinel\n")
    (root / "note.txt").write_text("untracked sentinel\n")
    (root / "note-link").symlink_to("note.txt")
    sentinels = protected(root)
    # Integration happened, but retained progress deliberately still says uncertain.
    retained = {"operation": "merge source", "outcome": "unknown", "checkpoint": "A", "spent": 1}
    git(root, "merge", "--ff-only", "source")
    integrated = git(root, "rev-parse", "HEAD")
    git(root, "merge-base", "--is-ancestor", source, "HEAD")
    assert integrated == source and retained["outcome"] == "unknown"
    # Direct lead disposition: observed applied; do not repeat integration.
    assert old_evidence["revision"] != integrated
    assert old_evidence["content"] != hashlib.sha256((root / "core.py").read_bytes()).hexdigest()
    run(root, "python3", "-B", "-c", "from core import value; assert value() == 1", expected=1)
    check(root, 2)
    assert protected(root) == sentinels
    # Mock lifecycle becomes confirmed stopped; authorized direct owner resumes partial work.
    lifecycle = {"owner": "mock-worker", "state": "stopped", "checkpoint": "A", "spent": 1}
    (root / "core.py").write_text("def value(): return 3\n")
    partial = git(root, "diff", "--", "core.py")
    assert partial and lifecycle["state"] == "stopped"
    lifecycle["spent"] += 1  # corrective direct write spends cycle two, not a fresh episode
    check(root, 3)
    resumed = commit(root, "bounded resumed correction")
    assert protected(root) == sentinels and lifecycle["spent"] == 2
    # Prepare conflicting branches. Both source sides and all sentinels must survive.
    git(root, "switch", "-c", "conflicting-source")
    (root / "core.py").write_text("def value(): return 4\n")
    conflict_source = commit(root, "source side")
    git(root, "switch", "main")
    (root / "core.py").write_text("def value(): return 5\n")
    conflict_target = commit(root, "target side")
    # A separate worktree permits conflict inspection without moving the dirty index.
    conflict = root / "conflict-worktree"
    git(root, "worktree", "add", "-b", "integration-attempt", str(conflict), "HEAD")
    git(conflict, "merge", "--no-edit", "conflicting-source", expected=1)
    unmerged = git(conflict, "ls-files", "-u")
    assert "core.py" in unmerged
    assert git(conflict, "rev-parse", "MERGE_HEAD") == conflict_source
    assert git(conflict, "show", ":2:core.py") == "def value(): return 5"
    assert git(conflict, "show", ":3:core.py") == "def value(): return 4"
    before_blocker = (git(conflict, "status", "--porcelain"), unmerged, (conflict / "core.py").read_bytes())
    # Authored blocker dispositions against synthetic observations; no scheduler/tool invocation.
    observations = {"native_blocker": "A", "A_closed": True, "accepted_integration": False,
                    "required_tool": "unavailable", "owner_state": "unknown", "spent": 2}
    decisions = {"dependent": "waiting", "check": "blocked", "replacement": "blocked",
                 "repair": "reassessment", "conflict": "lead needs bounded resolution approval"}
    assert observations["A_closed"] and not observations["accepted_integration"]
    assert before_blocker == (git(conflict, "status", "--porcelain"), git(conflict, "ls-files", "-u"), (conflict / "core.py").read_bytes())
    assert protected(root) == sentinels
    for branch in ("source", "conflicting-source"):
        git(root, "rev-parse", branch)
    print(json.dumps({"baseline": baseline, "uncertain_applied": integrated,
                      "resumed": resumed, "conflict_source": conflict_source,
                      "conflict_target": conflict_target, "sentinels_preserved": True,
                      "old_check_exit": 1, "fresh_checks_exit": 0,
                      "operation_preserved": "MERGE_HEAD + stages 2/3",
                      "authored_dispositions": decisions}, indent=2))
    # Only this explicitly disposable fixture is removed on context exit, even with conflict.
