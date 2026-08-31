# Create Changelog

An agent skill for creating a project's first `CHANGELOG.md` from repository evidence.

The skill produces a concise, user-facing release history rather than copying commit messages. It follows Semantic Versioning, links known issues and pull requests, and leaves uncertain history undocumented instead of guessing.

## When to use it

Invoke the skill manually when a software project needs its first changelog:

```text
/create-changelog
```

If the project already has a changelog, use `update-changelog` instead.

## How it works

The skill:

1. inspects documentation, package metadata, tags, releases, commits, pull requests, and issue references;
2. selects changes relevant to users, operators, integrators, or security reviewers;
3. separates pending work from released versions;
4. applies Semantic Versioning and ISO 8601 release dates;
5. writes `CHANGELOG.md` at the repository root;
6. verifies ordering, links, evidence, and formatting.

Routine refactors, formatting changes, test-only work, and dependency churn without user impact are excluded.

## Output

The generated changelog uses an `Unreleased` section and non-empty categories such as:

- Breaking changes
- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security

Every entry is a short statement of observable impact. Release and issue links are added only when repository evidence supports them.

## Files

```text
create-changelog/
├── SKILL.md
├── README.md
└── references/
    └── example-changelog.md
```

- [`SKILL.md`](SKILL.md) defines invocation, evidence gathering, writing, and verification.
- [`references/example-changelog.md`](references/example-changelog.md) provides the target Keep a Changelog structure.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill create-changelog
```

You can also copy the `create-changelog` directory into your agent's skill discovery path.
