# Small-change trial plan and entry/readiness return

Trial owner: the lead Pi agent, sole author/implementer. Parent #14, work #29.
Tested workflow source: `e171a9b5f18495d5f388a1daeaa0dcdfba08527e` (`main`).
Fixture agreement: [REQUEST.md](fixture/baseline/REQUEST.md), F1–F4.
Fixture policy: [AGENTS.md](fixture/baseline/AGENTS.md).
These are original synthetic inputs selected within #29, not customer approval.

## Entry and authority (actual lead execution)

The maintainer requested “Work on #29”, then approved the proposed two bounded,
read-only Standards/Spec agents with “yes go ahead”. Loaded the repository's
Work On entry and shared contract directly; no global skill installation or
legacy workflow invocation. Read project/workflow policy, #14/#29, accepted
#18 design, inventory and validation, and predecessor procedure outputs.

Read-only, paginated GitHub observations: #29 has native blockers #20
(database ID 5826825005) and #26 (5826826720), and native parent #14
(5825322858). Reverse blocker observations include #29 (5826827492).
#20 and #26 are closed as completed, with accepted integration through merged
PRs #35 (`ce07d95a4fa1ae35f44b2dfc6f812d86669618fe`) and #42
(`cd8ee6cd28d9068c96207a5d294dbb95ff709ba4`). No tracker mutation.

Repository Git preflight: clean `main`, equal to `origin/main` at the tested
revision after fetch; no PR for `main` or outstanding commits. Created
`test/small-change-workflow-trial` from that base, PR target `main`.
Resolved installed `implementation-preflight` from runtime skill discovery,
read its complete entry; compatible with explicit project branch policy and
protected-work preservation. No unrelated repository changes were present.

Prepared a disposable project outside any Git checkout from the retained
[baseline](fixture/baseline/). `git rev-parse --is-inside-work-tree` there
returned exit 128, “not a git repository”; fixture Git preflight is inapplicable.
Retained baseline/delivered directories are artifact copies, not independent
Git projects. The outer repository's branch preflight still applies.

Read actual fixture instructions, request, README, implementation, caller and
all existing test assertions. Chose raw-request → lightweight agreement →
technical readiness → direct build; no setup, specification issue, technical
questionnaire, ticketing or worker implementation. The supplied synthetic
agreement settles the relevant product branches and four concern dispositions;
no additional product questions are needed. No meanings/ADR changes.

## Technical return and ready-to-build decision (before implementation)

- Reuse `is_markdown` and its sole caller `markdown_files`; strings in, Boolean
  or unchanged filtered strings out, no I/O or persistent state. Keep API,
  caller, ordering and duplicate handling unchanged.
- Normalize only the compared final three-character suffix; preserve original
  filenames. One local expression change suffices; no wrapper/configuration.
- Risks: missing mixed-case suffixes (F1), accidentally accepting other suffixes
  or trimming (F2), lowercasing returned names or changing order (F3), touching
  unrelated user work (F4). Access/disclosure, persistence and destructive
  product operations are inapplicable: pure string classification, no I/O.
  Protected artifacts still need explicit before/after checks.
- Existing coverage: lowercase matching, final suffix negatives, no trimming,
  order/duplicates. Extend with mixed-case direct and caller assertions.
- Method: first run existing baseline, then demonstrate the new assertions fail
  for missing mixed-case behavior, apply the smallest fix, rerun tests and
  integrated verification. This is a lead-owned method, not `/tdd` invocation.
- Documentation owner: README behavior sentence; no fixture changelog/version
  policy exists. Outer repository changes only retain evidence; no public
  runtime behavior change, changelog entry or release-impact label needed.
- Ready to build: approved trial scope, fixed F1–F4 oracle, inspected design and
  checks, no dependencies inside fixture, exclusive lead ownership, safe outer
  Git preflight and non-Git fixture manifest. Independent review is still a
  later gate, not already completed.

## Evidence capture semantics

[capture.py](capture.py) fingerprints all immediate fixture paths, file bytes
and permissions without following symlinks. Tests run with Python `-B` to avoid
bytecode writes. JSON captures the exact command, Python version, actual check
exit/output and before/after manifest. The only output sanitization replaces
this disposable project's absolute path with `<fixture>`. Utility exit 0 means
capture succeeded, **not** that the captured test passed. The initial non-Git
probe's expected exit 128 is separate from the unittest regression failure.

Copied retained snapshots must match the actual project's manifests before
review. The lead freezes all fixture files, agreement, policies, plan, capture
script and raw check inputs during review; only reviewer output artifacts may
be added. At most two active read-only reviewers, fresh separate contexts,
finite 10-minute timeouts, no recursion, no code execution by reviewers.
Review Delivery is resolved from this project's named package mapping and
complete entry/scope/report contracts at the tested workflow revision; legacy
`code-review` is not substituted.

Checkpoint `small-change/F1-F4`: zero repair cycles spent initially; maximum two
under the shared contract. Red-before-green development is planned behavior
sensitivity, not an acceptance repair. If independent review identifies material
problems, preserve reports, start a bounded cycle before correcting, invalidate
and refresh affected evidence. Significant workflow defects become separately
proposed follow-ups, not an expansion of this trial.
