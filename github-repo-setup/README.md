# GitHub Repository Setup

An agent skill for creating or configuring a GitHub repository while preserving project files, history, remotes, and organization policy.

The skill keeps the repository footprint small while configuring Dependabot and secret-scanning protections wherever GitHub permits them.

## When to use it

Request this skill when creating a repository or configuring an existing open-source, private, or enterprise-owned GitHub repository:

```text
/github-repo-setup
```

It can also be reached by an approved `setup-project` handoff. Loading its guidance never authorizes mutations: it requires an explicit setup request and a confirmed plan, or that exact approved handoff. An existing GitHub remote selects configuration; it does not trigger repository recreation. Ambiguous target identity or intent still requires clarification.

## Defaults

| Profile | Visibility | Files added when missing |
| --- | --- | --- |
| Open source | Public | `README.md`, stack-specific `.gitignore`, user-selected license |
| Private | Private | `README.md`, stack-specific `.gitignore` |
| Enterprise | Confirmed with the user | `README.md`, stack-specific `.gitignore` |

For a new repository, the plan proposes disabling Projects, Discussions, and Wikis. Existing repositories preserve those settings unless individual changes are approved. Dependabot alerts, Dependabot security updates, secret scanning, and push protection remain the required security baseline, subject to approval and feature availability.

Everything else is opt-in, including contribution files, issue templates, Actions, Dependabot version updates, teams, and deployment environments.

The skill resolves how changes should reach the default branch, reusing confirmed decisions instead of repeating an orchestrator's interview. You can allow direct work, require branch-to-default pull requests, or add a persistent development branch as an integration step. It resolves protected branches, required checks, and exactly approved bypass actors/modes without inventing organization requirements.

## How it works

The skill:

1. inspects the local Git state, files, stack, remotes, and GitHub CLI authentication;
2. asks only for decisions it cannot infer, including the branch and pull-request workflow;
3. presents the complete creation, security, branch, protection, and exception plan for confirmation;
4. creates a new repository or applies only the approved delta to an existing one;
5. creates a development branch only when requested and applies only confirmed rules and additions;
6. verifies the owner, visibility, branches, commits, security settings, protection rules, bypass exceptions, and preserved local state.

A required security feature that is blocked by permissions, plan limits, or organization policy is reported as blocked. The skill does not silently weaken the baseline.

## Requirements

- [GitHub CLI](https://cli.github.com/) installed
- An authenticated GitHub account with permission to create and configure the target repository
- Any organization approval required for enterprise settings

## Files

```text
github-repo-setup/
├── SKILL.md
├── README.md
└── references/
    ├── handoff.md
    └── validation.md
```

[`SKILL.md`](SKILL.md) contains route-specific behavior, commands, and completion checks. [The handoff contract](references/handoff.md) defines composition with a setup orchestrator. [Validation guidance](references/validation.md) covers standalone, existing-repository, partial-failure, and handoff scenarios. No live mutation is needed for an offline walkthrough.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill github-repo-setup
```

You can also copy the `github-repo-setup` directory into your agent's skill discovery path.
