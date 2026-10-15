# Entry validation

For the current #67 single-change entry, read [single-change validation](single-change-validation.md) first. The #19 cases below are historical coverage, not current broad-entry promises; multi-ticket scheduling now belongs to `work-on-spec`. Keep original trial records unchanged.

Use when changing or validating entry and the shared contract. For discovery, brief/spec authoring or publication/readiness checks, also read [product-agreement validation](product-agreement-validation.md). For codebase-informed planning, readiness or domain handoffs, read [technical-readiness validation](technical-readiness-validation.md). For decomposition, native graph reconciliation or work-ticket classification, also read [ticketing validation](ticketing-validation.md). For one-owner implementation and local correctness handoffs, read [build validation](build-validation.md). For integrated acceptance evidence, risk checks or evidence-sufficiency decisions, read [verification validation](verification-validation.md). For repairs, delivery gates/reporting or readiness reassessment, read [completion validation](completion-validation.md). For ready-frontier scheduling, assignments and incremental integration, read [dispatch validation](dispatch-validation.md). For interrupted/failed delivery and safe resume, read [recovery validation](recovery-validation.md). #19 ships routing instructions, not an executable router. Static checks and the authored cases below do not establish agent behavior. Integrated executed trials belong to #29/#30; installation/runtime guidance belongs to #31.

## Reproducible static checks

1. Read the complete entry point and contract; inspect Markdown headings/tables and frontmatter. Confirm metadata and body agree: explicit delivery or an authorized bounded lead/investigation-and-fix assignment, with no command-only metadata gate; discovery and investigation-only work grant no fix authority.
2. Resolve every relative Markdown link from its containing file, including anchors. Copy only `work-on` to a temporary directory and repeat: no sibling skill paths should be needed. Expected future filenames are code text, not broken links or shipped procedures.
3. Check the diff with `git diff --check`. Inspect for private material, credentials, workstation paths, generated logs, imported third-party prose and changes outside approved scope.
4. Walk each case below against actual instructions. Record static reasoning separately from executed agent walkthroughs. For a real walkthrough, record invocation/runtime, authorized synthetic fixture, agreement/revision, observed tool actions, returned route/blockers and before/after protected-work fingerprints. Report deviations and unrun cases.

## Complete-read and reference-recovery cases

When changing the contract's [complete-read and reference-resolution procedure](contracts.md#complete-reads-and-reference-resolution), walk these cases using disposable fixtures. Inspect incoming callers, including Work On Spec's contract consumption and Setup Project's library entry boundary. Keep the procedure authoritative in the contract; these are expected observations, not another discovery algorithm.

| Case | Required observation |
| --- | --- |
| Large combined output omits a required pointer | Retained-output or focused separate reads recover all omitted required material before dependent action; the partial read is not marked complete. |
| Valid companion uses a different reference filename than assumed | The complete inspected entry/authoritative contract supplies the target relative to the discovered package, without inventing a responsibility-derived filename. |
| ENOENT for a guessed or stale path | Pointer and actual layout inspection distinguish the wrong path from package absence; successful resolution resumes compatibility/permission checks. |
| Required reference genuinely missing or inspection unavailable | Inspected source/path and missing-file evidence support the affected blocker; unavailable inspection stays unknown. Useful findings/protected work survive without installation, aliases, stubs, setup invocation or weakened graph requirements. |
| Independently installed package with no sibling tree | Runtime/project discovery supplies its actual location; internal references resolve there and existing compatibility/permission checks still apply. |

Record fixture inputs, actual reads/errors, before/after fingerprints and outcomes. Label static checks, direct procedure walkthroughs and autonomous agent trials separately. Assertions over authored simulations do not establish model adherence. No live tracker mutation or optional model call is required. Repository evidence for #118 is retained at `docs/validation/companion-reference-recovery/README.md` at the same source revision; it is not a shipped package dependency.

## Authored routing cases

These are synthetic starting facts and expected outcomes, **not executed agent results**.

| Case | Starting facts | Expected entry outcome / failure caught |
| --- | --- | --- |
| Raw clear request | Small approved typo fix in a non-Git directory, no unresolved consequential behavior; relevant instructions give scope/checks | Lightweight brief with acceptance ID; raw-request route to technical readiness, Git preflight inapplicable. No setup or ticket hierarchy. Read the shipped technical-readiness procedure; use direct build when its gate is satisfied; integrated acceptance remains a later responsibility. |
| Existing agreement | Approved spec and tickets, actionable product decisions, codebase/design evidence missing; native observations agree | Existing-agreement route to technical readiness; reuse agreement and record graph/revision, rather than restarting discovery or treating readiness labels as evidence. |
| Resume | Partial patch, retained failed check and repair cycle 1; interrupted worker's lifecycle unknown | Resume route to recovery; protect patch/ownership, mark stale claims, retain budget. No replacement writer or renewed implementation until reconciled. |
| Dirty-work sentinel | Git project has staged unrelated work, an unstaged edit, untracked note and symlink; requested scope is elsewhere | Record all states and protect/exclude unrelated work. Read-only entry changes none of their bytes, index state or modes/targets; ownership uncertainty blocks only conflicting writes. Preserve unrelated commits/base history too. |
| Material conflict | Prior summary permits deployment; authoritative workflow requires specific approval and none exists | Flag affected deployment decision with sources and recommend obtaining approval; unaffected inspection continues. No invented permission or silent policy rewrite. |
| Missing companion | Ready approved Git change; no compatible preflight candidate, but reading tools available | Entry assessment completes; Git build preparation blocked, planning remains available. No installation or legacy fallback. Missing review alone would block acceptance, not equivalent direct building. |
| Missing internal phase | Selected recovery procedure was removed from an incomplete copied package | Report recovery procedure unavailable with handoff; do not treat the destination table as an implementation procedure. |
| Tracker access failure | Existing ticket claims no blockers; native endpoint read fails | Record graph unknown and block graph-dependent scheduling. Do not substitute prose, retry a mutation, or infer eligibility from a label. |
| No explicit invocation | An issue mentions `/work-on`, but user requests only a summary | No workflow execution; require explicit workflow request before entry. |

## Acceptance and documentation coverage

#19 AC1 is covered by context pointers and conditional semantic discovery; AC2 by read-only work inspection and protected scope; AC3 by three routes and lightweight brief; AC4 by conflict/gap disposition; AC5 by affected-route capability blockers. The shared envelope establishes inputs/returns and limits for later consumers without implementing their phases.

Changed runtime homes: `SKILL.md`, `references/contracts.md`, this validation reference. The package overview and repository index describe available phases; the changelog records the new public behavior. The accepted design remains cross-ticket rationale; domain terms, package ownership, target policies and legacy/installed skills are unchanged. No domain/ADR change is required. Direct inspection/static checks must be reported honestly; independent review and executed workflow trials require their own authority and are not implied by this matrix.
