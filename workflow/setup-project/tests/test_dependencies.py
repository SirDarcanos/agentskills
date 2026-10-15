import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / 'scripts' / 'dependencies.py'
spec = importlib.util.spec_from_file_location('dependencies', MODULE)
deps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deps)
REPO = 'example/project'


def issue(number, repo=REPO):
    return {'number': number, 'id': 1000 + number,
            'repository_url': f'https://api.github.com/repos/{repo}'}


def plan(*edges):
    return {'repository': REPO, 'dependencies': [{'blocked': a, 'by': b} for a, b in edges]}


class FakeGitHub:
    def __init__(self, graph=None):
        self.graph = copy.deepcopy(graph or {})
        self.writes = []
        self.fail_on = None
        self.ignore_write = False
        self.hide_reverse = False

    def request(self, suffix, method='GET', payload=None, paginated=False):
        number = int(suffix.split('/')[0])
        if method == 'POST':
            blocker = payload['issue_id'] - 1000
            self.writes.append((number, blocker))
            if not self.ignore_write:
                self.graph.setdefault(number, set()).add(blocker)
            if self.fail_on == number:
                raise deps.Blocked('timeout after possible mutation')
            return issue(blocker)
        if '/' not in suffix:
            return issue(number)
        if suffix.endswith('/blocked_by'):
            return [issue(n) for n in sorted(self.graph.get(number, set()))]
        if suffix.endswith('/blocking'):
            return [] if self.hide_reverse else [issue(n) for n, bs in self.graph.items() if number in bs]
        raise AssertionError(suffix)


class DependencyWorkflowTests(unittest.TestCase):
    def test_read_only_plan_deduplicates_and_preserves_existing_edges(self):
        api = FakeGitHub({10: {7, 9}})
        report = deps.reconcile(plan((10, 9), (11, 9), (11, 9)), api)
        self.assertEqual(report['additions'], [{'blocked': 11, 'by': 9}])
        self.assertEqual(report['already_present'], 1)
        self.assertEqual(api.writes, [])
        self.assertEqual(api.graph, {10: {7, 9}})

    def test_apply_uses_database_id_correct_direction_and_rerun_is_noop(self):
        api = FakeGitHub({10: {7}})
        p = plan((10, 9), (11, 9), (12, 10), (12, 11))
        report = deps.reconcile(p, api, apply=True)
        self.assertEqual(report, {'status': 'verified', 'repository': REPO, 'added': 4, 'edges': 4})
        self.assertEqual(api.graph, {10: {7, 9}, 11: {9}, 12: {10, 11}})
        self.assertEqual(api.writes, [(10, 9), (11, 9), (12, 10), (12, 11)])
        self.assertEqual(deps.reconcile(p, api, apply=True)['added'], 0)
        self.assertEqual(len(api.writes), 4)

    def test_cycles_are_checked_through_existing_and_planned_edges_before_writes(self):
        for graph, p in [({9: {7}, 7: {10}}, plan((10, 9))),
                         ({}, plan((10, 9), (9, 10))),
                         ({9: {7}, 7: {9}}, plan((10, 9)))]:
            with self.subTest(graph=graph, p=p):
                api = FakeGitHub(graph)
                with self.assertRaisesRegex(deps.Blocked, 'cycle'):
                    deps.reconcile(p, api, apply=True)
                self.assertEqual(api.writes, [])

    def test_failed_write_is_not_retried_and_next_run_inspects_partial_success(self):
        api = FakeGitHub()
        api.fail_on = 11
        events = []
        with self.assertRaisesRegex(deps.Blocked, 'timeout'):
            deps.reconcile(plan((10, 9), (11, 9)), api, apply=True, emit=events.append)
        self.assertEqual(api.writes, [(10, 9), (11, 9)])
        self.assertEqual([x['status'] for x in events], ['attempting', 'verified', 'attempting'])
        api.fail_on = None
        self.assertEqual(deps.reconcile(plan((10, 9), (11, 9)), api, apply=True)['added'], 0)
        self.assertEqual(len(api.writes), 2)

    def test_success_without_forward_or_reverse_readback_is_blocked(self):
        for attribute in ['ignore_write', 'hide_reverse']:
            with self.subTest(attribute=attribute):
                api = FakeGitHub()
                setattr(api, attribute, True)
                with self.assertRaisesRegex(deps.Blocked, 'Read-back mismatch'):
                    deps.reconcile(plan((10, 9), (11, 9)), api, apply=True)
                self.assertEqual(api.writes, [(10, 9)])

    def test_database_id_mismatch_in_either_direction_blocks_further_writes(self):
        for direction in ['blocked_by', 'blocking']:
            class WrongID(FakeGitHub):
                def request(self, suffix, **kwargs):
                    result = super().request(suffix, **kwargs)
                    if kwargs.get('method', 'GET') == 'GET' and self.writes and suffix.endswith('/' + direction):
                        return [{**item, 'id': item['id'] + 5000} for item in result]
                    return result
            api = WrongID()
            with self.subTest(direction=direction), self.assertRaisesRegex(deps.Blocked, 'Database ID mismatch'):
                deps.reconcile(plan((10, 9), (11, 9)), api, apply=True)
            self.assertEqual(api.writes, [(10, 9)])

    def test_existing_edge_id_mismatch_blocks_planning_and_all_writes(self):
        for direction in ['blocked_by', 'blocking']:
            class WrongID(FakeGitHub):
                def request(self, suffix, **kwargs):
                    result = super().request(suffix, **kwargs)
                    if kwargs.get('method', 'GET') == 'GET' and suffix.endswith('/' + direction):
                        return [{**item, 'id': item['id'] + 5000} for item in result]
                    return result
            for apply in [False, True]:
                api = WrongID({10: {9}})
                with self.subTest(direction=direction, apply=apply), self.assertRaisesRegex(deps.Blocked, 'Database ID mismatch'):
                    deps.reconcile(plan((10, 9), (11, 9)), api, apply=apply)
                self.assertEqual(api.writes, [])

    def test_reverse_scope_and_permissions_are_checked_before_any_write(self):
        for mode in ['foreign', 'forbidden', 'mismatch']:
            class UnsupportedReverse(FakeGitHub):
                def request(self, suffix, **kwargs):
                    if suffix.endswith('/blocking'):
                        if mode == 'forbidden':
                            raise deps.Blocked('reverse endpoint forbidden')
                        return [issue(10, 'other/repo' if mode == 'foreign' else REPO)]
                    return super().request(suffix, **kwargs)
            api = UnsupportedReverse()
            with self.subTest(mode=mode), self.assertRaises(deps.Blocked):
                deps.reconcile(plan((10, 9)), api, apply=True)
            self.assertEqual(api.writes, [])

    def test_post_write_cycle_error_preserves_truth_about_completed_writes(self):
        class ConcurrentCycle(FakeGitHub):
            def request(self, suffix, **kwargs):
                if suffix == '9' and self.writes:
                    self.graph.setdefault(9, set()).add(10)
                return super().request(suffix, **kwargs)
        api = ConcurrentCycle()
        events = []
        with self.assertRaisesRegex(deps.Blocked, 'cycle') as error:
            deps.reconcile(plan((10, 9)), api, apply=True, emit=events.append)
        self.assertNotIn('no writes', str(error.exception))
        self.assertEqual(api.writes, [(10, 9)])
        self.assertEqual([e['status'] for e in events], ['attempting', 'verified'])

    def test_unavailable_read_does_not_mean_missing_relationship(self):
        api = FakeGitHub()
        with patch.object(api, 'request', side_effect=deps.Blocked('forbidden')):
            with self.assertRaisesRegex(deps.Blocked, 'forbidden'):
                deps.reconcile(plan((10, 9)), api, apply=True)
        self.assertEqual(api.writes, [])

    def test_unknown_identity_cross_repository_and_pull_requests_fail_closed(self):
        for value in [issue(10, 'other/repo'), {'number': 10, 'id': 1010},
                      {**issue(10), 'pull_request': {}}, issue(99)]:
            api = FakeGitHub()
            with patch.object(api, 'request', return_value=value):
                with self.assertRaises(deps.Blocked):
                    deps.reconcile(plan((10, 9)), api, apply=True)
            self.assertEqual(api.writes, [])

    def test_malformed_plans_never_contact_github(self):
        bad = [plan((1, 1)), plan((True, 2)), plan((-1, 2)),
               {'repository': '../repo', 'dependencies': []},
               {'repository': REPO, 'dependencies': [{'blocked': 10, 'by': 9, 'delete': True}]},
               {'repository': REPO, 'dependencies': 'bad'}]
        for p in bad:
            with self.subTest(plan=p), patch.object(deps.GitHub, 'request') as request:
                with self.assertRaises(deps.Blocked):
                    deps.reconcile(p, apply=True)
                request.assert_not_called()

    def test_large_graph_stops_before_mutations(self):
        api = FakeGitHub({10: {9}, 9: {8}})
        with patch.object(deps, 'MAX_ISSUES', 2):
            with self.assertRaisesRegex(deps.Blocked, 'limit'):
                deps.reconcile(plan((10, 9)), api, apply=True)
        self.assertEqual(api.writes, [])

    def test_empty_plan_needs_no_network(self):
        with patch.object(deps.GitHub, 'request') as request:
            self.assertEqual(deps.reconcile(plan(), apply=True)['edges'], 0)
            request.assert_not_called()


class TransportTests(unittest.TestCase):
    def test_cli_reads_all_pages_and_pins_host(self):
        response = subprocess.CompletedProcess([], 0, json.dumps([[issue(1)], [issue(2)]]), '')
        with patch.object(deps.subprocess, 'run', return_value=response) as run:
            values = deps.GitHub(REPO).request('10/dependencies/blocked_by', paginated=True)
        self.assertEqual([i['number'] for i in values], [1, 2])
        args = run.call_args.args[0]
        self.assertIn('--paginate', args)
        self.assertIn('--slurp', args)
        self.assertEqual(args[args.index('--hostname') + 1], 'github.com')
        self.assertEqual(args[args.index('--method') + 1], 'GET')

    def test_cli_write_passes_id_as_json_without_shell_interpolation(self):
        response = subprocess.CompletedProcess([], 0, json.dumps(issue(9)), '')
        with patch.object(deps.subprocess, 'run', return_value=response) as run:
            deps.GitHub(REPO).request('10/dependencies/blocked_by', method='POST', payload={'issue_id': 1009})
        self.assertEqual(json.loads(run.call_args.kwargs['input']), {'issue_id': 1009})
        self.assertNotIn('shell', run.call_args.kwargs)
        self.assertEqual(run.call_count, 1)

    def test_errors_and_bad_page_shapes_are_not_empty_graphs(self):
        for rc, body in [(1, 'not authorized'), (0, 'bad json'), (0, '{}'), (0, '[{}]')]:
            with self.subTest(rc=rc, body=body):
                response = subprocess.CompletedProcess([], rc, body, 'sensitive diagnostic')
                with patch.object(deps.subprocess, 'run', return_value=response):
                    with self.assertRaises(deps.Blocked) as error:
                        deps.GitHub(REPO).request('10/dependencies/blocked_by', paginated=True)
                    self.assertNotIn('sensitive diagnostic', str(error.exception))

    def test_timeout_does_not_retry_or_claim_no_write(self):
        with patch.object(deps.subprocess, 'run', side_effect=subprocess.TimeoutExpired('gh', 60)) as run:
            with self.assertRaisesRegex(deps.Blocked, 'inspect state before retry'):
                deps.GitHub(REPO).request('10/dependencies/blocked_by', method='POST', payload={'issue_id': 1009})
            self.assertEqual(run.call_count, 1)


if __name__ == '__main__':
    unittest.main()
