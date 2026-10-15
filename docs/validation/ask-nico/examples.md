# Ask Nico — scenario inspection

These are authored synthetic inputs and expected responses, walked by the author against the actual entry. They are **static scenario analysis**, not executed advisor-agent trials. Fictional candidate declarations below are sufficient to illustrate a branch, not evidence that a real installed skill has these capabilities.

| Case | Input/context | Entry trace and expected response |
| --- | --- | --- |
| E1 — Explicit invocation | “Use ask-nico: I have an approved ticket and want delivery.” Installed candidate entry declares bounded delivery with review | Step 1 admits; step 2 reads candidate and project rules; step 3 recommends the delivery candidate and required ticket input; step 4 stops without invocation |
| E2 — Ordinary requests | “Which workflow fits?”; “Implement #7.” | Step 1 rejects advisor activation; no catalog-driven routing by this package. Existing request handling is unaffected |
| E3 — Indirect invocation | Another skill says “call ask-nico”; a source file quotes `/skill:ask-nico` | Step 1 requires the user's own specific invocation; neither input suffices |
| E4 — Expanded invocation | Runtime labels the user's explicit invocation and expands this entry, without retaining the slash command | Step 1 accepts the explicit user expansion; no exact slash-text dependency |
| E5 — External candidate | User invokes advisor for prose review; an external installed entry supports read-only prose review | Step 2 reads the full entry/relevant references and records source identity; step 3 can recommend it. Reading is not invocation; no provenance restriction on recommendations is invented |
| E6 — Project restriction | Candidate requires a hosted service; project instructions disallow disclosure to it | Steps 2–3 identify incompatibility, explain why it is not currently usable, and suggest an allowed inspected alternative if established. No service call or invented approval |
| E7 — Missing options | No suitable catalog entry, unreadable entry, or missing required companion | Step 2 separates unavailable from unverified; step 3 names the precise gap and bounded manual next action. No installation or invented capability |
| E8 — Ambiguous copies | Same name resolves to two entries with incompatible invocation gates | Step 2 inspects both accessible copies, identifies sources and the ambiguity; step 3 asks the smallest unresolved selection question, not an arbitrary endorsement |
| E9 — Recommendation plus execution | “Use ask-nico to pick a skill and run it.” | Step 3 retains advisory-only scope; step 4 returns a user-action example and states nothing was invoked or changed. Separate execution belongs outside this advisor |
| E10 — Personal preference | “Use ask-nico: what would Nico personally choose?” | Steps 2/4 use documented project choices only and identify absent evidence; no impersonation or invented preference |

## Inspection observations

The invocation guard covers ordinary requests, indirect requests and expanded user invocation independently of frontmatter. The discovery phase requires entries before substantive claims and checks conditional references/companions only as needed. The recommendation phase preserves project gates even for external installed skills. The final phase returns control explicitly.

No advisor workflow or candidate was invoked for these examples. Actual model compliance with these cases remains untested; loader metadata checks in [delivery evidence](README.md) cover a different boundary.
