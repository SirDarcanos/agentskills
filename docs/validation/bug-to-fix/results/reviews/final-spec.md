# Spec review — #71 / `bug-to-fix-71`

## Identity and independence

Fresh read-only Spec reviewer: `reviewer`, execution `a91d19d4-c015-4204-99be-08d8959dfffd`. I did not author or modify the reviewed implementation/evidence, consult another reviewer, delegate, execute scripts, contact services, or perform assessments.

I did not read prior axis reports, retrospective README commentary, or `.pi` history. The diff inventory exposed report filenames only, not their conclusions. Protected target file/link contents were not inspected.

Authority: this assignment and repository standing independent-review permission. Bound: five minutes. The root owns the freeze, worker ledger and final freshness comparison.

## Agreement and snapshot

- Repository agreement: `docs/validation/bug-to-fix/agreement.md`, particularly Scope, Verification, Boundaries, and Delivery/documentation.
- Repository input revision: `c532dc698c68fca7c5496e116ce66ea4af6e325c`, as recorded in `results/sources.json`.
- Synthetic target base and HEAD: `5fbaa7f0ea2c5f8a5be8f80655848cf2cbf5447a`.
- Included target sources: `pricing.py`, `caller.py`, `test_existing.py`, `test_discount.py`, `reproduction.py`, `AGREEMENT.md`.
- Inspected the actual frozen target sources, original `../scope.json` and `../commands.json`, exported scope, separate staged/unstaged patches, status, and direct-change sources.
- Original and exported pins show the same listed identities/fingerprints, with the exported root replaced by `<workspace>/target`. I did not independently recompute hashes or inspect Git metadata: no command-execution tool was available.

The repository changes visible to `watchdog_diff` are untracked #71 artifacts. This tool does not establish a committed-range comparison against the requested repository base.

## Inspected coverage

Read the three harness sources, agreement, both PR-impact reports, all eleven raw check logs, commands, ticket/tracker, state, investigation stop, branches, direct manifest, scope, freshness and source records.

Direct assertion inspection included:

- `docs/validation/investigate-bug/test_investigation.py` and its supporting `check.py`;
- `docs/validation/write-tickets/tracker_fixture.py`;
- all five method `scripts/check-fixture.py` files;
- all four assessment authorization/procedure test suites, three replay test suites, Jev’s procedure fixture, and initial request cases for the three local packages.

Standards inspected included project/workflow/tracker/label guidance, accepted composable design and validation mapping, review entry/handoff/scope/report, PR entry/impact, and the Work On execution contract. Full assessment runtime implementations and every fixture-data row were not audited.

## Synthetic acceptance — separate from repository #71

| Requirement | Actual source/assertion and raw evidence | Assessment |
|---|---|---|
| **R1:** subtotal 100 at `.10` returns 90 | Actual `pricing.py:1–3` multiplies subtotal by `1-discount`; `test_discount.py:4` asserts 90. Original commands record reproduction `(99.9, 90)`, meaningful regression red, green/refactor success, and final `90.0`. | Covered locally. |
| **R2:** zero discount preserves subtotal; empty carts return zero, including `.10` | `test_existing.py:4–5`, `test_discount.py:5`; raw red identifies `-0.1 != 0`, while both original controls pass. All four checks pass after green/refactor. | Covered locally. |
| Signature and caller units preserved | Actual `pricing.py:1`, `caller.py:2`; both implementation patches preserve the signature. | Covered by source inspection. |
| **D1:** display 90 as `Total: 90.00` | `results/direct/display.py:1–2`, `check.py:2`; commands show assertion failure then success, with unchanged check digest in `direct.json`. | Covered separately; not pricing acceptance or currency-rounding evidence. |
| Exclusions | Synthetic `AGREEMENT.md:6–7` excludes rounding/domain expansion and real payment integration. | No excluded production claim inferred. |

## Repository #71 obligation mapping

| Obligation / referenced acceptance | Evidence and boundary |
|---|---|
| Confirmed investigation stops at a complete ticket; no investigation-only fix (**AC7**) | `run_fixture.py`, `investigate()` retains expected/actual, impact, environment, reproduction, cause, deciding digests, scope/exclusions, risks, acceptance and method. It performs JSON read-back and verifies unchanged production code/protected state. `investigation-stop.json` records the buggy digest and no shipped fix. The denied-delivery regression checks no regression-file creation or added commands. |
| Authorized delivery reuses current evidence without repeated analysis (**AC3/AC4**) | `deliver()` checks authorization, ticket-ready state and exact deciding inputs before characterization/TDD. Inspection shows no investigation/analysis invocation in delivery. `test_same_ticket_composition_preserves_protected_layers` verifies unchanged ticket bytes; raw handoff log passes. State counters corroborate but are not treated as independent enforcement proof. |
| Clear direct change (**AC2/AC3**) | D1’s actual formatting source, unchanged check, before/after manifest and failure/pass commands establish the direct build-and-check example. |
| Useful composition and all five examples (**AC6**) | Characterization protects intended controls, detects an isolated `+1` perturbation, then TDD repairs R1/R2. Separately rerun method examples demonstrate shipping red/green/refactor and rejected oracles; bounded cancellation prototype/disposition; characterization intent/defect/unknown separation; acceptance-first API→SQLite and side-effect sensitivity; immediate code/document/config checks and stopped dependent progression. These are executed authored fixtures, not five autonomous skill invocations. |
| Stale deciding code (**AC4/AC7**) | `branches()` changes pricing, verifies delivery stops before adding checks, then observes `100.9` without repair. `branches.json` preserves old inputs and unchanged agreement. Investigation regression separately covers changed caller applicability. |
| Unresolved/unconfirmed/intermittent diagnosis (**AC7**) | Investigation tests publish `investigation-only` records with cause/access/input gaps and next actions; original product remains unchanged. Seven raw named cases pass. These paths deliberately withhold facts; they do not demonstrate real-world intermittent diagnosis. |
| Duplicate reconciliation (**AC7/AC13**) | Harness and investigation assertions match cause/input identities, preserve canonical identity/labels, avoid another issue and retain graph state. `tracker.json` has one canonical issue; its reconciled body explicitly describes retained pre-fix evidence, not a current delivered-code failure. |
| Enabled/denied policy paths using mocks (**AC10/AC11**) | Local authorization tests assert exact allowed payload and one send; denied/missing/wrong identity/disclosure/budget paths assert zero effects. Pre-send revocation, shared exhaustion/resume, advisory mismatch, insufficient data and lifecycle ownership are exercised. Jev tests additionally cover spend reservations, unknown charges and bounded retry/correction. Transport and lifecycle effects are mocked. No actual policy parser, inference or autonomous compliance is established. |
| Independent dirty-work review and ownership (**AC13**) | Actual staged green plus unstaged refactor, included untracked regression/reproduction, and unchanged support sources were inspected. Scope accounts for protected dirty file/link separately. Preservation assertions and initial freshness support ownership. This fresh Spec report supplies one independent axis, not both axes or acceptance. |
| Commands, revisions, findings/unrun checks; evidence rather than expected outcomes (**AC15**) | Commands contain exit codes, outputs and input digests; check summary records commands/environment/inputs. Raw logs include intentional failures and limitations. Both reports distinguish fixture execution from autonomous enforcement and exclude hosted/live/installed effects. |
| Standalone/package and delivery/documentation commitments (**AC1 and agreement delivery clauses**) | Existing method fixture executions and assessment isolated-copy assertions support their bounded package examples. No skill entry/procedure change appears in the visible #71 delta; unchanged-package frontmatter/isolation is not proof of a new installed integration. Reports justify repository-only documentation, no public behavior/changelog change, and retain maintainer acceptance/merge as separate gates. Native prerequisite/merge eligibility was not independently verified remotely. |

## PR-impact claims

**Fixture report:** Source/assertions support two unchanged controls plus two added regressions, with zero removed/updated/moved tests. Reproduction is correctly separate. Staged/unstaged/untracked local delivery is explicitly not remote delivery. Reversal correctly warns that restoring old source restores the defect and cannot undo hypothetical external payment effects.

**Repository report:** The seven new harness methods match `test_handoffs.py` and its raw log. The reported 183 named cases reconcile as:

- retained TDD behavioral methods: 2;
- characterize: 5; acceptance-first: 5; build-and-check: 4;
- handoffs: 7; investigation: 7;
- assessment suites: 37 + 40 + 40 + 36.

Prototype observations are separate. TDD diagnostic anti-examples and repeatedly executed methods must not be counted as additional retained test identities. Totals are consistent; underlying assertions, not the total, establish the coverage described above.

Both reports appropriately mark hosted duration/compute/billing/speedup unavailable and separate source merge from deployment, release and installation. Repository workflow independently states no shared test command or GitHub Actions workflows. I could not independently inspect baseline Git trees, CI definitions/hooks, external settings or final publication state with the available tools. Thus absolute CI/automatic-effect absence is **not fully independently verified here**, rather than contradicted.

## Evidence limits and next action

- No tests were rerun by this reviewer. Results are retained root-executed evidence inspected against authored sources/assertions.
- No independent final fingerprint comparison was performed. Initial freshness is root-provided evidence; root must compare full scope/support and repeat discovery after both fresh axes return.
- No conclusion about prior reviews is made.
- Excluded live inference, hosted CI measurements, production/payment checks, actual installed migration and remote publication are not material missing local fixture evidence.
- This review does not certify arbitrary agent adherence, complete #48 delivery, #72/#73 trials, prerequisite integration, maintainer acceptance or merge.
- Before consuming this report for acceptance, the root should retain the separate fresh Standards result and final freshness evidence. Any material drift requires affected review renewal.

## Review

- **Correct:** Synthetic R1/R2 and separate D1 are supported by actual sources, meaningful failures and subsequent passes. The #71 local trial obligations have inspectable assertion/raw-evidence mappings, with appropriate fixture/live/acceptance distinctions.
- **Fixed:** None; read-only review.
- **Findings:** No issues found.
- **Merge verdict:** **OK with notes** for the inspected Spec scope. This is not acceptance or merge authorization; final freshness and the separate Standards axis remain caller-owned gates.