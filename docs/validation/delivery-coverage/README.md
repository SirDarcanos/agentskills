# Delivery installation and acceptance coverage

Evidence for [#31](https://github.com/SirDarcanos/agentskills/issues/31), reconciling
[spec #14](https://github.com/SirDarcanos/agentskills/issues/14) after accepted trial
PRs [#45](https://github.com/SirDarcanos/agentskills/pull/45) and
[#46](https://github.com/SirDarcanos/agentskills/pull/46). This is repository evidence,
not an installed procedure or a declaration that the parent spec is complete.

## Agreement and delivered state

- Inspected #14 body SHA-256: `2452a4c1f3dc9609c2a4bf66878d4dfeea86beaa0dbbe7ab49563962fcdf05a7`
  (`gh issue view 14 --json body --jq .body`, including its output newline).
  Scope: #31's installation, package validation, coverage and integrated classification checks.
- Accepted [design](../../design/delivery-workflow.md) through PR #32 at
  `ec7de9c2725209388fd1f4ca11719f68c1e7cef1`; read its inventory and design validation.
  They remain historical design observations/paper scenarios, not trial execution.
- Preflight: clean `main`; fetched base `6fb45ef6541563eb79578f9c0fd7875250ed6f5f`
  (merged #46). Created `docs/delivery-installation-coverage` from `origin/main`;
  PR target `main`, no existing PR/unrelated work. The containing PR commit identifies
  the documentation/checker changes; historical trials retain their own revisions.
- Changed scope: repository and two package READMEs, Unreleased changelog,
  Review Delivery report/validation reference, two package MIT notices, this evidence
  directory. One direct author; no workers, delegated assessment or repair episode.
  No remote label/relationship mutation, global installation, release or merge.

## Packages, discovery and compatibility

Isolated validation covers `work-on`, `review-delivery`, and their maintained
conditional companions `implementation-preflight`, `domain-modeling`, `setup-project`.
Their complete entry points and applicable references were inspected. Review is a
separate package; product, technical, ticketing, build, verification, completion,
dispatch and recovery procedures remain inside Work On. Validation references are
reachable from entry/validation pointers; runtime phase pointers state when to load
procedures completely. Relative file links stay inside each copied package.

[Work On's contract](../../../workflow/work-on/references/contracts.md#capability-checks)
owns semantic compatibility and affected-route blockers. Package READMEs now explain
installation, collision checks, source/revision discovery, copied-install updates and
actual requirements. They do not imply installed slash expansion was tested.
`setup-project` is discovered for its tracker library, not invoked; its setup-only
GitHub companion is not a delivery dependency. TDD and optional model assessments
remain separately requested methods, not hidden requirements. No legacy fallback,
SDK adapter, sibling path or hosted service was introduced.

The [provenance inventory](../../design/delivery-workflow-inventory.md#license-decision)
records newly authored procedures, not an imported external implementation. Direct
integrated inspection found no newly vendored third-party bodies/notices. Existing
notices are unchanged; each new independently distributed delivery package now
includes the complete root MIT notice (copyright 2026 Nicola Mustone; maintainer name corrected after the original checks). Conditional
companions were inspected, not repackaged or relicensed by this change.

## #14 criterion-by-criterion evidence

Kinds below distinguish **static/direct inspection**, **offline executable checks**,
**historical agent trials**, **historical independent review**, and **live read-only
checks**. The historical records' acceptance-pending wording describes their original
pre-merge state; accepted merged PRs supersede it, not the recorded evidence limits.

| Criterion | Shipped implementation | Executed evidence and remaining limit |
| --- | --- | --- |
| AC1 — Context/authority | [Entry](../../../workflow/work-on/SKILL.md) steps 1–2; [contracts](../../../workflow/work-on/references/contracts.md); recovery | #29 reads target policy and preserves non-Git note/link; #30 preserves staged/unstaged/untracked/link work. Static inspection confirms invocation/operation authority separation. No private target or sensitive-disclosure trial. |
| AC2 — Entry routes | Entry step 3; product agreement; recovery | #29 clear request/lightweight agreement; #30 existing spec/tickets and actual checkpoint pause/resume. Unresolved raw-intent interviewing and process-restart resume remain unrun. |
| AC3 — Product agreement | [Product agreement](../../../workflow/work-on/references/product-agreement.md), #20/PR #35 | #29 reuses an agreed brief/concern dispositions. Direct static review of discovery, four dispositions, consequential approval and publication/read-back; no autonomous consequential discovery or live spec-publication trial. |
| AC4 — Technical readiness | [Technical readiness](../../../workflow/work-on/references/technical-readiness.md), #21/PR #36; discovered domain companion | #29 inspects caller/coverage; #30 defines normalization/report interface and shared README ownership. Static design/complexity/domain-handoff inspection. No live domain/ADR editing trial. |
| AC5 — Work graph | [Ticketing](../../../workflow/work-on/references/ticketing.md), #22/PR #37; discovered tracker library; dispatch | Offline helper tests cover identities, cycles, pagination transport, additive/read-back failure paths. #30 uses controlled native observations and rejects writes. Live #31 reads confirm actual parent/blockers. Work On live publication/mutation, cross-repository graph and real API-failure execution are not established. |
| AC6 — Execution | [Build](../../../workflow/work-on/references/build.md), #23/PR #38; [dispatch](../../../workflow/work-on/references/dispatch.md), #27/PR #43 | #29 one direct fix; #30 direct serial owner/integration and bounded separate reviewers. Offline #27 fixture serial merges/preservation. No concurrent implementers, real third-slot refusal or worker-timeout/kill trial. |
| AC7 — Verification | [Verification](../../../workflow/work-on/references/verification.md), #25/PR #41 | #29 baseline/red/fixed/integrated checks; #30 baseline/failure/repair/final checks, freshness and cross-ticket behavior. Offline #25 fixture distinguishes baseline/privacy regression and missing material evidence. These do not cover every consumer's security/persistence risks. |
| AC8 — Independent review | [Review Delivery](../../../workflow/review-delivery/SKILL.md), #24/PRs #39/#40 | Historical #24 reviewers detect dirty/untracked defects and stale scope; #29 independent axes cover the small delivered change; #30 failed, clean renewed and final axes cover integrated behavior. Packet exposure was retained as ineligible, not accepted evidence. Current #31 independent repository-diff review is recorded below, with its limits. |
| AC9 — Repair/recovery | [Completion](../../../workflow/work-on/references/completion.md), #26/PR #42; [recovery](../../../workflow/work-on/references/recovery.md), #28/PR #44 | #30 one actual failed prerequisite, cycle-1 correction, retained history, pause/resume and renewed review. Offline #26 two-cycle counterfactual and #28 actual conflict/dirty-work checks are separate fixture evidence. No real worker crash, remote uncertain write or autonomous exhausted-budget trial. |
| AC10 — Completion | Completion gates/readiness; phase-owned documentation; #31 READMEs/changelog/this matrix | #29/#30 reports separate implemented/verified/unverified/deferred/blocked with target snapshots. Direct integrated review checks no implied closure/release; [classification scenarios](tracker-scenarios.md) inspect reconciliation. #31 remains unaccepted until project gates and merge; parent completion is not inferred from ticket closure. |
| AC11 — Portability/validation | Package READMEs, conditional contract, local helpers/validation | Both integrated trials executed on Pi/macOS; isolated package links/frontmatter/syntax/helper checks executed here. No CLI installation, installed slash expansion, Windows, alternate-runtime certification or isolated autonomous workflow run. Python 3.9 syntax is checked; execution is Python 3.14.7, not 3.9. |

Primary historical evidence: [#24 review](../review-delivery/README.md),
[#25 verification](../work-on-verification/README.md),
[#26 completion](../work-on-completion/README.md),
[#27 dispatch](../work-on-dispatch/README.md), [#28 recovery](../work-on-recovery/README.md),
[#29 small trial](../work-on-small-change/README.md),
[#30 multi-ticket/failure trial](../work-on-multi-ticket/README.md).
Read their raw sources/checks/reports and limitations, not issue status alone.

## Executed #31 checks

Environment: macOS, Python 3.14.7, Git 2.54.0 (Apple Git-157); no installation.

1. Before edits at the base above: `python3 -B review-delivery/scripts/test_snapshot.py`
   passed 11 tests; `python3 -B -m unittest discover -s setup-project/tests -v`
   passed 21 tests. Both historical `verify.py --replay` commands passed: #29 exits
   **0/1/0**, #30 **0/1/0/0**, with expected failure assertions, membership and pins.
   Replay is not a new agent trial or independent review.
2. Isolated package/link/frontmatter/Python 3.9 syntax and helper checks:
   `python3 -B docs/validation/delivery-coverage/check_packages.py`.
   Passed in source and one-package-only copies: Work On 111 links/anchors,
   Review Delivery 11, preflight 1, domain 9, setup 27; repository documentation 49.
   Isolated review helper: 11 passed. Isolated setup suite: 21 discovered, 19 passed,
   2 companion-presence checks correctly skipped; those companion packages were
   separately checked above. MIT copies match the root notice byte-for-byte.
   The script removes only its explicitly disposable copies; no runtime install.
3. Integrated direct instruction review traced all phase homes and completion gates:
   one shared handoff/authority contract, one review snapshot owner, project-specific
   graph/label authority, no expanded setup invocation. [Classification scenarios](tracker-scenarios.md)
   received direct static walkthroughs; they are not agent or live mutation results.
4. The #30 review-packet failure prompted a small checklist in the existing report
   contract and an authored validation case: neutral inputs, explicit search roots,
   retained ineligible exposure, lifecycle-safe replacement. No packet generator,
   sandbox, runtime adapter or new domain/ADR decision. A fresh behavioral trial of
   this checklist remains unrun; historical clean replacement evidence is not a
   test of the changed text.
5. Historical pins are intentionally not rewritten. Current README/report changes
   make original trial-support pins stale; use the recorded historical revision for
   replay. Both current `verify.py --replay` calls exited 1 with their expected stale
   support/runtime assertions; original pins and records are unchanged. That is
   evidence invalidation, not a regression in fixture behavior.
6. Reran the supplied repository-local checks with `python3 -B`:
   `docs/validation/work-on-verification/exercise.py`,
   `docs/validation/work-on-completion/exercise.py`,
   `docs/validation/work-on-dispatch/exercise.py`, and
   `docs/validation/work-on-recovery/exercise.py`: all exited 0. Inspected expected
   baseline/privacy failures, stale-scope results, cycle counts 1/2 with no third
   correction, closed-without-integration waiting, cross-ticket failure sensitivity,
   protected-state equality and retained merge conflict. These are scripted
   disposable fixtures/direct inspection, not new agent or independent-review runs.
7. Existing `marked` (resolved from the installed runtime dependency, without
   installation) rendered all Work On/Review Delivery Markdown and changed repository
   Markdown. Inspected HTML headings/tables/code blocks and changed package prose/
   packet checklist; no unresolved Markdown links. This is direct HTML inspection,
   not browser layout testing. Complete companion Markdown/frontmatter and conditional
   pointers received source inspection and isolated link/anchor checks.
8. Repeated live read-only #14 child/title/label, #14/#31 assignment, #31 parent/
   blocked-by and #29/#30 reverse-blocking reads: matched pre-edit observations.
   No remote mutation, unrelated assignment or edge change. `git diff --check`
   passed; direct full scoped-diff/new-file inspection found no credentials, private
   material, workstation paths, generated trial outputs, bytecode or legacy changes.
   Released changelog sections and historical trial trees remain byte-identical.

## Independent review follow-up

After user approval, fresh read-only Standards and Spec contexts inspected the fixed
base above through `2c085934b0c337c601f37d2fe41d4000b10165c3`, with 15-minute bounds.
The initial pair indirectly encountered a historical verdict in an expressly
permitted checker source. Both stopped, returned ineligible exposure records and
terminated before replacement. Historical narrative/checker sources were then
excluded from supporting inputs; current changed documents remained claims under
review. One bounded packet-correction episode; at most two active reviewers.

Clean replacements reported no issues within their inspected scopes and no excluded
conclusion exposure. They performed static source/diff inspection, not test/Git
execution. Historical verdict contents remain unverified by them; parent-executed
checks and receipts are separate evidence. Final parent path discovery/status,
161-path snapshot, agreement/diff hashes and supplemental root LICENSE matched
after both returns before releasing the freeze.

[Full separate reports, original ineligible records and publication hashes](https://github.com/SirDarcanos/agentskills/pull/47#issuecomment-6150514797)
are retained in PR #47. Only transient packet paths were normalized for publication;
this is ordinary observed review/lifecycle evidence, not execution attestation or
filesystem sandbox certification. This follow-up records outcomes after review;
it is a parent-inspected administrative update, not part of that pinned review.
No runtime source, package requirement or acceptance commitment changed afterward.

## Outstanding gates and documentation disposition

**Blocking acceptance:** the maintainer must assess the matrix's evidence sufficiency
and any material gaps, accept the work and approve its merge. Independent review
of the pinned delivery is complete within the stated limits; lead self-review did
not substitute for either axis. #31 and #14 stay open; package
checks and closed predecessors alone do not establish completion. No material
remaining target-fixture defect was reported by #29/#30; broader missing evidence
is not hidden by their scoped no-findings results.

**Unrun/unsupported:** installation CLI/global updates, installed command expansion,
a dedicated checklist behavior trial (distinct from its observed application during
this review), live graph/label writes and failure read-back,
concurrent implementers, real crash/timeout/kill, process restart, alternate OS/runtime
and Python 3.9 execution. Existing offline conflict/budget evidence remains distinct.
These need explicit bounded follow-up/permissions if material to the acceptance
agreement; no new issue, tracker edge or expanded runtime contract is silently added.

**Documentation:** updated repository discovery, both package install/requirements
sections, review packet/validation, license distribution and Unreleased entry.
Removed only the stale Unreleased claim that later delivery phases are unavailable;
released history is preserved. Domain meanings, ADR boundary, project authority,
tracker mappings, installed legacy skills and historical trial artifacts are unchanged,
so their authoritative homes need no edits. This is backward-compatible guidance
and review-safety clarification; patch impact is recommended, not a publication.
