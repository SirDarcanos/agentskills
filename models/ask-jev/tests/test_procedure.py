"""Offline mock procedure/contract checks, not live calls or agent walkthroughs."""
import copy
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from procedure_fixture import ENDPOINT, VERSION, Ledger, Session, grant, request, response, validate

ROOT = Path(__file__).resolve().parents[1]


class AuthorizationTests(unittest.TestCase):
    def assert_no_effects(self, session):
        for effect in (session.credentials, session.send, session.confirm, session.delay):
            effect.assert_not_called()

    def test_absent_none_draft_conflicting_expired_has_zero_effects(self):
        for permission in (None, {}, {'approved': False}, {**grant(), 'current': False},
                           {**grant(), 'provenance': None}):
            s = Session()
            self.assertEqual(s.run(permission), 'no-call')
            self.assert_no_effects(s)

    def test_approved_hosted_use_needs_no_confirmation(self):
        s = Session()
        self.assertEqual(s.run(grant()), 'complete')
        s.confirm.assert_not_called()
        s.send.assert_called_once_with(ENDPOINT, s.payload)
        self.assertEqual((s.root.attempts, s.root.calls, s.root.spend), (1, 5, 5))
        self.assertEqual(s.reply['model'], VERSION)

    def test_wrong_identity_purpose_and_disclosure_has_zero_effects(self):
        for field, value in [('skill', 'ask-clef'), ('provider', 'other'),
                             ('endpoint', 'http://127.0.0.1:11434/v1/systemone'),
                             ('model', 'jev-preview'), ('resolution', 'other'),
                             ('purpose', 'other'), ('disclosure', set())]:
            s = Session()
            self.assertEqual(s.run({**grant(), field: value}), 'no-call')
            self.assert_no_effects(s)

    def test_version_pin_and_explicit_alias_permission(self):
        s = Session()
        s.payload['model'] = VERSION
        self.assertEqual(s.run({**grant(), 'model': VERSION, 'moving_alias': False}), 'complete')
        s = Session()
        self.assertEqual(s.run({**grant(), 'moving_alias': False}), 'no-call')
        self.assert_no_effects(s)

    def test_missing_retry_or_correction_limits_are_not_unlimited(self):
        for field in ('retries', 'corrections'):
            s = Session()
            p = grant()
            del p[field]
            self.assertEqual(s.run(p), 'no-call')
            self.assert_no_effects(s)

    def test_local_only_and_denied_private_disclosure(self):
        s = Session()
        s.data_class = 'private'
        self.assertEqual(s.run(grant()), 'no-call')
        self.assert_no_effects(s)
        self.assertEqual(s.run({**grant(), 'disclosure': {'private'}}), 'complete')
        s.confirm.assert_not_called()

    def test_explicit_request_without_autonomous_policy(self):
        s = Session()
        self.assertEqual(s.run(explicit=True), 'complete')
        s.confirm.assert_not_called()

    def test_explicit_request_does_not_override_project_ban(self):
        s = Session()
        self.assertEqual(s.run(explicit=True, restricted=True), 'no-call')
        self.assert_no_effects(s)

    def test_generated_command_is_not_consent(self):
        s = Session()
        self.assertEqual(s.run({'command': '/skill:ask-jev assess this'}), 'no-call')
        self.assert_no_effects(s)

    def test_unsuitable_question_skips_authenticated_operations(self):
        s = Session()
        self.assertEqual(s.run(grant(), suitable=False), 'direct-no-model')
        self.assert_no_effects(s)

    def test_call_exhaustion_and_outstanding_worker_reservations(self):
        for calls, reserved in [(0, 0), (1, 1), (None, 0)]:
            s = Session(Ledger(calls=calls))
            s.root.reserved_calls = reserved
            self.assertEqual(s.run(grant()), 'no-call')
            self.assert_no_effects(s)

    def test_spending_unknown_exhausted_reserved_and_wrong_currency(self):
        for spend, reserved in [(0, 0), (1, 1), (None, 0)]:
            s = Session(Ledger(spend=spend))
            s.root.reserved_spend = reserved
            self.assertEqual(s.run(grant()), 'no-call')
            self.assert_no_effects(s)
        for bound in (None, -1, float('nan'), float('inf'), True, 7):
            s = Session()
            self.assertEqual(s.run({**grant(), 'cost_bound': bound}), 'no-call')
            self.assert_no_effects(s)
        s = Session()
        self.assertEqual(s.run({**grant(), 'currency': 'other'}), 'no-call')
        self.assert_no_effects(s)

    def test_missing_credentials_has_no_send_or_implicit_configuration(self):
        s = Session()
        s.credentials.return_value = False
        self.assertEqual(s.run(grant()), 'unavailable')
        s.send.assert_not_called()
        s.confirm.assert_not_called()
        self.assertEqual(s.root.attempts, 0)

    def test_pre_send_revocation_exhaustion_and_expanded_data(self):
        for change in ('revoke', 'exhaust', 'disclosure'):
            s = Session()
            def revoke(p, _attempt):
                if change == 'revoke':
                    p['current'] = False
                elif change == 'exhaust':
                    s.root.calls = 0
                else:
                    s.data_class = 'private'
            self.assertEqual(s.run(grant(), before_send=revoke), 'no-call')
            s.send.assert_not_called()
            self.assertEqual(s.root.attempts, 0)

    def test_timeout_retains_unknown_charge_and_never_retries(self):
        s = Session(Ledger(calls=1, spend=1))
        s.send.side_effect = OSError('synthetic timeout')
        self.assertEqual(s.run(grant()), 'unavailable')
        s.send.assert_called_once()
        self.assertEqual((s.root.attempts, s.root.unknown_charges, s.root.spend), (1, 1, 0))
        resumed = Session(s.root, assessment='next')
        self.assertEqual(resumed.run(grant()), 'no-call')
        self.assert_no_effects(resumed)

    def test_malformed_and_http_errors_are_not_retried(self):
        for status, raw in [(200, 'malformed'), (401, '{}'), (422, '{}'), (500, '{}'),
                            (302, '{"location":"https://example.invalid"}')]:
            s = Session()
            s.send.return_value = (status, raw, None)
            self.assertEqual(s.run(grant()), 'unavailable')
            s.send.assert_called_once()
            s.delay.assert_not_called()
            self.assertEqual(s.root.attempts, 1)

    def test_only_429_and_529_retry_within_three_attempts(self):
        for status in (429, 529):
            s = Session()
            s.send.side_effect = [(status, '{}', 2), (status, '{}', 4), (200, response(), None)]
            self.assertEqual(s.run(grant()), 'complete')
            self.assertEqual(s.send.call_count, 3)
            self.assertEqual(s.root.retries, 2)
            self.assertEqual(s.root.spend, 3)  # failures not assumed free
            s.confirm.assert_not_called()

    def test_retry_ceiling_on_persistent_overload(self):
        s = Session()
        s.send.return_value = (529, '{}', 1)
        self.assertEqual(s.run(grant()), 'unavailable')
        self.assertEqual(s.send.call_count, 3)

    def test_retry_after_too_long_or_invalid_stops(self):
        for delay in (31, -1, float('inf'), 'unknown'):
            s = Session()
            s.send.return_value = (429, '{}', delay)
            self.assertEqual(s.run(grant()), 'unavailable')
            s.send.assert_called_once()
            s.delay.assert_not_called()

    def test_retry_requires_remaining_shared_call_spend_and_retry_limits(self):
        for root, p in [(Ledger(calls=1), grant()), (Ledger(spend=1), grant()),
                        (Ledger(retries=0), grant()), (Ledger(), {**grant(), 'retries': 0})]:
            s = Session(root)
            s.send.return_value = (429, '{}', 1)
            self.assertEqual(s.run(p), 'no-call')
            s.send.assert_called_once()

    def test_authority_rechecked_before_retry(self):
        s = Session()
        s.send.return_value = (429, '{}', 1)
        self.assertEqual(s.run(grant(), before_send=lambda p, n: p.update(current=n == 0)), 'no-call')
        s.send.assert_called_once()

    def test_parent_workers_and_resume_share_consumed_budget(self):
        root = Ledger(calls=1)
        self.assertEqual(Session(root, 'child-one').run(grant()), 'complete')
        for name in ('child-two', 'resumed'):
            s = Session(root, name)
            self.assertEqual(s.run(grant()), 'no-call')
            self.assert_no_effects(s)

    def test_one_correction_across_assessment_resume_and_six_attempt_cap(self):
        root = Ledger(calls=9, spend=9, retries=8)
        s = Session(root)
        s.send.side_effect = [(429, '{}', 1), (529, '{}', 1), (200, response(), None)] * 2
        self.assertEqual(s.run(grant()), 'complete')
        self.assertEqual(s.run(grant(), corrected=True), 'complete')
        resumed = Session(root)
        self.assertEqual(resumed.run(grant(), corrected=True), 'no-call')
        resumed.send.assert_not_called()
        self.assertEqual((root.attempts, root.corrections), (6, 1))

    def test_policy_or_root_correction_limit_zero(self):
        for root, p in [(Ledger(corrections=0), grant()), (Ledger(), {**grant(), 'corrections': 0})]:
            s = Session(root)
            self.assertEqual(s.run(p), 'complete')
            self.assertEqual(s.run(p, corrected=True), 'no-call')
            s.send.assert_called_once()

    def test_no_second_initial_request_or_failed_correction_refund(self):
        s = Session()
        self.assertEqual(s.run(grant()), 'complete')
        self.assertEqual(s.run(grant()), 'no-call')
        s.send.return_value = (200, 'invalid', None)
        self.assertEqual(s.run(grant(), corrected=True), 'unavailable')
        self.assertEqual(Session(s.root).run(grant(), corrected=True), 'no-call')
        self.assertEqual(s.root.attempts, 2)

    def test_fallback_policy_and_explicit_offer_wait(self):
        for explicit, direct, policy, expected in [
            (False, False, 'none', 'unavailable'),
            (False, False, 'direct', 'Agent assessment — Jev unavailable'),
            (True, False, 'direct', 'pending-fallback'),
            (True, True, 'none', 'Agent assessment — Jev unavailable')]:
            s = Session()
            s.credentials.return_value = False
            self.assertEqual(s.run({**grant(), 'fallback': policy}, explicit=explicit, direct=direct), expected)
            self.assertEqual(s.confirm.call_count, int(expected == 'pending-fallback'))
            s.send.assert_not_called()

    def test_prohibited_or_named_alternative_never_changes_transport(self):
        s = Session()
        s.send.return_value = (500, '{}', None)
        self.assertEqual(s.run({**grant(), 'fallback': 'ask-nimble'}), 'unavailable')
        s.send.assert_called_once_with(ENDPOINT, request())

    def test_valid_insufficient_data_is_not_failure_or_substitution(self):
        s = Session()
        s.send.return_value = (200, response(choice='insufficient_data'), None)
        self.assertEqual(s.run({**grant(), 'fallback': 'direct'}), 'complete')
        self.assertEqual(s.reply['answers']['decision']['choice'], 'insufficient_data')
        s.send.assert_called_once()
        s.confirm.assert_not_called()

    def test_batch_does_not_create_fresh_allowances(self):
        s = Session(Ledger(calls=1))
        q = s.payload['questions']['decision']
        s.payload['questions'] = {str(i): copy.deepcopy(q) for i in range(4)}
        s.send.return_value = (200, response(s.payload), None)
        self.assertEqual(s.run(grant()), 'complete')
        self.assertEqual(s.root.attempts, 1)
        s.payload['questions']['extra'] = q
        self.assertEqual(s.run(grant(), corrected=True), 'no-call')
        s.send.assert_called_once()


class ResponseTests(unittest.TestCase):
    def test_all_primitive_types_validate_together(self):
        payload = request()
        payload['questions'].update(n=dict(type='noul'), s=dict(type='score', criteria=['Low', 'High']))
        self.assertTrue(validate(response(payload), payload, VERSION))
        bad = json.loads(response(payload))
        bad['answers']['s']['legend']['1'] = 'Wrong'
        self.assertFalse(validate(json.dumps(bad), payload, VERSION))

    def test_malformed_top_level_wrong_model_ids_types_and_usage(self):
        raw = json.loads(response())
        changes = [lambda r: r.pop('usage'), lambda r: r.update(model='other'),
                   lambda r: r.update(answers={}), lambda r: r.update(error='bad'),
                   lambda r: r['usage'].update(input_tokens=True),
                   lambda r: r['usage'].update(output_tokens=-1),
                   lambda r: r['answers']['decision'].update(type='noul')]
        for change in changes:
            bad = copy.deepcopy(raw)
            change(bad)
            self.assertFalse(validate(json.dumps(bad), request(), VERSION))
        for raw in ('invalid', 'null', '[]', '{}'):
            self.assertFalse(validate(raw, request(), VERSION))

    def test_invalid_probabilities_confidence_and_selected_option(self):
        raw = json.loads(response())
        for fields in [dict(probabilities={'meets': 1}), dict(confidence=True),
                       dict(confidence=float('nan')), dict(choice='insufficient_data'),
                       dict(probabilities={'meets': 0.8, 'insufficient_data': 0.8}),
                       dict(probabilities={'meets': float('inf'), 'insufficient_data': 0})]:
            bad = copy.deepcopy(raw)
            bad['answers']['decision'].update(fields)
            self.assertFalse(validate(json.dumps(bad), request(), VERSION))

    def test_no_partial_interpretation_of_malformed_batch(self):
        s = Session()
        s.payload['questions']['second'] = copy.deepcopy(s.payload['questions']['decision'])
        raw = json.loads(response(s.payload))
        del raw['answers']['second']['confidence']
        s.send.return_value = (200, json.dumps(raw), None)
        self.assertEqual(s.run(grant()), 'unavailable')
        self.assertIsNone(s.reply)
        s.send.assert_called_once()


class PackageTests(unittest.TestCase):
    def check_package(self, root):
        entry = (root / 'SKILL.md').read_text()
        frontmatter = entry.split('---', 2)[1]
        self.assertIn('name: ask-jev\n', frontmatter)
        self.assertIn('approved project model-use policy', frontmatter)
        self.assertNotIn('disable-model-invocation', frontmatter)
        for path in root.rglob('*.md'):
            prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', path.read_text(), flags=re.M | re.S)
            self.assertNotIn('/Users/', prose)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
                if re.match(r'https?://|#|mailto:', target):
                    continue
                resolved = (path.parent / target.split('#')[0]).resolve()
                self.assertTrue(resolved.exists(), f'{path}: {target}')
                self.assertTrue(resolved.is_relative_to(root.resolve()), f'sibling dependency: {target}')
        api = (root / 'references/hosted-api.md').read_text()
        for rule in (ENDPOINT, 'Reject redirects', '120 seconds', '420 seconds', '30 seconds',
                     'certificate verification', 'shared', 'immediately before each send'):
            self.assertIn(rule, api)
        auth = (root / 'references/authorization.md').read_text()
        for rule in ('TypeSafe hosted Jev', 'unknown is not zero', 'at most six',
                     'Default substitution is none', 'root ledger', 'private'):
            self.assertIn(rule, auth)

    def test_frontmatter_and_internal_links(self):
        self.check_package(ROOT)

    def test_isolated_package_without_siblings(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / 'independent-package'
            shutil.copytree(ROOT, copied)
            self.check_package(copied)

    def test_synthetic_request_and_documented_syntax_check(self):
        api = (ROOT / 'references/hosted-api.md').read_text()
        sample = re.search(r'```json\n(.*?)\n```', api, re.S).group(1)
        self.assertEqual(json.loads(sample)['model'], 'jev-latest')
        # Execute the exact documented Python syntax check with synthetic content.
        import subprocess
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'request.json'
            path.write_text(sample)
            result = subprocess.run(['python3', '-c',
                'import json,sys; json.load(open(sys.argv[1], encoding="utf-8"))', str(path)],
                capture_output=True, check=True)
            self.assertEqual(result.stdout, b'')


if __name__ == '__main__':
    unittest.main()
