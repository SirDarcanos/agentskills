---
name: pr
description: Prepare a plain-language pull-request report from delivered changes and current verification/review evidence, or open/update a PR within explicit task and project authority. Use for standalone PR writing and bounded delivery handoffs.
---

# PR

Own the decision report and authorized PR preparation/publication, not implementation, independent review, acceptance, merge, issue closure, deployment, release or installed-skill replacement. Loading this skill grants no effects. A report-only request stops at the report.

## 1. Establish the reporting contract

Locate applicable target instructions and its meaningful project agreement: context/decision authority, requested effects/stages, safety, verification/review, documentation and evidence/continuation. Reuse compatible guidance regardless of filenames or Setup origin. Missing/conflicting common guidance blocks dependent project reporting with a specific reconciliation recommendation, not automatic setup. Conditional gaps block only their capability. Common policy comes from that agreement; this package owns the PR procedure.

Identify target, audience, requested report or exact PR action, approved behavior/exclusions, agreement revision and acceptance IDs, comparison baseline, branch/base/PR target, protected work, evidence location and permitted disclosure. Read target instructions and relevant workflow, documentation, tracker-completion and release policies. Ordinary requests supply these facts through conversation and inspection; no handoff form is required.

For a bounded handoff, consume the caller's agreement, deciding sources/revisions (including dirty files), checks/environment, confirmed decisions/gaps, effect authority, ownership/state and expected return. Inspect the actual artifacts and raw results, not just the caller's preferred verdict. Preserve existing build/accept/report gate decisions and finding lineage; this package does not decide them anew.

Distinguish authority to draft, retain a local report, commit/push a branch, and create/update a remote PR. Use only effects selected by the user and permitted by project policy. Delivery or branch/commit/push permission alone does not select PR preparation/publication; an explicit compound request can select both stages. Unknown authority leaves the report local/conversational and publication blocked. Publication also needs permission for the exact content disclosed.

**Complete when:** scope, baseline, evidence sources, protected work and requested effects are known, or their specific blockers are recorded.

## 2. Inspect delivered evidence and its freshness

Inspect the full relevant diff/files, including committed, staged, unstaged and included untracked changes, renames, deletions, modes and symlinks. Identify the report's state separately from the remote PR's head; local dirty work is not remotely delivered. Record revisions/content digests, supporting inputs and environment. Protect unrelated work rather than staging or cleaning it.

Read current criterion/risk evidence and separate Standards/Spec reports, their identities, scope, findings and limitations when supplied. Reuse current complete evidence without restarting analysis or review. Compare deciding agreement/code/config/test/environment identities and coverage. Changed inputs invalidate dependent claims; retain old results for their old state. Unknown impact makes all relevant evidence stale. A matching HEAD alone does not establish dirty-work freshness.

Discover companions through the target/runtime catalog or an explicit approved location, read the complete resolved entry and needed references, record source/revision and check semantic capabilities. Ambiguous candidates require disambiguation. For snapshot/review gaps, compatible `review-delivery` owns full dirty-scope fingerprinting and independent Standards/Spec review; request that bounded return only with review authority. Lead inspection is not independent review. Missing/incompatible review capability blocks acceptance claims, not an honest partial report. Do not install a helper or invoke an older same-name package as fallback. Before delegated review, inspect discovered `work-on`'s documented conditional coordination library and any existing root allocation, not its delivery procedure or universal contract. An old universal-contract-only package blocks that delegated route. Recorded corrections return to their owner with retained checkpoint/allowance state; PR does not repair. Reporting itself needs no delivery-lead invocation or worker.

Summarize implemented, verified, unverified, deferred and blocked work distinctly. Material unresolved findings, failed/unrun material checks and stale review remain acceptance blockers even if the report is complete or a draft PR is allowed. Report evidence gaps to their owner; do not repair, rerun costly benchmarks or request optional models merely to improve the report.

**Complete when:** each material claim has current inspectable evidence or an explicit unknown/stale/blocked disposition, and local versus remote state is clear.

## 3. Account for tests, CI and merge effects

Read [impact accounting](references/impact.md) completely for every report. Inspect baseline and delivered tests, CI configuration and actual deployment/release hooks; use existing authorized measurements and run records. Report protection changes, not a test-count target or presumed speedup. Missing measurements remain unavailable. Additional checks or benchmarks require their own scope, environment, resource and disclosure authority; reporting grants none.

**Complete when:** counting basis and test changes, CI jobs and qualified measurements, actual post-merge behavior, risks and reversal limits are accounted for in supporting evidence, including explicit none/unknown cases. This internal accounting is not a list of mandatory summary sections.

## 4. Write the decision report

Write for a maintainer deciding whether to merge, without requiring code reading or an audit of engineering notes. Follow the target's PR template while keeping the summary outcome-first. Aim for 100–200 words for routine changes; use more when consequential risks, migrations or required decisions need explanation. Do not pad a simple report to reach a word target.

1. Explain what changed or was fixed, the before/after outcome and why it matters, in project language. Explain necessary technical terms.
2. Give a brief plain-language verification result: what meaningful behavior was checked and the outcome. Distinguish independent review from direct inspection. Say which checks passed, not “all tests passed” unless that exact complete scope is evidenced. Put commands and technical provenance in supporting evidence.
3. Make material failed, unrun or stale checks, unresolved findings, uncertainty and acceptance blockers prominent, with their consequence and next action. Include relevant compatibility changes, lost/replaced protection, migrations and required manual actions with owners/approvals. Never bury these in supporting detail.
4. Omit unchanged tests, CI, deployment, reversal and procedural boilerplate when they do not affect the decision. Include those topics when actual protection changes, merge effects or reversal limits matter. Do not repeat gate ledgers or lists of actions not taken merely to prove diligence.
5. Use `Closes #X` only when merging should close that issue under target completion policy. Use `Refs #X` for related issues that should remain open. Do not use `Fixes` or `Resolves` as closing keywords.

Keep technical support separate from the short summary. Same-session evidence can remain in conversation. When persistence/publication is selected and authorized, prefer a dedicated PR/issue comment or a collapsed **Validation details** section. Link accessible evidence once when useful rather than reproducing it in the summary. Keep hashes, commands, raw outputs, reviewer identifiers, snapshot history, test arithmetic and full original reviewer reports in that record. Retain checked-state/supporting-input identities, environment, acceptance coverage, impact accounting, limitations and gate/documentation dispositions there. Keep material caveats in the visible summary even when their technical details are recorded separately.

Use temporary local storage for intermediate logs and snapshots. Publish only useful, disclosure-safe evidence within existing publication authority; inspect read-back before claiming persistence. If publication is unrequested, return evidence conversationally without treating routine storage as missing. If requested publication is unavailable/unauthorized, identify that blocked action and any selected durable-storage gap, without exposing private logs or claiming publication. User-selected persistence does not erase active owners, uncertain effects or spent allowances; retain their safety state under target guidance. Keep reusable tests, fixtures and scripts committed and runnable; do not create routine per-change committed `docs/validation/` reports. Preserve historical evidence unless its migration/removal is separately approved.

**Complete when:** a reader can decide the next action without code-diagram literacy, every claimed outcome is evidence-bounded and missing information is visible.

## 5. Publish only the authorized action and return

For opening/updating a PR, read [publication](references/publication.md) completely. With report-only authority, skip remote mutation and return the draft. With missing permission/capability, return the useful report plus the blocked action and recommended next step.

Return complete/partial/blocked **report and publication outcomes separately**: report/artifact pointer, reported baseline/state, actual check/review coverage and limitations, findings/blockers, test/CI impact, documentation disposition, applied versus proposed effects, PR URL/read-back if any and next action. A complete blocked-delivery report is not accepted delivery. Stop without merge, closure, deployment, release, installation or automatic progression.

For changes or validation of this package, read [validation](references/validation.md).
