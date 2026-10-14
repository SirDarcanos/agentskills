"""Test-only rendition of the prose procedure; NEVER a hosted client/policy parser.

Resolved permission dictionaries are synthetic facts, not a policy format.
No network, environment/secret access, real timers or process effects exist here.
Passing these simulations is not evidence of real agent/runtime enforcement.
"""
import copy
import json
import math
from unittest.mock import Mock

ENDPOINT = 'https://api.typesafe.ai/v1/systemone'
MODEL = 'jev-latest'
VERSION = 'jev-1.13.0'


def grant():
    return dict(approved=True, provenance='synthetic approval', current=True,
                skill='ask-jev', provider='TypeSafe', endpoint=ENDPOINT,
                model=MODEL, resolution=VERSION, purpose='evidence-support',
                disclosure={'synthetic'}, cost_bound=1, currency='USD',
                fallback='none', retries=2, corrections=1, moving_alias=True)


def request():
    return dict(model=MODEL, state={'source': 'synthetic', 'fact': 'check passed'},
                questions={'decision': dict(type='choice', instructions='Assess fact.',
                                            criteria={'meets': 'Supported.',
                                                      'insufficient_data': 'Unknown.'})})


def response(payload=None, choice='meets'):
    payload = payload or request()
    answers = {}
    for key, question in payload['questions'].items():
        kind = question['type']
        if kind == 'choice':
            answers[key] = dict(type=kind, choice=choice, confidence=1,
                                probabilities={k: int(k == choice) for k in question['criteria']})
        elif kind == 'noul':
            answers[key] = dict(type=kind, noul=0.75)
        else:
            legend = {str(i): level for i, level in enumerate(question['criteria'])}
            answers[key] = dict(type=kind, score=1, legend=legend, confidence=1,
                                probabilities={k: int(k == '1') for k in legend})
    return json.dumps(dict(model=VERSION, answers=answers,
                           usage=dict(input_tokens=100, output_tokens=10)))


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate(raw, payload, version):
    """Test-only response contract rendition for all three primitive types."""
    try:
        result = json.loads(raw)
        if result.get('model') != version or not version or 'error' in result:
            return False
        if set(result['answers']) != set(payload['questions']):
            return False
        for key in ('input_tokens', 'output_tokens'):
            value = result['usage'][key]
            if type(value) is not int or value < 0:
                return False
        for key, question in payload['questions'].items():
            answer = result['answers'][key]
            kind = question['type']
            if answer['type'] != kind:
                return False
            if kind == 'noul':
                if not number(answer['noul']) or not 0 <= answer['noul'] <= 1:
                    return False
                continue
            criteria = question['criteria']
            options = criteria if kind == 'choice' else {str(i): x for i, x in enumerate(criteria)}
            probs = answer['probabilities']
            if set(probs) != set(options) or not all(number(x) and 0 <= x <= 1 for x in probs.values()):
                return False
            if abs(sum(probs.values()) - 1) > 0.01:
                return False
            if not number(answer['confidence']) or not 0 <= answer['confidence'] <= 1:
                return False
            if kind == 'choice':
                if answer['choice'] not in probs or probs[answer['choice']] != max(probs.values()):
                    return False
            elif kind == 'score':
                score = answer['score']
                if answer['legend'] != options or not number(score) or not 0 <= score <= len(options) - 1:
                    return False
                if abs(score - sum(int(k) * v for k, v in probs.items())) > 0.05:
                    return False
            else:
                return False
        return True
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


class Ledger:
    """Root allowance and outstanding reservations shared by simulated workers."""
    def __init__(self, calls=6, spend=6, retries=4, corrections=1):
        self.calls, self.spend, self.retries = calls, spend, retries
        self.corrections_remaining = corrections
        self.currency = 'USD'
        self.reserved_calls = self.reserved_spend = 0
        self.attempts = self.corrections = 0
        self.logical = {}  # assessment IDs persist across handoff/resume
        self.unknown_charges = 0


class Session:
    def __init__(self, ledger=None, assessment='one'):
        self.root = ledger if ledger is not None else Ledger()
        self.assessment = assessment
        self.payload = request()
        self.data_class = 'synthetic'
        self.credentials = Mock(return_value=True)  # presence only; never a key
        self.send = Mock(return_value=(200, response(), None))
        self.confirm = Mock()
        self.delay = Mock()
        self.reply = None

    def eligible(self, permission):
        r, p = self.root, permission
        return (isinstance(p, dict) and p.get('approved') is True
                and bool(p.get('provenance')) and p.get('current') is True
                and p.get('skill') == 'ask-jev' and p.get('provider') == 'TypeSafe'
                and p.get('endpoint') == ENDPOINT and p.get('model') == self.payload['model']
                and p.get('resolution') == VERSION
                and (p['model'] != MODEL or p.get('moving_alias') is True)
                and p.get('purpose') == 'evidence-support'
                and self.data_class in p.get('disclosure', set())
                and 1 <= len(self.payload['questions']) <= 4
                and p.get('currency') == r.currency and number(p.get('cost_bound'))
                and p['cost_bound'] >= 0 and number(r.spend)
                and r.spend - r.reserved_spend >= p['cost_bound']
                and type(r.calls) is int and r.calls > r.reserved_calls
                and type(p.get('retries')) is int and 0 <= p['retries'] <= 2
                and type(p.get('corrections')) is int and 0 <= p['corrections'] <= 1
                and type(r.retries) is int and r.retries >= 0
                and type(r.corrections_remaining) is int and r.corrections_remaining >= 0)

    def unavailable(self, permission, explicit, direct):
        if (explicit and direct) or (not explicit and permission.get('fallback') == 'direct'):
            return 'Agent assessment — Jev unavailable'
        if explicit:
            self.confirm('direct-fallback')
            return 'pending-fallback'
        return 'unavailable'

    def run(self, permission=None, explicit=False, restricted=False, suitable=True,
            corrected=False, direct=False, before_send=None):
        if not suitable:
            return 'direct-no-model'
        if permission is None and explicit and not restricted:
            permission = grant()  # synthetic resolved explicit scope/pricing
        if restricted or not self.eligible(permission):
            return 'no-call'
        r = self.root
        logical = r.logical.setdefault(self.assessment, {'initial': 0, 'correction': 0, 'attempts': 0})
        if ((not corrected and logical['initial'])
                or (corrected and (not logical['initial'] or logical['correction']
                                   or not permission['corrections'] or not r.corrections_remaining))):
            return 'no-call'
        if not self.credentials():
            return self.unavailable(permission, explicit, direct)
        for attempt in range(3):
            if before_send:
                before_send(permission, attempt)
            if (not self.eligible(permission) or logical['attempts'] >= 6
                    or (attempt and (attempt > permission['retries'] or r.retries <= 0))):
                return 'no-call'
            # Exclusive reservation + dispatch accounting; no concurrency in fixture.
            r.calls -= 1
            r.spend -= permission['cost_bound']
            r.attempts += 1
            logical['attempts'] += 1
            if attempt:
                r.retries -= 1
            else:
                logical['correction' if corrected else 'initial'] += 1
                if corrected:
                    r.corrections += 1
                    r.corrections_remaining -= 1
            try:
                status, raw, retry_after = self.send(ENDPOINT, copy.deepcopy(self.payload))
            except OSError:
                r.unknown_charges += 1
                return self.unavailable(permission, explicit, direct)
            if status == 200:
                if not validate(raw, self.payload, permission['resolution']):
                    r.unknown_charges += 1
                    return self.unavailable(permission, explicit, direct)
                self.reply = json.loads(raw)
                return 'complete'
            # No billing promise for errors: keep the worst-case charge.
            r.unknown_charges += 1
            if status not in (429, 529) or attempt == 2:
                return self.unavailable(permission, explicit, direct)
            delay = retry_after if retry_after is not None else 2 ** attempt
            if not number(delay) or not 0 <= delay <= 30:
                return self.unavailable(permission, explicit, direct)
            self.delay(delay)  # mock only, no real waiting
        raise AssertionError('unreachable')
