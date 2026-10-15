# Research

Investigate a bounded question using authoritative sources and return cited findings, applicable dates/versions, uncertainty and requested recommendations. It works directly or through an authorized background worker; neither delegation nor repository writes are mandatory.

## Use

Ask a question such as “For version 2, what retry behavior is documented?” or provide an authorized research handoff with existing findings and source pointers. The agent follows [SKILL.md](SKILL.md), reuses current evidence and refreshes only affected claims. Research stops at findings, without creating product commitments, tickets or implementation.

Copy the complete `research/` directory into the runtime's discovery location, or install this package with the skills CLI:

```sh
npx skills add SirDarcanos/agentskills --skill research
```

Installation examples are guidance, not executed installation evidence. An existing installed same-name package needs a separately approved update/migration; merging this repository does not replace it.

## Requirements and limits

Direct work needs authorized source-reading tools and a return channel. No named model or hosted service is required. Source access, private disclosure and retained/public outputs follow target policy. Findings can remain in the conversation when no write/retention authority is supplied.

Optional delegation requires permission, a bounded inspectable runtime and the shared execution library in a discovered compatible `work-on` package. That library is read without starting delivery. Missing optional capability selects equivalent direct research; background-only requirements stay blocked. Companion locations need not be siblings. See [delegation](references/delegation.md).

[Validation](references/validation.md) defines package checks and workflow exercises. The existing [Clef feasibility note](clef-feasibility.md) is preserved as historical research; it is not this skill's procedure or current policy.
