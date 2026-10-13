# Frozen review packet

Agreement: [baseline REQUEST.md](fixture/baseline/REQUEST.md), F1–F4; unchanged
in delivered copy. Standards: fixture AGENTS.md and README; outer repository
AGENTS.md/project/workflow and shared Work On / Review Delivery contracts.
Policy sources and agreement contents are pinned by [scope.json](scope.json).

## Identity and scope

Non-Git project executed outside any checkout; Git base/HEAD/index/branch are
inapplicable to the fixture. Workflow tested at outer repository revision
`e171a9b5f18495d5f388a1daeaa0dcdfba08527e`. Evidence is on the outer branch
`test/small-change-workflow-trial` based on that revision, PR target `main`.
Do not interpret its initial untracked evidence directory as delivered target
code or omit the non-Git source comparison.

- Actual before/after source copies: [baseline](fixture/baseline/) and
  [delivered](fixture/delivered/). Retained copies are manifest-equivalent to
  the temporary execution project; [delivered.diff](delivered.diff) exposes
  the full changes without temporary paths or timestamps.
- Included changed paths: `file_types.py`, `test_file_types.py`, `README.md`.
- Included unchanged support: `AGENTS.md`, `REQUEST.md`, sole caller
  `markdown_files` within `file_types.py`; all test assertions.
- Protected/excluded contents: `unrelated-note.txt`, `note-link`; synthetic
  unrelated work, do not read their contents or follow the link. Their bytes,
  full observed modes and link target are fingerprinted for F4. No unavailable
  material source; no renames, deletions, extra files or other ownership.
- Supporting packet: [plan](plan.md), capture/replay scripts, four raw check
  records, diff, runtime procedures and authoritative outer policy documents.
  SHA-256 support inventory is in scope.json. Review output and later completion
  report are outside this frozen input scope.
- Lead is the sole implementation author and freeze owner. No writes to source,
  tests, policy, agreement, scripts or raw evidence until both reports return
  and freshness/path discovery completes. Reviewer result artifacts only may
  be added. Both reviewers receive this same packet, not each other's reports
  or the lead's preferred review verdict.

## Actual check handoff (not independent review)

All commands were lead-executed using Python 3.14.7, standard library, macOS;
outer Git 2.54.0. `capture.py <fixture> evidence/NAME.json --test` invokes the
fixture's existing `python3 -B -m unittest -v` in the actual temporary target;
the JSON stores the check exit (distinct from capture utility exit).

| Record | State and observation |
| --- | --- |
| [Baseline](evidence/baseline.json) | Original implementation/assertions: exit 0, four existing tests pass. |
| [Red](evidence/red.json) | Added direct and caller mixed-case assertions only: exit 1; missing F1/F3 behavior, four assertion failures, not tooling failures. |
| [Green](evidence/green.json) | Suffix expression fix and README update: exit 0, six tests pass. |
| [Integrated](evidence/integrated.json) | Second execution against direct-built final target: exit 0, six tests pass; same input manifest as green. |

Tests changed no fixture files; before/after manifests match for every run.
Baseline→final comparison changes exactly the three owned paths. The retained
baseline/final copies match captured manifests. Pin/check compares complete
fixture path membership and supporting files before launch and after return.

Verification mapping: F1 direct mixed-case test; F2 unchanged negative and
no-trimming assertions; F3 both original and mixed-case caller tests (names,
order, duplicates); F4 complete before/after hashes, modes and symlink target.
Pure string classification has no access/persistence/destructive product paths;
protected unrelated artifacts are still explicitly checked. No live/production
check, cross-runtime certification or fixture acceptance is claimed.

## Reviewer contract

Separate fresh read-only contexts: Standards and Spec, not the lead author or
each other's conclusions. User authorized these two agents in the current
conversation. Each has a ten-minute finite timeout; two active workers maximum;
no recursive delegation, project mutation, shell execution, installation,
network, optional assessment or tracker mutation. Returning the configured
report artifact is allowed. Inspect actual source, agreement and raw records;
static inspection is not executing tests. Stop and report any inaccessible
material input or stale scope rather than inventing a pass.

Use Review Delivery entry, scope and report contracts at the tested source.
Standards checks binding policy, correctness, ownership, simplicity, regressions
and documentation. Spec maps every F1–F4 to source and raw evidence; both may
raise cross-cutting findings. Return inspected scope/coverage, findings with
stable IDs, locations, evidence, materiality and correction, or bounded
no-findings, plus limitations. Do not decide acceptance or mutate the fixture.

Checkpoint `small-change/F1-F4`, initially 0/2 repair cycles; any material
findings require lead disposition and fresh affected checks/review. The outer
#29 report must separately evaluate actual execution versus scripted replay
and unrun branches; this packet alone is not its completion verdict.
