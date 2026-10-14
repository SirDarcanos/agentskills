"""Bounded, authored trial actions; not a runtime workflow/permission engine.

Run each phase separately so the lead can inspect its return before continuing.
Only a newly created disposable workspace is supported. No network or inference.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[3]
BUG = "def total(prices, discount):\n    return sum(prices) - discount\n"
GREEN = "def total(prices, discount):\n    return sum(prices) * (1 - discount)\n"
REFACTOR = "def total(prices, discount):\n    subtotal = sum(prices)\n    return subtotal * (1 - discount)\n"
BASE_TESTS = '''import unittest
from pricing import total
class Existing(unittest.TestCase):
    def test_zero_discount(self): self.assertEqual(total([40, 60], 0), 100)
    def test_empty(self): self.assertEqual(total([], 0), 0)
'''
REGRESSION = '''import unittest
from pricing import total
class Discount(unittest.TestCase):
    def test_fraction(self): self.assertEqual(total([40, 60], .1), 90)
    def test_empty_fraction(self): self.assertEqual(total([], .1), 0)
'''
AGREEMENT = '''# Synthetic pricing agreement
R1: Discount is a fraction of subtotal: [40, 60] at .10 returns 90.
R2: Zero discount returns subtotal; empty prices return zero, including at .10.
D1: Display a total of 90 as "Total: 90.00". This direct change is separate from R1/R2.
Keep the total(prices, discount) signature and caller fraction units.
No currency/rounding semantics, invalid-input contract, tax, persistence or API redesign.
Python arithmetic fixture only; no real customer/payment integration.
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def environment():
    # Never let ambient Git routing/config/hooks touch another repository.
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
               GIT_CONFIG_SYSTEM=os.devnull, PYTHONDONTWRITEBYTECODE='1',
               GIT_AUTHOR_DATE='2026-01-01T00:00:00+0000',
               GIT_COMMITTER_DATE='2026-01-01T00:00:00+0000')
    return env


def run(root, *args):
    if args[0] == 'git':
        args = ('git', '-c', 'core.hooksPath=' + os.devnull,
                '-c', 'init.templateDir=', *args[1:])
    return subprocess.run(args, cwd=root, env=environment(), capture_output=True,
                          text=True, timeout=10)


def git(root, *args):
    result = run(root, 'git', *args)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()


def save(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')


def load(path):
    return json.loads(path.read_text())


def log(home, root, name, args, expected=0, failure=None):
    result = run(root, *args)
    entry = dict(name=name, cwd=root.name,
                 command=['python3' if a == sys.executable else a for a in args],
                 exit=result.returncode,
                 stdout=result.stdout.replace(str(home), '<workspace>'),
                 stderr=result.stderr.replace(str(home.resolve()), '<workspace>').replace(str(home), '<workspace>'),
                 inputs={p.name: digest(p) for p in sorted(root.glob('*.py'))})
    records = load(home / 'commands.json')
    records.append(entry)
    save(home / 'commands.json', records)  # preserve failures before asserting
    assert result.returncode == expected, entry
    if failure:
        assert failure in result.stdout + result.stderr, entry
    return entry


def protected(root):
    return dict(content=digest(root / 'protected.txt'),
                mode=(root / 'protected.txt').stat().st_mode & 0o777,
                index=git(root, 'ls-files', '--stage', '--', 'protected.txt'),
                staged=git(root, 'show', ':protected.txt'),
                link=os.readlink(root / 'protected-link'))


def tracker(home):
    spec = importlib.util.spec_from_file_location(
        'trial_tracker', REPO / 'docs/validation/write-tickets/tracker_fixture.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.FakeTracker(home / 'tracker.json')


def initialize(home):
    home.mkdir()  # refuse existing paths, including symlinks; never overwrite
    save(home / 'commands.json', [])
    root = home / 'target'
    root.mkdir()
    for name, body in {'pricing.py': BUG, 'caller.py': 'from pricing import total\nresult = total([40, 60], .10)\n',
                       'test_existing.py': BASE_TESTS, 'AGREEMENT.md': AGREEMENT,
                       'protected.txt': 'baseline unrelated work\n'}.items():
        (root / name).write_text(body)
    git(root, 'init', '-q', '-b', 'main')
    git(root, 'config', 'user.name', 'Synthetic Fixture')
    git(root, 'config', 'user.email', 'fixture@example.invalid')
    git(root, 'add', '.')
    git(root, 'commit', '-qm', 'synthetic baseline')
    base = git(root, 'rev-parse', 'HEAD')
    git(root, 'switch', '-qc', 'fix/fractional-discount')
    (root / 'protected.txt').write_text('staged unrelated work\n')
    git(root, 'add', 'protected.txt')
    (root / 'protected.txt').write_text('unstaged unrelated work\n')
    (root / 'protected.txt').chmod(0o640)
    (root / 'protected-link').symlink_to('protected.txt')
    log(home, root, 'baseline controls', [sys.executable, '-B', '-m', 'unittest', 'test_existing', '-v'])
    save(home / 'state.json', dict(base=base, protected=protected(root), phase='initialized',
         environment='Python ' + sys.version.split()[0],
         agreement=digest(root / 'AGREEMENT.md'), investigation_runs=0,
         analysis_runs=0, fix_authority=False))


def investigate(home):
    state = load(home / 'state.json')
    assert state['phase'] == 'initialized'
    root = home / 'target'
    source = digest(root / 'pricing.py')
    api = tracker(home)
    assert api.load()['issues'] == []  # complete local duplicate search
    (root / 'reproduction.py').write_text('from pricing import total\nactual = total([40, 60], .10)\nprint(actual)\nassert actual == 90, (actual, 90)\n')
    red = log(home, root, 'investigation reproduction', [sys.executable, '-B', 'reproduction.py'], 1, '99.9, 90')
    observation = log(home, root, 'bounded cause controls', [sys.executable, '-B', '-c',
        'from pricing import total; print([total([40,60], d) for d in (0,.1,.2)])'])
    assert observation['stdout'].strip() == '[100, 99.9, 99.8]'
    assert 'return sum(prices) - discount' in (root / 'pricing.py').read_text()
    evidence = dict(kind='implementation-ready', agreement='AGREEMENT.md R1/R2',
        agreement_digest=state['agreement'], expected=90, actual=99.9,
        impact='Synthetic customer would be overcharged 9.90 on subtotal 100',
        environment=state['environment'], reproduction='python3 -B reproduction.py',
        attempts=1, control_observations=[100, 99.9, 99.8], red=red,
        cause='pricing.py:2 subtracts the raw fraction, not subtotal times fraction',
        rejected_hypothesis='Caller supplies .10 as agreed; not amount 10 or wrong subtotal',
        inputs={p: digest(root / p) for p in ('pricing.py', 'caller.py', 'test_existing.py', 'AGREEMENT.md', 'reproduction.py')},
        fix_scope=['pricing.py', 'test_discount.py'], dependencies=[],
        constraints='Keep signature and fractional caller units',
        exclusions='No rounding, invalid-input, tax, persistence or API redesign',
        risks='Preserve zero-discount and empty-cart controls; empty fractional cart must return zero',
        acceptance={'R1': '100 at .10 returns 90', 'R2': 'Zero discount preserves subtotal and empty prices return zero'},
        regression='Retain existing controls; add fraction and empty-fraction checks',
        method='characterize existing controls then tdd for R1/R2',
        uncertainty='Synthetic arithmetic, not production payment/rounding evidence',
        protected='protected.txt index/worktree/mode and protected-link target',
        artifacts='Reproduction retained; no production probes or repair',
        authority='Local JSON ticket only under #71 fixture scope; no remote issue writes or fix in investigation')
    issue = api.create('Fractional discount overcharges synthetic cart', json.dumps(evidence, sort_keys=True), ['bug'])
    readback = tracker(home).request(str(issue['number']))
    assert readback == issue and json.loads(readback['body']) == evidence
    assert api.load()['parents'] == {} and api.load()['blockers'] == {}
    save(home / 'ticket.json', readback)
    assert digest(root / 'pricing.py') == source and protected(root) == state['protected']
    state.update(phase='ticket-ready', investigation_runs=1)
    save(home / 'state.json', state)
    save(home / 'investigation-stop.json', dict(product_sha256=source, product_unchanged=True,
         fix_shipped=False, publication='local JSON read-back only', ticket=issue['number']))


def deliver(home, authorized):
    state = load(home / 'state.json')
    assert authorized, 'Separate fix authorization required (fixture input, not real consent detection)'
    assert state['phase'] == 'ticket-ready'
    root = home / 'target'
    evidence = json.loads(load(home / 'ticket.json')['body'])
    current = {p: digest(root / p) for p in evidence['inputs']}
    assert current == evidence['inputs'], 'Stale deciding inputs; targeted reassessment required'
    assert protected(root) == state['protected']
    # No investigation/Analyze invocation: inspect/reuse the exact persisted cause.
    log(home, root, 'characterize intended controls', [sys.executable, '-B', '-m', 'unittest', 'test_existing', '-v'])
    original = (root / 'pricing.py').read_bytes()
    sensitivity = home / 'sensitivity'
    sensitivity.mkdir()
    (sensitivity / 'pricing.py').write_text(BUG.replace('sum(prices)', 'sum(prices) + 1'))
    (sensitivity / 'test_existing.py').write_text(BASE_TESTS)
    log(home, sensitivity, 'characterization sensitivity (isolated)',
        [sys.executable, '-B', '-m', 'unittest', 'test_existing', '-v'], 1, '101 != 100')
    assert (root / 'pricing.py').read_bytes() == original
    (root / 'test_discount.py').write_text(REGRESSION)
    log(home, root, 'TDD meaningful red', [sys.executable, '-B', '-m', 'unittest', 'discover', '-v'], 1, '99.9 != 90')
    (root / 'pricing.py').write_text(GREEN)
    log(home, root, 'TDD minimal green', [sys.executable, '-B', '-m', 'unittest', 'discover', '-v'])
    git(root, 'add', 'pricing.py')  # retained staged green, unstaged refactor
    (root / 'pricing.py').write_text(REFACTOR)
    log(home, root, 'TDD refactor green', [sys.executable, '-B', '-m', 'unittest', 'discover', '-v'])
    log(home, root, 'integrated reproduction passes', [sys.executable, '-B', 'reproduction.py'])
    assert protected(root) == state['protected']
    state.update(phase='implemented-unaccepted', fix_authority=True,
                 methods=['characterize', 'tdd'], repair_cycles=0)
    save(home / 'state.json', state)


def direct(home):
    root = home / 'direct'
    root.mkdir()  # non-Git before/after manifest; existing test is reused unchanged
    (root / 'display.py').write_text('def display(value):\n    return "Total: " + str(value)\n')
    test = 'from display import display\nassert display(90) == "Total: 90.00"\n'
    (root / 'check.py').write_text(test)
    before = {p.name: digest(p) for p in root.iterdir()}
    log(home, root, 'direct baseline', [sys.executable, '-B', 'check.py'], 1, 'AssertionError')
    (root / 'display.py').write_text('def display(value):\n    return f"Total: {value:.2f}"\n')
    log(home, root, 'build-and-check immediate increment', [sys.executable, '-B', 'check.py'])
    assert (root / 'check.py').read_text() == test
    save(home / 'direct.json', dict(method='build-and-check', acceptance='D1',
         before=before, after={p.name: digest(p) for p in root.iterdir()},
         tests_added=0, tests_removed=0, tests_updated=0,
         limitations='Presentation only, not a currency rounding contract or delivery acceptance'))


def branches(home):
    # Separate disposable deciding-code variant, not a change to the ready ticket.
    variant = home / 'stale'
    initialize(variant)
    investigate(variant)
    root = variant / 'target'
    old = json.loads(load(variant / 'ticket.json')['body'])
    (root / 'pricing.py').write_text(BUG.replace('sum(prices)', 'sum(prices) + 1'))
    changed = digest(root / 'pricing.py')
    before_checks = len(load(variant / 'commands.json'))
    try:
        deliver(variant, True)
    except AssertionError as error:
        assert 'Stale deciding inputs' in str(error)
    else:
        raise AssertionError('Stale delivery was not stopped')
    assert len(load(variant / 'commands.json')) == before_checks
    targeted = log(variant, root, 'targeted changed deciding-code observation',
                   [sys.executable, '-B', 'reproduction.py'], 1, '100.9, 90')
    assert digest(root / 'pricing.py') == changed  # no speculative repair
    assert digest(root / 'AGREEMENT.md') == old['agreement_digest']
    api = tracker(home)
    canonical = api.request('1')
    body = json.loads(canonical['body'])
    matches = [i for i in api.load()['issues']
               if json.loads(i['body'])['inputs'] == body['inputs']
               and json.loads(i['body'])['cause'] == body['cause']]
    assert [i['id'] for i in matches] == [canonical['id']]
    previous_graph = (api.load()['parents'], api.load()['blockers'])
    data = api.load()
    body['reconciliation'] = 'Duplicate fixture report maps to retained old-state evidence; delivered code is separately reviewed'
    data['issues'][0]['body'] = json.dumps(body, sort_keys=True)
    api.save(data)  # exact local body-only reconciliation, no new ticket/labels
    readback = tracker(home).request('1')
    assert json.loads(readback['body']) == body and readback['labels'] == canonical['labels']
    assert len(api.load()['issues']) == 1
    assert (api.load()['parents'], api.load()['blockers']) == previous_graph
    save(home / 'branches.json', dict(
        stale=dict(old_inputs=old['inputs'], changed_pricing=changed,
                   observation=targeted, unchanged_agreement=old['agreement_digest'],
                   stale=['reproduction', 'cause completeness', 'fix applicability'],
                   next_action='Targeted cause reassessment; retain old-state cause and contract',
                   fix_shipped=False, analysis_rerun=False),
        duplicate=dict(canonical=readback['number'], count=1, readback=readback,
                       labels_preserved=True, graph_preserved=True,
                       limitation='Matches retained pre-fix inputs, not a new current reproduction claim')))


def export(home, destination):
    # Export only named synthetic evidence, never .git, absolute roots or private files.
    destination.mkdir(parents=True, exist_ok=True)
    for name in ('commands.json', 'state.json', 'ticket.json', 'investigation-stop.json', 'direct.json', 'branches.json', 'tracker.json'):
        (destination / name).write_bytes((home / name).read_bytes())
    for relative in ('target/pricing.py', 'target/caller.py', 'target/test_existing.py',
                     'target/test_discount.py', 'target/reproduction.py', 'target/AGREEMENT.md',
                     'direct/display.py', 'direct/check.py'):
        output = destination / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes((home / relative).read_bytes())
    root = home / 'target'
    (destination / 'staged.patch').write_text(git(root, 'diff', '--cached', '--', 'pricing.py') + '\n')
    (destination / 'unstaged.patch').write_text(git(root, 'diff', '--', 'pricing.py') + '\n')
    (destination / 'status.txt').write_text(git(root, 'status', '--short', '--untracked-files=all') + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['init', 'investigate', 'deliver', 'direct', 'branches', 'export'])
    parser.add_argument('workspace', type=Path)
    parser.add_argument('--authorize-fix', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    home = args.workspace.absolute()
    if args.phase == 'init': initialize(home)
    elif args.phase == 'investigate': investigate(home)
    elif args.phase == 'deliver': deliver(home, args.authorize_fix)
    elif args.phase == 'direct': direct(home)
    elif args.phase == 'branches': branches(home)
    else:
        if args.output is None: parser.error('export requires --output')
        export(home, args.output)
    print(args.phase + ': completed (authored fixture action; lead must inspect return)')


if __name__ == '__main__':
    main()
