"""Disposable #27 direct tool fixture, not a scheduler or agent runner.

Frontier decisions are authored and asserted explicitly. Native observations and
acceptance are synthetic; Git integrations and checks actually execute locally.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SNAPSHOT = Path(__file__).resolve().parents[3] / 'review-delivery/scripts/snapshot.py'
FILES = ['core.py', 'formatting.py', 'consumer.py', 'test_core.py',
         'test_formatting.py', 'test_consumer.py', 'agreement.md']


def run(root, *args, expected=0):
    result = subprocess.run(args, cwd=root, text=True, capture_output=True)
    if result.returncode != expected:
        raise AssertionError((args, expected, result.returncode, result.stdout, result.stderr))
    return result.stdout + result.stderr


def revision(root):
    return run(root, 'git', 'rev-parse', 'HEAD').strip()


def checks(root):
    output = run(root, sys.executable, '-B', '-m', 'unittest', 'discover', '-v')
    assert 'OK' in output
    print(output.strip())
    return {'revision': revision(root), 'command': 'python3 -B -m unittest discover -v',
            'exit': 0, 'sha256': hashlib.sha256(output.encode()).hexdigest()}


def pin(root, record, base):
    output = run(root, sys.executable, '-B', str(SNAPSHOT), 'pin', '--base', base, '--', *FILES)
    record.write_text(output)
    print('Pinned integrated scope:', output.strip())


def change(root, branch, base, replacements, owned):
    run(root, 'git', 'switch', '-qc', branch, base)
    for name, content in replacements.items():
        (root / name).write_text(content)
    changed = set(run(root, 'git', 'diff', '--name-only').splitlines())
    assert changed == set(replacements) and changed <= set(owned)
    print('Inspected direct assignment diff:', branch)
    print(run(root, 'git', 'diff', '--', *owned).strip())
    local = checks(root)  # Dirty state, not evidence for target integration.
    local['dirty_diff_sha256'] = hashlib.sha256(run(root, 'git', 'diff', '--', *owned).encode()).hexdigest()
    run(root, 'git', 'add', '--', *owned)
    run(root, 'git', 'commit', '-qm', branch)
    result = {'source': branch, 'revision': revision(root), 'paths': sorted(changed),
              'local_check': local, 'integrated': False, 'accepted': False}
    run(root, 'git', 'switch', '-q', 'main')
    return result


def integrate(root, result, record, base):
    before = revision(root)
    # Synthetic target explicitly permits serial local merges in this disposable repo.
    print('Return inspected:', json.dumps(result, sort_keys=True))
    run(root, 'git', 'merge', '--no-edit', result['source'])
    after = revision(root)
    assert before != after
    run(root, 'git', 'merge-base', '--is-ancestor', result['revision'], after)
    drift = run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record), expected=1)
    print('Prior integrated evidence stale:', drift.strip())
    pin(root, record, base)
    evidence = checks(root)
    run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record))
    result.update(integrated=True, target_revision=after, integration_check=evidence)
    print('Serial integration:', before, '->', after)


def main():
    print('Python:', sys.version.split()[0])
    # Fixture labels/relationships are observations, never GitHub API claims.
    mapping = {'spec': 'spec', 'work': 'implementation-step', 'ready': 'ready-for-agent'}
    issues = {
        'P': {'title': 'Improve calculations', 'labels': {'spec', 'ready-for-agent'}},
        'A': {'title': 'Double values', 'labels': {'implementation-step', 'ready-for-agent'}},
        'B': {'title': 'Document calculation interface', 'labels': {'implementation-step', 'ready-for-agent'}},
        'C': {'title': 'Consume doubled values', 'labels': {'implementation-step', 'ready-for-agent'}},
        'D': {'title': 'Uppercase display names', 'labels': {'implementation-step', 'ready-for-agent'}},
    }
    native = {'parent': {key: 'P' for key in 'ABCD'},
              'blocked_by': {'A': [], 'B': [], 'C': ['A'], 'D': []}}
    intended = json.loads(json.dumps(native))
    assert native == intended  # Authored complete observation, not graph/API reconciliation coverage.
    original = {key: sorted(item['labels']) for key, item in issues.items()}
    original_graph = json.dumps(native, sort_keys=True)
    candidates = {key for key, item in issues.items() if mapping['work'] in item['labels']}
    assert candidates == set('ABCD') and mapping['spec'] in issues['P']['labels']
    ownership = {'A': {'core.py', 'test_core.py'}, 'B': {'core.py'},
                 'C': {'consumer.py', 'test_consumer.py'},
                 'D': {'formatting.py', 'test_formatting.py'}}
    assert ownership['A'] & ownership['B'] == {'core.py'}
    assert not ownership['A'] & ownership['D']
    # Lead's explicit step-2 decisions: C waits for A; B serializes with A.
    frontier = ['A', 'D']
    assert 'P' not in frontier and 'C' not in frontier and 'B' not in frontier
    print('Initial selected frontier:', frontier, '; B waits for core owner; C waits for A')
    print('Direct execution selected: no delegation authority/capability assumed; active workers 0')
    with tempfile.TemporaryDirectory(prefix='dispatch-fixture-') as directory:
        root = Path(directory) / 'target'
        root.mkdir()
        record = Path(directory) / 'scope.json'
        run(root, 'git', 'init', '-q', '-b', 'main')
        run(root, 'git', 'config', 'user.name', 'Fixture')
        run(root, 'git', 'config', 'user.email', 'fixture@example.invalid')
        print(run(root, 'git', '--version').strip())
        contents = {
            'core.py': 'def calculate(value):\n    return value\n',
            'formatting.py': 'def display(name):\n    return name\n',
            'consumer.py': 'def consume(value):\n    return value\n',
            'test_core.py': 'import unittest\nfrom core import calculate\nclass Core(unittest.TestCase):\n    def test_calculate(self):\n        self.assertEqual(calculate(2), 2)\n',
            'test_formatting.py': 'import unittest\nfrom formatting import display\nclass Display(unittest.TestCase):\n    def test_display(self):\n        self.assertEqual(display("Ada"), "Ada")\n',
            'test_consumer.py': 'import unittest\nfrom consumer import consume\nclass Consumer(unittest.TestCase):\n    def test_consume(self):\n        self.assertEqual(consume(2), 2)\n',
            'agreement.md': 'A double; B document shared core; C consume double plus one; D uppercase.\n',
        }
        for name, content in contents.items():
            (root / name).write_text(content)
        run(root, 'git', 'add', '--', *FILES)
        run(root, 'git', 'commit', '-qm', 'fixture baseline')
        base = revision(root)
        sentinel = root / 'unrelated.txt'
        sentinel.write_text('protected synthetic user work\n')
        protected = sentinel.read_bytes()
        pin(root, record, base)
        checks(root)
        # Prepared disjoint direct results share a base; no concurrent agents run.
        a = change(root, 'work-a', base, {
            'core.py': 'def calculate(value):\n    return value * 2\n',
            'test_core.py': contents['test_core.py'].replace('calculate(2), 2', 'calculate(2), 4'),
        }, ownership['A'])
        a['closed'] = True  # Deliberate premature synthetic tracker closure.
        assert not a['integrated'] and not a['accepted']
        assert 'C' not in frontier
        print('A closed + local pass but not integrated/accepted: C stays waiting')
        d = change(root, 'work-d', base, {
            'formatting.py': 'def display(name):\n    return name.upper()\n',
            'test_formatting.py': contents['test_formatting.py'].replace('"Ada"), "Ada"', '"Ada"), "ADA"'),
        }, ownership['D'])
        integrate(root, d, record, base)
        # Independent progress cannot unlock C; A's branch still exists unintegrated.
        run(root, 'git', 'show-ref', '--verify', 'refs/heads/work-a')
        assert not a['integrated'] and 'C' not in frontier
        integrate(root, a, record, base)
        assert a['integrated'] and not a['accepted']
        print('A integrated/checks current but synthetic required acceptance absent: C still waits')
        a['accepted'] = True  # Explicit mock acceptance, not independent review/user acceptance.
        run(root, 'git', 'merge-base', '--is-ancestor', a['revision'], 'main')
        assert a['integration_check']['exit'] == 0 and a['accepted']
        frontier = ['B', 'C']  # A stopped; shared core ownership is now released.
        print('Accepted integration evidence:', a['target_revision'], '; next frontier:', frontier)
        b = change(root, 'work-b', revision(root), {
            'core.py': 'def calculate(value):\n    """Return twice the input; consumer relies on this interface."""\n    return value * 2\n',
        }, ownership['B'])
        integrate(root, b, record, base)
        c = change(root, 'work-c', revision(root), {
            'consumer.py': 'from core import calculate\ndef consume(value):\n    return calculate(value) + 1\n',
            'test_consumer.py': contents['test_consumer.py'].replace('consume(2), 2', 'consume(2), 5'),
        }, ownership['C'])
        integrate(root, c, record, base)
        # Regression sensitivity: old interface breaks the integrated cross-ticket check.
        core = (root / 'core.py').read_text()
        (root / 'core.py').write_text(contents['core.py'])
        failure = run(root, sys.executable, '-B', '-m', 'unittest', '-v', 'test_consumer', expected=1)
        assert '3 != 5' in failure
        print('Cross-ticket sensitivity: reverting doubled interface fails consumer assertion (exit 1)')
        (root / 'core.py').write_text(core)
        checks(root)
        run(root, sys.executable, '-B', str(SNAPSHOT), 'check', str(record))
        assert sentinel.read_bytes() == protected
        assert run(root, 'git', 'status', '--porcelain').strip() == '?? unrelated.txt'
        for result in [a, b, c, d]:
            run(root, 'git', 'show-ref', '--verify', 'refs/heads/' + result['source'])
            assert result['integrated']
        assert original_graph == json.dumps(native, sort_keys=True)
        assert original == {key: sorted(item['labels']) for key, item in issues.items()}
        print('Retained all source branches and protected sentinel; no graph/label mutations')
        print('Final target:', revision(root), '; evidence current; independent review absent')
        print('Fixture disposition: disposable directory removed by explicit test protocol only')
    print('PASS: synthetic assertions/tools, not autonomous dispatch, live tracker or acceptance')


if __name__ == '__main__':
    main()
