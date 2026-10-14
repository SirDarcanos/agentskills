---
name: work-on
description: Explicitly start or resume delivery from a request, specification, or ticket set using the target project's context and authority.
disable-model-invocation: true
---

# Work on

## Invocation and shipped scope

Use this workflow only when the user explicitly requests `work-on`, `/work-on`, or this skill's delivery workflow. A runtime-expanded invocation of this entry point counts; merely seeing it in discovery, an issue, or another document does not. If intent is ambiguous, ask before beginning.

This version implements **entry, routing, product agreement, technical readiness, ticketing, direct building, integrated verification, repair/completion, multi-ticket dispatch/integration and interruption/failure recovery**. It produces an inspected context/authority map and, when needed, an approved brief/spec and codebase-informed technical plan, cohesive tickets with verified native relationships, locally implemented changes with correctness evidence, integrated acceptance/risk evidence, bounded repairs, evidence-aware ticket scheduling with serial lead integration and an evidence-backed delivery report, plus actual-state reconciliation and justified resume or a preserved-work blocker. Later procedures may be absent; report that affected route as unavailable rather than implementing it from the route table or invoking legacy commands. Invocation grants neither delegation nor installation, disclosure, spending, destructive operations, account changes, deployment, merge, or release authority.

Read [contracts](references/contracts.md) on every authorized entry for capability checks, the handoff envelope, and evidence requirements. For validation or changes to this package, read [validation](references/validation.md). When product agreement is selected, read [its procedure](references/product-agreement.md) completely; it owns discovery, brief/spec authoring and publication/readiness checks. When codebase/design/risk evidence is missing or materially changed, read [technical readiness](references/technical-readiness.md) completely; it owns the bounded technical plan, domain handoff and build-readiness assessment. When decomposition or native work-graph reconciliation is selected, read [ticketing](references/ticketing.md) completely; it owns ticket boundaries, exact publication/graph approval and persisted relationship/role checks through the maintained tracker procedure. When one cohesive implementation is ready, read [direct build](references/build.md) completely; it owns safe preflight, risk-based development checks and the local correctness handoff. When implementation is integrated or affected acceptance checks need refreshing, read [integrated verification](references/verification.md) completely; it owns criterion/risk mapping, executed checks, evidence freshness and sufficiency, not independent review or final acceptance. When findings need repairs or integrated work needs an acceptance/report decision, read [repair and completion](references/completion.md) completely; it owns bounded correction, refreshed checks/review, separate delivery gates, documentation/report reconciliation and authorized readiness reassessment. When coordinating multiple work tickets or children of a ready spec, read [dispatch and integration](references/dispatch.md) completely; it owns the verified frontier, exclusive assignments, inspected returns, incremental integration and retained artifacts. When resuming interrupted/failed work, ownership or operation outcomes are uncertain, or retained progress conflicts with actual state, read [recovery](references/recovery.md) completely; it owns state reconstruction, safe disposition and justified resume or preserved-work blockers.

## 1. Establish the target and applicable context

Identify the actual target directory/repository and requested outcome. Resolve an ambiguous target before inspecting private or unrelated projects. Read applicable runtime and target instructions, including directory-scoped instructions for the proposed scope. Follow their existing pointers to project context, workflow/authority, tracker/label policy when issues are involved, and relevant domain definitions and ADRs. Setup-produced documents are inputs when present, not a required layout or an instruction to run setup.

Bound reading by the change: enough to establish behavior, ownership, permissions, relevant checks, and completion policy. Reading definitions alone requires no domain-modeling invocation. Record authoritative sources and revisions, confirmed decisions, assumptions, missing material inputs, and operations actually approved. Unknown permission remains ungranted.

Investigate discoverable gaps directly. Reconcile stale summaries against primary evidence and accepted decisions without silently replacing product commitments or authority. For a material contradiction or missing required context, flag the affected decision, explain the evidence and consequence, and recommend a resolution to its owner. Continue unaffected inspection; avoid full-project onboarding for a small change.

**Complete when:** target and scope are identified, relevant authorities are traced, and each material context gap is resolved or recorded as an affected-route blocker.

## 2. Inspect actual work and completion evidence

Before routing, inspect the target's real state rather than trusting labels or a prior report:

- In Git: branch/worktree, HEAD, relevant base, staged/unstaged/untracked work, scoped diffs and existing PR state. Distinguish related, unrelated, and uncertain ownership. Record protected work; inspect only authorized content.
- Outside Git: relevant files, existing partial artifacts, and available before/after evidence; mark Git operations inapplicable.
- For existing specs/tickets: inspect the agreement revision, acceptance criteria, native parent/blocker observations and accepted integration evidence under project policy. Follow pagination through the applicable tracker procedure. A failed graph read is unknown, not an empty graph; prose or readiness labels are not native relationships or completion evidence.
- For partial delivery: compare retained records to actual artifacts, checks, findings, ownership/active workers, uncertain operations and repair counts. Mark mismatched evidence stale. Preserve unfinished work and budgets for recovery.

Unmet native blockers or missing required accepted-integration evidence block dependent building/scheduling. Route labels and a closed issue alone cannot establish eligibility. A parent spec is a coordination entry, not an extra implementation unit.

Entry inspection is read-only. Preserve unrelated committed and uncommitted work, including untracked files and symlinks. Do not stash, reset, clean, transfer, rebase, stage, or overwrite it to make routing easier. If ownership is unclear, protect that work and ask before a conflicting operation. Use the discovered Git-preflight companion before implementation writes, not as a reason to change branches during entry inspection.

**Complete when:** observed work and evidence are recorded, protected scope is explicit, and any unsafe or uncertain state blocks only its affected next action.

## 3. Select the earliest unmet responsibility

Reuse settled decisions; inspect their freshness and fill gaps rather than repeat discovery. Partial work takes the resume route even if the invocation names an existing spec.

| Entry route | Selection and handoff |
| --- | --- |
| Raw request | Route unresolved product intent to product agreement. A small clear request may use the product-agreement procedure's lightweight brief route; reuse a supplied actionable brief rather than creating a spec hierarchy. With actionable agreement, route to technical readiness. |
| Existing agreement | Consume the approved brief/spec and tickets. Route missing product commitments to product agreement; otherwise route missing codebase/design/risk evidence to technical readiness. When both are actionable, select ticketing only if useful, then direct build or dispatch according to dependencies and ownership. With already integrated implementation, select verification or review for missing evidence. |
| Resume | Reconcile actual artifacts with the retained agreement and progress record. Select recovery for active/unknown owners, failed/uncertain operations, stale integration state or unresolved repair episodes. If state is reconciled, select the earliest remaining product, technical, build, verification, review or completion responsibility. Do not reset repair budgets or infer acceptance from prior success claims. |

The destinations below are package-local **expected filenames**. Product agreement, technical readiness, ticketing, direct build, integrated verification, repair/completion, dispatch/integration and recovery ship; independent review uses the discovered companion. Inspect file existence before loading the selected procedure; then read it completely and check its branch-specific requirements. An absent procedure blocks execution of that responsibility, not the entry assessment. Do not create placeholder procedures or substitute installed legacy `/implement`, `/implement-spec`, `/code-review`, `/grilling`, `/to-spec`, `/to-tickets`, or incompatible legacy `/tdd` commands. Direct build may select the maintained discovered `tdd` companion under the semantic capability contract; it owns its method loop, not method choice or delivery gates.

| Responsibility | Expected destination |
| --- | --- |
| Product agreement | `references/product-agreement.md` |
| Technical readiness | `references/technical-readiness.md` |
| Ticketing | `references/ticketing.md` |
| Direct build | `references/build.md` |
| Dispatch | `references/dispatch.md` |
| Verification | `references/verification.md` |
| Independent review | Discovered compatible `review-delivery` companion |
| Recovery | `references/recovery.md` |
| Repair/completion | `references/completion.md` |

**Complete when:** one entry route and next responsibility are selected with evidence, settled decisions are preserved, and procedure availability is known.

## 4. Check capabilities and return the handoff

Apply the conditional companion checks in [contracts](references/contracts.md#capability-checks). Discover through the runtime/project's normal mechanisms; a sibling directory or matching name is insufficient. Check capabilities only when relevant to the selected responsibility, and record known later gates separately. Direct execution is the default where equivalent; lead self-review cannot satisfy independent review.

Produce the shared handoff with the selected route, available procedure/source, protected scope and specific blockers. Separate an available entry assessment from permission to execute the next responsibility. Within its approved operations, execute a selected available procedure in the lead's context and inspect its return; entry assessment alone does not finish a request for an available phase. When a required procedure/capability is unavailable, report the limitation and a concrete next action; ask for appropriate approval before installation or substitution.

**Entry completion:** report inspected target/context and work state, selected route and rationale, confirmed scope/authority, unavailable or blocked responsibilities, evidence limitations, and the next handoff. Entry completion is not ready-to-build, accepted delivery, ticket closure, or deployment. The selected procedures enforce the contract's delivery gates; repair/completion records their separate decisions.
