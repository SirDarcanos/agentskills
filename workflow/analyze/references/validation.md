# Analyze validation

Read when changing this package or exercising standalone/handoff routing. Expected scenarios are authored inputs, not execution evidence.

## Local checks

1. Inspect rendered Markdown and frontmatter: `name: analyze`, ordinary matching requests and bounded handoffs, no command-only gate, recommendations without implementation, explicit completion/partial/blocking conditions.
2. Resolve every relative link from its containing file. Copy the entire package including LICENSE to an isolated directory without sibling skills and repeat link/frontmatter checks.
3. With Python 3.9+ and no dependencies run `python3 -B workflow/analyze/scripts/check-fixture.py` (use the copied path for isolation). Six unittest checks exercise synthetic catalogs outside the target, all five method contract stubs, matching content identities, caller-only invalidation, missing/incompatible methods and preserved target bytes. Only temporary synthetic files are written; there is no network, model, agent launch or installed mutation.
4. Inspect each stub against step 4's semantic requirements. These fixtures exercise the method availability/freshness contract without requiring installed method packages. Their scripted assertions do not execute Analyze, prove method selection, certify full stub compatibility or replace actual candidate-entry inspection.
5. Walk the cases below through the complete entry, inspecting real fixture sources/assertions. Record observed recommendations, deciding inputs, check mappings, authority/domain disposition and stop behavior outside the installable package. Clearly distinguish a direct walkthrough from independent/delegated trials.
6. Review the integrated diff for credentials, private data, generated artifacts, nonportable paths, duplicate ownership and preserved notices. Recheck deciding identities before returning.

## Routing and boundary cases

| Input | Expected result |
| --- | --- |
| Clear behavioral change with useful test seam | TDD recommended with targeted behavior/error checks; no user seam questionnaire |
| Uncertain adapter feasibility | Research/inspection for source gaps, bounded prototype recommendation if experiment needed; subsequent production method conditional on findings |
| Poorly understood legacy formatting | Characterization then suitable production method; intended, unknown and defective behavior kept distinct |
| Agreed cross-component workflow | Acceptance-first with observable executable examples plus meaningful failure paths; child-local checks alone insufficient |
| Straightforward heading/config correction | Build-and-check with proportionate existing text/parser/link checks, not manufactured unit tests |
| Current complete investigation/analysis | Reuse cited deciding evidence; no complete rerun or mandatory specialist/model call |
| Changed deciding caller with unchanged service | Refresh dependent consumer findings/checks, keep unaffected service evidence; dirty identities matter |
| Missing recommended method / incompatible same-name candidate | Supported recommendation remains; method execution unavailable, no install/legacy fallback; justified equivalent only when truly suitable |
| Required missing research/domain capability | Affected conclusion/record remains blocked; unaffected analysis continues, no locally duplicated specialist |
| Unapproved consequential behavior or document write | Proposed conclusion/plan-only disposition; permission owner receives recommendation, not routine method choice |
| Standalone, plan-only, non-code target | Conversation brief and explicit stop without implementation, publication, new hierarchy or unapproved artifact writes |
| Ticketing prerequisite within existing inspection authority | Bounded supported return to the caller, which consumes it and resumes drafts without asking permission for routine inspection or skill use; no standalone publication |
| Product coverage change or missing authority | Specific affected blocker and concise outcome/scope/risk recommendation; no silent new commitment or expanded effects |
| Interim Work On route | Discover Analyze through catalog, consume current evidence or inspected return; lead selects next gate with its own authority, never automatic standalone continuation |

## Limits

Static checks and fixture assertions are offline contract evidence, not installed discovery, composed runtime compliance, live API/model use or independent review. Check availability and analysis support are separate from delivery execution/acceptance. Preserve historical Work On validation records at their original paths.
