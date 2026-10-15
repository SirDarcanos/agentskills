# Establish or reconcile model-use permission

Use this procedure during explicit setup, including a bounded setup handoff. The [documentation contract](documentation-contract.md) owns document mapping; the target's approved policy owns permission values. Setup authors policy, not assessment runtime procedures. Here, model-use permission means auxiliary assessment services such as Jev, Clef and Nimble, not ordinary skill execution or configured reviewer/implementer agents. Keep that distinction explicit in generated guidance. No model, service, credential, download, installation, or spending operation is part of discovery, application, verification, or rerun.

## 1. Discover authority

Follow AGENTS/CLAUDE and workflow pointers; inspect existing assessment/model guidance and approval records. Map `docs/agents/model-use.md` or a valid existing authoritative equivalent. Preserve its location, custom content, rationale and provenance. Resolve competing authorities before editing; availability, credentials, installed packages, earlier calls and preferences establish no permission.

Inventory auxiliary assessment skills actually available through runtime skill discovery, including Jev, Nimble, Clef variants and other installed assessment packages. Read each candidate's complete entry point and permission/disclosure references before describing its capabilities. Record exact skill names, purpose, local/hosted transport, evidence sent, cost/service implications and supported invocation modes from those sources. Installation is not permission or proof that its service is running or usable. Unknown availability/capability stays unknown; do not probe by calling a model, starting a service or installing anything.

Classify policy as absent, approved none, approved bounded permission, incomplete, conflicting, or unverifiable. Record evidence separately from proposals. Missing permission remains ungranted; missing material limits are ambiguous, not unlimited. Reuse settled facts, asking only consequential gaps. Offer **none** as a useful choice: ordinary engineering needs no decision-model service.

**Done:** the policy home, evidence, current effective restrictions and blocking gaps are identified without effects.

## 2. Propose a checkable agreement

### Ask explicitly about installed assessment skills

In setup's files-and-permissions step, name the discovered assessment skills rather than asking for generic “model-use permission.” Explain in plain language that these are optional consultations for bounded judgments, separate from normal agent work and independent review. For each installed candidate, show its exact name, what it can help with, where evidence goes, and known cost/service implications. State capability gaps honestly and keep the list short enough for this step or a focused follow-up.

Ask the owner to choose **disallowed**, **only when explicitly requested**, or **bounded automatic use** for each candidate (or a clearly named group with identical terms). Offer all-disallowed as a valid choice without presenting it as already settled. Offer automatic use only when the installed package supports policy-authorized invocation; otherwise explain its explicit-only limit. Existing settled choices need no repeat question; newly discovered skills receive no inherited permission.

For example, adapted to the actual inventory and explained implications:

> I found `ask-jev`, `ask-nimble` and `ask-clef`. These optionally send selected task evidence to their assessment models for a bounded judgment; they are separate from ordinary agent work and reviewer agents. For each, should use be disallowed, only on your explicit request, or automatic within agreed limits where supported? You can choose different rules for each. Are there any other actions, tools or services you want to allow, require confirmation for, or prohibit?

Use only names actually discovered and include other installed assessment skills, not just those example brands. If none are available, say so without proposing installation; if discovery is unavailable, report that limitation instead of claiming none exist. Still invite other permissions or prohibitions. Keep existing binding restrictions visible when proposing a change.

Ask that open-ended permissions question once even when the owner declines all assessments. Clarify the exact scope and consequences of any additional allowance/disallowance, map ordinary workflow decisions to workflow guidance and assessment decisions to the model-policy home, and retain unresolved items as ungranted. Broad answers such as “yes, use them” are preferences to refine, not unlimited authorization. Collect technical facts from installed package evidence; propose concrete limits and ask only the remaining consequential decisions in short follow-ups.

### Resolve the selected agreement

Present the exact policy delta and entry-point/workflow pointers in this step and retain them in the cumulative plan for final execution approval. For explicit-request-only routes, record no automatic permission and the package's per-request gate and restrictions; an explicit request still needs its bounded assessment contract. For each automatic route, resolve the following record before it becomes effective; use explicit none/not-applicable where appropriate rather than empty fields:

| Field | Required decision |
| --- | --- |
| Mode and identity | None, or exact assessment skill, variant/model identifier, provider/service, transport and endpoint. Local-only is an endpoint/disclosure restriction, not permission for every local model. |
| Purpose | Permitted questions/tasks and autonomous versus explicit-only use. Deterministic facts/checks and independent review remain ordinary engineering responsibilities; outputs are advisory. |
| Data and retention | Permitted evidence classes, sensitive/private exclusions, minimum disclosure, and whether/where payloads/results may be retained. Local permission never implies hosted disclosure. Store no credentials. |
| Shared limits | Finite attempted-request, transport-retry, evidence-correction and spending limits, currency, scope (for example one work unit or whole spec), expiry/reset authority, and any narrower per-assessment allocation. Count failed/unknown-charge attempts and batches; package ceilings also apply, whichever is stricter. |
| Delegation accounting | Root owner and shared ledger location under retention rules; reserve before sending, reconcile actual usage, workers request allocations. Handoffs, new sessions, retries and resume preserve consumed/reserved allowance; no child budget reset. Unknown paid cost blocks sending unless a safe allowed reservation can be established. |
| Service lifecycle | Exact service startup authority or reuse-only, owned process handle, shutdown owner/disposition. Reused services remain untouched. Installation/downloads and credential changes require separate approval even if startup is permitted. |
| Fallback | Direct agent-only assessment allowed or offer-and-wait; named alternative skill/model/endpoint if approved, otherwise none. Each alternative needs its own purpose/data/budget authority and distinct invocation. Unavailability never implies substitution. |
| Escalation | Action on denial, missing facts, exhaustion, unavailable service or insufficient data: ordinary engineering where sufficient, otherwise bounded gap/blocker and required approval owner. Valid insufficient-data is not a retry-until-green trigger. |
| Rationale and provenance | Why these permissions/limits fit the project; approving authority, date or durable approval reference, exact approved scope and any expiry. A draft is not approval. Preserve existing provenance on unchanged decisions. |

For **none**, state zero authorized auxiliary assessment requests/retries/spend, no assessment-service startup/substitution, ordinary-engineering fallback, scope, rationale and provenance. Ordinary agent work, bounded delegation and lead-owned review/repair remain governed by workflow authority, not disabled by this choice. Identify remaining installation/disclosure restrictions and how a future change receives approval; per-model fields are not applicable.

Explain invocation semantics in the target's guidance: autonomous consultation needs unambiguous approved permission and remaining shared allowance; a compatible assessment package can then act without repeated confirmation. Explicit user assessment authorizes only that named bounded package assessment within applicable restrictions, not other services, broader disclosure or installation. An explicit project prohibition still requires resolution with its authorized owner. For explicit requests, direct fallback remains offer-and-wait unless already authorized. Runtime restrictions and the current package's invocation gate also apply: a policy cannot enable a package that still requires explicit invocation.

**Done:** none or every allowed route has resolved material facts; unresolved routes are blocked, and the exact proposed docs are approved before writing. Setup approval to write a policy is not approval to exercise it.

## 3. Apply the approved document delta

Re-read affected sources and authorization. Use targeted edits, preserving existing equivalents, symlinks, rationale and approvals. Mark unresolved proposals as drafts with no new effective permission; useful independent documents may proceed only within separately approved scope. Link the single policy home from the target entry point and workflow with a condition to read before proposing/using model assessments, service lifecycle actions, or changing model permission.

Keep provider/runtime enforcement with each assessment package. Target guidance assigns the lead policy-fit/budget reservation check and the assessment owner's immediate pre-send authority/payload/transport/limit check; it does not duplicate package API procedures or introduce a gateway. Policy publication alone proves neither runtime compatibility nor enforcement.

**Done:** actual policy values/pointers match the approved delta, unrelated material survives, and per-operation outcomes identify any blocked writes.

## 4. Read back and rerun

Inspect resulting files, approval provenance and links. Compare every allowed identity, purpose, disclosure, shared limit, lifecycle and fallback against the plan. Confirm none/unknown/conflicting routes imply zero automatic calls; checks stay offline. Re-inspect as a rerun: unchanged facts produce no rewrite, timestamp churn, renewed permission, budget reset or service action. Changed permissions require an exact newly approved delta; a missing pointer may be repaired without relocating or broadening the existing policy.

Return policy source, proposed/applied/preserved decisions, approval evidence, verified pointers, gaps and **complete**, **partial**, or **blocked** status. Stop at operating guidance; no assessment, application delivery or installation follows automatically.

**Done:** approved required document operations are read back or individually blocked, and all model/service effects remain zero.
