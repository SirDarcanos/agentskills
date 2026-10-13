# Ticketing

Read completely when a technically actionable brief/spec needs cohesive work tickets or reconciliation of an existing work graph. Use the inspected [technical plan](technical-readiness.md) and [shared handoff](contracts.md#handoff-envelope). This is an internal procedure of an explicitly requested Work On run, not a separate command. For changes or validation, read [ticketing validation](ticketing-validation.md).

## 1. Establish the agreement and tracker capability

Pin the approved brief/spec and technical-plan revisions, acceptance IDs, exclusions, settled decisions, authority and protected work. Missing material product/design decisions return to their owning phase; ticketing does not settle them by creating tasks. For a small cohesive change, recommend direct build instead of manufacturing a hierarchy. Reuse suitable existing tickets rather than decomposing again.

Read the target's tracker, title, label, readiness and completion policies. Resolve its actual host/repository/project identity and available native parent and blocker capabilities through authorized read-only access. Discover the maintained tracker procedure through [capability checks](contracts.md#capability-checks), recording its source/revision and compatibility.

For GitHub, discover `setup-project`, read its complete entry point for the library-use boundary, then its `references/issue-tracker.md`, especially **Native GitHub graph**. Read the optional helper and its documented limits before choosing it. This reads a procedure library; it does not invoke `/setup-project`, authorize setup mutations or require a sibling installation. That procedure owns the graph algorithm/API recipes; use it throughout inspection, application and verification instead of copying it here. Other trackers need an inspected project-approved native procedure. Missing/incompatible required capability blocks remote graph work; ask for agreement on an explicit alternative, never silently substitute body links. Planning may continue without claiming persistence.

**Complete when:** agreement and technical readiness are pinned, decomposition is justified, target mappings and a compatible native procedure are known, or the affected capability gap has an owner and next action.

## 2. Inspect and propose cohesive tickets

Use the maintained procedure to inspect current issues and both directions of parentage and blockers, including all pages, database IDs, repository identities, transitive blockers and parent ancestry. Failed/incomplete reads are unknown, not absent edges. Include existing edges reachable beyond the proposed ticket set; unrelated ownership and blockers remain protected. Record the observed graph and observation time before proposing a delta.

Choose session-sized deliverables by behavior and ownership, not module count or a fixed ticket quota. Keep tightly coupled state/interface changes with one owner when splitting would reduce coherence. Separate design or validation when it is genuinely a bounded deliverable. Name true prerequisites rather than imposing a linear sequence for convenience; distinguish a scheduling blocker from shared ownership that should serialize or stay together. Dependencies do not grant delegation or dispatch authority.

Each proposed ticket contains:

| Item | Required content |
| --- | --- |
| Identity | Stable draft key or existing actual tracker identity, descriptive title under target convention, owning spec/revision |
| Behavior | One bounded intended outcome, rationale and referenced spec acceptance IDs; checkable ticket acceptance criteria |
| Scope | Owned behavior/files/interfaces where known, protected work and explicit exclusions; one cohesive session boundary |
| Verification | Appropriate existing/needed checks, environment and meaningful expected results; planned checks remain distinct from executed evidence |
| Dependencies | True blockers and why they precede this work; separately identify native owning parent and any coordination/ownership constraints |
| Classification | Mapped work-ticket role and independently justified other labels/readiness; no copied parent label set |

Apply the target's approved work-ticket role (for example, `implementation-step`, or its approved equivalent) to bounded work under a spec, including design and validation. A parent spec or subordinate spec retains the spec role; a delivery PR is not a work ticket. If an existing item has a conflicting workflow role, propose the exact authorized role correction rather than adding both. Assess ordinary type/readiness labels independently. An actionable blocked child may be ready under target policy while retaining its native blockers; readiness never proves eligibility or integration. Missing mappings/labels require a scoped decision, not an unrelated label/settings audit or automatic vocabulary creation.

**Complete when:** every proposed ticket has behavior, acceptance traceability, verification, exclusions and justified prerequisites; cohesive ownership is preserved; the native observation is complete enough to assess the proposed graph.

## 3. Obtain exact publication and graph approval

Present one concrete plan: target identity, ticket drafts/reused IDs, exact title/body and label deltas, parent → child membership, and **dependent is blocked by prerequisite** edges with reasons. Distinguish already-present edges, missing additions and protected unrelated edges/parentage. Use the maintained procedure's combined existing-plus-planned conflict checks before asking approval. Self-links, cycles, reversed intended blockers, conflicting parents and unknown graph reads prevent application; propose a corrected plan rather than removing or reparenting unrelated work.

Approval must cover the exact ticket creation/update, role assignments and graph effects. Broad delivery permission, a readiness label or prose mentions are insufficient relationship authority. For new tickets, stable approved draft keys can identify the exact graph before database IDs exist. Create only the approved drafts, resolve the returned actual identities/IDs, then bind those keys to the IDs without changing the approved graph. If resolution is ambiguous, the observed graph changed materially, or the intended ownership/dependency changed, stop for reconciliation and renewed approval of the changed delta.

**Complete when:** an exact publication/graph delta is approved with protected state and draft-to-ID binding rules, or ticketing returns a plan-only handoff with the missing decision.

## 4. Apply and read back the approved delta

Reinspect affected state against the approval immediately before writes. Publish/update only approved tickets and mapped role/other-label deltas, preserving unrelated content and assignments. Resolve actual repository identities and database IDs for new tickets; record draft-key bindings and per-operation outcomes. Read back titles, scoped body changes and label assignments; confirm each bounded work ticket has the approved role and no conflicting spec role.

Apply graph additions through the maintained native procedure. Use its helper only for compatible additive blockers in one github.com repository, with the exact approved plan and fresh inspection. Parentage and unsupported graph scopes remain with the procedure, not the helper. Keep server conflict protection enabled. Existing intended edges are no-ops; preserve unrelated edges and parentage. Removals or reparenting are separate specifically approved changes outside this additive route.

After writes, compare the persisted graph to the approved intended graph by actual identities/IDs, reading both directions and all pages via that procedure. Confirm intended parent membership, blocker direction, preserved unrelated state and conflict-free combined graphs. Verify labels separately; prose summaries can now reflect the observed native graph, but are never persistence evidence.

On timeout, interrupted creation, failed write or read-back, stop affected operations and retain successful, failed and unknown outcomes. Inspect actual issues/assignments/relationships before any retry; search for a possibly created ticket using approved content and identity evidence rather than creating duplicates. Ambiguous matches require clarification. Resume only missing approved operations after fresh inspection and authority checks; do not automatically roll back, delete, or replay the batch. A missing permission/capability or incomplete read-back blocks graph-dependent scheduling and requires a concrete next action or approved alternative.

**Complete when:** publication, mapped roles and both native relationship directions match the intended IDs with preserved unrelated state, or the return explicitly identifies partial/unknown outcomes and affected blockers. A clean rerun adds nothing.

## 5. Return the verified graph or affected blocker

Return the shared envelope with ticket identities/draft bindings and revisions, acceptance references, observed/intended/persisted graph, approval pointer, procedure/helper source, actual operations and read-back evidence. Distinguish planned/static/executed checks, uncertainties and unavailable capabilities. Include role/readiness decisions, preserved labels/edges/parentage and documentation updates or justified no-change. Update target-owned tracker summaries only within authority; keep native relationships authoritative.

The lead inspects actual ticket contents, classifications and graph evidence against the approved plan rather than accepting a summary. A verified graph supports a later dispatch handoff; it does not prove blocker completion, authorize worker launch or implement dispatch. Check the selected next procedure's availability through entry; report absent dispatch/build unavailable instead of invoking legacy commands.

**Ticketing completion:** cohesive tickets with approved, read-back native parentage/blockers and mapped roles, or an explicit plan-only/partial/blocked result with preserved state and next action. This is not implementation, accepted delivery, issue closure, merge or release.
