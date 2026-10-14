# Analyze extraction evidence (#60)

## Scope and authority

Implemented under the maintainer's request to work on #60, not #69. Input `main`/`origin/main`: `772d424432a4caa771f2baa16aab7ad627e67cfa`; clean worktree; branch `feat/standalone-analyze`, PR target `main`. Read #48/#50, accepted design, inventory and validation mapping. Read-only native #60 blocker endpoint returned #54 closed; PR #78's merged research commit `bc22076610581b71b883217753fff1e6b809215c` is integrated in the input source. #50 design records explicit acceptance and PR #75 merge authority. No prerequisite closure is used as a substitute for accepted integration.

This extraction moves technical-readiness ownership to Analyze and retains a thin Work On adapter. It does not narrow Work On, move its loops/dispatch, implement a product, alter native relationships, update installed copies or enable model use. Inspection and safe local synthetic checks are authorized; delegation and external assessment are not granted and were not run.

## Direct routing walkthrough

The author directly read the complete Analyze entry and `fixture.py` implementation, caller and assertions, and ran its four baseline checks on Python 3.14.7. This is an in-session source-informed walkthrough, not an independent agent trial or an automatic router test. The synthetic scenarios below are separate bounded analysis questions against that same inspected source; no requested feature was implemented.

Fixture source SHA-256: `3799956a0532d58a7b1962bdb1de8ede0fcd826fc02d07bf1454775912e777f7`.

| Supplied bounded question | Observed author conclusion and meaningful checks |
| --- | --- |
| Clear behavior: add a trailing newline only for nonempty authorized exports | Recommend TDD at existing `export_rows` seam; reuse permission/empty assertions and add nonempty/empty newline checks. Existing owner and caller are suitable; no new formatter framework. |
| Uncertain feasibility: can a remote sink stream this export under a strict memory limit? | Current join/string-return implementation does not establish streaming feasibility. Inspect versioned sink API through research if needed, then recommend a bounded prototype measuring the actual path. Missing sink/environment facts block production readiness, not the recommendation. Prototype → production method only after inspected findings; no performance claim from code reading. |
| Legacy change: alter normalization without breaking intended callers | `legacy_label` strips and uppercases; only one assertion exists and no caller intent is established. Recommend characterize then TDD for agreed new behavior; current uppercase is observed, not automatically required. Unknown intent and non-string/whitespace edges need disposition. |
| Cross-component acceptance: export/download workflow must retain MIME/body and deny unauthorized users | Recommend acceptance-first for observable `download` results and denial through `export_rows`; reuse existing tests for adequate boundaries, add new examples only for agreed changes/gaps. Per-component passes alone do not prove a changed workflow. |
| Straightforward change: rename help heading to “Saved records” | Recommend build-and-check: inspect the heading's consumer, immediately validate expected text and documentation consistency. No domain decision or unit-test quota needed; absent consumer is a recorded check gap, not invented coverage. |

All five returns remain recommendations for the lead, not questions asking the maintainer to choose a technique. Existing access checks are retained. No changed meaning or enduring architectural decision was identified, so no domain-modeling call or ADR/glossary write occurred. Local fixture contents answer ordinary code questions without a research invocation; the unknown remote sink remains a gap rather than a fabricated fact. Standalone output stops at the brief, with no product writes, tickets or PR from the analyzed fixture.

## Freshness, compatibility and old-route inspection

Ran `python3 -B analyze/scripts/check-fixture.py`: six tests passed. Catalog entries live outside the synthetic target; all five semantic capability stubs can be inspected without installing methods. Matching service/caller/check digests remain reusable. A dirty caller changes only the consumer-label support set, retaining service findings. A missing Prototype entry preserves the recommendation and unavailable execution state. A same-name TDD stub lacking the required contract is incompatible. Inspection preserves all target bytes.

These are deterministic contract fixtures and authored support dependencies, not evidence that an agent autonomously invalidates/selects correctly. No actual runtime catalog was populated. Real companion compatibility still requires complete entry/reference inspection; the fixtures cannot certify an installed package.

Direct adapter review: Work On's entry still selects its shipped technical-readiness path, now resolves Analyze by catalog/approved source, sends the shared envelope and inspects the returned brief. Current complete evidence bypasses a needless new run. Missing Analyze blocks only needed analysis; missing method blocks execution, not a supported brief. The lead retains method choice, build gates and optional ticketing/direct-build continuation within the active delivery request. Standalone Analyze has no such continuation. No full Work On trial was launched; old historical execution records remain untouched.

## Static and isolated-package results

- Analyze frontmatter, procedure bounds, internal links/anchors and Python 3.9 syntax compatibility passed at source and in a non-sibling isolated copy: four Markdown links each; six copied-package fixture tests passed.
- Work On frontmatter, bounds and 110 relative links/anchors passed at source and isolated copy. Root README/changelog: 24 relative links passed. Evidence contains no relative links to resolve.
- Node/Marked rendered 11 changed Markdown files containing ten tables. Inspected the rendered Analyze entry and integrated Markdown/diff; this is structural/rendered-HTML review, not browser visual inspection.
- `python3 -B docs/validation/delivery-coverage/check_packages.py` completed with exit 0: five source/isolated packages checked, 11 snapshot tests passed, and 22 tracker/package tests completed with two standalone-companion skips (20 passed). Repository documentation: 53 relative links/anchors passed. These are existing checks, not new target tests or agent trials.
- `git diff --check` and `git diff --cached --check` passed. Direct integrated scope/authority review found no private/local-path/generated-artifact leakage, duplicate technical-analysis body or changed installed copies. Per-package notices match the reused source.

## Acceptance mapping

| #48 reference | #60 evidence |
| --- | --- |
| AC1 | Complete independent Analyze entry, standalone stop, isolated package checks |
| AC3 | Recommendations with lead method choice; no routine maintainer questionnaire |
| AC4 | Deciding-input reuse/targeted refresh contract and current/dirty-caller fixtures |
| AC6 | All five capabilities and composition cues; fixture availability separate from real installation |
| AC8 | Source-gap research and actual domain-work gates; direct local evidence reuse |
| AC15 | Commands/results, direct walkthrough and explicit fixture/trial limitations |

## Documentation and limits

Updated Analyze entry/overview/notices/validation/fixtures; Work On entry/overview/contracts/technical-readiness adapter and route validation; root index and one Unreleased Added entry. CONTEXT, ADRs and accepted design remain unchanged: existing meanings and approved extraction boundaries suffice. No installed migration material (#69/#74) changes. The reused Work On notice is Nicola Mustone MIT; no external body/template was newly imported.

Target test baseline: zero tests in the new Analyze package/evidence location; added six contract tests and four synthetic-source baseline tests, zero existing tests deleted. Historical validation cases are replaced by an adapter-validation pointer while their original repository execution records stay intact. No CI configuration changes; repository has no CI workflow, so timing impact is unmeasured/inapplicable. Analysis test success is not delivery acceptance.

Independent Standards/Spec review and installed/cross-runtime/composed trials were not run; delegation was not authorized. No live model, network source experiment, installation, tracker mutation, service lifecycle or consumer product implementation was performed. Static/package results are recorded below after execution; the PR pins the delivered revision. The issue remains open until accepted and merged under project policy.
