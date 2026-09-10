---
name: github-repo-setup
description: Create and configure a GitHub repository from a new or existing local project.
disable-model-invocation: true
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

Everything beyond this baseline is opt-in. Examples include `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, issue forms, pull-request templates, GitHub Actions, Dependabot version-update configuration, team access, and deployment environments.

The repository workflow is a required decision, not a default. Ask how changes should reach the default branch and configure branch rules only after the user confirms the workflow.

## Workflow

### 1. Inspect

Inspect the current directory before asking questions. Determine:

- whether it is already a Git repository;
- whether it has commits or uncommitted changes;
- whether an `origin` remote already exists;
- which baseline files already exist;
- the likely stack for `.gitignore` selection;
- whether `gh` is installed and authenticated;
- the current and default branch names;
- any existing local development branch, GitHub ruleset, branch protection, or organization rule that constrains the workflow.

Stop if the directory already points to a GitHub repository and clarify whether the user wants configuration rather than creation. Never overwrite an existing remote or project file.

If the /grill-me skill is available, use it when more information is needed to properly set up the repository. Otherwise, ask the user to provide the information.

### 2. Resolve decisions

Infer decisions already supplied by the user. Ask once for only the missing items:

- repository name;
- owner (personal account or organization);
- profile: open source, private, or enterprise;
- enterprise visibility: private, internal, or public;
- short description, if wanted;
- open-source license;
- whether to push the current local project;
- how contributors should work:
  1. push directly to the default branch;
  2. work on branches and merge pull requests into the default branch; or
  3. merge work into a development branch, then merge that branch into the default branch;
- whether the default branch should reject direct pushes and require a pull request;
- whether any people, teams, GitHub Apps, or repository roles may bypass that rule, and whether each exception applies always or only to pull requests; `none` is a valid answer;
- for a development-branch workflow: the branch name, whether to create it, how changes enter it, and whether it receives its own direct-push or pull-request rules;
- any additional merge requirements, such as approval count, status checks, conversation resolution, signed commits, linear history, or merge queue;
- any opt-in additions.

Ask workflow questions as concrete choices and explain their effect. Recommend branch-to-default pull requests for a simple review gate. Recommend a development branch only when the user wants a persistent integration or release-staging step; do not create one by convention alone.

For enterprise repositories, treat organization rules as authoritative. Do not invent teams, owners, bypass actors, required checks, security contacts, or compliance requirements. Ask for them only when the requested addition needs them. Resolve every bypass actor to the exact GitHub actor type and ID before execution, and show that resolved identity in the plan.

### 3. Present the plan

Before changing local files or GitHub, show a compact plan containing:

- owner/name and visibility;
- local directory and whether existing history will be pushed;
- files to create;
- required Dependabot and secret-scanning settings;
- other repository settings to change;
- the chosen branch flow, including the source and destination of each pull request;
- branches to create;
- rules for the default and development branches;
- every bypass exception, or explicitly `none`;
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

8. Establish the confirmed branch workflow after the first commit is available remotely:
   - preserve the existing default branch unless the user approved changing it;
   - when requested, create the development branch from the confirmed starting branch and push it;
   - create no empty or orphan development branch merely to satisfy the plan.
9. Apply the confirmed branch rules. Prefer repository rulesets when the account and repository support them; otherwise use branch protection when it can enforce the same confirmed behavior. Before creating a rule, inspect repository and organization rules to avoid duplicate or contradictory protection. Match explicit refs, or GitHub's default-branch selector, rather than broad patterns that capture unintended branches.
10. A pull-request workflow must block direct updates to its protected destination branch. Configure only the confirmed requirements. Add bypass actors only when the user approved the exact resolved identity and bypass mode; an administrator is not implicitly an exception.
11. Apply only confirmed opt-in additions. Check feature availability and organization policy before changing access, rulesets, Actions, or other security settings.
12. If `/setup-matt-pocock-skills` is available, mention it as an optional next command for repositories that will use Matt Pocock's issue-tracking, triage, or domain-document workflows.

When a required security command needs unavailable permissions, a paid GitHub feature, or an organization-policy change, explain the exact constraint and mark setup as blocked rather than weakening or silently skipping the baseline. Treat confirmed branch protection the same way: if GitHub cannot enforce the agreed workflow, report the protection as blocked instead of claiming the repository is ready.

### 5. Verify

Completion requires all applicable checks to pass:

- `gh repo view OWNER/REPO` resolves to the confirmed repository;
- visibility and owner match the plan;
- Projects, Discussions, and Wikis are disabled;
- Dependabot alerts and security updates are enabled;
- secret scanning and push protection are enabled;
- the expected default and development branches and commits are present when requested;
- each confirmed ruleset or branch-protection rule is active and targets only the intended branch;
- direct pushes and pull-request requirements match the selected workflow;
- every approved bypass actor and mode is present, with no unapproved exception;
- no pre-existing file, remote, branch rule, or organization policy was overwritten;
- every confirmed opt-in addition is present or reported as blocked with a reason.

Report the repository URL, what was created or changed, what was intentionally left out, and any blocked step.
