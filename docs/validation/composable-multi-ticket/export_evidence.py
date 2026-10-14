#!/usr/bin/env python3
"""Export explicitly authorized #72 artifacts with path-only sanitization.

Original local artifacts remain untouched. This is not attestation or acceptance.
No raw sessions, credentials, environment variables or arbitrary logs are copied.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def export(root, source, runtime, outputs, destination):
    destination.mkdir(parents=True, exist_ok=False)
    prefixes = {str(root): '<fixture>', str(root.resolve()): '<fixture>',
                str(source): '<source>', str(source.resolve()): '<source>',
                str(runtime): '<runtime>', str(runtime.resolve()): '<runtime>',
                str(outputs): '<outputs>', str(outputs.resolve()): '<outputs>'}
    replacements = sorted(prefixes.items(), key=lambda p: len(p[0]), reverse=True)
    manifest = {}

    def copy(path, relative):
        raw = path.read_bytes()
        content = raw.decode('utf-8')
        for old, new in replacements:
            content = content.replace(old, new)
        # Workers can report resolved /private aliases of source/session roots.
        if '/Users/' in content or '/var/folders/' in content:
            raise ValueError('Unresolved local path in ' + str(relative))
        dest = destination / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)
        manifest[str(relative)] = {'original_sha256': sha(raw),
                                   'retained_sha256': sha(dest.read_bytes()),
                                   'path_sanitized': raw != dest.read_bytes()}

    for path in sorted((root / 'evidence').iterdir()):
        if path.is_file() and path.suffix in {'.json', '.log', '.md', '.patch', '.diff', '.py'}:
            copy(path, Path('evidence') / path.name)
    for name in ['AGENTS.md', 'technical.md', 'graph.json', 'test_trial.py',
                 'render.py', 'normalize.py', 'pipeline.py']:
        copy(root / 'target' / name, Path('target') / name)
    for path in sorted(outputs.glob('*.md')):
        copy(path, Path('reports') / path.name)

    # Whitelist actual lifecycle observations, retaining both start and terminal
    # timestamps/identities; omit task text, local directories and provider data.
    events = []
    for line in (runtime / 'events.jsonl').read_text().splitlines():
        item = json.loads(line)
        if item['type'] == 'subagent.child-status' and item['status'] == 'started':
            events.append({k: item[k] for k in ['ts', 'runId', 'type', 'childId',
                          'status', 'agent', 'childRunId', 'workflowKey']})
        elif item['type'] == 'subagent.workflow.child_settled':
            events.append({k: item[k] for k in ['ts', 'runId', 'type',
                          'childKey', 'childRunId', 'outcome']})
    (destination / 'lifecycle.json').write_text(json.dumps(events, indent=2) + '\n')
    manifest['lifecycle.json'] = {
        'original_event_file_sha256': sha((runtime / 'events.jsonl').read_bytes()),
        'retained_sha256': sha((destination / 'lifecycle.json').read_bytes()),
        'transformation': 'selected start/settled events and whitelisted fields'}
    # Summarize actual recorded tool starts without exporting raw sessions or
    # arguments (which can contain local paths). This is not a syscall audit.
    audit = []
    for event in events:
        if event['type'] != 'subagent.child-status':
            continue
        path = runtime.parent / event['childRunId'] / 'events.jsonl'
        if not path.exists():
            continue  # Offline exporter tests need no actual child runtime.
        calls = [json.loads(line) for line in path.read_text().splitlines()
                 if json.loads(line).get('type') == 'tool_execution_start']
        counts = {}
        for call in calls:
            name = call['toolName']
            counts[name] = counts.get(name, 0) + 1
        audit.append({'key': event['workflowKey'], 'childRunId': event['childRunId'],
                      'event_file_sha256': sha(path.read_bytes()), 'tool_counts': counts})
    (destination / 'tool-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
    manifest['tool-audit.json'] = {
        'retained_sha256': sha((destination / 'tool-audit.json').read_bytes()),
        'transformation': 'tool start counts only; arguments and sessions excluded'}
    (destination / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Exported', len(manifest), 'artifacts; originals unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['root', 'source', 'runtime', 'outputs', 'destination']:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    export(args.root, args.source, args.runtime, args.outputs, args.destination)
