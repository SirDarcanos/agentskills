#!/usr/bin/env python3
"""Capture a manually driven fixture; no scheduling or agent launch logic."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OWNED = ['AGENTS.md', 'REQUEST.md', 'README.md', 'tracker.json',
         'names.py', 'test_names.py', 'report.py', 'test_report.py']
PROTECTED = ['sentinel.txt', 'untracked-note.txt', 'note-link']


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def run(root, args, expected=0):
    result = subprocess.run(args, cwd=root, capture_output=True, text=True)
    def sanitize(text):
        for name in sorted({str(root), str(root.resolve())}, key=len, reverse=True):
            text = text.replace(name, '<synthetic-target>')
        return text

    recorded_args = ['python3', *args[1:]] if args[0] == sys.executable else args
    record = {'command': recorded_args, 'exit': result.returncode,
              'stdout': sanitize(result.stdout), 'stderr': sanitize(result.stderr)}
    history = HERE / 'evidence' / 'commands.jsonl'
    history.parent.mkdir(exist_ok=True)
    with history.open('a') as stream:
        stream.write(json.dumps(record, sort_keys=True) + '\n')
    if result.returncode != expected:
        raise RuntimeError('unexpected exit: ' + repr(record))
    return result.stdout.strip()


def helper():
    source = REPO / 'review-delivery' / 'scripts' / 'snapshot.py'
    spec = importlib.util.spec_from_file_location('snapshot', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def manifest(root):
    result = {}
    for path in sorted(root.iterdir()):
        if path.name == '.git':
            continue
        info = path.lstat()
        entry = {'mode': stat.S_IMODE(info.st_mode)}
        if path.is_symlink():
            entry.update(kind='symlink', target=os.readlink(path))
        elif path.is_file():
            entry.update(kind='file', sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        else:
            raise RuntimeError('unexpected fixture member: ' + path.name)
        result[path.name] = entry
    return result


def state(root, base, paths):
    captured = helper().capture(root, base, paths)
    captured['root'] = '<synthetic-target>'
    return captured


def protection(root):
    # Committed base->HEAD is deliberately excluded: only owned commits change HEAD.
    data = state(root, run(root, ['git', 'rev-parse', 'HEAD']), PROTECTED)
    for key in ['base', 'head', 'branch', 'committed_sha256', 'root']:
        data.pop(key)
    return data


def tracker_read(method, endpoint):
    observations = json.loads((HERE / 'fixture' / 'baseline' / 'tracker.json').read_text())
    if method != 'GET':
        raise PermissionError('mock tracker is read-only')
    if endpoint not in observations:
        raise KeyError('unplanned endpoint')
    return observations[endpoint]


def initialize():
    root = Path(tempfile.mkdtemp(prefix='work-on-multi-'))
    seed = HERE / 'fixture' / 'baseline'
    for path in seed.iterdir():
        shutil.copy2(path, root / path.name)
    run(root, ['git', 'init', '-b', 'main'])
    run(root, ['git', 'config', 'user.name', 'Synthetic Trial'])
    run(root, ['git', 'config', 'user.email', 'trial@example.invalid'])
    run(root, ['git', 'add', '--', *[p.name for p in seed.iterdir()]])
    run(root, ['git', 'commit', '-m', 'baseline synthetic target'])
    base = run(root, ['git', 'rev-parse', 'HEAD'])
    run(root, ['git', 'switch', '-c', 'feature/name-report'])
    (root / 'sentinel.txt').write_text('unrelated staged change\n')
    run(root, ['git', 'add', '--', 'sentinel.txt'])
    (root / 'sentinel.txt').write_text('unrelated unstaged change\n')
    (root / 'sentinel.txt').chmod(0o755)
    (root / 'untracked-note.txt').write_text('unrelated note retained\n')
    (root / 'note-link').symlink_to('untracked-note.txt')
    save(HERE / 'evidence' / 'protected.json', protection(root))
    # Runtime pointer stays outside the public repository and is never committed.
    descriptor, name = tempfile.mkstemp(prefix='work-on-multi-pointer-', suffix='.json')
    os.close(descriptor)
    pointer = Path(name)
    save(pointer, {'root': str(root), 'base': base})
    print(pointer)


def capture(root, base, label, expected):
    before = manifest(root)
    result = run(root, [sys.executable, '-B', '-m', 'unittest', '-v'], expected)
    del result
    if manifest(root) != before:
        raise RuntimeError('checks changed fixture')
    scope = state(root, base, OWNED)
    protected = protection(root)
    if protected != json.loads((HERE / 'evidence' / 'protected.json').read_text()):
        raise RuntimeError('protected work changed')
    destination = HERE / 'fixture' / label
    destination.mkdir(parents=True, exist_ok=False)
    for name in OWNED:
        if (root / name).exists():
            shutil.copy2(root / name, destination / name)
    save(HERE / 'evidence' / (label + '.json'), {
        'scope': scope, 'membership': before, 'protected': protected,
        'test_exit': expected, 'python': sys.version.split()[0],
        'status_nul_hex': helper().git(root, 'status', '--porcelain=v1', '-z',
                                     '--untracked-files=all').hex()})
    patch = helper().git(root, 'diff', '--no-ext-diff', '--binary', '--full-index',
                        '--no-color', base, 'HEAD', '--', *OWNED)
    (HERE / 'evidence' / (label + '.diff')).write_bytes(patch)
    print(json.dumps({'label': label, 'head': scope['head'], 'test_exit': expected}))


def freshness(root, base, label):
    record = json.loads((HERE / 'evidence' / (label + '.json')).read_text())
    matching = (state(root, base, OWNED) == record['scope']
                and manifest(root) == record['membership']
                and protection(root) == record['protected'])
    print(json.dumps({'label': label, 'matching': matching}))
    if not matching:
        raise RuntimeError('stale scope or membership')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['init', 'capture', 'freshness', 'git'])
    parser.add_argument('--pointer', type=Path)
    parser.add_argument('--label')
    parser.add_argument('--expected', type=int, default=0)
    parser.add_argument('args', nargs='*')
    options = parser.parse_args()
    if options.command == 'init':
        initialize()
        return
    location = json.loads(options.pointer.read_text())
    root, base = Path(location['root']), location['base']
    if options.command == 'capture':
        capture(root, base, options.label, options.expected)
    elif options.command == 'freshness':
        freshness(root, base, options.label)
    else:
        print(run(root, ['git', *options.args], options.expected))


if __name__ == '__main__':
    main()
