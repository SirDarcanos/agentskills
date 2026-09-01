# D&D Create Monster

An agent skill for designing, rebalancing, and converting D&D 2024 monsters for play or use in any tool.

The skill treats encounter role and memorable table play as design constraints, then checks the resulting stat block against creatures from the official SRD 5.2 bestiary. It returns a readable Markdown stat block by default and supports validated [OpenFray](https://github.com/SirDarcanos/openfray) Creature JSON when requested.

## When to use it

Use the skill to:

- create a monster from a concept, target challenge rating, or party level;
- rebalance an existing creature without rewriting unrelated details;
- convert a published or custom stat block to Markdown, OpenFray Creature JSON, or another supplied tool format;
- compare a design with role-similar SRD creatures;
- render a complete, readable 2024-style stat block.

Example requests:

```text
Create a CR 6 skirmisher built around dragging isolated characters into darkness.
```

```text
Rebalance this creature for CR 10 and return the OpenFray JSON.
```

## How it works

The skill:

1. establishes the creature's encounter role, challenge, and signature play pattern;
2. preserves source information when revising or converting an existing creature;
3. benchmarks AC, HP, attack bonus, save DC, and expected damage against comparable SRD creatures;
4. builds and reconciles the creature's mechanics independently of output format;
5. validates OpenFray JSON when that format is requested and follows another tool's actual schema when supplied;
6. applies [`dnd-format-prose`](../dnd-format-prose/) when creating bestiary lore or player-facing description;
7. presents the selected format with a short design rationale.

Markdown is the default output. OpenFray JSON or another machine-readable format is returned only when requested. New monsters are treated as custom, while published creatures retain their source and identifier wherever the target format supports them. D&D Format Prose governs only the lore layer; creature mechanics remain under this skill's balance workflow.

## Benchmark and OpenFray tools

The bundled Python script can inspect the SRD baseline for every output format and validate OpenFray Creature JSON:

```bash
python3 scripts/benchmark.py stats 6
python3 scripts/benchmark.py show "Young Black Dragon" "Wyvern"
python3 scripts/benchmark.py validate creature.json
```

Run these commands from the skill directory. Benchmarking is format-independent. JSON validation applies specifically to OpenFray output. The script prefers an available local OpenFray compendium, falls back to the bundled SRD 5.2 data, and can retrieve the current OpenFray SRD compendium from GitHub.

## Requirements

- Python 3
- Network access only when neither a local nor bundled data source is available

## Files

```text
dnd-create-monster/
├── SKILL.md
├── README.md
├── references/
│   ├── balance.md
│   ├── schema.md
│   └── srd-creatures.json
└── scripts/
    └── benchmark.py
```

- [`SKILL.md`](SKILL.md) defines the design workflow, 2024 rules, and stat-block presentation.
- [`references/balance.md`](references/balance.md) documents balance targets and encounter-design conventions.
- [`references/schema.md`](references/schema.md) describes the optional OpenFray Creature JSON output shape.
- [`references/srd-creatures.json`](references/srd-creatures.json) supplies the bundled SRD 5.2 benchmark data.
- [`scripts/benchmark.py`](scripts/benchmark.py) provides comparison and validation commands.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill dnd-create-monster
```

You can also copy the `dnd-create-monster` directory into your agent's skill discovery path.
