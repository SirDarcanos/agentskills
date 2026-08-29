# Agent Skills

Reusable skills for coding agents. This repository collects skills that I use in my own workflows and share for others to adapt.

## Repository layout

Each skill lives in its own directory and uses `SKILL.md` as its entry point:

```text
skill-name/
├── SKILL.md
├── references/    # Optional supporting material
└── scripts/       # Optional automation
```

A skill's `SKILL.md` explains when to use the skill and gives the agent its working instructions. Supporting files stay beside the skill so it can be copied as one unit.

## Using a skill

Clone the repository, then copy or link the skill directory into the skills location used by your coding agent:

```bash
git clone https://github.com/SirDarcanos/agentskills.git
```

Consult your agent's documentation for its skill discovery path and supported metadata. Review a skill before enabling it because instructions and tool assumptions can differ between agent runtimes.

## Adapting skills

Treat these skills as starting points. Update paths, tools, commands, and completion checks to match your environment. Keep related references and scripts with the skill when copying it.
