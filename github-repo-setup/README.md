# GitHub Repository Setup

An agent skill for creating a GitHub repository from a new or existing local project without overwriting project files, history, or remotes.

The skill keeps the repository footprint small while configuring Dependabot and secret-scanning protections wherever GitHub permits them.

## When to use it

Explicitly invoke the skill when creating or initializing an open-source, private, or enterprise-owned GitHub repository:

```text
/github-repo-setup
```

It does not activate automatically because it creates remote resources and changes repository-wide settings. If the current project already points to a GitHub repository, the skill stops and clarifies whether configuration rather than creation is intended.

## Defaults

| Profile | Visibility | Files added when missing |
| --- | --- | --- |
| Open source | Public | `README.md`, stack-specific `.gitignore`, user-selected license |
| Private | Private | `README.md`, stack-specific `.gitignore` |
| Enterprise | Confirmed with the user | `README.md`, stack-specific `.gitignore` |

Projects, Discussions, and Wikis are disabled. Dependabot alerts, Dependabot security updates, secret scanning, and push protection are enabled when available for the repository and organization.

Everything else is opt-in, including contribution files, issue templates, Actions, Dependabot version updates, teams, and deployment environments.

The skill always asks how changes should reach the default branch. You can allow direct work, require branch-to-default pull requests, or add a persistent development branch as an integration step. It also asks which branches reject direct pushes, what pull-request checks apply, and whether any explicitly named people, teams, apps, or repository roles may bypass those rules.

## How it works

The skill:

1. inspects the local Git state, files, stack, remotes, and GitHub CLI authentication;
2. asks only for decisions it cannot infer, including the branch and pull-request workflow;
3. presents the complete creation, security, branch, protection, and exception plan for confirmation;
4. creates the repository and missing baseline files with the GitHub CLI;
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
└── README.md
```

[`SKILL.md`](SKILL.md) contains the defaults, decision points, GitHub CLI commands, safety rules, and completion checks.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill github-repo-setup
```

You can also copy the `github-repo-setup` directory into your agent's skill discovery path.
