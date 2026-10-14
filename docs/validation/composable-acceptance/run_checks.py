"""Collect #73 offline evidence without refreshing historical result directories."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from check_packages import offline_environment

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest_inputs():
    # Full deciding packages and historical executable fixtures, not just main scripts.
    result = {}
    roots = [p.parent for p in REPO.glob('*/SKILL.md')]
    roots += [REPO / 'docs/validation', REPO / 'docs/agents', REPO / 'docs/design', REPO / 'docs/adr']
    for root in roots:
        for path in sorted(root.rglob('*')):
            if path.is_file() and not path.is_symlink() and HERE not in path.parents and '__pycache__' not in path.parts:
                result[path.relative_to(REPO).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    for name in ('README.md', 'AGENTS.md', 'CHANGELOG.md', 'CONTEXT.md', 'LICENSE'):
        result[name] = hashlib.sha256((REPO / name).read_bytes()).hexdigest()
    for path in sorted(HERE.iterdir()):
        if path.suffix in ('.py', '.mjs', '.md'):
            result[path.relative_to(REPO).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main():
    output = HERE / 'results'
    output.mkdir(exist_ok=True)
    before = digest_inputs()
    env = offline_environment()
    jobs = []
    for name, directory in (
        ('migration', 'installed-skill-migration'), ('handoffs', 'bug-to-fix'),
        ('investigation', 'investigate-bug'), ('ticketing', 'write-tickets'),
        ('pr-impact', 'pr'), ('multi-ticket-harness', 'composable-multi-ticket'),
        ('invocation-regressions', 'delivery-coverage'), ('collector-regressions', 'composable-acceptance')):
        jobs.append((name, ['-m', 'unittest', 'discover', '-s', 'docs/validation/' + directory, '-p', 'test_*.py', '-v']))
    jobs.append(('retained-multi-ticket', ['docs/validation/composable-multi-ticket/check_evidence.py', '-v']))
    summary = []
    with tempfile.TemporaryDirectory(prefix='composable-acceptance-') as scratch:
        jobs.append(('discovery-ticket-replay', ['docs/validation/discovery-spec-tickets/run_fixture.py', scratch + '/discovery']))
        for name, args in jobs:
            result = subprocess.run([sys.executable, '-B'] + args, cwd=REPO, env=env,
                                    capture_output=True, text=True, timeout=120)
            raw = (result.stdout + result.stderr).replace(str(REPO), '<repository>')
            for prefix in {tempfile.gettempdir(), str(Path(tempfile.gettempdir()).resolve())}:
                raw = re.sub(re.escape(prefix.rstrip('/')) + r'/[^/\s\"\']+/', '<scratch>/', raw)
            (output / (name + '.txt')).write_text(raw)
            summary.append(dict(name=name, command=['python3', '-B'] +
                                [a.replace(scratch, '<scratch>') for a in args],
                                exit=result.returncode, evidence=name + '.txt'))
            print(name, 'exit', result.returncode, flush=True)
        discovery = Path(scratch) / 'discovery'
        if discovery.exists():
            # Replay's outputs are portable synthetic artifacts; originals untouched.
            for path in sorted(discovery.glob('*')):
                if path.is_file():
                    raw = path.read_text().replace(scratch, '<scratch>').replace(str(REPO), '<repository>')
                    (output / ('discovery-' + path.name)).write_text(raw)
    after = digest_inputs()
    (output / 'checks.json').write_text(json.dumps(dict(
        python=sys.version.split()[0], jobs=summary, checked_inputs=before,
        inputs_unchanged=before == after), indent=2) + '\n')
    assert before == after, 'historical/package inputs changed'
    assert all(row['exit'] == 0 for row in summary), 'failed check; inspect retained logs'


if __name__ == '__main__':
    main()
