# Recovery validation

Use when changing or validating [recovery](recovery.md). Apply [entry static checks](validation.md#reproducible-static-checks), including complete entry/frontmatter, rendered Markdown, links/anchors, isolated package copy and diff hygiene. These cases are **authored expectations, not executed agent behavior**. They apply to current local recovery; whole-spec graph/frontier/worker reconstruction and its validation belong to discovered `work-on-spec`, not a hidden local scheduler.

| Case | Starting facts | Expected result |
| --- | --- | --- |
| Dirty-work sentinels | Staged and unstaged unrelated content, untracked note and symlink; partial owned patch | Step 1 inventories/protects every state; steps 3–4 preserve them through resume or blocker. |
| Uncertain integration succeeded | Retained summary says pending; source is already in actual target | Step 2 records applied result, checks acceptance/evidence and avoids a second integration. Squashed results need content and policy inspection, not ancestry alone. |
| Uncertain write unresolved | Remote/read-back unavailable or partial | Step 2 blocks the affected retry/dependent claim with owner and pointer; no assumed success or repeat mutation. |
| Failed owner / unknown lifecycle | Partial artifacts remain after timeout/session crash | Steps 1–2 retain capacity/ownership until stopped or safely isolated; no replacement writer while unknown. |
| Stale checks/review | Current target or relevant supporting input differs from checked snapshot | Step 3 marks affected evidence stale and refreshes verification/required independent review, retaining old failures/results. |
| Blocked dependency | Closed prerequisite lacks required accepted integration | Step 3 keeps this bounded ticket waiting and returns prerequisite observations to the overall lead or dependency owner. Only discovered Work On Spec may recompute a multi-ticket frontier or progress other eligible tickets. |
| Merge conflict | Unmerged entries and useful changes on both sides | Steps 1–3 preserve operation/both sides, resolve only within approved scope or report owner/action; no implicit abort/reset. |
| Missing required tool | Material check or reviewer capability unavailable | Step 3 reports immediate affected blocker; no install, substitution or two performative retries. |
| Budget / changed scope | Same finding resumed after two failed cycles; or requested scope/privilege changes | Steps 1–3 preserve lineage/count and escalate bounded reassessment; no fresh budget or authority. Unknown history blocks correction. |
| Cleanup / durable pointer | Source has unique dirty work, active owner or recovery record is unavailable | Step 4 retains source; only authorized safe disposition permits removal. Unavailable durable location is explicit, not new persistence infrastructure. |
| Non-Git / equivalent commit | Partial file manifest, or content-identical new commit | Steps 1/3 inspect modes/content/supporting inputs; retain equivalent content evidence only with proof, rerun state-sensitive checks. |

## Bounded execution protocol

Use a disposable local Git target with synthetic native observations, acceptance and lifecycle records. Preserve staged/unstaged/untracked/symlink sentinels. Execute an integration whose retained summary remains uncertain, inspect the actual outcome and demonstrate no duplicate application. Execute stale-check failure and refreshed checks at the current target. Exercise a stopped-owner safe direct resume and a preserved-work conflict/tool/dependency blocker; retain source and operation state until explicit fixture disposition.

Retain reproduction source, commands/results, revisions and direct lead decisions outside the installable package at the approved evidence location. Fixture assertions check local facts and authored dispositions, not an implemented recovery engine or autonomous instruction-following. Distinguish executed tools from paper walkthroughs and separately authorized agent trials. Historical #30 multi-ticket/failure evidence remains unchanged; #72 owns the new composed runtime trial. This local check replaces neither those trials nor independent review.

## Acceptance and documentation impact

Historical #28 criteria covered actual state/graph/findings, failed owners/prerequisites/conflicts, preserved artifacts, uncertain outcomes/fresh evidence, a justified phase/frontier and accessible recovery report. Current local coverage maps to step 1 (this change's actual artifacts/prerequisites/findings), steps 2–3 (local failed owners, conflicts, capability blockers and nonduplicated effects), steps 1/4 (preservation/disposition), step 3 (one justified remaining responsibility with authority/bounds/escalation), and step 4 (accessible local recovery report). Work On Spec now owns overall graph/frontier recovery; this mapping does not claim local scheduling or rewrite historical execution evidence.

Runtime homes are local recovery and this validation reference, with entry/shared/completion and dispatch compatibility pointers. #68 updates overviews/design/Unreleased for the new coordinator and transferred overall responsibility. Domain meanings, accepted ADR decisions, target policies, tracker relationships/vocabulary and installed copies remain unchanged. No orchestration persistence service or destructive cleanup is introduced.
