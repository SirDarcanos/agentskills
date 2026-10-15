"""Disposable #26 tool fixtures, not an agent runner or completion engine."""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SNAPSHOT = Path(__file__).resolve().parents[3] / "workflow/review-delivery/scripts/snapshot.py"
BAD = "def public(record):\n    return dict(record)\n"
GOOD = "def public(record):\n    return {'name': record['name']}\n"
TEST = """import unittest
from service import public
class Projection(unittest.TestCase):
    def test_public_name(self):
        self.assertEqual(public({'name': 'Ada'})['name'], 'Ada')
    def test_private_field(self):
        self.assertNotIn('token', public({'name': 'Ada', 'token': 'synthetic'}))
"""


def run(root, *args, expected=0):
    result = subprocess.run(args, cwd=root, text=True, capture_output=True)
    if result.returncode != expected:
        raise AssertionError((args, expected, result.returncode, result.stdout, result.stderr))
    return result.stdout + result.stderr


def tests(root, expected):
    output = run(root, sys.executable, '-B', '-m', 'unittest', '-v', 'test_service', expected=expected)
    print(output.strip())
    if expected:
        assert "'token' unexpectedly found" in output
    else:
        assert 'OK' in output


def pin(root, record):
    output = run(root, sys.executable, '-B', str(SNAPSHOT), 'pin', '--base',
                 run(root, 'git', 'rev-parse', 'HEAD').strip(), '--',
                 'service.py', 'test_service.py', 'agreement.md')
    record.write_text(output)
    print('Snapshot:', output.strip())


def tracker_fixture():
    # Authored native observations only; no GitHub/network calls.
    parent = {'role': 'spec', 'actionable': False}
    child = {'role': 'step', 'actionable': True}
    edges = {'parent': {'child': 'parent'}, 'blocked_by': {'child': ['predecessor']}}
    before_edges = json.dumps(edges, sort_keys=True)
    labels = {'parent': {'spec', 'enhancement', 'needs-info'},
              'child': {'implementation-step', 'enhancement', 'ready-for-agent'}}
    parent['actionable'] = True  # Synthetic accepted design decision.
    delta = {'add': {'ready-for-agent'}, 'remove': {'needs-info'}}
    before_labels = {key: set(value) for key, value in labels.items()}
    authority = False
    assert not authority
    # Missing authority: record proposal, perform no write.
    assert labels == before_labels
    print('Accepted decision: parent actionable; proposed parent delta',
          {key: sorted(value) for key, value in delta.items()}, '; no mutation authority')
    predecessor = {'closed': True, 'accepted': False, 'integrated': False}
    assert predecessor['closed'] and not (predecessor['accepted'] and predecessor['integrated'])
    print('Closed predecessor without integration: child actionable but execution blocked')
    predecessor.update(accepted=True, integrated=True)
    assert child['actionable'] and predecessor['accepted'] and predecessor['integrated']
    print('Accepted predecessor merge: child eligible under observed graph; parent coordinates')
    # Exact synthetic approval for parent delta only, not graph/child edits.
    authority = True
    if authority:
        labels['parent'].difference_update(delta['remove'])
        labels['parent'].update(delta['add'])
    readback = {key: set(value) for key, value in labels.items()}
    assert readback['parent'] == {'spec', 'enhancement', 'ready-for-agent'}
    assert readback['child'] == before_labels['child']
    assert json.dumps(edges, sort_keys=True) == before_edges
    print('Mock read-back:', {key: sorted(value) for key, value in readback.items()},
          '; unrelated labels/native observations preserved')
    # Rerun sees no missing change.
    assert not (delta['add'] - readback['parent'])
    assert not (delta['remove'] & readback['parent'])


def main():
    print('Python:', sys.version.split()[0])
    with tempfile.TemporaryDirectory(prefix='completion-fixture-') as directory:
        root = Path(directory) / 'target'
        root.mkdir()
        record = Path(directory) / 'scope.json'  # Outside reviewed scope.
        run(root, 'git', 'init', '-q')
        run(root, 'git', 'config', 'user.name', 'Fixture')
        run(root, 'git', 'config', 'user.email', 'fixture@example.invalid')
        (root / 'service.py').write_text(BAD)
        (root / 'test_service.py').write_text(TEST)
        (root / 'agreement.md').write_text('C1 preserve public name; C2 omit private token.\n')
        run(root, 'git', 'add', 'service.py', 'test_service.py', 'agreement.md')
        run(root, 'git', 'commit', '-qm', 'fixture baseline')
        print('Git:', run(root, 'git', '--version').strip())
        checkpoint = {'id': 'projection-acceptance', 'finding': 'privacy-leak', 'spent': 0}
        pin(root, record)
        tests(root, 1)
        print('Material finding unresolved: acceptance blocked; honest blocked report available')
        # Direct corrective work, cycle start recorded before writing.
        checkpoint['spent'] += 1
        (root / 'service.py').write_text(GOOD)
        print(run(root, 'git', 'diff', '--', 'service.py').strip())
        drift = run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record), expected=1)
        print('Old evidence stale:', drift.strip())
        pin(root, record)
        tests(root, 0)
        run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record))
        print('Repair inspected:', checkpoint,
              '; C1/C2 verified; independent review absent, acceptance still blocked')
        old_agreement = hashlib.sha256((root / 'agreement.md').read_bytes()).hexdigest()
        (root / 'agreement.md').write_text('C1 preserve name; C2 omit token; C3 recovery required.\n')
        assert old_agreement != hashlib.sha256((root / 'agreement.md').read_bytes()).hexdigest()
        run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record), expected=1)
        print('Changed agreement detected; passing C1/C2 supplies no C3 evidence')
        # Fresh counterfactual target, not a reset of the repaired checkpoint.
        root = Path(directory) / 'exhaustion'
        root.mkdir()
        (root / 'test_service.py').write_text(TEST)
        (root / 'service.py').write_text(BAD)
        exhausted = {'id': 'exhausted-projection-acceptance', 'finding': 'privacy-leak', 'spent': 0}
        for candidate in [BAD + '# first incomplete correction\n', BAD + '# second incomplete correction\n']:
            assert exhausted['spent'] < 2
            exhausted['spent'] += 1
            (root / 'service.py').write_text(candidate)
            tests(root, 1)
        assert exhausted['spent'] == 2
        preserved = (root / 'service.py').read_bytes()
        renamed = dict(exhausted, id='renamed-checkpoint')
        assert renamed['spent'] == 2  # Renaming cannot replenish the cause's budget.
        print('Exhausted:', exhausted, '; no third repair; recommend design reassessment')
        assert (root / 'service.py').read_bytes() == preserved
    tracker_fixture()
    print('PASS: synthetic assertions only; no independent review, live mutation or agent trial')


if __name__ == '__main__':
    main()
