# Hosted Jev authorization validation (#53)

Scope: [#53](https://github.com/SirDarcanos/agentskills/issues/53), under [#48](https://github.com/SirDarcanos/agentskills/issues/48) AC10, AC11 and AC15 and the [accepted design](../../design/composable-delivery.md). These are direct offline procedure/contract simulations and document checks, not real agent walkthroughs, independent review, live inference or installed migration.

## Input and delivered behavior

Base: `bcc928c` (`main`, merged #81). Preflight found a clean tree on main, fetched origin, inspected branches/PRs and created `feat/hosted-jev-policy` from origin/main, targeting main with no existing PR. Read the actual #53 agreement, #48, accepted #50 design/ADR pointers and inventory/validation map, project/workflow/tracker/label guidance, CONTEXT and full package entry/references. Native read-only inspection found parent #48, blocker #51 and downstream #67; #51 is closed and its PR #76 is merged. Accepted #50 PR #75 and #51 merge commits are ancestors of the base. No relationship or label change was needed.

Discovery, body gate, hosted API guidance, fallback, completion and validation now support exact approved-policy handoffs alongside explicit user requests. The new shipped authorization reference owns policy-fit checks, disclosure and shared spending/attempt reservations; the target's policy remains the sole home for permission values. Explicit use still respects project prohibitions; generated commands are not user consent. Named TypeSafe transport stays fixed; alternative packages require separate lead discovery and authorization. Shared failed/unknown use persists across retry, correction, handoff and resume. Missing pricing without a safe bound blocks a paid send.

This repository still has no separately approved model policy. No credential value was accessed, authenticated API request made, model called, service started, package installed, or installed skill changed.

## Executable checks

The baseline package contained five Markdown files and no automated package tests. The new suite has **36 unittest test methods added, zero removed or updated**; subtests are cases inside those methods, not additional counted tests. The fixture is a test-only rendition of instructions, not a production client or policy parser. Its resolved permission dictionaries are synthetic facts, not a target policy format.

Commands:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s ask-jev/tests -p 'test_*.py' -v
# From a temporary complete package copy without siblings:
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Initial suite: 33 methods passed before adding explicit alias/pin and missing/zero correction-limit checks. Final 36-method runs both passed: source 0.039 seconds; isolated copy 0.042 seconds (local elapsed unittest timing, not CI measurements). Python runtime: 3.14.7. The isolated run copies the complete package into a fresh non-sibling directory and uses only the standard library. Temporary copies and synthetic JSON are removed by their owning temporary-directory contexts.

Coverage includes:

- Exact approved hosted use without confirmation, explicit use without autonomous permission, version pin and moving-alias permission, and valid insufficient-data attribution.
- Zero mocked credential/transport effects for absent/none/draft/conflicting/expired/denied authority, generated consent, incompatible identity/purpose, prohibited private disclosure, unsuitable questions and exhausted/reserved/unknown call or spending limits.
- Missing credentials; failure/malformed response; ambiguous timeout and conservative unknown charges; redirect rejection; only 429/529 retries within shared and package ceilings, bounded Retry-After and immediate permission rechecks.
- Parent/worker/resume shared allowances, outstanding worker reservations, one correction across resume, stricter policy/root correction limits, six-attempt package cap and four-question batch accounting.
- Direct fallback allowed/denied and explicit offer-and-wait; named alternatives never changing Jev transport; whole-batch validation and no partial malformed interpretation.
- Choice, Noul and Score response consistency, model/IDs/types/usage, invalid probabilities/confidence/legend and expected weighted score.
- Frontmatter, internal links, non-sibling package portability, documented JSON syntax-check execution with synthetic input, and static named transport/timeout/redirect guidance.

## Document and contract checks

Parsed frontmatter with an existing YAML library: name/description present, obsolete command-only flag absent. Rendered eight Markdown documents with an existing Marked library (entry, package README, four references including unchanged judgment design, root README and changelog): 65 headings and four tables. Inspected the Markdown and changed procedure branches directly; this is structural rendering, not browser visual inspection. Package tests verify relative targets remain inside the copied package; a separate direct check resolved all 12 relative Markdown targets across the six package documents and this evidence record. No helper installation was performed.

Read current public TypeSafe [API](https://docs.typesafe.ai/api.md), [models](https://docs.typesafe.ai/models.md), [index](https://docs.typesafe.ai/llms.txt), [Choice](https://docs.typesafe.ai/primitives/choice.md), [Score](https://docs.typesafe.ai/primitives/score.md) and [Noul](https://docs.typesafe.ai/primitives/noul.md) guidance without credentials or project payloads. At inspection, `jev-latest` resolves to `jev-1.13.0`; pricing is input-only $0.042/Mtok with output free, and context limits are 64k total / 32k state plus longest question. Existing API contract and primitive checks remain consistent. These observations establish neither future pricing nor permission: the shipped procedure rechecks current contracts, pricing, exact model and safe request bound at use time. No upstream source bodies were imported.

Direct integrated diff inspection covers scope, disclosure, fixed attribution, no repeated confirmation inside valid bounds, preserved explicit routing, shared accounting and doc consistency. `git diff --check` passed. No payloads, keys, machine-specific source paths, generated files or private records were included in the reviewed changes; `CLAUDE.md` remains a symlink to `AGENTS.md`. Final staged check and reviewed revision are recorded in the PR.

## Documentation impact and limits

Updated owners: Ask Jev entry/README, authorization, hosted API and testing references, root skill listing and one Unreleased Changed entry. Judgment-design guidance is unchanged. Project/workflow/AGENTS already describe the approved mechanism with calls disabled here, so no policy opt-in or operating delta is needed. CONTEXT and ADR/design history are unchanged: no new term, architecture decision or ownership boundary is introduced. No release, deployment, CI or installation automation exists to run; CI jobs/timing changes are zero/not measured. This is compatible functionality (minor).

Not run: live billing/inference, real credentials, production TLS/proxy/redirect/timeout enforcement, real shared-budget concurrency, actual agent confirmation behavior, independent Standards/Spec review, installed discovery/migration or composed delivery acceptance. The mocked procedure and static strings cannot prove those runtime properties. Actual assessment clients still need their own offline transport validation; composed acceptance remains downstream. No acceptance or merge claim follows from these tests. Keep #53 open until accepted and merged; opening its PR grants no merge/release/migration authority.

Source reversion restores the previous command-only package behavior but cannot undo already incurred hosted charges/disclosure or change installed copies and policy/ledger state. Merging changes source only; consuming the new package still requires explicit invocation or a separately approved policy.
