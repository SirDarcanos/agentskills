# Authorization and shared hosted limits

Read before checking credentials or making any authenticated operation; recheck immediately before every send. The target's approved policy owns permission values. This package owns named-provider enforcement, not a policy parser or mandatory gateway.

## 1. Identify authority

For autonomous consultation, follow the target's `AGENTS.md` pointer to `docs/agents/model-use.md` or its existing authoritative equivalent. Inspect approval provenance, current revision, purpose, scope/expiry and conflicts with project/runtime restrictions. Require an exact match for **ask-jev**, **TypeSafe hosted Jev**, **POST https://api.typesafe.ai/v1/systemone**, the permitted requested model ID/alias, and disclosure of the actual evidence classes. A policy pin requires that version; permission for `jev-latest` must explicitly allow its moving resolution. Never infer hosted permission from a local model grant.

Absent, none, draft, denied, conflicting, expired or materially incomplete authority returns **no-call** before credential access or authenticated probes. Credentials, discovery, generated command text and model recommendations grant nothing. Do not prompt automatically to opt in; ordinary engineering continues where sufficient, otherwise report a material evidence gap.

An explicit user request, including a user-originated Pi-expanded skill block, authorizes the named normal billable assessment under package bounds and applicable restrictions. Absent autonomous policy alone does not block explicit use; an explicit project prohibition does. Resolve conflicts with the authorized policy owner before sending. Explicit use does not authorize another recipient/model, expanded sensitive disclosure, installations, credential changes or retained records.

A bounded handoff identifies question/criterion, deciding evidence/revisions, exact policy/approval source, root ledger and exclusive allocation, protected work and expected return. Inspect these facts rather than trusting an “authorized” label. Follow-ups and resume retain scope and spent allowance. Standalone use owns its own bounded root; no delivery companion is required.

**Done:** exact identity, purpose, payload disclosure and applicable authority are established, or zero authenticated effects and a no-call outcome are recorded.

## 2. Reserve calls and spending

The lead checks policy fit and reserves shared allowance before handoff. The assessment owner independently rechecks immediately before each attempt, including retries and correction. Keep the root ledger in the conversation or the target's approved private retention location, not automatically in a public repository.

Record finite attempted-request, retry, correction and spending limits, currency, scope, expiry/reset authority, owner, approval source, spent use and outstanding reservations. Autonomous permission needs all material limits; missing values are not unlimited. Apply the stricter project/allocation/package bound:

- One initial logical request and at most one evidence-corrected logical request per assessment; at most four questions per request.
- At most two retries, only for explicit HTTP 429/529, per logical request; at most six attempted sends for the whole assessment. A batch does not multiply this allowance.
- One shared correction across stale/misrepresented evidence; no retry of malformed responses, ambiguous network failures or unwanted verdicts.
- Package ceilings are not enlarged by policy. Extra experiments or dependent requests need a separately approved bounded assessment, still charged to remaining root allowance.

Before a paid attempt, establish a conservative worst-case cost bound using verified current pricing, the exact model and enforced request token limits (including all questions and billed overhead). Record the pricing source and assumptions. If exact token counting is unavailable, use a verified maximum billable request bound; byte length or a guessed token estimate is insufficient. Unknown pricing or an unsafe reservation blocks sending, including explicit use. The explicit normal allowance covers the bounded package attempts at verified pricing; it is not unlimited spend. Stricter project spending caps always apply.

Reserve the next attempt exclusively from remaining calls/spend, subtracting others' outstanding reservations. Before dispatch, record attempted use; failed, timed-out and unknown-charge attempts count. Keep worst-case spending charged for unknown usage until reconciled; unknown is not zero. Record service-reported tokens separately from estimated cost. Release only confirmed unused reservations or verified excess, never an attempted call slot. If safe reconciliation is impossible, retain the conservative charge and report it.

Workers request allocations from the root. Parent/child handoffs, changed variants, new sessions, follow-ups and resumed work never reset use. Unknown previous operations retain reservations until inspected. Recheck changed permission, payload, pricing and remaining allowance before every send; earlier approval cannot override revocation or expanded disclosure. Exhaustion blocks the affected send without recurring approval requests inside valid bounds.

**Done:** the exact next attempt has an exclusive safe call/spend reservation under current authority, or no send occurs and the blocker is returned.

## 3. Unavailability and fallback

Missing credentials, unavailable contracts/service/model or invalid responses return **unavailable**, not a fabricated Jev decision. No service installation, provisioning or credential change follows automatically. This hosted package has no local service lifecycle to start or stop.

- Autonomous use takes direct agent assessment only when policy allows it; otherwise return unavailable to the lead, which can continue ordinary engineering without a model result.
- Explicit use offers direct fallback and waits unless the user already authorized it.
- Label accepted fallback **Agent assessment — Jev unavailable**, reusing sourced evidence and the agreed criterion without Jev probabilities or implied endorsement.
- Default substitution is none. An explicitly named alternative is returned to the lead for separate package discovery through the runtime catalog or approved location, full-entry reading, compatibility, disclosure and remaining-budget checks. Missing/ambiguous/incompatible alternatives block that route. Ask Jev never changes its own provider, endpoint or model on failure.

A valid `insufficient_data` decision is not unavailability. Preserve the gap and smallest useful next evidence action; do not seek another verdict until green. Results remain advisory, never executed verification, independent review, engineering approval or policy mutation.

**Done:** return complete, partial, no-call or unavailable with evidence/policy/ledger pointers, actual and uncertain usage, fallback disposition, gaps and next action. Stop at assessment; no delivery or policy change starts automatically.
