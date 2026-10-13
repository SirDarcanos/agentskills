"""Offline Git fixture checks; no agent/reviewer execution or network."""
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).with_name("snapshot.py").resolve()
CAPTURE = runpy.run_path(str(HELPER))["capture"]


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "target"
        self.root.mkdir()
        self.git("init", "-b", "main")
        self.write("formatter.py", "def heading(text):\n    return text.strip()\n")
        self.write("committed.txt", "baseline\n")
        self.write("staged.txt", "baseline\n")
        self.write("deleted.txt", "baseline\n")
        self.write("old name.txt", "rename baseline\n")
        self.write("protected.txt", "unrelated baseline\n")
        self.git("add", ".")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "-m", "baseline")
        self.base = self.git("rev-parse", "HEAD").decode().strip()
        self.write("committed.txt", "delivered commit\n")
        self.git("add", "committed.txt")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "-m", "delivered")
        self.write("staged.txt", "staged delivery\n")
        self.git("add", "staged.txt")
        self.write("staged.txt", "unstaged over staged\n")
        # Known Spec defect exists only in dirty work.
        self.write("formatter.py", "def heading(text):\n    return text.upper().strip()\n")
        # Known Standards defect: duplicate ownership of heading normalization.
        self.write("duplicate.py", "def heading(text):\n    return text.strip()\n")
        (self.root / "deleted.txt").unlink()
        (self.root / "old name.txt").rename(self.root / "new name.txt")
        (self.root / "note-link").symlink_to("duplicate.py")
        self.write("protected.txt", "unrelated staged\n")
        self.git("add", "protected.txt")
        self.write("protected.txt", "unrelated unstaged\n")
        self.write("private-note.txt", "unrelated untracked\n")
        self.paths = ["formatter.py", "committed.txt", "staged.txt", "duplicate.py",
                      "deleted.txt", "old name.txt", "new name.txt", "note-link"]

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args],
                                       stderr=subprocess.PIPE)

    def write(self, name, content):
        (self.root / name).write_text(content)

    def snapshot(self):
        return CAPTURE(self.root, self.base, self.paths)

    def cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(HELPER), *args],
                              cwd=self.root, capture_output=True, text=True)

    def test_layers_scope_and_known_dirty_findings(self):
        state = self.snapshot()
        self.assertEqual(set(state["files"]), set(self.paths))
        self.assertEqual(state["files"]["deleted.txt"], {"kind": "absent"})
        self.assertEqual(state["files"]["old name.txt"], {"kind": "absent"})
        self.assertEqual(state["files"]["note-link"]["kind"], "symlink")
        self.assertEqual(len({state[k] for k in ["committed_sha256", "staged_sha256",
                                               "unstaged_sha256"]}), 3)
        # Execute the defect rather than claiming a reviewer detected it.
        heading = runpy.run_path(str(self.root / "formatter.py"))["heading"]
        self.assertNotEqual(heading("Hello world"), "Hello world")
        self.assertIn("def heading", (self.root / "duplicate.py").read_text())
        self.assertNotIn("private-note.txt", state["files"])

    def test_cli_and_protected_work_unchanged(self):
        before_status = self.git("status", "--porcelain=v1", "-z", "--untracked-files=all")
        before_index = self.git("ls-files", "--stage", "-z")
        before_history = self.git("rev-list", "HEAD")
        before_bytes = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
        result = self.cli("pin", "--base", self.base, "--", *self.paths)
        self.assertEqual(result.returncode, 0, result.stderr)
        record = Path(self.temp.name) / "scope.json"
        record.write_text(result.stdout)
        result = self.cli("check", str(record))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before_status, self.git("status", "--porcelain=v1", "-z",
                                                "--untracked-files=all"))
        self.assertEqual(before_index, self.git("ls-files", "--stage", "-z"))
        self.assertEqual(before_history, self.git("rev-list", "HEAD"))
        self.assertEqual(before_bytes, {p.name: p.read_bytes() for p in self.root.iterdir()
                                       if p.is_file()})
        self.write("duplicate.py", "changed after review\n")
        result = self.cli("check", str(record))
        self.assertEqual(result.returncode, 1)
        self.assertIn("files", json.loads(result.stdout)["changed_fields"])

    def test_index_change_even_with_identical_worktree(self):
        before = self.snapshot()
        self.git("add", "staged.txt")
        after = self.snapshot()
        self.assertEqual(before["files"], after["files"])
        self.assertNotEqual(before["index_sha256"], after["index_sha256"])

    def test_content_identical_commit_is_not_automatically_fresh(self):
        before = self.snapshot()
        self.git("add", "formatter.py")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "-m", "commit dirty file")
        after = self.snapshot()
        self.assertEqual(before["files"], after["files"])
        self.assertNotEqual(before["head"], after["head"])

    def test_mode_symlink_and_deletion_drift(self):
        before = self.snapshot()
        (self.root / "duplicate.py").chmod(0o755)
        self.assertNotEqual(before["files"], self.snapshot()["files"])
        (self.root / "note-link").unlink()
        (self.root / "note-link").symlink_to("missing-target")
        self.assertNotEqual(before["files"]["note-link"],
                            self.snapshot()["files"]["note-link"])
        (self.root / "duplicate.py").unlink()
        self.assertEqual(self.snapshot()["files"]["duplicate.py"], {"kind": "absent"})

    def test_support_input_and_unusual_names(self):
        name = "support\n[policy].txt"
        self.write(name, "binding policy\n")
        self.paths.append(name)
        before = self.snapshot()
        self.write(name, "changed policy\n")
        self.assertNotEqual(before["files"][name], self.snapshot()["files"][name])

    def test_outside_scope_is_protected_but_requires_rediscovery(self):
        before = self.snapshot()
        self.write("new-relevant.py", "new candidate\n")
        self.assertEqual(before, self.snapshot())
        self.assertIn(b"new-relevant.py", self.git("status", "--porcelain=v1", "-z",
                                                  "--untracked-files=all"))
        self.paths.append("new-relevant.py")
        self.assertNotEqual(before, self.snapshot())

    def test_invalid_paths_directories_and_symlinked_parents(self):
        for name in ["../outside", "/absolute", ".", ".git/config", "./formatter.py"]:
            with self.subTest(name=name), self.assertRaises(ValueError):
                CAPTURE(self.root, self.base, [name])
        (self.root / "directory").mkdir()
        with self.assertRaises(ValueError):
            CAPTURE(self.root, self.base, ["directory"])
        (self.root / "parent-link").symlink_to(self.temp.name)
        with self.assertRaises(ValueError):
            CAPTURE(self.root, self.base, ["parent-link/secret"])

    def test_dirty_only_scope_does_not_require_committed_diff(self):
        state = CAPTURE(self.root, self.git("rev-parse", "HEAD").decode().strip(),
                        ["formatter.py", "duplicate.py"])
        import hashlib
        self.assertEqual(state["committed_sha256"], hashlib.sha256(b"").hexdigest())
        self.assertEqual(set(state["files"]), {"formatter.py", "duplicate.py"})

    def test_submodule_and_unmerged_index_require_manual_capture(self):
        self.git("update-index", "--add", "--cacheinfo", "160000", self.base, "module")
        with self.assertRaises(ValueError):
            CAPTURE(self.root, self.base, ["module"])
        blob = self.git("rev-parse", "HEAD:formatter.py").decode().strip()
        entries = "0 " + "0" * 40 + "\tformatter.py\n"
        entries += "100644 " + blob + " 1\tformatter.py\n"
        subprocess.run(["git", "-C", str(self.root), "update-index", "--index-info"],
                       input=entries.encode(), check=True, capture_output=True)
        with self.assertRaises(ValueError):
            CAPTURE(self.root, self.base, ["formatter.py"])

    def test_invalid_base_and_snapshot_fail_closed(self):
        self.assertEqual(self.cli("pin", "--base", "missing", "formatter.py").returncode, 2)
        record = Path(self.temp.name) / "invalid.json"
        for data in ["{}", "[]", "not-json", '{"format": 1, "paths": null}',
                     '{"format": 1, "root": 3, "base": [], "paths": [false]}']:
            record.write_text(data)
            with self.subTest(data=data):
                self.assertEqual(self.cli("check", str(record)).returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
