# Work in sessions you can review

Use this guide to choose what you want from your coding agent. You decide what the software should do and which stage to start. The agent chooses routine engineering methods, checks the result, and brings consequential decisions back with a recommendation.

Separate planning, delivery and publication sessions can keep context focused. They are recommendations, not a required pipeline: combine stages when useful, or start with one small change.

## 1. Establish the project agreement

Choose a route using the [installation, update and migration guide](installation.md). Native plugins bundle the full collection once available; standalone/npx copies can be selective and editable. Examples below use standalone names: Claude plugin users use `/agentskills:setup-project`, `/agentskills:work-on` and the same prefix for other skills; Codex's native resolver exposes `agentskills:work-on`, used as `$agentskills:work-on`; interactive selection remains untested. Use the guide's client-specific picker/namespace instructions. Copy complete packages, including references and license notices. Installation supplies instructions, not tools, permissions or compatible companions. Check the [single-change requirements](../workflow/work-on/README.md#install-and-dependencies) and [whole-spec requirements](../workflow/work-on-spec/README.md) before delivery. Whole-spec work needs a writable coding-agent runtime; an inspect-only reviewer cannot replace it.

For a new project, ask:

```text
/setup-project
```

Setup inspects the project, agrees conventions with you, then asks before applying the agreed changes. Existing useful guidance can live in its current files; there is no required template or filename. Project-oriented skills need meaningful guidance about decisions, permitted actions, safety, verification, documentation and continuation. Compatible existing guidance works without running Setup again.

If guidance is missing or conflicts with a newer skill, the agent should name the affected prerequisite and recommend reconciliation, not rewrite permissions or run Setup automatically. Tracker and model details are needed only for those capabilities. A local project can support planning, diagnosis and direct work without a tracker. No model-use policy means no autonomous optional assessments; additional models are not needed for this workflow.

## 2. Agree the plan, then choose an outcome

```text
/shape-work I want people to book places in my classes.
```

Answer questions about users, behavior, scope and trade-offs. The agent investigates discoverable technical facts and asks you to confirm the plan. A confirmed plan completes shaping. It may offer a next step, but creates no spec or tickets and starts no implementation just because you agreed.

Choose what is useful next:

| Desired outcome | Example request | Where it stops |
| --- | --- | --- |
| One bounded change | `/work-on the cancellation change we agreed on` | Implemented result, checks, independent review and a change summary; limitations explicit |
| A lasting specification | `/write-spec the booking plan we agreed on` | In a configured project, published spec and verified link, with a concise summary |
| Tasks from an agreed scope | `/write-tickets for the agreed booking specification` | Actual tickets and a table of linked IDs and short descriptions; exact scope/relationship approvals still apply |
| Draft or local artifact only | `/write-spec a local draft; do not publish it` | Selected draft/local artifact, no tracker writes |

You need not approve unchanged commitments again line by line. New consequential behavior, missing permissions or an unknown publication destination still need resolution. Full published bodies belong in the tracker; publication alone does not establish readiness or satisfy dependencies. Failed or unpublished items must be distinguished from real IDs.

## 3. Deliver from the selected agreement

In a later session, give the agent the spec, issue, saved plan or diagnosis it needs; a new session cannot assume it can see your previous conversation.

```text
/work-on #42
/work-on-spec the booking specification #40
```

Use `work-on` for one bounded change and `work-on-spec` for delivery across a spec's tasks. The agent checks current files, prerequisites and existing evidence rather than repeating settled discovery. A closed blocker is not enough when accepted integration is required. It owns routine method selection and coordination; you should not need to choose test seams or manage workers.

For a small clear request, go directly to `work-on`. A spec or ticket hierarchy is not required merely to edit a small thing. Standalone research, analysis, prototypes and reviews also remain available within their own scope.

Delivery should preserve unrelated work, perform relevant checks and applicable independent Standards/Spec review, and report what is implemented, verified and blocked. Missing material verification prevents an acceptance-ready claim, even when other checks pass. Completion creates no PR or handoff automatically.

## 4. Diagnose bugs, then select repair or tickets

```text
/investigate-bug Cancelling a booking doesn't free up a place.
```

Expect observed behavior, reproduction evidence, cause when established, impact and a bounded fix/check recommendation in conversation. Diagnosis can complete without tracker access. Unconfirmed symptoms or unresolved cause stay investigation-only; investigation alone ships no fix.

From a current complete diagnosis, choose direct work or ticket creation:

```text
/work-on the bounded fix from this diagnosis
/write-tickets for the fix from this diagnosis
```

You can also authorize both responsibilities at once: “Investigate and fix this cancellation bug.” The agent reuses the completed diagnosis for delivery without manufacturing a ticket or asking you to repeat the already-authorized command. Each responsibility retains its own checks and permission limits.

## 5. Try the result before publishing a PR

Read the change summary and limitations, then try the result. Request adjustments while the work is still unpublished:

```text
Please change the cancellation message to include the class name.
```

The agent refreshes affected checks and review rather than restarting unrelated work. When you want a pull request—a proposal to merge the changes—ask explicitly:

```text
/pr Open a pull request for this delivered change.
```

PR preparation/publication reuses current evidence and verifies the actual published state. Report-only requests publish nothing. A branch push is not PR publication, and a PR request is not permission to merge, deploy or release. Missing tools or authority should produce a specific blocked action, not an invented PR link.

## 6. Choose whether to preserve context

Same-session work can finish in conversation. When moving to another session, explicitly select what to save and where:

```text
/handoff Save the cancellation diagnosis for later delivery at the approved destination.
```

Give the next agent the returned artifact and a request for the next task. Handoff preserves context, not permission to continue. Use a durable destination when needed; temporary files can disappear. The receiver inspects current state and reports missing or stale history honestly. Active owners, uncertain operations and spent repair allowances remain safety obligations even without a handoff request.

Authoritative domain maintenance is different from optional session notes. Confirmed authorized meaning changes belong in the project's glossary/context records during the responsible work. ADR creation or changes need explicit agreement and permission; accepted replacements preserve rationale and supersession links. Routine implementation choices do not automatically need ADRs.

## When you are unsure

```text
/what-now
```

The explicitly invoked advisor inspects relevant installed skills and recommends a route. It works before setup and starts no workflow. It is the former `ask-nico` advisor under a new name, not a new execution gateway. Other skills can also offer useful next steps without starting them.

Source merges do not refresh installed copies. Follow the [client-specific update steps and support limits](installation.md); check compatibility and preserve local edits before replacing skills. Installation and migration require their own approval. No workflow shortcut grants destruction, disclosure, spending, installation, merge or release permission.

## Evidence and limits

See the [session-workflow validation map](validation/session-workflow/README.md) for reproducible offline checks, instruction-reading comparisons and behavioral routes that still need observation. Static assertions and fixtures do not certify every agent runtime or prove that an agent follows these boundaries.
