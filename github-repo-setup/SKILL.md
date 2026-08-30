---
name: github-repo-setup
description: Create a new GitHub repository from a new or existing local project. Use when the user asks to create or initialize an open-source, private, or enterprise-owned GitHub repo. Keep files minimal while always configuring Dependabot and secret scanning where GitHub permits them.
---

# GitHub repository setup

Create a usable repository with the smallest appropriate footprint. Preserve existing project files and organization policy.

## Defaults

| Profile | Visibility | Default additions |
| --- | --- | --- |
| Open source | Public | `README.md`, a stack-specific `.gitignore`, and a license chosen by the user |
| Private | Private | `README.md` and a stack-specific `.gitignore` |
| Enterprise | Ask: private, internal, or public | `README.md` and a stack-specific `.gitignore` |

Only create a listed file when it is missing. Infer the `.gitignore` from the project; omit it when no stack is identifiable. For an open-source repository, ask the user to choose a license rather than assuming one.

Repository settings created by this skill:

- Projects disabled
- Discussions disabled
- Wikis disabled
- Dependabot alerts enabled
- Dependabot security updates enabled
- Secret scanning enabled
- Secret scanning push protection enabled
- Other settings left at GitHub or organization defaults

These security settings are required baseline work, not opt-ins. Check their availability for the repository visibility, GitHub plan, and organization policy. If GitHub blocks one, report the exact constraint; do not silently omit it or replace it with a weaker setting.

Everything beyond this baseline is opt-in. Examples include `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, issue forms, pull-request templates, GitHub Actions, Dependabot version-update configuration, rulesets, team access, and deployment environments.

## Workflow

### 1. Inspect

Inspect the current directory before asking questions. Determine:

- whether it is already a Git repository;
- whether it has commits or uncommitted changes;
- whether an `origin` remote already exists;
- which baseline files already exist;
- the likely stack for `.gitignore` selection;
- whether `gh` is installed and authenticated.

Stop if the directory already points to a GitHub repository and clarify whether the user wants configuration rather than creation. Never overwrite an existing remote or project file.

If the /grill-me skill is available, use it when more information are needed to properly set up the repository. Otherwise, ask the user to provide the information.

### 2. Resolve decisions

Infer decisions already supplied by the user. Ask once for only the missing items:

- repository name;
- owner (personal account or organization);
- profile: open source, private, or enterprise;
- enterprise visibility: private, internal, or public;
- short description, if wanted;
- open-source license;
- whether to push the current local project;
- any opt-in additions.

For enterprise repositories, treat organization rules as authoritative. Do not invent teams, owners, required checks, security contacts, or compliance requirements. Ask for them only when the requested addition needs them.

### 3. Present the plan

Before changing local files or GitHub, show a compact plan containing:

- owner/name and visibility;
- local directory and whether existing history will be pushed;
- files to create;
- required Dependabot and secret-scanning settings;
- other repository settings to change;
- opt-in additions, if any.

Get confirmation before executing the plan.

### 4. Create safely

Use the GitHub CLI where possible.

1. Run `gh auth status` and resolve authentication before continuing.
2. Create only missing baseline files, using project-specific content rather than generic filler.
3. Initialize Git only when needed. Preserve the current branch, history, and uncommitted work.
4. Create the repository with `gh repo create` using the confirmed owner, visibility, source directory, and push choice.
5. Disable Projects, Discussions, and Wikis:

```bash
gh repo edit OWNER/REPO --enable-projects=false --enable-discussions=false --enable-wiki=false
```

6. Enable Dependabot alerts and security updates:

```bash
gh api --method PUT repos/OWNER/REPO/vulnerability-alerts
gh api --method PUT repos/OWNER/REPO/automated-security-fixes
```

7. Enable secret scanning first, then push protection:

```bash
gh repo edit OWNER/REPO --enable-secret-scanning=true
gh repo edit OWNER/REPO --enable-secret-scanning-push-protection=true
```

8. Apply only confirmed opt-in additions. Check feature availability and organization policy before changing access, rulesets, Actions, or other security settings.
9. If the /setup-matt-pocock-skills is available, ask the user if they want you to run it as well.

When a required security command needs unavailable permissions, a paid GitHub feature, or an organization-policy change, explain the exact constraint and mark setup as blocked rather than weakening or silently skipping the baseline.

### 5. Verify

Completion requires all applicable checks to pass:

- `gh repo view OWNER/REPO` resolves to the confirmed repository;
- visibility and owner match the plan;
- Projects, Discussions, and Wikis are disabled;
- Dependabot alerts and security updates are enabled;
- secret scanning and push protection are enabled;
- the expected branch and commits are present when a push was requested;
- no pre-existing file or remote was overwritten;
- every confirmed opt-in addition is present or reported as blocked with a reason.

Report the repository URL, what was created or changed, what was intentionally left out, and any blocked step.
