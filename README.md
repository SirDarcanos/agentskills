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

Install the skills with the `skills` CLI:

```bash
npx skills add SirDarcanos/agentskills
```

To install a specific skill for Claude Code and Pi:

```bash
npx skills add SirDarcanos/agentskills --skill github-repo-setup --agent claude-code pi
```

You can also clone the repository and copy or link a skill directory into the discovery path used by your coding agent:

```bash
git clone https://github.com/SirDarcanos/agentskills.git
```

Review a skill before enabling it because instructions and tool assumptions can differ between agent runtimes.

## Adapting skills

Treat these skills as starting points. Update paths, tools, commands, and completion checks to match your environment. Keep related references and scripts with the skill when copying it.
