# Domain Modeling

Maintain a project's domain vocabulary, context maps, and selective architectural decision records. Use it directly or through a discovery, setup, or delivery workflow.

```text
/domain-modeling
```

The skill reuses existing definitions and decisions, resolves consequential ambiguity with concrete scenarios, and preserves historical rationale. It supports mutation-free planning and approved edits without repeating a caller's interview. Project operating preferences remain in their own documents. Confirmed glossary/context-map updates use existing task/project authorization; ADR creation or change, including drafts, needs explicit agreement and permission. Record maintenance is part of the current work, not optional session storage. Complete plans/findings may remain in conversation without a durable report or downstream invocation.

## Install and requirements

```sh
npx skills add SirDarcanos/agentskills --skill domain-modeling
```

Requires established project guidance or a meaningful equivalent and an agent with file-reading/editing capabilities. Check the agreement once per context; missing/conflicting common guidance produces a specific prerequisite and setup/reconciliation recommendation, never automatic setup or empty records. No installed setup package, GitHub login, particular SDK, subagent runtime, or model service is required. Callers discover the skill by name, read its entry point and applicable references, and follow the [handoff contract](references/handoff.md).

If another package with this name is installed, inspect which one the runtime resolves. This maintained package's contract includes plan-only and approved handoffs; a same-named installation is not proof of compatibility. Replacement or installation requires the user's approval.

## Package

- [SKILL.md](SKILL.md): scope, authority, workflow, and completion checks.
- [Vocabulary](references/vocabulary.md): meanings, relationships, and context maps.
- [Decision records](references/decisions.md): qualification, creation, and supersession.
- [Validation](references/validation.md): package checks and behavioral scenarios.

This package extracts the repository's original setup guidance and adds a reusable specialist contract. No text or templates were imported from the separately installed third-party domain-modeling package; its local files supplied no license to import. This is not a repackaging of that skill.
