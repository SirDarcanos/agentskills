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
| **Agree on the result** | `write-spec` records what the software should do and how you'll tell whether it works. | Check that the plan describes what you mean. |
| **Plan the work** | `analyze` examines the existing project. For larger work, `write-tickets` proposes smaller tasks and the order they depend on. | Decide on choices that affect scope, cost, or risk; approve any changes to your issue tracker. |
| **Build and check** | `work-on` handles one agreed change and relevant checks. `work-on-spec` coordinates a larger plan across tasks. | Answer new product questions and approve work beyond the agreed scope. |
| **Review the result** | `review-delivery` calls for separate reviews of project rules and agreed behavior. `pr` explains the changes and remaining risks in plain language. | Try the result and decide whether to accept it. |

Once the project is set up, a small, clear change can go straight to `work-on`. You don't need another interview when the decisions are already settled. Planning alone does not authorize building; merging changes, publishing a release, and putting software online remain separate decisions.

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
/setup-project Set up this project for working with a coding agent. I don't code; explain the decisions I need to make and show me your plan before changing anything.
```

The agent inspects the project, asks about missing working conventions, and proposes a setup plan. Review and approve that plan before it makes changes. Setup can be local-only; GitHub configuration needs the relevant access and approval. It prepares the project's instructions and conventions, not the application itself.

If the project is already set up, `setup-project` inspects what exists and proposes only needed changes. You don't need to repeat setup for every feature.

### 3. Work through your first idea

With setup complete, run:

```text
/shape-work Help me plan a booking tool for my classes. Ask me about what it should do before we build anything.
```

Answer the questions and confirm or correct the brief. Then follow the [booking example below](#example-a-booking-tool) to turn that agreement into work. You can stop after planning; building requires a separate request.

The examples use slash commands entered in your agent, not your terminal. Check that your agent exposes the installed skills as commands; invocation support varies. For delivery, check the [`work-on` companions](workflow/work-on/README.md#install-and-dependencies) and, for multi-task work, the [`work-on-spec` requirements](workflow/work-on-spec/README.md#installation-and-compatibility). An installed coordinator alone does not supply every tool, permission, or companion it needs.

## Example: a booking tool

*An illustrative sequence to try in your agent, not a tested application or customer story. Run each command separately, after the previous step has finished and you've answered its questions.*

Suppose you teach small classes and want people to reserve a place without messaging you. Install the workflow skills first, as shown above.

### 1. Set up the project

In your project folder, run this unless setup is already complete:

```text
/setup-project This project will be a booking tool for my classes. Set up the agent instructions and working conventions. Show me the proposed changes before applying them.
```

Answer the setup questions, approve the changes you want, and check the setup report for anything blocked before continuing.

### 2. Decide what the first version should do

```text
/shape-work I teach small classes and want people to reserve a place themselves. Help me decide what belongs in the first version. I don't code, so ask me about how bookings should work rather than which technology to use.
```

The agent might ask how many places each class has, whether people can cancel, and when they pay. For this example, suppose you agree on a class list, reservations, and a clear “full” message. You explicitly leave payments and waiting lists for later.

### 3. Record the agreement

After confirming the brief:

```text
/write-spec Write a specification from the booking-tool brief we agreed on. Keep payments and waiting lists out of this version. Describe how we'll check that bookings work, including when only one place is left. Show me the draft before publishing anything.
```

Read the specification and correct anything that doesn't match your intent. Confirm it before moving on; writing it does not start the build.

### 4. Check the technical starting point

```text
/analyze Review the approved booking-tool specification against this project. Recommend how to build and check it, and flag any decisions I still need to make. Don't implement it yet.
```

Resolve any product decisions or missing requirements. The agent should investigate technical facts rather than asking you to guess. If current analysis already covers the agreed work, reuse it instead of repeating this step.

### 5. Request the build

If the agreed work can be delivered as one change:

```text
/work-on Implement the booking flow in the approved specification. Show which checks ran and anything still unverified. Don't deploy it.
```

If the plan needs several tasks, first ask for a breakdown:

```text
/write-tickets Break the approved booking-tool specification into tasks using the analysis. Show me the proposed tasks and dependencies before publishing them.
```

Review the breakdown and approve the exact tracker changes. After the approved tasks and their dependencies are published, request the whole plan. `work-on-spec` handles the order of dependent tasks during delivery:

```text
/work-on-spec Deliver the approved booking-tool specification through its published tasks. Report what was checked and what still needs my decision. Don't deploy it.
```

Use one delivery route, not both for the same work. `work-on-spec` needs tracker access and an agent environment that supports assigning work to separate coding agents, with your permission. Missing capabilities or permission block that route; they aren't supplied by the command.

### 6. Try the result and read the report

Delivery includes relevant checks and, when the required reviewer capability and permission are available, independent review through `review-delivery`. Missing required review leaves the work unaccepted. `pr` prepares the change report; opening a pull request needs the project's permission. You don't need to invoke those skills again if delivery has already completed those steps.

Look for evidence that someone can reserve the last place, that the next booking is refused, and that two simultaneous bookings don't take the same place. These are examples of checks to expect, not claims that they have run. Try reserving a place yourself and compare the result with the specification.

Before putting the tool online, consider hosting, personal data, security, and ongoing support separately. A build request doesn't authorize those steps.

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
