"""Local JSON tracker CRUD fixture, not a policy engine or GitHub emulator.

Python 3.9+, no network. Caller chooses operations/labels; this fixture deliberately
makes no authorization or readiness decisions. Store must be a disposable file.
"""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("store", type=Path)
    parser.add_argument("operation", choices=("list", "create", "update", "read"))
    parser.add_argument("--number", type=int)
    parser.add_argument("--title")
    parser.add_argument("--body", type=Path)
    parser.add_argument("--labels", nargs="*")
    parser.add_argument("--timeout-after-write", action="store_true")
    parser.add_argument("--fail-read", action="store_true")
    args = parser.parse_args()
    state = json.loads(args.store.read_text()) if args.store.exists() else {"issues": []}
    if args.operation == "list":
        result = state["issues"]
    elif args.operation == "create":
        assert args.title and args.body
        result = {"number": max((i["number"] for i in state["issues"]), default=0) + 1,
                  "title": args.title, "body": args.body.read_text(),
                  "labels": args.labels or [], "revision": 1, "relationships": []}
        state["issues"].append(result)
    else:
        result = next(i for i in state["issues"] if i["number"] == args.number)
        if args.operation == "update":
            if args.title is not None:
                result["title"] = args.title
            if args.body is not None:
                result["body"] = args.body.read_text()
            if args.labels is not None:
                result["labels"] = args.labels
            result["revision"] += 1
    if args.operation in ("create", "update"):
        args.store.write_text(json.dumps(state, indent=2) + "\n")
        if args.timeout_after_write:
            raise SystemExit("simulated timeout after persistence: outcome unknown to caller")
    if args.fail_read:
        raise SystemExit("simulated read unavailable")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
