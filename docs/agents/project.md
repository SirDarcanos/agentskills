# Project context

## Purpose and maintenance

Agent Skills is a public, MIT-licensed collection of reusable coding-agent skills. The maintainer uses these skills in personal workflows and shares them for others to install or adapt. Contributors and coding agents consume the repository's instructions; each skill documents its own runtime and tool requirements.

This is a single-maintainer repository. The maintainer owns product scope, consequential trade-offs, and acceptance. Agents handle routine engineering within approved scope and explain consequential choices in practical terms. There are no teams, corporate approval chains, or assumed dedicated operations staff.

Keep maintenance proportionate to a collection of independently installable skills, supporting references, and selected scripts. New infrastructure, shared tooling, or abstractions need a current requirement rather than hypothetical organizational growth. No usage targets, service-level commitments, or operating budget have been established.

## Risks and constraints

- Instructions can cause agents to modify a consumer's files, repositories, settings, or credentials. Invocation and approval boundaries are part of observable behavior, not just prose quality.
- Some skills use local models or hosted services. Disclosure, spending, installation, and service-management permissions must remain explicit; ordinary validation must work without live inference.
- Public examples and retained artifacts must exclude credentials, private project material, personal profiles, and workstation-specific paths.
- A skill copied on its own must retain its shipped references and follow the [source-independence decision](../adr/0004-skill-package-source-independence.md). Companion requirements must explain discovery, compatibility, and unavailable-helper behavior rather than assume a particular installation tree.
- Maintainer copyright notices name Nicola Mustone, not the GitHub handle. Imported or directly adapted material requires license and attribution review; packages substantially inspired by Matt Pocock's skills also retain his MIT notice and source credit. Keep upstream notices with only the affected independently installable packages, not every skill. Preserve existing third-party notices and runtime assumptions unless the change deliberately updates those assumptions.
- Static checks and synthetic benchmarks have limited scope. Report what was executed and what remains uncertain; model agreement is not independent proof of correctness.

## Policy homes

[Workflow](workflow.md) owns authority, delivery, verification, release policy, and documentation maintenance. [Tracker guidance](issue-tracker.md) owns GitHub relationships and completion semantics; [label guidance](triage-labels.md) owns the label vocabulary. [CONTEXT.md](../../CONTEXT.md) contains domain meanings, not operating preferences.
