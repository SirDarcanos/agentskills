# Repair/completion validation

Use when changing or validating [repair/completion](completion.md). Follow [entry validation](validation.md#reproducible-static-checks) for Markdown/frontmatter inspection, relative links/anchors, isolated package copying and diff hygiene. Walk the cases against actual instructions and record step references; these expected outcomes are **authored cases, not executed agent evidence**.

| Case | Starting facts | Expected behavior |
| --- | --- | --- |
| Successful repair | Material public-interface finding, cycle 0, approved fix | Steps 1–2 assign the behavior owner, start cycle 1, inspect actual integrated change, invalidate old evidence, rerun relevant checks and renew significant-change review before acceptance. |
| Changed revision | Green check/review for old scope; a supporting input or new path changes | Steps 1–3 retain old results as stale, repin complete scope and refresh affected checks/review; HEAD alone or a matching old file list is insufficient. |
| Unresolved material finding | Unrelated checks pass; disclosure criterion still fails | Steps 1 and 3 block acceptance. Step 5 can report partial/blocked work honestly; ready-to-report is distinct from ready-to-accept. |
| Exhausted bound | Two partial/failed repairs of the same cause; attempt is renamed or moved | Step 2 preserves lineage/count, stops corrective execution and recommends reassessment. An explicit revised plan/budget is needed, not a new vote or silently reduced commitment. |
| Earlier stop | Material tool/permission absent or substantive disagreement arises before two cycles | Steps 1–2 stop affected work immediately; no performative retry. Routine diagnosis may continue safely within authority. |
| Changed agreement | Owner approves a consequential acceptance delta | Steps 1 and 3 record authoritative change/consequences, remap remaining evidence and renew affected review; approval does not manufacture a check pass. |
| Missing independent review | Author-only checks pass; delegation ungranted or one axis incomplete | Steps 1 and 3 leave acceptance blocked, report direct inspection honestly and recommend the required capability/permission. |
| Documentation and release | Fix changes a domain rule and public behavior; target uses fragments and non-SemVer impact roles | Step 3 routes meaning changes to the companion, updates actual owners/fragments/mappings, and requests only required approvals; no imposed repository layout or automatic release. |
| Accepted decision / merge | Parent decision becomes actionable, or predecessor has accepted integrated completion | Step 4 reassesses affected parent/children and dependents separately. Ready parent coordinates children; child readiness and execution eligibility remain distinct. |
| Closed without integration | Required predecessor issue closed; accepted integration evidence absent | Step 4 keeps dependent execution blocked even if its criteria are actionable and its label remains ready. |
| Missing tracker authority | Evidence supports an exact readiness-label delta but no approved mutation | Step 4 returns proposed delta, leaves assignments/edges unchanged and requests no blanket permission expansion. |
| Read-back failure / rerun | Authorized additive label update partially succeeds or times out | Step 4 inspects actual state, records uncertain/failed reconciliation and preserves unrelated assignments/edges. A clean rerun is a no-op; no blind retry. |

## Bounded execution protocol

Use a disposable Git fixture with a public-name/privacy projection and existing assertions. Observe the material failure, start a stable repair checkpoint, make the approved correction and inspect its actual diff. Use the discovered Review Delivery snapshot format/helper to identify dirty state, detect stale evidence after change and repin/rerun. Record independent review as absent unless separately authorized and actually executed. Exercise two unsuccessful corrective attempts and preserved counts without launching a third.

For tracker cases, inspect synthetic native observations with distinct parent and dependency graphs, accepted decision/merge evidence and scoped label authority. An in-memory authorized label write/read-back may demonstrate fixture preservation; clearly distinguish it from a live API test and from native graph capability. Retain before/after labels and edges, exact proposed/applied delta and read-back result. Do not create production issues or mutate live labels to test this procedure.

Retain reproduction source, commands/results, actual state pointers, inspected gate/disposition decisions and limitations **outside this installable package** at the approved evidence location. A script tests fixture assertions, not whether an agent follows prose. The lead's direct walkthrough, static inspection, independent review and autonomous end-to-end trials must remain separate.
