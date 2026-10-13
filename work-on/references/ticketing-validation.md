# Ticketing validation

Read when changing ticket decomposition, native graph reconciliation or work-ticket classification. Follow [entry validation](validation.md) for Markdown/frontmatter, diff and isolated-package link checks. Read [ticketing](ticketing.md) and the discovered maintained tracker procedure completely. This phase is instructions, not an executable ticketing engine; static walkthroughs do not establish agent compliance. Integrated executed trials remain with #29/#30.

## Executable coverage to reuse

Locate `setup-project` through discovery, then run its documented offline unittest command and helper `--help` from that source. In this repository:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s setup-project/tests -p 'test_*.py'
python3 setup-project/scripts/dependencies.py --help
git diff --check
```

Its existing tests execute the actual blocker reconciler with synthetic GitHub observations and a mocked CLI transport: successful graph/IDs/direction, no-op rerun, self/transitive/combined cycles, pagination, failed reads/permissions, partial write followed by fresh inspection, missing forward/reverse read-back and unsupported identities. Reuse these cases; extend only for a distinct uncovered executable failure. #22 adds database-ID mismatch coverage in both directions after a write and on an existing edge before any write or planned-success claim. They do not exercise parentage, label assignment, ticket creation, approval or agent behavior. The helper is optional; its absence alone does not block an otherwise compatible procedure.

## Synthetic walkthroughs

Use the facts below to inspect each procedure gate directly. For executed agent validation, supply an authorized synthetic target and tracker shim that rejects unapproved writes; record agreement/revision, runtime/invocation, observed requests with actual fixture IDs, approval evidence, final graph/labels and protected-state fingerprints. An authored or directly inspected trace is **static evidence**, not an executed agent trace or production API validation.

Fixture identities: `example/project` on github.com, issue numbers 1–6 with database IDs 9001–9006 (never use issue numbers as database IDs). #1 is the parent spec; #2 design, #3 implementation and #4 validation are bounded work; #5 is a subordinate spec and #6 a delivery PR. Parent links #1 → #2/#3/#4/#5 are observed natively, #3 is blocked by #2, and #4 by #3. All have unrelated `area-a` labels to preserve. Native relationships do not classify #5 as a step merely because it has a parent.

| Case / observation | Expected gate and evidence |
| --- | --- |
| Cohesive boundary | Technical plan has tightly coupled state/interface changes and a separately useful validation deliverable. Step 2 keeps coupled work under one owner; each draft has intended behavior, acceptance IDs, verification, exclusions and true blockers, not a module-per-ticket split. |
| Successful parent + blocker | Approved draft keys resolve to #3/#4, IDs 9003/9004. Step 4 writes only missing approved native edges and checks #1's paginated children plus each child's parent, each dependent's blocked-by plus prerequisite's blocking. Persisted IDs, mapped roles and preserved edges must match the plan. |
| Clean rerun | Same tickets, graph and labels already exist. Fresh inspection yields no publication, relationship or label delta; no duplicate tickets or cosmetic regeneration. Existing helper rerun coverage applies to blockers. |
| Cycle / reversed edge | Adding #2 blocked by #4 closes a transitive cycle; a proposal saying #2 depends on #3 reverses the intended prerequisite. Step 3 stops before writes through the maintained conflict checks and explicit direction/reason comparison. Also inspect combined planned parent cycles and prospective parent ancestry; hierarchy and blockers stay separate. |
| Foreign parent | #4 already belongs to `other/project` #1 with a different database ID. Preserve that parent; proposal to attach it to fixture #1 is blocked, not `replace_parent=true`. Identity must include repository, not equal issue numbers. |
| Pagination | Intended #4 appears only on page 2 of #1's children or #3's blocking list. All pages must be read before absence/delta/read-back claims; helper transport tests separately execute paginated blocker parsing. |
| Failed read / ambiguous absence | Parent endpoint returns ambiguous 404 or a later children page fails. Graph is unknown; no write or scheduling claim. Establish absence only via supported API/metadata semantics, not the failure. |
| Partial write / interrupted creation | Creation of #4 times out, or parent succeeds and blocker write times out. Retain confirmed/unknown operations; inspect matching ticket identity and both graph directions before retry. Ambiguous duplicate matches block. Retry only missing approved operations; no rollback, duplicate creation or blind replay. Helper tests exercise interrupted blocker writes only. |
| Missing permission / native capability | Required parent or blocker write/read-back is unavailable. Report affected partial/blocked state and seek an explicit approved alternative; prose remains supplementary, never a silently verified graph. |
| Drift after approval | Fresh observations introduce conflicting parentage or changed ticket ownership. Stop changed operations for reconciliation/renewed approval; binding known draft keys to actual IDs alone changes no approved graph. |
| Role distinctions | Only #2/#3/#4 receive `implementation-step`; #1/#5 retain `spec`, #6 receives neither work-ticket role. Read back all approved assignments. Bounded design/validation count as work, subordinate specs/PRs do not. |
| Ready but blocked / unrelated labels | #3 is actionable under target policy. Independently justified approved `ready-for-agent` may coexist with its #2 blocker; preserve blocker and `area-a`, never copy #1's spec/readiness/release set or infer predecessor integration. |
| Approved equivalents | Repeat classification with mapped spec=`proposal`, step=`work-item` and a project-approved title prefix. Use those mappings and titles, preserving unrelated labels; do not create repository-specific names or rename history. |
| Conflicting role / unapproved mutations | #3 has the spec role, or step mapping is absent. Propose an exact role correction or mapping decision; no mutually exclusive role pile-up, label/settings audit, or unapproved edge. Plan-only produces no writes. |
| Unavailable next phase | Graph verified, dispatch/build absent. Return graph evidence and unavailable next handoff, not worker launch or a legacy command. |

## Acceptance and documentation impact

#22 / #14 AC5: ticketing step 2 owns cohesive scope/acceptance/verification and mapped roles; steps 1–3 use the maintained native procedure for complete observations/conflict checking and exact approval; step 4 applies additive deltas and reads back actual IDs/roles; steps 4–5 preserve interrupted/unknown outcomes and block unsupported persistence. Discovery and the explicit setup library contract keep one authoritative graph algorithm.

Runtime changes belong to the ticketing reference and entry pointer; package/repository overviews, accepted-design runtime pointer and changelog describe the newly shipped phase. Setup documents expose library use without invoking setup. Domain meanings, ADR/package boundary, target policies, native production graph, legacy commands and installed copies are unchanged. Report actual test/static results, revision and limitations in the PR. Live mutations, independent review and agent walkthroughs need their own authority and are not implied by this reference.
