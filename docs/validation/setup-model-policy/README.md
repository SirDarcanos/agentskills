# Setup model-policy validation — #51

Direct evidence for [#51](https://github.com/SirDarcanos/agentskills/issues/51), under #48 AC9/AC11/AC14/AC15 and the [accepted design](../../design/composable-delivery.md#model-use-permission-contract). Input base: `a95a9588ff86304f2390cae8d87df4addf7da1d1`; branch `feat/setup-model-policy`, target `main`. PR/commit history identifies the delivered revision. These are focused policy-document walkthroughs by the implementing agent, not independent review or a full setup/GitHub workflow trial.

## Executed direct fixtures

The agent created seven disposable local targets, read their entry points and existing policies, selected the necessary policy delta using the shipped [procedure](../../../setup-project/references/model-use.md), applied three synthetic-approved document plans with file tools, and read back actual outputs. Synthetic approvals N1/L1/H1 exist only for these disposable targets, never this repository or a real model call. [Input/output snapshots and decisions](fixtures.json) retain the exact text rather than authored expected results presented as execution.

| Fixture | Actual outcome |
| --- | --- |
| None | Wrote zero requests/retries/spend, no startup/substitution, ordinary-engineering fallback, rationale/provenance and an AGENTS pointer. |
| Local-only | Wrote exact Clef/Ollama loopback route, synthetic-only disclosure, shared work-unit attempt/correction/spend bounds, reuse-only lifecycle, no named alternative and root accounting. Preserved explicit-only package gate. |
| Bounded hosted | Wrote exact Jev alias/HTTPS endpoint, public-safe-only disclosure, whole-spec USD/request bounds shared across workers, safe reservation/unknown-charge rules, no substitution or lifecycle effects. No inference or live endpoint validation. |
| Existing equivalent | Preserved `policy.md`, custom retention text, E1 approval and already-valid entry pointer byte-for-byte; no competing default policy. |
| Missing facts | Blocked unresolved endpoint/disclosure/shared limits/approval; selected no target writes. |
| Conflicting facts | Existing none versus unattributed unlimited hosted instruction remained unresolved; no expansion or target writes, owner clarification required. |
| Proposal-only | Recommended none with approval pending; target bytes remained unchanged. |

Read-only reruns of none/local/hosted/existing policy outputs selected no further delta. Python assertions checked the actual target bytes against initial snapshots: all four no-write targets unchanged, sentinel/custom text preserved, new entry links resolved, rationale/provenance present. Tool-action inspection found zero model requests, service operations, credential access, downloads or installations. This is observed direct behavior, not a sandbox-enforced guarantee. The fixture setup and evidence recorder themselves wrote only local synthetic fixture/evidence files.

Reproduce the behavioral check by materializing each `before` mapping from `fixtures.json` in a fresh temporary directory, giving a direct agent the current setup entry and reference with the recorded synthetic decision/approval scope, then comparing its actual selected writes and resulting bytes to the recorded delta. Keep blocked/proposal targets unchanged, inspect tool actions, and rerun without refreshed approval or budgets. The JSON is an evidence snapshot, not a policy parser or automated agent runner. The three applied plans also created workflow pointers assigning lead reservation and assessment pre-send checks; those files were read back and their links verified. Full setup discovery/interview and unrelated domain/tracker routes were outside these focused plans.

## Package and document checks

Commands from repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s setup-project/tests -p 'test_*.py'
python3 setup-project/scripts/dependencies.py --help
git diff --check
```

Actual results: 22 tests passed with no skips; dependency helper help and `git diff --check` passed. All seven retained snapshots matched the actual temporary targets and exact selected deltas, with entry/workflow links resolving. The repository has no opt-in policy and `CLAUDE.md` remains the existing symlink.

An additional package test copies setup into a temporary non-sibling directory and verifies frontmatter and all shipped relative links. It does not invoke companions. Existing package checks cover the present domain/GitHub companions, while the dependency suite exercises its offline mock transports; the dependency helper is unchanged. Test-count baseline is the input base: one test added, none removed or updated; no model-enforcement unit tests are claimed.

Markdown was rendered using the already-installed Marked module and structurally inspected, including the model-policy field table and required conditional links. The initial repository-local module lookup failed; the available installed module was used without installation. Direct diff inspection checked policy approval versus use, explicit-only staging, shared budgets, existing authority, source-repository disabled calls, package portability, preserved CLAUDE symlink and absence of sensitive/local-path material. No independent reviewers were launched.

## Documentation and limits

Updated setup entry, discovery, documentation mapping, reconciliation, validation, package README, root listing/changelog, and source-repository AGENTS/workflow authority. The new reference owns the setup procedure; target permission values have one approved home. No `docs/agents/model-use.md` is created for this repository: a separate maintainer policy decision is still required, and calls remain disabled. Existing domain meanings, ADR/design history, actual assessment runtime procedures, installations and tracker graph remain unchanged; no glossary or ADR update is needed.

Assessment enforcement, mock pre-send/retry/lifecycle behavior and composed delivery budget trials belong to #52/#53/#67/#68/#73 and were not run here. Also unrun: full standalone setup interview, cross-runtime trials, companion discovery invocation, live inference, live service/API/credential checks and GitHub configuration mutations. The package needs ordinary file/shell tools, with Python 3.9+ for offline checks; this run used Python 3.14.7 on macOS/Pi. No CI configuration changed and CI duration was not measured. Merge publishes source only, not an installation, model opt-in, deployment or release; reverting restores source guidance, not consumer policies already authored elsewhere.
