#!/usr/bin/env python3
"""Check retained evidence; optional offline replay is not a new agent trial."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((HERE / name).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    integrity = read('integrity.json')
    actual = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}
    assert actual == set(integrity['artifacts']) | {'integrity.json'}, 'artifact membership drift'
    for name, value in integrity['artifacts'].items():
        assert digest(HERE / name) == value, 'changed artifact: ' + name
    for name, value in integrity['runtime_sources'].items():
        assert digest(REPO / name) == value, 'historical runtime pin stale: ' + name

    protected = read('evidence/protected.json')
    records = [json.loads(line) for line in (HERE / 'evidence/commands.jsonl').read_text().splitlines()]
    checks = [r for r in records if r['command'] == ['python3', '-B', '-m', 'unittest', '-v']]
    assert [r['exit'] for r in checks] == [0, 1, 0, 0]
    assert "AssertionError: ' a ' != 'a'" in checks[1]['stderr']
    assert 'FAILED (failures=1)' in checks[1]['stderr']
    assert all('OK' in checks[i]['stderr'] for i in [0, 2, 3])
    heads = []
    for label, expected in [('baseline-check', 0), ('failed', 1), ('repaired', 0), ('final', 0)]:
        record = read('evidence/' + label + '.json')
        scope = record['scope']
        heads.append(scope['head'])
        assert record['test_exit'] == expected
        assert record['protected'] == protected
        assert digest(HERE / 'evidence' / (label + '.diff')) == scope['committed_sha256']
        directory = HERE / 'fixture' / label
        present = {name for name, info in scope['files'].items() if info['kind'] != 'absent'}
        assert {p.name for p in directory.iterdir()} == present
        for name in present:
            path = directory / name
            assert digest(path) == scope['files'][name]['sha256']
            assert path.stat().st_mode & 0o777 == scope['files'][name]['mode']
            assert record['membership'][name]['sha256'] == digest(path)
        if args.replay:
            with tempfile.TemporaryDirectory(prefix='work-on-multi-replay-') as temporary:
                root = Path(temporary)
                for path in directory.iterdir():
                    shutil.copy2(path, root / path.name)
                result = subprocess.run([sys.executable, '-B', '-m', 'unittest', '-v'],
                                        cwd=root, capture_output=True, text=True)
                assert result.returncode == expected, label + ': unexpected replay exit'
                if expected:
                    assert "AssertionError: ' a ' != 'a'" in result.stderr
                print(label + ': replay exit ' + str(result.returncode))
    assert len(set(heads)) == 4
    event = read('evidence/prerequisite-event.json')
    assert event['integrated_head'] == heads[2] and event['acceptance_recorded']
    assert event['spent'] == 1 and event['limit'] == 2
    assert not read('progress.json')['ticket_102_started']
    final_progress = read('progress-final.json')
    assert final_progress['ticket_102_started']
    assert final_progress['integrated_ticket_102'] == heads[3]
    assert final_progress['repair_count_after_corrective_commit'] == 1
    assert final_progress['final_integration_repair_count'] == 0
    for name, value in event['review_report_hashes'].items():
        assert digest(HERE / 'reports' / name) == value
    graph = read('evidence/tracker-read.json')
    assert graph['network_calls'] == 0
    assert graph['rejected_methods'] == ['POST', 'PATCH', 'DELETE']
    assert graph['reads'] == event['graph_reobserved']
    receipts = read('review-receipts.json')
    assert receipts['max_active_non_lead'] == 2
    for workflow in receipts['workflows']:
        assert workflow['workflow_state'] == 'completed'
        assert workflow['inventory_complete']
        assert len(workflow['children']) == 2
        for child in workflow['children']:
            assert child['state'] == 'completed'
            assert child['requested_context'] == child['resolved_context'] == 'fresh'
            assert digest(HERE / child['report']) == child['published_report_sha256']
    assert 'ineligible' in (HERE / 'reports/repaired-spec.md').read_text()
    assert 'No issues found' in (HERE / 'reports/final-spec.md').read_text()
    # Adapter check is local and has no network/process mutation route.
    import importlib.util
    source = importlib.util.spec_from_file_location('trial', HERE / 'trial.py')
    trial = importlib.util.module_from_spec(source)
    source.loader.exec_module(trial)
    for endpoint, value in graph['reads'].items():
        assert trial.tracker_read('GET', endpoint) == value
    for method in ['POST', 'PATCH', 'DELETE']:
        try:
            trial.tracker_read(method, 'issues/102/dependencies/blocked_by')
        except PermissionError:
            pass
        else:
            raise AssertionError('mock accepted a write')
    print('retained artifacts, runtime pin, scope, preservation, graph and lifecycle records match')
    print('offline replay is not agent execution, independent review or live GitHub verification')


if __name__ == '__main__':
    main()
