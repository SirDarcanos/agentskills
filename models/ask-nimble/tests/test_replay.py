import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("replay", ROOT / "scripts" / "replay.py")
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


def response_for(case):
    answers = {}
    for key, question in case["request"]["questions"].items():
        target = case["expected_answers"][key]
        kind = question["type"]
        if kind == "noul":
            answers[key] = {"type": kind, "noul": 0.99 if target else 0.01}
        elif kind == "choice":
            answers[key] = {"type": kind, "choice": target, "confidence": 1,
                            "probabilities": {k: int(k == target) for k in question["criteria"]}}
        else:
            legend = {str(i): level for i, level in enumerate(question["criteria"])}
            answers[key] = {"type": kind, "score": target, "confidence": 1, "legend": legend,
                            "probabilities": {k: int(int(k) == target) for k in legend}}
    return {"model": "nimble", "answers": answers}


class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.cases = replay.load_cases(ROOT / "tests" / "cases.json")
        self.case = self.cases[0]
        self.request = self.case["request"]
        self.response = response_for(self.case)

    def test_offline_default_never_calls_server(self):
        with patch.object(replay, "replay") as call, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(replay.main([]), 0)
            call.assert_not_called()

    def test_all_fixture_types_and_expected_labels(self):
        for case in self.cases:
            with self.subTest(case=case["id"]):
                answers = replay.validate_response(case["request"], response_for(case))
                self.assertTrue(replay.matches(answers, case["expected_answers"]))

    def test_expected_labels_are_not_sent(self):
        sent = []
        def sender(body):
            sent.append(json.loads(body))
            return json.dumps(self.response)
        record = replay.replay(self.case, sender=sender)
        self.assertEqual(record["status"], "pass")
        self.assertEqual(sent, [self.request])
        self.assertNotIn("expected_answers", sent[0])

    def test_mismatch_is_distinct_from_contract_error(self):
        response = copy.deepcopy(self.response)
        response["answers"]["decision"]["choice"] = "unauthorized"
        record = replay.replay(self.case, sender=lambda body: json.dumps(response))
        self.assertEqual(record["status"], "model_mismatch")

    def test_malformed_and_error_responses(self):
        for raw in ["not json", "[]", '{"answers":{}}', '{"answers":NaN}']:
            with self.subTest(raw=raw):
                self.assertEqual(replay.replay(self.case, sender=lambda body: raw)["status"], "response_contract_error")

    def test_service_failure(self):
        def sender(body):
            raise urllib.error.URLError("connection refused")
        self.assertEqual(replay.replay(self.case, sender=sender)["status"], "service_error")
        record = replay.replay(self.case, sender=lambda body: '{"error":"missing model"}')
        self.assertEqual(record["status"], "service_error")
        body = io.BytesIO(b'error body')
        error = urllib.error.HTTPError(replay.ENDPOINT, 500, "failure", {}, body)
        def http_failure(payload):
            raise error
        self.assertEqual(replay.replay(self.case, sender=http_failure)["status"], "service_error")
        self.assertTrue(body.closed)

    def test_reject_bad_probabilities_and_confidence(self):
        for value in [True, float("nan"), float("inf"), -0.1, 1.1, "0.9", None]:
            for field in ["probability", "confidence"]:
                with self.subTest(value=value, field=field):
                    response = copy.deepcopy(self.response)
                    answer = response["answers"]["decision"]
                    if field == "probability":
                        answer["probabilities"]["authorized"] = value
                    else:
                        answer["confidence"] = value
                    with self.assertRaises(ValueError):
                        replay.validate_response(self.request, response)

    def test_reject_missing_extra_mistyped_and_unknown_answers(self):
        changes = [
            lambda r: r["answers"].pop("decision"),
            lambda r: r["answers"].update(extra={}),
            lambda r: r["answers"]["decision"].update(type="score"),
            lambda r: r["answers"]["decision"].update(choice="other"),
            lambda r: r["answers"]["decision"]["probabilities"].pop("unauthorized"),
            lambda r: r["answers"]["decision"]["probabilities"].update(unauthorized=0.5),
        ]
        for change in changes:
            response = copy.deepcopy(self.response)
            change(response)
            with self.assertRaises(ValueError):
                replay.validate_response(self.request, response)

    def test_score_and_noul_contracts(self):
        case = self.cases[-1]
        changes = [
            lambda r: r["answers"]["urgency"].update(score=1),
            lambda r: r["answers"]["urgency"].update(score=True),
            lambda r: r["answers"]["urgency"]["legend"].update({"0": "Wrong level"}),
            lambda r: r["answers"]["refund_requested"].update(noul=True),
            lambda r: r["answers"]["refund_requested"].update(noul=-0.1),
        ]
        for change in changes:
            response = response_for(case)
            change(response)
            with self.assertRaises(ValueError):
                replay.validate_response(case["request"], response)

    def test_request_limits_and_types(self):
        for change in [
            lambda r: r.update(model="other"),
            lambda r: r.update(state="x" * 65536),
            lambda r: r.update(questions={}),
            lambda r: r.update(questions={str(i): copy.deepcopy(r["questions"]["decision"]) for i in range(5)}),
            lambda r: r["questions"]["decision"].update(instructions=""),
        ]:
            request = copy.deepcopy(self.request)
            change(request)
            with self.assertRaises(ValueError):
                replay.validate_request(request)

    def test_live_recording_is_opt_in_and_preserves_details(self):
        with tempfile.TemporaryDirectory() as directory:
            records = Path(directory) / "records"
            results = {case["id"]: replay_record(case) for case in self.cases}
            with patch.object(replay, "replay", side_effect=lambda c: results[c["id"]]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(replay.main(["--live", "--record-dir", str(records)]), 0)
            files = list(records.glob("*.json"))
            self.assertEqual(len(files), len(self.cases))
            saved = json.loads((records / "authorized.json").read_text())
            for key in ["request", "response", "expected_answers", "interpretation", "timestamp_utc", "elapsed_seconds"]:
                self.assertIn(key, saved)
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                replay.main(["--live", "--record-dir", str(records)])

    def test_transport_ignores_proxies_and_uses_loopback(self):
        with patch.object(replay.urllib.request, "build_opener") as build:
            build.return_value.open.return_value.__enter__.return_value.read.return_value = b'{}'
            self.assertEqual(replay.send_local(b'{}'), '{}')
            proxy_handler, redirect_handler = build.call_args.args
            self.assertEqual(proxy_handler.proxies, {})
            self.assertIsInstance(redirect_handler, replay.NoRedirect)
            request = build.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, replay.ENDPOINT)

    def test_redirects_are_refused(self):
        with self.assertRaises(urllib.error.HTTPError) as caught:
            replay.NoRedirect().redirect_request(
                replay.urllib.request.Request(replay.ENDPOINT), None, 302,
                "redirect", {}, "https://example.com/collect"
            )
        caught.exception.close()

    def test_saved_response_validation_is_offline(self):
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            response = Path(directory) / "response.json"
            request.write_text(json.dumps(self.request))
            response.write_text(json.dumps(self.response))
            with patch.object(replay, "send_local") as send, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(replay.main(["--request", str(request), "--response", str(response)]), 0)
                send.assert_not_called()


def replay_record(case):
    return replay.replay(case, sender=lambda body: json.dumps(response_for(case)))


if __name__ == "__main__":
    unittest.main()
