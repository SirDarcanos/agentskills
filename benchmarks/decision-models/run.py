#!/usr/bin/env python3
"""Validate 100 synthetic fixtures offline, or explicitly compare decision models."""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import statistics
import time
import urllib.error
import urllib.request

from cases import build_cases

MODELS = ("nimble", "clef", "clef-flash", "jev-latest", "jev-1.13.0")
LOCAL = "http://127.0.0.1:11434"
HOSTED = "https://api.typesafe.ai/v1/systemone"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_json(raw):
    def reject(value):
        raise ValueError("non-finite JSON constant")
    return json.loads(raw, parse_constant=reject)


def number(value, low, high):
    return type(value) in (int, float) and math.isfinite(value) and low <= value <= high


def text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_request(request):
    require(isinstance(request, dict) and set(request) == {"model", "state", "questions"}, "invalid request fields")
    require(request["model"] in MODELS, "unsupported model")
    require(isinstance(request["state"], (str, dict, list)), "invalid state")
    if isinstance(request["state"], str):
        require(text(request["state"]), "blank state")
    questions = request["questions"]
    require(isinstance(questions, dict) and 1 <= len(questions) <= 4, "invalid question count")
    for key, question in questions.items():
        require(text(key) and isinstance(question, dict) and text(question.get("instructions")), "invalid question")
        kind, criteria = question.get("type"), question.get("criteria")
        if kind == "choice":
            require(isinstance(criteria, dict) and 2 <= len(criteria) <= 26, "invalid choice options")
            require(all(text(k) and text(v) for k, v in criteria.items()), "invalid choice descriptions")
        elif kind == "score":
            # The common subset fits both Ollama and hosted Jev.
            require(isinstance(criteria, list) and 2 <= len(criteria) <= 10 and all(text(v) for v in criteria), "invalid score levels")
        elif kind == "noul":
            require(isinstance(criteria, dict) and set(criteria) == {"true", "false"} and all(text(v) for v in criteria.values()), "invalid noul criteria")
        else:
            raise ValueError("unknown question type")
    body = json.dumps(request, ensure_ascii=False, allow_nan=False).encode()
    require(len(body) <= 65536, "request exceeds common text body limit")
    return body


def request_for(case, model):
    # Explicitly select the only outbound fields: expected labels, category,
    # oracle source, and rationale never enter a request.
    request = {"model": model, "state": case["request"]["state"], "questions": case["request"]["questions"]}
    validate_request(request)
    return request


def validate_cases(cases):
    require(isinstance(cases, list) and len(cases) == 100, "expected exactly 100 cases")
    seen = set()
    for case in cases:
        require(text(case.get("id")) and case["id"] not in seen, "duplicate or invalid case ID")
        seen.add(case["id"])
        require(text(case.get("category")) and text(case.get("rationale")), "missing case provenance")
        require(case.get("label_source") in {"rule-evaluator", "authored-semantic-annotation"}, "invalid label source")
        request = request_for(case, "nimble")
        expected = case.get("expected_answers")
        require(isinstance(expected, dict) and set(expected) == set(request["questions"]), "gold answer coverage mismatch")
        for key, question in request["questions"].items():
            gold = expected[key]
            if question["type"] == "choice":
                require(isinstance(gold, str) and gold in question["criteria"], "invalid choice gold")
            elif question["type"] == "noul":
                require(type(gold) is bool, "invalid noul gold")
            else:
                require(type(gold) is int and 0 <= gold < len(question["criteria"]), "invalid score gold")
    require(len(Counter(c["category"] for c in cases)) == 10, "expected ten categories")
    require(set(Counter(c["category"] for c in cases).values()) == {10}, "expected ten cases per category")
    return cases


def validate_response(request, response):
    validate_request(request)
    require(isinstance(response, dict) and "error" not in response, "error or non-object response")
    model = response.get("model")
    if request["model"].startswith("jev-"):
        require(text(model) and model.startswith("jev-"), "invalid returned Jev model")
        if request["model"] != "jev-latest":
            require(model == request["model"], "pinned model mismatch")
    else:
        require(model == request["model"], "local model mismatch")
    usage = response.get("usage")
    require(isinstance(usage, dict) and all(type(usage.get(k)) is int and usage[k] >= 0 for k in ("input_tokens", "output_tokens")), "invalid usage")
    answers = response.get("answers")
    require(isinstance(answers, dict) and set(answers) == set(request["questions"]), "answer coverage mismatch")
    for key, question in request["questions"].items():
        answer = answers[key]
        kind = question["type"]
        require(isinstance(answer, dict) and answer.get("type") == kind, "answer type mismatch")
        if kind == "noul":
            require(number(answer.get("noul"), 0, 1), "invalid noul probability")
            continue
        criteria = question["criteria"]
        options = set(criteria) if kind == "choice" else {str(i) for i in range(len(criteria))}
        probabilities = answer.get("probabilities")
        require(isinstance(probabilities, dict) and set(probabilities) == options, "probability coverage mismatch")
        require(all(number(v, 0, 1) for v in probabilities.values()) and abs(sum(probabilities.values()) - 1) <= 0.01, "invalid distribution")
        require(number(answer.get("confidence"), 0, 1), "invalid confidence")
        if kind == "choice":
            selected = answer.get("choice")
            require(isinstance(selected, str) and selected in options, "unknown choice")
            require(max(probabilities.values()) - probabilities[selected] <= 0.0001, "choice contradicts distribution")
        else:
            require(answer.get("legend") == {str(i): level for i, level in enumerate(criteria)}, "score legend mismatch")
            require(number(answer.get("score"), 0, len(criteria) - 1), "invalid score")
            require(abs(answer["score"] - sum(int(i) * p for i, p in probabilities.items())) <= 0.05, "score contradicts distribution")
    return answers


def label_for(answer):
    if answer["type"] == "choice":
        probabilities = answer["probabilities"]
        maximum = max(probabilities.values())
        winners = [key for key, value in probabilities.items() if value == maximum]
        # Tie-selected choices still satisfy the API, but are not a unique gold
        # prediction. Report ties separately rather than crediting label order.
        return (answer["choice"], False) if len(winners) == 1 else (None, True)
    if answer["type"] == "noul":
        return (None, True) if answer["noul"] == 0.5 else (answer["noul"] > 0.5, False)
    probabilities = answer["probabilities"]
    maximum = max(probabilities.values())
    winners = [int(key) for key, value in probabilities.items() if value == maximum]
    return (winners[0], False) if len(winners) == 1 else (None, True)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, new_url):
        raise urllib.error.HTTPError(request.full_url, code, "redirect refused", headers, fp)


def transport(model):
    hosted = model.startswith("jev-")
    headers = {"Content-Type": "application/json"}
    if hosted:
        require(not urllib.request.getproxies().get("https"), "hosted HTTPS proxy requires separate approval")
        key = os.environ.get("TYPESAFE_API_KEY")
        require(bool(key), "TYPESAFE_API_KEY is not configured in this process")
        headers["Authorization"] = "Bearer " + key
        opener = urllib.request.build_opener(NoRedirect())
    else:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    endpoint = HOSTED if hosted else LOCAL + "/v1/systemone"

    def send(body):
        request = urllib.request.Request(endpoint, data=body, headers=headers)
        with opener.open(request, timeout=120 if hosted else 300) as response:
            raw = response.read(1024 * 1024 + 1)
        require(len(raw) <= 1024 * 1024, "response exceeds 1 MiB")
        return raw.decode()
    return send


def local_provenance(model):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    with opener.open(LOCAL + "/api/tags", timeout=5) as response:
        tags = parse_json(response.read(1024 * 1024 + 1))
    require(isinstance(tags, dict) and isinstance(tags.get("models"), list), "invalid local model list")
    matches = [item for item in tags["models"] if item.get("name") in {model, model + ":latest"}]
    require(len(matches) == 1, "exact local model is missing; finish its download first")
    item = matches[0]
    return {"name": item["name"], "digest": item.get("digest"), "details": item.get("details")}


def evaluate(case, model, sender):
    request = request_for(case, model)
    result = {"case": case["id"], "category": case["category"], "model": model,
              "timestamp_utc": datetime.now(timezone.utc).isoformat()}
    start = time.monotonic()
    try:
        raw = sender(validate_request(request))
    except urllib.error.HTTPError as exc:
        result.update(status="service_error", http_status=exc.code, usage="unknown")
        exc.close()
    except (OSError, urllib.error.URLError):
        result.update(status="service_error", error="network failure; request may have been processed", usage="unknown")
    except ValueError:
        result.update(status="response_contract_error", error="transport response constraint failed")
    else:
        try:
            response = parse_json(raw)
            answers = validate_response(request, response)
        except (ValueError, TypeError, UnicodeError):
            result.update(status="response_contract_error", error="response did not satisfy the contract")
        else:
            judgments = []
            for key, question in request["questions"].items():
                observed, tied = label_for(answers[key])
                expected = case["expected_answers"][key]
                judgment = {"question": key, "type": question["type"], "expected": expected,
                            "observed": observed, "tied": tied, "correct": not tied and observed == expected}
                if question["type"] == "score":
                    judgment["weighted_absolute_error"] = abs(answers[key]["score"] - expected)
                judgments.append(judgment)
            result.update(status="pass" if all(j["correct"] for j in judgments) else "model_mismatch",
                          returned_model=response["model"], usage=response["usage"], judgments=judgments,
                          answers=answers)
    result["elapsed_seconds"] = time.monotonic() - start
    return result


def summary(cases, results):
    categories = {}
    for name in sorted({case["category"] for case in cases}):
        rows = [row for row in results if row["category"] == name]
        valid = [row for row in rows if row["status"] in {"pass", "model_mismatch"}]
        categories[name] = {"planned": sum(c["category"] == name for c in cases), "attempted": len(rows),
                            "valid": len(valid), "correct_cases": sum(row["status"] == "pass" for row in valid)}
    valid = [row for row in results if row["status"] in {"pass", "model_mismatch"}]
    judgments = [j for row in valid for j in row["judgments"]]
    by_type = {}
    for kind in ("choice", "noul", "score"):
        rows = [j for j in judgments if j["type"] == kind]
        by_type[kind] = {"evaluated": len(rows), "correct": sum(j["correct"] for j in rows), "ties": sum(j["tied"] for j in rows)}
        if kind == "score" and rows:
            by_type[kind]["weighted_mae"] = statistics.mean(j["weighted_absolute_error"] for j in rows)
    durations = [row["elapsed_seconds"] for row in results]
    return {"planned_cases": len(cases), "planned_questions": sum(len(c["expected_answers"]) for c in cases),
            "attempted_cases": len(results), "not_run": len(cases) - len(results), "valid_cases": len(valid),
            "correct_cases": sum(row["status"] == "pass" for row in valid),
            "case_accuracy_on_valid_responses": sum(row["status"] == "pass" for row in valid) / len(valid) if valid else None,
            "statuses": dict(Counter(row["status"] for row in results)), "categories": categories, "question_types": by_type,
            "returned_models": sorted({row["returned_model"] for row in valid}),
            "latency_seconds": {"first": durations[0] if durations else None,
                                "median_all": statistics.median(durations) if durations else None,
                                "median_excluding_first": statistics.median(durations[1:]) if len(durations) > 1 else None},
            "known_usage": {key: sum(row["usage"][key] for row in valid) for key in ("input_tokens", "output_tokens")},
            "usage_unknown_cases": len(results) - len(valid)}


def write_private(path, value):
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as output:
        json.dump(value, output, indent=2, ensure_ascii=False, allow_nan=False)
        output.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models", nargs="+", choices=MODELS, default=["nimble", "clef", "clef-flash"])
    parser.add_argument("--live", action="store_true", help="explicitly send the corpus; offline by default")
    parser.add_argument("--allow-hosted", action="store_true", help="approve billable Jev requests containing synthetic fixtures")
    parser.add_argument("--record-dir", type=Path, help="explicitly retain requests/results in a NEW private directory outside the repo")
    parser.add_argument("--export-cases", type=Path, help="export legacy replay-compatible JSON for one selected model; offline only")
    args = parser.parse_args(argv)
    if len(set(args.models)) != len(args.models):
        parser.error("models must be unique")
    if args.record_dir and not args.live:
        parser.error("recording requires --live")
    if args.live and any(model.startswith("jev-") for model in args.models) and not args.allow_hosted:
        parser.error("Jev requires explicit --allow-hosted approval")
    if args.export_cases and (args.live or len(args.models) != 1):
        parser.error("export is offline and requires exactly one model")
    try:
        cases = validate_cases(build_cases())
        corpus_hash = hashlib.sha256(json.dumps(cases, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        if args.export_cases:
            export = {"version": 1, "cases": [{**case, "request": request_for(case, args.models[0]), "interpretation": case["rationale"]} for case in cases]}
            write_private(args.export_cases, export)
            print(f"Exported {len(cases)} cases; no network or credentials accessed")
            return 0
        if not args.live:
            print(json.dumps({"status": "offline_pass", "cases": len(cases), "questions": sum(len(c['expected_answers']) for c in cases),
                              "categories": dict(Counter(c["category"] for c in cases)), "corpus_sha256": corpus_hash,
                              "network": "not accessed", "credentials": "not accessed"}))
            return 0
        if args.record_dir:
            repository = Path(__file__).resolve().parents[2]
            require(not args.record_dir.resolve().is_relative_to(repository), "records must be outside the repository")
            args.record_dir.mkdir(mode=0o700, parents=True, exist_ok=False)
        failed = False
        for model in args.models:
            provenance = None
            try:
                sender = transport(model)
                if not model.startswith("jev-"):
                    provenance = local_provenance(model)
            except (ValueError, OSError, urllib.error.URLError):
                print(json.dumps({"model": model, "status": "setup_blocked", "detail": "Check credentials, proxy policy, or exact local model availability; no decision calls sent."}), flush=True)
                failed = True
                continue
            results = []
            for case in cases:
                result = evaluate(case, model, sender)
                results.append(result)
                # Print diagnosis, but neither complete evidence nor credentials.
                public = {k: v for k, v in result.items() if k != "answers"}
                print(json.dumps(public), flush=True)
                if args.record_dir:
                    write_private(args.record_dir / f"{model}-{case['id']}.json", {"request": request_for(case, model), "expected_answers": case["expected_answers"], "rationale": case["rationale"], "result": result})
                failed |= result["status"] != "pass"
                # No automatic retries, fallback, or continuation through an
                # availability/contract failure. Valid label mismatches continue.
                if result["status"] not in {"pass", "model_mismatch"}:
                    break
            report = {"model": model, "corpus_sha256": corpus_hash, "local_provenance": provenance, **summary(cases, results)}
            print(json.dumps({"summary": report}), flush=True)
            if args.record_dir:
                write_private(args.record_dir / f"{model}-summary.json", report)
        return int(failed)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"benchmark configuration error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
