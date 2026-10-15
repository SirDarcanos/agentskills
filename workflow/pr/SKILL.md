---
name: pr
description: Prepare a plain-language pull-request report from delivered changes and current verification/review evidence, or open/update a PR within explicit task and project authority. Use for standalone PR writing and bounded delivery handoffs.
---

# PR

Own the decision report and authorized PR preparation/publication, not implementation, independent review, acceptance, merge, issue closure, deployment, release or installed-skill replacement. Loading this skill grants no effects. A report-only request stops at the report.

## 1. Establish the reporting contract

Identify target, audience, requested report or exact PR action, approved behavior/exclusions, agreement revision and acceptance IDs, comparison baseline, branch/base/PR target, protected work, evidence location and permitted disclosure. Read target instructions and relevant workflow, documentation, tracker-completion and release policies. Ordinary requests supply these facts through conversation and inspection; no handoff form is required.

For a bounded handoff, consume the caller's agreement, deciding sources/revisions (including dirty files), checks/environment, confirmed decisions/gaps, effect authority, ownership/state and expected return. Inspect the actual artifacts and raw results, not just the caller's preferred verdict. Preserve existing build/accept/report gate decisions and finding lineage; this package does not decide them anew.

Distinguish authority to draft, retain a local report, commit/push a branch, and create/update a remote PR. Use only effects approved by the task and project policy; an approved implementation may include PR publication if that policy expressly permits it. Unknown authority leaves the report local/conversational and publication blocked. Publication also needs permission for the exact content disclosed.

**Complete when:** scope, baseline, evidence sources, protected work and requested effects are known, or their specific blockers are recorded.

## 2. Inspect delivered evidence and its freshness

Inspect the full relevant diff/files, including committed, staged, unstaged and included untracked changes, renames, deletions, modes and symlinks. Identify the report's state separately from the remote PR's head; local dirty work is not remotely delivered. Record revisions/content digests, supporting inputs and environment. Protect unrelated work rather than staging or cleaning it.

Read current criterion/risk evidence and separate Standards/Spec reports, their identities, scope, findings and limitations when supplied. Reuse current complete evidence without restarting analysis or review. Compare deciding agreement/code/config/test/environment identities and coverage. Changed inputs invalidate dependent claims; retain old results for their old state. Unknown impact makes all relevant evidence stale. A matching HEAD alone does not establish dirty-work freshness.

Discover companions through the target/runtime catalog or an explicit approved location, read the complete resolved entry and needed references, record source/revision and check semantic capabilities. Ambiguous candidates require disambiguation. For snapshot/review gaps, compatible `review-delivery` owns full dirty-scope fingerprinting and independent Standards/Spec review; request that bounded return only with review authority. Lead inspection is not independent review. Missing/incompatible review capability blocks acceptance claims, not an honest partial report. Do not install a helper or invoke an older same-name package as fallback. Before any delegated/corrective route, consume the discovered `work-on` execution library and existing root ledger; missing capability blocks that route. Reporting itself needs no delivery-lead invocation or worker.

Summarize implemented, verified, unverified, deferred and blocked work distinctly. Material unresolved findings, failed/unrun material checks and stale review remain acceptance blockers even if the report is complete or a draft PR is allowed. Report evidence gaps to their owner; do not repair, rerun costly benchmarks or request optional models merely to improve the report.

**Complete when:** each material claim has current inspectable evidence or an explicit unknown/stale/blocked disposition, and local versus remote state is clear.

## 3. Account for tests, CI and merge effects

Read [impact accounting](references/impact.md) completely for every report. Inspect baseline and delivered tests, CI configuration and actual deployment/release hooks; use existing authorized measurements and run records. Report protection changes, not a test-count target or presumed speedup. Missing measurements remain unavailable. Additional checks or benchmarks require their own scope, environment, resource and disclosure authority; reporting grants none.

**Complete when:** counting basis and test changes, CI jobs and qualified measurements, actual post-merge behavior, risks and reversal limits are accounted for, including explicit none/unknown cases.

## 4. Write the decision report

Lead with what changes for people and why. Explain necessary technical terms in project language. Keep commands, paths, raw outputs and optional diagrams as accessible supporting evidence, not the primary explanation. Follow the target's PR template while retaining these facts (combine headings when clearer):

- **Change and purpose:** before/after behavior, who benefits, scope and exclusions, agreement/issue links.
- **Evidence and remaining work:** actual checks with command/run/source, state and environment; passed/failed/not-run/stale distinctions, acceptance coverage, independent review versus direct inspection, unresolved findings and consequences. Say which checks passed, not “all tests passed” unless that exact complete scope is evidenced.
- **Test and CI impact:** declared baseline/count unit, added/removed/updated/moved tests and protection impact; job changes, duration/compute measurements or absent/unavailable evidence with reasons.
- **Risks and limitations:** affected users/data/interfaces, known uncertainties, accepted deferrals and owners, compatibility and migration effects.
- **After merge and reversal:** automatic effects established by configuration/run evidence, manual actions and their owners/approvals, deployment/release/install state, rollback steps and data/installation consequences a source revert cannot undo.
- **Decision/state:** report readiness distinct from acceptance, remote PR/merge/deploy/release state, material blockers and recommended next action. Documentation/changelog/release-impact disposition under target policy.

Default supporting evidence to a collapsed **Validation details** section in the PR/issue body or a dedicated PR/issue comment. Keep the visible summary focused on changes, fixes and material risks, failed/unrun checks, unresolved blockers and required actions; do not hide consequential problems in collapsed detail. Retain actual commands, results/raw outputs, relevant checked state and supporting-input identities, limitations and original independent review reports in retrievable detail, with a direct section/comment pointer in the handoff.

Use temporary local storage for intermediate logs and snapshots. Publish only useful, disclosure-safe evidence within existing publication authority; inspect read-back before claiming persistence. If publication is unavailable or unauthorized, return the evidence conversationally and identify the blocked action and any durable-storage gap, without exposing private logs or claiming publication. Keep reusable tests, fixtures and scripts committed and runnable; do not create routine per-change committed `docs/validation/` reports. Preserve historical evidence unless its migration/removal is separately approved.

**Complete when:** a reader can decide the next action without code-diagram literacy, every claimed outcome is evidence-bounded and missing information is visible.

## 5. Publish only the authorized action and return

For opening/updating a PR, read [publication](references/publication.md) completely. With report-only authority, skip remote mutation and return the draft. With missing permission/capability, return the useful report plus the blocked action and recommended next step.

Return complete/partial/blocked **report and publication outcomes separately**: report/artifact pointer, reported baseline/state, actual check/review coverage and limitations, findings/blockers, test/CI impact, documentation disposition, applied versus proposed effects, PR URL/read-back if any and next action. A complete blocked-delivery report is not accepted delivery. Stop without merge, closure, deployment, release, installation or automatic progression.

For changes or validation of this package, read [validation](references/validation.md).
