# Review axes and report

## Independent assignments

Give both reviewers the same agreement, authority, pinned scope and raw evidence. Neither receives the other's conclusions before returning. Record reviewer identity/context, relationship to authors, source access and timeout/turn bound. They may inspect overlapping files while keeping distinct questions:

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
Freshness: initial/per-review/final comparison; path-discovery and input results
Standards: inspected files/rules; findings; checks/evidence; limitations
Spec: per-criterion covered/gap/blocked; findings; checks/evidence; limitations
Documentation: affected authoritative docs/changelog/impact policy; updates or justified no-change
Outcome: current complete / incomplete / stale / blocked review, with reason
Next action: unresolved findings, decisions and affected review/check renewal
```

Keep each original axis report accessible. Record commands, environment/baseline, exact inspected state, outcomes and evidence pointers. Distinguish **executed**, **static**, **not-run**, **failed**, and **stale**; authored scenarios are not execution evidence. A report cannot call itself complete if an axis or material scope is missing.

The caller records findings' dispositions separately (resolved with fresh evidence, accepted agreement change by its owner, deferred nonmaterial issue, or unresolved blocker). Reviewers do not silently change acceptance, mutate tracker labels, repair files, merge, publish or claim acceptance. Delivery completion requires the caller's other gates too.
