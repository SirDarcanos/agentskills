# D&D Speak with Dead

An agent skill for rewriting supplied text as an answer from a corpse affected by D&D's **Speak with Dead** spell.

The skill preserves the answer's facts and intent while expressing them through the deceased creature's knowledge, personality, vocabulary, and limited perspective.

## When to use it

Invoke the skill by name or explicitly ask for a Speak with Dead rewrite:

```text
Use dnd-speak-with-dead to rewrite: “The duke poisoned me during dinner.”
```

```text
Rewrite these five answers as responses from an anxious court wizard under Speak with Dead.
```

The skill transforms answers rather than automatically adjudicating whether a casting is valid.

## How it works

The skill:

1. identifies the facts and intent in the supplied answer;
2. limits the response to knowledge the creature possessed while alive;
3. rewrites the answer in the corpse's first-person voice;
4. uses brief, restrained phrasing shaped by the creature's established character;
5. returns only the rewritten answer unless notes or alternatives are requested.

For one casting, it returns no more than five numbered answers.

## Boundaries

The corpse cannot learn through the conversation, access its soul or an afterlife, know events after its death, or predict the future. When required knowledge is unavailable, it expresses uncertainty or ignorance in character.

The skill does not invent lore, clues, motives, or facts. It introduces deception only when the user requests it or establishes an antagonistic corpse and asks the agent to decide its response.

## Files

```text
dnd-speak-with-dead/
├── SKILL.md
└── README.md
```

[`SKILL.md`](SKILL.md) defines the rewrite method, voice guidance, spell boundaries, and guardrails.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill dnd-speak-with-dead
```

You can also copy the `dnd-speak-with-dead` directory into your agent's skill discovery path.
