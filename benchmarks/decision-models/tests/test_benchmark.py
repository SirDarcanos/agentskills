import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import cases
import run


def response_for(case, model="nimble"):
    answers = {}
    for key, question in case["request"]["questions"].items():
        gold = case["expected_answers"][key]
        kind = question["type"]
        if kind == "noul":
            answer = {"type": kind, "noul": 0.99 if gold else 0.01}
        elif kind == "choice":
            answer = {"type": kind, "choice": gold, "confidence": 1,
                      "probabilities": {option: int(option == gold) for option in question["criteria"]}}
        else:
            legend = {str(i): level for i, level in enumerate(question["criteria"])}
            answer = {"type": kind, "score": gold, "confidence": 1, "legend": legend,
                      "probabilities": {index: int(int(index) == gold) for index in legend}}
        answers[key] = answer
    return {"model": "jev-1.13.0" if model == "jev-latest" else model,
            "usage": {"input_tokens": 100, "output_tokens": 0}, "answers": answers}


class BenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.corpus = cases.build_cases()
        self.by_id = {case["id"]: case for case in self.corpus}
        self.case = self.corpus[0]

    def test_corpus_size_categories_question_types_and_unique_payloads(self):
        run.validate_cases(self.corpus)
        self.assertEqual(len(self.corpus), 100)
        self.assertEqual(sum(len(c["expected_answers"]) for c in self.corpus), 120)
        payloads = {json.dumps(c["request"], sort_keys=True) for c in self.corpus}
        self.assertEqual(len(payloads), 100)
        self.assertEqual({q["type"] for c in self.corpus for q in c["request"]["questions"].values()}, {"choice", "noul", "score"})
        self.assertEqual(cases.build_cases(), self.corpus)

    def test_gold_sequences_are_reviewable_independently_of_evaluators(self):
        expected = {
            "authorization-scope": ["authorized", "unauthorized", "insufficient_data", "insufficient_data", "insufficient_data", "insufficient_data", "insufficient_data", "authorized", "unauthorized", "authorized"],
            "policy-exceptions": ["eligible", "ineligible", "eligible", "ineligible", "eligible", "insufficient_data", "insufficient_data", "insufficient_data", "eligible", "eligible"],
            "revision-precedence": ["rejected", "rejected", "approved", "insufficient_data", "approved", "insufficient_data", "insufficient_data", "rejected", "rejected", "approved"],
            "negation-and-scope": [True, False, False, True, False, True, False, True, False, True],
            "evidence-support": ["supports", "contradicts", "insufficient_data", "contradicts", "supports", "insufficient_data", "insufficient_data", "insufficient_data", "supports", "contradicts"],
            "semantic-routing": ["billing", "technical", "account", "sales", "no_match", "insufficient_data", "technical", "billing", "sales", "account"],
            "untrusted-instructions": ["authorized", "unauthorized"] * 5,
            "conjunction-and-unknowns": ["ready", "blocked", "blocked", "blocked", "insufficient_data", "insufficient_data", "insufficient_data", "blocked", "insufficient_data", "blocked"],
            "ordinal-rubrics": [0, 0, 1, 1, 2, 2, 3, 3, 0, 2],
        }
        for category, labels in expected.items():
            actual = [next(iter(c["expected_answers"].values())) for c in self.corpus if c["category"] == category]
            self.assertEqual(actual, labels, category)
        mixed_gold = [
            ("allowed", "present", 0), ("denied", "present", 1),
            ("allowed", "absent", 2), ("denied", "absent", 3),
            ("insufficient_data", "present", 1), ("allowed", "insufficient_data", 3),
            ("denied", "insufficient_data", 0), ("insufficient_data", "absent", 2),
            ("allowed", "present", 3), ("denied", "absent", 1),
        ]
        for index, (access, receipt, urgency) in enumerate(mixed_gold, 1):
            self.assertEqual(self.by_id[f"independent-dimensions-{index:02d}"]["expected_answers"],
                             {"access": access, "receipt": receipt, "urgency": urgency})

    def test_oracle_scope_permutation_and_mutation_properties(self):
        records = [{"account": 42, "refund": "R1", "signer": "Mira"}]
        self.assertEqual(cases.authorization(records), "authorized")
        irrelevant = {"account": 43, "refund": "R1", "signer": "Noah"}
        self.assertEqual(cases.authorization(records + [irrelevant]), "authorized")
        records[0]["signer"] = "Noah"
        self.assertEqual(cases.authorization(records), "unauthorized")
        records.append({"account": 42, "refund": "R1", "signer": "Mira"})
        self.assertEqual(cases.authorization(records), cases.authorization(list(reversed(records))))
        self.assertEqual(cases.authorization(records), "insufficient_data")
        self.assertEqual(cases.readiness([False, None, True]), "blocked")
        self.assertEqual(cases.readiness([True, None, True]), "insufficient_data")
        self.assertEqual(cases.urgency(True, False, False), 3)
        self.assertEqual(cases.urgency(False, False, True), 1)

    def test_all_gold_responses_validate_for_all_models(self):
        for model in run.MODELS:
            for case in self.corpus:
                with self.subTest(model=model, case=case["id"]):
                    request = run.request_for(case, model)
                    answers = run.validate_response(request, response_for(case, model))
                    self.assertTrue(all(run.label_for(answers[key])[0] == target for key, target in case["expected_answers"].items()))

    def test_gold_and_rationales_are_never_sent(self):
        sent = []
        def sender(body):
            sent.append(json.loads(body))
            return json.dumps(response_for(self.case))
        result = run.evaluate(self.case, "nimble", sender)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(set(sent[0]), {"model", "state", "questions"})
        self.assertNotIn("expected_answers", sent[0])
        self.assertNotIn("rationale", sent[0])
        self.assertEqual(sent[0]["state"], self.case["request"]["state"])

    def test_offline_never_reads_credentials_or_network(self):
        class UnavailableEnvironment(dict):
            def get(self, key, default=None):
                if key == "TYPESAFE_API_KEY":
                    raise AssertionError("offline credential access")
                # argparse/gettext legitimately consult locale variables.
                return super().get(key, default)
        with patch.object(run.os, "environ", UnavailableEnvironment()), patch.object(run, "transport") as network, patch.object(run, "local_provenance") as probe, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(run.main(["--models", "jev-latest"]), 0)
            network.assert_not_called()
            probe.assert_not_called()

    def test_hosted_and_recording_require_explicit_flags(self):
        for args in (["--live", "--models", "jev-latest"], ["--record-dir", "/tmp/no-records"], ["--export-cases", "/tmp/no-export", "--live"], ["--models", "nimble", "nimble"]):
            with contextlib.redirect_stderr(io.StringIO()), patch.object(run, "transport") as network, self.assertRaises(SystemExit):
                run.main(args)
            network.assert_not_called()

    def test_bad_gold_and_duplicate_cases_are_rejected(self):
        for mutate in (lambda c: c[0]["expected_answers"].update(decision="invented"), lambda c: c[1].update(id=c[0]["id"]), lambda c: c[0].pop("rationale")):
            corpus = copy.deepcopy(self.corpus)
            mutate(corpus)
            with self.assertRaises(ValueError):
                run.validate_cases(corpus)

    def test_malformed_envelopes_and_answers_are_rejected(self):
        request = run.request_for(self.case, "nimble")
        for mutate in (
            lambda r: r.update(model="clef"), lambda r: r.pop("usage"),
            lambda r: r["usage"].update(input_tokens=True), lambda r: r["usage"].update(output_tokens=-1),
            lambda r: r["answers"].update(extra={}), lambda r: r["answers"]["decision"].update(type="score"),
            lambda r: r["answers"]["decision"].update(confidence=float("nan")),
            lambda r: r["answers"]["decision"].update(choice="unauthorized"),
            lambda r: r["answers"]["decision"]["probabilities"].update(authorized=0.5),
        ):
            response = response_for(self.case)
            mutate(response)
            with self.assertRaises(ValueError):
                run.validate_response(request, response)
        with self.assertRaises(ValueError):
            run.parse_json('{"x": NaN}')

    def test_noul_and_score_contracts_and_ties(self):
        for case_id, question, mutate in (
            ("negation-and-scope-01", "refund_requested", lambda a: a.update(noul=True)),
            ("ordinal-rubrics-01", "urgency", lambda a: a.update(score=True)),
            ("ordinal-rubrics-01", "urgency", lambda a: a["legend"].update({"0": "wrong"})),
            ("ordinal-rubrics-01", "urgency", lambda a: a.update(score=2)),
        ):
            case = self.by_id[case_id]
            response = response_for(case)
            mutate(response["answers"][question])
            with self.assertRaises(ValueError):
                run.validate_response(run.request_for(case, "nimble"), response)
        self.assertEqual(run.label_for({"type": "noul", "noul": 0.5}), (None, True))
        self.assertEqual(run.label_for({"type": "choice", "choice": "a", "probabilities": {"a": 0.5, "b": 0.5}}), (None, True))
        self.assertEqual(run.label_for({"type": "score", "probabilities": {"0": 0.5, "1": 0.5}}), (None, True))

    def test_label_mismatch_is_not_an_api_failure(self):
        response = response_for(self.case)
        response["answers"]["decision"].update(choice="unauthorized", probabilities={"authorized": 0, "unauthorized": 1, "insufficient_data": 0})
        result = run.evaluate(self.case, "nimble", lambda body: json.dumps(response))
        self.assertEqual(result["status"], "model_mismatch")
        self.assertEqual(result["judgments"][0]["observed"], "unauthorized")

    def test_transport_errors_are_redacted_and_not_retried(self):
        body = io.BytesIO(b'private error body')
        error = urllib.error.HTTPError(run.HOSTED, 429, "sensitive", {}, body)
        with patch.object(run, "validate_request", wraps=run.validate_request):
            sender = unittest.mock.Mock(side_effect=error)
            result = run.evaluate(self.case, "jev-latest", sender)
        self.assertEqual(result["status"], "service_error")
        self.assertEqual(result["http_status"], 429)
        self.assertEqual(result["usage"], "unknown")
        self.assertNotIn("sensitive", json.dumps(result))
        sender.assert_called_once()
        self.assertTrue(body.closed)
        self.assertEqual(run.evaluate(self.case, "nimble", lambda body: "not json")["status"], "response_contract_error")

    def test_model_run_stops_after_service_failure_and_reports_not_run(self):
        with patch.object(run, "transport", return_value=lambda body: "not json"), patch.object(run, "local_provenance", return_value={}), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(run.main(["--live", "--models", "nimble"]), 1)
        rows = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[-1]["summary"]["attempted_cases"], 1)
        self.assertEqual(rows[-1]["summary"]["not_run"], 99)
        self.assertIsNone(rows[-1]["summary"]["case_accuracy_on_valid_responses"])

    def test_local_transport_has_no_auth_and_ignores_proxies(self):
        with patch.object(run.urllib.request, "build_opener") as build:
            build.return_value.open.return_value.__enter__.return_value.read.return_value = b'{}'
            self.assertEqual(run.transport("clef")(b'{}'), '{}')
            proxy, redirect = build.call_args.args
            self.assertEqual(proxy.proxies, {})
            self.assertIsInstance(redirect, run.NoRedirect)
            request = build.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, run.LOCAL + "/v1/systemone")
            self.assertNotIn("Authorization", request.headers)

    def test_hosted_auth_proxy_and_redirect_boundaries(self):
        with patch.dict(run.os.environ, {"TYPESAFE_API_KEY": "synthetic-test-key"}), patch.object(run.urllib.request, "getproxies", return_value={}), patch.object(run.urllib.request, "build_opener") as build:
            build.return_value.open.return_value.__enter__.return_value.read.return_value = b'{}'
            self.assertEqual(run.transport("jev-latest")(b'{}'), '{}')
            request = build.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, run.HOSTED)
            self.assertEqual(request.headers["Authorization"], "Bearer synthetic-test-key")
            self.assertEqual(build.return_value.open.call_args.kwargs["timeout"], 120)
        with patch.object(run.urllib.request, "getproxies", return_value={"https": "https://proxy.invalid"}), self.assertRaises(ValueError):
            run.transport("jev-latest")
        with self.assertRaises(urllib.error.HTTPError) as caught:
            run.NoRedirect().redirect_request(urllib.request.Request(run.HOSTED), None, 302, "redirect", {}, "https://example.com/collect")
        caught.exception.close()

    def test_summary_case_question_denominators_and_score_mae(self):
        case = self.by_id["independent-dimensions-01"]
        good = run.evaluate(case, "nimble", lambda body: json.dumps(response_for(case)))
        response = response_for(case)
        response["answers"]["receipt"].update(choice="absent", probabilities={"present": 0, "absent": 1, "insufficient_data": 0})
        bad = run.evaluate(case, "nimble", lambda body: json.dumps(response))
        report = run.summary([case, case], [good, bad])
        self.assertEqual(report["correct_cases"], 1)
        self.assertEqual(report["case_accuracy_on_valid_responses"], 0.5)
        self.assertEqual(report["question_types"]["choice"]["correct"], 3)
        self.assertEqual(report["question_types"]["score"]["weighted_mae"], 0)

    def test_export_is_offline_and_compatible_with_existing_replays(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixtures.json"
            with patch.object(run, "transport") as network, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(run.main(["--models", "nimble", "--export-cases", str(target)]), 0)
                network.assert_not_called()
            spec = importlib.util.spec_from_file_location("nimble_replay", ROOT.parents[1] / "models/ask-nimble/scripts/replay.py")
            legacy = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(legacy)
            self.assertEqual(len(legacy.load_cases(target)), 100)
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                run.main(["--models", "nimble", "--export-cases", str(target)])


if __name__ == "__main__":
    unittest.main()
