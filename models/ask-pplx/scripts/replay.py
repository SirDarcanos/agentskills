#!/usr/bin/env python3
"""Offline contract checks or explicitly opted-in local Pplx regression replay."""

import argparse
import base64
import binascii
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
import time
import urllib.error
import urllib.request

ENDPOINT = "http://127.0.0.1:11434/v1/systemone"
MODEL = "pplx-decider"
DEFAULT_CASES = Path(__file__).resolve().parent.parent / "tests" / "cases.json"
MAX_IMAGES = 4
MAX_IMAGE_BYTES = 4 * 1024 * 1024
TEXT_LIMIT = 64 * 1024
BODY_LIMIT = 32 * 1024 * 1024
MAX_JSON_DEPTH = 64


def parse_json(text):
    def reject_constant(value):
        raise ValueError(f"non-finite JSON constant: {value}")
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    def finite_float(value):
        parsed = float(value)
        require(math.isfinite(parsed), "non-finite JSON number")
        return parsed
    try:
        value = json.loads(text, parse_constant=reject_constant, parse_float=finite_float,
                           object_pairs_hook=unique_object)
        validate_nesting(value)
        return value
    except RecursionError as exc:
        raise ValueError("JSON nesting exceeds parser limits") from exc


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_nesting(value):
    # Count object/array containers, including the root, without recursion.
    # This also protects pretty-printed error recording on Python versions
    # whose JSON decoder accepts more depth than the encoder can serialize.
    pending = [(value, 0)]
    while pending:
        current, depth = pending.pop()
        if isinstance(current, (dict, list)):
            depth += 1
            require(depth <= MAX_JSON_DEPTH, "JSON nesting exceeds 64 containers")
            children = current.values() if isinstance(current, dict) else current
            pending.extend((child, depth) for child in children)


def finite_number(value):
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def number(value, low, high):
    return finite_number(value) and low <= value <= high


def description(value):
    return isinstance(value, str) and bool(value.strip())


def validate_request(request):
    require(isinstance(request, dict), "request must be an object")
    validate_nesting(request)
    require(request.get("model") == MODEL, f"model must be {MODEL}")
    require(set(request) <= {"model", "state", "questions", "images", "keep_alive"}, "unsupported request fields")
    require(isinstance(request.get("state"), (str, dict, list)), "state must be text, object, or array")
    if isinstance(request.get("state"), str):
        require(description(request["state"]), "state must not be blank")
    if "keep_alive" in request:
        keep_alive = request["keep_alive"]
        require(description(keep_alive) or finite_number(keep_alive), "invalid keep_alive")
    images = request.get("images", [])
    require(isinstance(images, list) and len(images) <= MAX_IMAGES, "expected at most four images")
    for image in images:
        require(description(image), "image must be raw base64")
        require(len(image) <= 4 * ((MAX_IMAGE_BYTES + 2) // 3), "encoded image exceeds package limit")
        try:
            decoded = base64.b64decode(image, validate=True)
        except (ValueError, binascii.Error) as exc:
            raise ValueError("image must be raw base64") from exc
        require(0 < len(decoded) <= MAX_IMAGE_BYTES, "decoded image exceeds package limit")
        # Envelope screening only. The agent must separately inspect a real
        # image's readability/dimensions; magic bytes are not a full decoder.
        supported = decoded.startswith(b"\x89PNG\r\n\x1a\n") or decoded.startswith(b"\xff\xd8\xff") or (decoded.startswith(b"RIFF") and decoded[8:12] == b"WEBP")
        require(supported, "image must have a PNG, JPEG, or WebP signature")
    questions = request.get("questions")
    require(isinstance(questions, dict) and 1 <= len(questions) <= 4, "expected 1-4 questions")
    for key, question in questions.items():
        require(description(key) and isinstance(question, dict), "invalid question")
        require(set(question) <= {"type", "instructions", "criteria"}, "unsupported question fields")
        require(description(question.get("instructions")), "instructions must be nonempty text")
        kind, criteria = question.get("type"), question.get("criteria")
        if kind == "choice":
            require(isinstance(criteria, dict) and 2 <= len(criteria) <= 26, "invalid Choice criteria")
            require(all(description(k) and description(v) for k, v in criteria.items()), "invalid option description")
        elif kind == "score":
            require(isinstance(criteria, list) and 2 <= len(criteria) <= 10, "invalid Score criteria")
            require(all(description(v) for v in criteria), "invalid level description")
        elif kind == "noul":
            if criteria is not None:
                require(isinstance(criteria, dict) and set(criteria) == {"true", "false"}, "invalid Noul criteria")
                require(all(description(v) for v in criteria.values()), "invalid Noul description")
        else:
            raise ValueError("unsupported question type")
    text_schema = {key: value for key, value in request.items() if key != "images"}
    require(len(json.dumps(text_schema, allow_nan=False).encode("utf-8")) <= TEXT_LIMIT,
            "text/schema exceeds 64 KiB; images do not expand this limit")
    body = json.dumps(request, allow_nan=False).encode("utf-8")
    require(len(body) <= BODY_LIMIT, "request exceeds body limit; token fit must also be checked separately")
    return body


def validate_response(request, response):
    validate_request(request)
    require(isinstance(response, dict) and "error" not in response, "error or non-object response")
    validate_nesting(response)
    require(response.get("model") == MODEL, "response model mismatch")
    usage = response.get("usage")
    require(isinstance(usage, dict), "missing usage")
    require(all(type(usage.get(key)) is int and usage[key] >= 0 for key in ("input_tokens", "output_tokens")), "invalid usage")
    answers = response.get("answers")
    require(isinstance(answers, dict) and set(answers) == set(request["questions"]), "answer ID coverage mismatch")
    for key, question in request["questions"].items():
        answer = answers[key]
        kind = question["type"]
        require(isinstance(answer, dict) and answer.get("type") == kind, "answer type mismatch")
        if kind == "noul":
            require(number(answer.get("noul"), 0, 1), "invalid Noul probability")
            continue
        criteria = question["criteria"]
        options = set(criteria) if kind == "choice" else {str(i) for i in range(len(criteria))}
        probabilities = answer.get("probabilities")
        require(isinstance(probabilities, dict) and set(probabilities) == options, "probability coverage mismatch")
        require(all(number(v, 0, 1) for v in probabilities.values()), "invalid probability")
        require(abs(sum(probabilities.values()) - 1) <= 0.01, "probabilities do not sum to 1")
        require(number(answer.get("confidence"), 0, 1), "invalid confidence")
        if kind == "choice":
            require(isinstance(answer.get("choice"), str) and answer["choice"] in options, "unknown choice")
            require(max(probabilities.values()) - probabilities[answer["choice"]] <= 0.0001, "choice is not a maximum-probability option")
        else:
            legend = {str(i): level for i, level in enumerate(criteria)}
            require(answer.get("legend") == legend, "Score legend mismatch")
            require(number(answer.get("score"), 0, len(criteria) - 1), "invalid score")
            weighted = sum(int(i) * p for i, p in probabilities.items())
            require(abs(answer["score"] - weighted) <= 0.05, "score is not the weighted level")
    return answers


def load_cases(path):
    document = parse_json(path.read_text(encoding="utf-8"))
    require(isinstance(document, dict) and document.get("version") == 1, "unsupported fixture version")
    cases = document.get("cases")
    require(isinstance(cases, list) and cases, "no regression cases")
    seen = set()
    for case in cases:
        require(isinstance(case, dict), "case must be an object")
        key = case.get("id")
        require(isinstance(key, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key), "unsafe case ID")
        require(key not in seen, "duplicate case ID")
        seen.add(key)
        validate_request(case.get("request"))
        expected = case.get("expected_answers")
        require(isinstance(expected, dict) and set(expected) == set(case["request"]["questions"]), "expected answer coverage mismatch")
        for question_id, target in expected.items():
            question = case["request"]["questions"][question_id]
            if question["type"] == "choice":
                require(isinstance(target, str) and target in question["criteria"], "invalid expected Choice")
            elif question["type"] == "noul":
                require(type(target) is bool, "expected Noul must be boolean")
            else:
                require(type(target) is int and 0 <= target < len(question["criteria"]), "expected Score must be a level index")
    return cases


def matches(answers, expected):
    for key, target in expected.items():
        answer = answers[key]
        if answer["type"] == "choice":
            probabilities = answer["probabilities"]
            maximum = max(probabilities.values())
            if sum(value == maximum for value in probabilities.values()) != 1:
                return False
            observed = answer["choice"]
        elif answer["type"] == "noul":
            # Test-label comparison only; not an application acceptance threshold.
            if answer["noul"] == 0.5:
                return False
            observed = answer["noul"] > 0.5
        else:
            probabilities = answer["probabilities"]
            maximum = max(probabilities.values())
            winners = [int(i) for i, p in probabilities.items() if p == maximum]
            if len(winners) != 1:
                return False
            observed = winners[0]
        if observed != target:
            return False
    return True


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, "redirect refused", headers, fp)


def send_local(body):
    # Ignore ambient proxies and reject redirects: fixture evidence stays local.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    request = urllib.request.Request(ENDPOINT, data=body, headers={"Content-Type": "application/json"})
    with opener.open(request, timeout=300) as response:
        raw = response.read(1024 * 1024 + 1)
    require(len(raw) <= 1024 * 1024, "response exceeds 1 MiB")
    return raw.decode("utf-8")


def replay(case, sender=send_local):
    record = {
        "case": case["id"],
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "request": case["request"],
        "expected_answers": case["expected_answers"],
        "interpretation": case.get("interpretation", ""),
    }
    start = time.monotonic()
    try:
        raw = sender(validate_request(case["request"]))
    except (OSError, urllib.error.URLError, ValueError) as exc:
        record.update(status="service_error", error=str(exc))
        if isinstance(exc, urllib.error.HTTPError):
            exc.close()
    else:
        record["raw_response"] = raw
        try:
            response = parse_json(raw)
            record["response"] = response
            if isinstance(response, dict) and "error" in response:
                record.update(status="service_error", error=str(response["error"]))
                record["elapsed_seconds"] = time.monotonic() - start
                return record
            answers = validate_response(case["request"], response)
        except (ValueError, TypeError) as exc:
            record.update(status="response_contract_error", error=str(exc))
        else:
            record["status"] = "pass" if matches(answers, case["expected_answers"]) else "model_mismatch"
    record["elapsed_seconds"] = time.monotonic() - start
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--live", action="store_true", help="send fixture requests to existing local Ollama; never start it")
    parser.add_argument("--record-dir", type=Path, help="explicitly save live records to a NEW private directory")
    parser.add_argument("--request", type=Path, help="validate a saved request, optionally with --response, without network")
    parser.add_argument("--response", type=Path)
    args = parser.parse_args(argv)
    if args.response and not args.request:
        parser.error("--response requires --request")
    if args.request and (args.live or args.record_dir):
        parser.error("saved-response validation is offline; omit --live and --record-dir")
    if args.record_dir and not args.live:
        parser.error("--record-dir requires --live")
    try:
        if args.request:
            request = parse_json(args.request.read_text())
            validate_request(request)
            if args.response:
                validate_response(request, parse_json(args.response.read_text()))
                print("PASS saved response contract (not judgment correctness)")
            else:
                print("PASS saved request contract (not evidence quality or context fit)")
            return 0
        cases = load_cases(args.cases)
        if not args.live:
            print(f"PASS {len(cases)} fixture schemas; no network or inference performed")
            return 0
        if args.record_dir:
            args.record_dir.mkdir(mode=0o700, parents=True, exist_ok=False)
        failed = False
        for case in cases:
            record = replay(case)
            print(json.dumps({k: record[k] for k in ("case", "status", "elapsed_seconds")}), flush=True)
            if args.record_dir:
                target = args.record_dir / (case["id"] + ".json")
                with target.open("x", encoding="utf-8") as output:
                    json.dump(record, output, indent=2, allow_nan=False)
                    output.write("\n")
            failed |= record["status"] != "pass"
        return int(failed)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"validation error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
