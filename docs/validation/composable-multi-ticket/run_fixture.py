#!/usr/bin/env python3
"""Local Git fixture tooling for #72; not a scheduler or agent simulator.

setup creates disposable worktrees. inspect/check/integrate are explicit lead
operations; agent execution is separately authorized through trial-workflow.js.
No network, model transport, installation, cleanup, or automatic retries.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def env():
    return {**{k: v for k, v in os.environ.items() if not k.startswith('GIT_')},
            'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
            'GIT_TERMINAL_PROMPT': '0', 'PYTHONDONTWRITEBYTECODE': '1'}


def git(cwd, *args):
    return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null',
                           '-c', 'commit.gpgSign=false', *args], cwd=cwd,
                          env=env(), check=True, capture_output=True).stdout


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def protected(repo):
    return {'bytes': digest((repo / 'protected.txt').read_bytes()),
            'untracked': digest((repo / 'private-note.txt').read_bytes()),
            'link': os.readlink(repo / 'protected-link'),
            'modes': {p: oct((repo / p).lstat().st_mode) for p in
                      ['protected.txt', 'private-note.txt', 'protected-link']},
            'index': digest(git(repo, 'ls-files', '--stage', '-z', '--',
                                'protected.txt', 'protected-link'))}


TESTS = '''import unittest
from render import render
from normalize import normalize
from pipeline import make_receipt

class A(unittest.TestCase):
    def test_render(self):
        self.assertEqual(render("Ada"), "Receipt: Ada")

class B(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(normalize("  Ada  "), "Ada")
    def test_reject_blank(self):
        for value in ("", "   "):
            with self.assertRaises(ValueError):
                normalize(value)
    def test_reject_nonstring(self):
        for value in (None, 7):
            with self.assertRaises(ValueError):
                normalize(value)

class D(unittest.TestCase):
    def test_optional_upper(self):
        self.assertEqual(normalize(" Ada ", upper=True), "ADA")
        self.assertEqual(normalize(" Ada ", upper=False), "Ada")

class C(unittest.TestCase):
    def test_receipt(self):
        self.assertEqual(make_receipt(" Ada "), "Receipt: ADA")
    def test_invalid(self):
        for value in (" ", None):
            with self.assertRaises(ValueError):
                make_receipt(value)
'''

AGREEMENT = '''# Synthetic receipt delivery agreement — revision 1

Local-only trial for #72 / #48 AC2, AC3, AC4, AC10, AC11, AC13, AC15.
Approved by the maintainer in the parent session. This is a disposable local
tracker, not production GitHub issues or a substitute for live API validation.
Graph.json stores roles, parent membership and both dependency directions.

- A: render(name) returns "Receipt: " + name. Own render.py only.
- B: normalize(name) trims strings; blank or non-string input raises ValueError.
  Own normalize.py. First attempt deliberately returns partial after trim only
  and an observed rejection-test failure; no further repair in that assignment.
- D: add keyword-only upper=False to normalize; upper=True uppercases the
  trimmed name, preserving B's rejection/default behavior. Own normalize.py.
  No native prerequisite, but serialized behind B's exclusive interface owner.
- C: make_receipt(name) composes normalize(name, upper=True) and render.
  Own pipeline.py; blocked by accepted integration of B and D.

Tests are supplied acceptance examples; workers may not weaken/edit them.
No new product design/analysis is needed: inspect the supplied technical record
and deciding files and reuse current facts. Refresh only changed inputs.

Policy: root alone integrates scoped patches and commits in this disposable
repository. Local implementation is not acceptance. Required prerequisite
acceptance = inspected integration, relevant passing checks, both independent
review axes and root disposition. No PR/remote/merge requirement inside this
fixture. Repository delivery still targets a real PR on main with no merge.
Root owns shared interface decisions, execution ledger, worker launches and
final integration checkpoint. At most two active non-lead assignments (including
read-only gates/review), no recursive delegation, finite runtime per assignment.
B checkpoint B-reject: maximum two correction cycles; partial cycle one spends
one, resumed cycle two uses the remaining one. No reset on resume or owner switch.
Optional assessment allowance is zero; no calls/reservations/services/substitution.

Protected: staged+unstaged protected.txt, protected-link symlink, untracked
private-note.txt. Preserve bytes, index entries, modes and link target. Workers
must not stage/commit or touch files outside their single module. Temporary
outputs go outside worktrees. No cleanup or installed-source writes.
'''

TECHNICAL = '''# Supplied technical readiness — revision 1

Python stdlib only. Render is independent of normalize's interface. Existing
modules are stubs; acceptance tests already cover all approved behavior.
B/D share the same callable and must serialize even without a native blocker.
C uses both approved interfaces, so integrated cross-ticket tests must rerun.
Choose a compatible method inline (build-and-check is sufficient); report
actual baseline, increments and results. No fresh analyze/research is needed.
Baseline failures are expected missing behavior, not environment failures.
Read the actual modules/tests before trusting this record. On resume B retains
its already implemented trim increment and adds only missing validation.
D changes the callable signature; refresh B/D/C interface-dependent evidence,
not render's settled behavior. Root rechecks graph/ledger before every launch.
'''


def setup(parent=None):
    root = Path(tempfile.mkdtemp(prefix='issue72-', dir=parent))
    repo = root / 'target'
    repo.mkdir()
    (root / 'evidence').mkdir()
    (root / 'lanes').mkdir()
    git(repo, 'init', '--initial-branch=main', '--template=')
    git(repo, 'config', 'user.name', 'Synthetic Trial')
    git(repo, 'config', 'user.email', 'trial@example.invalid')
    files = {'AGENTS.md': AGREEMENT, 'technical.md': TECHNICAL,
             'render.py': 'def render(name):\n    raise NotImplementedError\n',
             'normalize.py': 'def normalize(name):\n    raise NotImplementedError\n',
             'pipeline.py': 'def make_receipt(name):\n    raise NotImplementedError\n',
             'test_trial.py': TESTS, 'protected.txt': 'baseline\n'}
    for name, content in files.items():
        (repo / name).write_text(content)
    (repo / 'protected-link').symlink_to('protected.txt')
    graph = {'P': {'role': 'spec', 'children': ['A', 'B', 'C', 'D'], 'parent': None},
             'A': {'role': 'implementation-step', 'parent': 'P', 'blocked_by': [], 'blocking': []},
             'B': {'role': 'implementation-step', 'parent': 'P', 'blocked_by': [], 'blocking': ['C']},
             'C': {'role': 'implementation-step', 'parent': 'P', 'blocked_by': ['B', 'D'], 'blocking': []},
             'D': {'role': 'implementation-step', 'parent': 'P', 'blocked_by': [], 'blocking': ['C']}}
    save(repo / 'graph.json', graph)
    git(repo, 'add', '.')
    git(repo, 'commit', '-m', 'test: seed synthetic receipt agreement')
    base = git(repo, 'rev-parse', 'HEAD').decode().strip()
    for ticket in ('A', 'B'):
        git(repo, 'worktree', 'add', '-b', 'ticket-' + ticket, str(root / 'lanes' / ticket), base)
    (repo / 'protected.txt').write_text('staged unrelated work\n')
    git(repo, 'add', 'protected.txt')
    (repo / 'protected.txt').write_text('unstaged unrelated work\n')
    (repo / 'private-note.txt').write_text('synthetic protected note\n')
    save(root / 'evidence' / 'initial.json', {'base': base, 'protected': protected(repo),
          'graph_digest': digest((repo / 'graph.json').read_bytes()),
          'technical_digest': digest((repo / 'technical.md').read_bytes()),
          'optional_models': {'limit': 0, 'reserved': 0, 'attempted': 0},
          'checkpoint': {'id': 'B-reject', 'spent': 0, 'limit': 2}})
    print(root)
    return root


def inspect(root):
    repo = root / 'target'
    initial = json.loads((root / 'evidence' / 'initial.json').read_text())
    assert protected(repo) == initial['protected'], 'Protected state changed'
    graph = json.loads((repo / 'graph.json').read_text())
    assert digest((repo / 'graph.json').read_bytes()) == initial['graph_digest']
    for ticket in graph['P']['children']:
        assert graph[ticket]['parent'] == 'P'
        assert graph[ticket]['role'] == 'implementation-step'
        for blocker in graph[ticket]['blocked_by']:
            assert ticket in graph[blocker]['blocking']
        for dependent in graph[ticket]['blocking']:
            assert ticket in graph[dependent]['blocked_by']
    print(git(repo, 'status', '--short').decode(), end='')
    print('Protected bytes/index/modes/link and bidirectional local graph match.')


def check(root, ticket, target):
    cwd = root / ('target' if target else 'lanes/' + ticket)
    result = subprocess.run(['python3', '-B', '-m', 'unittest',
                             'test_trial' if ticket == 'all' else 'test_trial.' + ticket],
                            cwd=cwd, env=env(), capture_output=True, text=True)
    output = result.stdout + result.stderr
    for prefix in sorted({str(root), str(root.resolve())}, key=len, reverse=True):
        output = output.replace(prefix, '<fixture>')
    label = ('target-' if target else 'lane-') + ticket
    count = len(list((root / 'evidence').glob(label + '-*.log')))
    log = root / 'evidence' / f'{label}-{count}.log'
    log.write_text(output + f'\nExit: {result.returncode}\n')
    print(output, end='')
    print('Exit:', result.returncode)
    return result.returncode


def integrate(root, ticket):
    repo = root / 'target'
    lane = root / 'lanes' / ticket
    module = {'A': 'render.py', 'B': 'normalize.py', 'D': 'normalize.py', 'C': 'pipeline.py'}[ticket]
    status = git(lane, 'status', '--porcelain', '-z', '--untracked-files=all').split(b'\0')
    assert [s[3:].decode() for s in status if s] == [module], 'Unexpected worker paths'
    patch = git(lane, 'diff', '--binary', '--', module)
    assert patch, 'Missing worker patch'
    (root / 'evidence' / (ticket + '.patch')).write_bytes(patch)
    before = git(repo, 'rev-parse', 'HEAD').decode().strip()
    inspect(root)
    patchfile = root / 'evidence' / (ticket + '.patch')
    git(repo, 'apply', '--check', '--index', str(patchfile))
    git(repo, 'apply', '--index', str(patchfile))
    git(repo, 'commit', '--only', '-m', 'test: integrate synthetic ticket ' + ticket, '--', module)
    after = git(repo, 'rev-parse', 'HEAD').decode().strip()
    inspect(root)
    save(root / 'evidence' / (ticket + '-integration.json'),
         {'ticket': ticket, 'source_base': git(lane, 'rev-parse', 'HEAD').decode().strip(),
          'before': before, 'after': after, 'paths': [module], 'patch_sha256': digest(patch),
          'content_sha256': digest((repo / module).read_bytes()),
          'source_content_equal': (repo / module).read_bytes() == (lane / module).read_bytes()})
    print('Integrated', ticket, before, '->', after)


def lane(root, ticket):
    assert ticket in ('C', 'D')
    repo = root / 'target'
    git(repo, 'worktree', 'add', '-b', 'ticket-' + ticket, str(root / 'lanes' / ticket), 'HEAD')
    print('Prepared lane', ticket, 'at', git(repo, 'rev-parse', 'HEAD').decode().strip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['setup', 'inspect', 'check', 'integrate', 'lane'])
    parser.add_argument('--root', type=Path)
    parser.add_argument('--ticket', choices=['A', 'B', 'C', 'D', 'all'])
    parser.add_argument('--target', action='store_true')
    args = parser.parse_args()
    if args.action == 'setup':
        setup()
        return 0
    if args.root is None:
        parser.error('--root required')
    if args.action == 'inspect':
        inspect(args.root)
    else:
        if args.ticket is None:
            parser.error('--ticket required')
        if args.action == 'check':
            return check(args.root, args.ticket, args.target)
        if args.action == 'integrate':
            integrate(args.root, args.ticket)
        if args.action == 'lane':
            lane(args.root, args.ticket)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
