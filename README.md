# Agent Skills

[![skills.sh](https://skills.sh/b/SirDarcanos/agentskills)](https://skills.sh/SirDarcanos/agentskills)

Reusable skills for coding agents. This repository collects skills that I use in my own workflows and share for others to adapt.

## Skills

### General skills

| Skill | When to use it |
| --- | --- |
| [`ask-clef`](ask-clef/) | Explicitly request an evidence-backed local Clef judgment over text or images. |
| [`ask-clef-flash`](ask-clef-flash/) | Explicitly request an evidence-backed local Clef Flash judgment over text or images. |
| [`ask-jev`](ask-jev/) | Explicitly request an evidence-backed hosted Jev judgment and interpretation, with confirmation only for exceptional scope. |
| [`ask-nimble`](ask-nimble/) | Explicitly request an evidence-backed local Nimble judgment, with direct answers for unsuitable questions. |
| [`build-with-nimble`](build-with-nimble/) | Build applications with Nimble's composable decisions through local or self-hosted Ollama. |
| [`create-changelog`](create-changelog/) | Create a project's first `CHANGELOG.md` from repository evidence and Semantic Versioning history. |
| [`domain-modeling`](domain-modeling/) | Establish or revise domain vocabulary, context maps, and ADRs directly or through another workflow. |
| [`github-repo-setup`](github-repo-setup/) | Create or configure a GitHub repository through an approved standalone plan or project-setup handoff. |
| [`implementation-preflight`](implementation-preflight/) | Select or create the correct Git branch and PR target before an implementation workflow begins. |
| [`review-delivery`](review-delivery/) | Independently review Standards and Spec against the actual delivered scope, including dirty work, with pinned evidence and stale-review detection. |
| [`setup-project`](setup-project/) | Establish project-aware agent instructions, operating context, domain records, and approved GitHub tracker configuration. |
| [`slop-guard`](slop-guard/) | Audit, rewrite, or draft human-facing prose while preserving facts, meaning, and the writer's voice. |
| [`stay-positive`](stay-positive/) | Reframe prose constructively without forcing optimism or weakening necessary negativity. |
| [`update-changelog`](update-changelog/) | Maintain an existing changelog after notable changes, during release preparation, or when correcting release history. |
| [`work-on`](work-on/) | Explicitly start or resume delivery with context-aware routing, product agreement, technical planning, native ticket graphs, direct building, integrated verification, bounded repair/completion, multi-ticket dispatch/integration and safe interruption/failure recovery. |

## Repository layout

Each skill lives in its own directory and uses `SKILL.md` as its entry point:

```text
skill-name/
├── SKILL.md
├── README.md
├── references/    # Optional supporting material
└── scripts/       # Optional automation
```

A skill's `SKILL.md` explains when to use the skill and gives the agent its working instructions. Its `README.md` provides a human-facing overview. Supporting files stay beside the skill so it can be copied as one unit.

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

Install `work-on` for explicitly requested delivery and `review-delivery` for the independent acceptance-review gate. Follow their package READMEs for installation examples and conditional companions: `implementation-preflight` for Git building, `domain-modeling` for meaning/ADR changes, and the discovered `setup-project` tracker library for GitHub graph work. Reading that library does not invoke setup. Copy complete directories and their notices; companions use semantic discovery, not sibling paths. Missing tools, compatible companions or review authority block the affected route rather than prompting automatic installation or legacy-command fallback.

[Delivery coverage and installation checks](docs/validation/delivery-coverage/README.md) maps #14's criteria to shipped procedures, executed trials and remaining gaps. Observed Pi/macOS trials are not cross-runtime certification, installed slash-command tests or proof of live tracker mutation. Installation examples have not been executed here; repository merges do not refresh separately copied skills.

## Comparing decision models

[The shared decision-model benchmark](benchmarks/decision-models/) contains 100 synthetic cases with 120 known-label questions for Nimble, Clef, Clef Flash, and Jev. It reports category-level correctness and separates model mismatches from API failures. Validation is offline by default; live inference, hosted billing, and retained records require explicit opt-in.

## Adapting skills

Treat these skills as starting points. Update paths, tools, commands, and completion checks to match your environment. Keep related references and scripts with the skill when copying it.
