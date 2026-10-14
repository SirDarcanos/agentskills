#!/usr/bin/env python3
"""Read-only replay of retained #72 evidence, not a new agent execution."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).parent / 'executed'


def read(name):
    return json.loads((ROOT / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Evidence(unittest.TestCase):
    def test_retained_integrity(self):
        manifest = read('manifest.json')
        self.assertTrue(manifest)
        for name, item in manifest.items():
            self.assertEqual(sha(ROOT / name), item['retained_sha256'], name)

    def test_capacity_lifecycle_and_no_early_dependent(self):
        active = set()
        started = {}
        settled = {}
        peak = 0
        for event in read('lifecycle.json'):
            if event['type'] == 'subagent.child-status':
                key = event['workflowKey']
                self.assertNotIn(key, started)
                active.add(key)
                started[key] = event
                peak = max(peak, len(active))
                self.assertLessEqual(len(active), 2)
            else:
                key = event['childKey']
                self.assertIn(key, active)
                self.assertEqual(event['outcome'], 'completed')
                active.remove(key)
                settled[key] = event
        self.assertEqual(active, set())
        self.assertEqual(peak, 2)
        audit = read('tool-audit.json')
        self.assertEqual({item['key'] for item in audit}, set(started))
        for item in audit:
            for tool in item['tool_counts']:
                self.assertFalse(tool in {'subagent', 'bg_delegate', 'bg_run', 'fusion_reason'}
                                 or tool.startswith('ask-') or tool.startswith('ask_'), tool)
        self.assertEqual({k for k in started if k.endswith('-build') or k in ('B-partial', 'B-resume')},
                         {'A-build', 'B-partial', 'B-resume', 'D-build', 'C-build'})
        self.assertNotIn('P', started)
        for earlier, later in [('B-partial', 'B-resume'), ('B-resume', 'D-build'),
                               ('dependent-dispatch-gate', 'C-build'),
                               ('interim-standards', 'C-build'), ('interim-spec', 'C-build'),
                               ('aggregate-review-gate', 'final-standards'),
                               ('aggregate-review-gate', 'final-spec')]:
            self.assertLessEqual(settled[earlier]['ts'], started[later]['ts'])
        for key, event in started.items():
            self.assertLessEqual(settled[key]['ts'] - event['ts'], 600000, key)

    def test_serial_integration_and_refreshed_snapshots(self):
        initial = read('evidence/initial.json')
        prior = initial['base']
        for ticket in ('A', 'B', 'D', 'C'):
            item = read('evidence/' + ticket + '-integration.json')
            self.assertEqual(item['before'], prior)
            self.assertTrue(item['source_content_equal'])
            self.assertEqual(sha(ROOT / ('evidence/' + ticket + '.patch')), item['patch_sha256'])
            prior = item['after']
        interim = read('evidence/interim-scope.json')
        final = read('evidence/final-scope.json')
        self.assertEqual(final['head'], prior)
        self.assertNotEqual(interim['head'], final['head'])
        for name, item in final['files'].items():
            self.assertEqual(sha(ROOT / 'target' / name), item['sha256'])
        self.assertEqual(interim['files']['render.py'], final['files']['render.py'])
        self.assertEqual(interim['files']['normalize.py'], final['files']['normalize.py'])
        self.assertNotEqual(interim['files']['pipeline.py'], final['files']['pipeline.py'])
        self.assertIn('Ran 7 tests', (ROOT / 'evidence/final-checks.log').read_text())
        self.assertIn('OK', (ROOT / 'evidence/final-checks.log').read_text())
        self.assertIn('Exit: 0', (ROOT / 'evidence/final-checks.log').read_text())

    def test_partial_state_lineage_protection_and_zero_budget(self):
        failure = read('evidence/B-failure-scope.json')
        self.assertEqual(sha(ROOT / 'evidence/B-partial.py'), failure['files']['normalize.py']['sha256'])
        raw = (ROOT / 'evidence/B-final.log').read_text()
        self.assertIn('ValueError not raised', raw)
        self.assertIn('FAILED', raw)
        initial = read('evidence/initial.json')
        final = read('evidence/final-state.json')
        self.assertEqual(initial['protected'], final['protected'])
        self.assertEqual(initial['optional_models'], final['optional_models'])
        self.assertEqual(final['optional_models'], {'limit': 0, 'reserved': 0, 'attempted': 0})
        self.assertEqual(final['checkpoint'], {'id': 'B-reject', 'spent': 2, 'limit': 2})
        self.assertEqual(final['final_checkpoint'], {'id': 'final-integration', 'spent': 1, 'limit': 2})
        self.assertTrue(final['source_packages_unchanged'])
        self.assertTrue(final['graph_unchanged'])
        self.assertTrue(final['analysis_reused'])
        self.assertEqual(final['active_workers'], 0)
        graph = read('target/graph.json')
        self.assertEqual(graph['C']['blocked_by'], ['B', 'D'])
        for child in graph['P']['children']:
            self.assertEqual(graph[child]['parent'], 'P')
            for blocker in graph[child]['blocked_by']:
                self.assertIn(child, graph[blocker]['blocking'])
        for phase in ('interim', 'final'):
            for axis in ('standards', 'spec'):
                self.assertTrue((ROOT / 'reports' / f'{phase}-{axis}.md').is_file())


if __name__ == '__main__':
    unittest.main()
