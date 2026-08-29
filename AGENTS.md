# Agent instructions

## Repository purpose

This repository contains reusable skills for coding agents. Each top-level skill directory is an independent package with `SKILL.md` as its entry point and optional supporting files beside it.

## Working with skills

- Read a skill's complete `SKILL.md` before changing it.
- Resolve relative references from the directory containing `SKILL.md`.
- Keep trigger conditions in frontmatter specific enough to route matching requests without activating on unrelated work.
- Write ordered actions for procedures and checkable completion criteria for each workflow.
- Put branch-specific or lengthy reference material in a nearby file and link it from `SKILL.md` with a clear condition for reading it.
- Keep each instruction in one authoritative location.
- Preserve the skill author's tool names and runtime assumptions unless the change updates those assumptions across the whole skill.

## File conventions

A skill may use this structure:

```text
skill-name/
├── SKILL.md
├── references/
└── scripts/
```

Use lowercase kebab-case directory names. Keep `SKILL.md` at the skill root. Use relative links for files that ship with the skill.

## Validation

For each changed skill:

1. Read the rendered Markdown and check its frontmatter.
2. Follow every relative link from `SKILL.md` and confirm the target exists.
3. Check commands and scripts in the environment they name.
4. Verify that the description states when an agent should load the skill.
5. Review the diff for credentials, private data, generated files, and local paths that should remain portable.

The repository has no shared build or test command. Document any skill-specific validation in that skill.

## Pull requests

Keep a pull request focused on one skill or one related set of changes. State what behavior changed, how you validated it, and which agent runtimes or tools the skill expects.
