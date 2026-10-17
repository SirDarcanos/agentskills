# All skills

Pick a skill for the job in front of you. Each link explains what it does, what it needs, and how to use it. For the short introduction, see the [project README](../README.md); for stage selection, session boundaries and shortcuts, follow the [workflow guide](workflow-guide.md).

For installation, updates and migration, use the [installation guide and support matrix](installation.md). Native plugins bundle all groups; standalone/npx installations can select skills and retain editable copies. Native commands can be namespaced; translate standalone examples using that guide.

## Workflow

### Understand and plan

| Skill | What it helps you do |
| --- | --- |
| [`what-now`](../workflow/what-now/) | Explicitly ask which installed skill or route fits; get inspected recommendations without starting a workflow. |
| [`shape-work`](../workflow/shape-work/) | Work out what you want to build through questions about goals, users, priorities, and trade-offs. |
| [`research`](../workflow/research/) | Investigate a question using cited sources and make uncertainty visible. |
| [`analyze`](../workflow/analyze/) | Find technical risks and existing work you can reuse before committing to a build. |
| [`write-spec`](../workflow/write-spec/) | Give you and the agent a shared description of what to build and how to judge the result. |
| [`write-tickets`](../workflow/write-tickets/) | Create tickets from agreed work and return linked IDs with short descriptions; new consequential scope and relationship effects retain their approval gates. |
| [`domain-modeling`](../workflow/domain-modeling/) | Give you and the agent shared terms for the project and records of important design decisions. |
| [`investigate-bug`](../workflow/investigate-bug/) | Find out what is going wrong and why, and prepare the evidence for a fix. Investigation alone stops before repair. |

### Build and deliver

| Skill | What it helps you do |
| --- | --- |
| [`work-on`](../workflow/work-on/) | Take one agreed change through implementation, checks, independent review, and a change report. |
| [`work-on-spec`](../workflow/work-on-spec/) | Coordinate delivery of an approved specification across its tasks. |
| [`prototype`](../workflow/prototype/) | Try a runnable experiment to answer a design or feasibility question before committing to the full build. |
| [`tdd`](../workflow/tdd/) | Build with tests first: demonstrate the missing behavior, implement it, then improve the code. |
| [`acceptance-first`](../workflow/acceptance-first/) | Start with executable examples of the workflow people need, then build against them. |
| [`characterize`](../workflow/characterize/) | Add checks around existing behavior so you can spot unintended changes when updating older code. |
| [`build-and-check`](../workflow/build-and-check/) | Make small changes and check each one before moving on, including documentation and configuration work. |
| [`resolve-merge-conflicts`](../workflow/resolve-merge-conflicts/) | Resolve active merge/rebase conflicts within existing integration authority, preserving compatible intent and unrelated work. |
| [`review-delivery`](../workflow/review-delivery/) | Get independent reviews of whether changes follow project rules and deliver what was agreed. |
| [`pr`](../workflow/pr/) | Explicitly request a PR report or publication after inspecting delivery; reuse current evidence without restarting delivery. Merge remains separate. |
| [`handoff`](../workflow/handoff/) | Carry one task into another session with a purpose-specific document, existing artifact references, and clear approval boundaries. |

### Set up the project

| Skill | What it helps you do |
| --- | --- |
| [`setup-project`](../workflow/setup-project/) | Establish project context, agent instructions, and working conventions through an approved setup plan. |
| [`github-repo-setup`](../workflow/github-repo-setup/) | Create or configure a GitHub repository within an approved scope. |
| [`implementation-preflight`](../workflow/implementation-preflight/) | Check where changes belong in Git before editing, so unrelated work stays separate. |

## Writing

Optional help with the words around your software.

| Skill | What it helps you do |
| --- | --- |
| [`writing-for-agents`](../writing/writing-for-agents/) | Write skills, instruction files and referenced guides with clear routing, ordered actions and checkable completion while preserving project authority. |
| [`slop-guard`](../writing/slop-guard/) | Remove generic or padded prose while keeping your meaning and voice. |
| [`stay-positive`](../writing/stay-positive/) | Make prose more constructive without softening important warnings or forcing optimism. |
| [`create-changelog`](../writing/create-changelog/) | Create a project's first changelog from its actual history. |
| [`update-changelog`](../writing/update-changelog/) | Keep an existing changelog focused on changes that matter to users. |

## Models

Optional specialist tools for evidence-backed judgments or building model-powered features. You don't need these additional models to use the delivery workflow. Assessments require an explicit request or an approved project policy; installation, data sharing, and spending retain their own approval requirements.

| Skill | What it helps you do |
| --- | --- |
| [`ask-clef`](../models/ask-clef/) | Ask local Clef to assess a specific question against supplied evidence. |
| [`ask-clef-flash`](../models/ask-clef-flash/) | Ask local Clef Flash for an evidence-backed assessment. |
| [`ask-nimble`](../models/ask-nimble/) | Ask local Nimble to judge a specific question against supplied evidence. |
| [`ask-jev`](../models/ask-jev/) | Use hosted Jev for an evidence-backed assessment, within approved data-sharing and spending limits. |
| [`build-with-nimble`](../models/build-with-nimble/) | Build features such as routing, ranking, and verification with Nimble through Ollama. |

For comparisons, see the [decision-model benchmark](../benchmarks/decision-models/). It uses synthetic cases; its scores are not a guarantee for your task. Validation is offline by default, with live inference and hosted billing requiring explicit opt-in.

## Adapting skills and finding the details

Skills live in `workflow/`, `writing/`, and `models/`. Each skill directory contains a `SKILL.md` entry point, a human-facing `README.md`, and any supporting references or scripts. When copying manually, copy the complete skill directory, including its license notices; for example, `workflow/shape-work/`, not the whole `workflow/` folder. Adjust instructions, tools, and checks to suit your project.

Separate standalone copies need deliberate updates; native plugins use their client's catalog/plugin operations. A source merge alone does not refresh installed content. Follow the [update and migration guidance](installation.md) before replacing edits or mixing companion versions.

- **Single-change delivery:** [`work-on` dependencies and runtime requirements](../workflow/work-on/README.md).
- **Multi-task delivery:** [`work-on-spec` requirements](../workflow/work-on-spec/README.md).
- **What has been checked:** [session-workflow coverage and remaining acceptance](validation/session-workflow/README.md), [earlier composable-delivery evidence and limits](validation/composable-acceptance/README.md), and [historical delivery coverage](validation/delivery-coverage/README.md). Historical ownership descriptions are not current installation guidance. The [distribution support matrix](installation.md#support-and-evidence) separates documentation, offline checks, live local installation/update simulations and remaining public-delivery/session checks; recorded Pi/macOS workflow trials do not certify installation routes.
- **Replacing an existing installation:** [approved-target migration runbook](agents/installed-skill-migration.md) and [sandbox migration checks](validation/installed-skill-migration/README.md). The checks do not modify real installations.
