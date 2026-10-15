"""Retain raw offline checks. No live endpoints or services are invoked."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from run_fixture import REPO, environment


def sanitize(raw):
    raw = raw.replace(str(REPO), '<repository>')
    # Python resolves macOS /var aliases in tracebacks; handle both spellings.
    prefixes = {tempfile.gettempdir(), str(Path(tempfile.gettempdir()).resolve())}
    for prefix in sorted(prefixes, key=len, reverse=True):
        raw = re.sub(re.escape(prefix.rstrip('/')) + r'/[^/\s\"\']+/',
                     '<scratch>/', raw)
    return raw


def inputs(directory):
    files = {}
    for path in sorted(directory.rglob('*')):
        if not path.is_file() or any(part in ('__pycache__', 'results') for part in path.parts):
            continue
        if directory.name == 'bug-to-fix' and path.suffix != '.py' and path.name != 'agreement.md':
            continue
        files[path.relative_to(REPO).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def main():
    output = Path(__file__).resolve().parent / 'results/checks'
    output.mkdir(parents=True, exist_ok=True)
    jobs = [(name, REPO, [sys.executable, '-B', 'workflow/' + name + '/scripts/check-fixture.py'])
            for name in ('tdd', 'prototype', 'characterize', 'acceptance-first', 'build-and-check')]
    for name, directory in [('handoffs', 'docs/validation/bug-to-fix'),
                            ('investigation', 'docs/validation/investigate-bug')]:
        jobs.append((name, REPO, [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', directory, '-p', 'test_*.py', '-v']))
    for package in ('ask-nimble', 'ask-clef', 'ask-clef-flash', 'ask-jev'):
        jobs.append((package, REPO / 'models' / package, [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v']))
    summary = []
    for name, root, command in jobs:
        source = (REPO / 'docs/validation/bug-to-fix' if name == 'handoffs' else
                  REPO / 'docs/validation/investigate-bug' if name == 'investigation' else
                  REPO / ('models' if name.startswith('ask-') else 'workflow') / name)
        before = inputs(source)
        result = subprocess.run(command, cwd=root, env=environment(),
                                capture_output=True, text=True, timeout=90)
        # Test code uses disposable roots; raw output must exclude workstation paths.
        raw = sanitize(result.stdout + result.stderr)
        (output / (name + '.txt')).write_text(raw)
        summary.append(dict(name=name, cwd=root.relative_to(REPO).as_posix(),
                            command=['python3' if a == sys.executable else a for a in command],
                            exit=result.returncode, evidence=name + '.txt',
                            environment='Python ' + sys.version.split()[0],
                            checked_inputs=before, inputs_unchanged=inputs(source) == before))
        print(name, 'exit', result.returncode, flush=True)
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    assert all(row['exit'] == 0 and row['inputs_unchanged'] for row in summary), summary


if __name__ == '__main__':
    main()
