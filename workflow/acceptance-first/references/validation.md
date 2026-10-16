# Acceptance First validation

Read when changing or validating this package. Expected workflow cases below are authored scenarios, not executed agent evidence.

## Package and executable checks

1. Read the complete entry and rendered Markdown. Check `name: acceptance-first`, matching-request/handoff triggers, ordinary model invocation and checkable completion/blocking conditions.
2. Resolve every relative link from its containing file. Copy the complete package into an isolated directory without sibling skills, verify internal links and run the fixture there.
3. From the package directory, with Python 3.9+ and no third-party dependencies, run:

   ```sh
   python3 scripts/check-fixture.py
   ```

   The script writes only owned temporary synthetic files, runs at most twelve child Python processes with five-second timeouts, and removes its own temporary directory. No network, model, Git/tracker mutation, installed-copy change or user-project cleanup occurs.
4. Inspect five unittest results and raw observations. The workflow test observes AC1 receipt mismatch before changes, checks a persistence increment, observes AC2 rejection failure, then verifies accepted persistence and zero/negative rejection without persistence. Two mutation cases prove sensitivity to lost persistence and forbidden rejection side effects, restore the implementation and rerun green. Expected failures are caught assertions on behavior; process/import failures fail the fixture rather than count as meaningful red.
5. Inspect the synthetic AC3/AC4 reporting cases: undecided duplicate behavior is blocked without edits; missing real remote payment evidence stays unverified. These deterministic reporting oracles do not execute a real gateway or prove agent escalation. All cases verify agreement, storage implementation, harness and unrelated bytes remain unchanged.
6. Review the integrated diff for credentials/private data, generated files, local paths, protected work and notices. Retain actual commands/environment/source identity outside the copied package, separately from these expected cases.

## Authored workflow cases

Inspect direct and bounded entry with the same compatible existing agreement (no filename/template or Setup-origin requirement). Check missing/conflicting common guidance yields a specific prerequisite without setup or writes; conditional gaps affect only their capability. Exercise an unavailable material check and a recorded correction with prior spent lineage, including an old universal-contract-only companion. Record actual reads/actions/outcomes separately from these expectations. Ordinary same-session work returns evidence in conversation, without a new lead ledger or durable report.

Run package checks from an isolated copy using only its shipped files. Keep maintenance validation separate from ordinary method execution; no source checkout or historical comparison is required.

| Case | Expected outcome |
| --- | --- |
| Standalone agreed workflow | Map commitments, establish meaningful examples, implement/check small increments and return local criterion evidence; no automatic PR or acceptance. |
| Work On handoff | Consume current agreement/preflight/readiness inline; return artifacts and raw results for caller verification/review without duplicating its gates. |
| Ambiguous product commitment | Recommend clarification, pause affected example/implementation and preserve approved expectations; safe unaffected work may continue. |
| Material integration unavailable | Report criterion unverified/blocked, mocked boundary limits and next environment action; no stub pass or automatic installation/startup. |
| Wrong-reason red | Harness/import/auth failure is a gap, not a meaningful failing acceptance example. |
| Behavior already satisfied | Reuse current passing evidence; use authorized isolated sensitivity only if needed, not invented production breakage. |
| Acceptance disagrees with implementation | Diagnose code/harness/intent; changed product expectations require owner approval and authoritative record update, never silent weakening. |
| Stale input or subsequent edit | Invalidate/rerun dependent evidence; retain unaffected facts and old evidence's original state. |
| Missing/ambiguous helper outside sibling layout | Block dependent Git/domain/delegation/correction route, not ordinary safe direct development. |
| Plan-only authority | Return examples/check plan without file writes, runs beyond authority or installation. |
| Recorded finding/resume | Inspect only documented conditional coordination/repair libraries; preserve root ownership/bounds and existing checkpoint/lineage/spent cycles. An old universal-contract-only package blocks that route without resetting state; ordinary development remains independent. |
| Temporary data or competing edits | Exact authorized owned unchanged cleanup only; preserve unrelated and uncertain artifacts. |

## Limits

Static checks and synthetic fixtures do not prove agent adherence, standalone/composed workflow routing, actual installed discovery, live services, reviewer independence or cross-runtime compatibility. Separate authorized trials cover those claims. Passing examples are not exhaustive risk coverage. Return unrun material checks honestly.
