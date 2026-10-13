# Repair and completion

Read completely when verification/review returns findings, or integrated work needs an acceptance and report decision. This internal Work On procedure belongs to the lead; it grants no additional execution, delegation or tracker authority. Consume the [handoff](contracts.md#handoff-envelope) and maintain the existing [evidence record](contracts.md#lead-evidence-record). For changes or validation, read [completion validation](completion-validation.md).

## 1. Inspect findings and current state

Read the approved agreement, integrated artifacts/diff, raw [verification](verification.md) evidence and separate Standards/Spec reports from the discovered compatible `review-delivery`. Inspect their sources, independence, scope and freshness through [capability checks](contracts.md#capability-checks). A summary, passing suite or closed issue cannot establish acceptance. Missing review permission/capability is an acceptance blocker; lead self-review remains distinct.

Reconcile findings in the existing record: stable ID and lineage, requirement/risk and source location, materiality, owner, proposed correction/decision, affected checks/review axes, checkpoint and spent budget. Preserve original axis reports and failed/stale results. Overlapping findings may share a repair, but keep their rationales traceable. Separate binding violations from judgment calls; inspect evidence before accepting or rejecting a finding.

Give each finding a disposition: unresolved blocker; resolved with current evidence; accepted agreement change by its proper owner; or explicitly deferred nonmaterial work with rationale and an authorized follow-up location when needed. Material findings and missing material evidence cannot be deferred into success. A proposed scope reduction remains unapproved until its owner changes the authoritative agreement and consequences are recorded. Substantive disagreement goes to reassessment with a recommendation, not another vote.

**Complete when:** every finding/gap has an inspected disposition and owner, the integrated state and agreement are identified, and any stale/missing material inputs block acceptance explicitly.

## 2. Perform bounded repairs and inspect results

Use the [execution and repair limits](contracts.md#execution-and-repair-limits) as the authoritative budget/counting rules. Before a fix, recover the stable checkpoint, finding lineage and spent count; uncertain history blocks automatic repair until reconciled. Check available budget, authority, ownership and preflight. Known unavailable permission/check tooling blocks immediately. On exhaustion, disagreement or unsafe authority, stop affected execution, preserve artifacts and return diagnosis, state/evidence pointers and a recommended bounded reassessment of design, scope or environment. Further repair needs an explicitly approved revised plan and recorded budget.

Assign implementation defects to the behavior owner, evidence gaps to verification/review, and product/authority decisions to their proper decision-maker. The lead may repair directly where equivalent and authorized. A handoff is not permission to launch a worker. For delegated work, apply the shared bounds and exclusive ownership; confirm any prior owner stopped or is isolated before replacement. Integration remains the lead's responsibility, one result at a time; [dispatch](dispatch.md) owns multi-ticket scheduling/integration; [recovery](recovery.md) owns interruption/uncertain-state reconstruction before replacement or resume.

Record the cycle start before the first corrective assignment/direct fix. Supply exact owned scope, acceptance/finding IDs, expected correction, protected work, base/integrated state, meaningful checks, approval source and remaining budget. Inspect the actual returned artifacts/diff, raw checks, scope/authority compliance, documentation and integration result. A partial or failed attempt still spends its cycle; a worker's “done” does not resolve its findings.

On any relevant change, mark affected verification and review evidence stale immediately, retaining the old result for its old state. Release the old write freeze only for authorized repairs, then repin the complete integrated scope and supporting inputs and freeze writes again. Use integrated verification to rerun affected checks; new related findings/regressions retain the episode and budget. Renew affected independent review, always for significant fixes such as behavior, interface, security, persistence, acceptance or material evidence changes. If impact cannot be isolated, renew both axes and all relevant checks. For a narrowly non-significant change, record the impact analysis and why retained evidence still covers it; never silently carry an affected old verdict forward. Content-identical commits require recorded equivalence and state-sensitive reruns under the shared contract.

**Complete when:** each attempted repair has an inspected integrated result and spent count; all material findings have fresh resolution evidence, or a preserved blocker/reassessment ends the affected execution. No rename, ticket move or resumed session replenishes the same finding's budget.

## 3. Decide the separate delivery gates

Evaluate the [delivery gates](contracts.md#delivery-gates) against the current agreement and integrated snapshot. Record pass/blocked, reason and evidence pointers for each; evaluate build readiness from its approved agreement/design/ownership/dependency/preflight evidence, not retrospectively from green checks. Use the existing build/readiness returns rather than rerunning settled discovery.

For acceptance, inspect per-criterion/risk evidence, both independent review axes and every material finding's disposition. Confirm refreshed evidence covers repairs, actual files and supporting inputs, and repeat freshness/path discovery when consuming retained results. Stale, incomplete or missing material evidence blocks ready-to-accept, even if other criteria pass. An authorized acceptance change requires remapping verification/review to the changed agreement; approval alone supplies no evidence for remaining obligations. Ready-to-accept is a recommendation to the target's acceptance owner, not acceptance, merge or release permission.

Reconcile documentation before deciding ready-to-report. List affected authoritative homes and their owners, actual updates or justified no-change decisions. Route meaning/model or qualifying ADR changes through the discovered domain companion; commitments need their owner's approval. Inspect code/document conflicts against accepted primary evidence. Maintain the target's actual changelog or source fragments and resolve release impact under its policy, without inventing a generator, version source or publication authority.

Ready-to-report can pass for an honest blocked/partial outcome while acceptance stays blocked: claims must reflect evidence, documentation impact and limitations. Report neither all-green acceptance nor completed delivery while material obligations remain. Identify PR-ready, awaiting acceptance, accepted, merged, deployed and released states only when actual project-policy evidence supports them. Keep issues open until the target's completion rules permit closing. Use approved closing references and read back issue state after an authorized merge; do not merge, close or publish merely to satisfy a gate.

**Complete when:** build, acceptance and report decisions are separately traceable to the current agreement/state; documentation and release-impact dispositions are reconciled, and project completion actions are authorized or proposed only.

## 4. Reassess affected tracker readiness

After an accepted consequential decision or merge, inspect affected parent/spec and child/work-ticket readiness using the target's mapped roles, title/readiness policy, actual agreement revisions and accepted integration evidence. Use the discovered maintained tracker procedure for paginated native parent/blocker observations and both directions; do not duplicate its graph algorithm. Include affected dependents and relevant predecessors, bounded to the event's impact; record unavailable graph reads as unknown, not absent dependencies.

Evaluate each item's actionable agreement separately from execution eligibility. A ready parent enables coordination of eligible children, not a second implementation unit. An actionable child may remain labeled ready while its blockers prevent starting. A closed predecessor without required integration/acceptance evidence does not unblock its dependent. Preserve unrelated labels, native parentage and blocker edges; a readiness reassessment is not permission to rewire the graph, change role labels or expand the backlog.

Return a compact delta per affected item: identity/role, observed labels/relationships, accepted event/evidence, readiness versus eligibility, exact proposed additions/removals or no-change rationale, and mutation authority. Apply only the exact changes within current approval, following the target mapping and maintained procedure. Without authority, return the proposed delta and leave the tracker unchanged; this does not erase the assessment or authorize scheduling. A no-op rerun makes no mutation.

Re-read changed assignments and relevant native relationships, compare with the intended delta and preserved unrelated state, and record actual identifiers/results. Failed, partial or uncertain operations remain explicit; inspect before any authorized retry. Failed read-back blocks claims that readiness was reconciled and any dependent action relying on that claim.

**Complete when:** affected parent/child readiness and execution eligibility have evidence-based dispositions; authorized changes are read back, or proposed/unknown deltas and their blockers are reported without permission expansion.

## 5. Return the delivery report

Give the user a concise outcome, with technical evidence accessible through the existing record rather than requiring code inspection:

- **Implemented:** delivered behavior/artifacts and integrated revision/worktree pointer; distinguish partial and not-integrated work.
- **Verified:** acceptance/risk coverage, actual check and independent review evidence at the current snapshot, with limitations.
- **Unverified:** unrun, stale or uncertain checks/criteria and consequences; identify material gaps also under blocked work.
- **Deferred:** only accepted deferrals/nonmaterial follow-ups, their rationale and owner; preserve original required commitments until approved otherwise.
- **Blocked:** unresolved material findings, unavailable authority/capability, exhausted checkpoint/count, affected dependencies and recommended next action.
- Documentation/changelog/release-impact disposition, separate gate decisions, actual PR/acceptance/merge/issue state, and tracker changes versus proposed deltas.
- Only consequential decisions requiring user input, phrased as consequence plus recommendation. Routine engineering stays with the lead.

Mark empty categories explicitly or combine them concisely without hiding uncertainty. Preserve failed attempts, original reports and freshness/budget history at the authorized evidence location; avoid publishing private logs. Do not turn a script's expected-failure exit 0, authored scenario or reviewer consensus into a delivery pass.

**Completion:** an evidence-backed delivery report or explicit preserved blocker, with remaining decisions and next action. This procedure does not imply deployment, release, global installation, or completion of multi-ticket dispatch or recovery.
