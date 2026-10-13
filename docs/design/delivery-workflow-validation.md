# Delivery contract design validation

Design-level verification for [#18](https://github.com/SirDarcanos/agentskills/issues/18). Read with the [contract](delivery-workflow.md) when accepting it or checking downstream coverage. The walkthroughs below are authored paper exercises inspected directly by the design author. They are **not executed agent workflows, independent review, or trial results**. #29 and #30 remain responsible for actual integrated trials.

## Spec coverage

| #14 criterion | Design coverage | Implementation / validation owner |
| --- | --- | --- |
| AC1 — Context and authority | Context/capability contract, approved-operation envelope, distinct invocation and delegation authority, protected work | #19, #23, #28; trial #29/#30 |
| AC2 — Entry routes | Raw request, existing agreement and resume routes; lightweight brief; actual-state reconciliation | #19, #20, #28 |
| AC3 — Product agreement | Discovery/specification handoffs, four concern dispositions, consequential approval and spec-label ownership | #20; trial #29 |
| AC4 — Technical readiness | Codebase/coverage inspection, responsibility/interface and complexity rationale, domain companion | #21 |
| AC5 — Work graph | Native procedure reuse, exact graph approval/read-back, evidence-aware frontier | #22, #27; trial #30 |
| AC6 — Execution | Direct default, two-worker ceiling, exclusive write ownership, serial lead integration, target branch policy | #23, #27 |
| AC7 — Verification | Per-criterion/risk evidence tied to delivered state; baseline and not-run distinctions; invalidation after changes | #25; both trials |
| AC8 — Independent review | Independent reusable package, Standards/Spec outputs, full dirty-work snapshot and unchanged-scope check | #24; both trials |
| AC9 — Repair and recovery | Two-cycle checkpoint budget with preserved lineage, explicit reassessment, uncertain-state reconciliation | #26, #28; trial #30 |
| AC10 — Completion | Build/accept/report gates, phase-owned document changes, actual changelog/versioning policy and no implied release | #26, #31 |
| AC11 — Portability and validation | Package-local references, semantic discovery, explicit conditional companions, provenance, isolated package checks and actual trials | All changed packages; #29–#31 |

This matrix assigns responsibility, not completion. The native issue graph is unchanged. #19 and #24 remain blocked by #18 until its accepted design and merge evidence permit them to start.

## Paper walkthrough A: one direct fix

**Synthetic starting facts:** an existing Git project documents branch/PR rules and permits a scoped implementation plus independent review. Its request is a small input-validation fix with an agreed invalid-input response. Existing checks exercise the public interface. A separate untracked note belongs to the user. Required companions are compatible; no setup or account change is requested.

| Step | Expected contract decision / evidence |
| --- | --- |
| Entry | Read existing policy and inspect dirty state. Record the unrelated note as protected/excluded; choose a lightweight brief rather than creating a spec issue and tickets. No full setup run. |
| Readiness | Name expected behavior and failure risk, inspect existing coverage, reuse the current interface. The lead chooses a regression check; it asks the user only if the invalid-input behavior is unresolved. No glossary/ADR output is needed merely for reading terms. |
| Build | Preflight chooses the correct short-lived branch. The lead builds directly, using test-first development if useful rather than invoking the incompatible installed TDD instructions. Record the local result and dirty delivered state. |
| Verify | Execute the relevant checks against the integrated state and record criterion, command, result, baseline and snapshot. A passing unrelated suite does not establish the input behavior. |
| Review | Freeze scoped writes; independent Standards and Spec review inspects the actual modified and relevant untracked files. The user's excluded note is not sent as review context. Reviewers receive evidence and sources, not an instruction to approve. |
| Repair | A material finding starts repair cycle 1. The corrected file changes the snapshot; affected checks and significant-change review repeat. A content-identical later commit preserves content evidence only after an explicit equivalence check. |
| Report | Report the delivered behavior, executed verification and refreshed review, documentation/changelog disposition, limitations and PR readiness. The issue is not closed ahead of the project's acceptance/merge policy. |

**Variants inspected on paper:** without independent-review permission or capability, building may finish but acceptance remains blocked; missing material check tooling produces the same honest evidence gap without installation. If existing user policy mandates a check or TDD, this workflow follows it or requests an approved change rather than silently overriding it.

**Design result:** the handoffs support a complete lightweight route without an issue hierarchy, worker pool or hidden legacy-command invocation. This is a consistency conclusion, not behavioral proof.

## Paper walkthrough B: multi-ticket failure and resume

**Synthetic starting facts:** an accepted spec has tickets A and B independent, and C natively blocked by A. The project permits up to two delegated workers and provides safe isolation. A and B have disjoint write ownership and stable interfaces. Native graph reads and independent review are available; issue closing requires accepted integration. These letters describe a fixture, not extra GitHub issues created by #18.

| Step | Expected contract decision / evidence |
| --- | --- |
| Graph inspection | Compare native parents/blockers and completion evidence with the approved plan. Confirm A and B ready; C waits. If edges exist only in prose, stop affected dispatch rather than inventing native success. |
| Assignment | Launch A and B with bounded authority, separate ownership and finite runtime bounds. Both slots are occupied; no additional exploration/reviewer starts until capacity is available. |
| Failure | A's worker fails after partial changes. Record uncertain operations and branch/artifact pointers. Preserve them and confirm the worker has stopped or is isolated before replacing its ownership. C remains blocked even if A's issue was accidentally closed. |
| Independent progress | Inspect and integrate B serially under target branch policy. A's preserved scope is not reset or discarded. If B changes an interface A depends on, replan/rebase only with the necessary authority; do not hide the dependency behind disjoint filenames. |
| Repair | Diagnosis identifies a fix for A's material failed check. Start cycle 1 for A's checkpoint; rerun affected evidence. If it fails, cycle 2 is the final automatic attempt. A new related regression or worker failure still consumes the same episode's budget. |
| Budget exhaustion | After two unsuccessful cycles, report A/C blocked, B's actual integrated/verified state, preserved work, failed evidence and a concrete reassessment recommendation. No cleanup, repeated voting or silent acceptance reduction. |
| Resume | Read actual workers, revisions, graph, findings and stored counts. Resubmission does not reset A's budget. Further repair needs an explicitly approved revised plan/budget. C starts only after A has the integration/completion evidence the project requires. |
| Final integration | Record the new integrated state, refresh affected checks and independent review. A cross-ticket finding can have an integration checkpoint, but moving A's unresolved finding there cannot give it two new attempts. |

**Variants inspected on paper:** if A and B own a shared interface, serialize or combine their work; if a remote write times out, inspect before retry; if graph read-back or required tool access becomes unavailable, preserve safe progress and report the affected blocker. A requested tracker graph cannot be silently replaced with a local checklist.

**Design result:** capacity, ownership, integration and repair evidence have distinct roles; partial success does not become whole-spec completion. Actual scheduling/recovery behavior remains unverified until #30.

## #18 acceptance and documentation impact

| #18 requirement | Deliverable |
| --- | --- |
| Installed entry-point inventory | [Inventory](delivery-workflow-inventory.md), observed behavior versus intended disposition, content fingerprints |
| Package/invocation and compatibility choices | [Contract](delivery-workflow.md), package map, unchanged legacy commands, semantic companion requirements |
| Specialist handoffs and caller checks | Contract's shared envelope, responsibility table and inspection obligations |
| Concrete limits and evidence | Concurrency/repair definitions, counting and resume rules, revision-aware record and review scope |
| Provenance/license review | Exact upstream license reference, installed-source uncertainty, no-import approach and future notice requirements in inventory |
| Decisions, approvals and downstream impacts | Contract status, [proposed ADR](../adr/0001-delivery-workflow-ownership.md), destination map and acceptance gate |

Documentation changes are limited to this design set, its ADR, an agent-entry read pointer and the tracker document's description of #14/#18. Product commitments and native issue relationships stay in GitHub. `CONTEXT.md` needs no change because no domain meaning changed. README/install listings and changelog remain unchanged because #18 ships no runtime behavior or installable package. No release-impact label is warranted for this design-only PR.

## Reproducible document checks

From the repository root, inspect the changed Markdown and run `git diff --check`. Resolve each relative Markdown link from its containing file, including anchor targets, and inspect the rendered tables/headings. Check that proposed package paths are formatted as planned destinations, not broken links or claims of existing packages. Check the integrated diff for private data, local installation paths, copied third-party source, generated artifacts and accidental runtime changes.

Verify the inspected installed entry points were left unchanged by comparing their hashes with the inventory; installed copies are inputs, not deliverables. Record the actual commands/results and reviewed Git revision in the PR, alongside this paper-exercise limitation. There is no new executable workflow or skill package to test in #18, and no universal repository suite is implied.
