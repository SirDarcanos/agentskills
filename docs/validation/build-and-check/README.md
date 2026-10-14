# Build and Check execution evidence

Repository-local evidence for [#59](https://github.com/SirDarcanos/agentskills/issues/59), under the accepted [composable design](../../design/composable-delivery.md). This is direct inspection and offline fixture execution, not independent review or an installed/composed agent trial.

## Scope and prerequisite

Base: `3fe4df0ffb9b314976b6e78d0832d9308f3f027b`. Read native #59 blocked-by: #50 only. #50 is closed and accepted design PR #75 is merged at `a95a9588ff86304f2390cae8d87df4addf7da1d1`, present in this base. No labels, native relationships, installed copies or model permissions changed.

Added the original Build and Check method, package-local validation and fixture; replaced Work On's implementation-first loop with semantic companion discovery and inspected local return. Work On retains preflight, scope, repair, verification and acceptance ownership; this does not perform #67's single-change cutover.

## Executed checks

Environment: macOS, Python 3.14.7, Git 2.54.0. Commands executed in the scoped dirty feature branch, then the complete packages copied to disposable isolated directories without sibling skills.

- Entry increment: Python assertions inspected frontmatter, numbered steps, ordinary invocation, immediate-check gate and absence of test quotas before further implementation.
- `python3 build-and-check/scripts/check-fixture.py`: four unittest cases passed, six child check runs. The unchanged existing harness passed before/after a code refactor. Documentation edits passed text/link checks before a JSON formatting increment passed parser/value checks. Zero new target tests were required for these increments; four repository fixture tests were added, none removed or updated relative to the base.
- Failure case: whitespace conversion regression reached a behavioral `AssertionError`, exit 1. The scripted gate withheld `dependent.txt`; restoration/recheck exited 0 before that dependent artifact was created. This demonstrates the synthetic gate and sensitivity, not autonomous agent compliance.
- Unavailable-consumer case: blocked/unverified deterministic reporting oracle, not a live missing-tool experiment.
- Reused `docs/validation/delivery-coverage/check_packages.py` functions through an inline Python import: `check_package` passed frontmatter, procedure bounds, Markdown links/anchors and Python 3.9 grammar for Build and Check (4 links) and Work On (111 links), both at source and in isolated copies. The isolated Build and Check fixture also passed all four cases. Build and Check's license matched the repository MIT notice byte-for-byte.
- `check_links` passed 23 relative links/anchors across root README/changelog. `git diff --check` passed. Directly inspected integrated diff and new package contents for scope, private material, portability, generated artifacts and notices.

Fixture scratch is synthetic and removed through its owned temporary-directory lifecycle. No network, external assessment, tool install, service action or installed-skill mutation was used for validation. GitHub reads and PR publication are delivery operations, not fixture effects.

## Documentation and remaining limits

Updated package entry/README/validation, Work On entry/README/build/capability/validation references, root listing and one Unreleased Added entry. Existing design, inventory, historical evidence and CONTEXT need no updates: ownership/names follow accepted decisions and no domain meaning changes. No CI jobs/checks changed; this repository has no CI workflow, so no CI duration comparison exists.

Authored helper, authority, stale-evidence, policy and recorded-repair cases remain scenarios rather than executed agent trials. Actual runtime discovery, composed method routing, reviewer independence and other runtimes/OS remain unverified. Independent review was not authorized or performed; direct inspection is not a substitute. #59 remains open pending maintainer acceptance and merge. Merge does not install a skill, publish a release or opt into model use; consumers using Work On's implementation-first route must stage both updated packages. A source rollback must restore the caller and method together.
