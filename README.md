# Agent Skills

Reusable skills for coding agents. This repository collects skills that I use in my own workflows and share for others to adapt.

## Skills

### General skills

| Skill | When to use it |
| --- | --- |
| [`create-changelog`](create-changelog/) | Create a project's first `CHANGELOG.md` from repository evidence and Semantic Versioning history. |
| [`github-repo-setup`](github-repo-setup/) | Create a new GitHub repository from a local project with a minimal file set, Dependabot, and secret scanning. |
| [`implementation-preflight`](implementation-preflight/) | Select or create the correct Git branch and PR target before an implementation workflow begins. |
| [`slop-guard`](slop-guard/) | Audit, rewrite, or draft human-facing prose while preserving facts, meaning, and the writer's voice. |
| [`stay-positive`](stay-positive/) | Reframe prose constructively without forcing optimism or weakening necessary negativity. |
| [`update-changelog`](update-changelog/) | Maintain an existing changelog after notable changes, during release preparation, or when correcting release history. |

### Dungeons & Dragons skills

| Skill | When to use it |
| --- | --- |
| [`dnd-create-monster`](dnd-create-monster/) | Design, rebalance, or convert D&D 2024 monsters, returning Markdown by default with optional tool-specific formats. |
| [`dnd-format-prose`](dnd-format-prose/) | Transform prose into table-ready D&D narration, boxed text, bestiary lore, or adventure lore. |
| [`dnd-speak-with-dead`](dnd-speak-with-dead/) | Rewrite supplied text as an answer from a corpse affected by the Speak with Dead spell. |

## Repository layout

Each skill lives in its own directory and uses `SKILL.md` as its entry point:

```text
skill-name/
├── SKILL.md
├── README.md
├── references/    # Optional supporting material
└── scripts/       # Optional automation
```

A skill's `SKILL.md` explains when to use the skill and gives the agent its working instructions. Its `README.md` provides a human-facing overview. Supporting files stay beside the skill so it can be copied as one unit.

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
