# D&D Format Prose

An agent skill for transforming established prose into restrained, table-ready D&D narration, boxed text, bestiary lore, and adventure lore.

The skill preserves the source's facts and mechanics, keeps player-facing description separate from DM-only information, and formats read-aloud passages for spoken delivery without directing player actions.

## When to use it

The skill activates when a user asks for D&D prose and whenever an agent's current work includes creating or revising prose intended for a DM to read to players.

Example requests:

```text
Rewrite this room description as D&D boxed text without adding details.
```

```text
Separate this creature description into player-facing narration and DM lore.
```

```text
Adapt this modern security procedure into fantasy archive lore.
```

It does not govern rules text, stat blocks, encounter balance, character dialogue, or operational DM notes unless the task also includes player-facing or sourcebook-style prose.

## Modes

- **Voice-only:** Changes diction, rhythm, structure, and emphasis while preserving all referents and facts. This is the default.
- **Diegetic adaptation:** Replaces modern or nonfantasy concepts with fantasy analogues while preserving their relationships and implications. This requires an explicit request.
- **Lore expansion:** Adds setting details, history, motives, or sensory information. This also requires an explicit request.

## How it works

The skill:

1. identifies the prose type, mode, and requested length;
2. locks facts, causality, certainty, names, chronology, quantities, mechanics, and perspective;
3. separates observable description, hidden lore, and mechanics when necessary;
4. applies the appropriate read-aloud or DM-lore guidance;
5. checks spoken rhythm, information boundaries, fidelity, and D&D register;
6. returns only the transformed prose unless commentary is requested.

Read-aloud prose describes the scene available when the DM chooses to speak it. It does not introduce “you,” assume that characters enter or move, or dictate their attention, emotions, or conclusions. Direct address may remain only when inherited from the source.

## Files

```text
dnd-format-prose/
├── SKILL.md
├── README.md
└── references/
    ├── read-aloud.md
    ├── dm-lore.md
    ├── examples.md
    └── sources.md
```

- [`SKILL.md`](SKILL.md) defines invocation, modes, workflow, and the finish gate.
- [`references/read-aloud.md`](references/read-aloud.md) covers player-facing narration and spoken delivery.
- [`references/dm-lore.md`](references/dm-lore.md) covers bestiary lore, adventure background, and hidden information.
- [`references/examples.md`](references/examples.md) provides original paired transformations for the supported modes.
- [`references/sources.md`](references/sources.md) records the SRD basis, source boundary, and CC BY attribution.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill dnd-format-prose
```

You can also copy the `dnd-format-prose` directory into your agent's skill discovery path.
