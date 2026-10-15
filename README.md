# Agent skills for turning ideas into software

[![skills.sh](https://skills.sh/b/SirDarcanos/agentskills)](https://skills.sh/SirDarcanos/agentskills)

Have an idea for an app, but aren't sure what to ask your coding agent next? You can describe who it's for and what it should do without knowing how to design a database or write a test.

These are the skills I use in my own projects and share for others to adapt. They guide your agent from questions about your idea to implementation, checks, and review:

- **Decide what to build.** Work through what matters, what can wait, and what a useful first version would do.
- **Delegate the coding steps.** Let the agent choose how to build an agreed change while bringing important product choices back to you.
- **See what was checked.** Ask for the checks that ran, their results, and anything still unverified. Use that report alongside your own trial of the software to decide whether it meets your needs.

Already write code? The same workflow helps you focus on behavior, review findings, and risks instead of supervising every generated line.

## What are agent skills?

A **skill** is a set of instructions your coding agent loads for a particular job. These are editable files for your existing agent, not another app to learn.

The skills are free and open source under the [MIT license](LICENSE). Your agent and any services you choose may have their own costs.

**[Start with `setup-project`](#get-started)** · [See a booking-tool example](#example-a-booking-tool) · [Browse all skills](#all-skills)

## From idea to delivery

Start with `setup-project` to establish how the agent should work in your project. Then use the stages your change needs.

| Stage | What it helps you get | Your part |
| --- | --- | --- |
| **Set up the project** | `setup-project` establishes project context, agent instructions, and working conventions before delivery begins. | Answer questions about how you want to work and approve the proposed setup changes. |
| **Clarify the idea** | `shape-work` asks about goals, users, and trade-offs in manageable rounds, so the agent doesn't have to guess what you want. | Explain the problem and choose what matters first. |
| **Keep a specification when useful** | `write-spec` records the agreed behavior for work that needs a lasting reference. A small, single-session task can skip it. | Confirm that it captures the agreement. |
| **Split larger work into tasks** | `write-tickets` uses the specification and current context to propose tasks and dependencies. Skip it when one change is enough. | Review the breakdown and approve publication to your tracker. |
| **Build and check** | `work-on` handles one agreed change and relevant checks. `work-on-spec` coordinates a larger plan across tasks. | Answer new product questions and approve work beyond the agreed scope. |
| **Review the result** | `review-delivery` calls for separate reviews of project rules and agreed behavior. `pr` explains the changes and remaining risks in plain language. | Try the result and decide whether to accept it. |

These are responsibilities, not a checklist of commands you must run. Once the project is set up, a small, clear change can go straight to `work-on`. It brings in `analyze` when technical evidence is missing, selects an implementation method, and handles checks, review, and reporting. You can call a specialist directly when you want that specific job, but you don't need to manage every handoff.

The skills use the conversation and project context. Give them the idea, task, or issue reference; you don't need to repeat their procedures or remind them to ask for approval. Planning, building, merging, and deployment retain their separate permission boundaries.

Independent review needs an agent that can run separate reviewers and your permission to use them. If a required check or review is unavailable, the workflow calls for reporting the gap rather than treating the work as verified.

## Get started

You'll need a coding agent that supports skills and can read your project files. The installation command also requires Node.js and `npx`. Start in a project you can safely experiment with.

### 1. Install the workflow skills

Run this in your terminal:

```bash
npx skills add SirDarcanos/agentskills
```

Choose your agent, installation destination, and the workflow skills, including `setup-project`. Writing and model skills are optional. Check for existing skills with the same names before replacing them.

Skills can need other skills for particular jobs. For example, `setup-project` needs `domain-modeling` for domain records and `github-repo-setup` for GitHub configuration. Include those companions when selecting your skills; running one skill does not authorize it to install missing tools or skills. See the [`setup-project` requirements](workflow/setup-project/README.md#install-and-requirements).

### 2. Run `/setup-project` in your agent

Open your project folder in the agent, then enter:

```text
/setup-project
```

The skill inspects what already exists and asks about the missing decisions: what the project is for, how you want to work, and which actions need your approval. It prepares the agent instructions and project guidance so later skills can use those answers. You don't need to name the files or tell it how to conduct setup.

It shows you a plan before changing anything, applies only what you approve, and checks the result. Existing instructions and useful conventions are preserved. Run it when establishing the project, or when the setup needs updating—not before every feature.

#### When you use GitHub

`setup-project` coordinates the GitHub work through `github-repo-setup`; you don't need to run that companion separately. It covers:

- **The repository:** create a new one or configure the existing one. For a new repository, it asks about the owner, name, visibility, license where applicable, and whether to push your local work. An existing remote is not a reason to create a second repository.
- **How changes are approved:** agree on how work reaches the main branch, such as through pull requests, then configure the approved branch protections and any exceptions. It does not invent reviewers or override existing organization rules.
- **Security settings:** check Dependabot alerts and security updates, secret scanning, and protection against pushing secrets. Missing protections go into the approval plan; availability depends on GitHub permissions, plan, and organization rules.
- **The issue workflow:** review existing labels and propose the labels and conventions that specs, tasks, and releases need. Later skills use this guidance to create spec issues, link their tasks, and record dependencies using GitHub's actual relationships. Setup does not create a backlog for you.
- **Instructions for later sessions:** record the agreed repository, tracker, permission, and release conventions so you don't have to explain them again to every skill.

If these choices are unfamiliar or you don't have a preference, tell your agent: “Choose sensible defaults based on this project's size and scope.”

You'll see the proposed local and GitHub changes together before approving them. Existing settings and labels are preserved unless their changes are explicitly approved. The skill checks the resulting GitHub state; unavailable access or required protections are reported as blocked, not silently treated as complete.

The GitHub route needs an authenticated GitHub CLI (`gh`) and sufficient permissions. If you aren't using GitHub, setup can stay local with no GitHub login. Setup does not build or deploy your application.

### 3. Bring your idea

With setup complete, describe what you want:

```text
/shape-work I want people to book places in my classes.
```

The skill asks the product questions needed to clarify the idea. Answer them and confirm the resulting agreement. The [booking example below](#example-a-booking-tool) shows how to continue for a small task or a larger project.

Enter these slash commands in your agent, not your terminal. Check that your agent exposes the installed skills as commands; invocation support varies. For delivery, check the [`work-on` companions](workflow/work-on/README.md#install-and-dependencies) and the [`work-on-spec` requirements](workflow/work-on-spec/README.md#installation-and-compatibility). Installing a skill does not supply missing tools or permissions.

## Example: a booking tool

*An illustration, not a tested application or customer story. Issue numbers below are examples. Continue after setup, one command at a time, answering questions and approving decisions as they arise.*

### Start with the idea

```text
/shape-work I want people to book places in my classes.
```

The skill might ask how many places each class has, whether people can cancel, and when they pay. Suppose you agree on a class list, reservations, and a clear “full” message, leaving payments and waiting lists for later. You supply the decisions; the skill knows how to explore and record them.

### For a small, single-session change

Once you've agreed on the work:

```text
/work-on the booking tool we agreed on
```

You don't need a separate specification or tickets for one cohesive change. `work-on` uses the agreement in the conversation, obtains any missing technical analysis, and takes the work through implementation, checks, review, and reporting.

If the change is already captured in an issue, reference that instead:

```text
/work-on #4
```

You can also supply the issue URL. The skill reads the issue and project context; you don't need to paste its contents or add instructions about testing and approval.

### For larger work that needs a specification and tasks

From the agreed conversation, run:

```text
/write-spec
```

The skill uses the existing agreement, preserves decisions such as leaving payments for later, and asks about any missing commitments. Confirm the specification and, when using GitHub, approve any proposed publication. Suppose the resulting spec issue is `#12`.

If the work needs breaking into tasks, continue:

```text
/write-tickets
```

It uses the specification and current context, obtains missing technical evidence when needed, and proposes the tasks and their dependencies. Review and approve the tracker changes before they are published. If suitable tasks already exist, you don't need to create them again.

Then request delivery of the specification:

```text
/work-on-spec #12
```

A link to the spec issue works too. `work-on-spec` coordinates its tasks, starts eligible work, and waits for prerequisites as needed. It requires tracker access and an agent environment that can assign work to separate coding agents, with your permission. It reports missing capability rather than pretending the work ran.

These short commands rely on the conversation and project context. If you move to a fresh session, provide the relevant issue or document reference. You don't need to repeat the skills' procedures or safeguards.

### Try the result

Delivery handles the relevant checks and independent review through `review-delivery`, then the change report through `pr`. Required tools and permissions still apply; missing required review leaves the work unaccepted. You don't need to call those skills again to repeat completed work.

Read what was checked and what remains uncertain. For this tool, useful evidence might cover reserving the last place, refusing the next booking, and preventing two people from taking the same place. These are examples, not claims that checks have run. Try the booking flow yourself against the agreement.

Deployment is a separate decision: the delivery commands don't grant permission to put the tool online. You don't need to append “don't deploy” to make that boundary apply.

## When something goes wrong

Describe the bug in ordinary language: what you expected, what happened, and how to reproduce it if you know. When the agent recognizes that a bug needs investigation, it can load [`investigate-bug`](workflow/investigate-bug/) itself. You can also invoke it directly:

```text
/investigate-bug Cancelling a booking doesn't free up a place in the class.
```

The skill tries to reproduce the problem, trace its cause, and gather evidence for a fix. It checks for existing reports and uses `write-tickets` to prepare or update a bug ticket, with your approval before tracker changes. If it can't confirm the bug or establish the cause, it reports what remains unknown rather than calling the ticket ready for a fix.

An investigation-only request stops there. When you're ready to authorize the repair, ask `work-on` to deliver the resulting ticket. Delivery reuses current investigation evidence and handles implementation, regression checks, review, and reporting; you don't need to repeat the diagnosis.

## Continue in another session

When moving work to another session, harness or directory, ask for a handoff:

```text
/handoff Continue investigating the booking cancellation bug.
```

[`handoff`](workflow/handoff/) writes a focused document with the relevant decisions, work state, evidence pointers, approval boundaries and suggested next skills. It runs only when requested and does not start the next task. Give the receiving agent the returned file path; for later resumption, supply an approved durable destination because temporary files can disappear. For shortening the current conversation without moving work, use your agent's built-in compaction instead.

## All skills

Pick a skill for the job in front of you. Each link explains what it does, what it needs, and how to use it.

### Workflow

#### Understand and plan

| Skill | What it helps you do |
| --- | --- |
| [`shape-work`](workflow/shape-work/) | Work out what you want to build through questions about goals, users, priorities, and trade-offs. |
| [`research`](workflow/research/) | Investigate a question using cited sources and make uncertainty visible. |
| [`analyze`](workflow/analyze/) | Find technical risks and existing work you can reuse before committing to a build. |
| [`write-spec`](workflow/write-spec/) | Give you and the agent a shared description of what to build and how to judge the result. |
| [`write-tickets`](workflow/write-tickets/) | Break agreed work into manageable tasks, with approval before publishing them. |
| [`domain-modeling`](workflow/domain-modeling/) | Give you and the agent shared terms for the project and records of important design decisions. |
| [`investigate-bug`](workflow/investigate-bug/) | Find out what is going wrong and why, and prepare the evidence for a fix. Investigation alone stops before repair. |

#### Build and deliver

| Skill | What it helps you do |
| --- | --- |
| [`work-on`](workflow/work-on/) | Take one agreed change through implementation, checks, independent review, and a change report. |
| [`work-on-spec`](workflow/work-on-spec/) | Coordinate delivery of an approved specification across its tasks. |
| [`prototype`](workflow/prototype/) | Try a runnable experiment to answer a design or feasibility question before committing to the full build. |
| [`tdd`](workflow/tdd/) | Build with tests first: demonstrate the missing behavior, implement it, then improve the code. |
| [`acceptance-first`](workflow/acceptance-first/) | Start with executable examples of the workflow people need, then build against them. |
| [`characterize`](workflow/characterize/) | Add checks around existing behavior so you can spot unintended changes when updating older code. |
| [`build-and-check`](workflow/build-and-check/) | Make small changes and check each one before moving on, including documentation and configuration work. |
| [`review-delivery`](workflow/review-delivery/) | Get independent reviews of whether changes follow project rules and deliver what was agreed. |
| [`pr`](workflow/pr/) | Get a plain-language account of what changed, what was checked, and how hard it would be to undo, in a pull request—a proposal to merge the changes. |
| [`handoff`](workflow/handoff/) | Carry one task into another session with a purpose-specific document, existing artifact references, and clear approval boundaries. |

#### Set up the project

| Skill | What it helps you do |
| --- | --- |
| [`setup-project`](workflow/setup-project/) | Establish project context, agent instructions, and working conventions through an approved setup plan. |
| [`github-repo-setup`](workflow/github-repo-setup/) | Create or configure a GitHub repository within an approved scope. |
| [`implementation-preflight`](workflow/implementation-preflight/) | Check where changes belong in Git before editing, so unrelated work stays separate. |

### Writing

Optional help with the words around your software.

| Skill | What it helps you do |
| --- | --- |
| [`slop-guard`](writing/slop-guard/) | Remove generic or padded prose while keeping your meaning and voice. |
| [`stay-positive`](writing/stay-positive/) | Make prose more constructive without softening important warnings or forcing optimism. |
| [`create-changelog`](writing/create-changelog/) | Create a project's first changelog from its actual history. |
| [`update-changelog`](writing/update-changelog/) | Keep an existing changelog focused on changes that matter to users. |

### Models

Optional specialist tools for evidence-backed judgments or building model-powered features. You don't need these additional models to use the delivery workflow. Assessments require an explicit request or an approved project policy; installation, data sharing, and spending retain their own approval requirements.

| Skill | What it helps you do |
| --- | --- |
| [`ask-clef`](models/ask-clef/) | Ask local Clef to assess a specific question against supplied evidence. |
| [`ask-clef-flash`](models/ask-clef-flash/) | Ask local Clef Flash for an evidence-backed assessment. |
| [`ask-nimble`](models/ask-nimble/) | Ask local Nimble to judge a specific question against supplied evidence. |
| [`ask-jev`](models/ask-jev/) | Use hosted Jev for an evidence-backed assessment, within approved data-sharing and spending limits. |
| [`build-with-nimble`](models/build-with-nimble/) | Build features such as routing, ranking, and verification with Nimble through Ollama. |

For comparisons, see the [decision-model benchmark](benchmarks/decision-models/). It uses synthetic cases; its scores are not a guarantee for your task. Validation is offline by default, with live inference and hosted billing requiring explicit opt-in.

## What to expect

These skills guide an agent; they do not guarantee it will follow every instruction or produce correct software. Checks and separate reviews can miss problems, so try the important workflows yourself. Get qualified technical review before relying on software that handles sensitive data, money, or other high-stakes operations.

If a tool, permission, companion skill, or required check is missing, the agent should tell you. Check the selected skills' requirements for your agent; this collection is not certified across all runtimes.

[Start with `setup-project`](#get-started), then explore your idea with `shape-work`.

## Adapting skills and finding the details

Skills live in `workflow/`, `writing/`, and `models/`. Each skill directory contains a `SKILL.md` entry point, a human-facing `README.md`, and any supporting references or scripts. When copying manually, copy the complete skill directory, including its license notices; for example, `workflow/shape-work/`, not the whole `workflow/` folder. Adjust instructions, tools, and checks to suit your project.

Separate installed copies need their own updates. A merge in this repository does not refresh them, and an older skill with the same name may not be compatible with newer companions.

- **Single-change delivery:** [`work-on` dependencies and runtime requirements](workflow/work-on/README.md).
- **Multi-task delivery:** [`work-on-spec` requirements](workflow/work-on-spec/README.md).
- **What has been checked:** [current composable-delivery evidence and limits](docs/validation/composable-acceptance/README.md) and [historical delivery coverage](docs/validation/delivery-coverage/README.md). Historical ownership descriptions are not current installation guidance. The installation commands above have not been exercised as part of this documentation change; recorded Pi/macOS trials do not certify every agent or installation route.
- **Replacing an existing installation:** [approved-target migration runbook](docs/agents/installed-skill-migration.md) and [sandbox migration checks](docs/validation/installed-skill-migration/README.md). The checks do not modify real installations.
