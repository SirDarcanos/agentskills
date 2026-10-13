# #27 dispatch/integration evidence

Repository-local evidence, outside the installable package. [Dispatch](../../../work-on/references/dispatch.md) owns runtime behavior; [dispatch validation](../../../work-on/references/dispatch-validation.md) contains authored cases and the execution boundary.

## Reproduction and actual execution

From the repository root with Python 3.9+ and Git:

```sh
python3 -B docs/validation/work-on-dispatch/exercise.py
```

The author ran and inspected [exercise.py](exercise.py) with Python 3.14.7 and Git 2.54.0: exit 0. It uses the existing Review Delivery snapshot helper, creates an explicitly disposable local Git target, executes direct changes/checks/serial merges and removes only its own temporary fixture at the protocol's end. It launches no agents, installs nothing and performs no live tracker mutation, production merge, release or global skill update. Synthetic target policy permits these local merges; it does not override this repository's PR-only policy.

The frontier transitions are explicitly authored decisions asserted against synthetic observations, not an executable scheduling implementation. Parent P and children A/B/C/D all have plain descriptive titles and mapped readiness metadata. Native-observation fixtures have P owning A/B/C/D, C blocked by A and no other blocker edges. A/B overlap on `core.py`; D owns independent formatting; C consumes the agreed doubled-value interface. Fixture graph/label preservation is asserted, but no native API reconciliation is exercised.

Actual disposable revisions from this run (commit IDs vary on rerun):

| Result | Source revision | Target after serial integration |
| --- | --- | --- |
| Baseline | `e771cbac8283a9094fd14d74fcd6cb768ad306ae` | same |
| D, uppercase display | `012c1b3f6012646da9aa73cc848845aa9a9fe9fb` | same |
| A, doubled calculation | `2d6ce47c28230a93c3d5ec8cce35a75d7b12dbbd` | `fb9a750edf548c684b07050a4bc210f3b3600ffb` |
| B, shared-interface documentation | `1ca3c937add9f888173e1f02ca5bbba88487fc4b` | same |
| C, consume double plus one | `c7c70b43132e8a058152c259c11560ededc4b8f1` | same |

Final base-to-target diff SHA-256: `700ec68682fdbd628dbedc796f6345bf18a012cd4a2cfadefaf305713ce11863`. Pinned scope: `agreement.md`, `core.py`, `consumer.py`, `formatting.py` and their three assertion files, all mode 0644. Final `core.py` SHA-256: `7bf0aefaf419f7f92b685bc5603293729296d019526f25eefadc749bae785474`; `consumer.py`: `f07bf5841d052f97cba1aed56cc9dbbc3da44e5f822dc78deadeb62115c51841`. Staged/unstaged scoped diffs were empty at final verification; excluded `unrelated.txt` stayed byte-identical and untracked. Full temporary fingerprints/raw output were inspected locally, not committed with workstation paths.

## Inspected decisions against procedure

| Observed tool/fixture result | Lead's direct walkthrough disposition |
| --- | --- |
| Mapped candidates are A/B/C/D, not P; initial selected frontier A/D | Steps 1–2: parent coordinates. C waits for native prerequisite A; B serializes with A's core ownership despite no native blocker. Step metadata does not impose a linear order. |
| Direct local changes prepared on disjoint A/D branches from one baseline; diffs limited to owned paths; local checks pass | Steps 2–3: direct execution with zero workers is sufficient. These are scripted direct assignments, not worker launches or bounded-runtime evidence. |
| A synthetically marked closed with local green checks but absent integration/acceptance | Steps 2/5: C remains waiting. Closure and local checks supply no accepted integrated completion. |
| D integrated first, suite rerun, A source retained; C still waiting | Steps 4–5: unaffected work progresses independently, one integration at a time. Native observations remain unchanged. |
| A integrated, old snapshot check exits 1, repinned checks pass; acceptance still absent | Steps 4–5: evidence is refreshed at the actual target; integration alone still cannot unlock C under this fixture's acceptance rule. |
| Explicit mock acceptance recorded for A; source ancestor verified in target; current integrated check present | Steps 2/5: next eligible frontier B/C. Acceptance is a synthetic input, not reviewer/maintainer approval of this skill or the fixture. |
| B edits core only after A finishes; then C uses the stable interface; each serial integration detects old snapshot drift and reruns checks | Steps 3–5: overlapping ownership serialized; old-base A result combined with independent D safely. Relevant integrated evidence refreshed after every result. |
| Temporarily reverting doubled core makes the consumer assertion fail (`3 != 5`, exit 1); restoring it passes and snapshot freshness succeeds | Step 4: the cross-ticket check detects an actual interface regression, rather than relying only on owner summaries. This temporary fault demonstration is not a repair episode or acceptance pass. |
| All four source branches exist at end; sentinel and labels/edges unchanged | Steps 4–5: useful artifacts preserved through verified integration, then explicitly disposed only as this temporary test's protocol. No automatic cleanup behavior claimed. |

Direct static inspection also covered all 12 authored validation cases: equivalent mappings/subordinate roles, unknown/mismatched graph, capability blockers, combined capacity, bounded delegated envelope, unexpected returns, PR-only waiting, frozen scope and failed/unknown owner preservation. These are paper walkthroughs, **not executed agent scenarios**. Existing native graph procedure remains authoritative; no second graph engine was added.

## Gates, source state and documentation

Preflight: clean `main` at `cd8ee6cd28d9068c96207a5d294dbb95ff709ba4`, equal to fetched `origin/main`. Created `feat/multi-ticket-dispatch`, base/PR target `main`, no existing PR or unrelated work. Native #27 blocked-by inspection returned #22 (database ID 5826825517) and #26 (5826826720), both closed. Reverse blocking reads include #27; native parent #14 and its paginated child list include #27. Integrated predecessors: merged PR #37 at `6f8c35634f28aaab1181f38e4d3687115d4b5fb8` and PR #42 at the base above; their bodies, accepted design contract and actual shipped ticketing/completion outputs were read. Package revision is identified by this change's PR commit, distinct from disposable fixture revisions.

Build readiness: scoped approved #27 behavior, accepted design, integrated predecessors, safe preflight and one direct author. Implemented: dispatch/integration procedure and its routing/docs. Verified locally: fixture tool/assertion checks, snapshot freshness/regression sensitivity and structural checks. Unverified: independent Standards/Spec review and autonomous instruction execution. Acceptance remains unaccepted; an honest report is available while review/acceptance gates remain outstanding. #27 stays open pending maintainer acceptance and approved merge.

Updated dispatch/validation, entry/shared-contract/completion pointers, package/repository overviews, design implementation pointer and Unreleased changelog. No meaning/model, ADR/package boundary, authority, tracker vocabulary/relationship, legacy command or installed copy changed; those authoritative homes need no edits. Compatible new functionality has minor release impact; no label mutation or release requested. Recovery and integrated trials remain #28–#31, not silently added here.

Executed structural checks: 132 relative Markdown links/anchors in Work On and affected repository documents, 93 in an isolated Work On copy, frontmatter/invocation/routing inspection, Python 3.9 syntax parsing and `git diff --check`. Installed `marked` rendered entry, package overview, dispatch and validation; generated HTML headings/tables/prose were directly inspected without installing a renderer. These are structural/direct inspections, not independent review.

Not executed: authorized delegated workers/capacity saturation, timeout/conflict recovery, independent or renewed review, live graph/read-back failures, PR-only synthetic integration, separate worktrees, non-Git delivery and autonomous multi-ticket/failure trial. Dispatch instructions cover their boundaries, but this fixture does not certify those runtime behaviors. Missing independent review remains explicit; synthetic expected-failure exit 0 is not whole-agreement acceptance.
