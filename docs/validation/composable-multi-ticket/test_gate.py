"""Exercise the actual workflow source with offline runs stubs, never agents."""
import json
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).parent
RUNNER = r'''
const fs = require('node:fs');
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const source = fs.readFileSync(input.source, 'utf8');
const calls = [];
const approval = 'ROOT_APPROVED_NEXT_STAGE';
const runs = {
  all: async items => items.map(item => {
    calls.push({key: item.key, output: item.output, task: item.task});
    return {key: item.key, ok: true, output: approval};
  }),
  run: async (key, item) => {
    calls.push({key, output: item.output, task: item.task});
    return key === 'failure-recovery-gate' ? input.result
         : {key, ok: true, output: approval};
  }
};
(async () => {
  try {
    await new AsyncFunction('args', 'runs', source)(
      {root: '<fixture>', source: '<source>', model: '<mock>'}, runs);
    console.log(JSON.stringify({completed: true, calls}));
  } catch (error) {
    console.log(JSON.stringify({completed: false, error: error.message, calls}));
  }
})();
'''


def run(source, result):
    completed = subprocess.run(['node', '-e', RUNNER], input=json.dumps(
        {'source': str(source), 'result': result}), text=True, capture_output=True,
        check=True, timeout=20)
    return json.loads(completed.stdout)


class ApprovalGate(unittest.TestCase):
    def test_current_workflow_package_sources_exist(self):
        observed = run(ROOT / 'trial-workflow.js',
                       {'ok': True, 'output': 'ROOT_APPROVED_NEXT_STAGE'})
        self.assertTrue(observed['completed'])
        paths = {path for call in observed['calls']
                 for path in re.findall(r'<source>/([^\s]+\.md)', call['task'])}
        self.assertEqual(paths, {
            'workflow/work-on/SKILL.md',
            'workflow/work-on/references/recovery.md',
            'workflow/build-and-check/SKILL.md',
            'workflow/implementation-preflight/SKILL.md',
            'workflow/review-delivery/SKILL.md',
        })
        for relative in paths:
            self.assertTrue((ROOT.resolve().parents[2] / relative).is_file(), relative)

    def test_denials_fail_closed_before_next_writer(self):
        cases = [
            {'ok': True, 'output': 'BLOCKED: parent did not send ROOT_APPROVED_NEXT_STAGE'},
            {'ok': True, 'output': '"ROOT_APPROVED_NEXT_STAGE"'},
            {'ok': True, 'output': 'not ROOT_APPROVED_NEXT_STAGE'},
            {'ok': True, 'output': 'ROOT_APPROVED_NEXT_STAGE but denied'},
            {'ok': False, 'output': 'ROOT_APPROVED_NEXT_STAGE'},
            {'ok': 1, 'output': 'ROOT_APPROVED_NEXT_STAGE'},
            {'ok': True, 'output': None},
            {'ok': True},
        ]
        for result in cases:
            with self.subTest(result=result):
                observed = run(ROOT / 'trial-workflow.js', result)
                self.assertFalse(observed['completed'])
                self.assertEqual([c['key'] for c in observed['calls']],
                                 ['A-build', 'B-partial', 'failure-recovery-gate'])
        # Sensitivity: the retained executed source did accept the denied token.
        original = run(ROOT / 'source-history/trial-workflow.executed.txt', cases[0])
        self.assertTrue(original['completed'])
        self.assertIn('B-resume', [c['key'] for c in original['calls']])

    def test_exact_approval_proceeds_without_output_binding_suffix(self):
        for output in ['ROOT_APPROVED_NEXT_STAGE', ' \nROOT_APPROVED_NEXT_STAGE\n']:
            with self.subTest(output=output):
                observed = run(ROOT / 'trial-workflow.js', {'ok': True, 'output': output})
                self.assertTrue(observed['completed'])
                self.assertIn('C-build', [c['key'] for c in observed['calls']])
                self.assertIn('final-spec', [c['key'] for c in observed['calls']])
                for call in observed['calls']:
                    if call['key'].endswith('-gate'):
                        self.assertIs(call['output'], False)


if __name__ == '__main__':
    unittest.main()
