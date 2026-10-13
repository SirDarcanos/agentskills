# Executed multi-ticket and failure trial

Repository-only evidence for [#30](https://github.com/SirDarcanos/agentskills/issues/30)
under [#14](https://github.com/SirDarcanos/agentskills/issues/14). Work On and
Review Delivery sources were tested at `77c4bb63cf944af770dff51b529eee15d65574fc`.
No shipped skill or installed copy changed.

**Outcome:** the direct Pi lead coordinated two synthetic tickets, kept the
dependent waiting through a failed prerequisite, repaired in cycle 1, renewed
checks/review, then integrated the dependent and refreshed final checks/review.
The final feature matches N1/R1; dirty-work preservation checks passed. Final
Standards/Spec reviewers found no issues within the agreed fixture scope.
Repository acceptance and merge remain the maintainer's decisions.

## Evidence index

| Record | Contents |
| --- | --- |
| [Entry and plan](plan.md) | Authority, native predecessor observations, fixture agreement, graph and ownership |
| [Actual actions](actions.md) | Lead's ordered decisions, checkpoint resume, review-boundary failure and recovery |
| [Fixture baseline](fixture/baseline/) / [failed](fixture/failed/) / [repaired](fixture/repaired/) / [final](fixture/final/) | Actual original and retained delivered source copies |
| [Baseline capture](evidence/baseline-check.json) / [failed](evidence/failed.json) / [repaired](evidence/repaired.json) / [final](evidence/final.json) | Base/HEAD, full scope and Git-layer/content/mode fingerprints, membership and protected state |
| [Raw commands](evidence/commands.jsonl) / [final patch](evidence/final.diff) | Actual local Git/check operations and integrated changes; all historical patches retained |
| [Mock graph observations](evidence/tracker-read.json) / [prerequisite event](evidence/prerequisite-event.json) | Controlled endpoint reads/write rejection and separate synthetic acceptance evidence |
| [Checkpoint progress](progress.json) / [final progress](progress-final.json) | Stable finding/budget and integration pointers without reviewer conclusions |
| [Failed Standards](reports/failed-standards.md) / [Spec](reports/failed-spec.md) | Original blocking findings for the injected lower-only behavior |
| [Superseded Standards](reports/repaired-standards.md) / [ineligible Spec](reports/repaired-spec.md) | Retained review-packet failure; not consumed for acceptance |
| [Clean renewed Standards](reports/repaired-clean-standards.md) / [Spec](reports/repaired-clean-spec.md) | Independent prerequisite evidence after correction |
| [Final Standards](reports/final-standards.md) / [Spec](reports/final-spec.md) | Independent complete integrated scope review |
| [Runtime receipts](review-receipts.json) / [sanitization](evidence/sanitization.json) | Observed terminal/fresh-context fields, report hashes and publication transformations; not attestation |
| [Capture helper](trial.py) / [offline verification](verify.py) / [integrity pin](integrity.json) | Evidence utilities; no scheduler, agent launcher or automatic acceptance engine |

## Observed behavior and #30 coverage

| Requirement | Executed observation |
| --- | --- |
| Actionable synthetic project and controlled tracker | Explicit N1/R1/P1/G1/E1, Python/Git target, two work tickets under parent 100, IDs distinct from numbers, complete mocked forward/reverse/parent observations. Adapter rejected POST/PATCH/DELETE before any network write. |
| Failed/blocked route and recovery | Actual prerequisite check exited 1. Lead kept 102 unstarted despite closed/ready 101, retained the failed commit/source/evidence, resumed the checkpoint, spent cycle 1/2, corrected trimming and obtained current checks/reviews. |
| Readiness, ownership and integration order | Lead direct serial owner; shared README serialized. Two read-only reviewers at most, replacements after terminal completion. Source integration: candidate `93e4d2d…` → correction `aaacb949…` → dependent `42b09950…`. Only scoped commits consumed owned paths. Parent was never an implementation assignment. |
| Preserved unfinished/unrelated work and resume | Failed implementation remains in reachable local history and retained snapshots. Staged/unstaged sentinel index/bytes/mode, untracked note and leaf symlink fingerprints stayed equal at every capture and final live check. Same lead resumed after a real review pause without duplicating integration or resetting the episode. |
| Refresh after repair and final claims | Failed evidence remains failed for old HEAD. Correction reran affected tests and renewed both axes. Dependent integration reran cross-ticket tests and final independent axes at `42b0995033daf25dc1f00bafc00ad52ab233034d`; post-pair full target freshness passed. |
| Findings, rework and maintenance | Known injected N1-trim defect resolved by one line. Meaningful independent-review boundary failure disclosed and blocked consumption; original reports preserved, two contexts replaced. No workflow source repair or substantial new infrastructure. |

The injected defect was known to the lead and described in the trial agreement.
Initial reviewers identified it from actual code and failed checks, but this is
not a blinded reviewer-sensitivity experiment. Their severity labels differed;
the lead used the source-grounded material requirement, not a vote.

The first repaired Spec reviewer accidentally saw prior report snippets in a
broad search. It requested a supervisor decision and stopped; the parent marked
it ineligible. The parent also noticed that its own supplied action narrative
contained retrospective reviewer commentary and conservatively superseded the
Standards result. A fresh pair with explicit source/evidence allowlists and neutral
progress metadata excluded those inputs. That avoidable packet/search rework is
part of the observed trial, not omitted from a success narrative. The eventual
clean and final pairs report no conclusion exposure. Boundaries are procedural,
not a filesystem sandbox certification.

Maintenance: fixture behavior adds only two small functions and standard-library
checks. The repository record retains source/check/review history plus narrow
capture/replay tools; it adds no production service, configuration or dependency.
Capture-authoring fixes normalized local path labels and closed a temporary file
descriptor; their direct checks are distinct from target repair. One user exchange
was necessary for delegation permission; the supervisor exchange and review
replacement were handled by the lead without another user decision. Product
choices, tickets, installation and manual runtime coordination were not added.

**Bounded follow-up proposal:** use #31's validation/documentation reconciliation
to assess an outcome-free review-packet checklist with explicit search boundaries
and a case for prior-report exposure. If implementing isolated packet tooling or
changing runtime contracts is substantial, request a separate session-sized
follow-up with acceptance for independent inputs, retained blocked reports and
capacity-safe replacement. No new issue, tracker edge or runtime rule was created
by this trial. Concurrent implementer/real failed-worker trials would require a
separately authorized bounded scope; they are not claimed here.

## Delivery and documentation disposition

- **Implemented:** synthetic normalization and composed reporting; final owned
  target changes are names.py/test_names.py/report.py/test_report.py/README.md.
  Retained source, patches, manifests, failure/review history and lifecycle metadata.
- **Verified:** N1/R1 by executed assertions and direct source inspection; P1 at
  captured/live checkpoints; G1/E1 by executed lead decisions, mocked observations,
  stable budget, actual Git/check evidence, refreshed independent reviews and
  final freshness. These sources have different evidential strength.
- **Unverified:** live native mutations/API failures/pagination beyond one mock
  page, concurrent implementers or third-slot refusal, worker crash/timeout/kill,
  session-process restart, merge-conflict handling, cycle-two exhaustion, Windows,
  alternate runtimes, installed slash expansion, isolated package execution and
  absence of transient edits between observations. Prior #28 checks remain separate.
- **Deferred:** broader installation/acceptance coverage belongs to #31; proposed
  packet-hardening assessment is not silently added to this ticket's requirements.
- **Blocked:** no material remaining fixture behavior/evidence blocker within this
  bounded direct trial; repository maintainer acceptance and authorized merge remain
  pending. #30 stays open until accepted and merged. No production merge/release.

Build, fixture acceptance-readiness and truthful-report gates pass within the
stated limits. Fixture policy intentionally permits direct integration and
fixture-lead acceptance; it does not change this repository's PR-only policy.
Graph results and prerequisite acceptance are synthetic, not GitHub mutations.
The repository's #30/#28 predecessor inspection was real read-only GitHub access.

Documentation affected: fixture README and this retained repository trial record.
No skill behavior, package boundary, domain meaning, ADR, operating policy or
tracker mapping changed; their authoritative homes need no update. No changelog
entry or release-impact label: repository-only evidence changes no public skill
behavior or installation contract. #31 can link the two executed trial records.
Later capture/publication helper corrections and completion prose received lead
inspection/offline checks, not an additional independent repository-diff review.

## Offline reproduction and limits

From the repository root:

```sh
python3 -B docs/validation/work-on-multi-ticket/verify.py
python3 -B docs/validation/work-on-multi-ticket/verify.py --replay
```

The first verifies retained artifact membership/hashes, pinned runtime sources,
source/patch manifests, protected-state consistency, mock adapter rejection,
checkpoint/event continuity and lifecycle/report metadata. The second additionally
runs baseline/failed/repaired/final checks in disposable directories, requiring
exits **0, 1, 0, 0** and the actual trimming assertion failure. Neither invocation
launches an agent, reruns the historical scheduling decisions, recaptures the live
dirty Git target, performs independent review or contacts GitHub. Assertion checks
must run without Python's optimization flag.

Observed environment: macOS, Python 3.14.7, Git 2.54.0 (Apple Git-157), native Pi
read/edit/bash tools and fresh native reviewer contexts. Standard-library tools;
no installation. Mode/link metadata is filesystem-specific. Git identities and
commit dates are synthetic. Current runtime-source drift makes the historical
pin stale; inspect this evidence's commit rather than rewriting old fingerprints.

The temporary target was retained, not deleted. Its private session pointer is
not published. Public snapshots/patches/metadata allow offline inspection, not
restoration of the exact Git object database or cryptographic proof of execution.
Logs preserve original outcomes; local path labels were normalized as recorded
in sanitization.json. Receipts identify ordinary observed lifecycle/context fields;
they do not establish OAuth/auth routes or attestation. Model agreement is not
independent proof of correctness.

Final repository checks: `verify.py --replay` passed the four expected exits and
all retained artifact/source/receipt comparisons; Python 3.9 syntax parsing passed
for both helpers. All 29 relative Markdown links resolved, retained JSON parsed,
and no bytecode or workstation-path strings remained. Existing `marked` rendered
the overview, plan, actions and final reports; headings/table structure and prose
were inspected directly. Scoped runtime sources are unchanged from the tested
revision. The staged diff is confined to this evidence directory. Default
`git diff --check` flags three retained patch blank-context markers and five
original Spec-report Markdown hard breaks; these were inspected as intentional
artifact bytes and preserved. All other staged paths pass the whitespace check.
