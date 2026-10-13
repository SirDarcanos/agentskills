# Integrated tracker classification walkthroughs

#31 direct **static** walkthroughs against the integrated product, ticketing,
dispatch, completion and review paths. These authored scenarios were inspected;
no agent executed them, no synthetic decision engine was tested and no live labels
or edges were written. The [coverage record](README.md) owns executed evidence/gaps.

Authority: target title/label policy → Work On entry/shared contract →
[product agreement](../../../work-on/references/product-agreement.md) publication →
[ticketing](../../../work-on/references/ticketing.md) role/graph reconciliation →
[dispatch](../../../work-on/references/dispatch.md) eligibility →
[completion](../../../work-on/references/completion.md) readiness/read-back →
[Review Delivery](../../../review-delivery/references/report.md) independent challenge.
The target policy owns mappings; review checks them without becoming administrator.

| Starting scenario | Integrated path and static disposition |
| --- | --- |
| Draft parent spec titled “Improve import behavior”; behavior decisions unresolved | Product step 4 publishes only within exact approval, applies/read-backs mapped `spec` and separately assesses readiness. Draft publication alone adds no ready claim. Dispatch consumes actionable scope and evidence, not a title prefix. |
| Accepted parent with resolved design; children include “Define format contract” and “Validate import recovery” | Product readiness is reassessed after decision; ticketing step 4 gives design and validation units `implementation-step`, not `spec`, while native parent links identify membership. Assess each child's criteria/decisions independently; do not copy the parent's labels. Ready parent coordinates, never becomes an additional build assignment. |
| Subordinate specification already has its own native parent and children | Ticketing preserves its `spec` purpose and existing parentage. It is not a bounded step merely because it is subordinate. Dispatch routes/co-ordinates its eligible actual work children; any ownership/graph change needs exact approval, not relabeling to fit a flat plan. |
| Delivery PR “fix(import): preserve recovery state” references accepted steps | Project commit/PR title convention applies; ticketing does not put the step role on a PR. Review checks delivered behavior/release impact against actual target policy. Closing references do not prove acceptance or change native issue relationships. |
| Approved alternate roles `type:agreement`, `type:work`, `actionable`; target titles require `[Data]` prefix | Product/ticketing use the explicit equivalent mappings and target title rule. Role names remain exclusive; unrelated `priority:high` remains. Dispatch reads metadata/native graph, not `[Data]` parsing. This repository's sentence-case/no-role-prefix rule is not exported. |
| Parent decision accepted, but child C awaits native blocker A and its criteria are already actionable | Completion step 4 reassesses parent and child separately. C may remain ready-for-agent while dispatch keeps it waiting. Accepted parent or closed A is insufficient without required accepted integration evidence. No automatic label sweep/edge removal. |
| A's PR accepted and merged; C's current agreement and checks unchanged; unrelated labels/edges exist | Completion step 4 inspects decision/merge evidence and proposes only an authorized exact readiness delta. Read back assignments and both native directions through the maintained procedure if graph changes are approved. Dispatch recomputes the frontier; C is eligible only if all blockers/ownership/capability conditions pass. Preserve unrelated assignments, parentage and blocker edges. |
| Read-back fails or label write times out after an approved readiness delta | Completion records uncertainty, inspects before retry and blocks the affected claim. Recovery retains state/budget. An unapproved mutation becomes a proposal only; no blind retry, substituted prose edge or assertion of a successful reconciliation. |
| Prior review snippets appear in an otherwise neutral packet or broad search | Review report's packet checklist separates source/raw checks from conclusions, records exposure as ineligible and requires lifecycle-safe replacement within two slots. This static check covers the clarification; only #30's historical trial actually observed exposure and clean replacement. |

## Live read-only observation

Before edits, `gh api --paginate repos/SirDarcanos/agentskills/issues/14/sub_issues`
returned #18–#31 with plain descriptive titles: #18–#30 closed, #31 open, all mapped
`implementation-step` and no `spec`. #14 has `enhancement`, `spec`, `ready-for-agent`.
#31's native parent read returned #14; blocked-by returned #29/#30, closed/completed;
reverse blocking reads from both returned #31. Accepted merged PRs #45/#46 and their
actual retained outputs were inspected, rather than accepting closed state as proof.
#31's existing readiness remains actionable with integrated predecessors; #14's
ready label remains a coordination status, not delivery completion. No label delta
was needed or authorized in this documentation task.

Commands also inspected #14/#31 titles/labels and merged PR revision pointers through
read-only `gh issue view` / `gh pr list`. There were no mutation requests: existing
assignments and native graph were left unchanged. Final read-only comparison is
recorded in the coverage report. This establishes observed repository state, not
live execution of alternate mappings, subordinate-spec creation or readiness writes.
