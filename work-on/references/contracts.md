# Delivery contracts

Read on each authorized entry and before handing work to a procedure or companion. This is the shared runtime contract; phase-specific procedures own their detailed actions. A handoff can stay in the lead's context and never launches a worker by itself.

## Capability checks

For each needed dependency: discover candidates through the runtime/project, read the complete entry point and relevant branch-specific references, identify source/revision (or content digest), compare its behavior with the requirements below, and record the resolution. Compatibility is semantic; no particular version marker, literal `Skill` tool, SDK, installation tree, or judgment service is required. Ambiguous candidates block that route until disambiguated. Recheck changed companion files, authority, and resumed-task requirements.

| Dependency / condition | Required behavior | Unavailable or incompatible outcome |
| --- | --- | --- |
| File tools and project checks | Inspect actual authorized files; edit only within approved scope; execute applicable existing checks when needed | Inspection can proceed with read access. Missing writes blocks building; unrun material checks block acceptance. |
| `implementation-preflight`, before implementation writes in Git | Preserve dirty work; honor explicit project branch policy over incidental branch names; select correct base and PR target; avoid implicit resets or work transfer | Block Git implementation preparation; planning may continue. Mark inapplicable outside Git. |
| `domain-modeling`, for meaning/model changes or qualifying ADRs | Plan-only/approved bounded handoffs, source/document mapping, proposed versus accepted status, preserved rationale and per-operation evidence | Block the required modeling work. Reading existing definitions is not a modeling invocation. |
| `review-delivery`, for independent review and acceptance | Pin the complete delivered scope including dirty work; independent inspection; separate Standards/Spec reports; stale-snapshot detection; authority/capability blockers | Building may yield implemented-but-unaccepted work. Acceptance stays blocked; legacy review is not a silent substitute. |
| Maintained tracker procedure, for native graph inspection, publication or scheduling | Target-specific authority, native parents and blockers, identity and pagination handling, cycle checks, additive reconciliation and read-back | Block affected graph decisions/operations; direct approved work without a graph may continue. An alternative representation needs explicit agreement. |
| Delegation runtime, only for an authorized delegated assignment | Separately inspectable results, bounded lifecycle control, exact authorized scope and suitable ownership/isolation | Use direct execution where equivalent. Independent review still requires distinct reviewer contexts and permission. |

For GitHub, locate `setup-project` through discovery and read its maintained `references/issue-tracker.md` as a procedure library, not an invocation of setup. Its helper is optional and limited to its documented scope. Target policy owns operations and authority. Other trackers need an inspected project-approved native procedure. Do not duplicate the graph algorithm here. Installation, replacement, new disclosure and spending require separate approval.

## Handoff envelope

Every internal or companion handoff supplies:

1. **Agreement:** target, task/spec/brief source and revision or inspected-body digest, acceptance IDs, purpose and exclusions.
2. **Context:** authoritative pointers, observed evidence, confirmed decisions, assumptions and unresolved questions. Receivers inspect relevant sources rather than treating the summary as proof.
3. **Authority:** inspection/plan-only or exact approved operations, approval source, permitted effects and unavailable permissions.
4. **Ownership/state:** owned files/behavior/interfaces, protected unrelated work, branch/base/integration pointers where applicable, dependencies and observed completion evidence.
5. **Result contract:** expected artifacts/decisions, meaningful checks and evidence, blocking conditions and applicable execution/repair budget.

A delegated assignment additionally names the exact worker, exclusive ownership, isolation, finite timeout/turn bound and permission scope. Workers may not delegate recursively. Independent review receives the agreement, actual sources/changes and raw evidence, not the lead's preferred verdict.

Every return identifies actual outcomes, changed artifacts and delivered state, criterion/check evidence, remaining uncertainty, findings, documentation impact and next action. Failed/partial operations retain their status. The lead inspects relevant artifacts, checks scope/authority and evidence freshness, and selects the next gate; a worker's “done” or specialist judgment cannot override human product/authority decisions.

## Lead evidence record

Use compact Markdown at the target's approved task/PR location under its retention/disclosure policy. A small direct change may keep the record in the conversation and final PR report. A multi-session run needs an approved durable artifact/pointer before leaving unfinished work; do not default to a new committed state directory or publish private logs.

| Field | Minimum content |
| --- | --- |
| Agreement/context | Target, source/revision, acceptance IDs, approved scope/exclusions, authoritative decisions and permission pointers, conflicts and resolution |
| Entry/state | Route and rationale, next responsibility/availability, companion source and compatibility, branch/worktree, resolved base/HEAD, scoped changed-path inventory and working-tree fingerprint, protected/excluded work and inclusion rationale |
| Checks | Criterion/risk, command or inspection, environment/baseline, exact state checked, result and evidence location; label executed, static, not-run, failed or stale |
| Review | Reviewer identity/independence, Standards/Spec reports, pinned snapshot, findings and disposition; explicitly record absent/incomplete review |
| Progress/recovery | Native graph observation and limitations, assignment ownership/revision/bounds, active workers, integrated/not-integrated state, repair checkpoint/cycle counts and uncertain operations |
| Outcome | Implemented, verified, unverified, deferred and blocked scope; documentation/changelog/impact disposition, limitations, decisions and next action |

Mark inapplicable fields; do not fabricate missing evidence. Preserve enough history to explain changed results and budget use. Fingerprint only authorized scope and avoid retaining secret contents. Before execution/review, dirty scope identification must distinguish staged/unstaged changes and included untracked content/modes or symlink targets, deletions/renames and relevant supporting inputs. Non-Git work uses a before/after content/mode manifest. HEAD alone does not identify dirty work. `review-delivery` owns the detailed delivered-snapshot format; an entry inventory is not a substitute for that pinned review scope.

Changed scope invalidates affected evidence. Reviewers need actual diff/files and relevant context, not hashes alone. Freeze scoped writes or use an immutable authorized snapshot and compare fingerprints before/after review. After repair, refresh affected checks and significant-change review. A content-identical commit may retain content evidence only with recorded equivalence; state-sensitive checks still rerun.

## Execution and repair limits

These limits constrain all consumers; entry does not itself dispatch, repair or integrate. [Repair/completion](completion.md) implements checkpoint disposition and gate decisions; [dispatch](dispatch.md) implements frontier scheduling, bounded assignments and incremental integration; [recovery](recovery.md) implements actual-state reconstruction and justified resume after interruption/failure.

- At most **two active non-lead workers** across building, exploration and review, or fewer under runtime/project limits. Submitted unfinished assignments occupy slots even when idle. Declare finite runtime bounds before launch; workers cannot recursively delegate or automatically call optional models.
- Writes need independent exclusive ownership, stable interfaces and suitable isolation. Shared interfaces serialize or have one owner. The lead alone integrates one result at a time under target branch policy; freeze writes/integration into a scope during its verification/review snapshot check.
- Review uses two read-only contexts, Standards and Spec, separate from the reviewed scope's authors and from each other's conclusions. They may run sequentially with one slot. Lead self-review is not independent review.
- On failure/expiry, preserve artifacts and inspect progress. Replacement begins only after the prior owner is confirmed stopped or isolated. Resume reconciles actual workers; a crashed session does not free ownership.
- Allow at most **two automatic repair cycles per work-unit acceptance checkpoint**, including a final integration checkpoint for cross-ticket findings. Record stable checkpoint ID, finding lineage, counts and budget. First corrective assignment/direct fix starts a cycle; failed/partial attempts spend it. Diagnosis alone is not a repair cycle, but delegated diagnosis is bounded.
- Related new findings/regressions remain in the episode. Moving/renaming a finding or resuming does not reset its count. Current evidence resolving all material findings ends an episode; recurrence of the same unresolved cause earns no fresh budget.
- After cycle two with material findings remaining, or earlier substantive disagreement/unsafe authority, stop affected execution. Return diagnosis, preserved state and a recommendation to reassess scope/design/environment. Further repair needs an explicitly approved revised plan/budget. Known missing permission/tooling is an immediate blocker, not two retries.

## Delivery gates

Consumer procedures must establish these gates; [repair/completion](completion.md#3-decide-the-separate-delivery-gates) records their decisions. Routing is not evidence that they passed.

- **Build:** approved actionable behavior and verifiable acceptance, known material design/ownership/dependencies/risks, sufficient authority and safe preflight.
- **Accept:** integrated-state acceptance/risk evidence and independent Standards/Spec review; material findings resolved or acceptance explicitly changed by its owner; evidence refreshed after repairs.
- **Report:** evidence-backed implemented/verified/unverified claims, documentation impact, limitations and consequential decisions. PR readiness, accepted/merged and deployed/released remain distinct under target policy.

The phase changing a fact updates its existing authoritative document. Use the target's documentation ownership, actual changelog/fragments, versioning and label mappings; a justified no-change decision is valid. Specification and work-ticket roles remain distinct from independently assessed readiness and native relationships. Release classification authorizes no publication. Consumer procedures implement their gates and tracker mutations within their own approved scope.
