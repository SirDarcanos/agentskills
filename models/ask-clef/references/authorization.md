# Authorization and shared limits

Read before any transport (including availability probes) or server operation, and recheck immediately before every decision request. The target's approved policy owns permission values; this package owns their application. These are agent instructions, not a mandatory model gateway.

## 1. Identify authority and scope

For autonomous use, inspect the target's `AGENTS.md` policy pointer: default home `docs/agents/model-use.md`, or its existing authoritative equivalent. Verify approval provenance, current revision, scope/expiry and conflicts with operating/runtime restrictions. A draft, available credential, installed model, caller preference or model recommendation grants nothing.

Require an unambiguous match for **ask-clef**, Ollama **clef**, and **http://127.0.0.1:11434/v1/systemone**, the bounded purpose, and disclosure of the actual submitted data. Model tags/digests must match any policy pin; record the installed digest after authorized discovery. Other variants, endpoints and transports are not aliases. Missing, none, denied, ambiguous, conflicting or expired permission returns **no-call**, with zero transport/server effects. Do not automatically prompt to opt in; ordinary delivery can continue without a model.

An explicit user request authorizes this named bounded assessment, not unrestricted use. Check applicable project prohibitions, disclosure restrictions and shared limits; resolve conflicts with their authorized owner. An absent autonomous policy alone does not prevent a compatible explicit assessment. Startup, installation/downloads, retained records and alternative models are separate permissions.

For explicit standalone use without stricter project limits, the package allowance is one initial request plus at most one evidence-corrected request, no automatic transport retries, and no billable service use. This does not authorize dependent extra requests; obtain a finite expanded request allocation for those before sending. Autonomous policy limits still must be explicit and finite.

A standalone caller owns its bounded allowance. A handoff supplies question/criteria, deciding evidence/revisions, exact approval and policy source, protected work, root ledger/reservation pointer, lifecycle owner and expected return. Inspect those facts rather than trusting an “authorized” label. Reuse current complete evidence; stale deciding inputs require targeted refresh, not another automatic consultation.

**Done:** authority source, exact identity, scope, disclosure and restrictions are established, or a no-call outcome is returned before effects.

## 2. Reserve the shared allowance

The lead checks policy fit and reserves from the root run's ledger before handoff; the assessment owner rechecks it before sending. Standalone use acts as its own root. Keep the ledger in the target's approved retention location or conversation, not automatically in a public repository. No new delivery companion is required for a direct assessment.

Record finite call/retry/correction/spending limits, their shared scope, spent and outstanding reservations, owner, approval source and expiry/reset authority. Missing material limits are not unlimited. Apply the stricter policy/allocation/package ceiling:
- At most four questions per request; a batch is one attempted request, not four fresh budgets.
- At most one evidence-corrected request across stale/misrepresented evidence for the entire assessment.
- No automatic transport or malformed-response retries. This package reports the failure and follows fallback; a policy cannot enlarge that ceiling.
- Any dependent follow-up request requires remaining shared allowance and a finite assessment bound agreed before sending; never build an unbounded decision loop.

Reserve each attempted send before dispatch, including the corrected request. Count failed, timed-out and unknown-outcome sends; do not refund them because no verdict arrived. Reconcile actual usage and release only confirmed unused reservations. Local cost may be explicitly zero, not silently assumed; if an allowed worst-case spending reservation cannot be established, block the send. Probes/startup are permitted effects, not fresh inference budgets.

Workers obtain allocations from the root rather than creating a budget. Handoffs, variant changes, new sessions and resume preserve spent/outstanding use. Uncertain previous sends remain charged until reconciled. Exhausted/ambiguous reservations return no-call. Re-read changed policy/authority/payload immediately before transport; a valid earlier reservation cannot override revoked permission.

**Done:** the exact next request has an exclusive safe reservation, or no send occurs and the blocker is returned.

## 3. Lifecycle and fallback

Only after suitability and authority pass may the [API lifecycle](ollama-api.md#server-lifecycle) probe or reuse the local service. Reused servers remain unowned and untouched. Autonomous startup requires policy authority for the exact loopback Ollama service and assigned start/cleanup ownership; denied startup returns unavailable without launching anything. Explicit use may ask for invocation-specific startup permission. Installation, upgrades and downloads need their own explicit approval; never run them as recovery effects.

Record the tracked handle and verified ownership. Follow the approved stop/leave-running disposition for owned processes, including call/readiness failure; absent disposition means ask and report pending state. Stop only the verified owned handle, never another session's service. Passing ownership between callers needs an acknowledged transfer, not a guessed PID.

For an unavailable service/model/endpoint or invalid response:
- Autonomous use performs direct agent assessment only if the configured fallback permits it. Otherwise return unavailable; the lead may continue ordinary engineering but cannot claim a substitute model result.
- Explicit use offers and waits for direct fallback unless the user already authorized it.
- Label direct results **Agent assessment — named model unavailable**, with sources, assumptions and gaps; no fabricated model verdict/probabilities.
- Default model substitution is none. If a policy explicitly names an alternative, return its authorized option to the lead, which discovers its separate package through the runtime catalog or approved location (not sibling paths), reads the complete entry/relevant references and checks semantic compatibility and remaining shared allowance. Missing/ambiguous/incompatible alternatives block only that route. This package never switches its own model or transport. Local authority never implies hosted disclosure.

A valid insufficient-data answer is not unavailability. Preserve the evidence gap and smallest useful next evidence action; do not retry or substitute for a preferred verdict. All results remain advisory, never deterministic proof, independent review or authority for implementation/policy changes.

**Done:** validated advisory output or no-call/unavailable/gap is returned with actual usage, fallback disposition and owned-service status; no downstream work starts automatically.
