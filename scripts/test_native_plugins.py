#!/usr/bin/env python3
"""Offline packaging checks; no installed clients, network, or inference."""

import base64
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import native_plugins as native


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        self.root.mkdir()
        for group, name in zip(native.GROUPS, ("model", "work", "write")):
            package = self.root / group / name
            (package / "references").mkdir(parents=True)
            (package / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Use for a bounded {name} request.\n---\n"
                "Read [procedure](references/procedure.md).\n")
            (package / "references/procedure.md").write_text("Read [notice](../LICENSE).\n")
            (package / "LICENSE").write_text("Synthetic notice\n")
            script = package / "fixture.sh"
            script.write_text("#!/bin/sh\nexit 0\n")
            script.chmod(0o755)
        (self.root / "LICENSE").write_text("Synthetic collection notice\n")
        for path, contents in zip((native.CLAUDE, native.CODEX), native.manifests(self.root, "2.0.0")):
            native.save(self.root, path, contents)
        for path, contents in zip(native.CATALOGS, native.catalogs("2.0.0")):
            native.save(self.root, path, contents)

    def mutate(self, path, change):
        data = native.load(self.root, path)
        change(data)
        native.save(self.root, path, data)

    def test_whole_collection_and_resource_copy_without_source_history(self):
        destination = self.root.parent / "export"
        native.export(self.root, destination)
        self.assertEqual(native.inventory(destination), native.inventory(self.root))
        self.assertFalse((destination / ".git").exists())
        native.compare_resources(self.root, destination)
        # Source history, docs and tracker are not needed to check a copied bundle.
        moved = self.root.with_name("source-unavailable")
        self.root.rename(moved)
        self.assertEqual(native.check(destination), ("2.0.0", "2.0.0"))

    def test_export_refuses_existing_destination(self):
        with self.assertRaisesRegex(ValueError, "must not exist"):
            native.export(self.root, self.root)

    def test_export_refuses_source_descendant_before_writing(self):
        destination = self.root / "workflow/export"
        with self.assertRaisesRegex(ValueError, "outside the source"):
            native.export(self.root, destination)
        self.assertFalse(destination.exists())

    def test_omitted_and_duplicate_skill_registration(self):
        for change in (lambda m: m["skills"].pop(), lambda m: m["skills"].append(m["skills"][0])):
            with self.subTest(change=change):
                original = native.load(self.root, native.CLAUDE)
                self.mutate(native.CLAUDE, change)
                with self.assertRaisesRegex(ValueError, "Manifest drift"):
                    native.check(self.root)
                native.save(self.root, native.CLAUDE, original)

    def test_new_skill_is_detected_until_inventory_is_regenerated(self):
        package = self.root / "workflow/new-skill"
        package.mkdir()
        (package / "SKILL.md").write_text("---\nname: new-skill\ndescription: Use for new work.\n---\n")
        (package / "LICENSE").write_text("Notice\n")
        with self.assertRaisesRegex(ValueError, "Manifest drift"):
            native.check(self.root)
        native.prepare(self.root, "2.0.0")
        self.assertEqual(len(native.inventory(self.root)), 4)

    def test_missing_linked_resource_and_notice_fail(self):
        for relative in ("workflow/work/references/procedure.md", "writing/write/LICENSE"):
            with self.subTest(relative=relative):
                path = self.root / relative
                content = path.read_bytes()
                path.unlink()
                with self.assertRaisesRegex(ValueError, "Missing resource|Missing package notice"):
                    native.check(self.root)
                path.write_bytes(content)

    def test_package_link_cannot_require_source_repository(self):
        path = self.root / "workflow/work/references/procedure.md"
        path.write_text("Read [source](../../../docs/history.md).\n")
        with self.assertRaisesRegex(ValueError, "Non-package instruction link"):
            native.check(self.root)

    def test_export_resource_omission_corruption_and_modes_fail(self):
        destination = self.root.parent / "export"
        native.export(self.root, destination)
        path = destination / "workflow/work/fixture.sh"
        path.chmod(0o644)
        with self.assertRaisesRegex(ValueError, "mode"):
            native.compare_resources(self.root, destination)
        path.chmod(0o755)
        path.write_text("changed")
        with self.assertRaisesRegex(ValueError, "Changed packaged resource"):
            native.compare_resources(self.root, destination)
        path.unlink()
        with self.assertRaisesRegex(ValueError, "Omitted"):
            native.compare_resources(self.root, destination)

    def test_version_drift_unpinned_and_development_sources_fail(self):
        for path in native.CATALOGS:
            original = native.load(self.root, path)
            changes = (
                lambda c: c["plugins"][0].update(version="2.1.0"),
                lambda c: c["plugins"][0]["source"].update(ref="main"),
                lambda c: c["plugins"][0]["source"].pop("ref"),
                lambda c: c["plugins"][0].update(source="./"),
                lambda c: c["plugins"].append(c["plugins"][0]),
            )
            for change in changes:
                with self.subTest(path=path, change=change):
                    self.mutate(path, change)
                    with self.assertRaises(ValueError):
                        native.check(self.root)
                    native.save(self.root, path, original)
        self.mutate(native.CODEX, lambda m: m.update(version="9.0.0"))
        with self.assertRaisesRegex(ValueError, "Manifest drift"):
            native.check(self.root)

    def test_hook_and_service_effects_fail(self):
        self.mutate(native.CLAUDE, lambda m: m.update(hooks={"SessionStart": []}))
        with self.assertRaisesRegex(ValueError, "Manifest drift"):
            native.check(self.root)
        native.prepare(self.root, "2.0.0")
        for name in ("hooks", ".mcp.json", "skills", "plugin.json"):
            with self.subTest(name=name):
                path = self.root / name
                path.write_text("{}")
                with self.assertRaisesRegex(ValueError, "auto-discovery"):
                    native.check(self.root)
                path.unlink()

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True,
                              capture_output=True, text=True, timeout=10).stdout.strip()

    def test_release_transition_excludes_unpublished_main_and_requires_publication(self):
        self.git("init", "-b", "main")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Fixture")
        self.git("add", ".")
        self.git("commit", "-m", "synthetic release")
        self.git("tag", "v2.0.0")
        release = {"tag_name": "v2.0.0", "draft": False, "prerelease": False, "published_at": "fixture"}

        def request(endpoint):
            if endpoint == "releases/latest":
                return release
            prefix, ref = endpoint.split("?ref=")
            content = self.git("show", f"{ref}:{prefix.removeprefix('contents/')}")
            return {"content": base64.b64encode(content.encode()).decode()}

        native.published("2.0.0", request)
        path = self.root / "workflow/work/SKILL.md"
        path.write_text(path.read_text() + "\nUnpublished change.\n")
        native.prepare(self.root, "2.1.0")
        self.git("add", ".")
        self.git("commit", "-m", "unpublished candidate")
        self.assertEqual(native.check(self.root), ("2.1.0", "2.0.0"))
        native.published(native.selected_version(self.root), request)
        selected_ref = native.load(self.root, native.CATALOGS[0])["plugins"][0]["source"]["ref"]
        self.assertNotIn("Unpublished change", self.git("show", f"{selected_ref}:workflow/work/SKILL.md"))
        before = [(self.root / p).read_bytes() for p in native.CATALOGS]
        with self.assertRaisesRegex(ValueError, "latest published"):
            native.select(self.root, "2.1.0", request)
        self.assertEqual(before, [(self.root / p).read_bytes() for p in native.CATALOGS])
        self.git("tag", "v2.1.0")
        for state in ({"draft": True}, {"prerelease": True}, {"published_at": None}):
            with self.subTest(state=state):
                with self.assertRaises(ValueError):
                    native.select(self.root, "2.1.0", lambda _: {**release, "tag_name": "v2.1.0", **state})
        release["tag_name"] = "v2.1.0"  # Simulate publication, not an actual public release.
        native.select(self.root, "2.1.0", request)
        self.assertEqual(native.check(self.root), ("2.1.0", "2.1.0"))
        self.assertIn("Unpublished change", self.git("show", "v2.1.0:workflow/work/SKILL.md"))

    def test_remote_failure_and_released_manifest_drift_do_not_write(self):
        before = [(self.root / p).read_bytes() for p in native.CATALOGS]
        with self.assertRaises(OSError):
            native.select(self.root, "2.0.0", lambda _: (_ for _ in ()).throw(OSError("offline")))
        def request(endpoint):
            if endpoint == "releases/latest":
                return {"tag_name": "v2.0.0", "published_at": "fixture"}
            return {"content": base64.b64encode(b'{"name":"agentskills","version":"1.0.0"}').decode()}
        with self.assertRaisesRegex(ValueError, "manifest/version mismatch"):
            native.select(self.root, "2.0.0", request)
        self.assertEqual(before, [(self.root / p).read_bytes() for p in native.CATALOGS])

    def test_invalid_versions_rejected(self):
        for invalid in ("main", "2.0.0-rc.1", "02.0.0", "2.0", "../x"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                native.prepare(self.root, invalid)


if __name__ == "__main__":
    unittest.main()
