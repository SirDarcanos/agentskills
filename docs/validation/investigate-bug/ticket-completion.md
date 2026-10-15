# Ticket-outcome checkpoint evidence

For [#122](https://github.com/SirDarcanos/agentskills/issues/122). Comparison base: `01142c714b6cdcd99d9b914d6773f497f39dd384` (inspected `origin/main`); branch: `fix/investigate-bug-ticket-completion`, PR target: `main`. This record contains a sanitized observation summary, not a copied private transcript.

## Observed failure and bounded diagnosis

The maintainer supplied the reporting session for local read-only inspection. The inspected sequence was:

1. A user reported Shape Work deferring necessary analysis and asked whether an old copy was installed.
2. The assistant loaded the complete Investigate Bug entry successfully. Its tool result is byte-identical to this change's baseline entry (SHA-256 `d18fb686c8be27e58979c6ae76b02a7b1398d90f4092c787c74450659b0c5d71`). There is no truncation marker in that result.
3. The assistant inspected the reported session and package identities, then returned findings. It did not search duplicate issues, load Write Tickets, prepare an exact proposal, or request publication approval before that final answer. No attempted ticketing tool failure or approval refusal appears in this interval.
4. A subsequent explicitly invoked advisor inspected Work On and recommended delivery. It did not account for the unfinished ticket handoff.
5. After the user challenged the omission and explicitly invoked Write Tickets, the same session inspected tracker guidance, searched existing issues, presented two exact proposals and awaited approval. Following approval, it created the issues and read them back. #122 is the canonical issue for this failure; no new ticket is needed.

**Established execution cause:** the agent treated diagnostic findings as the workflow's final output and omitted the required ticket-preparation continuation. It later advised from those findings rather than the unfinished ticket state. This is observed instruction noncompliance, not evidence that the package lacked a publication procedure.

**Rejected explanations:** an outdated or partially loaded Investigate Bug entry does not explain this instance; the complete baseline instructions were available. No failed Write Tickets discovery/execution or withheld approval explains the initial stop because neither was attempted. Eventual publication shows the later route worked, not that availability was checked at the initial stop.

**Unproven:** why the agent failed to follow loaded instructions. The old step 3 said “Stop when” probing was done, while step 5 required continuation; that local stopping cue and the publication-focused companion wording are plausible contributing ambiguities, not a demonstrated unique root cause. This correction removes those ambiguities and requires an inspectable ticket outcome. Instruction changes are not an enforced runtime state machine or proof of reliable future compliance.

Diagnostic bound: inspect the supplied session's investigation/advice/ticketing sequence, compare the loaded entry with repository source, and inspect existing package/fixture coverage. No recursive session search, model assessment, diagnostic product edits or installed changes. Prior source inspection is reused; the supplied session fills the missing execution evidence only.

## Bounded correction and acceptance mapping

Use Build and Check for one documentation increment followed by package/link inspection, then aligned overview/validation/changelog evidence and relevant offline checks. No executable production engine, new tracker algorithm or advisor implementation is introduced. Write Tickets still owns proposals, approval, duplicate reconciliation, writes and read-back; Work On still owns separately requested delivery.

| #122 criterion | Source-level correction and evidence category |
| --- | --- |
| Determine why execution stopped; do not assume stronger wording suffices | Session observations above distinguish the omitted continuation from missing instructions or tool failure. Cognitive cause and future adherence remain unproven. |
| Confirmed and unresolved cause reach an exact proposal without another skill invocation | Entry dependencies require direct drafting continuation; step 3 ends probing, not the workflow; steps 4–5 require the proposal or a named capability blocker. Static walkthroughs cover both routes. |
| Withheld approval yields labeled draft; approved publication is read back | Step 5 ticket-outcome table distinguishes draft, verified publication and failed/unknown persistence. Existing fixtures exercise approved synthetic persistence; withheld-approval routing is static, not an executed agent trial. |
| Duplicate reconciliation; investigation-only never starts delivery | Existing canonical issue and approved-delta route preserved; step 5 requires its actual state. Existing synthetic duplicate/protected-byte checks are reused. |
| Actionable published ticket recommends Work On, never automatically invokes it | Explicit next-action rule after verified publication/reconciliation; drafts/unresolved/persistence blockers retain their own next action. Static inspection only. |
| Later authorized Work On reuses current investigation | Existing final receiver identity comparison and gap-only reuse retained; fixture reuse test inspects persisted evidence without a new reproduction. This is not a later autonomous Work On trial. |

The package validation reference adds seven authored ticket-outcome walkthroughs. They are not seven executed tests. Existing tests contain seven investigation unittest methods and ten Write Tickets methods; none are added, removed, moved or modified by this change. Those fixtures execute synthetic buggy code and JSON persistence, but their caller routing/approval is authored. They cannot detect an agent that reads and ignores the procedure.

## Checks and limitations

The first entry-only increment passed `python3 -B docs/validation/investigate-bug/check.py` (source/isolated frontmatter, links/anchors, procedure bounds, Python syntax and notices) and `git diff --check` before dependent documentation edits.

Final package, fixture, Markdown and freshness results are recorded in the PR with their raw execution evidence and independent review reports. The relevant commands are:

```sh
python3 -B docs/validation/investigate-bug/check.py
python3 -B -m unittest discover -s docs/validation/investigate-bug -p 'test_*.py' -v
python3 -B -m unittest discover -s docs/validation/write-tickets -p 'test_*.py' -v
git diff --check
```

No new autonomous before/after agent trial, live tracker mutation trial, installed discovery trial or later product-fix trial is performed. The supplied historical session is real observed agent behavior; static walkthroughs and the existing offline fixtures remain separate evidence categories. Acceptance claims must stay within these source-level and synthetic limits.

## Authority, state and documentation

The user's Work On request for #122 authorizes this bounded repository correction under project workflow; inspection of the supplied private session is local only. No raw transcript, private product material or workstation path is retained publicly. Initial working tree was clean; previous branch PR #123 was merged. A new branch was created from current `origin/main`, without transferring unrelated work. Native blocked-by returned an empty list; the parent endpoint reported no parent. No labels or native relationships changed.

Changed homes: Investigate Bug entry, package overview, package validation, this evidence record and the existing Unreleased Added changelog entry. The skill is not in a published release, so no separate Fixed bullet is added. Compatible instruction correction (patch impact); no release or metadata mutation is implied. Public catalog description remains accurate; domain meanings, ADRs, design ownership, Work On, Write Tickets and the advisor package need no change. Repository sources contain no GitHub Actions jobs; external automation and hosted duration/compute are unmeasured.

Root lead owns all edits. No implementation/exploration workers or optional assessments; independent Standards/Spec review may use two read-only slots with finite 600-second bounds under standing project permission. Checkpoint `122-ticket-outcome`: zero repair cycles spent before review. Scoped writes freeze for verification/review; original review reports and raw logs stay separate from neutral reviewer inputs. PR/report evidence records final snapshot equivalence and any findings/disposition. Keep #122 open until accepted and merged. Merging source does not install, deploy or release it; reverting source cannot undo tickets already published by any consumer.
