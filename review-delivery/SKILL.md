---
name: review-delivery
description: Review delivered changes against project standards and an approved spec or brief, including uncommitted work. Use for an explicit delivery review or a bounded independent-review handoff from another workflow.
---

# Review delivery

Review only; this package is the maintained independent-review owner, not a competing `code-review` implementation. It does not implement repairs, accept delivery, close issues or retire installed copies. Loading it grants no delegation, installation, disclosure, spending or mutation permission.

On every entry, read [handoff](references/handoff.md) completely for standalone inputs, bounded caller adaptation, execution-library discovery and evidence reuse. Standalone review stops at its report; a delivery handoff does not start the rest of a pipeline.

## 1. Establish agreement and authority

Identify the target, approved change/exclusions, spec or lightweight brief and acceptance IDs. Read target instructions and their relevant project, workflow, domain/ADR, documentation and release-policy pointers. Inspect primary agreement and check evidence; the author's summary is context, not proof. Record source revisions or body digests and missing material inputs.

Confirm permission for distinct read-only reviewer contexts, authorized disclosure and runtime capability: separately inspectable results, finite timeout/turn bounds and lifecycle control. Reviewers must be separate from the change's authors and each other's conclusions. Use two contexts, one Standards and one Spec; sequence them if capacity permits only one. The authorized root reserves and launches reviewers under the discovered execution library's shared limits; ticket workers request these assignments from the root. No nested delegation or automatic optional assessments.

If independence, permission, lifecycle control or material agreement is unavailable, return an acceptance blocker. Inspection by an author or delivery lead remains **lead self-review**, never independent review; other direct inspection records its actual author relationship and missing axis/context limitations. A standalone Standards-only result can be useful, but does not satisfy delivery acceptance without Spec review.

**Complete when:** scope/agreement, sources, permissions, reviewer identities and finite bounds are recorded, or the affected review gate is explicitly blocked.

## 2. Pin the actual delivered state

Read [scope](references/scope.md) completely. Resolve the comparison base, delivered revision and file inventory, including committed, staged, unstaged and relevant untracked work. Protect unrelated work; examine uncertainty before excluding a potentially material path. Empty committed diffs do not imply empty delivered scope.

Freeze writes/integration into reviewed files and supporting inputs, or use an authorized immutable snapshot. Supply each reviewer the same pinned state, actual diffs/files, agreement, standards and raw checks. Hashes identify evidence; they do not replace inspecting it. Review assignments are read-only, with explicit exclusions and result locations under target retention policy.

**Complete when:** both reviewers can inspect the full authorized state and material inputs, protected work is excluded, and the initial freshness comparison matches.

## 3. Inspect independently on both axes

Read [report](references/report.md) for axis responsibilities and required findings. Each reviewer inspects applicable instructions, the full delivered changes and relevant unchanged callers/tests/docs. Independently challenge correctness, acceptance coverage, integration/regressions, state/behavior ownership, interface depth, duplicated rules, speculative abstractions, unnecessary complexity and documentation impact. Trace findings to primary evidence; distinguish executed checks, static inspection and unrun checks. Run only safe authorized checks; read-only review does not grant arbitrary project-script execution permission.

Keep axis reports separate until both return. Partial, failed or timed-out reviews remain incomplete. Preserve results and confirm a failed worker stopped or is isolated before replacement. Do not average verdicts, ask for votes or infer coverage from reviewer agreement.

**Complete when:** each axis reports inspected files/criteria, evidence and limitations, actionable findings or an evidence-bounded no-findings result, without relying on the other axis's conclusions.

## 4. Recheck freshness and return

Repeat scope discovery and fingerprints as [scope](references/scope.md) requires, including supporting inputs and newly relevant paths. A mismatch marks affected review evidence **stale**, even when checks passed. Block acceptance until scope is repinned and affected review renewed; retain the old reports as history, not evidence for new work. If impact cannot be isolated, mark both axes stale.

Return [the report](references/report.md#return-format), separate Standards/Spec findings and unresolved blockers to the caller. The caller owns disposition, repairs and acceptance under target policy. Material unresolved findings block delivery acceptance; a judgment call requests its proper decision-maker rather than becoming an invented rule. Significant repairs need renewed review and affected checks; this package does not run that repair loop.

**Review completion:** both independent axes cover the same current scope, or the report explicitly identifies incomplete/stale/blocked evidence. Review completion alone is not acceptance, merge or release.

For changes or validation of this package, read [validation](references/validation.md).
