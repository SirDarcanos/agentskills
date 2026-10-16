# Writing for agents

Write skills, instruction files and referenced agent-facing guides with clear actions, conditional pointers and checkable completion. [SKILL.md](SKILL.md) preserves established facts, meaning and permissions while reducing duplication.

## Use and requirements

Ask your agent to write or revise a specific agent-facing document, or to review it without editing. For example:

```text
Use writing-for-agents to revise this skill's routing description and references.
Review AGENTS.md for duplicated instructions; preserve all approval gates.
Rewrite the referenced testing guide as ordered actions with checkable completion.
```

Requires file inspection and, for edits, scoped writing tools. Validation uses the target environment's existing checks where available; unavailable rendering, parsers or runtime checks are reported. There is no required companion, model service or special runtime. Optional companions must have verified `SirDarcanos/agentskills` provenance and be able to operate within that same boundary; otherwise the agent writes directly. Installed names alone are insufficient.

For structure and routing choices read [structure guidance](references/structure.md). For finish checks and regression cases read [validation](references/validation.md).

## Project context

Project work requires the target's existing working agreement or meaningful equivalent; missing or conflicting guidance is reported for explicit reconciliation, not replaced by this skill. Non-project supplied-text work remains usable without setup. No delivery workflow is required for ordinary writing; results need no automatic handoff artifact.

## Install

After approving installation, copy this complete directory, including its [license](LICENSE) and references, into your agent's skill discovery location, or use:

```sh
npx skills add SirDarcanos/agentskills --skill writing-for-agents
```

The installation command has not been exercised in this delivery. Repository delivery neither replaces the existing reference installation nor authorizes its retirement. Invocation behavior depends on the consuming agent; static metadata checks do not certify every runtime.

## Source credit

Substantially inspired by Matt Pocock's `writing-for-agents` reference skill: conditional context pointers, progressive disclosure, co-location, completion criteria and one authoritative home. This package adds an ordered writing workflow, explicit fidelity and companion boundaries, and an environment-aware validation gate. It does not carry forward runtime-independent claims about invocation metadata or guaranteed model behavior.

Upstream project: [Matt Pocock's skills](https://github.com/mattpocock/skills), distributed under the [MIT license](https://github.com/mattpocock/skills/blob/main/LICENSE). The inspected reference copy did not include a source revision; these links identify the upstream project, not an asserted exact source revision. The package [LICENSE](LICENSE) retains Matt Pocock's notice alongside Nicola Mustone's.
