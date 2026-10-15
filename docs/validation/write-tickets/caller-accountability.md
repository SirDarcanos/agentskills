# Caller accountability evidence (#117)

## Scope and method

Agreement: [#117](https://github.com/SirDarcanos/agentskills/issues/117), OWN1–OWN5. Base: `7d6de09` (`origin/main` at entry); branch `fix/caller-specialist-accountability`. Clean initial worktree; no unrelated dirty work. Native blocked-by read returned `[]`; parent endpoint returned “No parent issue found,” consistent with the standalone agreement. No relationship writes were made.

The lead used build-and-check for two documentation increments: entry instructions, then package overviews/regression guidance/changelog. Each increment passed package checks and `git diff --check` before dependent progress. Companions were resolved from the runtime catalog (Work On, Implementation Preflight, Build and Check, Writing for Agents, Review Delivery); source identities for review are retained in the task snapshot. Analyze and Write Tickets were inspected at this repository base. The tracker library was read without invoking setup. No optional assessment calls or installed-copy changes.

## Direct synthetic walkthrough

These are source-informed actions and decisions by the author in this delivery, **not an autonomous agent trial or live tracker exercise**. The existing synthetic `docs/validation/analyze/fixture.py` was copied into a disposable directory and executed: four baseline tests passed. Original and copied SHA-256 both equaled `3799956a0532d58a7b1962bdb1de8ede0fcd826fc02d07bf1454775912e777f7`. The source was inspected, not modified. Synthetic target: `example/ticket-sandbox` (not contacted).

### 1. Authorized prerequisite and continuation — OWN1–OWN3

Input: prepare tickets for adding a trailing newline to nonempty authorized exports, retaining empty exports and access denial. Inspection and conversation drafting permitted; no publication permission. Technical readiness initially missing.

Direct bounded Analyze pass: inspected `export_rows`, its `download` caller and all four baseline assertions. The existing seam is sufficient; recommend TDD with nonempty/empty export and download-body expectations, retaining denial. Current baseline tests pass but do not assert the proposed newline. No research, new abstraction, dependency split or user seam choice is needed. This is a recommendation, not an implementation.

Caller consumption: inspected that support, chose one cohesive ticket rather than splitting coupled exporter/caller work, and continued to the complete draft below. No redundant “may I analyze?” prompt and no hand-back asking the user to turn findings into tickets. Ordinary technical inspection is already authorized; publication is not.

### 2. Standalone Analyze — OWN5

Input: analyze the same newline proposal only. Direct result: the supported brief above, test-first recommendation and missing newline assertions. Stopped without draft publication, implementation, PR or scheduling. The caller continuation in case 1 depends on its original ticketing request, not on Analyze granting effects.

### 3. Consequential scope decision — OWN3/OWN5

Variant: someone suggests dropping access-denial coverage to simplify the change. That alters protected product coverage. Direct disposition: retain denial and ask, “Should unauthorized downloads remain denied? I recommend keeping the existing restriction.” Unaffected draft preparation can continue; technical method choice does not approve removing access control.

### 4. Decision-ready approval with complete draft — OWN4

Complete synthetic plan **P1**, draft **T1**:

- Target: `example/ticket-sandbox`; create one issue. No updates to existing issues, labels, parentage or blocker edges; no readiness assignment.
- Title: “Terminate nonempty authorized exports with a newline”.
- Body: “Ensure nonempty authorized exports end in one newline, including the download response body. Preserve empty output and denial for unauthorized downloads. Scope: `export_rows`, its `download` caller and relevant tests in the synthetic fixture. Acceptance: nonempty rows `[1, 2]` produce `1\n2\n`; empty rows produce an empty string; unauthorized downloads raise `PermissionError`; download MIME remains `text/plain`. Verify existing baseline and targeted nonempty/empty/download/denial tests. Use the existing export seam; no streaming work, account changes or dependency migration. Standalone work with no execution prerequisites.”

Direct approval-request draft: “I recommend one ticket to add the newline while preserving empty exports and access denial. May I publish plan P1/T1 above to `example/ticket-sandbox`? This creates one issue only; no labels or relationships change.” This is a walkthrough artifact, not a real approval request or evidence that approval was granted. Technical detail remains inspectable in T1 without requiring a method-selection questionnaire.

### 5. Missing authority and changed effects — OWN2/OWN4/OWN5

No publication approval was supplied: stopped at P1/T1, with zero tracker writes. Variant: assume P1 was approved but a later draft adds a second ticket or blocker edge. That is not P1; reconcile the changed delta and obtain renewed approval before affected writes. Incompatible/missing Analyze would instead block technical readiness with the bounded missing-evidence handoff; it would not justify installation, unsupported readiness or publication. These variants are direct procedure walkthroughs, not API execution or runtime failure injection.

## Executed checks and limitations

- `python3 -B docs/validation/write-tickets/check.py`: passed source/isolated package frontmatter, procedure bounds, links/anchors, notices and Python syntax; retained Work On adapter checks passed.
- `python3 -B workflow/analyze/scripts/check-fixture.py`: six tests passed; availability/freshness fixtures, not agent compliance.
- `python3 -B -m unittest discover -s docs/validation/write-tickets -p 'test_*.py'`: ten passed.
- `python3 -B -m unittest discover -s workflow/setup-project/tests -p 'test_*.py'`: 22 passed.
- Disposable Analyze source baseline: four passed; dependency helper `--help` and `git diff --check` passed.

No tests were added/deleted or assertions weakened. Existing tests protect tracker reconciliation and analysis fixtures, not natural-language caller adherence; the direct walkthrough supplies bounded instruction evidence. Live publication, installed discovery, autonomous workflow compliance and browser rendering were not run. Inspect Markdown structure/frontmatter and isolated links separately from those limitations. No CI configuration exists or changed; no CI timing claim.

## Documentation disposition

Updated both package entries, overviews and regression guidance. Changelog retains one Unreleased Added entry per not-yet-released package, updated with #117. Public impact is a compatible behavior fix (patch), not publication authority. Existing Work On adapters already inspect returns and continue under their own authority, so no duplicate continuation procedure was added there. No ownership migration, domain/ADR change or index change; historical evidence is preserved. The private incident transcript and unrelated project content were not used as fixtures or published.

Independent review reports and final snapshot/gate decisions remain in the delivery task/PR record rather than this neutral reviewer input. Issue #117 stays open pending maintainer acceptance and merge. No merge, release, installation, model service action or live tracker fixture mutation is implied.
