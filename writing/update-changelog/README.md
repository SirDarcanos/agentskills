# Update Changelog

An agent skill for maintaining an existing software changelog from repository evidence.

The skill preserves the project's established changelog format, records only notable user-facing changes, and keeps releases, issue links, and version comparisons accurate.

## When to use it

The skill can run automatically after a notable change in a project that already has a changelog. It can also be invoked manually to:

- add entries under `Unreleased`;
- prepare a Semantic Versioning release;
- add a missing historical release;
- correct an existing entry.

```text
/update-changelog
```

Use `create-changelog` when the project has no changelog yet.

## How it works

The skill:

1. reads the complete changelog and learns its existing conventions;
2. inspects the requested change, commits, diffs, tags, releases, pull requests, and issue references;
3. assigns each supported change to one changelog location;
4. writes concise entries using the project's category and link style;
5. moves pending entries into a dated release when requested;
6. verifies that unrelated release content remains unchanged.

It does not infer missing history, duplicate existing entries, or restructure a mixed or malformed changelog without approval.

## Release handling

For releases, the skill checks the requested version against Semantic Versioning, preserves unrelated `Unreleased` entries, keeps versions newest first, and updates comparison links when the changelog uses them.

## Files

```text
update-changelog/
├── SKILL.md
├── README.md
└── references/
    └── example-changelog.md
```

- [`SKILL.md`](SKILL.md) defines automatic and manual invocation, update modes, and verification.
- [`references/example-changelog.md`](references/example-changelog.md) is used when the project follows Keep a Changelog.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill update-changelog
```

You can also copy the `update-changelog` directory into your agent's skill discovery path.
