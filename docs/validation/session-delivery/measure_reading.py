#!/usr/bin/env python3
"""Static full-file reading comparison; never tokens, timing or agent adherence.

Run: python3 -B docs/validation/session-delivery/measure_reading.py --base 45e5a24
The baseline is explicit and resolved to a commit. No repository writes occur.
"""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ["AGENTS.md", "docs/agents/project.md", "docs/agents/workflow.md"]
TRACKER_POLICY = ["docs/agents/issue-tracker.md", "docs/agents/triage-labels.md"]


def entry(name):
    return f"workflow/{name}/SKILL.md"


def ref(name, file):
    return f"workflow/{name}/references/{file}.md"


REVIEW = [entry("review-delivery")] + [ref("review-delivery", name)
          for name in ("handoff", "scope", "report")]
METHOD = [entry("implementation-preflight"), entry("build-and-check")]
LOCAL = [ref("work-on", name) for name in ("build", "verification", "completion")]
# PR's reporting contract reads target tracker-completion and release policy.
# In this project workflow.md owns releases; the two tracker documents supply
# completion and release-label rules. Charge them in both revisions/PR contexts.
PR = [entry("pr"), ref("pr", "impact"), ref("pr", "publication")] + TRACKER_POLICY
OLD_TRACKER = [entry("setup-project"), ref("setup-project", "issue-tracker")]
NEW_TRACKER = [ref("setup-project", "native-tracker")]


def manifests(historical):
    """Explicit branches, not a Markdown crawler that loads every optional link."""
    lead = [entry("work-on"), ref("work-on", "contracts" if historical else "coordination")]
    delivery = lead + LOCAL + METHOD + REVIEW
    planner = [entry(name) for name in ("shape-work", "analyze", "build-and-check")]
    diagnosis = [entry("investigate-bug")]
    # Baseline investigation cannot finish without its selected ticket outcome.
    tracker = OLD_TRACKER if historical else NEW_TRACKER
    investigation = diagnosis + [entry("write-tickets")] + tracker + TRACKER_POLICY
    if not historical:
        investigation += [ref("investigate-bug", "ticket-stage")]
    return {
        "planning": {"planner": planner},
        "investigation_selected_ticket": {"investigator": investigation},
        "investigation_diagnosis_only": {"investigator": investigation if historical else diagnosis},
        "bounded_delivery_before_PR": {"lead": delivery, "standards": REVIEW, "spec": REVIEW},
        # Equivalent published endpoint in one context: user explicitly selects PR
        # for the candidate. Baseline requires it automatically. No repair branch.
        "bounded_delivery_with_PR": {"lead": delivery + PR, "standards": REVIEW, "spec": REVIEW},
        "selected_PR_fresh_context": {"publisher": PR},
    }


def measure(base):
    def content(path, historical):
        return (subprocess.check_output(["git", "show", f"{base}:{path}"], cwd=ROOT, text=True)
                if historical else (ROOT / path).read_text())

    def surface(paths, historical):
        return {path: len(content(path, historical).split()) for path in sorted(set(paths))}

    observations = {}
    # Hold common project instructions fixed as in the accepted design, but also
    # expose actual per-revision totals so moving bulk into project docs is visible.
    fixed_project = surface(PROJECT, True)
    for historical, name in ((True, "baseline"), (False, "candidate")):
        actual_project = surface(PROJECT, historical)
        scenarios = {}
        for scenario, contexts in manifests(historical).items():
            measured = {}
            for context, paths in contexts.items():
                package = surface(paths, historical)
                measured[context] = {
                    "instruction_paths": package,
                    "fixed_project_paths": fixed_project,
                    "actual_project_paths": actual_project,
                    "fixed_project_total": sum(package.values()) + sum(fixed_project.values()),
                    "actual_project_total": sum(package.values()) + sum(actual_project.values()),
                }
            scenarios[scenario] = {
                "contexts": measured,
                "fixed_project_total": sum(row["fixed_project_total"] for row in measured.values()),
                "actual_project_total": sum(row["actual_project_total"] for row in measured.values()),
            }
        observations[name] = scenarios
    comparisons = {}
    for kind in ("fixed", "actual"):
        comparisons[kind] = {}
        for scenario in observations["baseline"]:
            before = observations["baseline"][scenario][kind + "_project_total"]
            after = observations["candidate"][scenario][kind + "_project_total"]
            comparisons[kind][scenario] = {
                "baseline": before, "candidate": after,
                "reduction_words": before - after,
                "reduction_percent": round(100 * (before - after) / before, 2)}
    return {"base": base, "unit": "whitespace words; full files once per context",
            "comparisons_with_fixed_project": comparisons["fixed"],
            "comparisons_with_actual_project": comparisons["actual"], "observations": observations,
            "limits": [
                "Static instruction arithmetic, not runtime tokens, latency or intervention counts.",
                "Planning includes inline Analyze and inspected Build and Check; no source/domain gap.",
                "Investigation selected-ticket compares the same complete published-artifact endpoint.",
                "Diagnosis-only baseline includes its compulsory ticket route; endpoints differ.",
                "Before-PR delivery baseline is an intermediate boundary, not its old completion endpoint.",
                "With-PR compares equivalent completion; fresh PR context is reported separately.",
                "Delivery includes root coordination and two separate neutral reviewer contexts.",
                "No recovery, recorded repair, domain, optional model or whole-spec branch is selected.",
                "Task evidence, automatic harness prompts, README/LICENSE and maintenance files excluded.",
            ]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    base = subprocess.check_output(["git", "rev-parse", "--verify", args.base + "^{commit}"],
                                   cwd=ROOT, text=True).strip()
    print(json.dumps(measure(base), indent=2))


if __name__ == "__main__":
    main()
