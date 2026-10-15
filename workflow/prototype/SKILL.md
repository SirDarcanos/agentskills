---
name: prototype
description: Answer a bounded design, UX, state-model or feasibility question with a runnable experiment. Use for prototype-first requests or authorized method handoffs, before committing to production implementation.
---

# Prototype

Own the experiment and learning, not production delivery. Use directly for a matching request or inline through an authorized bounded handoff. Read [validation](references/validation.md) when changing or validating this package.

## 1. Establish the question and authority

Read applicable target instructions, agreement/acceptance references, relevant code/callers, existing findings and environment. Inspect supplied evidence against current deciding inputs, including dirty files; reuse current observations and reassess only material gaps or changed dependencies. Record source revisions or content identities. A direct request may supply the same facts through context rather than a formal handoff.

State one deciding question and what observation would support or reject each option. Distinguish design/state behavior, human UX judgment and technical feasibility: a script can observe transitions or constraints, but cannot establish user preference. Keep settled product decisions and exclusions intact. Resolve consequential intent or permission gaps with their owner; routine experiment choices belong to the technical lead. Standalone execution acts as its own bounded lead.

Inspect actual work and ownership before writes. Identify owned artifact locations, protected files, approved read/write/run effects, data/disclosure and retention constraints, and expected return. A request for exploration grants no production promotion, installation, delegation, service startup, spending, destructive cleanup, merge or release permission. Unknown authority remains ungranted; plan-only authority returns an experiment plan.

Discover conditional companions through the runtime catalog or an explicit approved package location, not sibling paths. Read the complete candidate entry and relevant references, record source/revision or digest, and check semantic capability. Ambiguous or incompatible helpers block the dependent route; installation is not a fallback.

- Before Git writes, use compatible `implementation-preflight`, or inspect a current caller-supplied result for this scope/state. Outside Git, retain a before/after artifact manifest.
- Required domain meanings or qualifying decision-record changes use the discovered `domain-modeling` owner; reading existing definitions needs no invocation.
- Delegation or correction of recorded acceptance findings consumes the discovered `work-on` execution/repair contract as a read-only library, without invoking delivery. Retain root ownership, ledger, limits and finding lineage; workers request extra work from the root. Missing contract blocks that route, not an ordinary direct experiment.

**Complete when:** one question, deciding evidence, ownership, authority and required dependencies are known; otherwise return a plan or affected-route blocker with protected work intact.

## 2. Bound the experiment

Choose the smallest runnable artifact that can distinguish the options: a transition harness for state behavior, a local interactive mock for UX, or a focused probe for technical feasibility. Follow target conventions; no universal HTML format, UI variant count or adjacent production route is required. Mark the artifact as a prototype in its name and visible description.

Before execution, record:

- Hypothesis/options, observable success/rejection criteria and what remains unknowable from this experiment.
- Finite bounds: explicit case/variant count, iteration count and execution timeout or end time; resource/cost ceiling when applicable. Stop at the first of question answered or bound reached. Extending bounds requires an explicitly approved revised plan, not an automatic new loop.
- Run command/environment, inputs and expected observations, relevant baseline/comparison, necessary instrumentation and safe failure handling.
- Owned files/processes/data and planned disposition: retain, export learning, or remove only specifically authorized owned artifacts. Default to preserving useful artifacts pending a disposition decision. No implicit commit or tracker publication.

Use synthetic/local data where adequate and permitted. Persistence, external services, real user data or participant studies require their specific authority. Reused services and existing data remain untouched. Missing tooling or unsafe execution returns a gap rather than triggering installation. For interactive work, identify who will observe which tasks; unavailable user feedback limits the UX conclusion.

**Complete when:** the experiment has a runnable plan, distinguishing observations, explicit finite limits, safe inputs and an authority-compatible disposition.

## 3. Build, execute and observe

Build only enough to run the planned cases, with instrumentation and safety checks needed for trustworthy observations. Keep experimental artifacts separate from production entry points unless that exact temporary integration is authorized. Record intentional simplifications rather than disguising them as completed production behavior.

Execute the run command and inspect raw output or actual interactions. Record case/input, expected versus actual observation, failures, environment, elapsed time and checked artifact/source identities. For UX, distinguish direct interaction, participant feedback and untested visual assumptions; rendering alone does not establish usability. Authored scenarios, compilation or artifact creation alone are not executed evidence answering the question.

Change one relevant assumption/variant at a time within the declared iteration limit. Reuse unaffected evidence; refresh observations dependent on changed inputs. Stop when evidence answers the question, a bound is reached, authority becomes unsafe, or a required capability is missing. Harness/environment failures are not evidence against the hypothesis. Preserve partial work and raw failures instead of widening exploration or pursuing a preferred answer until it passes.

**Complete when:** the bounded cases have actual observations, or an explicit partial/blocked result identifies the unrun cases and stopping reason.

## 4. Interpret and account for artifacts

Compare observations to the predeclared criteria. Return **supported**, **rejected** or **inconclusive** for the question, with evidence and scope of confidence. Contradictory, insufficient, wrong-environment or bound-limited results remain inconclusive; recommend the smallest next evidence action without executing another method. Separate observed facts from assumptions and recommendations.

List production-readiness limitations concretely: omitted integrations, error/security/access paths, persistence/recovery, performance conditions, accessibility or real-user checks as relevant. Successful prototype behavior proves only the tested experiment. Promotion requires a separately authorized production scope and appropriate checks; neither copying code nor a favorable recommendation establishes production acceptance.

Apply only the approved artifact disposition. Preserve useful runnable artifacts and raw learning at an approved location, with run instructions and non-production marking. Commit/export/publish only within target authority. Before cleanup, compare the owned manifest to actual bytes/modes/link targets and intervening edits; uncertainty or conflicting changes blocks deletion. Remove only specifically authorized artifacts/processes created by this experiment; removing a symlink must leave its shared target intact. Record retained, removed, protected and unresolved items. Broad reset/clean operations are not prototype cleanup. Keep evidence needed to explain the result even if scratch artifacts are removed.

**Complete when:** the conclusion and recommendation trace to observations, production limitations are explicit, and every owned artifact/process has an actual or blocked disposition without unrelated cleanup.

## 5. Return and stop

Inspect the scoped diff/manifest and protected work. Update owned documentation/changelog under target policy or justify no change. Return **complete**, **partial** or **blocked** separately from the question's conclusion: a completed bounded experiment may legitimately be inconclusive.

Include question/agreement references and exclusions; bounds planned/spent and stopping reason; commands/interactions, actual observations, environment and source/artifact identities; reused/stale/failed/not-run evidence; conclusion, recommendation, uncertainty and production-readiness limitations; artifact manifest/disposition, companion resolutions, branch/base/PR target or non-Git state, protected work and documentation disposition. Retain the shared ledger and finding lineage when applicable.

**Method completion:** the bounded experiment has an honest evidence-backed result and artifact account, or preserved partial/blocking work. Return to the caller with a recommended next action; do not recursively launch analysis, another method, production implementation, a PR or delivery acceptance. The caller chooses any subsequent handoff and refreshes only affected readiness.
