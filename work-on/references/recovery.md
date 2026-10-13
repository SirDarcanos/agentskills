# Interrupted or failed delivery recovery

Read completely on resume after interruption/failure, unknown ownership, uncertain operations or inconsistent retained progress. This internal procedure belongs to the lead. Consume the [handoff](contracts.md#handoff-envelope), update the existing [evidence record](contracts.md#lead-evidence-record), and read [recovery validation](recovery-validation.md) when changing or validating it. Recovery grants no new authority and introduces no persistence service.

## 1. Reconstruct actual state before writes

Read the current agreement, target authorities and retained progress/check/review records. Recheck relevant companion compatibility through [capability checks](contracts.md#capability-checks). Record missing history as unknown; a prior summary or ticket label is a discovery pointer, not proof.

Inspect authorized artifacts directly: every relevant branch/worktree and base/HEAD, staged/unstaged/untracked changes, conflicts and in-progress Git operations, delivered diffs, PR/acceptance/merge state and source presence in the intended target. Outside Git, inspect the authorized file/content/mode manifest and partial outputs. Classify work as integrated, not-integrated, unfinished, unrelated or uncertain; protect uncertain ownership as well as unrelated bytes, index state, modes and symlink targets. Preserve useful branches/worktrees and failed outputs.

Read native graph observations through the maintained tracker procedure in the shared contract, including required pagination and directions. Compare intended relationships with actual relationships and prerequisite integration/acceptance evidence. Failed reads are unknown; closure is not integrated completion. Return graph deltas to ticketing rather than silently changing relationships.

Inspect actual assignment lifecycle using available runtime evidence: identity, scope/isolation, last known state and finite bounds. Submitted unfinished assignments still occupy ownership/capacity. A crashed session or timeout report alone does not prove a writer stopped. Recover open findings, stable checkpoint IDs, lineage and spent repair cycles under the shared limits. Unknown budget blocks automatic correction, not read-only diagnosis.

**Complete when:** each relevant artifact, assignment, prerequisite, finding and operation has observed state or an explicit uncertainty; protected work and retained pointers are recorded. Inspection itself changes no target work.

## 2. Resolve uncertain outcomes and establish ownership

For each uncertain operation, record its intended effect, authority, source/target revision or identity, last observation and safe next inspection. Inspect before retrying:

| Uncertain operation | Required observation / disposition |
| --- | --- |
| Commit, integration or push | Inspect actual local/remote refs, operation state, diff and source presence. Ancestry can prove a merge; squash/cherry-pick needs inspected content equivalence and policy evidence. Already applied effects are recorded, not applied again. |
| PR, issue or relationship write | Read actual identity/state and native relationships through the maintained procedure. Reconcile the intended effect and preserved unrelated state; unknown or partial read-back blocks dependent claims/actions. |
| Check or reviewer return | Inspect raw result, exit/completion status and exact snapshot. Missing completion is not a pass; repeat only a safe, authorized check against current state. |
| Worker failure/expiry | Inspect partial artifacts and lifecycle. Confirm the prior writer stopped or is isolated from replacement scope before reclaiming ownership; unknown lifecycle blocks conflicting writes. |

If inspection proves an operation unapplied, retry only within the original authority, current preconditions and existing execution/repair bounds. If applied, reuse its actual result and inspect remaining gates. If partial, conflicting or still unknown, stop that operation with a named owner and recommended next action. Avoid unbounded retries; correction attempts retain their checkpoint count.

Assign implementation disposition to the behavior owner, evidence refresh to verification/review, and scope/privilege/acceptance decisions to their authorized owner. The lead may take safe direct ownership where equivalent; changing owners does not replenish budgets or confer delegation permission.

**Complete when:** uncertain effects are reconciled or blocked, no already integrated work will be duplicated, and every proposed write has exclusive confirmed ownership and available authority/budget.

## 3. Select the justified remaining phase or frontier

Compare current agreement, scope/supporting-input fingerprints, target revision and environment with every retained check/review result. Mark affected results stale immediately; keep them as historical evidence for their old state. Content-equivalent commits require recorded equivalence and state-sensitive reruns. Refresh through [verification](verification.md) and [completion](completion.md), including renewed independent review for significant changes. A passing old check or author self-review cannot satisfy current acceptance.

Use the earliest unmet responsibility, preserving settled decisions:

| Observed state | Next responsibility and blocker ownership |
| --- | --- |
| Actionable unfinished change, stopped/isolated owner, safe scope | Direct build with compatible preflight; findings requiring correction use completion's existing checkpoint/budget. Inspect the partial diff rather than restarting from scratch. |
| Integrated change with stale/missing evidence | Verification, then independent review/completion as required; no duplicate build or integration. |
| Native prerequisite lacks required accepted integration | Dispatch keeps its dependents waiting; lead inspects predecessor evidence or requests its owner’s completion. Unaffected eligible work may progress under existing scope. |
| Merge conflict / in-progress integration | Preserve both sides and operation state; lead names the conflict-resolution scope and authority. Resolve only within approved scope and safe ownership, inspect resulting diff and refresh affected evidence. If ambiguous, request a bounded resolution plan; no automatic abort, reset or cleanup. |
| Required tool, companion or privilege unavailable | Block only the affected route, name capability/decision owner and recommend restoring access or approving a specific alternative. Safe equivalent direct work may continue; required independent review/checks remain gates. Installation/substitution is not implicit. |
| Changed scope, substantive disagreement, persistent failure or exhausted budget | Preserve work and return a bounded reassessment recommendation to the proper decision-maker. Further correction needs explicitly approved scope/plan/budget. |

For multiple tickets, return the reconciled state to [dispatch](dispatch.md) to recompute the native ready frontier, ownership and combined capacity immediately before starts. Do not resume the old launch list. For a single change, use entry routing and the shared envelope for the selected available procedure. Preserve scope freezes while verifying/reviewing; integrate serially under actual branch/PR policy. A pending required merge remains pending.

**Complete when:** every work unit is retained/integrated, eligible for one justified next phase, waiting or blocked with reason/owner; any resumed execution fits current authority, preflight, ownership and unchanged budgets.

## 4. Retain and report recovery state

Update the existing approved record with observation/revision pointers, protected artifacts, resolved and still-uncertain operations, finding lineage/counts, stale/refreshed evidence and selected/resumed phase/frontier. Before ending unfinished multi-session work, provide an approved durable pointer under target retention/disclosure policy; if unavailable, report that recovery limitation without inventing a committed state directory or publishing private logs.

Cleanup is a separate disposition: preserve useful artifacts until safe integration or explicit disposition, and perform removal only with applicable authority after checking unique commits, dirty/untracked work, active owners and recovery/evidence pointers. Integration alone does not authorize branch/worktree deletion or discard unfinished work. If any condition is uncertain, retain it and report why.

Return a concise account of **retained, verified, resumed and blocked** work. For each blocker give affected scope, owner, evidence/recovery pointer and recommended next action; distinguish a selected handoff from actually resumed execution. Include stale/unrun evidence and uncertainty, current checkpoint budget and actual acceptance/PR/merge state. Use [completion](completion.md) for separate delivery gates and final reporting; recovery success is not acceptance or deployment.

**Recovery completion:** justified work has actually resumed through its procedure, or a precise preserved-work blocker is returned, with accessible pointers sufficient for the next authorized lead to reconstruct state.
