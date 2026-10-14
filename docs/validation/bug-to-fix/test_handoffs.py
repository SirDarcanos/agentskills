"""Regression tests for the authored trial harness, not agent-adherence tests."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import run_fixture as trial
import run_checks


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / 'run'
        trial.initialize(self.home)

    def test_existing_workspace_is_never_reinitialized(self):
        before = trial.load(self.home / 'state.json')
        with self.assertRaises(FileExistsError): trial.initialize(self.home)
        self.assertEqual(trial.load(self.home / 'state.json'), before)

    def test_investigation_stops_and_denied_fix_has_no_writes(self):
        trial.investigate(self.home)
        root = self.home / 'target'
        self.assertEqual((root / 'pricing.py').read_text(), trial.BUG)
        before = trial.load(self.home / 'commands.json')
        with self.assertRaisesRegex(AssertionError, 'Separate fix authorization'):
            trial.deliver(self.home, False)
        self.assertEqual(trial.load(self.home / 'commands.json'), before)
        self.assertFalse((root / 'test_discount.py').exists())
        self.assertEqual(trial.tracker(self.home).request('1')['labels'], ['bug'])

    def test_same_ticket_composition_preserves_protected_layers(self):
        trial.investigate(self.home)
        ticket_before = (self.home / 'ticket.json').read_bytes()
        trial.deliver(self.home, True)
        state = trial.load(self.home / 'state.json')
        self.assertEqual((state['investigation_runs'], state['analysis_runs']), (1, 0))
        self.assertEqual(trial.protected(self.home / 'target'), state['protected'])
        self.assertEqual((self.home / 'ticket.json').read_bytes(), ticket_before)
        self.assertEqual(state['phase'], 'implemented-unaccepted')
        self.assertEqual(state['repair_cycles'], 0)
        self.assertNotEqual(trial.git(self.home / 'target', 'diff', '--cached', '--', 'pricing.py'), '')
        self.assertNotEqual(trial.git(self.home / 'target', 'diff', '--', 'pricing.py'), '')

    def test_stale_deciding_code_blocks_and_duplicate_preserves_identity(self):
        trial.investigate(self.home)
        trial.branches(self.home)
        branches = trial.load(self.home / 'branches.json')
        self.assertFalse(branches['stale']['fix_shipped'])
        self.assertEqual(branches['stale']['observation']['exit'], 1)
        self.assertEqual(branches['duplicate']['count'], 1)
        self.assertTrue(branches['duplicate']['graph_preserved'])
        self.assertEqual((self.home / 'target/pricing.py').read_text(), trial.BUG)

    def test_direct_change_reuses_check_and_exports_only_synthetic_scope(self):
        trial.investigate(self.home)
        trial.branches(self.home)
        trial.deliver(self.home, True)
        trial.direct(self.home)
        output = Path(self.temp.name) / 'export'
        trial.export(self.home, output)
        self.assertFalse((output / '.git').exists())
        self.assertFalse((output / 'target/protected.txt').exists())
        self.assertEqual(trial.load(output / 'direct.json')['tests_updated'], 0)
        for path in output.rglob('*'):
            if path.is_file():
                self.assertNotIn(str(self.home), path.read_text())
                self.assertNotIn(str(self.home.resolve()), path.read_text())

    def test_collector_scrubs_external_temporary_paths_preserving_failure(self):
        prefixes = {tempfile.gettempdir(), str(Path(tempfile.gettempdir()).resolve())}
        for prefix in prefixes:
            raw = f'File "{prefix}/unrelated-package-123/test_case.py", line 4\nAssertionError: 99.9 != 90\n'
            retained = run_checks.sanitize(raw)
            self.assertNotIn(prefix, retained)
            self.assertIn('<scratch>/test_case.py', retained)
            self.assertIn('AssertionError: 99.9 != 90', retained)
        self.assertNotIn(str(trial.REPO), run_checks.sanitize(str(trial.REPO / 'test.py')))

    def test_hostile_git_routing_cannot_touch_external_repository(self):
        outside = Path(self.temp.name) / 'external'
        outside.mkdir()
        trial.git(outside, 'init', '-q')
        sentinel = outside / 'sentinel'
        sentinel.write_text('protected\n')
        env = dict(GIT_DIR=str(outside / '.git'), GIT_WORK_TREE=str(outside),
                   GIT_INDEX_FILE=str(outside / 'hostile-index'),
                   GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='core.hooksPath',
                   GIT_CONFIG_VALUE_0=str(outside))
        with patch.dict(os.environ, env):
            other = Path(self.temp.name) / 'safe'
            trial.initialize(other)
            self.assertEqual(trial.git(other / 'target', 'branch', '--show-current'), 'fix/fractional-discount')
        self.assertEqual(sentinel.read_text(), 'protected\n')
        self.assertFalse((outside / 'hostile-index').exists())
        self.assertFalse((outside / '.git/index').exists())


if __name__ == '__main__':
    unittest.main()
