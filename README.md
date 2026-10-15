# Agent Skills

[![skills.sh](https://skills.sh/b/SirDarcanos/agentskills)](https://skills.sh/SirDarcanos/agentskills)

Turn an idea into software with a coding agent, without having to direct every coding step.

These are the skills I use in my own projects and share for others to adapt. They give an agent a way to work through the questions, planning, implementation, checks, and review that sit between “I want to build this” and a result you can evaluate.

If you don't code, start with the problem you want to solve. The workflow asks you about users, priorities, and trade-offs while leaving routine technical choices to the agent. If you do code, it gives you a way to delegate implementation and focus your review on behavior, evidence, and risks rather than reading every generated line.

A **skill** is a set of instructions your coding agent can load for a particular job. These are editable files, not a separate app or a replacement for your agent. Use the idea-to-delivery workflow, or pick a skill for the task in front of you.

[Get started](#get-started) · [See an example](#example-a-booking-tool) · [Browse the skills](#all-skills)

## From idea to delivery

You decide what the software should do. The skills guide the agent through figuring out how to build it and showing what was checked.

| Stage | What the agent works on | Where you stay involved |
| --- | --- | --- |
| **Clarify the idea** | `shape-work` explores unresolved goals, users, and trade-offs through questions in manageable rounds. | Explain the problem, choose priorities, and confirm the scope. |
| **Agree on the result** | `write-spec` turns the agreement into a description of expected behavior and how to tell whether it works. | Check that it describes what you actually want. |
| **Plan the work** | `analyze` checks the technical starting point. For larger work, `write-tickets` proposes smaller tasks and their dependencies. | Approve consequential choices and any proposed tracker changes. |
| **Build and check** | `work-on` delivers one agreed change, choosing a suitable implementation method and running relevant checks. `work-on-spec` coordinates a specification across multiple tasks. | Answer new product questions and approve effects outside the agreed scope. |
| **Review and hand back** | Delivery uses `review-delivery` for separate reviews of project standards and agreed behavior, then `pr` for a plain-language change report. | Try the result, inspect the evidence and remaining risks, and decide whether to accept it. |

This is a guide, not a requirement to run every skill in order. A small, clear change can go straight to `work-on`; an existing agreement doesn't need another interview. Planning alone does not authorize building. Merging changes, publishing a release, and putting software online are separate decisions.

The intended handback tells you what changed, what was checked, what remains uncertain, and what needs your decision. That is more useful than “done,” whether or not you read code. Independent review needs an agent runtime that supports separate reviewers and your permission to use them; unavailable checks or review are reported as gaps, not passes.

## Get started

You need a coding agent that supports skills, access to your project files, and the tools required by the skills you choose. Start in a project you can safely experiment with.

### 1. Install the skills

With Node.js and `npx` available, run this in your terminal:

```bash
npx skills add SirDarcanos/agentskills
```

Choose your agent, installation destination, and skills in the installer. For the idea-to-delivery workflow, choose the workflow skills; writing and model skills are optional. Review the destination and any existing same-name skills before replacing files.

To try the discovery conversation first, install just `shape-work`:

```bash
npx skills add SirDarcanos/agentskills --skill shape-work
```

Skills can need companions for particular tasks. Shape Work may need `research` or `analyze` to investigate facts before recommending a choice. For delivery, use the [Work On installation guide](workflow/work-on/README.md#install-and-dependencies); installing `work-on` alone does not supply its review, implementation, and reporting companions.

### 2. Start with your idea

In your coding agent, ask:

```text
Use shape-work to help me plan a booking tool for my classes.
I don't code. Ask me about what it should do before we build anything.
```

Where your agent supports skill slash commands, you can use `/shape-work` instead. Invocation and tool support vary by agent; check that it can find the installed skill.

For a new project that also needs working conventions and agent instructions, explicitly ask to use [`setup-project`](workflow/setup-project/). It proposes those changes for approval; it does not build the application.

### 3. Move to building when you're ready

After agreeing on one bounded change, ask:

```text
Use work-on to implement the change we agreed on.
Show me what was checked and anything I still need to decide.
```

For an approved specification split into multiple tasks, use [`work-on-spec`](workflow/work-on-spec/) instead. It additionally needs tracker access and an authorized runtime that can assign work to separate coding agents. See its [requirements](workflow/work-on-spec/README.md#installation-and-compatibility) before choosing that route.

## Example: a booking tool

*This is an illustrative conversation, not a report of a tested application.*

Suppose you teach small classes and want people to reserve a place without messaging you.

**Start with the problem.** You ask Shape Work to explore the idea. It might ask how many places each class has, whether people can cancel, and whether payment belongs in the first version. You answer in terms of how your classes work, not database design.

**Agree on a small first version.** For this example, suppose you choose a class list, reservations, and a clear “full” message when no places remain. You explicitly leave payments and waiting lists for later. Ask `write-spec` to capture those decisions and the observable results you expect. No implementation starts just because the specification exists.

**Ask for the agreed work.** The agent assesses the existing project with `analyze` where technical facts are missing. If the first version needs several tasks, `write-tickets` proposes the breakdown; you approve any publication to your tracker. You can then request `work-on` for one task or `work-on-spec` for the whole agreed specification, subject to their runtime requirements.

**Evaluate more than the happy path.** Relevant checks could include reserving the last place, refusing another booking when the class is full, and handling two people trying to book that last place at once. Delivery calls for independent review against both the project rules and your agreement. The final report should distinguish checks that actually ran from anything still unverified.

You try booking a place yourself and decide whether the result meets your needs. Before putting it online, you still need to consider hosting, personal data, security, and ongoing support. Those aren't silently approved by asking the agent to build the tool.

## All skills

Each link opens a human-facing overview with requirements and a link to the agent's instructions. You don't need to learn every skill before starting: begin with `shape-work` for an unclear idea or `work-on` for one agreed change.

### Workflow

#### Understand and plan

| Skill | What it helps you do |
| --- | --- |
| [`shape-work`](workflow/shape-work/) | Work out what you want to build through questions about goals, users, priorities, and trade-offs. |
| [`research`](workflow/research/) | Investigate a question using cited sources and make uncertainty visible. |
| [`analyze`](workflow/analyze/) | Understand what a change involves in the existing project before building it. |
| [`write-spec`](workflow/write-spec/) | Put agreed behavior and success criteria into a clear specification. |
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
| [`characterize`](workflow/characterize/) | Capture existing behavior with checks before making a risky change to older code. |
| [`build-and-check`](workflow/build-and-check/) | Make small changes and check each one before moving on, including documentation and configuration work. |
| [`review-delivery`](workflow/review-delivery/) | Get independent reviews of whether changes follow project rules and deliver what was agreed. |
| [`pr`](workflow/pr/) | Explain a proposed change, its checks, risks, and reversal limits in a pull request: a reviewable proposal to merge it. |

#### Set up the project

| Skill | What it helps you do |
| --- | --- |
| [`setup-project`](workflow/setup-project/) | Establish project context, agent instructions, and working conventions through an approved setup plan. |
| [`github-repo-setup`](workflow/github-repo-setup/) | Create or configure a GitHub repository within an approved scope. |
| [`implementation-preflight`](workflow/implementation-preflight/) | Prepare the right Git branch and pull-request target before changes begin. |

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

These skills are instructions for an agent, not a guarantee that it will follow them perfectly or produce correct software. Checks and separate reviews can reduce how much you need to supervise, but they can miss problems. Try the important workflows yourself and get qualified technical review before relying on software that handles sensitive data, money, or other high-stakes operations.

The agent should make routine engineering decisions and bring meaningful product choices back to you. It should also tell you when a tool, permission, compatible companion, or required check is missing rather than quietly declaring success. Review each skill's requirements for your agent; this collection is not certified across all runtimes.

## Adapting skills and finding the details

Skills live in `workflow/`, `writing/`, and `models/`. Each skill directory contains a `SKILL.md` entry point, a human-facing `README.md`, and any supporting references or scripts. When copying manually, copy the complete skill directory, including its license notices; for example, `workflow/shape-work/`, not the whole `workflow/` folder. Adjust instructions, tools, and checks to suit your project.

Separate installed copies need their own updates. A merge in this repository does not refresh them, and an older skill with the same name may not be compatible with newer companions.

- **Single-change delivery:** [Work On dependencies and runtime requirements](workflow/work-on/README.md).
- **Multi-task delivery:** [Work On Spec requirements](workflow/work-on-spec/README.md).
- **What has been checked:** [current composable-delivery evidence and limits](docs/validation/composable-acceptance/README.md) and [historical delivery coverage](docs/validation/delivery-coverage/README.md). Historical ownership descriptions are not current installation guidance. The installation commands above have not been exercised as part of this documentation change; recorded Pi/macOS trials do not certify every agent or installation route.
- **Replacing an existing installation:** [approved-target migration runbook](docs/agents/installed-skill-migration.md) and [sandbox migration checks](docs/validation/installed-skill-migration/README.md). The checks do not modify real installations.
