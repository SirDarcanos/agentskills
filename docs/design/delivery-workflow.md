# Delivery workflow design contract

Design deliverable for [#18](https://github.com/SirDarcanos/agentskills/issues/18), implementing the design portion of [spec #14](https://github.com/SirDarcanos/agentskills/issues/14). Read before implementing #19–#31 or changing the delivery contracts. This document defines the intended implementation; it is not an installed skill or evidence that the workflow works.

## Status and authority

- **Confirmed:** #14's product commitments and ticket graph, and the maintainer's request to complete #18. Project authority, verification, and delivery rules remain in [workflow](../agents/workflow.md); domain meanings remain in [CONTEXT](../../CONTEXT.md).
- **Recommended design, pending acceptance of #18:** the concrete names, package boundary, companion contracts, limits, and evidence representation below. These choices are ready for implementation after acceptance, rather than questions delegated to later tickets.
- **Consequential acceptance:** accept or revise the two-package boundary and new public invocation names through the #18 PR. No product-scope expansion, paid dependency, global replacement, or additional configuration is proposed. Downstream work remains blocked until this design is accepted and merged; this document does not change readiness labels.
- **Deferred:** optional Nimble/Jev/Clef checkpoints, legacy-command migration, a general runtime adapter framework, and broader runtime certification. None is an implicit implementation requirement.

[Inventory and provenance](delivery-workflow-inventory.md) records observed behavior separately from this design. [ADR 0001](../adr/0001-delivery-workflow-ownership.md) records the package-boundary rationale. [Design validation](delivery-workflow-validation.md) contains acceptance coverage and paper walkthroughs, not executed workflow trials.

## Package and invocation boundary

Implement two new skill packages. These names were absent from the inspected installed-skill inventory; recheck collisions before any future installation.

| Package / invocation | Responsibility and invocation contract |
| --- | --- |
| `work-on` / `/work-on <request, spec, issue, or ticket set>` | Explicitly requested delivery entry point, with `disable-model-invocation: true` and an in-body explicit-request gate. Owns phase selection, integration, repair, and completion accountability. It reads its shipped specialist references internally; it does not invoke command-only legacy skills behind the user's back. |
| `review-delivery` / `/review-delivery <scope>` | Independently useful review package, also discoverable by another workflow. Its description routes explicit reviews and bounded delivery-review handoffs; it has no command-only gate. Loading it does not grant delegation, disclosure, or mutation permission. |

The working responsibilities called `/analyze`, `/dispatch`, `/verify`, revised grilling, `/to-spec`, and `/implement` in #14 become procedures inside `work-on`, not new public commands. They remain separable responsibilities with the handoffs below. Review remains a companion because independent review is also useful outside delivery. Domain modeling and Git preflight retain their existing owners.

The intended package-local homes are below. These are implementation destinations, not links to files that already exist. Add only the files needed by the implementing ticket; incomplete routes must report unavailable rather than implying the entire workflow has shipped.

| Home | Authoritative procedure | Ticket |
| --- | --- | --- |
| `work-on/SKILL.md` | Explicit invocation, context read pointers, routing, lead obligations, completion gates | #19; gates connected in #26 |
| `work-on/references/contracts.md` | Internal handoff envelope, lead evidence record, capability checks, concurrency and repair limits | #19 establishes the contract; #26/#27 implement its consumers |
| `work-on/references/product-agreement.md` | Discovery and brief/spec authoring, concern disposition, approval and spec-label read-back | #20 |
| `work-on/references/technical-readiness.md` | Codebase-informed design, risk/verification plan, domain handoff | #21 |
| `work-on/references/ticketing.md` | Cohesive decomposition, exact graph approval, use of the maintained tracker procedure | #22 |
| `work-on/references/build.md` | Direct building, optional test-first method, local correctness handoff | #23 |
| `review-delivery/SKILL.md` and its package-local scope/report references | Independent review procedure, pinned scope format, Standards/Spec findings | #24 |
| `work-on/references/verification.md` | Integrated acceptance evidence and risk-based checks | #25 |
| `work-on/references/completion.md` | Repair episodes, renewed checks/review, acceptance and director-level report | #26 |
| `work-on/references/dispatch.md` | Ready frontier, assignments, ownership and serial integration | #27 |
| `work-on/references/recovery.md` | State reconciliation, interrupted work, failure disposition and resume | #28 |
| Package-local validation references/fixtures and READMEs | Executed trial evidence, installation/discovery and limitations | #29–#31; each earlier ticket still validates its own changes |

Keep procedure instructions in those runtime homes once implemented. This design remains the cross-ticket contract and rationale, not a second step-by-step runtime manual. Implementation tickets must reconcile changed design facts here; substantial changes to accepted ownership use the ADR process. Package-local links stay inside the copied package. Companions are reached through runtime discovery, never `../other-skill` or a workstation path.

### Existing commands

Leave installed `/implement`, `/implement-spec`, `/code-review`, `/grilling`, `/to-spec`, `/to-tickets`, `/tdd`, and their source packages unchanged. Do not create aliases, remove commands, or interpret their names as the new contract. The workflow uses newly authored procedures satisfying #14 rather than wrapping incompatible instructions and trying to override them.

`review-delivery` deliberately avoids shadowing the installed `code-review`. Both may coexist; documentation must distinguish them. No legacy command is a hidden dependency or fallback. An explicit future migration would need its own approved installation and compatibility plan.

## Context and capability contract

At entry, read actual target-project authorities through their existing pointers. Use setup-produced documents when present; do not require a particular tree, run setup automatically, or infer a team/risk profile. A small change needs enough context to establish scope, checks, permissions, and completion, not a forced onboarding run. Missing material context or contradictory authority blocks the affected decision; the lead investigates facts and recommends resolutions.

Basic execution needs file inspection/editing and the target project's existing check tools. Git is needed for Git operations, not for reading a local brief. No literal `Skill` tool, agent SDK, or hosted judgment service is required. Before choosing delegation, the runtime must offer separately inspectable worker results, bounded lifecycle control, and an authorized scope. If not, use direct execution where equivalent; independent review remains a separate gate and cannot be replaced by lead self-review.

Compatibility is semantic, not a name or version-string match. Discover a candidate, read its complete entry point and branch-specific contract, identify its source, check the capabilities below, and record the resolved procedure/revision. If multiple candidates cannot be disambiguated, stop that route. Existing companions need no retrofitted version marker to qualify. Recheck when their files, authority, or the resumed task changes. Installation, replacement, new disclosure, and spending require their own permission.

| Dependency / when needed | Required compatibility | Missing or incompatible outcome |
| --- | --- | --- |
| `implementation-preflight`, before writing implementation in Git | Preserves dirty work; honors explicit project branch policy; selects the correct base/PR route; does not reset or transfer work implicitly | Block Git implementation preparation; planning can continue. Non-Git work records the route as inapplicable. |
| `domain-modeling`, when changing meanings/models or qualifying ADRs | Plan-only and approved bounded handoffs, source/document mapping, proposed/accepted distinction, historical rationale and per-operation evidence | Block required modeling work. Reading existing definitions alone requires no invocation. |
| `review-delivery`, before acceptance and for explicit review | Pinned full delivered scope, independent inspection, separate Standards/Spec reports, stale-scope detection, permission/capability blockers | Build may return implemented-but-unaccepted work; ready-to-accept is blocked. Never silently substitute the legacy review. |
| Maintained tracker procedure, when publishing or scheduling a tracker graph | Project-specific authority, native hierarchy and blockers, identity/pagination/cycle handling, additive reconciliation and read-back | Block affected remote publishing/scheduling. A direct approved change without a tracker graph may continue. An alternative representation needs explicit agreement. |
| Target project's discovered check tools | Can actually run the applicable checks under current authority | Record unexecuted evidence; material gaps block acceptance. Ask before installing anything. |

For GitHub, reuse the procedure already maintained in the `setup-project` package's `references/issue-tracker.md` and its optional dependency helper. #22 must make this read-only library use explicit in that package's compatibility documentation and the caller; reading the procedure does not invoke `/setup-project` or authorize setup mutations. Locate the package through discovery, not a sibling assumption. Target-project tracker policy remains the authority for the target and approved operations. Do not copy the native graph algorithm into `work-on` or extract a new shared package just to avoid this conditional dependency. The helper remains optional and limited to its documented scope; the procedure owns parentage and unsupported cases. Other trackers need an inspected project-approved native procedure, not an invented universal API.

TDD is a development method inside the build responsibility, not a mandatory companion. A compatible separately requested method may be used under its own rules; the inspected installed TDD skill is not silently invoked because its seam-approval and refactoring rules differ from #14. Optional advisory assessments remain deferred and explicit-invocation/consent gates remain binding.

## Handoff contract and responsibilities

An internal procedure can run in the lead's context. A handoff alone never launches another agent. For a delegated assignment, the lead also supplies an exact worker identity, ownership, runtime bounds, and permission scope; workers cannot recursively delegate under this contract.

Independent review uses two read-only reviewer contexts, one for Standards and one for Spec, each separate from the authors of the reviewed scope and from the other axis's conclusions. Run them sequentially when only one worker slot is available. `review-delivery` defines these assignments; the lead launches them through the authorized runtime without worker-side recursive delegation. A standalone invocation places that lead role with its caller. Reviewers get the agreement, source changes and raw evidence; the lead's preferred verdict is not an input.

Every handoff carries:

1. Target, task/spec revision and acceptance IDs; purpose and explicit exclusions.
2. Existing evidence and authoritative context pointers, confirmed decisions, and unresolved questions. Receivers inspect relevant sources rather than blindly trusting a summary.
3. Mode: inspection/plan-only or approved operations; approval source and exact permitted effects. Unknown authority is ungranted.
4. Owned files/behavior and interfaces, protected unrelated work, integration/base pointers, and known dependencies.
5. Expected result, appropriate checks/evidence, blocking conditions, and applicable execution/repair budget.

Every return identifies actual outcomes, changed artifacts and delivered state, criterion/check evidence, remaining uncertainty, findings, documentation impact, and next action. Failed/partial operations retain their status; a result labeled done is not sufficient. The lead reads relevant changed artifacts and evidence, checks scope/authority and freshness, and decides the next gate. Specialist judgment never overrides the human's product/authority decisions.

| Responsibility | Additional input; owned decision | Output and lead inspection | Blocking condition |
| --- | --- | --- | --- |
| Lead / entry | Request, actual project/work state; owns phase selection and routine engineering within authority | Context/permission map, actionable scope and route; inspect live state against supplied history | Material authority conflict, unknown scope, unsafe branch/work state |
| Product discovery | Known intent and collaboration preference; owns which unresolved product branches to explore, not their consequential answers | Manageable rounds and four concern dispositions; check relevant branches are addressed/deferred and decisions have owners | Unresolved consequential product choice |
| Specification | Confirmed intent; owns brief/spec expression and verifiable acceptance IDs | Behavior, rationale, exclusions, accepted limitations, approvals and mapped spec-label read-back; lead checks fidelity and no accidental readiness claim | Unapproved commitment or unverifiable material criterion |
| Technical analysis | Actionable brief, codebase, domain/ADRs and existing coverage; owns technical structure and verification recommendation | Responsibilities, reuse, interfaces, dependencies, risks and complexity rationale; lead inspects code fit and documentation needs | Material design uncertainty or changed product commitment requiring approval |
| Domain modeling | Exact modeling subject and document mapping; owns terms/relationships and qualifying records | Companion's planned/applied delta with evidence; lead compares actual documents to authority and preserved history | Missing compatible companion, approval or meaning/decision evidence |
| Ticketing | Ready brief/technical plan and current tracker state; owns cohesive boundaries and proposed graph | Tickets, acceptance references and verified native edges; lead compares intended and persisted graphs, not mentions | Unapproved edge, graph conflict, unavailable native capability or failed read-back |
| Git preflight | Working tree, branch/PR evidence and project convention; owns safe branch-route recommendation/preparation within authority | Selected branch/base/target and preserved work; lead verifies actual HEAD and PR state | Ambiguous ownership or operation needing ungranted destructive/transfer authority |
| Dispatch / integration | Verified graph, completion evidence, ownership map and worker capacity; owns scheduling and integration order | Bounded assignments and integrated revisions; lead checks ready frontier and actual integrated changes | Unmet blocker, overlapping ownership, invalid evidence or unavailable isolation |
| Building / optional TDD | Ready scope, preflight result, verification strategy; owns local engineering and method choice | Implementation and local evidence; lead inspects changes and required docs, not just test totals | Changed commitments, missing authority, unsafe operation or persistent failed checks |
| Acceptance verification | Integrated state, acceptance/risks and observed baselines; owns check selection/execution and evidence sufficiency assessment | Per-criterion verified/unverified/blocked results; lead compares evidence to interpretation and revision | Material check unavailable, regression, unsupported claim or stale evidence |
| Independent review | Pinned delivered scope, spec/brief, standards and raw evidence; owns independent Standards/Spec challenge | Separate findings with locations, rationale and materiality; lead inspects findings and records their disposition | Reviewer independence/capability missing, incomplete scope, changed snapshot or missing material agreement |
| Repair / completion | Findings, evidence, budget and project closing/release policy; lead owns repair assignment and readiness | Refreshed evidence, disposition and concise delivery report; lead verifies gates and documentation consistency | Material unresolved finding, exhausted budget, stale/missing evidence or unapproved acceptance change |

## Execution and repair bounds

### Concurrency and ownership

The first-version ceiling is **two active non-lead workers per delivery run**, across implementers, exploration, and reviewers combined. Use fewer under runtime/project limits or when coordination adds no value. An active worker includes a submitted but unfinished assignment; inactivity does not free its slot. The lead doing direct work is not a worker slot, but still obeys ownership and scope-freeze rules. No nested delegation or automatic optional-model calls.

Before launch, declare the assignment's finite timeout/turn bound using the available runtime and expected work. On expiry/failure, preserve artifacts and inspect actual progress before reassignment. The runtime must support a bounded lifecycle; otherwise the delegated route is unavailable. A replacement starts only after the earlier owner is confirmed stopped or isolated from the scope. A crashed session does not reset active ownership; resume reconciles actual workers first.

Two workers may write only independently owned scopes with stable agreed interfaces and suitable isolation. Shared module/interface edits serialize or go to one owner. The lead alone integrates, one result at a time, using project branch/PR policy; no integration branch or merger agent is mandatory. Pause writes to the scope under verification/review. Do not integrate into that scope until its snapshot check is complete. Read-only review axes may run sequentially when only one slot is available.

Two is a conservative initial ceiling: it supports one useful parallel pair while keeping ownership and integration inspectable. Raising it requires an explicit revised execution plan and authority, not a silent runtime default. No target-specific staffing or capacity claim follows from the number.

### Repair episodes

Allow **at most two automatic repair cycles per work-unit acceptance checkpoint**. A checkpoint covers the ticket/change being accepted, or the final integrated delivery for cross-ticket findings. It has a stable ID, finding set and budget in the evidence record. Work-unit and integration checkpoints may address different failures; moving or renaming the same finding must not reset its spent budget.

A cycle starts when the first corrective assignment or direct fix for that checkpoint begins, and includes inspection of the result, affected checks, and renewed review where needed. A failed/partial worker attempt still spends that cycle. Pure diagnosis before a fix is not a cycle, but every delegated diagnosis is itself bounded. New related findings or regressions stay in the same episode. Resume preserves the count. Resolving all material findings with current evidence ends the episode; recurrence of the same unresolved cause does not earn another budget by changing tickets.

If material findings remain after cycle two, or substantive disagreement/unsafe authority appears earlier, stop affected execution and return diagnosis, preserved state, and a recommendation to reassess design, scope or environment. Further repair requires an explicitly approved revised plan and recorded budget, not another vote. Known missing permission or an unavailable material check blocks immediately rather than consuming two performative attempts.

This bounds unproductive iteration without pretending the initial implementation is correct. Two cycles permit one correction and one follow-up; #29/#30 trial evidence may justify a later approved change.

## Revision-aware evidence

Use a compact Markdown record, not a service, database, or required machine schema. Reuse the target's task/PR artifact location and retention/disclosure rules. A small direct change can keep its record in the conversation and final PR report; a run spanning sessions needs an approved durable artifact/pointer before leaving unfinished work. Do not create a new committed state directory by default or put private logs into public issues.

Minimum fields:

| Field | Required content |
| --- | --- |
| Agreement | Target and task/spec/brief reference, source revision or inspected body digest, acceptance IDs, approved scope/exclusions, decision/authority pointers |
| Delivered state | Branch/worktree identifier where applicable, resolved base and HEAD commit IDs, scoped changed-path inventory, working-tree fingerprint, protected/excluded work and inclusion rationale |
| Checks | Criterion/risk, command or inspection performed, environment/baseline, exact state checked, result and evidence location; distinguish executed, static, not-run, failed and stale |
| Review | Reviewer identity/independence, Standards and Spec reports, snapshot reference, findings and disposition; no-review or incomplete review remains explicit |
| Progress / recovery | Native graph observation, assignment ownership and revision, integrated/not-integrated status, active workers and bounds, repair checkpoint/cycle counts, uncertain operations |
| Outcome | Implemented, verified, unverified, deferred and blocked scope; documentation/changelog/impact disposition, limitations, pending decisions and next action |

Use only applicable fields; mark an inapplicable branch rather than fabricating evidence. Preserve sufficient history to explain changed results and repair budgets. A raw tool log is supporting evidence, not the completion report.

The delivered-state format is owned by `review-delivery`'s scope contract, consumed by the lead evidence record. For Git it must identify the resolved comparison base and HEAD, scope manifest, staged and unstaged change fingerprints, and content/mode or symlink-target fingerprints for included untracked files. Account for deletions/renames and relevant supporting inputs. A HEAD SHA alone cannot identify dirty work. For non-Git work, use a before/after file manifest with content/mode fingerprints. Fingerprint only the authorized scope; record relevant excluded/unavailable evidence and block review if it is material. Do not retain secret file contents as review artifacts.

Reviewers receive the actual diff/files and relevant context, not merely hashes or the lead's conclusions. Use an immutable authorized snapshot or freeze scoped writes and compare fingerprints before/after review. A changed scope invalidates the affected results; it is not silently incorporated into a report for the old revision. After repair, rerun affected checks and renew significant-change review. A content-identical commit may retain prior content evidence only after recording the equivalence; checks sensitive to commit/branch/integration state must still rerun.

## Ready gates and delivery ownership

- **Build:** actionable approved behavior and acceptance, known material design/ownership/dependencies, sufficient authority and safe preflight. Raw intent alone is not ready.
- **Accept:** integrated state has material acceptance/risk evidence and independent Standards/Spec review; findings are resolved or the proper decision-maker has explicitly changed the acceptance agreement. Refreshed evidence covers repairs. Passing a suite, worker consensus or issue closure alone is insufficient.
- **Report:** claims match the evidence, documentation impact is addressed, limitations and consequential decisions are explicit. Ready-for-PR, accepted/merged, and deployed/released are distinct states under target-project policy.

The phase changing a fact owns updating its existing authoritative document. Setup's [documentation contract](../../setup-project/references/documentation-contract.md) describes the input model; runtime uses the target project's actual ownership policy rather than imposing this repository's layout. Product changes need appropriate spec approval; domain changes use the companion; implementation/review maintain the actual changelog or fragments and versioning/label policy. A justified no-change decision is valid. Publishing or classifying release impact does not authorize release.

### Tracker classification across phases

Consume the target project's approved title and label mappings. Distinguish specification and bounded work-ticket roles, assess readiness independently, and retain native parentage/blockers as the work graph. This repository uses mutually exclusive `spec` and generic `implementation-step` roles under its [label guidance](../agents/triage-labels.md). Other projects retain their explicitly mapped equivalents and title conventions; a small request need not acquire a hierarchy.

Specification (#20) applies and reads back the mapped spec role and evaluates readiness separately from publication. Ticketing (#22) applies the mapped implementation-step role to bounded work under a spec, including design and validation; it does not copy the parent's spec/readiness/release labels or classify subordinate specs and delivery PRs as steps. Completion (#26) reassesses affected readiness after accepted decisions and merges within current mutation authority, with read-back. Dispatch (#27) treats a ready spec as a coordination entry point, schedules only eligible work tickets, and uses native blockers plus evidence rather than title parsing. Review checks project-policy compliance without becoming the label administrator. Integrated validation (#31) checks these distinctions, equivalent mappings and preservation of unrelated labels/relationships.

## Downstream application

The destination table allocates all #19–#31 work without changing native blockers. In particular, #19 establishes the common envelope before its consumers; #24 can proceed independently after #18 because it owns the review scope/return contract; #26 connects verification and review; #27 uses those gates for dispatch. #21 can consume an existing brief independently of the new discovery route in #20.

Before dispatching a ticket, inspect accepted predecessor artifacts and the live graph, not this summary alone. Any material contract adjustment discovered during implementation is a proposed delta with affected tickets and evidence invalidation explained. Keep unchanged confirmations; do not repeat product discovery or rewrite the whole design on each ticket.
