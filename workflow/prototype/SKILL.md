---
name: prototype
description: Answer a bounded design, UX, state-model or feasibility question with a runnable experiment. Use for prototype-first requests or authorized method handoffs, before committing to production implementation.
---

# Prototype

Own the experiment and learning, not production delivery. Use directly for a matching request or inline through an authorized bounded handoff. Read [validation](references/validation.md) when changing or validating this package.

## 1. Establish the question

Reuse applicable project guidance and relevant context/authority pointers once per context, including directory/runtime restrictions. Check decision/effect authority, safety, verification/review, documentation and continuation responsibilities. Direct and bounded use accept equivalent layouts. Missing/conflicting common guidance blocks dependent work: name the gap and recommend explicit setup/reconciliation without starting it or inventing policy. Conditional gaps block only that capability.

State one deciding question and what observation would support or reject each option. Inspect relevant code/callers, environment and supplied findings against current deciding inputs, including dirty content; reuse current observations. Distinguish state behavior, human UX judgment and feasibility: a script cannot establish user preference. Keep settled decisions and exclusions; the caller chooses routine experiment details.

Identify owned artifact locations, protected work and permitted run/data effects. Exploration is not authority to promote code to production. Plan-only requests return an experiment plan.

Use compatible `implementation-preflight` before Git writes, or inspect a current supplied result for the same scope/state; outside Git retain a before/after manifest. Actual meaning/decision-record changes use discovered `domain-modeling`; reading definitions alone needs no invocation. Missing/incompatible companions block their dependent route.

Only delegated work or recorded acceptance correction loads Work On's documented conditional coordination/repair library, without invoking delivery. Retain root ownership/bounds and checkpoint/lineage/spent cycles; method switches/resume reset nothing. An old universal-contract-only package blocks that route, not ordinary development.

**Complete when:** question, ownership, deciding evidence and experiment authority are actionable, or specific affected blockers preserve work.

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

Return the question and scope; bounds planned/spent and stopping reason; commands/interactions, observations and checked identities; failed/unrun/stale evidence; conclusion, uncertainty and production limitations; artifact disposition, protected-work comparison and documentation outcome. Reuse current task/preflight context, not a reconstructed lead record. Include existing coordination/repair state only when applicable.

**Method completion:** the bounded experiment has an honest evidence-backed result and artifact account, or preserved partial/blocking work. Return to the caller with a recommended next action; do not recursively launch analysis, another method, production implementation, a PR or delivery acceptance. The caller chooses any subsequent handoff and refreshes only affected readiness.
