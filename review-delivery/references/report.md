# Review axes and report

## Independent assignments

Give both reviewers the same inspected agreement, authority, pinned scope and raw evidence after the [handoff checks](handoff.md). Neither receives the other's conclusions before returning. Record reviewer identity/context, relationship to authors, source access and timeout/turn bound.

Before launch, check the review packet and permitted search roots:

1. Supply the approved agreement, actual source/diffs, standards and raw checks for the pinned scope. Keep progress metadata outcome-free; omit prior reviewer verdicts, quoted findings and the lead's preferred outcome from packet narratives and supporting inputs. Retain original reports separately as history, unchanged.
2. Give explicit file/search boundaries that exclude prior axis reports and retrospective commentary. A fresh context alone does not prevent exposure through a broad repository search. If a material source cannot be made available independently, return that blocker rather than hiding it.
3. If a reviewer sees excluded conclusions, stop consuming its result and retain it as ineligible. Preserve the exposure record, confirm terminal completion or isolation before replacement, correct the packet/boundaries and renew affected axes within the shared worker limit. Record what was actually observed; an allowlist is a procedural boundary, not proof of filesystem isolation.

**Packet complete when:** both assignments have independently inspectable source/evidence, neutral inputs and explicit search boundaries, or the review gate is blocked. They may inspect overlapping files while keeping distinct questions:

| Axis | Required challenge |
| --- | --- |
| Standards | Apply actual runtime/project/directory instructions. Check correctness, integration/regressions, state and behavior ownership, useful interfaces hiding complexity, duplicated rules, speculative abstractions and unnecessary layers/configurability. Check documentation, changelog/release classification and policy consistency. Cite binding instructions; architecture preferences remain judgment calls unless grounded in a requirement or demonstrated failure. |
| Spec | Trace every in-scope acceptance ID to delivered behavior and actual evidence, including failure paths and relevant regression/integration risks. Inspect sources/tests rather than trusting totals. Identify missing behavior, incorrect interpretation, unsupported verification, scope creep and documentation promises conflicting with the agreement. Distinguish accepted limitations and exclusions from new defects. |

Both can raise cross-cutting issues; preserve their original rationale rather than forcing unique findings. Check relevant unchanged callers, interfaces, tests and documentation. Missing material input/access, incomplete criteria coverage or unavailable material check remains an explicit gap. No-findings means no findings in the stated inspected scope, not proof of correctness.

## Findings

For each finding provide:

- Stable ID, axis and exact file/line or artifact/criterion location at the pinned state.
- Observed behavior and reproducible evidence (or clearly labeled static reasoning).
- Requirement/policy source for a binding violation, or explicit **judgment call** with alternatives/consequences.
- Rationale: user/operational impact and why this is material. Classify **blocking**, **nonblocking**, or **decision required**; explain rather than relying on a severity number.
- Actionable correction or bounded investigation, affected scope/checks and uncertainty.

A style preference without a policy or meaningful risk is not a binding acceptance failure. Conversely, a material correctness/coverage gap does not become optional just because no style rule describes it. Substantive disagreement goes to the caller/proper decision-maker with evidence, not another vote.

## Return format

Use Markdown; no required machine schema:

```text
Agreement: reference/revision or digest; acceptance IDs; exclusions
Snapshot: record pointer; base/HEAD or non-Git manifest; included paths/support
Independence: reviewer/context per axis; author relationship; authority and bounds
Execution: resolved library source; root/record pointer; slots and finding/checkpoint lineage
Freshness: initial/per-review/final comparison; path-discovery and input results
Standards: inspected files/rules; findings; checks/evidence; limitations
Spec: per-criterion covered/gap/blocked; findings; checks/evidence; limitations
Documentation: affected authoritative docs/changelog/impact policy; updates or justified no-change
Artifacts: original axis report locations; changed target artifacts (none for read-only review)
Outcome: current complete / partial (incomplete) / stale / blocked review, with reason
Next action: unresolved findings, decisions and affected review/check renewal
```

Keep each original axis report accessible. Record commands, environment/baseline, exact inspected state, outcomes and evidence pointers. Distinguish **executed**, **static**, **not-run**, **failed**, and **stale**; authored scenarios are not execution evidence. A report cannot call itself complete if an axis or material scope is missing.

The caller records findings' dispositions separately (resolved with fresh evidence, accepted agreement change by its owner, deferred nonmaterial issue, or unresolved blocker). Reviewers do not silently change acceptance, mutate tracker labels, repair files, merge, publish or claim acceptance. Delivery completion requires the caller's other gates too.
