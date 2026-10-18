import base64
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
    return {"model": replay.MODEL, "answers": answers, "usage": {"input_tokens": 100, "output_tokens": 0}}


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
        response["answers"]["decision"]["probabilities"] = {"authorized": 0, "unauthorized": 1, "insufficient_data": 0}
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
        for value in [True, float("nan"), float("inf"), -0.1, 1.1, "0.9", None, 10**400, -(10**400)]:
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

    def test_response_model_usage_and_choice_consistency(self):
        for change in [
            lambda r: r.update(model="other"),
            lambda r: r.pop("model"),
            lambda r: r.pop("usage"),
            lambda r: r["usage"].update(input_tokens=True),
            lambda r: r["usage"].update(output_tokens=-1),
            lambda r: r["answers"]["decision"].update(choice="unauthorized"),
        ]:
            response = copy.deepcopy(self.response)
            change(response)
            with self.assertRaises(ValueError):
                replay.validate_response(self.request, response)

    def test_exact_model_is_required(self):
        for model in ("clef", "clef-flash", "nimble", "jev-latest", "pplx-decider:cloud",
                      "pplx-decider:27b", "pplx-decider:latest", "pplx-decider:27b-q4_K_M"):
            request = copy.deepcopy(self.request)
            request["model"] = model
            with self.assertRaises(ValueError):
                replay.validate_request(request)

    def test_image_shape_encoding_and_body_limits(self):
        request = copy.deepcopy(self.request)
        # Synthetic signatures exercise encoding only, not image decoding or vision.
        for data in (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff", b"RIFFxxxxWEBP"):
            request["images"] = [base64.b64encode(data).decode("ascii")]
            self.assertTrue(replay.validate_request(request))
        for images in ("not an array", [True], [""], ["https://example.com/image.png"],
                       ["data:image/png;base64,AAAA"], ["!!!!"], ["dGV4dA=="]):
            request["images"] = images
            with self.assertRaises(ValueError):
                replay.validate_request(request)
        request["images"] = [base64.b64encode(b"\x89PNG\r\n\x1a\n").decode("ascii")]
        request["state"] = "x" * 65536
        with self.assertRaisesRegex(ValueError, "text/schema"):
            replay.validate_request(request)
        request["state"] = "Compact evidence"
        for images in ([base64.b64encode(b"\x89PNG\r\n\x1a\n").decode("ascii")] * 5,
                       [base64.b64encode(b"\x89PNG\r\n\x1a\n" + b"x" * replay.MAX_IMAGE_BYTES).decode("ascii")]):
            request["images"] = images
            with self.assertRaises(ValueError):
                replay.validate_request(request)

    def test_request_limits_and_types(self):
        for change in [
            lambda r: r.update(model="other"),
            lambda r: r.update(state=" "),
            lambda r: r.update(videos=[]),
            lambda r: r.update(keep_alive=True),
            lambda r: r.update(state="x" * 65536),
            lambda r: r.update(questions={}),
            lambda r: r.update(questions={str(i): copy.deepcopy(r["questions"]["decision"]) for i in range(5)}),
            lambda r: r["questions"]["decision"].update(instructions=""),
        ]:
            request = copy.deepcopy(self.request)
            change(request)
            with self.assertRaises(ValueError):
                replay.validate_request(request)

    def test_score_level_api_boundary_and_choice_package_boundary(self):
        for kind, valid, invalid in (("score", 10, 11), ("choice", 26, 27)):
            request = copy.deepcopy(self.request)
            question = request["questions"]["decision"]
            question["type"] = kind
            for count, accepted in ((valid, True), (invalid, False), (1, False)):
                question["criteria"] = ([f"Level {i}" for i in range(count)] if kind == "score"
                                        else {f"option{i}": f"Category {i}" for i in range(count)})
                if accepted:
                    self.assertTrue(replay.validate_request(request))
                else:
                    with self.assertRaises(ValueError):
                        replay.validate_request(request)

    def test_duplicate_keys_and_nonfinite_json_are_rejected(self):
        for raw in ('{"model":"other","model":"pplx-decider"}',
                    '{"answers":{"x":{},"x":{}}}', '{"state":NaN}',
                    '{"confidence":1e400}', '{"confidence":-1e400}'):
            with self.assertRaises(ValueError):
                replay.parse_json(raw)

    def test_tied_choice_is_valid_but_not_a_unique_fixture_win(self):
        response = copy.deepcopy(self.response)
        response["answers"]["decision"].update(
            choice="authorized", confidence=0,
            probabilities={"authorized": 0.5, "unauthorized": 0.5, "insufficient_data": 0})
        answers = replay.validate_response(self.request, response)
        self.assertFalse(replay.matches(answers, self.case["expected_answers"]))

    def test_partial_mixed_batch_is_never_interpreted(self):
        case = self.cases[-1]
        response = response_for(case)
        response["answers"].pop("urgency")
        record = replay.replay(case, sender=lambda body: json.dumps(response))
        self.assertEqual(record["status"], "response_contract_error")

    def test_saved_request_validation_and_invalid_cli_are_offline(self):
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            request.write_text(json.dumps(self.request))
            with patch.object(replay, "send_local") as send, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(replay.main(["--request", str(request)]), 0)
                send.assert_not_called()
            for args in (["--response", str(request)], ["--request", str(request), "--live"],
                         ["--record-dir", str(Path(directory) / "records")]):
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    replay.main(args)

    def test_oversized_integers_have_explicit_failure_results(self):
        cases_and_fields = [(self.case, "decision", "confidence"),
                            (self.case, "decision", "probability"),
                            (self.cases[-1], "refund_requested", "noul"),
                            (self.cases[-1], "urgency", "score")]
        for case, key, field in cases_and_fields:
            with self.subTest(field=field):
                response = response_for(case)
                if field == "probability":
                    response["answers"][key]["probabilities"]["authorized"] = 10**400
                else:
                    response["answers"][key][field] = 10**400
                record = replay.replay(case, sender=lambda body: json.dumps(response))
                self.assertEqual(record["status"], "response_contract_error")
                self.assertIn("raw_response", record)
        with tempfile.TemporaryDirectory() as directory:
            request_path = Path(directory) / "request.json"
            response_path = Path(directory) / "response.json"
            request_path.write_text(json.dumps(self.request))
            response = copy.deepcopy(self.response)
            response["answers"]["decision"]["confidence"] = 10**400
            response_path.write_text(json.dumps(response))
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                replay.main(["--request", str(request_path), "--response", str(response_path)])
            self.assertEqual(caught.exception.code, 2)
            request = copy.deepcopy(self.request)
            request["keep_alive"] = 10**400
            request_path.write_text(json.dumps(request))
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                replay.main(["--request", str(request_path)])
            self.assertEqual(caught.exception.code, 2)

    def test_numeric_parse_failures_record_all_cases_without_network(self):
        original_replay = replay.replay
        for token in ("1e400", "-1e400"):
            with self.subTest(token=token), tempfile.TemporaryDirectory() as directory:
                records = Path(directory) / "records"
                def malformed_record(case):
                    raw = json.dumps(response_for(case)).replace('"confidence": 1', '"confidence": ' + token)
                    return original_replay(case, sender=lambda body: raw)
                with patch.object(replay, "replay", side_effect=malformed_record), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(replay.main(["--live", "--record-dir", str(records)]), 1)
                self.assertEqual(len(list(records.glob("*.json"))), len(self.cases))
                for path in records.glob("*.json"):
                    record = replay.parse_json(path.read_text())
                    self.assertEqual(record["status"], "response_contract_error")
                    self.assertIn(token, record["raw_response"])
                    self.assertNotIn("response", record)

    def test_json_nesting_boundary_counts_containers_not_strings(self):
        depth = replay.MAX_JSON_DEPTH
        self.assertIsInstance(replay.parse_json("[" * depth + "0" + "]" * depth), list)
        with self.assertRaisesRegex(ValueError, "nesting"):
            replay.parse_json("[" * (depth + 1) + "0" + "]" * (depth + 1))
        self.assertEqual(replay.parse_json(json.dumps("[" * 10000)), "[" * 10000)
        request = copy.deepcopy(self.request)
        request["state"] = replay.parse_json("[" * depth + "0" + "]" * depth)
        with self.assertRaisesRegex(ValueError, "nesting"):
            replay.validate_request(request)
        response = copy.deepcopy(self.response)
        response["extra"] = request["state"]
        with self.assertRaisesRegex(ValueError, "nesting"):
            replay.validate_response(self.request, response)
        record = replay.replay(self.case, sender=lambda body: json.dumps(response))
        self.assertEqual(record["status"], "response_contract_error")
        self.assertNotIn("response", record)

    def test_nested_json_has_explicit_failure_outcomes(self):
        raw = "[" * 10000 + "0" + "]" * 10000
        # Decoder depth differs across Python versions; package depth does not.
        record = replay.replay(self.case, sender=lambda body: raw)
        self.assertEqual(record["status"], "response_contract_error")
        self.assertEqual(record["raw_response"], raw)
        self.assertNotIn("response", record)
        with patch.object(replay.json, "loads", side_effect=RecursionError("parser depth")):
            record = replay.replay(self.case, sender=lambda body: raw)
            self.assertEqual(record["status"], "response_contract_error")
            self.assertEqual(record["raw_response"], raw)
            self.assertNotIn("response", record)
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            response = Path(directory) / "response.json"
            request.write_text(json.dumps(self.request))
            response.write_text(raw)
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                replay.main(["--request", str(request), "--response", str(response)])
            self.assertEqual(caught.exception.code, 2)
        original_replay = replay.replay
        with tempfile.TemporaryDirectory() as directory:
            records = Path(directory) / "records"
            with patch.object(replay, "replay", side_effect=lambda case: original_replay(case, sender=lambda body: raw)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(replay.main(["--live", "--record-dir", str(records)]), 1)
            self.assertEqual(len(list(records.glob("*.json"))), len(self.cases))
            for path in records.glob("*.json"):
                self.assertEqual(replay.parse_json(path.read_text())["status"], "response_contract_error")

    def test_unknown_question_fields_are_rejected(self):
        request = copy.deepcopy(self.request)
        request["questions"]["decision"]["temperature"] = 0
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
