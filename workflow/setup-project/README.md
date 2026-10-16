# Setup Project

One explicit command to establish a project's operating context, agent instructions, domain vocabulary, and approved repository workflow.

```text
/setup-project
```

The agent inspects first, then confirms one short step at a time: target and Git; files and permissions; history and safeguards; labels and tracker. It waits for each answer before advancing and asks briefly before applying the agreed steps, then verifies the result. It adapts to project risk, resources, and collaboration preferences independently: neither solo nor corporate work implies a fixed architecture.

## Output

The [documentation contract](references/documentation-contract.md) defines a compact project-owned working agreement and conditional pointers, not an always-read specialist manual or mandatory installed common-contract package. Existing equivalent layouts and authored content are preserved, with context inline or separate as useful. Missing common guidance is a specific prerequisite for dependent project work; ordinary skills recommend explicit reconciliation without starting setup. An unchanged compatible rerun is a no-op. No terms, decisions or tracker means no empty glossary, ADR or tracker artifacts.

New workflow guidance defaults to allowing ordinary skill work, bounded task delegation, independent read-only review and lead-owned repair/recheck/re-review within requested scope, without extra permission prompts once the policy is approved. Standalone review stays report-only unless fixes are requested. Auxiliary assessments such as Jev, Clef and Nimble remain separately gated, as do consequential actions such as spending, installation and destructive changes; existing restrictions remain authoritative.

For unresolved assessment choices or proposed permission changes, setup names installed skills such as Jev, Nimble and Clef, explains their purpose, disclosure and cost/service implications, and asks whether each should be disallowed, explicit-request-only, or automatic within agreed limits where supported. Settled prohibitions remain valid without reinterviewing them; absent policy grants no autonomous calls. It also asks what other actions, tools or services the owner wants to allow, gate or prohibit. The [model-use agreement](references/model-use.md) defines discovery and exact approval; availability never implies permission. After approval it writes or reconciles one policy home and entry-point pointers, preserving existing authority and provenance. Shared request/retry/spending limits apply across delegates and resume; disclosure, lifecycle and fallback stay explicit. Setup itself makes zero model/service/credential/installation operations. Assessment packages must separately support the selected invocation contract.

Setup inspects the project's actual versioning and changelog convention, preserves existing release history/automation, and proposes an evidence-backed changelog when one is missing.

For GitHub, setup composes the maintained `github-repo-setup` skill and audits the full label vocabulary—not just a fixed starter set. It adds a `spec` role, applicable release-impact roles (`patch`, `minor`, `major` for SemVer), and other useful project labels. The labels step explicitly groups kept, renamed/edited, added, consolidated, deleted and unresolved labels after checking historical usage and automation. Retained `good first issue` and `help wanted` labels are proposed as `good-first-issue` and `help-wanted`, with consumer/assignment migrations where needed. Tracker guidance requires actual native sub-issues and blocker relationships, not just issue-body references. Local-only setup is supported without GitHub authentication.

The agreement distinguishes agent-owned engineering from user-selected stages: configured spec/ticket commands select scoped publication without duplicate prose approval, ordinary delivery stops before PR preparation/publication, and session persistence is user-directed. Active ownership, uncertain effects and spent allowances still require safe accounting. Confirmed authorized glossary maintenance remains part of work; ADR changes need explicit agreement/permission and preserved history. Permission changes are approved deltas, never automatic consequences of skill updates.

The conservative bridge preserves live Work On libraries and safeguards while callers migrate. Legacy diagnosis and delivery endpoints are not yet migrated; a conflict with selected stages blocks that route rather than granting automatic tickets/PRs. This setup change does not claim the complete #132 workflow is shipped or update installed copies.

Setup stops at operating guidance and approved repository configuration. It does not implement an application, start delivery, exercise model permission, or authorize deployment, destructive changes or global installations.

## Install and requirements

```sh
npx skills add SirDarcanos/agentskills --skill setup-project
# Required when domain records need assessment or changes:
npx skills add SirDarcanos/agentskills --skill domain-modeling
# Required only for GitHub creation/configuration:
npx skills add SirDarcanos/agentskills --skill github-repo-setup
```

An agent needs file-reading/editing and shell capabilities. The GitHub route needs authenticated `gh` and appropriate repository/organization permissions. Locate companions through the runtime's discovery mechanism; missing or incompatible companions block the affected route rather than triggering automatic installation. A same-named older domain skill must support the maintained handoff contract before setup uses it.

Operating-document and AGENTS authoring guidance ships inside this package. Domain procedures belong to the separately installed `domain-modeling` companion; setup requests a plan first and passes approved edits afterward. A project with no existing domain records or modeling needs can omit that route without the companion. The optional blocker helper and offline tests use Python 3.9+ standard library. No particular agent SDK, model, or subagent runtime is required. Command-only frontmatter is supplemented by an explicit invocation/approval gate for runtimes that do not enforce it.

## Tracker procedure library

Tracker consumers discover this package root through runtime/project metadata and read the complete [native tracker library](references/native-tracker.md) directly, without the setup entry or label audit. It owns discovery/authority, roles/readiness, native graph operations and optional helper limits. Callers record source identity and check compatibility; missing/older incompatible libraries block the affected route without installation. Existing [tracker integration](references/issue-tracker.md#native-github-graph) callers forward to the same owner. Actual operations remain subject to target policy and exact approval; reading the library grants no setup or configuration authority and does not update installed copies.

## Files and validation

- [SKILL.md](SKILL.md): orchestrator and completion gates.
- [Documentation contract](references/documentation-contract.md): authoritative output and upkeep policy.
- [Discovery](references/discovery.md) and [reconciliation](references/reconciliation.md): conditional procedures.
- [Model-use agreement](references/model-use.md): policy discovery, exact approval, document application and unchanged rerun.
- [Domain handoff](references/domain-records.md): setup integration with the domain-modeling companion.
- [Tracker integration](references/issue-tracker.md): setup label audit/cleanup and retained graph forwarding target.
- [Native tracker library](references/native-tracker.md): directly readable role/readiness and native relationship contract.
- [Release setup](references/releases.md): versioning detection, changelog creation/maintenance, and release authority.
- [Validation](references/validation.md): offline commands, scenario matrix, and limits.
- [Dependency helper](scripts/dependencies.py): read-only planning or explicitly applied blocker edges, never parentage or label mutations.

These are instructions for an agent, not a fully automated project generator. Offline tests establish helper behavior and package integrity, not end-to-end agent compliance.
