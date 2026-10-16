#!/usr/bin/env python3
"""Source-development reading comparison, not a shipped consumer prerequisite.

Run from any directory: python3 -B <this-file> --base <source-revision>
Reports static whitespace-word surfaces, not tokens, speed or agent adherence.
The source revision is an explicit input; no historical record is required by skills.
"""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ["AGENTS.md", "docs/agents/project.md", "docs/agents/workflow.md"]
REVIEW = ["workflow/review-delivery/SKILL.md"] + [
    f"workflow/review-delivery/references/{name}.md" for name in ("handoff", "scope", "report")]
COMMON = PROJECT + ["workflow/work-on/SKILL.md",
                    "workflow/implementation-preflight/SKILL.md",
                    "workflow/build-and-check/SKILL.md"] + [
    f"workflow/work-on/references/{name}.md" for name in ("build", "verification", "completion")
] + REVIEW
PR = ["workflow/pr/SKILL.md", "workflow/pr/references/impact.md"]
# Equivalent planning outcome: Shape Work uses inline Analyze and inspects the
# Build and Check capability. No source/domain gap or delegation is selected.
# Analyze's domain/delegation references are mandatory only on those branches;
# they and the discovered companion closures must be added if that task changes.
PLANNING = PROJECT + [f"workflow/{name}/SKILL.md" for name in
                      ("shape-work", "analyze", "build-and-check")]

# Equivalent established-cause investigation followed by the selected ticket
# stage. Baseline always drafts a ticket; candidate explicitly selects it. No
# technical/source gap, new record, helper execution or delegation. Diagnosis-only
# is reported separately, never substituted for the equivalent ticket endpoint.
TRACKER_POLICY = ["docs/agents/issue-tracker.md", "docs/agents/triage-labels.md"]
INVESTIGATION = PROJECT + TRACKER_POLICY + [
    "workflow/investigate-bug/SKILL.md", "workflow/write-tickets/SKILL.md"]
OLD_TRACKER = ["workflow/setup-project/SKILL.md",
               "workflow/setup-project/references/issue-tracker.md"]
NEW_TRACKER = ["workflow/investigate-bug/references/ticket-stage.md",
               "workflow/setup-project/references/native-tracker.md"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    base = subprocess.check_output(["git", "rev-parse", "--verify", args.base + "^{commit}"],
                                   cwd=ROOT, text=True).strip()

    def surface(paths, historical):
        result = {}
        for path in sorted(set(paths)):
            content = (subprocess.check_output(["git", "show", f"{base}:{path}"], cwd=ROOT, text=True)
                       if historical else (ROOT / path).read_text())
            result[path] = len(content.split())
        return {"words": sum(result.values()), "paths": result}

    # Representative small code change: established compatible project, current
    # plan, no tracker/domain/assessment gap, direct Build and Check, required
    # independent review. Two fresh reviewers each load relevant policy and review
    # procedure, not the lead's unrelated method/repair library. No README/LICENSE,
    # maintenance instructions, task evidence or scripts counted as instructions.
    # Full files count even if an operational branch uses only a section; repeated
    # reads in one context deduplicate, distinct contexts count separately.
    observations = {}
    for historical, name in ((True, "baseline"), (False, "candidate")):
        extra = "contracts" if historical else "coordination"
        lead = surface(COMMON + [f"workflow/work-on/references/{extra}.md"], historical)
        reviewer = surface(PROJECT + REVIEW, historical)
        pr = surface(PROJECT + PR, historical)
        observations[name] = {"planning": surface(PLANNING, historical),
                              "investigation_to_ticket": surface(
                                  INVESTIGATION + (OLD_TRACKER if historical else NEW_TRACKER), historical),
                              "diagnosis_only": surface(
                                  INVESTIGATION + OLD_TRACKER if historical else
                                  PROJECT + ["workflow/investigate-bug/SKILL.md"], historical),
                              "lead_delivery": lead, "each_of_two_reviewers": reviewer,
                              "delivery_total": lead["words"] + 2 * reviewer["words"],
                              "selected_PR_fresh_context": pr}
        if historical:
            # The old entry additionally required PR-report preparation. Keep its
            # endpoint cost separate rather than claiming all savings are dedup.
            observations[name]["former_ordinary_endpoint_total"] = (
                lead["words"] + 2 * reviewer["words"] + surface(PR, historical)["words"])
    print(json.dumps({"base": base, "unit": "whitespace words; static reading paths",
                      "assumptions": "planning: inline Analyze and Build and Check capability inspection; "
                                     "delivery: direct small code change and two neutral reviewers; "
                                     "investigation-to-ticket: established cause and explicitly selected ticket stage; "
                                     "same project, no source/domain gaps, no delegation; diagnosis-only "
                                     "reported separately because baseline requires ticket preparation",
                      "limits": "Static full-file counts, including actual project guidance per revision; "
                                "not tokens, timing or agent adherence. Conditional branches are not measured.",
                      "contexts": observations}, indent=2))


if __name__ == "__main__":
    main()
