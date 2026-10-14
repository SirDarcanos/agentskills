"""Offline privacy/integrity checks for the narrow artifact exporter."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from export_evidence import export


class Export(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='issue72-export-')
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base / 'fixture'
        self.source = base / 'source'
        self.runtime = base / 'runtime'
        self.outputs = base / 'outputs'
        self.destination = base / 'retained'
        for directory in [self.root / 'evidence', self.root / 'target',
                          self.source, self.runtime, self.outputs]:
            directory.mkdir(parents=True)
        for name in ['AGENTS.md', 'technical.md', 'graph.json', 'test_trial.py',
                     'render.py', 'normalize.py', 'pipeline.py']:
            (self.root / 'target' / name).write_text('synthetic\n')
        (self.outputs / 'result.md').write_text(f'Read {self.source}/work-on/SKILL.md\n')
        (self.runtime / 'events.jsonl').write_text(json.dumps({
            'ts': 1, 'runId': 'r', 'type': 'subagent.child-status',
            'childId': 'A-build', 'status': 'started', 'agent': 'worker',
            'childRunId': 'a', 'workflowKey': 'A-build',
            'asyncDir': str(self.runtime), 'task': 'not retained'}) + '\n')

    def test_sanitizes_paths_preserves_original_and_whitelists_events(self):
        original = self.root / 'evidence' / 'raw.log'
        original.write_text(f'{self.root}/lanes/A\n')
        raw = original.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            export(self.root, self.source, self.runtime, self.outputs, self.destination)
        self.assertEqual(original.read_bytes(), raw)
        self.assertEqual((self.destination / 'evidence/raw.log').read_text(), '<fixture>/lanes/A\n')
        manifest = json.loads((self.destination / 'manifest.json').read_text())
        item = manifest['evidence/raw.log']
        self.assertEqual(item['original_sha256'], hashlib.sha256(raw).hexdigest())
        self.assertTrue(item['path_sanitized'])
        events = json.loads((self.destination / 'lifecycle.json').read_text())
        self.assertNotIn('task', events[0])
        self.assertNotIn('asyncDir', events[0])
        # Publication never silently overwrites an earlier export.
        with self.assertRaises(FileExistsError):
            export(self.root, self.source, self.runtime, self.outputs, self.destination)

    def test_unknown_workstation_path_blocks_export(self):
        (self.root / 'evidence/raw.log').write_text('/Users/unknown/private-material\n')
        with self.assertRaisesRegex(ValueError, 'Unresolved local path'):
            export(self.root, self.source, self.runtime, self.outputs, self.destination)
        self.assertFalse((self.destination / 'evidence/raw.log').exists())


if __name__ == '__main__':
    unittest.main()
