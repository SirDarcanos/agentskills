# Dispatch validation

Use when changing or validating [dispatch](dispatch.md). Follow [entry static checks](validation.md#reproducible-static-checks) for full entry/frontmatter, Markdown rendering, relative links/anchors, isolated package copying and diff hygiene. Walk these cases against actual step references. They are **authored expectations, not executed agent behavior**.

| Case | Starting facts | Expected behavior |
| --- | --- | --- |
| Ready parent, non-prefixed titles | Mapped ready spec P has ready work A/B/C; C natively blocked by A; titles have no classification prefixes | Steps 1–2 coordinate P, queue eligible children only; C waits. Step labels do not order independent A/B. |
| Equivalent mapping | Target uses `type:agreement`, `type:work`, `actionable` and prefix-bearing titles | Step 1 follows approved metadata mapping, not this repository's spelling or title parsing. Subordinate specs/PRs are not duplicate implementation work. |
| Graph mismatch / failed read | Intended blocker missing, parent differs, page unavailable or transitive blocker unknown | Step 1 blocks affected dispatch and returns reconciliation through maintained procedure/ticketing. No implicit graph/label mutation or prose fallback. |
| Closed without integration | A closed, local tests green, required accepted merge absent | Step 2 keeps C waiting. Step 5 unlocks only after inspected target-required integration evidence. |
| Ownership conflict | A and B edit a shared interface despite no blocker; D owns independent behavior | Step 2 groups within approved boundaries or serializes A/B; D may progress. Disjoint filenames using an unstable contract are also coupled. |
| Direct route / no worker capability | Authorized cohesive build; delegation ungranted or bounded lifecycle unavailable | Steps 2–3 choose direct build where equivalent; missing independent review still blocks acceptance. Unsafe ownership or unavailable writes produces a blocker. |
| Capacity | Unfinished building and exploration assignments occupy both allowed slots; a reviewer is proposed | Steps 2–3 wait or use a safe direct route; idle unfinished work still occupies capacity. No hidden third or nested worker. |
| Bounded assignment | Ready ticket with compatible runtime and explicit delegation approval | Step 3 records identity, exclusive scope, isolation, authority, acceptance/checks, revision/context pointers, finite bound and return contract before start. |
| Returned drift / old base | Worker reports done but adds unrelated files or assumes a changed interface | Step 4 inspects actual diff/evidence and blocks or repairs within authority; an old local pass is not an integrated pass. |
| Serial integration / frozen review | Two valid returns; target requires PRs; scope under review | Step 4 integrates one at a time only after snapshot checks complete and authorized policy actions. Pending merge cannot unlock a required-merge dependent. |
| Incremental verification | Independent result integrated; later dependent result changes shared behavior | Steps 4–5 refresh affected and cross-ticket checks/review at the new revision; lead keeps whole-agreement accountability. |
| Failed owner / retained artifacts | Worker expired or integration conflicted, useful branch/worktree remains | Steps 3–4 preserve artifacts and uncertain state; confirm stopped/isolated before replacement. Entry selects recovery if needed; absent recovery blocks that route. No cleanup by default. |

## Bounded execution protocol

Use a disposable Git project and synthetic native parent/blocker observations, not production tracker fixtures. Give the ready parent and ready children plain descriptive titles. Include an initially blocked child, independent work and overlapping interface ownership. Record the lead's inspected frontier and each waiting reason against procedure steps; keep classification and readiness separate from dependency order.

Exercise actual local direct changes and serial integration, retaining source branches/worktrees until the fixture's explicit disposition. Run applicable checks after each integrated result. Demonstrate that a closed predecessor without accepted integration cannot unlock its child; then add inspected synthetic acceptance/integration evidence and observe the next eligible frontier. Include a material cross-ticket check and show relevant old evidence is stale after changes. Preserve unrelated fixture work and native observations.

Keep reproduction source, commands/results, before/after revisions and per-case decisions outside the installable package at the approved evidence location. A fixture assertion checks synthetic facts/expected transitions; it is not a production scheduler, native graph/API test, autonomous skill trial or independent review. Distinguish direct walkthroughs from executed tools and separately authorized agent runs. #30 owns the integrated multi-ticket/failure trial; #28 owns interruption/resume.

## Acceptance and documentation impact

#27 criteria map to step 1 (reconciled native graph, mapped roles and parent coordination), step 2 (evidence-aware frontier, coupled ownership, direct/default and limits), step 3 (bounded owners/context), step 4 (return inspection, serial integration, refreshed evidence and preservation), step 5 (recomputed frontier and lead accountability). Shared contracts, maintained graph library, build, verification and completion retain their existing authority; no second graph algorithm or orchestration engine is introduced.

Runtime homes: dispatch and this reference, entry/shared-contract pointers. Package/repository overviews, design implementation pointer and Unreleased changelog describe compatible new functionality (minor release impact). Domain meanings, ADR/package boundary, tracker vocabulary/edges, project authority, legacy commands and installed copies remain unchanged. Recovery, integrated trials and final installation coverage remain later scoped work.
