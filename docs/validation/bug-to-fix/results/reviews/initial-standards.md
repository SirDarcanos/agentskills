# Standards review — #71 / bug-to-fix-71

## Identity and independence

Reviewer: fresh read-only Standards subagent, artifact identity `3a9386d5-80b8-4092-94dd-df25e2efa52c`. I did not author or modify the reviewed files, consult other reviewers’ conclusions, delegate, access remotes, install tools, or invoke models. Authority: the assignment and `docs/agents/workflow.md#independent-review-permission`. Runtime bound: five minutes.

This is an original Standards report, not acceptance or merge authorization.

## Scope and evidence

**A — dirty pricing fixture**

Inspected all six included files: `AGREEMENT.md`, `pricing.py`, `caller.py`, `test_existing.py`, `test_discount.py`, and `reproduction.py`; plus supplied `../scope.json`, `../commands.json`, `../ticket.json`, and `../investigation-stop.json`.

The supplied pin identifies branch `fix/fractional-discount`, base=HEAD=`5fbaa7f0ea2c5f8a5be8f80655848cf2cbf5447a`, separate staged/unstaged fingerprints, and included untracked content. Agreement digest: `6d4e81a4293a7dacf55a45e6f37ae01812a7ba325c30655c7c1398945189ede4`.

**B — repository #71 evidence**

Inspected the complete `run_fixture.py`, `run_checks.py`, `test_handoffs.py`, and primary `agreement.md`; exported target/direct sources, staged/unstaged patches, status, commands, ticket, investigation-stop, state, branches, direct manifest, check summary, and every raw check output under `results/checks/`.

Scoped working-tree inspection confirmed the three scripts and agreement are untracked. Comparison against absence at main `c532dc6` is supplied task context, not independently verified Git history.

**Binding standards inspected:** `AGENTS.md`, project/workflow instructions, accepted composable-delivery design and validation mapping, Review Delivery entry/handoff/scope/report, and Work On’s execution contract.

## Review

### A — fixture R1/R2

- **Correct:** `pricing.py:1–3` preserves the interface and applies the fractional discount to subtotal. `caller.py:2` retains `.10` units. This satisfies `AGREEMENT.md:2–3,5` without introducing excluded rounding, input-validation, or payment semantics.
- **Correct:** `test_existing.py:4–5` retains zero-discount/empty controls; `test_discount.py:4–5` checks the fractional calculation and empty fractional cart. `reproduction.py:2–4` independently expresses R1’s oracle.
- **Correct:** supplied command records show the meaningful failures `99.9 != 90` and `-0.1 != 0`, followed by four passing tests and reproduction output `90.0`. Green records identify the final pricing digest recorded by the pin.
- **Correct:** the inspected exported patches distinguish staged minimal green from unstaged refactoring. Neither layer introduces unrelated functionality.

**No issues found.**

### B — repository #71

- **Correct:** `run_fixture.py:183–213` checks persisted deciding inputs before delivery, retains existing coverage, performs isolated characterization sensitivity, and records red/green/refactor execution. `test_handoffs.py:25–56` tests denied delivery, ticket preservation, dirty layers, stale evidence, and duplicate identity.
- **Correct:** `run_fixture.py:47–65` strips ambient Git routing/configuration and disables hooks. `test_handoffs.py:73–91` includes an external-repository preservation test.
- **Correct:** method outputs retain substantive limitations: prototype is not production-ready; acceptance-first leaves ambiguous/unavailable criteria blocked or unverified. These match the accepted design rather than promoting synthetic results into acceptance.
- **Correct:** fixture counters and actions are explicitly authored. They do **not** enforce agent investigation reuse, consent, delegation limits, or model policy. The recorded checks demonstrate harness behavior, not autonomous-agent compliance.

#### Finding S-71-01 — P1, blocking publication of the retained evidence

**Location:** `docs/validation/bug-to-fix/run_checks.py:24–26`; `results/checks/tdd.txt:28,75`; `results/checks/build-and-check.txt:8`.

The collector replaces only the repository root. Actual retained tracebacks still contain workstation-specific temporary paths beneath `/private/var/folders/…`.

**Binding requirement:** `docs/agents/project.md:15` requires public examples and retained artifacts to exclude workstation-specific paths; `AGENTS.md`’s validation instructions require portable retained paths. The collector’s own line 24 states this intended boundary.

**Impact:** newly retained public-validation artifacts disclose local filesystem details and violate the repository’s evidence-retention standard.

**Smallest fix:** normalize disposable workspace roots while preserving filenames, traceback lines, assertions, and outcomes; refresh these outputs. Add a regression covering temporary paths outside the repository root—the existing export test at `test_handoffs.py:68–71` checks only its own workspace strings and does not cover this collector.

**Nonblocking findings:** none.

**Decision-required findings:** none; the path-retention restriction is binding, not an architectural preference.

## Limitations and disposition

- No executable checks were run by this reviewer. Results described above are inspected recorded execution, not reviewer reruns.
- Protected fixture files were not opened. Preservation is supported by harness assertions and recorded test output, not independent inspection of their contents.
- No command-execution tool was available to independently inspect A’s live Git layers or recompute fingerprints. The pin was reread unchanged; that is not a fresh capture. Exported patches are supporting evidence, not proof of live-target equivalence.
- Package-check summaries omit source identities/environment. Under `agreement.md:12`, their association with current package revisions remains unverified here. Underlying sibling test implementations were outside authorized roots.
- PR-impact reporting, prerequisites, final two-axis freshness, acceptance, merge, and live inference are not certified by this report.

Documentation/changelog judgment: this scope adds internal validation evidence, not demonstrated public skill behavior; no public-behavior changelog change is established.

**Merge verdict: BLOCK** for repository scope B’s retained-path violation. This does not identify an R1/R2 defect in scope A. After correction, renew the affected collector/output inspection and checks; the root owns final freshness and disposition.