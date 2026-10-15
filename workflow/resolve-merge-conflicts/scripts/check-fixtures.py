#!/usr/bin/env python3
"""Scripted Git mechanics checks, not an agent or permission evaluator."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]
# Retain ordinary process settings, never inherited repository/config overrides.
ENV = dict({key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
           GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
           GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
           GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid",
           GIT_EDITOR="true", GIT_SEQUENCE_EDITOR="true", GIT_TERMINAL_PROMPT="0")


class Repo:
    def __init__(self, root):
        self.root = root
        self.git("init", "-b", "main")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", str(root / "no-hooks"))
        self.write("rules.txt", "alpha=base\nbeta=base\n")
        self.write("staged.txt", "original staged\n")
        self.write("unstaged.txt", "original unstaged\n")
        self.git("add", "--", "rules.txt", "staged.txt", "unstaged.txt")
        self.git("commit", "-m", "baseline")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args, expected=0):
        result = subprocess.run(["git", *args], cwd=self.root, env=ENV,
                                text=True, capture_output=True, timeout=15)
        if result.returncode != expected:
            raise AssertionError(f"git {' '.join(args)}: exit {result.returncode}, "
                                 f"expected {expected}\n{result.stdout}{result.stderr}")
        return result.stdout.strip()

    def write(self, path, content):
        (self.root / path).write_text(content)

    def commit_rules(self, content, message):
        self.write("rules.txt", content)
        self.git("add", "--", "rules.txt")
        self.git("commit", "-m", message)

    def merge_conflict(self):
        self.git("switch", "-c", "incoming")
        self.commit_rules("alpha=incoming\nbeta=base\n", "change alpha")
        self.incoming = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        self.commit_rules("alpha=base\nbeta=current\n", "change beta")
        self.current = self.git("rev-parse", "HEAD")
        self.git("merge", "incoming", expected=1)
        assert self.git("ls-files", "-u")

    def active(self, name):
        return (self.root / self.git("rev-parse", "--git-path", name)).exists()

    def resolve(self, content):
        self.write("rules.txt", content)
        self.git("add", "--", "rules.txt")
        assert not self.git("ls-files", "-u")
        self.git("diff", "--cached", "--check")

    def protected(self):
        paths = ["staged.txt", "unstaged.txt", "note.txt", "note-link"]
        manifest = []
        for path in paths:
            item = self.root / path
            manifest.append((path, item.lstat().st_mode,
                             os.readlink(item) if item.is_symlink() else item.read_bytes()))
        return (manifest, self.git("ls-files", "--stage", "--", *paths),
                self.git("status", "--porcelain=v1", "--", *paths))

    def sentinels(self, staged):
        if staged:
            self.write("staged.txt", "unrelated staged\n")
            self.git("add", "--", "staged.txt")
        self.write("unstaged.txt", "unrelated unstaged\n")
        self.write("note.txt", "untracked\n")
        (self.root / "note-link").symlink_to("note.txt")
        return self.protected()


class Fixtures(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="conflict-fixture-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Repo(Path(self.temp.name))

    def test_compatible_merge_completion(self):
        r = self.repo
        r.merge_conflict()
        # Available side blobs retain distinct intended changes.
        self.assertEqual(r.git("show", ":2:rules.txt"), "alpha=base\nbeta=current")
        self.assertEqual(r.git("show", ":3:rules.txt"), "alpha=incoming\nbeta=base")
        protected = r.sentinels(staged=False)
        combined = "alpha=incoming\nbeta=current\n"
        r.resolve(combined)
        self.assertEqual((r.root / "rules.txt").read_text(), combined)
        self.assertEqual(r.git("diff", "--cached", "--name-only"), "rules.txt")
        r.git("merge", "--continue")
        self.assertFalse(r.active("MERGE_HEAD"))
        self.assertEqual(r.git("show", "-s", "--format=%P").split(), [r.current, r.incoming])
        self.assertEqual((r.root / "rules.txt").read_text(), combined)
        self.assertEqual(r.protected(), protected)
        r.git("merge-base", "--is-ancestor", r.base, "HEAD")

    def test_unrelated_staged_work_blocks_completion(self):
        r = self.repo
        r.merge_conflict()
        protected = r.sentinels(staged=True)
        head = r.git("rev-parse", "HEAD")
        r.resolve("alpha=incoming\nbeta=current\n")
        staged = r.git("diff", "--cached", "--name-only").splitlines()
        self.assertEqual(staged, ["rules.txt", "staged.txt"])
        # The driver deliberately pauses: merge --continue would consume both.
        self.assertTrue(r.active("MERGE_HEAD"))
        self.assertEqual(r.git("rev-parse", "HEAD"), head)
        self.assertEqual(r.protected(), protected)

    def test_incompatible_intent_remains_pending(self):
        r = self.repo
        r.git("switch", "-c", "incoming")
        r.commit_rules("access=deny\n", "deny access")
        r.git("switch", "main")
        r.commit_rules("access=allow\n", "allow access")
        r.git("merge", "incoming", expected=1)
        before = (r.git("ls-files", "-u"), (r.root / "rules.txt").read_bytes(),
                  r.git("rev-parse", "HEAD"))
        self.assertIn("access=allow", r.git("show", ":2:rules.txt"))
        self.assertIn("access=deny", r.git("show", ":3:rules.txt"))
        # Requires a product decision; no write, stage, abort or continuation.
        self.assertTrue(r.active("MERGE_HEAD"))
        self.assertEqual(before, (r.git("ls-files", "-u"),
                                 (r.root / "rules.txt").read_bytes(), r.git("rev-parse", "HEAD")))

    def test_failed_check_preserves_resolutions(self):
        r = self.repo
        r.merge_conflict()
        r.resolve("alpha=incoming\nbeta=base\n")  # deliberately lost current intent
        head = r.git("rev-parse", "HEAD")
        result = subprocess.run(
            ["git", "show", ":rules.txt"], cwd=r.root, env=ENV,
            text=True, capture_output=True, check=True, timeout=15)
        check = subprocess.run(
            [os.sys.executable, "-c", "import sys; assert 'beta=current' in sys.stdin.read()"],
            input=result.stdout, text=True, capture_output=True, timeout=15)
        self.assertEqual(check.returncode, 1)
        self.assertIn("AssertionError", check.stderr)
        self.assertTrue(r.active("MERGE_HEAD"))
        self.assertEqual(r.git("rev-parse", "HEAD"), head)
        self.assertIn("alpha=incoming", r.git("show", ":rules.txt"))
        self.assertFalse(r.git("ls-files", "-u"))  # staged does not imply checked

    def test_rebase_dirty_work_blocks_continuation(self):
        r = self.repo
        r.git("switch", "-c", "topic")
        r.commit_rules("alpha=topic\nbeta=base\n", "topic alpha")
        r.git("switch", "main")
        r.commit_rules("alpha=upstream\nbeta=upstream\n", "upstream defaults")
        r.git("switch", "topic")
        r.git("rebase", "main", expected=1)
        protected = r.sentinels(staged=False)
        r.resolve("alpha=topic\nbeta=upstream\n")
        stopped = r.git("rev-parse", "REBASE_HEAD")
        r.git("rebase", "--continue", expected=1)
        self.assertEqual(r.git("rev-parse", "REBASE_HEAD"), stopped)
        self.assertEqual(r.protected(), protected)
        self.assertFalse(r.git("ls-files", "-u"))
        self.assertTrue(r.active("rebase-merge") or r.active("rebase-apply"))

    def test_multi_commit_rebase_continuation(self):
        r = self.repo
        r.git("switch", "-c", "topic")
        r.commit_rules("alpha=topic\nbeta=base\n", "topic alpha")
        r.commit_rules("alpha=topic\nbeta=topic\n", "topic beta")
        r.git("switch", "main")
        r.commit_rules("alpha=upstream\nbeta=upstream\n", "upstream defaults")
        upstream = r.git("rev-parse", "HEAD")
        r.git("switch", "topic")
        r.git("rebase", "main", expected=1)
        # Unlike merge completion, rebase --continue requires no unstaged tracked edits.
        r.write("note.txt", "untracked\n")
        (r.root / "note-link").symlink_to("note.txt")
        protected = r.protected()
        first = r.git("rev-parse", "REBASE_HEAD")
        self.assertEqual(r.git("show", ":2:rules.txt"), "alpha=upstream\nbeta=upstream")
        self.assertEqual(r.git("show", ":3:rules.txt"), "alpha=topic\nbeta=base")
        r.resolve("alpha=topic\nbeta=upstream\n")
        r.git("rebase", "--continue", expected=1)  # second commit stops again
        self.assertNotEqual(r.git("rev-parse", "REBASE_HEAD"), first)
        self.assertTrue(r.git("ls-files", "-u"))
        self.assertEqual(r.protected(), protected)
        r.resolve("alpha=topic\nbeta=topic\n")
        r.git("rebase", "--continue")
        self.assertFalse(r.active("rebase-merge"))
        self.assertFalse(r.active("rebase-apply"))
        self.assertEqual(r.git("branch", "--show-current"), "topic")
        self.assertEqual(r.git("rev-list", "--count", f"{upstream}..HEAD"), "2")
        self.assertEqual(r.git("show", "HEAD:rules.txt"), "alpha=topic\nbeta=topic")
        self.assertEqual(r.protected(), protected)
        r.git("merge-base", "--is-ancestor", upstream, "HEAD")

    def test_isolated_package(self):
        target = Path(self.temp.name) / "copied-package"
        shutil.copytree(PACKAGE, target)
        for doc in target.rglob("*.md"):
            content = doc.read_text()
            self.assertEqual(content.count('```') % 2, 0)
            for link in re.findall(r"\]\(([^)]+)\)", content):
                if "://" not in link:
                    self.assertNotIn("#", link, "add anchor validation when anchors are introduced")
                    self.assertTrue((doc.parent / link).exists(), (doc.name, link))
        skill = (target / "SKILL.md").read_text()
        self.assertTrue(skill.startswith("---\nname: resolve-merge-conflicts\ndescription: "))
        self.assertNotIn("disable-model-invocation", skill)
        self.assertIn("already-authorized integration", skill)
        self.assertIn("Copyright (c) 2026 Matt Pocock", (target / "LICENSE").read_text())
        self.assertIn("Copyright (c) 2026 Nicola Mustone", (target / "LICENSE").read_text())


if __name__ == "__main__":
    print("Scripted Git fixtures; no autonomous agent behavior claimed.", flush=True)
    unittest.main(verbosity=2)
