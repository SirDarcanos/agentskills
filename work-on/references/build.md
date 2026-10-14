# Direct build

Read completely when entry selects one cohesive implementation with an actionable agreement and technical plan. This is an internal procedure of an explicitly requested Work On run, not a separate command. Use the [handoff contract](contracts.md#handoff-envelope); for changes or validation, read [build validation](build-validation.md).

## 1. Establish the build gate and ownership

Consume the approved brief/spec revision, acceptance IDs, exclusions, context/authority pointers, technical plan and verification strategy. Inspect their freshness against the affected files, interfaces and actual work state. Reuse settled decisions; route missing design evidence to [technical readiness](technical-readiness.md) and changed product commitments to [product agreement](product-agreement.md).

Confirm one owner for this bounded deliverable and its relevant interfaces. Direct execution is the default when coordination adds no value. Preserve unrelated committed, staged, unstaged and untracked work, including modes and symlinks; record protected scope and uncertain ownership before writes. Active or unknown competing owners block conflicting writes until reconciled. This procedure neither launches workers nor integrates their results.

For a ticket, consume entry's native blocker observations and accepted predecessor outputs. Refresh stale or unknown graph/completion evidence through the maintained tracker procedure in [capability checks](contracts.md#capability-checks). Unmet blockers or missing required integration evidence block dependent building; labels and issue closure alone are insufficient. A small approved direct request needs no ticket hierarchy.

Before any implementation writes in Git, discover and read the complete compatible `implementation-preflight` entry point and applicable references through the shared capability contract. Perform its maintained procedure; inspect the resulting HEAD, branch/base/PR target, existing PR state and preservation of protected work. Explicit target branch policy wins over incidental branch names. Record the companion source/revision and actual outcome rather than copying its branch algorithm here. Outside Git, mark preflight inapplicable and retain a before/after file manifest.

**Complete when:** approved behavior and verifiable acceptance, actionable design/risks/dependencies, exclusive ownership, sufficient authority and safe preflight are evidenced. A missing compatible preflight blocks Git preparation; inspection/planning can continue. Unknown permission remains ungranted.

## 2. Select development checks and method

Inspect existing assertions and documented commands for the affected behavior, not merely test names or totals. Map acceptance and meaningful risks to existing coverage or a needed check, with expected results, environment and baseline status. Extend adequate coverage rather than adding redundant permutations. Protect meaningful failure paths for access/disclosure, destructive actions, persistence/recovery and important domain rules when relevant.

Run safe relevant baseline checks when useful and authorized. Record actual command, exit/result and state checked; distinguish pre-existing failures from new regressions. If a material check cannot run, retain its reason and evidence gap, and choose only safe progress within authority. Missing tooling does not authorize installation or make the baseline green.

Choose a method suited to the change, respecting binding project policy:

- For reproducible bugs and logic changes, select test-first development when useful. The discovered compatible `tdd` companion owns the complete red–green–refactor procedure; read its full entry and applicable references, supply the current bounded agreement/check mapping/authority/state, execute in this context and inspect its local evidence return. Do not duplicate its loop here. Missing or incompatible TDD blocks the selected test-first route, not inspection or a separately justified method choice.
- For already-covered behavior, copy edits or mechanical changes, existing checks or focused inspections may suffice. Record why they address the distinct failure risks; no blanket TDD, new-test quota or universal suite applies.
- If project policy mandates TDD or another check, follow it or seek its owner's approved revision. This procedure retains method choice; selecting TDD uses the maintained companion, never an incompatible legacy `/tdd` or implementation command.

**Complete when:** each material acceptance/risk has a development check or explicit gap, baseline claims have evidence, and the method and required environment are known.

## 3. Implement within the agreement

Modify only the owned scope, retaining suitable existing responsibilities and interfaces. Build directly in coherent slices and execute relevant checks as behavior changes. Refactor when it improves the affected design while relevant checks remain green; keep behavior, scope and authority stable rather than postponing all structural work to review.

Routine technical refinements stay with the owner: update the technical brief and check mapping when new evidence changes the approach. Escalate changed product commitments, expanded scope, meaningful authority/cost/risk changes or material uncertainty with evidence and a recommended bounded next step. Pause affected writes pending approval; preserve partial artifacts and continue only unaffected safe work. Required meaning/model or qualifying ADR changes return through technical readiness's domain handoff.

On failed checks, inspect the actual failure and separate baseline/environment limitations from regressions. Preserve unfinished and unrelated work. Apply the shared [execution and repair limits](contracts.md#execution-and-repair-limits) whenever correcting checkpoint findings; retain finding lineage and spent budget across interruptions. Known missing permission/tooling blocks immediately; persistent failure or exhausted budget returns diagnosis and reassessment rather than an unbounded repair loop.

Update the authoritative documentation changed by the implementation under target policy. Maintain its actual changelog/fragments and release-impact classification for notable public changes, or record a justified no-change decision. Domain meanings and approved product commitments retain their own owners; release classification grants no publication authority.

**Complete when:** the owned change is implemented or a preserved partial result is identified, relevant checks are current or explicitly failed/unrun, and scope/documentation decisions remain within authority.

## 4. Return local correctness evidence

Inspect the actual delivered diff/files against acceptance, protected work and target instructions. Confirm protected bytes, index state, modes/targets and unrelated history remain intact where applicable. Record deviations rather than calling preservation successful from an unchanged filename list.

Return the shared evidence record and handoff, including:

- Changed behavior/artifacts and acceptance references; implemented, partial, deferred and blocked scope.
- Actual development commands/results and why they address the meaningful risks, baseline failures, new failures, uncertainty and unrun checks. Identify the exact checked state, scoped dirty-work fingerprint and relevant supporting inputs through the [lead evidence record](contracts.md#lead-evidence-record). Refresh affected evidence after subsequent writes.
- Documentation/changelog updates or justified no-change decisions and release-impact disposition under target policy.
- Owner, companion/preflight result, branch/base/HEAD/PR pointers or non-Git manifest, protected/excluded work, dependencies and next action. Retain repair/progress state when applicable.
- Review and integration limitations: explicitly identify independent review or integrated acceptance checks as absent unless actually performed at the recorded scope. Direct inspection is not independent review.

The lead inspects actual artifacts and raw check evidence, not only a success summary, and selects the next verification/review gate. Report an unavailable next procedure as an affected blocker with a concrete next action; locally implemented work can still be handed off. Keep ticket closure, acceptance/merge, deployment and release subject to their separate project gates and permissions.

**Build completion:** one owner returns a truthful local correctness handoff or preserved partial/blocking result. Local implementation and passing development checks are not final acceptance.
