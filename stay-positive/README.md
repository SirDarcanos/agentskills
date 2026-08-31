# Stay Positive

An agent skill for making prose more constructive when the change preserves its meaning, context, facts, stakes, emotion, and voice.

Stay Positive does not force optimism. It leaves necessary negativity intact and treats grief, warnings, criticism, accountability, firm boundaries, conflict, and technical failure as meaningful rather than defects to polish away.

## How it works

The skill supports three modes:

- **Audit:** Reports useful reframing opportunities without rewriting the prose.
- **Edit:** Makes the minimum effective changes to supplied prose.
- **Draft:** Uses constructive framing where it serves the purpose and facts.

Potentially negative passages are classified as constructive opportunities, necessary negativity, or uncertain. Uncertain passages remain unchanged and are presented to the user for confirmation.

When [`slop-guard`](../slop-guard/) is installed, Stay Positive loads it in the same mode so constructive framing also preserves voice and avoids generic prose.

## Example requests

```text
Use stay-positive to audit this feedback. Do not rewrite it.
```

```text
Edit this email so it is constructive without softening the refusal.
```

```text
Draft an encouraging project update from these facts. Keep the missed deadline and its consequences clear.
```

The skill may also activate during prose reviews, edits, and drafts. It changes only framing that can become more constructive without losing meaning or context.

## What it protects

- facts, responsibility, severity, and uncertainty;
- legitimate emotion and intentional negative tone;
- warnings, criticism, refusals, and consequences;
- characterization, satire, irony, quotations, and technical terms;
- the writer's recognizable voice;
- uncertainty that requires the user's judgment.

It never invents hope, praise, progress, agency, lessons, solutions, or silver linings.

## Files

```text
stay-positive/
├── SKILL.md
├── README.md
└── references/
    ├── casebook.md
    └── decision-guide.md
```

- [`SKILL.md`](SKILL.md) defines invocation, modes, workflow, and the finish gate.
- [`references/decision-guide.md`](references/decision-guide.md) distinguishes constructive opportunities from necessary or uncertain negativity.
- [`references/casebook.md`](references/casebook.md) provides apply, preserve, and ask examples.

## Install

From the repository root, install the skill for a supported coding agent:

```bash
npx skills add SirDarcanos/agentskills --skill stay-positive
```

You can also copy the `stay-positive` directory into your agent's skill discovery path.
