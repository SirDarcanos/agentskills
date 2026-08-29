# Contributing

Contributions that improve an existing skill or add a focused, reusable skill are welcome.

## Add or update a skill

1. Create one directory per skill.
2. Add a `SKILL.md` entry point with valid YAML frontmatter.
3. Give the skill a specific name and describe the conditions that should trigger it.
4. Keep instructions actionable and include clear completion criteria.
5. Put optional detail in nearby `references/` or `scripts/` directories.
6. Check every relative path and command from the skill's directory.

Keep each pull request limited to one skill or one related change. Explain the behavior you tested and any agent, model, or tool assumptions.

## Before opening a pull request

- Read the rendered Markdown for formatting errors.
- Check links and relative paths.
- Remove credentials, personal data, generated output, and local agent state.
- Confirm that examples use placeholder secrets and safe commands.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
