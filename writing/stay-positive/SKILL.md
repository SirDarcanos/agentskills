---
name: stay-positive
description: Reframe human-facing prose constructively without forcing optimism or weakening meaning. Use when auditing, editing, or drafting prose, and when the user invokes stay-positive or asks to make writing more positive, constructive, encouraging, or less negative.
---

# Stay Positive

Treat positivity as a framing choice, not a sentiment requirement. Reframe negativity only when a constructive alternative preserves the meaning, context, facts, stakes, emotion, and recognizable voice.

## Invocation

Load this skill when the user:

- invokes `stay-positive` by name;
- asks to make prose more positive, constructive, encouraging, or less negative;
- asks to audit, edit, rewrite, review, or draft human-facing prose.

Apply it to prose meant for people, including articles, documentation, reports, feedback, correspondence, announcements, marketing copy, and fiction. For source code or structured data, apply it only to embedded human-facing prose.

Invocation authorizes consideration, not automatic brightening. Change only passages with a constructive alternative that preserves their purpose and meaning. When no such opportunity exists, leave the framing intact.

## Choose the mode

Infer the mode from the request. Ask which mode the user wants only when the deliverable would otherwise be ambiguous.

- **Audit:** Identify useful reframing opportunities without rewriting the prose.
- **Edit:** Revise supplied prose with the minimum effective changes.
- **Draft:** Write new prose using constructive framing where it serves the piece.

## Workflow

### 1. Establish the writing contract

Determine the purpose, audience, context, intended effect, factual boundaries, and voice. For an edit or audit, read the full prose before judging individual lines. For a draft, use only supplied or verified facts.

When the `slop-guard` skill is installed, load and apply it in the same mode. Its voice, fidelity, and anti-slop requirements remain part of the writing contract.

**Complete when:** the requested mode and the boundaries that must survive are clear enough to proceed without guessing.

### 2. Classify the framing

Read [references/decision-guide.md](references/decision-guide.md) and [references/casebook.md](references/casebook.md).

Classify each potentially negative passage as:

- **Constructive opportunity:** a more positive or constructive frame preserves its meaning and function.
- **Necessary negativity:** the negative framing carries truth, stakes, emotion, characterization, warning, criticism, or voice and should remain.
- **Uncertain:** reframing might sanitize, distort, trivialize, or change the writer's intent.

Leave necessary negativity alone. Leave uncertain passages unchanged, report only the uncertainty around those passages, and ask the user to confirm the intended treatment. Continue safe work elsewhere when the uncertain passage does not block it.

**Complete when:** every proposed reframe passes the decision guide and no meaningful negativity has been treated as a defect merely for being negative.

### 3. Produce the mode-specific result

#### Audit

Report material constructive opportunities without rewriting the prose. For each finding, provide:

- a short quotation or exact location;
- what the current framing does;
- why a constructive alternative would better serve the piece;
- the smallest useful correction.

List uncertain passages separately with a focused confirmation question. State when no useful reframing opportunities exist.

#### Edit

Make the minimum effective edit. Preserve strong original lines and all necessary negativity. Return the revised prose or edit the requested file, followed by a short summary of material changes. List unchanged uncertain passages separately and ask for confirmation.

#### Draft

Choose framing that gives the reader clarity, agency, or a credible way forward when the facts support it. Keep negative language when the subject, purpose, or voice requires it. Surface unresolved framing choices rather than inventing a silver lining.

### 4. Run the finish gate

Verify:

- **Meaning:** The actors, actions, scope, causality, modality, and conclusions still match the source or brief.
- **Context:** The rewrite has not hidden stakes, power differences, conflict, harm, or uncertainty.
- **Emotion:** Grief, anger, fear, disappointment, and other legitimate emotions retain their force when they matter.
- **Function:** Warnings still warn, criticism still criticizes, refusals remain clear, and consequences remain visible.
- **Voice:** The result sounds like the intended writer rather than a motivational speaker or corporate announcement.
- **Restraint:** Every positive change earns its place; no optimism, reassurance, praise, or solution was invented.
- **Uncertainty:** Ambiguous passages remain unchanged and are presented for confirmation.
- **Mode:** The result follows the Audit, Edit, or Draft contract.
- **Slop:** When `slop-guard` is installed, its finish gate also passes.

If any check fails, revise and run the gate again.
