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

**[Try Shape Work with your own idea](#get-started)** · [See a booking-tool example](#example-a-booking-tool) · [Browse all skills](#all-skills)

## From idea to delivery

Use the stages your project needs.

| Stage | What it helps you get | Your part |
| --- | --- | --- |
| **Clarify the idea** | `shape-work` asks about goals, users, and trade-offs in manageable rounds, so the agent doesn't have to guess what you want. | Explain the problem and choose what matters first. |
| **Agree on the result** | `write-spec` records what the software should do and how you'll tell whether it works. | Check that the plan describes what you mean. |
| **Plan the work** | `analyze` examines the existing project. For larger work, `write-tickets` proposes smaller tasks and the order they depend on. | Decide on choices that affect scope, cost, or risk; approve any changes to your issue tracker. |
| **Build and check** | `work-on` handles one agreed change and relevant checks. `work-on-spec` coordinates a larger plan across tasks. | Answer new product questions and approve work beyond the agreed scope. |
| **Review the result** | `review-delivery` calls for separate reviews of project rules and agreed behavior. `pr` explains the changes and remaining risks in plain language. | Try the result and decide whether to accept it. |

For a small, clear change, start with `work-on`. You don't need another interview when the decisions are already settled. Planning alone does not authorize building; merging changes, publishing a release, and putting software online remain separate decisions.

Independent review needs an agent that can run separate reviewers and your permission to use them. If a required check or review is unavailable, the workflow calls for reporting the gap rather than treating the work as verified.

## Get started

Try Shape Work with one idea before choosing whether to build it. You can start here without learning the rest of the catalog.

You'll need a coding agent that supports skills and can read your project files. The terminal commands below also require Node.js and `npx`. Start in a project you can safely experiment with.

### 1. Install Shape Work

Run this in your terminal:

```bash
npx skills add SirDarcanos/agentskills --skill shape-work
```

Choose your agent and installation destination when prompted. Check for an existing skill with the same name before replacing it.

If the conversation needs fact-finding, Shape Work may also need `research` or `analyze`. Those companion skills are separate installs; missing requirements should be explained, not silently installed.

### 2. Start with your idea

Replace the example with your own idea and send this to your coding agent:

```text
Use shape-work to help me plan a booking tool for my classes.
I don't code. Ask me about what it should do before we build anything.
```

You should get questions about the decisions still open, followed by a brief you can confirm or correct. You can stop there: asking for help with an idea does not commit you to building it.

Where your agent supports skill slash commands, you can use `/shape-work` instead. Check that it can find the installed skill; invocation and tool support vary by agent.

If your project also needs working conventions and agent instructions, ask for [`setup-project`](workflow/setup-project/). It proposes changes for approval, without starting the application build.

### 3. Move to building when you're ready

Once you have agreed on a specific change, follow the [Work On installation guide](workflow/work-on/README.md#install-and-dependencies) to add the delivery skills it needs. Then ask:

```text
Use work-on to implement the change we agreed on.
Show me what was checked and anything I still need to decide.
```

For a larger approved plan split into tasks, use [`work-on-spec`](workflow/work-on-spec/). It needs access to your issue tracker, an agent environment that can assign work to separate coding agents, and your permission to do so. Read its [requirements](workflow/work-on-spec/README.md#installation-and-compatibility) before choosing that route.

To choose more skills from the collection, run:

```bash
npx skills add SirDarcanos/agentskills
```

Choose the workflow skills for idea-to-delivery guidance. Writing and model skills are optional; installing `work-on` alone does not include its implementation, review, and reporting companions.

## Example: a booking tool

*An illustration of the workflow, not a tested application or customer story.*

Suppose you teach small classes. Each booking means another message and another check of how many places are left. You want people to reserve a place themselves.

**Describe your classes, not a database.** Shape Work might ask: How many places are available? Can people cancel? Do they need to pay when booking? You can answer those questions from experience, without choosing the technology.

**Choose a first version you can judge.** Suppose you agree on a class list, reservations, and a clear “full” message. Payments and waiting lists can wait because you explicitly chose to leave them for later. `write-spec` captures the agreement before you decide to build.

**Hand over the coding steps.** The agent uses `analyze` where technical facts are missing and can propose smaller tasks through `write-tickets`. You approve any publication to your tracker, then request `work-on` for one task or `work-on-spec` for the whole plan, with the tools and permissions each requires.

**Ask what happens to the last place.** A booking form appearing on screen isn't enough. Can someone reserve the last place? Is the next booking refused? What if two people try at once? These are examples of checks the work could need, not claims that they have run. Delivery calls for independent review and a report separating executed checks from anything unverified.

Try reserving a place yourself. Before putting the tool online, consider hosting, personal data, security, and ongoing support separately; a build request doesn't authorize those steps.

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

[Start with Shape Work](#get-started) to explore your idea before building.

## Adapting skills and finding the details

Skills live in `workflow/`, `writing/`, and `models/`. Each skill directory contains a `SKILL.md` entry point, a human-facing `README.md`, and any supporting references or scripts. When copying manually, copy the complete skill directory, including its license notices; for example, `workflow/shape-work/`, not the whole `workflow/` folder. Adjust instructions, tools, and checks to suit your project.

Separate installed copies need their own updates. A merge in this repository does not refresh them, and an older skill with the same name may not be compatible with newer companions.

- **Single-change delivery:** [Work On dependencies and runtime requirements](workflow/work-on/README.md).
- **Multi-task delivery:** [Work On Spec requirements](workflow/work-on-spec/README.md).
- **What has been checked:** [current composable-delivery evidence and limits](docs/validation/composable-acceptance/README.md) and [historical delivery coverage](docs/validation/delivery-coverage/README.md). Historical ownership descriptions are not current installation guidance. The installation commands above have not been exercised as part of this documentation change; recorded Pi/macOS trials do not certify every agent or installation route.
- **Replacing an existing installation:** [approved-target migration runbook](docs/agents/installed-skill-migration.md) and [sandbox migration checks](docs/validation/installed-skill-migration/README.md). The checks do not modify real installations.
