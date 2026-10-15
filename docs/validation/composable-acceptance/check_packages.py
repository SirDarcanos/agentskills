"""#73 structural catalog checks, not a runtime installer or capability resolver.

Run from repository root with python3 -B. Copies are disposable and never active.
Reuse #31's Markdown link/anchor checker without changing historical evidence.
"""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    'delivery_links', REPO / 'docs/validation/delivery-coverage/check_packages.py')
links = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(links)

# Only documented offline commands, never arbitrary scripts discovered by name.
JOBS = {
    **{name: ['scripts/check-fixture.py'] for name in
       ('analyze', 'tdd', 'prototype', 'characterize', 'acceptance-first', 'build-and-check')},
    'work-on': ['scripts/check-single-change-fixture.py'],
    'work-on-spec': ['scripts/check-coordination-fixture.py'],
    'review-delivery': ['scripts/test_snapshot.py'],
    **{name: ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v']
       for name in ('setup-project', 'domain-modeling', 'ask-clef', 'ask-clef-flash',
                    'ask-nimble', 'ask-jev')},
}


def offline_environment():
    """Confine fixture Git routing and prevent ambient hooks/template/config use."""
    env = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
    env.update(PYTHONDONTWRITEBYTECODE='1', GIT_CONFIG_NOSYSTEM='1',
               GIT_CONFIG_GLOBAL=os.devnull, GIT_TEMPLATE_DIR='',
               GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='core.hooksPath',
               GIT_CONFIG_VALUE_0=os.devnull)
    return env


def run_offline(command, root):
    return subprocess.run(command, cwd=root, env=offline_environment(),
                          capture_output=True, text=True, timeout=120)


def metadata(entry):
    """Parse the scalar-only frontmatter subset actually shipped, fail closed."""
    lines = entry.splitlines()
    assert lines and lines[0] == '---', 'missing frontmatter'
    end = lines.index('---', 1)
    fields = {}
    key = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith((' ', '\t')):
            assert key == 'description', 'unsupported continuation'
            fields[key] += ' ' + line.strip()
            continue
        match = re.fullmatch(r'([a-z][a-z-]*):\s*(.*)', line)
        assert match, 'unsupported frontmatter field'
        key, value = match.groups()
        assert key not in fields, 'duplicate frontmatter field'
        if value in ('>', '|', '>-', '|-'):
            value = ''
        fields[key] = value.strip('"\'')
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields.get('name', '')), 'invalid name'
    assert fields.get('description', '').strip(), 'missing trigger description'
    return fields


def manifest(root):
    result = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            result[relative] = {'link': path.readlink().as_posix()}
        elif path.is_file():
            result[relative] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                                'mode': path.stat().st_mode & 0o777}
    return result


def inspect_package(root):
    fields = metadata((root / 'SKILL.md').read_text())
    notice = (root / 'LICENSE').read_text()
    authoritative = (REPO / 'LICENSE').read_text()
    assert 'Copyright (c) 2026 Nicola Mustone' in notice, 'maintainer notice absent'
    assert authoritative.split('Permission is', 1)[1] in notice, 'MIT permission/warranty absent'
    if fields['name'] == 'tdd':
        assert 'Copyright (c) 2026 Matt Pocock' in notice, 'upstream notice absent'
    markdown = sorted(root.rglob('*.md'))
    count = links.check_links(markdown, root)
    for path in root.rglob('*'):
        if path.is_symlink():
            assert path.resolve().is_relative_to(root.resolve()), 'external package symlink'
        elif path.suffix == '.py':
            ast.parse(path.read_text(), filename=path.name)
    return dict(name=fields['name'], description=fields['description'],
                command_only=fields.get('disable-model-invocation') == 'true',
                links=count, files=manifest(root))


def catalog(locations):
    """Explicit-path synthetic catalog: metadata identity, not semantic compatibility."""
    result = {}
    for location in locations:
        fields = metadata((location / 'SKILL.md').read_text())
        assert fields['name'] not in result, 'ambiguous duplicate catalog name'
        result[fields['name']] = location
    return result


def package_locations(root):
    packages = sorted(path.parent for group in ('workflow', 'writing', 'models')
                      for path in (root / group).glob('*/SKILL.md'))
    assert packages, 'no skill packages discovered'
    return packages


def main():
    packages = package_locations(REPO)
    readme = (REPO / 'README.md').read_text()
    records = []
    with tempfile.TemporaryDirectory(prefix='composable-package-check-') as scratch:
        scratch = Path(scratch)
        copies = []
        for index, source in enumerate(packages):
            before = manifest(source)
            original = inspect_package(source)
            assert original['name'] == source.name, 'directory/name mismatch'
            assert f']({source.relative_to(REPO).as_posix()}/)' in readme, 'missing public listing'
            # Independent arbitrary parents, not named sibling package directories.
            isolated = scratch / f'location-{index}' / 'payload'
            shutil.copytree(source, isolated, symlinks=True)
            assert inspect_package(isolated) == original, 'copy content differs'
            record = {**original, 'isolated': True, 'offline_command': None}
            if source.name in JOBS:
                command = [sys.executable, '-B'] + JOBS[source.name]
                completed = run_offline(command, isolated)
                raw = completed.stdout + completed.stderr
                # Temporary test targets can use the platform temp root as well.
                raw = raw.replace(str(REPO), '<repository>').replace(str(scratch), '<isolated>')
                for prefix in {tempfile.gettempdir(), str(Path(tempfile.gettempdir()).resolve())}:
                    raw = re.sub(re.escape(prefix.rstrip('/')) + r'/[^/\s\"\']+/',
                                 '<scratch>/', raw)
                record['offline_command'] = ['python3', '-B'] + JOBS[source.name]
                record['exit'] = completed.returncode
                record['output'] = raw
                assert completed.returncode == 0, (source.name, raw)
            assert manifest(source) == before, 'source modified by check'
            records.append(record)
            copies.append(isolated)
            print(source.name, original['links'], 'links; isolated check passed', flush=True)
        resolved = catalog(copies)
        assert set(resolved) == {path.name for path in packages}
        # Catalog checks only; route behavior comes from existing package fixtures.
        assert 'review-delivery' not in catalog([resolved['research']])
        try:
            catalog([copies[0], copies[0]])
        except AssertionError:
            pass
        else:
            raise AssertionError('duplicate accepted')
    docs = [REPO / 'README.md'] + sorted(Path(__file__).parent.glob('*.md'))
    print('Repository documentation:', links.check_links(docs, REPO), 'links')
    output = Path(__file__).parent / 'results/packages.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(dict(python=sys.version.split()[0], packages=records,
                                     catalog='explicit-path synthetic; no installed discovery'), indent=2) + '\n')
    print('No installation, service, assessment, agent or remote mutation performed.')


if __name__ == '__main__':
    main()
