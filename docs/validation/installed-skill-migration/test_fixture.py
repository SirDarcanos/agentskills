"""Offline #69 transaction model, NOT an installed-skill migration tool.

No path arguments, network, runtime discovery or installer integration. All
mutation is audited against a freshly owned TemporaryDirectory per test.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import unittest


class Blocked(RuntimeError):
    pass


OWNED = None
WRITES = 0


def contained(path, follow=True):
    p = Path(os.fsdecode(path)).absolute()
    # For unlink/rename/chmod-link, check the parent without following the leaf.
    resolved = p.resolve() if follow else p.parent.resolve() / p.name
    if OWNED is None or not resolved.is_relative_to(OWNED):
        raise Blocked("mutation outside owned temporary root")


def audit(event, args):
    global WRITES
    if OWNED is None:
        return
    if event == "open":
        _, mode, flags = args
        if isinstance(args[0], (str, bytes, os.PathLike)) and (
            (mode and any(c in mode for c in "wax+")) or
            flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        ):
            contained(args[0])
            WRITES += 1
    elif event in ("os.remove", "os.rmdir", "os.mkdir", "os.chmod", "os.utime"):
        # dir_fd paths are disallowed; the fixture uses pathname operations only.
        dir_fd = (args[3] if event == "os.utime" else
                  args[2] if event in ("os.mkdir", "os.chmod") else args[1])
        if dir_fd not in (-1, None):
            raise Blocked("dir_fd mutation unavailable")
        contained(args[0], follow=event not in ("os.remove", "os.rmdir"))
        WRITES += 1
    elif event in ("os.rename", "os.link"):
        if any(fd not in (-1, None) for fd in args[2:]):
            raise Blocked("dir_fd mutation unavailable")
        contained(args[0], follow=False)
        contained(args[1], follow=False)
        WRITES += 1
    elif event == "os.symlink":
        if args[2] not in (-1, None):
            raise Blocked("dir_fd mutation unavailable")
        contained(args[1], follow=False)
        WRITES += 1
    elif event in ("os.setxattr", "os.removexattr"):
        contained(args[0])
        WRITES += 1
    elif event in ("subprocess.Popen", "os.system"):
        raise Blocked("subprocess unavailable in fixture")


sys.addaudithook(audit)


def manifest(root):
    """Full package identity; never follow internal symlinks."""
    result = {}

    def visit(p, name):
        s = p.lstat()
        item = {"mode": stat.S_IMODE(s.st_mode)}
        if p.is_symlink():
            item.update(type="link", target=os.readlink(p))
        elif p.is_dir():
            item["type"] = "directory"
            for child in sorted(p.iterdir()):
                visit(child, name + "/" + child.name)
        elif p.is_file():
            item.update(type="file", sha256=hashlib.sha256(p.read_bytes()).hexdigest())
        else:
            raise Blocked("unsupported entry")
        result[name] = item

    visit(root, ".")
    return result


def copy_package(source, destination):
    contained(source)
    contained(destination)
    # copytree preserves internal links, byte content and modes; no external reads.
    shutil.copytree(source, destination, symlinks=True)


def erase(path):
    contained(path, follow=False)
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        # Avoid shutil's fd-based implementation to keep audit paths inspectable.
        for child in path.iterdir():
            erase(child)
        path.rmdir()


def write_json(path, data):
    temporary = path.with_suffix(".pending")
    with temporary.open("w") as f:
        json.dump(data, f, sort_keys=True)
        f.flush()
        os.fsync(f.fileno())
    temporary.replace(path)


def package(path, marker):
    path.mkdir(parents=True)
    (path / "SKILL.md").write_text(marker)
    (path / "references").mkdir()
    (path / "references" / "guide.md").write_text("local edit " + marker)
    (path / "scripts").mkdir()
    script = path / "scripts" / "check.sh"
    script.write_text("#!/bin/sh\nexit 0\n")
    script.chmod(0o755)
    (path / "assets").mkdir()
    (path / "assets" / "binary").write_bytes(b"\x00\xff\x02")
    (path / ".local").write_text("private fixture addition")
    (path / "empty").mkdir()
    (path / "guide").symlink_to("references/guide.md")


class Transaction:
    """Single synthetic target; reopens the persistent record on resume."""
    def __init__(self, root):
        self.root = root
        self.private = root / "private"
        self.active = root / "runtime-a" / "tdd"
        self.stage = self.private / "stage"
        self.backup = self.private / "backup"
        self.record = self.private / "record.json"
        self.registration = root / "registration.json"
        self.data = json.loads(self.record.read_text()) if self.record.exists() else {}

    def save(self):
        write_json(self.record, self.data)

    def discover(self):
        # Fake two-root catalog, intentionally no precedence to hide duplicates.
        return [p for r in ("runtime-a", "runtime-b")
                for p in (self.root / r).iterdir() if (p / "SKILL.md").is_file()]

    def prepare(self, approved=True):
        if self.data:
            raise Blocked("never replace original backup on resume")
        if not approved:
            raise Blocked("no exact target approval")
        old = manifest(self.active.resolve())
        link = os.readlink(self.active) if self.active.is_symlink() else None
        self.data = {"state": "approved", "old": old, "link": link,
                     "registration": json.loads(self.registration.read_text()),
                     "operations": [], "new": manifest(self.stage)}
        self.save()
        copy_package(self.active.resolve(), self.backup)
        self.verify_backup()
        rehearsal = self.private / "rehearsal"
        copy_package(self.backup, rehearsal)
        if manifest(rehearsal) != old:
            raise Blocked("restore rehearsal mismatch")
        if link is not None:
            (self.private / "rehearsal-link").symlink_to("rehearsal")
            if manifest((self.private / "rehearsal-link").resolve()) != old:
                raise Blocked("link restore rehearsal mismatch")
        self.validate_stage()
        self.data["state"] = "staged/validated"
        self.save()

    def verify_backup(self):
        if not self.backup.exists() or manifest(self.backup) != self.data["old"]:
            raise Blocked("invalid backup")

    def validate_stage(self):
        if manifest(self.stage) != self.data["new"] or not (self.stage / "SKILL.md").is_file():
            raise Blocked("invalid replacement")
        # Synthetic required companion is in another discovery root, not a sibling.
        if not (self.root / "runtime-b" / "companion" / "SKILL.md").is_file():
            raise Blocked("missing companion")

    def effect(self, kind, action, interrupt=None):
        self.data["operations"].append({"kind": kind, "outcome": "intent"})
        self.save()
        if interrupt == "before-" + kind:
            raise InterruptedError(kind)
        action()
        if interrupt == "after-" + kind:
            raise InterruptedError(kind)
        self.data["operations"][-1]["outcome"] = "applied"
        self.save()

    def resume(self):
        self.verify_backup()
        # Reconcile unfinished intents against actual disk state, not phase labels.
        for operation in self.data["operations"]:
            if operation["outcome"] != "intent":
                continue
            kind = operation["kind"]
            exists = self.active.exists() or self.active.is_symlink()
            if kind == "retire":
                if not exists:
                    applied = True
                elif manifest(self.active.resolve()) == self.data["old"]:
                    applied = False
                else:
                    raise Blocked("unknown retirement outcome")
            elif kind == "activate":
                if not exists:
                    applied = False
                elif manifest(self.active) == self.data["new"]:
                    applied = True
                else:
                    raise Blocked("unknown activation outcome")
            else:
                actual = json.loads(self.registration.read_text())
                if actual == {"source": "runtime-a/tdd", "revision": "new"}:
                    applied = True
                elif actual == self.data["registration"]:
                    applied = False
                else:
                    raise Blocked("unknown registration outcome")
            operation["outcome"] = "applied" if applied else "not-applied"
        self.save()

    def applied(self, kind):
        return any(o == {"kind": kind, "outcome": "applied"}
                   for o in self.data["operations"])

    def activate(self, interrupt=None, fail=False):
        self.resume()
        self.validate_stage()
        if not self.applied("retire"):
            if manifest(self.active.resolve()) != self.data["old"]:
                raise Blocked("old copy changed")
            if self.data["link"] != (os.readlink(self.active) if self.active.is_symlink() else None):
                raise Blocked("old link changed")
            self.effect("retire", lambda: erase(self.active), interrupt)
        if not self.applied("activate"):
            if self.active.exists() or self.active.is_symlink():
                raise Blocked("activation destination occupied")
            self.effect("activate", lambda: copy_package(self.stage, self.active), interrupt)
        if not self.applied("register"):
            if json.loads(self.registration.read_text()) != self.data["registration"]:
                raise Blocked("registration changed")
            self.effect("register", lambda: write_json(self.registration, {
                "source": "runtime-a/tdd", "revision": "new"}), interrupt)
        self.data["state"] = "retired/activated"
        self.save()
        if fail:
            self.data["state"] = "rollback-needed"
            self.save()
            raise Blocked("injected refresh failure")
        discovered = [p for p in self.discover() if p.name == "tdd"]
        if discovered != [self.active] or manifest(self.active) != self.data["new"]:
            raise Blocked("competing or incorrect discovery")
        self.data["state"] = "discovery-verified"
        self.save()

    def rollback(self):
        self.resume()
        self.data["state"] = "rollback-needed"
        self.save()
        actual_registration = json.loads(self.registration.read_text())
        if actual_registration not in (self.data["registration"], {
            "source": "runtime-a/tdd", "revision": "new"
        }):
            raise Blocked("registration conflict")
        exists = self.active.exists() or self.active.is_symlink()
        if self.applied("activate") and exists:
            if manifest(self.active) != self.data["new"]:
                raise Blocked("replacement edited; preserve conflict")
            erase(self.active)
            exists = False
        if not exists:
            if self.data["link"] is not None:
                source = Path(self.data["link"])
                if not source.is_absolute():
                    source = self.active.parent / source
                if manifest(source.resolve()) != self.data["old"]:
                    raise Blocked("shared source changed")
                self.active.symlink_to(self.data["link"])
            else:
                copy_package(self.backup, self.active)
        if manifest(self.active.resolve()) != self.data["old"]:
            raise Blocked("old restore mismatch")
        write_json(self.registration, self.data["registration"])
        if [p for p in self.discover() if p.name == "tdd"] != [self.active]:
            raise Blocked("old discovery incomplete")
        self.data["state"] = "restored"
        self.save()


class MigrationTests(unittest.TestCase):
    def setUp(self):
        global OWNED
        self.temp = tempfile.TemporaryDirectory(prefix="skill-migration-fixture-")
        self.root = Path(self.temp.name).resolve()
        OWNED = self.root
        for name in ("runtime-a", "runtime-b", "private"):
            (self.root / name).mkdir()
        (self.root / "private").chmod(0o700)
        package(self.root / "runtime-a" / "tdd", "old")
        package(self.root / "runtime-b" / "companion", "companion")
        package(self.root / "runtime-b" / "unrelated", "unrelated")
        package(self.root / "private" / "stage", "new")
        write_json(self.root / "registration.json", {"source": "runtime-a/tdd", "revision": "old"})
        self.t = Transaction(self.root)
        self.protected = manifest(self.root / "runtime-b")

    def tearDown(self):
        global OWNED
        self.assertEqual(manifest(self.root / "runtime-b"), self.protected)
        erase(self.root)
        OWNED = None
        self.temp.cleanup()

    def shared(self):
        source = self.root / "shared-source"
        self.t.active.rename(source)
        self.t.active.symlink_to("../shared-source")
        (self.root / "other-consumer").symlink_to("shared-source")
        return source

    def test_full_package_restore(self):
        self.t.prepare()
        self.t.activate()
        self.t.rollback()
        self.assertEqual(manifest(self.t.active), self.t.data["old"])
        self.assertEqual(json.loads(self.t.registration.read_text()), self.t.data["registration"])
        self.assertEqual(self.t.data["state"], "restored")
        self.assertTrue(self.t.backup.exists())

    def test_same_name_new_source(self):
        self.t.prepare()
        self.t.activate()
        self.assertEqual((self.t.active / "SKILL.md").read_text(), "new")
        self.assertNotEqual(manifest(self.t.active), self.t.data["old"])
        self.assertEqual(self.t.data["state"], "discovery-verified")
        self.t.verify_backup()

    def test_shared_symlink_retirement_and_restore(self):
        source = self.shared()
        before = manifest(source)
        self.t.prepare()
        self.t.activate()
        self.assertEqual(manifest(source), before)
        self.assertEqual((self.root / "other-consumer").resolve(), source)
        self.t.rollback()
        self.assertEqual(os.readlink(self.t.active), "../shared-source")
        self.assertEqual(manifest(source), before)

    def test_duplicate_discovery_blocks_success(self):
        package(self.root / "runtime-a" / "extra", "extra")
        duplicate = self.root / "runtime-b" / "tdd"
        package(duplicate, "old duplicate")
        self.protected = manifest(self.root / "runtime-b")
        self.t.prepare()
        with self.assertRaisesRegex(Blocked, "competing"):
            self.t.activate()
        with self.assertRaisesRegex(Blocked, "discovery incomplete"):
            self.t.rollback()
        self.assertEqual((duplicate / "SKILL.md").read_text(), "old duplicate")
        self.assertEqual(self.t.data["state"], "rollback-needed")

    def test_invalid_backup_blocks_retirement(self):
        self.t.prepare()
        (self.t.backup / "assets" / "binary").write_bytes(b"corrupt")
        with self.assertRaisesRegex(Blocked, "invalid backup"):
            self.t.activate()
        self.assertEqual(manifest(self.t.active), self.t.data["old"])
        self.assertFalse(self.t.data["operations"])

    def test_invalid_replacement_blocks_retirement(self):
        self.t.prepare()
        (self.t.stage / "references" / "guide.md").unlink()
        with self.assertRaisesRegex(Blocked, "invalid replacement"):
            self.t.activate()
        self.assertEqual(manifest(self.t.active), self.t.data["old"])

    def test_missing_companion_blocks_retirement(self):
        erase(self.root / "runtime-b" / "companion")
        self.protected = manifest(self.root / "runtime-b")
        with self.assertRaisesRegex(Blocked, "missing companion"):
            self.t.prepare()
        self.assertEqual(manifest(self.t.active), self.t.data["old"])

    def test_activation_failure_rolls_back(self):
        self.t.prepare()
        with self.assertRaisesRegex(Blocked, "refresh failure"):
            self.t.activate(fail=True)
        reopened = Transaction(self.root)
        reopened.rollback()
        self.assertEqual(reopened.data["state"], "restored")
        self.assertEqual(manifest(reopened.active), reopened.data["old"])

    def test_resume_all_intent_boundaries(self):
        # Fresh transaction per boundary, disk record is reopened after interruption.
        for boundary in ("before-retire", "after-retire", "before-activate",
                         "after-activate", "before-register", "after-register"):
            with self.subTest(boundary=boundary):
                self.t.prepare()
                backup = manifest(self.t.backup)
                with self.assertRaises(InterruptedError):
                    self.t.activate(interrupt=boundary)
                self.t = Transaction(self.root)
                self.t.activate()
                self.assertEqual(self.t.data["state"], "discovery-verified")
                self.assertEqual(manifest(self.t.backup), backup)
                with self.assertRaisesRegex(Blocked, "never replace"):
                    self.t.prepare()
                self.t.rollback()
                for p in (self.t.backup, self.t.private / "rehearsal",
                          self.t.record):
                    erase(p)
                self.t = Transaction(self.root)

    def test_intervening_edit_blocks_rollback(self):
        self.t.prepare()
        self.t.activate()
        (self.t.active / "SKILL.md").write_text("intervening")
        with self.assertRaisesRegex(Blocked, "replacement edited"):
            self.t.rollback()
        self.assertEqual((self.t.active / "SKILL.md").read_text(), "intervening")
        self.t.verify_backup()

    def test_changed_shared_source_blocks_restore(self):
        source = self.shared()
        self.t.prepare()
        self.t.activate()
        (source / "SKILL.md").write_text("intervening shared edit")
        with self.assertRaisesRegex(Blocked, "shared source changed"):
            self.t.rollback()
        self.assertEqual((source / "SKILL.md").read_text(), "intervening shared edit")
        self.assertEqual(self.t.data["state"], "rollback-needed")

    def test_unknown_interruption_blocks_resume(self):
        self.t.prepare()
        with self.assertRaises(InterruptedError):
            self.t.activate(interrupt="after-retire")
        package(self.t.active, "unexpected installation")
        self.t = Transaction(self.root)
        with self.assertRaisesRegex(Blocked, "unknown retirement"):
            self.t.activate()
        self.assertEqual((self.t.active / "SKILL.md").read_text(), "unexpected installation")

    def test_unapproved_target_untouched(self):
        old = manifest(self.t.active)
        with self.assertRaisesRegex(Blocked, "no exact target approval"):
            self.t.prepare(approved=False)
        self.assertEqual(manifest(self.t.active), old)
        self.assertFalse(self.t.backup.exists())

    def test_write_escape_guard(self):
        # No mutation actually leaves the root, including writes through a link.
        outside = self.root.parent / (self.root.name + "-escape")
        with self.assertRaisesRegex(Blocked, "outside owned"):
            outside.write_text("must not exist")
        self.assertFalse(outside.exists())
        link = self.root / "escape-link"
        link.symlink_to(outside)
        with self.assertRaisesRegex(Blocked, "outside owned"):
            link.write_text("must not exist")
        self.assertFalse(outside.exists())
        link.unlink()  # removing the owned link is permitted, never its target


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(MigrationTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({"tests": result.testsRun, "failures": len(result.failures),
                      "errors": len(result.errors), "audited_mutations": WRITES,
                      "real_installations_changed": False}, sort_keys=True))
    sys.exit(not result.wasSuccessful())
