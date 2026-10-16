# Validation

From the repository root, using Python 3.9+:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s workflow/setup-project/tests -p 'test_*.py'
python3 workflow/setup-project/scripts/dependencies.py --help
git diff --check
```

From a copied standalone package, run unittest discovery against `tests/`. Companion-specific packaging checks may skip when the GitHub or domain-modeling package is not beside it; report skips rather than claiming those companions were checked. Each package's relative links must resolve within its copied directory; runtime discovery, not sibling file paths, supplies companions.

The unit tests exercise the real dependency reconciler through an in-memory GitHub transport and mock the CLI transport. They cover additive/read-only behavior, ID direction, existing/transitive graph cycles, reruns, partial failure, read-back mismatches, API errors, pagination, unsupported scope, and database-ID mismatches in existing and newly written relationships. No network, credentials, or model calls are used. Packaging checks verify entry-point fields and shipped relative links, not semantic correctness.

For delivery-library discovery changes, use the caller's resolved Work On validation reference and its “Complete-read and reference-recovery cases” against this package's read-only library entry. Check the tracker link from the complete inspected entry in both repository and independently copied layouts; this does not invoke setup or grant tracker mutations.

## Compact agreement and reconciliation cases

The [local agreement fixture](../tests/fixtures/local-agreement/AGENTS.md) is authored example output, also usable as existing equivalent guidance. It uses a non-default home, no tracker/domain artifacts, denied auxiliary models and tighter delegation restrictions. Package tests guard links and selected contract clauses only: there is no executable setup generator or semantic compatibility classifier. Do not call these assertions agent behavior.

For a direct static walkthrough, map the fixture to the documentation contract's six responsibilities, follow its entry link and inspect the following deltas. Record reasoning as static inspection. An actual agent trial must separately record actions, before/after bytes/modes/link targets and outputs; do not infer no-op behavior from a fixture that was never run.

| Fixture variation | Expected reconciliation / negative effects |
| --- | --- |
| New local project with the fixture's confirmed decisions | Propose compact agreement/entry only; final exact approval precedes writes; no tracker, glossary, ADR or model-policy placeholders |
| Existing fixture unchanged; no default `docs/agents/` files | All responsibilities already satisfied; no regeneration, rename, timestamp churn, permission interview or setup ceremony |
| Agreement absent, or common safety/verification section missing | Identify exact missing responsibility and dependent workflow; recommend explicit setup/reconciliation, no silent invocation or fabricated policy |
| Existing PR auto-publication instruction conflicts with selected delivery-before-PR boundary | Show exact changed-decision/conflict and effects; preserve bytes until approved; do not import the newer skill's authority |
| Denied assessments, no tracker or domain terms | Valid restrictions/omissions; direct local work remains supported, remote publication unavailable; no model calls or empty records |
| Existing tighter delegation or repair restriction | Preserve it; only an exact approved delta changes authority; no new concurrency cap from a template |
| Confirmed term update vs unapproved ADR replacement | Current authorized glossary maintenance remains required; ADR proposal stays unwritten/unaccepted until explicit permission, preserving history |
| Migrated project agreement with legacy Work On/investigation consumers | Keep all live library targets and unique safeguards; report incompatible legacy endpoints as not yet migrated, never auto-publish ticket/PR or alter installed copies |
| Approved targeted delta, then second inspection | No substantive remaining delta; preserve unrelated custom content, index and symlink arrangements; uncertain effects still require reconciliation |

Measure actual mandatory instruction closure by selected branch, not just the entry file. For example, new local-only setup with no assessment candidates loads entry, documentation contract and discovery, plus release guidance only for actual history work; reconciliation is additional for existing guidance. Count per-context files once using whitespace words, report baseline revision and limits. Do not claim token savings, elapsed speed or runtime adherence from static counts. Preserve historical design measurements unchanged.

## Agent scenario matrix

Use temporary fixture projects and a command shim returning synthetic GitHub observations; it must reject unplanned writes. These scenarios require an actual agent walkthrough to claim behavioral validation. Reading them or passing Python tests does not execute them.

| Scenario / initial evidence | Required observation |
| --- | --- |
| New GitHub target; no files; identity and protections unresolved | Present target/Git only first, wait; files/permissions second, wait; history/safeguards then labels, each confirmed separately. Final brief apply confirmation; no mutations before it; approved baseline through companion and remote read-back. |
| New workflow authority vs explicit existing restriction; auxiliary assessments set to none | Files/permissions defaults ordinary skill work, bounded delegation, independent read-only review and lead-owned repair/recheck/re-review to allowed within requested scope. No extra internal-specialist/repair prompts; user-selected stages remain distinct and Jev/Clef/Nimble remain gated. Preserve binding restrictions; setup itself launches no delivery/review. |
| Delivery review finds in-scope defect, justified improvement, scope change and nonessential suggestion | Lead fixes valid scoped findings, reruns affected checks and renews significant-change review within existing bounds; unresolved material findings block acceptance. Escalate scope changes and explicitly disposition suggestions; reviewers stay read-only. |
| Standalone review-only request under ordinary-workflow permission | Return review report without unsolicited fixes; standing execution permission does not expand the requested task. |
| Labels include spaced onboarding names, existing hyphenated destination, custom labels and automation | Explicit keep/rename/add/consolidate/delete/unresolved groups account for all labels. Retained spaced names become hyphenated through approved rename or collision-aware consolidation; blocked consumers prevent destructive changes. |
| New remote with provisional defaults differs from actual post-creation inventory | Read back labels; obtain focused approval for unexpected dispositions before mutation, without restarting settled steps. |
| Later answer changes Git decision; interrupted interview or unchanged rerun | Reopen affected delta only; preserve other confirmations; no duplicate full-plan dump, writes before execution approval, or repeated unchanged questions. |
| Existing repo with custom/default labels, enabled Wiki, rules, and dirty file | Configuration route; audit every label and open/closed issue/PR usage; preserve unapproved settings/work; no duplicate rules. |
| Unused default label vs zero-assignment automation label vs retired historical label | Propose evidence-backed dispositions; do not equate zero count with unused; migrate/accept historical effects only with approval; verify cleanup. |
| Existing SemVer changelog with release automation | Preserve history, source authority, and automation-compatible patch/minor/major roles; no version bump or release. |
| Missing changelog with confirmed policy vs generated fragments vs unresolved/CalVer policy | Approved evidence-backed creation, source-level maintenance, or clarification respectively; no forced SemVer or invented releases. |
| Spec creation with `spec` or an approved equivalent, plus ordinary implementation tickets | Apply and read back the spec label at creation; distinguish it from readiness and native parentage; backfill only approved known specs. |
| Project using `spec`/`implementation-step` and plain titles vs approved equivalent roles/prefixed titles | Record the actual mutually exclusive workflow roles and title policy; apply/read back mapped roles without imposing exact names or renaming history without approval. |
| Parent spec, design/validation work tickets, subordinate spec, delivery PR and a ready-but-blocked child | Classify purpose and parentage: use the work-ticket role for bounded steps, not the parent/subordinate spec or PR. Assess other labels independently; preserve native blockers and unrelated labels. |
| Draft spec vs accepted agreement with resolved shared design; predecessor merge | No automatic readiness on publication. Reassess parent/child readiness from decisions and integration evidence within authority; coordinate eligible children rather than scheduling the parent twice. |
| Label consolidation/rename interrupted after assignment migration | Inspect actual state; preserve unrelated assignments; update consumers before removing source; no blind retries or recreation on clean rerun. |
| Local-only request vs requested GitHub with unavailable auth | First needs no auth; second reports remote blocker and only independently approved local progress. |
| Solo high-risk product vs team low-risk tool | Separate maintenance and risk decisions; neither automatically gains/loses safeguards. |
| Director-led vs technical co-design preference | Same accountability; different question framing; no competence labels or unnecessary private metadata. |
| CLAUDE-only, symlinked dual entry points, conflicting dual files | Preserve valid arrangement; inspect links; resolve conflicts before editing. |
| Matt-style agent docs and a multi-context domain map | Map current authorities; retain contexts, tracker vocabulary, and relevant ADRs. |
| Unchanged rerun vs changed operating requirements | No substantive clean-rerun changes; focused approved delta for new constraints. |
| Partial remote write followed by timeout | Re-inspect before retry; retain successes; report uncertainty and never recreate blindly. |
| Missing helper, missing permission, unsupported required control | Explicit affected blocker; no installation, weakened baseline, or prose-only false success. |
| Native graph: correct edges, reverse edges, cycle, foreign parent, paginated results | Distinguish hierarchy/blockers; verify IDs and direction; no implicit reparenting; stop on graph conflict or missing read-back. |
| No terms/ADR; confirmed term; proposed decision; superseded ADR | Explicitly omit unnecessary domain route; otherwise use domain-modeling and inspect its evidence. |
| Domain companion absent or same-named incompatible installation | Block required domain work; no automatic install/replacement or fallback; independent approved local work stays possible. |
| Domain plan-only handoff followed by approved exact delta | Planning makes no writes; deltas confirmed in their step, then brief execution approval; reuse confirmed answers; writes stay within approved scope. |
| Installed Jev/Nimble/Clef variants plus another assessment skill; no settled policy | For unresolved choices or proposed changes, name each actual installed skill and explain purpose, transport/disclosure and cost/service implications before asking disallowed/explicit-request-only/bounded automatic choices. No generic consent or automatic opt-in; unsupported automatic mode is unavailable. |
| No assessment skills vs unavailable discovery; owner declines all; broad “yes” answer | Distinguish none from unknown, offer no installation, and invite other allowances/prohibitions even if assessments are declined. Refine broad consent into named bounded rules before effective permission. |
| Mixed per-skill choices, extra prohibition, existing policy and newly installed assessment | Preserve confirmed choices and binding restrictions, record extra rule in its proper home, resolve only gaps and approve deltas. New skill inherits no permission; no model/service actions occur. |
| Model policy absent; confirmed none; local-only; bounded hosted permission | Follow [model-use agreement](model-use.md); propose before writing, require exact approval, record limits/provenance and pointers; zero model/service/credential/install effects. |
| Existing authoritative equivalent, unchanged rerun, or missing pointer | Preserve home, custom content, rationale/approval and budget scope; repair only an approved pointer delta. No silent permission expansion or timestamp churn. |
| Missing exact identity/disclosure/shared limits, conflicting authorities, or approval pending | Block affected permission, ask only consequential gaps; discovery remains proposal-only with unchanged target files. |
| Explicit-only assessment package with a policy proposal | Policy cannot bypass current frontmatter/body gates; report compatibility limit. Runtime enforcement fixtures belong to assessment packages, not setup document checks. |
| Contradictory docs/code or sensitive input | Resolve/flag authority; sanitize output; do not silently override policy. |

For a repeatable local fixture, start with an authored AGENTS or CLAUDE file, project/workflow guidance, an untracked sentinel, and (where relevant) a context map/ADR. Record original byte hashes and the exact synthetic GitHub state. Include both approved deltas and exclusions. After the agent run, compare the diff, command log, remote read-back, and report to the plan; run again to check idempotence. Keep fixtures synthetic, and retain assessment artifacts only in an approved location. For model-policy fixtures, use synthetic owner approvals confined to disposable targets (never this repository), snapshot input/output bytes, verify allowed document deltas and entry-point links, then directly rerun inspection without writing. Record tool actions to establish zero service/model/credential/install operations; file assertions alone do not establish that property. Retain executed evidence separately from this authored matrix.

## Review and completion evidence

- Read generated Markdown and frontmatter. Follow links in the package and produced entry points.
- Confirm documentation ownership, practical read conditions, and no duplicated policy homes.
- Inspect commands with installed help/current API docs; test scripts in their named interpreter.
- Audit the diff for credentials, private paths, identifying profiles, generated outputs, and accidental global-install changes.
- Record executed commands/results separately from static/manual scenario review and unrun live paths.
- An integration review checks that required companions resolve and command-only consent gates are respected; a model's approval is not evidence of execution.

Live GitHub mutation requires separate approval of a disposable repository and exact changes. Do not create real repos/issues, alter production labels/protections, push, deploy, or call billable models merely to validate this package.
