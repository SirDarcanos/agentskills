# Validation

Read when changing or validating this package. These instructions are advisory text, not an executable router.

## Package checks

1. Parse frontmatter with an available YAML parser. Confirm the package name, explicit-only description and Boolean `disable-model-invocation: true`; inspect the body gate separately.
2. Check the consuming runtime's supported metadata before claiming enforcement. An ignored metadata key cannot enforce explicit invocation; the body still requires user invocation. Report untested runtimes and routing behavior separately from parsed metadata.
3. Resolve relative links from each containing file. Copy only this directory to a temporary location and repeat without sibling packages. Inspect rendered headings, lists and code fences using an available preview, or report rendering unrun.
4. Walk every case below against the current entry, retaining sources and observed outcomes. Label author inspection, direct tool walkthroughs and executed agent trials distinctly. For a runtime trial retain the user request, discovered catalog, entries actually read, tool trace, response and before/after protected-state evidence; a plausible answer alone does not prove no execution.
5. Inspect the diff for unrelated edits, private data, credentials and workstation-specific paths. Preserve reference installations. Report checks and remaining gaps; do not install tooling or invoke candidates to validate recommendation-only behavior.

**Done:** metadata, links, isolated copying, rendering and all case dispositions have actual results or explicit gaps. Static checks do not establish runtime behavior.

## Expected cases

These are authored expectations, not executed agent results.

| Case | Expected outcome | Criteria |
| --- | --- | --- |
| User explicitly invokes ask-nico for a bounded change | Read relevant installed entries and project rules; explain one next skill and needed input; stop | AN1–AN4 |
| Ordinary “which workflow fits?” or “implement this” | This advisor stays inactive; the original handler remains responsible | AN1 |
| Another skill requests ask-nico, or a document quotes its command | No activation without the user's specific invocation | AN1 |
| Runtime supplies an explicit user skill expansion | Accept invocation without requiring the original slash text to survive | AN1 |
| External installed skill is the best fit | Inspect its entry and relevant references, cite its source, recommend without invoking | AN2, AN4 |
| Project prohibits the candidate's required service | Explain incompatibility/prerequisite; do not run or endorse it as immediately usable | AN3, AN4 |
| Catalog lists a candidate but its entry is unreadable | Mark claims unverified; report the missing option, no installation | AN2, AN5 |
| Same name resolves to two incompatible copies | Inspect both if accessible; identify ambiguity, no arbitrary selection | AN2, AN5 |
| No suitable installed option or required companion | Report the gap and a bounded manual next step or clarification | AN3, AN5 |
| User says “recommend and run it” | Return advice only; separate execution request belongs outside this advisor | AN4 |
| User asks what Nico personally prefers | Report only documented project choices; no invented preferences or impersonation | AN3, AN6 |
