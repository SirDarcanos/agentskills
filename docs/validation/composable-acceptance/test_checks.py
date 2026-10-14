"""Negative structural checks; these do not model runtime route decisions."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import check_packages as checks


class PackageChecks(unittest.TestCase):
    def test_current_frontmatter_and_folded_description(self):
        fields = checks.metadata('---\nname: test-skill\ndescription: >\n  Use for tests.\n  Stop here.\n---\n# Test\n')
        self.assertEqual(fields['description'], ' Use for tests. Stop here.')
        self.assertEqual(fields['name'], 'test-skill')

    def test_bad_or_duplicate_identity_and_missing_trigger_rejected(self):
        for front in ('name: bad_name\ndescription: test',
                      'name: test\nname: other\ndescription: test',
                      'name: test\ndescription:', 'description: test'):
            with self.subTest(front=front), self.assertRaises(AssertionError):
                checks.metadata('---\n' + front + '\n---\n# Test')

    def test_non_sibling_catalog_and_duplicate_rejection(self):
        with tempfile.TemporaryDirectory() as scratch:
            locations = []
            for index, name in enumerate(('research', 'review-delivery')):
                location = Path(scratch) / str(index) / 'payload'
                location.mkdir(parents=True)
                (location / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: test\n---\n# Test')
                locations.append(location)
            catalog = checks.catalog(locations)
            self.assertEqual(set(catalog), {'research', 'review-delivery'})
            self.assertNotIn('review-delivery', checks.catalog(locations[:1]))
            with self.assertRaises(AssertionError):
                checks.catalog([locations[0], locations[0]])

    def test_missing_link_escaping_link_and_missing_anchor_rejected(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch) / 'payload'
            root.mkdir()
            entry = root / 'SKILL.md'
            (Path(scratch) / 'outside.md').write_text('# Outside')
            (root / 'LICENSE').write_text((checks.REPO / 'LICENSE').read_text())
            for link in ('missing.md', '../outside.md', '#missing'):
                entry.write_text(f'---\nname: test\ndescription: test\n---\n# Test\n[reference]({link})')
                with self.subTest(link=link), self.assertRaises(AssertionError):
                    checks.inspect_package(root)

    def test_missing_or_truncated_notice_rejected(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / 'SKILL.md').write_text('---\nname: test\ndescription: test\n---\n# Test')
            with self.assertRaises(FileNotFoundError):
                checks.inspect_package(root)
            (root / 'LICENSE').write_text('Copyright (c) 2026 Nicola Mustone\n')
            with self.assertRaises(AssertionError):
                checks.inspect_package(root)
            (root / 'LICENSE').write_text((checks.REPO / 'LICENSE').read_text())
            self.assertEqual(checks.inspect_package(root)['name'], 'test')

    def test_package_subprocess_ignores_hostile_git_environment(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            external = root / 'external'
            external.mkdir()
            safe = checks.offline_environment()
            subprocess.run(['git', 'init', '-b', 'main'], cwd=external, env=safe,
                           capture_output=True, check=True, timeout=10)
            (external / 'protected.txt').write_text('protected external bytes\n')
            subprocess.run(['git', 'add', 'protected.txt'], cwd=external, env=safe,
                           capture_output=True, check=True, timeout=10)
            marker = root / 'hook-ran'
            hooks = root / 'hooks'
            hooks.mkdir()
            hook = hooks / 'pre-commit'
            hook.write_text('#!/bin/sh\nprintf hook > "' + str(marker) + '"\n')
            hook.chmod(0o755)
            template = root / 'template'
            (template / 'hooks').mkdir(parents=True)
            shutil.copy2(hook, template / 'hooks/pre-commit')
            config = root / 'hostile.gitconfig'
            config.write_text('[core]\n\thooksPath = ' + str(hooks) + '\n[init]\n\ttemplateDir = ' + str(template) + '\n')
            copied = root / 'fixture'
            shutil.copytree(checks.REPO / 'review-delivery', copied, symlinks=True)
            before = checks.manifest(external)
            hostile = dict(GIT_DIR=str(external / '.git'), GIT_WORK_TREE=str(external),
                           GIT_INDEX_FILE=str(external / '.git/index'),
                           GIT_TEMPLATE_DIR=str(template), GIT_CONFIG_GLOBAL=str(config),
                           GIT_CONFIG_SYSTEM=str(config), GIT_CONFIG_NOSYSTEM='0',
                           GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='core.hooksPath',
                           GIT_CONFIG_VALUE_0=str(hooks))
            with patch.dict(os.environ, hostile):
                result = checks.run_offline([sys.executable, '-B', 'scripts/test_snapshot.py'], copied)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn('Ran 13 tests', result.stderr)
            self.assertEqual(checks.manifest(external), before)
            self.assertFalse(marker.exists(), 'ambient hook executed')

    def test_content_and_modes_change_identity(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            file = root / 'data'
            file.write_text('before')
            first = checks.manifest(root)
            file.write_text('after')
            self.assertNotEqual(first, checks.manifest(root))
            second = checks.manifest(root)
            file.chmod(0o700)
            self.assertNotEqual(second, checks.manifest(root))


if __name__ == '__main__':
    unittest.main()
