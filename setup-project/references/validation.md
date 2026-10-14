# Validation

From the repository root, using Python 3.9+:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s setup-project/tests -p 'test_*.py'
python3 setup-project/scripts/dependencies.py --help
git diff --check
```

From a copied standalone package, run unittest discovery against `tests/`. Companion-specific packaging checks may skip when the GitHub or domain-modeling package is not beside it; report skips rather than claiming those companions were checked. Each package's relative links must resolve within its copied directory; runtime discovery, not sibling file paths, supplies companions.

The unit tests exercise the real dependency reconciler through an in-memory GitHub transport and mock the CLI transport. They cover additive/read-only behavior, ID direction, existing/transitive graph cycles, reruns, partial failure, read-back mismatches, API errors, pagination, unsupported scope, and database-ID mismatches in existing and newly written relationships. No network, credentials, or model calls are used. Packaging checks verify entry-point fields and shipped relative links, not semantic correctness.

## Agent scenario matrix

Use temporary fixture projects and a command shim returning synthetic GitHub observations; it must reject unplanned writes. These scenarios require an actual agent walkthrough to claim behavioral validation. Reading them or passing Python tests does not execute them.

| Scenario / initial evidence | Required observation |
| --- | --- |
| New GitHub target; no files; identity and protections approved | One plan; approved baseline through companion; meaningful docs; exact labels; remote read-back. |
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
| Domain plan-only handoff followed by approved exact delta | Planning makes no writes; one setup approval; reuse confirmed answers; writes stay within approved scope. |
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
