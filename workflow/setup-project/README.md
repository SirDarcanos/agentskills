# Setup Project

One explicit command to establish a project's operating context, agent instructions, domain vocabulary, and approved repository workflow.

```text
/setup-project
```

The agent inspects first, asks only missing consequential questions, presents one approval plan, applies it, and verifies the result. It adapts to project risk, resources, and collaboration preferences independently: neither solo nor corporate work implies a fixed architecture.

## Output

The [documentation contract](references/documentation-contract.md) defines default homes under `docs/agents/`, a concise agent entry point, a domain glossary when useful, and selective ADRs. Existing valid layouts and authored content are preserved. Reruns propose only necessary changes.

Setup proposes none or exact bounded model permissions using the [model-use agreement](references/model-use.md). After approval it writes or reconciles one policy home and entry-point pointers, preserving existing authority and provenance. Shared request/retry/spending limits apply across delegates and resume; disclosure, lifecycle and fallback stay explicit. Setup itself makes zero model/service/credential/installation operations. Assessment packages must separately support the selected invocation contract.

Setup inspects the project's actual versioning and changelog convention, preserves existing release history/automation, and proposes an evidence-backed changelog when one is missing.

For GitHub, setup composes the maintained `github-repo-setup` skill and audits the full label vocabulary—not just a fixed starter set. It adds a `spec` role, applicable release-impact roles (`patch`, `minor`, `major` for SemVer), and other useful project labels. It proposes unused default/custom labels for approved editing, migration, or removal after checking historical usage and automation. Tracker guidance requires actual native sub-issues and blocker relationships, not just issue-body references. Local-only setup is supported without GitHub authentication.

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

Delivery workflows may discover this package and read its entry point plus [tracker integration](references/issue-tracker.md) without invoking setup. The native-graph procedure is the authoritative reconciliation algorithm; its optional helper handles only additive blockers in one github.com repository, not parentage, labels or approval. Callers record the source/revision and verify semantic compatibility. Actual operations remain subject to the target project's policy and exact approval; reading the library grants no setup or configuration authority.

## Files and validation

- [SKILL.md](SKILL.md): orchestrator and completion gates.
- [Documentation contract](references/documentation-contract.md): authoritative output and upkeep policy.
- [Discovery](references/discovery.md) and [reconciliation](references/reconciliation.md): conditional procedures.
- [Model-use agreement](references/model-use.md): policy discovery, exact approval, document application and unchanged rerun.
- [Domain handoff](references/domain-records.md): setup integration with the domain-modeling companion.
- [Tracker integration](references/issue-tracker.md): label audit/cleanup, spec classification, and native relationships.
- [Release setup](references/releases.md): versioning detection, changelog creation/maintenance, and release authority.
- [Validation](references/validation.md): offline commands, scenario matrix, and limits.
- [Dependency helper](scripts/dependencies.py): read-only planning or explicitly applied blocker edges, never parentage or label mutations.

These are instructions for an agent, not a fully automated project generator. Offline tests establish helper behavior and package integrity, not end-to-end agent compliance.
