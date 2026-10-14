# Direct specification walkthrough

Executed by the author in the implementation session, not an independent or delegated agent trial. Inputs and outputs are synthetic. Source base: `c1465e7` (#61 integrated); procedure under test is the dirty #62 package in this PR. The package/check revision is pinned by the PR commit, not by base HEAD alone.

## Agreed ordinary input

Read [agreement-1](agreement.md) and applied Write Spec steps 1–4 in the current context. The approval owner, rationale, behavior, dispositions, home and fixture-only effects were supplied; no Shape Work session, questions, research, Analyze or model call was needed. Wrote [the actual spec](spec.md), then inspected each requirement:

- Filtered loaded entries and displayed order → AC1; pagination limitation retained.
- UTF-8 and headers, including empty result → AC1–AC2.
- CSV field-content preservation → AC3.
- Existing list unchanged → AC4.
- Deferred column selection/revisit and excluded scheduling retained with reasons.

All claims trace to agreement-1. Product approval is reused; unresolved filtering design is explicitly unready. This exercise verifies specification expression, not the future export behavior (no exporter was built or tested).

## Safe publication and existing identity

Executed `python3 -B docs/validation/write-spec/check.py`. It invokes the local CRUD fixture in a disposable directory: inspect empty list → create title `Proposal: Export the filtered reading list`, exact spec body and labels `product-agreement`, `feature` → read issue 1 revision 1 → compare full values. No `delivery-task` or `agent-actionable` role was sent. The body retains the design-readiness blocker. Actual fixture read-back matched, with zero relationships.

On the existing-spec pass, inspected list/read, reused issue 1 and performed no write. Byte comparison showed unchanged store and exactly one spec; no tickets were created. The fixture intentionally does not deduplicate: the caller's explicit reuse is what prevents a second create.

The fixture update then persisted revision 2 but returned a simulated timeout. A subsequent read established actual identity/body/roles before any retry; no second create occurred. A simulated unavailable read returned failure rather than success. These executed operations verify local persistence/fault mechanics, not remote API semantics or autonomous policy routing.

## Additional direct decision applications

Applied the entry/publication procedure to these synthetic variants in-session; these are direct inspection/returned decisions, not executable routing assertions:

| Variant | Actual returned decision and effects |
| --- | --- |
| Owner asks whether weekly email export should be added, without approving it | **Draft delta:** “Proposal P1: send a weekly export email; recipients, privacy effects and acceptance remain unresolved.” Preserve AC1–AC4 and existing exclusions; no new commitment or fixture mutation. Recommend owner decision/shaping only for this new branch. |
| Supplied spec has unchanged approval/evidence and no requested publication delta | **Complete unchanged agreement:** reuse artifact and AC1–AC4, no interview/rewrite/publication. Work On adapter step 1 can bypass writing and choose missing readiness. |
| Deciding design note changes from client filtering to server filtering, while agreement-1 remains unchanged | Preserve approved behavior/dispositions; invalidate dependent design/readiness claims only. Return missing updated technical evidence for Analyze within authority; no blanket rediscovery or model call. No technical claim is approved by this spec. |
| Tracker has both `product-agreement` and `delivery-task`, but no removal approval | Publication role mismatch; propose exact removal of `delivery-task`, preserve other metadata and block reliance. No mutation. |
| Draft tracker body retains `agent-actionable`, removal unapproved | Report contradictory readiness, propose authorized removal, block coordination. Draft publication alone grants no approval. No mutation. |
| Requested publication lacks mapped role or compatible tracker library | Return useful spec plus publication blocker; no label invention, install or legacy fallback. |
| Small approved heading correction, conversation-only return | Brief with criterion “the agreed heading is corrected; surrounding text unchanged”; no spec issue or discovery session. |

For the caller route, explicitly resolved Write Spec from the repository task's approved package location, read its complete entry/publication/validation, and inspected the authored spec and fixture outcomes against Work On's shared envelope. Required capabilities match; no sibling-directory assumption is part of runtime discovery. The adapter can return the inspected agreement and unresolved-design readiness blocker. Standalone execution ended at the spec return, without decomposition, implementation or scheduling. This is a direct caller walkthrough, not a full delivery or installed-runtime trial.

## Limits

No independent review, live tracker mutation, installed discovery/installation, autonomous agent-compliance trial, delegated work, model inference or full discovery→spec→tickets delivery was executed. #70 owns the broader composed trial. Authored validation tables remain scenarios; the Python test does not execute the Markdown policy. New commitments stay drafts and actual acceptance/merge remain maintainer decisions.
