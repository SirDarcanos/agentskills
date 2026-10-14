"""Offline fixture-tool checks; no agents, transports, network or installs."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import run_fixture as fixture


class Harness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='issue72-harness-')
        self.addCleanup(self.tmp.cleanup)
        with contextlib.redirect_stdout(io.StringIO()):
            self.root = fixture.setup(self.tmp.name)

    def test_graph_and_protected_layers(self):
        with contextlib.redirect_stdout(io.StringIO()):
            fixture.inspect(self.root)
        repo = self.root / 'target'
        self.assertEqual(fixture.git(repo, 'show', ':protected.txt'), b'staged unrelated work\n')
        self.assertEqual((repo / 'protected.txt').read_bytes(), b'unstaged unrelated work\n')
        self.assertTrue((repo / 'protected-link').is_symlink())

    def test_scoped_integration_preserves_index_and_dirty_work(self):
        repo = self.root / 'target'
        before = fixture.protected(repo)
        lane = self.root / 'lanes' / 'A'
        (lane / 'render.py').write_text('def render(name):\n    return "Receipt: " + name\n')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(fixture.check(self.root, 'A', False), 0)
            fixture.integrate(self.root, 'A')
            self.assertEqual(fixture.check(self.root, 'A', True), 0)
        self.assertEqual(fixture.protected(repo), before)
        self.assertEqual((repo / 'render.py').read_bytes(), (lane / 'render.py').read_bytes())
        # An already consumed patch is not silently reapplied.
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(Exception):
                fixture.integrate(self.root, 'A')
        self.assertEqual(fixture.protected(repo), before)

    def test_unexpected_worker_path_blocks_integration(self):
        lane = self.root / 'lanes' / 'A'
        (lane / 'render.py').write_text('def render(name):\n    return name\n')
        (lane / 'test_trial.py').write_text('# weakened tests\n')
        head = fixture.git(self.root / 'target', 'rev-parse', 'HEAD')
        with self.assertRaisesRegex(AssertionError, 'Unexpected worker paths'):
            fixture.integrate(self.root, 'A')
        self.assertEqual(fixture.git(self.root / 'target', 'rev-parse', 'HEAD'), head)

    def test_partial_failure_is_retained_as_failure(self):
        (self.root / 'lanes' / 'B' / 'normalize.py').write_text(
            'def normalize(name):\n    return name.strip()\n')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(fixture.check(self.root, 'B', False), 1)
        log = next((self.root / 'evidence').glob('lane-B-*.log')).read_text()
        self.assertIn('test_reject_blank', log)
        self.assertIn('FAILED', log)
        self.assertIn('Exit: 1', log)
        self.assertNotIn(str(self.root), log)
        self.assertNotIn(str(self.root.resolve()), log)


if __name__ == '__main__':
    unittest.main()
