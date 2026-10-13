---
name: github-repo-setup
description: Create or configure a GitHub repository when the user requests repository setup, or execute an approved GitHub handoff from setup-project.
---

# GitHub repository setup

Create or configure a usable repository with the smallest appropriate footprint. Preserve existing project files and organization policy.

Loading this skill does not authorize mutations. Execute only after an explicit repository-setup request and approval of the concrete plan, or an approved handoff from `setup-project`. For a handoff, read [the handoff contract](references/handoff.md) first; return a plan without executing when the orchestrator is still collecting approval. No literal Skill tool or subagent runtime is required.

## New-repository defaults

| Profile | Visibility | Default additions |
| --- | --- | --- |
| Open source | Public | `README.md`, a stack-specific `.gitignore`, and a license chosen by the user |
| Private | Private | `README.md` and a stack-specific `.gitignore` |
| Enterprise | Ask: private, internal, or public | `README.md` and a stack-specific `.gitignore` |

Only create a listed file when it is missing. Infer the `.gitignore` from the project; omit it when no stack is identifiable. For an open-source repository, ask the user to choose a license rather than assuming one.

For new repositories, propose these settings in the approval plan:

- Projects disabled
- Discussions disabled
- Wikis disabled
- Dependabot alerts enabled
- Dependabot security updates enabled
- Secret scanning enabled
- Secret scanning push protection enabled
- Other settings left at GitHub or organization defaults

Dependabot alerts/security updates and secret scanning/push protection are required security baseline work, not opt-ins. Check their availability for the repository visibility, GitHub plan, and organization policy. If GitHub blocks one, report the exact constraint; do not silently omit it or replace it with a weaker setting.

For existing repositories, preserve visibility, files, Projects, Discussions, Wikis, and unrelated settings unless an exact change is approved. Inspect the security baseline and propose missing protections for approval; a declined or unavailable required protection leaves this setup's baseline incomplete, not permission to mutate anyway. Existing organization rules remain authoritative.

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

Select **create-new** only when no intended repository already exists; select **configure-existing** when the project points at the intended GitHub repository. Ask if target identity or intent is ambiguous. Verify owner/name through GitHub, not a guessed remote string. Never overwrite an existing remote or project file, treat inaccessible state as absent, or create a replacement repository to bypass a permissions failure.

Reuse supplied inspected facts and confirmed decisions, verifying that they still hold. Ask remaining questions directly in concrete terms; do not require an external grilling skill or repeat the orchestrator's interview.

### 2. Resolve decisions

Infer decisions already supplied by the user. For an existing repository retain current values unless a change is requested. Ask once for only the missing items needed by the selected route:

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

Get confirmation before executing the plan. An orchestrator's approval of this exact scope satisfies this gate; changed scope requires renewed approval. Include an existing-to-proposed delta for configuration, including settings intentionally preserved.

### 4. Apply the approved route

Use the GitHub CLI where possible.

1. Run `gh auth status` and resolve authentication before continuing.
2. Re-read affected files/settings against the approved plan. Stop and reconcile changed state before writing. Create only approved missing files; preserve authored content and existing licenses.
3. Initialize Git only when explicitly planned and needed. Preserve the current branch, history, and uncommitted work. Commits and pushes require their own included approval; do not create a commit merely to make branch setup possible.
4. On **create-new**, use `gh repo create` with the confirmed owner, visibility, source directory, and push choice. On **configure-existing**, skip creation and remote assignment entirely. An ambiguous create response requires read-back before retrying.
5. On a new repository, apply the approved Projects/Discussions/Wikis defaults. On an existing repository, change only individually approved settings; do not run the all-three command unless all three changes are approved:

```bash
gh repo edit OWNER/REPO --enable-projects=false --enable-discussions=false --enable-wiki=false
```

6. Inspect and enable only approved missing Dependabot protections (already-enabled protections need no write):

```bash
gh api --method PUT repos/OWNER/REPO/vulnerability-alerts
gh api --method PUT repos/OWNER/REPO/automated-security-fixes
```

7. For approved missing scanning protections, enable secret scanning first, then push protection (omit already-satisfied flags):

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
12. Return the actual changes and verification evidence to the caller. Under `setup-project`, tracker labels and operating/domain documents are owned by that orchestrator; do not invoke a competing setup skill or create duplicate guidance.

When a required security command needs unavailable permissions, a paid GitHub feature, or an organization-policy change, explain the exact constraint and mark setup as blocked rather than weakening or silently skipping the baseline. Treat confirmed branch protection the same way: if GitHub cannot enforce the agreed workflow, report the protection as blocked instead of claiming the repository is ready.

### 5. Verify

Completion requires all applicable checks to pass:

- `gh repo view OWNER/REPO` resolves to the confirmed repository;
- visibility and owner match the plan;
- Projects, Discussions, and Wikis match the approved new-repository defaults or individually approved existing-repository changes; all unapproved existing settings are preserved;
- Dependabot alerts and security updates are enabled;
- secret scanning and push protection are enabled;
- the expected default and development branches and commits are present when requested;
- each confirmed ruleset or branch-protection rule is active and targets only the intended branch;
- direct pushes and pull-request requirements match the selected workflow;
- every approved bypass actor and mode is present, with no unapproved exception;
- existing files, remotes, rules, and organization policy were preserved except for exact approved changes; unrelated settings and custom rules remain intact;
- every confirmed opt-in addition is present or reported as blocked with a reason.

Verify via read-back: `gh repo view` for target/visibility, repository REST data for feature flags and scanning status, the vulnerability-alerts and automated-security-fixes GET endpoints for Dependabot, and active ruleset/branch-protection APIs for the approved refs. Follow pagination. A denied read or ambiguous 404 is unverified, not proof of disabled/absent configuration. Check enforcement and bypass actor IDs/modes, not just the existence of a ruleset. When controls cannot be inspected, report that verification gap rather than claiming success.

Report the repository URL, route, actual changes, intentionally preserved/omitted settings, read-back evidence, and blocked steps. After partial failure inspect actual state before retrying; never roll back user data or blindly repeat a creation command. An unchanged rerun should propose no substantive delta. When maintaining this skill, use [offline validation](references/validation.md); setup approval does not authorize live test repositories.
