# Writing for agents — #111 evidence

## Agreement and delivery boundary

- [#111](https://github.com/SirDarcanos/agentskills/issues/111) delivers only `writing/writing-for-agents/`, covering WA1–WA6 of authoritative [#109](https://github.com/SirDarcanos/agentskills/issues/109).
- Native inspection returned no blocked-by or blocking edges; parent is #109 and its paginated sub-issues include #111. No relationships or labels were changed. Readiness is not acceptance.
- Direct implementation by the calling technical lead; build-and-check selected for a new instruction package with focused static and synthetic examples. Existing readiness was reused; no fresh product decisions or domain/ADR changes were needed.
- Initial worktree/index were clean on the prior feature branch; its PR #113 was merged. New branch `feat/writing-for-agents` starts at current `origin/main`, `3934c929623b09add75109d9bb7e215177d32bb7`. Intended PR target: `main`. No unrelated dirty work was present.
- Approved scope: package, validation evidence, catalog and one Unreleased entry. Excluded: unrelated document rewrites, installation/retirement of reference copies, other #109 packages, tracker graph changes, merge and release.

## Implementation/check sequence

1. Wrote entry, structure reference and validation reference. Ran a Python check of all current internal links, scalar metadata shape, balanced fences and four completion criteria: pass.
2. Added package README/license, catalog/changelog and offline checker. Ran `python3 -B docs/validation/writing-for-agents/check-package.py`: pass. The checker checks packaged files and links, copies only the package, repeats checks without siblings, and rejects missing-file, missing-anchor and escaping-link probes. These negative cases execute checker failures, not agent behavior.
3. Parsed frontmatter with Ruby/Psych and inspected description/body routing: pass. Added [synthetic examples](examples.md) for skill, instruction file and referenced guide. Walked each through the actual steps as static author inspection, not an executed agent trial.
4. Rendered all four package Markdown files, both evidence Markdown files, the catalog and the changed Unreleased changelog section using existing Marked 18.0.11 and headless Chrome. Read the eight screenshots: headings, ordered lists, tables, code fences and links display correctly without clipping. No tools were installed and no document content was sent externally. Final evidence wording was re-rendered after this update.

### Reproduce safe checks

From the repository root, with Python 3.9+ (the checker uses only its standard library), Ruby with standard-library YAML/Psych, and Git:

```sh
python3 -B docs/validation/writing-for-agents/check-package.py
ruby -e 'require "yaml"; m=YAML.safe_load(File.read("writing/writing-for-agents/SKILL.md").split(/^---\s*$\n/)[1]); abort unless m.keys.sort == %w[description name] && m["name"] == "writing-for-agents" && m["description"].is_a?(String); puts "PASS: YAML frontmatter parses with Ruby/Psych"'
git diff --check
```

Executed with Python 3.14.7, system Ruby/Psych and Git 2.54.0 on macOS. No downloaded dependencies, network calls, global configuration writes or optional model assessments are needed by these checks. The checker is intentionally limited to the package's current inline-link/ATX-heading/fenced-code syntax; it is not a general Markdown or YAML parser. YAML parsing is the separate Ruby command.

## Criterion-level evidence

| Criterion | Delivered source and evidence | Disposition and limits |
| --- | --- | --- |
| WA1 — Coverage | Entry description/opening and step 1 cover skills, instruction files and referenced guides; E1–E3 instantiate all three | Verified by static inspection and authored transformations, not autonomous routing |
| WA2 — Actionability | Four ordered entry phases with completion criteria; structure reference specifies conditional pointers and observable criteria; E1/E3 show rewrites | Static coverage verified; runtime adherence untested |
| WA3 — Organization | Step 2 selects one authoritative home and preserves exceptions; conditional structure reference; E2 removes a duplicate while retaining local permission | Static coverage and isolated package links verified |
| WA4 — Fidelity | Steps 1/3 preserve commitments and stop unapproved policy changes; E2 keeps publication approval | Static safety boundary verified; no live publication attempted |
| WA5 — Companions | Step 3 requires project provenance and compatible transitive boundaries; direct writing for absent/unknown/external helpers; E1 and additional cases | Static coverage verified; no companion or optional model was invoked for the examples |
| WA6 — Validation | Step 4 and validation reference cover links, anchors, metadata/routing, formatting, environment and gaps; offline checker, Ruby parse, eight rendered screenshots, E3 | Package links/YAML and local rendering executed; runtime-specific invocation enforcement untested |

## Documentation and impact

Updated the package's own README/references/license, [catalog](../../skills.md) and [changelog](../../../CHANGELOG.md). Root README already points to the catalog; it needs no duplicate listing. No domain meaning, operating policy, ADR, existing skill or installed copy changes. Both MIT notices are included because this package is substantially inspired by Matt Pocock's reference skill; the README identifies source provenance limits.

Compatible new functionality: minor release impact, not release permission. No existing executable tests were removed, moved or modified. One new offline packaging-check script was added, plus three author-produced writing examples; these are not application tests or executed agent scenarios. Baseline and delivered repository CI definitions are absent; no CI jobs changed. CI duration/compute are inapplicable for inspected configuration; no timing or cost improvement is claimed. External automation is not established by this inspection. Merge would publish source only; it does not install skills, deploy or release. Source reversion can remove the package/catalog/entry but cannot roll back separately copied installations; no installation occurred here.

## Evidence limits and next gate

The initial PATH check found no `pandoc`, `cmark` or `markdown`; further discovery found Marked 18.0.11 already installed with the coding-agent runtime and a local Chrome binary. Markdown was converted with `marked.parse` (frontmatter excluded from display), wrapped in local HTML with readable table/code styling and a restrictive content-security policy, then captured by Chrome with `--headless --disable-background-networking --disable-component-update --no-first-run --no-default-browser-check --host-resolver-rules='MAP * ~NOTFOUND' --hide-scrollbars --window-size=1280,4000 --screenshot` and disposable browser profiles. The screenshot and HTML artifacts remain in the delivery session rather than the portable package. This demonstrates local Marked/Chrome rendering, not every host's styling. The offline checker itself still correctly reports that it does not test rendering.

No particular consuming runtime is mandated by the package; frontmatter syntax was parsed, but cross-runtime invocation and agent-adherence trials remain unexecuted. Installation command and upstream web-link reachability were not exercised. These are verification limits, not new accepted product limitations.

Independent Standards and Spec reports and the frozen review snapshot are retained in the delivery session and resulting PR report; this authored evidence document contains no reviewer verdicts. Build, acceptance and report decisions remain separate. Keep #111 open pending maintainer acceptance and merge. Global installation, retirement, merge and release remain separately gated.
