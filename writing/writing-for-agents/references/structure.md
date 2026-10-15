# Structure and routing

Use this reference when organizing instructions, writing pointers or changing skill metadata.

## Pointers

A pointer names material outside the current context and states the condition for reading it. Its wording determines whether an agent reaches the target. Name distinct cases rather than accumulating synonyms; keep the target's purpose recognizable.

- Weak: “See the release guide.”
- Actionable: “Before preparing a release, read the release guide for version selection and publication approval.”

Use a Markdown link where the target ships with the document. Resolve it from the containing file, not the repository root. Keep skill-package links internal to the package; discover optional companions rather than linking to assumed sibling installations. A pointer to an external authority may be appropriate in target documentation, but reading a source does not authorize invoking an external companion.

Keep required material easy to reach. First strengthen a weak pointer instead of duplicating its entire target in the entry point. A moved file also needs its incoming links updated within authorized scope, or the outstanding callers reported.

## Placement

Keep common actions inline. Disclose details used by only one branch in a nearby referenced file. Separate definitions from ordered execution when that makes the procedure easier to follow, while keeping each concept's caveats together. Split files for a real branch or reading need, not a line-count target.

Every split adds navigation for the human and a pointer for the agent. Retain enough context to make each independently reached section usable. Avoid creating a new workflow or mandatory companion merely to shorten prose.

## Completion criteria

Specify what can be checked and how missing evidence affects the next step.

- Weak: “Review the configuration thoroughly.”
- Actionable: “Compare each documented option with the active configuration; list unsupported options and stop dependent instructions until reconciled.”

Use the smallest sufficient criterion. Exhaustiveness is useful when omissions change safety or meaning; a checklist of irrelevant checks adds noise. Preserve clear failure and approval boundaries even when pruning repetition.

## Skill metadata

1. Read the target runtime's supported metadata rules before changing invocation behavior. Frontmatter support and explicit-only gates differ across runtimes; metadata alone does not prove enforcement.
2. Keep `name` consistent with the package identity and make `description` say when the agent should load the skill. Include skills, instruction files and referenced guides when those are the actual supported branches; avoid a generic “help with documentation” trigger.
3. Align description, body and actual authority. Preserve explicit-invocation restrictions where established, including body-level gates required by the target runtime.
4. Test relevant positive and negative routing examples by inspection or an authorized runtime check. Label inspection as such; runtime behavior remains unverified unless exercised.

Shared reference does not need to become another invokable skill. A plain file can serve several callers without starting a workflow.
