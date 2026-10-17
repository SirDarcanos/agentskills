#!/usr/bin/env python3
"""Rerun existing offline checks in disposable copies; not an agent workflow test.

Run from any directory: python3 -B <this-file>
Prints raw outcomes and input digests; creates no committed execution report.
No network, installed discovery, model calls or live tracker mutations are used.
"""
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile

REPO = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "package_checks", REPO / "docs/validation/composable-acceptance/check_packages.py")
packages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packages)

# Reuse documented commands. Added endpoints are Handoff, What Now, PR contracts,
# and project-guided Research; older history is not rewritten or silently waived.
JOBS = {**packages.JOBS,
        "handoff": ["scripts/check-handoff-fixture.py"],
        "research": ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
        "pr": ["scripts/test_contract.py"],
        "resolve-merge-conflicts": ["scripts/check-fixtures.py"]}
SUITES = ("discovery-spec-tickets", "investigate-bug", "bug-to-fix", "write-tickets",
          "pr", "installed-skill-migration", "delivery-coverage")


def main():
    failures = []
    before = {str(path.relative_to(REPO)): packages.manifest(path)
              for path in packages.package_locations(REPO)}

    def run(label, args, cwd):
        try:
            result = packages.run_offline([sys.executable, "-B"] + args, cwd)
        except Exception as error:
            failures.append(label)
            print(f"{label}: unavailable: {error}", flush=True)
            return
        print(f"\n=== {label}: exit {result.returncode} ===\n"
              + result.stdout + result.stderr, flush=True)
        if result.returncode:
            failures.append(label)

    with tempfile.TemporaryDirectory(prefix="session-workflow-") as scratch:
        scratch = Path(scratch)
        for index, source in enumerate(packages.package_locations(REPO)):
            isolated = scratch / f"package-{index}" / "payload"
            shutil.copytree(source, isolated, symlinks=True)
            try:
                observed = packages.inspect_package(isolated)
                assert observed["name"] == source.name
                assert packages.manifest(isolated) == before[str(source.relative_to(REPO))]
                print(f"{source.name}: isolated metadata/notices/links pass", flush=True)
            except Exception as error:
                failures.append(source.name + " structural")
                print(f"{source.name}: structural failure: {error}", flush=True)
            if source.name in JOBS:
                run(source.name, JOBS[source.name], isolated)
            if source.name == "review-delivery":
                run("review-delivery contracts", ["scripts/test_contract.py"], isolated)

        # Source-development suites need their repository fixtures, not installed
        # siblings. Copy a source tree, not an active installation or its .git.
        tree = scratch / "source"
        tree.mkdir()
        for directory in ("workflow", "writing", "models", "docs", "benchmarks"):
            shutil.copytree(REPO / directory, tree / directory, symlinks=True,
                            ignore=shutil.ignore_patterns("__pycache__", "results"))
        for name in ("README.md", "AGENTS.md", "CONTEXT.md", "LICENSE", "CHANGELOG.md"):
            shutil.copy2(REPO / name, tree / name)
        for suite in SUITES:
            run(suite, ["-m", "unittest", "discover", "-s", "docs/validation/" + suite,
                        "-p", "test_*.py", "-v"], tree)
        run("write-spec", ["docs/validation/write-spec/check.py"], tree)
        run("what-now", ["docs/validation/ask-nico/check-package.py"], tree)
        run("writing-for-agents", ["docs/validation/writing-for-agents/check-package.py"], tree)

    after = {str(path.relative_to(REPO)): packages.manifest(path)
             for path in packages.package_locations(REPO)}
    assert before == after, "source package drift"
    docs = [REPO / "README.md", REPO / "docs/skills.md", REPO / "docs/workflow-guide.md",
            REPO / "docs/design/session-oriented-workflow.md",
            REPO / "docs/validation/session-workflow/README.md"]
    print("Current document links:", packages.links.check_links(docs, REPO))
    print(json.dumps({"python": sys.version.split()[0], "package_inputs": before,
                      "source_packages_unchanged": True, "failed_jobs": failures,
                      "evidence_kind": "offline static assertions and authored synthetic fixtures; no agent trials"},
                     indent=2))
    return bool(failures)


if __name__ == "__main__":
    sys.exit(main())
