# Agent Skills

[![skills.sh](https://skills.sh/b/SirDarcanos/agentskills)](https://skills.sh/SirDarcanos/agentskills)

Reusable skills for coding agents. This repository collects skills that I use in my own workflows and share for others to adapt.

## Skills

### Workflow

| Skill | When to use it |
| --- | --- |
| [`acceptance-first`](workflow/acceptance-first/) | Implement agreed workflows from executable observable examples and return criterion-level evidence with explicit intent/environment gaps. |
| [`analyze`](workflow/analyze/) | Assess technical readiness from codebase evidence, reuse current findings and recommend proportionate methods/checks without implementation. |
| [`build-and-check`](workflow/build-and-check/) | Implement small increments with immediate relevant checks, existing coverage reuse and proportionate documentation/configuration validation. |
| [`characterize`](workflow/characterize/) | Protect relevant legacy behavior before risky changes, with baseline provenance and separate intent, unknown and defect evidence. |
| [`domain-modeling`](workflow/domain-modeling/) | Establish or revise domain vocabulary, context maps, and ADRs directly or through another workflow. |
| [`github-repo-setup`](workflow/github-repo-setup/) | Create or configure a GitHub repository through an approved standalone plan or project-setup handoff. |
| [`implementation-preflight`](workflow/implementation-preflight/) | Select or create the correct Git branch and PR target before an implementation workflow begins. |
| [`investigate-bug`](workflow/investigate-bug/) | Confirm defects and cause, then prepare or reconcile workable tickets; investigation-only stops before repair. |
| [`pr`](workflow/pr/) | Prepare plain-language PR reports with traceable test/CI impact, risks and reversal limits, and open/update only authorized PRs. |
| [`prototype`](workflow/prototype/) | Answer bounded design, UX, state-model or feasibility questions with runnable experiments, explicit limitations and artifact disposition. |
| [`research`](workflow/research/) | Investigate bounded questions directly or through authorized delegation, with cited sources, freshness checks and explicit uncertainty. |
| [`review-delivery`](workflow/review-delivery/) | Review standalone or bounded specialist handoffs with independent Standards/Spec contexts, full committed/dirty scope and revision-aware evidence. |
| [`setup-project`](workflow/setup-project/) | Establish project-aware agent instructions, operating context, approved model-use policy, domain records, and GitHub tracker configuration. |
| [`shape-work`](workflow/shape-work/) | Shape unresolved ideas into usable agreements in project terms, with evidence reuse, manageable rounds and preserved concern dispositions. |
| [`tdd`](workflow/tdd/) | Implement bounded test-first changes with behavioral red–green–refactor, coverage reuse and local evidence. |
| [`work-on-spec`](workflow/work-on-spec/) | Coordinate overall spec delivery through bounded Work On ticket agents, native dependencies, exclusive ownership, serial integration, aggregate verification/review and recovery. |
| [`work-on`](workflow/work-on/) | Deliver or resume one bounded change as technical lead, reusing current evidence and composing methods, verification, independent review, bounded repairs and PR handoff. |
| [`write-spec`](workflow/write-spec/) | Express agreed behavior with stable acceptance IDs, preserve decisions and publish only with separate authority and role/readiness read-back. |
| [`write-tickets`](workflow/write-tickets/) | Decompose agreed work or publish ready bug evidence with exact approval and verified native dependencies; stop before scheduling. |

### Writing

| Skill | When to use it |
| --- | --- |
| [`create-changelog`](writing/create-changelog/) | Create a project's first `CHANGELOG.md` from repository evidence and Semantic Versioning history. |
| [`slop-guard`](writing/slop-guard/) | Audit, rewrite, or draft human-facing prose while preserving facts, meaning, and the writer's voice. |
| [`stay-positive`](writing/stay-positive/) | Reframe prose constructively without forcing optimism or weakening necessary negativity. |
| [`update-changelog`](writing/update-changelog/) | Maintain an existing changelog after notable changes, during release preparation, or when correcting release history. |

### Models

| Skill | When to use it |
| --- | --- |
| [`ask-clef-flash`](models/ask-clef-flash/) | Request or policy-authorize a bounded evidence-backed local Clef Flash judgment over text or images. |
| [`ask-clef`](models/ask-clef/) | Request or policy-authorize a bounded evidence-backed local Clef judgment over text or images. |
| [`ask-jev`](models/ask-jev/) | Assess an evidence-backed question with hosted Jev by explicit request or exact approved project policy, within shared disclosure and spending limits. |
| [`ask-nimble`](models/ask-nimble/) | Request or policy-authorize a bounded evidence-backed local Nimble judgment, with direct answers for unsuitable questions. |
| [`build-with-nimble`](models/build-with-nimble/) | Build applications with Nimble's composable decisions through local or self-hosted Ollama. |

## Repository layout

Skills are grouped by purpose in `workflow/`, `writing/`, and `models/`. Workflow covers discovery, planning, setup, implementation methods, and delivery—not only coding. Each skill remains an independent package with `SKILL.md` as its entry point:

```text
workflow/    # Discovery, planning, setup, methods, and delivery
writing/     # Prose and changelogs
models/      # Model assessments and integrations
```

```text
skill-name/
├── SKILL.md
├── README.md
├── references/    # Optional supporting material
└── scripts/       # Optional automation
```

A skill's `SKILL.md` explains when to use the skill and gives the agent its working instructions. Its `README.md` provides a human-facing overview. Supporting files stay beside the skill so it can be copied as one unit. For example, copy `workflow/shape-work/`, not the whole `workflow/` folder. Skill names and name-based CLI selection are unchanged; manual source paths now include the group. Existing installed copies are not moved or refreshed by this reorganization.

## Using a skill

Install the skills with the `skills` CLI:

```bash
npx skills add SirDarcanos/agentskills
```

To install a specific skill for Claude Code and Pi:

```bash
npx skills add SirDarcanos/agentskills --skill github-repo-setup --agent claude-code pi
```

You can also clone the repository and copy or link a skill directory into the discovery path used by your coding agent:

```bash
git clone https://github.com/SirDarcanos/agentskills.git
```

Review a skill before enabling it because instructions and tool assumptions can differ between agent runtimes.

### Delivery workflow

Use `investigate-bug` for a reported defect lacking ready evidence. It uses discovered `write-tickets` for approved publication/reconciliation and stops there; a later authorized delivery consumes current evidence. Work On accepts an explicit delivery request or a bounded authorized lead/investigation-and-fix handoff; investigation-only still grants no fix authority. Use `work-on-spec` for explicitly requested whole-spec delivery through bounded Work On ticket agents. It owns scheduling, serial integration, aggregate acceptance and overall recovery under Work On's shared execution ledger; missing compatible writable worker runtime blocks multi-ticket execution, not graph inspection/planning. Work On keeps only dispatch compatibility pointers, never an old scheduler fallback.

Install `work-on` for single-change delivery and `review-delivery` for the independent acceptance-review gate. Follow their package READMEs for installation examples and conditional companions: `shape-work` for unresolved product intent, `write-spec` for specification writing or authorized publication, `analyze` for missing or changed technical readiness, `write-tickets` for decomposition or ticket/graph reconciliation, `implementation-preflight` for Git building, `tdd` when selecting test-first development, `prototype` when selecting a bounded experiment, `characterize` before selected risky legacy changes, `acceptance-first` when selecting executable workflow examples first, `build-and-check` when selecting small implementation-first increments, `domain-modeling` for meaning/ADR changes, `pr` for PR reports and authorized opening/updating, and the discovered `setup-project` tracker library for GitHub graph work. Reading that library does not invoke setup. Copy complete directories and their notices; companions use semantic discovery, not sibling paths. Stage only the companions needed by the intended routes: a selected method need not bring every other method, ordinary research needs no delivery coordinator or model, and spec drafting needs no tracker. For whole-spec execution, install `work-on-spec` with compatible `work-on` and the companions required by its selected ticket/acceptance routes. Check actual resolved sources and duplicate names before use; an older same-name installation is not automatically compatible. Missing tools, compatible companions or review authority block the affected route rather than prompting automatic installation or legacy-command fallback.

[Composable delivery acceptance](docs/validation/composable-acceptance/README.md) maps #48's AC1–AC16 to current package checks, three integrated trials and remaining obligations. [Earlier delivery coverage](docs/validation/delivery-coverage/README.md) preserves #14's historical evidence; its pre-extraction ownership descriptions are not current installation guidance. Observed Pi/macOS trials and non-sibling structural catalog checks are not cross-runtime certification, installed slash-command tests or proof of live tracker mutation. Installation CLI examples have not been executed here; repository merges do not refresh separately copied skills. For replacing existing installations, use the [approved-target migration runbook](docs/agents/installed-skill-migration.md) and its private backup/rollback record; [sandbox migration checks](docs/validation/installed-skill-migration/README.md) do not change real installations.

## Comparing decision models

[The shared decision-model benchmark](benchmarks/decision-models/) contains 100 synthetic cases with 120 known-label questions for Nimble, Clef, Clef Flash, and Jev. It reports category-level correctness and separates model mismatches from API failures. Validation is offline by default; live inference, hosted billing, and retained records require explicit opt-in.

## Adapting skills

Treat these skills as starting points. Update paths, tools, commands, and completion checks to match your environment. Keep related references and scripts with the skill when copying it.
