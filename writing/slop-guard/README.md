# Slop Guard

An agent skill for reviewing, rewriting, and drafting human-facing prose without flattening the writer's voice.

Slop Guard does not try to determine whether AI wrote a text. It finds editorial problems that often make prose feel generic: unsupported authority, portable claims, repeated structure, synthetic emphasis, mechanical rhythm, inflated diction, and decorative formatting.

## How it works

The skill supports three modes:

- **Audit:** Quotes and classifies findings without rewriting or scoring the draft.
- **Edit:** Makes the minimum effective revision while preserving facts, meaning, uncertainty, terminology, and voice.
- **Draft:** Writes from a supplied purpose, audience, factual basis, and voice instead of reaching for a generic template.

Every mode reviews prose from deep to surface:

1. claims and evidence;
2. purpose and reasoning;
3. structure and repetition;
4. voice and emphasis;
5. rhythm and syntax;
6. diction and formatting.

Recognizable AI-writing patterns are treated as review signals, not automatic violations. Context, repetition, and effect determine whether a phrase or construction needs changing.

## Example requests

```text
Use slop-guard to audit this article. Report findings without rewriting it.
```

```text
Rewrite this announcement to remove generic language, but preserve its facts and informal voice.
```

```text
Draft a project update from these notes. Keep it direct and do not invent missing details.
```

The skill may also activate when a user asks to review or rewrite prose, raises writing-quality concerns, or asks whether text sounds generic or AI-written. A review request produces findings only unless the user also asks for a rewrite.

## What it protects

During revision, the skill treats these as hard boundaries:

- no invented facts, examples, statistics, quotations, or product behavior;
- no silent changes to causality, certainty, scope, or conclusions;
- no polishing away humor, bluntness, hesitation, digressions, or useful rough edges;
- no numerical slop score or claim about AI authorship.

## Scope

Slop Guard is for prose meant to be read by people, including articles, reports, documentation, announcements, marketing copy, and fiction. It does not review source code or visual design.

Fiction receives additional checks for generic interiority, stock physical reactions, decorative atmosphere, borrowed profundity, and other narrative defaults.

## Files

```text
slop-guard/
├── SKILL.md
├── README.md
└── references/
    ├── fiction-patterns.md
    └── pattern-catalog.md
```

- [`SKILL.md`](SKILL.md) defines invocation, modes, workflow, and the finish gate.
- [`references/pattern-catalog.md`](references/pattern-catalog.md) contains the general editorial pattern families.
- [`references/fiction-patterns.md`](references/fiction-patterns.md) is loaded only for fiction and narrative prose.

## Install

From the repository root, install the skill for a supported coding agent:

```bash
npx skills add SirDarcanos/agentskills --skill slop-guard
```

You can also copy the `slop-guard` directory into your agent's skill discovery path.
