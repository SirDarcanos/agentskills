# Shape Work extraction evidence (#61)

## Scope and authority

Input clean `main`/`origin/main`: `ab540d53d604d501744f91581c165435bef3057a`. Fetched origin and created `feat/shape-work`, PR target `main`. Read #48/#61, accepted #50 design, inventory and acceptance mapping, context/workflow and affected full entries. Native #61 blocked-by read returned #60 closed; PR #85's merged Analyze extraction is present in the input commit. The design records explicit #50 acceptance and PR #75 merge authority. Eligibility uses this integrated source evidence, not closure alone.

The request authorizes this extraction and safe local checks, not delegation, installed migration, model calls, merge or release. Discovery now has one owner; Work On retains its broad entry and spec-writing/publication/gates. No #67 cutover, tracker graph change or installed grilling removal.

## Executed direct conversation walkthrough

This is an author-operated, in-session synthetic conversation: user turns below are scripted fixture inputs, not messages from the real maintainer. Agent responses are the author's actual application of the new entry to those inputs. The author read the complete entry, applied the bounded Analyze procedure directly to the inspected synthetic source and ran its baseline tests. No independent agent, autonomous conversation harness, installed slash command or real product approval is claimed. The transcript is execution evidence of this direct walkthrough, not just expected outputs; the package validation reference separately owns authored scenarios.

Target: synthetic private reading list represented by [reading_list.py](reading_list.py). Inspection/check authority only, conversation return; at most two discovery rounds after the initial intent clarification, limited to pinning and visible order. No product writes/publication. Baseline on Python 3.14.7: three tests passed (input order, privacy, empty list). Source SHA-256: `8bd75d96a037084637b56b5d10703d1ffbc3ac49771ee3e0d6d8eea57874cc71`.

### Round 1: intent and priority

**Scripted user:** “I lose track of the books I want to read next. Can we make them easier to find?”

**Actual response:** “Is this for your own list or a shared list? I recommend letting you pin books at the top of your own list, keeping everything else in its current order. Is choosing what to read next the priority, rather than reminders or sharing?”

**Scripted user:** “My own list. Pinning sounds right. Reminders can wait until I have enough books to need them; I don't want sharing.”

**Observed disposition:** proposed pinning becomes confirmed direction. Reminders deferred with revisit at larger list size; sharing excluded because the goal is a personal list. The exact ordering and limitation remain unresolved, not implicitly accepted.

### Bounded technical fact-finding, not a seam questionnaire

Resolved Analyze at the repository's explicit package location, not by sibling-install discovery. Read its complete entry. Handoff: inspect current reading-list ownership, order and relevant coverage only; use fixture identity above, confirmed personal-list intent, inspection/check authority, no writes; stop after this source and its assertions. No new method execution, external research or domain record.

**Actual inspected return:** `visible_books` lines 9–11 filters by reader and preserves input order. `reading_page` lines 14–15 consumes its result. Fixture records lines 21–25 contain reader/title only: no pin state or user-controlled ordering. Three executed tests support current order, no other reader's title, and empty-list behavior. New pin/unpin/order checks would be needed for implementation; these are recommendations, not executed feature passes. The existing reader filter is a boundary to retain. This source does not establish persistence, UI behavior, production scale or performance. Those remain future readiness questions, not facts to ask the user to engineer.

Analyze's narrowed fact question is answered; no full production-readiness claim or method availability claim. Technical lead can use existing function/caller seams and choose checks later without asking the owner to design them. Research is unnecessary because this question is answered by local primary evidence. No changed domain meaning or enduring architecture decision, so definitions are read/reused without domain-modeling invocation. Companion source identity is pinned by the input revision above; no installed package compatibility is certified.

### Round 2: consequential choice and success

**Actual response:** “The current list keeps your saved order. I recommend moving pinned books to the top while preserving that order within each group; unpinning puts a book back in its ordinary position. That avoids adding manual reordering, but you won't be able to arrange the pinned books yourself. Is that acceptable for this version? Would success mean you can spot your next books at the top and undo a pin without losing a book?”

**Scripted user:** “Yes. Keep that order, no manual reordering for now. I accept that limitation. That success description is right. Pins must not change anyone else's list.”

### Actual discovery return and stop

**Complete, synthetic agreement confirmed in the final scripted turn.** Goal: help an individual reader find their next books. Required now: pin/unpin in their own list; pinned group first; preserved existing relative order within both groups; unpin restores normal position; no lost entries or effects on another reader's list. Success: a reader finds pinned next books at the top, can undo the selection and still sees all their own books; privacy remains intact. Empty lists remain empty.

Four dispositions survive: pinning/undo/privacy required; reminders deferred until list growth warrants reconsideration; sharing excluded as outside personal-list intent; no manual ordering accepted explicitly in round 2. Proposals and assumptions are not counted as confirmations before that turn. Technical unknowns about persistence/UI/production checks remain for later analysis; they do not contradict the observable product intent. No production feasibility or delivery-readiness promise was made.

Return is conversation-only in the synthetic target. No existing authoritative product home needs reconciliation; no consumer documents changed. Repository transcript retention is within this issue's local synthetic validation scope. Stop after this usable brief: no formal spec, tickets, feature implementation or automatic next phase. No questions about internal abstractions, seams or routine method selection were sent to the owner.

## Executed settled-decision reuse walkthrough

Second supplied request: “Use that agreed pinning brief unchanged.” The same scripted owner, intent and source/check support apply. The author re-read the return and deciding source; `check.py` compared its SHA-256 before/after the baseline run and found the same bytes. No agreement delta, contradictory evidence or newly relevant path was supplied.

**Actual result:** complete reuse of the confirmed brief and all four dispositions; zero discovery questions, zero new Analyze/Research/domain/model calls, zero duplicate product artifacts. Old baseline checks remain evidence of current behavior, not pinning implementation. Standalone stops again; an authorized caller may inspect the brief and decide its next responsibility. This is direct reuse application and a byte-comparison check, not an autonomous stale-evidence test.

## Caller and failure-path inspection

Direct static inspection traced Work On entry → product-agreement adapter → catalog/approved source → inspected Shape Work return → retained spec-writing step. Current actionable agreements bypass fresh shaping; a missing/incompatible/ambiguous helper blocks required discovery only. A pending consequential limitation remains proposed and blocks reliance on that commitment; lack of document write permission returns the exact proposed delta. Standalone never inherits Work On's continuation. At initial implementation these failure/compatibility paths received source inspection only. The subsequent [executed caller walkthrough](caller-walkthrough.md) applies Work On's entry/product-agreement route through Shape Work and back to the retained brief/handoff, plus current-agreement bypass. It records actual direct-context actions and protected-file identity, not autonomous or installed-runtime compliance. Changed-source/domain/authority and missing-helper runtime trials remain unrun and visible.

## Check results

Executed results: Shape Work source/isolated frontmatter, bounds and five links passed; Work On source/isolated checks and 111 links passed. Root/evidence: 26 relative links passed. Three synthetic baseline tests passed and source identity remained unchanged. Existing delivery checker passed five source/isolated packages, 11 snapshot tests and 20 tracker/package tests (22 discovered, two standalone-companion skips); 54 repository documentation links passed. Python 3.9 syntax parsing passed for both new evidence scripts; actual execution used Python 3.14.7. Node/Marked rendered 11 changed Markdown documents (11 tables); directly inspected the rendered entry's headings, tables, branches and return statuses. This is rendered-HTML inspection, not browser visual testing. `git diff --check` passed; direct integrated diff/new-file review found no private/local-path/generated-artifact leakage, notice loss or duplicate discovery procedure. Reproducible local commands:

```sh
python3 -B docs/validation/shape-work/check.py
python3 -B docs/validation/delivery-coverage/check_packages.py
git diff --check
```

The first checks frontmatter, ordered procedure/completion bounds and links at source and in isolated non-sibling copies, plus the three fixture baseline tests and unchanged source identity. It reuses the maintained Markdown checker; it does not implement a discovery router or claim scripted assertions prove agent adherence. This instruction-only package ships no executable runtime.

## Maintainer wording clarification

After the initial PR, the maintainer confirmed that discovery should be exhaustive for relevant unresolved product concerns, with manageable rounds controlling pace rather than total question count. Updated the entry's exploration scope, round guidance and completion criterion accordingly. Confirmed decisions and discoverable facts still bypass user questions; explicit caller session limits return remaining concerns rather than implying completeness. Added a pacing/thoroughness scenario to package validation; it is authored coverage, not a newly executed multi-round trial. Existing two-round walkthrough remains evidence for its original inputs, not proof of this new scenario. Reran the source/isolated package checker and fixture baselines for this clarification; no new executable tests or effects.

## Acceptance and documentation

| #48 reference | #61 evidence |
| --- | --- |
| AC1 | Independent complete entry, bounded handoff/standalone return, conditional semantic discovery and isolated checks |
| AC4 | Current decision/source reuse; targeted invalidation contract; executed direct settled-brief reuse |
| AC5 | Manageable conversation, observable brief, all four dispositions, stop without automatic publication |
| AC8 | Bounded Analyze source inspection instead of a user engineering questionnaire; conditional research/domain gates |
| AC15 | Separate authored guidance, direct walkthrough, baseline and package checks, with unrun trials explicit |

Updated Shape Work entry/overview/validation/MIT notice; Work On entry/overview/contracts/discovery adapter/validation; root listing and one Unreleased Added entry. CONTEXT, ADRs, accepted design and operating policy remain unchanged because existing meanings/accepted ownership and authority suffice. Historical #14 execution records remain untouched. Original repository-owned discovery reused with Nicola Mustone MIT notice; no external body/template imported.

Executable-test baseline at the new evidence path: zero; three synthetic baseline tests added, none of the existing executable tests removed/updated. Removed old discovery scenario duplication from the caller validation and pointed to the new owner; retained caller-specific spec/publication checks. CI unchanged and no repository CI workflow; timing impact is unmeasured. Source rollback must revert package and caller adaptation coherently; it does not change installed copies.

At initial implementation, independent Standards/Spec review, installed/cross-runtime discovery, composed workflow trials and real non-scripted user conversation had not run. Subsequent review and direct caller-route validation are handled as follow-up evidence, not silently attributed to the original checks. Installed/cross-runtime discovery, full delivery trials and real non-scripted user conversation remain unrun. Initial implementation performed no delegation/model/service/installation/tracker mutation/product fix. The later explicit review request authorized two fresh read-only reviewer contexts; the caller trial itself remained direct, with no delegated trial agent or external effects. Direct author inspection and walkthroughs are not independent review or acceptance. #61 remains open until accepted and merged; the PR pins the delivered revision.
