# Investigate Bug validation

Read the complete entry and README before changes. This is an instruction package, not an executable diagnosis/readiness engine.

## Package checks

1. Check discoverable frontmatter and ordinary/bounded triggers; investigation-only must stop at the ticket.
2. Render and inspect Markdown; follow every internal link. Copy the whole package to a non-sibling temporary catalog, checking the license and links there. Resolve Write Tickets through catalog/approved-location discovery, not relative sibling links. Missing/ambiguous companions block dependent persistence; drafting remains possible.
3. Inspect invocation, exact execution/publication authority, finite bounds, complete ticket content, deciding-input reuse/invalidation and probe ownership/cleanup. Inspect final diffs for unrelated changes, credentials, private data and nonportable paths.
4. Record affected docs, actual commands/results and limitations separately from authored scenarios. No installed migration, external assessment, delegation or live tracker mutation is needed.

## Repository-only offline checks

Python 3.9+; repository fixtures are not shipped runtime dependencies:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 docs/validation/investigate-bug/check.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s docs/validation/investigate-bug -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s docs/validation/write-tickets -p 'test_*.py'
git diff --check
```

The tests run real synthetic buggy code, bounded observations and persisted JSON tracker read-back. Caller decisions and ticket contents are authored fixtures, not an autonomous agent executing these instructions or proof of policy enforcement. Live tracker/API, installed discovery and a real later Work On fix require separate trials/authority. Copied packages can perform the static steps without repository scripts.

## Ticket-outcome regression walkthroughs

Walk these against steps 3–5 and the actual returned artifact; findings or a suggestion to run Write Tickets do not count as a proposal. These are authored scenarios, not executed agent trials.

| Starting state | Required observable outcome |
| --- | --- |
| Confirmed symptom and established cause; no publication approval | Follow Write Tickets in the same context, inspect duplicates and present its exact title/body/classification and effects as **Draft — not published**. Request publication approval, not another skill invocation; make zero tracker writes. |
| Confirmed symptom but unresolved cause, or unconfirmed symptom | End bounded probing, then continue to an exact **investigation-only** proposal with attempted evidence, blocker and diagnostic acceptance/next action. Missing cause does not end the workflow at findings. |
| User withholds or declines approval | Retain the labeled exact draft and distinguish diagnostic readiness from unpublished state. No persistence claim, tracker mutation or automatic delivery. A later “what now?” points to the pending ticket outcome, not a fix. |
| Exact proposal approved | Publish only approved effects through Write Tickets; inspect actual contents, classification and read-back before reporting publication. Missing/unknown read-back remains partial/blocked. |
| Matching current issue exists | Inspect the canonical issue and propose only needed approved reconciliation; preserve unrelated body/labels/edges and verify the actual delta. No second issue or automatic closure. |
| Actionable fix ticket published/reconciled and read back | Recommend Work On with canonical identity and current evidence, without invoking it. A later explicit delivery request compares deciding identities and reuses current investigation; it fills only actual gaps. |
| Write Tickets unavailable/incompatible | Return a labeled supported draft with the exact capability blocker; do not claim an executed handoff, install a helper or route around the blocker into delivery. |

For #122's observed execution omission, rejected alternatives and evidence limits, read the repository's `docs/validation/investigate-bug/ticket-completion.md` when available. It is delivery evidence, not a copied-package runtime dependency.

## Procedure coverage

- Confirmed: inspect expectation source, actual reproduction, causal evidence, all ticket fields, cleanup and verified persistence; investigation-only leaves original product bytes unchanged.
- Intermittent/unconfirmed: record failing/passing attempts and bound, distinguish a harness/environment failure, never infer absence from a pass or a ready cause from the symptom.
- Unresolved cause: publish only investigation work within approval; attempted checks, remaining hypotheses, blocker and diagnostic next action remain visible.
- Duplicate/partial publication: compare actual behavior/version/cause, preserve unrelated issue content/labels/edges, reconcile only exact approved delta; uncertain creation/read-back is not retried blindly.
- Current/stale: compare relevant committed and dirty identities, consume complete current evidence directly; caller/config change invalidates dependent cause/check findings only, unaffected expectation/impact stays. Unknown impact expands staleness rather than retaining unsupported readiness.
- Artifacts: useful reproduction retained only under policy, owned probes restored/removed without erasing intervening edits; failed cleanup disclosed and ready handoff blocked.
- Missing helpers/approval: useful draft and capability blocker, no installation, legacy diagnosis fallback, automatic readiness or delivery. A separate fix request supplies its own compatible lead gate and consumes evidence; discovery alone does not grant it.

**Done:** applicable checks have recorded results and material unrun routes remain explicit. Authored scenarios are not executed agent workflow evidence.
