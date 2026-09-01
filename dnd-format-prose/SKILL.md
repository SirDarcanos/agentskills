---
name: dnd-format-prose
license: CC-BY-4.0
metadata:
  version: 1.0.0
description: Transform supplied prose into D&D-compatible read-aloud narration, boxed text, bestiary lore, or adventure lore. Use when a user explicitly requests D&D prose and whenever the current task itself includes creating or revising prose meant to be read to players. Do not use for rules text, mechanics, character dialogue, or private DM notes alone.
---

# D&D Format Prose

Transform an established passage or prose plan into restrained, table-ready D&D prose. Preserve the source before improving its delivery.

## Invocation

Load this skill when either condition is unambiguous:

- the user asks to rewrite or format prose as D&D narration, boxed text, bestiary lore, or adventure lore;
- the agent's current work includes creating or revising prose intended for a DM to read to players, even when prose formatting is only one part of a larger task.

Also use the DM-lore branch when a transformation must preserve hidden bestiary or adventure information outside the player-facing passage. Operational DM notes alone do not trigger the skill.

Rules text, stat blocks, encounter balance, and character dialogue remain outside this skill. When another active skill owns those parts, preserve its decisions and apply this skill only to the prose layer.

## Modes

Use **voice-only** unless the user requests another mode.

- **Voice-only:** Change diction, rhythm, structure, and emphasis while preserving every referent and fact.
- **Diegetic adaptation:** Replace modern or nonfantasy terms with fantasy analogues while preserving their relationships and implications. Use only when explicitly requested.
- **Lore expansion:** Add names, history, motives, sensory details, or supernatural explanations. Use only when explicitly requested, and keep additions consistent with the supplied setting.

A request can combine diegetic adaptation and lore expansion only when it clearly authorizes both.

## Workflow

1. **Set the contract.** Identify the requested mode, approximate length, and whether the result is player-facing read-aloud prose, DM lore, or mixed content. Treat missing mode and length instructions as voice-only and approximately source length.
2. **Lock the source.** Record the facts, causality, certainty, names, chronology, quantities, mechanics, point of view, and existing direct address. These remain invariant except where the selected mode explicitly permits a change.
3. **Load the branch guidance.** Read [`references/read-aloud.md`](references/read-aloud.md) for player-facing prose. Read [`references/dm-lore.md`](references/dm-lore.md) for bestiary or adventure lore and whenever hidden information must be separated. Read [`references/examples.md`](references/examples.md) when calibrating a mode or resolving mixed input.
4. **Partition mixed input.** Separate player-perceptible description from hidden lore and mechanics. Use **Read Aloud**, **DM Lore**, and **Mechanics** headings only when more than one category is present. Keep mechanics exact.
5. **Transform.** Make the smallest complete rewrite that establishes the appropriate D&D register. Preserve meaningful headings, paragraphs, lists, emphasis, and notation unless spoken delivery or the mixed-content split requires reflowing them.
6. **Run the finish gate.** Verify every check below. Revise until all checks pass.
7. **Return the prose.** Return only the transformed passage unless the user asks for alternatives, notes, or a fidelity report. Omit a heading when the result contains one unambiguous prose type.

## Finish gate

- Facts, causality, certainty, names, chronology, quantities, and mechanics remain intact.
- Voice-only output preserves every source referent; adaptations stay within their authorized mode.
- No lore, sensory detail, player action, reaction, emotion, or conclusion was invented without lore-expansion permission.
- Player-perceptible and DM-only information are separated.
- Direct address and assumed player action appear only when inherited from the source.
- Read-aloud prose works when spoken: sentences have clear breath points, names are manageable, and no clause carries too many details.
- Diction is concrete and setting-appropriate without faux-archaic phrasing, generic ominousness, or ornamental excess.
- Mechanics are mechanically exact and remain prose-independent.
- The result contains no commentary the user did not request.

## References

[`references/sources.md`](references/sources.md) records the official SRD basis, licensing, attribution, and the boundary on source material.
