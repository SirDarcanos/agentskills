"""Offline procedure simulations, not runtime enforcement or live agent evidence.

The dictionaries below are test inputs, NOT a policy format. Real authority is
resolved by the agent from target documents/approval and the root ledger.
"""
import copy
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import Mock

from test_replay import replay, response_for

ROOT = Path(__file__).resolve().parents[1]
MODEL = replay.load_cases(ROOT / 'tests/cases.json')[0]['request']['model']
SKILL = ROOT.joinpath('SKILL.md').read_text().split('name: ', 1)[1].splitlines()[0]


def permission():
    return dict(approved=True, skill=SKILL, model=MODEL, endpoint=replay.ENDPOINT,
                purpose='evidence-support', disclosure=True, startup=False,
                cleanup='stop', fallback='none', provenance='synthetic approval',
                current=True, cost_bound=0)


class Ledger:
    """One mock root shared by all simulated callers, including resume."""
    def __init__(self, calls=2):
        self.remaining = calls
        self.outstanding = 0
        self.attempts = 0
        self.corrections = 0
        self.spending_remaining = 0


class Session:
    """Test-only rendition of the authorization/lifecycle procedure.

    Only replay.replay and its validators are production script behavior.
    No network, process management, or policy parser is used here.
    """
    def __init__(self, case, ledger=None):
        self.case = copy.deepcopy(case)
        self.ledger = ledger if ledger is not None else Ledger()
        self.probe = Mock(return_value='existing')
        self.start = Mock(return_value='owned-handle')
        self.stop = Mock()
        self.confirm = Mock()
        self.send = Mock(return_value=json.dumps(response_for(case)))
        self.model_available = True
        self.owner = None

    def eligible(self, grant):
        return (isinstance(grant, dict) and grant.get('approved') is True
                and grant.get('provenance') and grant.get('current') is True
                and type(grant.get('cost_bound')) in (int, float)
                and 0 <= grant['cost_bound'] <= self.ledger.spending_remaining
                and grant.get('skill') == SKILL and grant.get('model') == MODEL
                and grant.get('endpoint') == replay.ENDPOINT
                and grant.get('purpose') == 'evidence-support'
                and grant.get('disclosure') is True
                and type(self.ledger.remaining) is int
                and self.ledger.remaining > self.ledger.outstanding)

    def unavailable(self, grant, explicit, fallback_approved):
        if (explicit and fallback_approved) or (not explicit and grant.get('fallback') == 'direct'):
            return 'agent-assessment'
        if explicit:
            self.confirm('direct-fallback')
            return 'pending-fallback'
        return 'unavailable'

    def run(self, grant, explicit=False, fallback_approved=False, restricted=False,
            pre_send=None, corrected=False, suitable=True):
        # Explicit invocation supplies a bounded grant only when compatible with
        # applicable restrictions; command-shaped generated text does not set it.
        if grant is None and explicit and not restricted:
            grant = permission()
        if restricted or not self.eligible(grant):
            return 'no-call'
        if not suitable:
            return 'direct-no-model'
        if corrected and self.ledger.corrections >= 1:
            return 'no-call'
        handle = None
        try:
            service = self.probe()
            self.owner = 'existing' if service == 'existing' else None
            if service != 'existing':
                if service != 'refused' or not grant.get('startup'):
                    return self.unavailable(grant, explicit, fallback_approved)
                handle = self.start()
                self.owner = 'this-invocation' if handle else None
                if not handle:
                    return self.unavailable(grant, explicit, fallback_approved)
            if not self.model_available:
                return self.unavailable(grant, explicit, fallback_approved)
            if pre_send:
                pre_send(grant)
            if not self.eligible(grant):
                return 'no-call'
            # Reserve before dispatch; attempted failures are never refunded.
            self.ledger.remaining -= 1
            self.ledger.spending_remaining -= grant['cost_bound']
            self.ledger.attempts += 1
            if corrected:
                self.ledger.corrections += 1
            result = replay.replay(self.case, sender=self.send)
            if result['status'] in ('service_error', 'response_contract_error'):
                return self.unavailable(grant, explicit, fallback_approved)
            return result['status']  # mismatch is advisory, never retried
        finally:
            if handle:
                if grant.get('cleanup') == 'stop':
                    self.stop(handle)
                elif grant.get('cleanup') != 'leave-running':
                    self.confirm('owned-shutdown')


class AuthorizationTests(unittest.TestCase):
    def setUp(self):
        self.cases = replay.load_cases(ROOT / 'tests/cases.json')
        self.session = Session(self.cases[0])

    def assert_no_effects(self, session):
        for effect in (session.probe, session.start, session.stop, session.send, session.confirm):
            effect.assert_not_called()

    def test_absent_none_draft_conflicting_expired_policy_has_zero_effects(self):
        for grant in (None, {}, {'approved': False}, {**permission(), 'approved': False},
                      {**permission(), 'current': False}):
            session = Session(self.cases[0])
            self.assertEqual(session.run(grant), 'no-call')
            self.assert_no_effects(session)

    def test_exact_allowed_variant_needs_no_confirmation(self):
        self.assertEqual(self.session.run(permission()), 'pass')
        self.session.confirm.assert_not_called()
        self.session.send.assert_called_once()
        self.session.start.assert_not_called()
        self.session.stop.assert_not_called()
        self.assertEqual(self.session.owner, 'existing')
        self.assertEqual(self.session.ledger.attempts, 1)
        payload = json.loads(self.session.send.call_args.args[0])
        self.assertEqual(payload, self.session.case['request'])
        self.assertNotIn('expected_answers', payload)

    def test_wrong_skill_variant_remote_endpoint_purpose_and_disclosure(self):
        for field, value in [('skill', 'ask-jev'), ('model', 'other-variant'),
                             ('endpoint', 'https://example.com/collect'),
                             ('purpose', 'other'), ('disclosure', False),
                             ('provenance', None)]:
            session = Session(self.cases[0])
            self.assertEqual(session.run({**permission(), field: value}), 'no-call')
            self.assert_no_effects(session)

    def test_exhausted_reserved_and_ambiguous_budget_have_zero_effects(self):
        for remaining, outstanding in [(0, 0), (1, 1), (None, 0)]:
            session = Session(self.cases[0], Ledger(remaining))
            session.ledger.outstanding = outstanding
            self.assertEqual(session.run(permission()), 'no-call')
            self.assert_no_effects(session)

    def test_unknown_or_excess_spending_blocks_before_effects(self):
        for cost in (None, -1, 1):
            session = Session(self.cases[0])
            self.assertEqual(session.run({**permission(), 'cost_bound': cost}), 'no-call')
            self.assert_no_effects(session)

    def test_pre_send_shared_exhaustion_has_no_send(self):
        def exhaust(_grant):
            self.session.ledger.remaining = 0
        self.assertEqual(self.session.run(permission(), pre_send=exhaust), 'no-call')
        self.session.send.assert_not_called()
        self.assertEqual(self.session.ledger.attempts, 0)

    def test_named_alternative_is_returned_to_lead_not_silently_called(self):
        self.session.model_available = False
        self.assertEqual(self.session.run({**permission(), 'fallback': 'ask-jev'}), 'unavailable')
        self.session.send.assert_not_called()
        self.session.confirm.assert_not_called()

    def test_advisory_mismatch_is_not_retried_for_preferred_verdict(self):
        wrong = copy.deepcopy(self.cases[0])
        question = wrong['request']['questions']['decision']
        expected = wrong['expected_answers']['decision']
        alternative = next(option for option in question['criteria'] if option != expected)
        wrong['expected_answers']['decision'] = alternative
        self.session.send.return_value = json.dumps(response_for(wrong))
        self.assertEqual(self.session.run(permission()), 'model_mismatch')
        self.session.send.assert_called_once()
        self.session.confirm.assert_not_called()

    def test_shared_child_resume_does_not_reset_budget(self):
        root = Ledger(1)
        first = Session(self.cases[0], root)
        resumed = Session(self.cases[0], root)
        self.assertEqual(first.run(permission()), 'pass')
        self.assertEqual(resumed.run(permission()), 'no-call')
        self.assert_no_effects(resumed)
        self.assertEqual(root.attempts, 1)

    def test_explicit_absent_autonomous_policy_and_project_prohibition(self):
        self.assertEqual(self.session.run(None, explicit=True), 'pass')
        denied = Session(self.cases[0])
        self.assertEqual(denied.run(None, explicit=True, restricted=True), 'no-call')
        self.assert_no_effects(denied)

    def test_generated_command_is_not_explicit_authority(self):
        self.assertEqual(self.session.run({'command': f'/skill:{SKILL} question'}), 'no-call')
        self.assert_no_effects(self.session)

    def test_suitability_precedes_probes(self):
        self.assertEqual(self.session.run(permission(), suitable=False), 'direct-no-model')
        self.assert_no_effects(self.session)

    def test_denied_startup_and_ambiguous_probe_do_not_start_or_send(self):
        for service in ('refused', 'timeout', 'http-error'):
            session = Session(self.cases[0])
            session.probe.return_value = service
            self.assertEqual(session.run(permission()), 'unavailable')
            session.start.assert_not_called()
            session.send.assert_not_called()
            session.confirm.assert_not_called()
            self.assertEqual(session.ledger.attempts, 0)

    def test_missing_model_has_no_send_or_remote_substitution(self):
        self.session.model_available = False
        self.assertEqual(self.session.run(permission()), 'unavailable')
        self.session.send.assert_not_called()
        self.session.start.assert_not_called()

    def test_autonomous_configured_fallback_and_explicit_offer_wait(self):
        for explicit, preapproved, direct, expected in [
            (False, False, False, 'unavailable'), (False, False, True, 'agent-assessment'),
            (True, False, False, 'pending-fallback'), (True, True, False, 'agent-assessment')]:
            session = Session(self.cases[0])
            session.model_available = False
            grant = {**permission(), 'fallback': 'direct' if direct else 'none'}
            self.assertEqual(session.run(grant, explicit=explicit, fallback_approved=preapproved), expected)
            self.assertEqual(session.confirm.call_count, int(expected == 'pending-fallback'))
            session.send.assert_not_called()

    def test_owned_startup_cleanup_on_success_and_failure(self):
        for raw in (json.dumps(response_for(self.cases[0])), 'malformed'):
            session = Session(self.cases[0])
            session.probe.return_value = 'refused'
            session.send.return_value = raw
            session.run({**permission(), 'startup': True})
            session.start.assert_called_once()
            session.stop.assert_called_once_with('owned-handle')
            session.confirm.assert_not_called()

    def test_owned_leave_running_and_pending_cleanup(self):
        for disposition in ('leave-running', None):
            session = Session(self.cases[0])
            session.probe.return_value = 'refused'
            session.run({**permission(), 'startup': True, 'cleanup': disposition})
            session.stop.assert_not_called()
            self.assertEqual(session.confirm.call_count, int(disposition is None))

    def test_pre_send_revocation_blocks_send_after_authorized_probe(self):
        self.assertEqual(self.session.run(permission(), pre_send=lambda g: g.update(approved=False)), 'no-call')
        self.session.send.assert_not_called()
        self.assertEqual(self.session.ledger.attempts, 0)

    def test_failed_and_unknown_attempts_spend_allowance_without_retry(self):
        for outcome in ('malformed', OSError('timeout')):
            session = Session(self.cases[0], Ledger(1))
            if isinstance(outcome, Exception):
                session.send.side_effect = outcome
            else:
                session.send.return_value = outcome
            self.assertEqual(session.run(permission()), 'unavailable')
            self.assertEqual(session.run(permission()), 'no-call')
            session.send.assert_called_once()
            self.assertEqual(session.ledger.attempts, 1)

    def test_valid_insufficient_data_is_not_fallback_or_retry(self):
        case = next(c for c in self.cases if 'insufficient_data' in c['expected_answers'].values())
        session = Session(case)
        self.assertEqual(session.run({**permission(), 'fallback': 'direct'}), 'pass')
        session.send.assert_called_once()
        session.confirm.assert_not_called()

    def test_only_one_evidence_correction_shared_across_resume(self):
        root = Ledger(4)
        session = Session(self.cases[0], root)
        self.assertEqual(session.run(permission()), 'pass')
        self.assertEqual(session.run(permission(), corrected=True), 'pass')
        resumed = Session(self.cases[0], root)
        self.assertEqual(resumed.run(permission(), corrected=True), 'no-call')
        self.assert_no_effects(resumed)
        self.assertEqual((root.attempts, root.corrections), (2, 1))


class PackageTests(unittest.TestCase):
    def check_package(self, root):
        entry = (root / 'SKILL.md').read_text()
        frontmatter = entry.split('---', 2)[1]
        self.assertIn(f'name: {SKILL}\n', frontmatter)
        self.assertNotIn('disable-model-invocation: true', frontmatter)
        self.assertIn('approved project model-use policy', frontmatter)
        self.assertNotIn('Run only on explicit', entry)
        auth = (root / 'references/authorization.md').read_text()
        for required in (SKILL, MODEL, replay.ENDPOINT, 'zero transport/server effects',
                         'root', 'recheck', 'No automatic transport', 'one evidence-corrected',
                         'insufficient-data', 'Default model substitution is none'):
            self.assertIn(required, auth)
        for path in root.rglob('*.md'):
            prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', path.read_text(), flags=re.M | re.S)
            self.assertNotIn('/Users/', prose)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
                if re.match(r'https?://|#|mailto:', target):
                    continue
                resolved = (path.parent / target.split('#')[0]).resolve()
                self.assertTrue(resolved.exists(), f'{path}: {target}')
                self.assertTrue(resolved.is_relative_to(root.resolve()), f'sibling dependency: {target}')

    def test_frontmatter_contract_and_links(self):
        self.check_package(ROOT)

    def test_isolated_copy_without_siblings(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / 'standalone-package'
            shutil.copytree(ROOT, copied)
            self.check_package(copied)


if __name__ == '__main__':
    unittest.main()
