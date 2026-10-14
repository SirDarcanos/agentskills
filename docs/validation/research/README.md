# Research execution evidence — #54

Direct lead execution in Pi on macOS, 2026-10-14, from `main` revision `dd67ea3`, branch `feat/evidence-backed-research`. Python 3.14.7 and Node v24.21.0 were available. This record covers agent source inspection and local package checks, not independent review, installed-runtime discovery, external API behavior or a background-agent trial.

## Agreement and authority

[#54](https://github.com/SirDarcanos/agentskills/issues/54) consumes the accepted design merged in PR #75 and [#48](https://github.com/SirDarcanos/agentskills/issues/48), AC1/AC4/AC8/AC14/AC15. Read-only native blocker inspection returned #50, closed; the design itself records acceptance and integration, not merely issue closure. Scope permits local package/docs changes and safe checks. No delegation or model-service permission is supplied; the unavailable-delegation route was exercised with zero launches. Sources below are original synthetic fixtures, not imported external material.

## Executed direct research

After authoring the package, the lead read its complete entry point, delegation and validation references, then used `read` on all three fixture sources. The bounded question was: **For Synthetic Retry Client 2.0, what attempt limit and runtime are supported by the selected sources?** Direct run D1 used only release configuration and reference documentation; conflict run D2 additionally included the release note. Retention is this approved validation record; no product implementation or tracker publication belongs to either research run.

Source identities, inspected 2026-10-14:

| Source | Version/date and locator | SHA-256 |
| --- | --- | --- |
| [release configuration](fixtures/release.json) | Version 2.0; publication date unknown; `maxAttempts`, `supportedRuntime` | `8249923b612f394fb21fc1e1f74dd3e05624db5e02a3e2fd358cf40af07d4019` |
| [reference](fixtures/reference.md) | `reference-2.0-a`, published 2026-10-01; Retry behavior / Runtime | `dfb2875edda3aa01596cf50e68597114094e9d06e9f331cda503954f3a4f7117` |
| [conflicting release note](fixtures/conflicting-note.md) | `release-2.0-b`, published 2026-10-02; Retry behavior | `a9917cdfe79499dd216d7a59ec7fc163509634bd4ddb08d2515f5dc849564af1` |

### D1 — complete within selected source scope

- **C1, configuration fact:** `maxAttempts` is 3 in release configuration 2.0.
- **C2, documented fact:** reference 2.0 says “three total attempts, including the initial request.” Together with C1 this supports a three-attempt configured/documented limit, not an observed runtime result.
- **C3, configuration/documented fact:** `supportedRuntime` is `20`; the reference Runtime section independently states version 20.
- **C4, interpretation:** these two selected sources agree for this question. No real client execution, latency or production suitability was checked; recommendation not requested.

The lead returned findings in the conversation and stopped at research. No application files, tickets, services or installations were changed. Delegation was optional and ungranted; direct execution was equivalent for these local sources, with zero workers and no worker/repair ledger allocation. The completed result is reusable only for this selected scope and these identities.

### D2 — blocked attempt-limit conclusion; useful findings retained

The lead inspected the release note as an additional same-version primary source. It says “five total attempts,” conflicting with C1/C2. Its later publication date supplies no precedence or reconciliation. Therefore the assertion that all selected authoritative sources agree on the 2.0 limit is blocked. C3 remains supported. Smallest next action: obtain a corrected first-party reference or authorized behavior check that resolves intended versus actual limits; no implementation is implied.

An assertion “the client uses a 100 ms backoff,” citing the reference, was checked against Retry behavior. The source describes immediate retries, not 100 ms. That assertion is unsupported; it was not promoted into the findings. This is source inspection, not a test of real retry timing.

### R1 — current reuse

A second SHA-256 comparison of all three original fixtures returned the same identities. The lead reused C1–C3 for their original scope and retained D2's conflict; no additional source search or worker/model call was made. Locators/support had already been inspected in this context. Current contradictory evidence prevents reusing D1's agreement conclusion for D2's broader source set.

### S1 — stale deciding configuration

A Python temporary-copy exercise copied all three fixtures outside the repository and changed only `maxAttempts` from 3 to 4. It printed original-versus-copy digest comparisons and an assertion confirming unchanged version/runtime. The lead then used `read` to inspect the changed copy:

- New configuration digest: `d355bc14e53dd3a5de06ea20f91ed09965d5de35f33600e97bf61bbb734df3d5`; `maxAttempts` is 4.
- Both Markdown source digests stayed unchanged; `supportedRuntime` is still `20`.
- C1 is stale for that copy; its refreshed configuration fact is 4. C2 remains a valid report of what the unchanged reference documents, but no longer establishes configuration agreement. C3 is reused. The old D1 findings remain valid for the original fixture scope.
- The changed copy's intended attempt-limit conclusion is blocked by conflicting source evidence. Runtime behavior remains unrun. No corrective implementation or blanket restart was made.

The original fixture digests were compared again and stayed unchanged. The temporary mutation was not committed. These are actual tool-assisted lead exercises, not automated judgment tests or independent agent evidence.

## Package validation and limitations

Package validation follows [the shipped guidance](../../../research/references/validation.md). The package and repository evidence have different homes: scenarios ship with Research; executed results live here. Executed local checks used Node with the already-installed Marked and YAML libraries (no dependency installation): parsed Research frontmatter in both original and isolated copies; rendered 10 Markdown files; resolved 28 relative links; copied the complete package into a temporary non-sibling directory and rendered its five Markdown files with all six internal relative links confined to that copy. All passed. The lead inspected the rendered entry-point HTML for heading/list/link structure; this was not browser visual inspection. Fixture JSON parsing/assertions passed. `git diff --check` passed; a scoped scan found no workstation paths, private-key blocks or token-like credentials in new package/evidence files. These are local static/executable checks, not automated tests of agent judgment. Historical `research/clef-feasibility.md` SHA-256 matches `main`: `5ffcacaae7df7ceba34b632786628a706441e6ebd4913dc78afc1a79c038f0f4`.

No authorized worker, independent review, real service, model call, installed-copy replacement, CLI installation or cross-runtime discovery was run. Access-denial, exhausted-bound, background-only and worker-failure cases remain authored scenarios rather than executed evidence. No shared build/test command or CI exists. Automated application tests added/removed/updated: 0/0/0 relative to `dd67ea3`; the fixture runs above are direct agent exercises, not a counted automated suite. No CI timing claim is made.

Documentation impact: new package entry/README/references, root skill listing and Unreleased changelog updated. Existing feasibility note preserved byte-for-byte. CONTEXT, ADRs, accepted design and operating/model policy remain unchanged because existing meanings, ownership and permissions suffice; historical inventories remain historical. Instructions are original, with no external skill/template import. Merge adds source only; separately installed same-name copies need an approved update. Reverting source can remove this addition but cannot undo separately performed consumer installations.
