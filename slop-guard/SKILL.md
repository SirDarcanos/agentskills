---
name: slop-guard
description: Review, rewrite, or draft human-facing prose without generic AI-writing patterns while preserving meaning and voice. Use when the user invokes slop-guard, raises writing-quality concerns, asks to review or rewrite prose, or asks whether text sounds generic or AI-written. For prose only; do not use for code or visual design.
---

# Slop Guard

Treat slop as an editorial failure, not an authorship verdict. A phrase, sentence shape, or formatting habit is evidence only when it weakens the prose or appears as part of a pattern.

## Invocation

Load this skill when the user:

- invokes it by name;
- raises concerns about writing quality;
- asks to review, critique, or assess human-facing prose;
- asks to rewrite, clean up, or sharpen prose;
- asks whether writing sounds generic, formulaic, or AI-generated.

Apply it to prose meant for people, including documentation, reports, articles, announcements, marketing copy, and fiction. Do not apply it to source code or visual design.

Infer whether the user wants an audit, edit, or draft from the request. A review authorizes findings only, not a rewrite. If two modes are plausible and the choice would change the deliverable, ask which one the user wants.

## Choose the mode

- **Audit:** Identify problems without rewriting. Use when the user asks for a review, diagnosis, scan, or opinion.
- **Edit:** Revise supplied prose. Use when the user asks to rewrite, clean up, sharpen, or fix it.
- **Draft:** Write new prose from the user's facts, purpose, audience, and desired voice.

## Workflow

### 1. Establish the writing contract

Read the full draft and any nearby style guide before judging individual lines. Determine:

- what the piece must accomplish;
- who will read it and where;
- what the reader should know, believe, feel, or do afterward;
- which facts, claims, quotations, uncertainty, and terminology must survive;
- which voice signals belong to the writer, such as vocabulary, cadence, bluntness, humor, formality, digressions, or rough edges.

Ask one focused question only when missing information blocks a faithful result. Do not make the user restate facts available in the draft or repository.

**Complete when:** the purpose, audience, factual boundaries, and voice constraints are known well enough to evaluate the prose without guessing.

### 2. Read the applicable patterns

Read [references/pattern-catalog.md](references/pattern-catalog.md) before auditing, editing, or drafting. For fiction or narrative prose, also read [references/fiction-patterns.md](references/fiction-patterns.md).

Treat listed words and constructions as searchlights, not bans. Keep a flagged pattern when it is accurate, natural in context, characteristic of the writer, or the clearest available wording.

**Complete when:** every applicable pattern family has been considered in context, including clusters and repetition rather than isolated matches alone.

### 3. Audit from deep to surface

Review in this order:

1. **Claims and support:** Check factual grounding, attribution, causal claims, comparisons, certainty, and invented specificity.
2. **Purpose and reasoning:** Check whether each section advances the intended outcome and whether conclusions follow from the material.
3. **Structure and repetition:** Find repeated ideas, generic section shapes, false balance, padded setup, and recap endings.
4. **Voice and emphasis:** Find passages that could belong to any writer or subject, tonal mismatches, flattened personality, and instructions telling the reader what to think.
5. **Rhythm and syntax:** Find repeated sentence shapes, mechanical symmetry, stacked fragments, and monotonous pacing.
6. **Diction and formatting:** Find clichés, inflated vocabulary, vague abstractions, decorative formatting, and other recognizable AI-associated habits.

Do not let a clean phrase scan excuse unsupported, repetitive, or purposeless prose.

**Complete when:** every finding names the actual harm it causes, not merely the pattern it resembles.

### 4. Produce the mode-specific result

#### Audit

Report findings without rewriting the draft. For each finding, provide:

- the pattern family;
- a short quotation or exact location;
- why it hurts this piece;
- the smallest useful correction.

Group repeated instances when they share one cause. State when no material problems are found. Do not assign a slop score, claim to detect AI authorship, or pad the report with harmless matches.

#### Edit

Make the minimum effective edit:

- preserve the writer's point, facts, uncertainty, terminology, and recognizable voice;
- leave strong sentences alone;
- protect concrete details instead of replacing them with polished abstractions;
- remove repetition and generic scaffolding before swapping words;
- retain deliberate fragments, repetition, hedging, passive voice, or jargon when they serve the piece;
- flag unsupported claims that cannot be repaired from available facts;
- never invent evidence, examples, statistics, quotations, product capabilities, or opinions.

Return the revised prose, or edit the requested file, followed by a short summary of material changes. Mention unresolved factual or interpretive questions separately.

#### Draft

Build from the writing contract rather than from a generic template:

- choose a structure that fits the reader and purpose;
- use only supplied or verified facts;
- make claims proportional to the evidence;
- use concrete nouns, verbs, examples, and consequences where the source material supports them;
- vary rhythm in service of meaning rather than variation for its own sake;
- preserve the requested degree of polish, personality, and formality.

If the brief lacks facts needed for specificity, expose the gap or use a clear placeholder. Do not fabricate specificity to make the draft sound authoritative.

**Complete when:** the deliverable matches the requested mode and contains no unmarked invention.

### 5. Run the finish gate

Before returning the work, verify:

- **Meaning:** Actors, actions, scope, modality, causality, and conclusions still match the source or brief.
- **Facts:** Every specific claim comes from the user, the source, or verified material.
- **Voice:** The writer would recognize the vocabulary, cadence, stance, and level of polish.
- **Purpose:** Each paragraph contributes to the intended reader outcome.
- **Structure:** No idea is repeated merely to simulate emphasis or completeness.
- **Patterns:** Flagged constructions were judged in context; repeated clusters were fixed.
- **Rhythm:** Sentence and paragraph shapes fit the content without becoming mechanical.
- **Restraint:** Strong original lines survived, and edits did not sanitize useful character.
- **Mode:** Audits contain no rewrite; edits contain the revision and change summary; drafts respect the factual boundary.

If any check fails, revise and run the gate again.
