# Multi-ticket trial agreement and entry

Issue #30 under #14; tested package revision `77c4bb63cf944af770dff51b529eee15d65574fc`.
The maintainer requested #30 and then approved bounded read-only Standards/Spec
reviewers, including renewed reviews after repair. Approval covers synthetic
local execution and retained public evidence, not production tracker writes,
installation, deployment, merge or release.

## Entry and readiness

Repository preflight: clean `main`, HEAD equal to fetched `origin/main` at the
revision above; no open PR. Created `test/multi-ticket-failure-trial` from that
base; PR target `main`. Native read-only paginated observations: #30 parent #14,
blocked-by #28; #28 blocking includes #30. #28 is closed completed and accepted
integration is merged PR #44 at `e171a9b5f18495d5f388a1daeaa0dcdfba08527e`,
which is an ancestor of this base. Read predecessor recovery output, small-change
trial, accepted design and linked inventory/validation, actual Work On entry,
contracts/build/dispatch/recovery/verification/completion and Review Delivery
entry/scope/report. Installed preflight was read completely and is compatible.
Tracker library discovered in repository `setup-project` and read without setup
invocation; native IDs, pagination, directions, graph and evidence distinctions
are compatible. No installed copies are changed.

## Synthetic target

A disposable Python/Git project: canonicalize names, then render a comma-separated
report. Its policy permits the lead to make scoped local commits on a short-lived
feature branch, count direct target commits as integration, and mark synthetic
prerequisite acceptance only after relevant checks and independent review. This
fixture policy differs explicitly from this repository's PR-only completion.

- N1: `normalize_name(value)` strips surrounding whitespace and lowercases a
  string; empty strings remain empty. Inputs are strings; validation/coercion,
  Unicode normalization and locale-sensitive transformations are excluded.
- R1: `render_names(values)` returns normalized names joined by `", "`, preserving
  order, duplicates and empty values; an empty sequence returns an empty string.
- P1: unrelated staged/unstaged bytes, index entries, executable mode, untracked
  note and leaf symlink target survive all scoped commits and recovery.
- G1: coordinate parent 100, schedule work 101 before dependent 102; closed/ready
  101 alone never unlocks 102. Checks, acceptance and integration are separate.
- E1: failure and old review remain historical; one stable repair episode is
  carried through resume; affected checks and both axes refresh after behavior
  changes; final claims identify the actual integrated state.

Graph observations are an explicitly authorized mock of native endpoint results,
not a real GitHub fixture. Database IDs 9100–9102 differ from issue numbers.
Parent 100 (`spec`, ready) owns 101/102 (`implementation-step`, ready); 102 is
blocked by 101 and the reverse endpoint lists 102. One page per endpoint, complete
fixture graph; no external edges/ancestors. Adapter accepts GET only and rejects
unplanned writes; no production subprocess/network tracker route exists.

## Technical plan and bounds

Two ticket scopes: 101 owns `names.py`, `test_names.py` and its README behavior;
102 owns `report.py`, `test_report.py` and its README behavior, consuming the
stable normalized-string interface. Serialize shared README ownership and
interface changes. Parent is never a work assignment. Lead writes directly:
parallel implementers add no value for two tiny coupled slices. At most two
non-lead reviewers; fresh read-only contexts, ten-minute lifecycle bounds,
no recursive delegation or optional models. Freeze source and supporting inputs
for every review pair; reviewers receive actual retained files, not just hashes.

Checks use Python standard-library unittest and Git. Baseline tests establish
existing behavior. Inject a lowercasing-only implementation into ticket 101:
its whitespace assertion must fail. Preserve it and inspect actual state before
repair; no failed-worker/crashed-session simulation is claimed. Resume the same
lead after a deliberate verification/review checkpoint pause. Carry checkpoint
`101-normalization`, finding `N1-trim`, count 0/2 into recovery; correction spends
cycle 1. Dependent 102 remains unstarted until 101's refreshed evidence permits.
Then integrate 102 and run cross-ticket checks plus final independent reviews.

Expected oracle: `normalize_name(" A ") == "a"`, `normalize_name("") == ""`,
`render_names([" A ", "b", " A ", ""]) == "a, b, a, "`, and
`render_names([]) == ""`. No new abstraction, dependency or service is needed.
Security/disclosure risks use public synthetic content only; destructive and
persistent product behavior is absent. Preservation is checked through Git layers
and content/mode/target manifests, not just filenames.

Evidence home is this repository-only directory. Capture/replay utilities record
commands and snapshots; they do not decide frontiers, launch agents or implement
a scheduler. Source snapshots and raw check output are review inputs. Runtime
receipts/reports are retained separately. This is direct lead agent behavior in
Pi, not autonomous worker orchestration or certification of other runtimes.
Substantial workflow repairs require a separately bounded follow-up; this trial
changes no runtime skill contract, domain definition, ADR or live tracker graph.
