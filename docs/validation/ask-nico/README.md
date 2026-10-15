# Ask Nico — #112 delivery evidence

## Agreement, state and authority

- [#112](https://github.com/SirDarcanos/agentskills/issues/112) delivers only `workflow/ask-nico/` under AN1–AN6 of authoritative [#109](https://github.com/SirDarcanos/agentskills/issues/109). Inspected issue bodies supply the agreement; no new product decisions are introduced.
- Native paginated reads returned no blocked-by/blocking edges. Parent read is #109; its sub-issues include #112 (database ID 5863999661). No graph or label mutation is needed.
- Initial index/worktree were clean; prior branch PR #114 was merged. Created `feat/ask-nico` from `origin/main` at `df2607ecf60a829523d14b5888e574ee5a3642d1`. PR target: `main`. No unrelated dirty work to protect; existing installations are excluded and unchanged.
- The calling lead owns package, evidence, catalog and changelog. Build-and-check selected from existing ticket readiness for this bounded instruction package. Independent Standards/Spec review is separately authorized by repository workflow; at most two read-only workers, 600-second bounds, no recursive work or optional assessments. Checkpoint `112-final`: initially zero repair cycles spent; optional assessment allocation zero.
- Preflight and build-and-check were read from the discovered installed catalog. Entry SHA-256 respectively: `ccb940cb60819792947274f1d848636c6461d47ae3856bae80fcd83d1df39d15`, `40a72625c2a7eadd3bba41c562879f248feef30fa5a42371396348ac61bd44a2`. Their contracts support scoped Git preparation and checked implementation increments. Work On owns verification/completion; Review Delivery owns the pinned two-axis review; PR owns reporting/publication.

## Implementation and checks

1. Wrote entry and validation reference; checked internal links, four completion criteria and explicit-only metadata shape: pass. Directly inspected the invocation, discovery, project-authority and no-execution boundaries.
2. Added package README/license and catalog/changelog entries. Internal links and isolated copy without sibling skills passed. Ruby/Psych parsed the frontmatter, including Boolean `disable-model-invocation: true`: pass. Generated checker-import bytecode was identified and removed; subsequent Python runs use `-B`.
3. Added offline checker and [scenario analysis](examples.md). The first run passed package/isolation/negative probes but correctly failed on the examples' link to this not-yet-written README. Added the evidence home and reran before dependent review. This is a development sequencing failure, not an agent behavior result or an acceptance repair cycle.
4. Executed the installed Pi loader against only this package: one skill, zero diagnostics, `disableModelInvocation === true`, empty automatic skill prompt. A false-flag control appeared in the prompt, confirming sensitivity to the flag. This exercises loader metadata, not model adherence or interactive invocation.
5. Rendered Markdown to HTML with the already available Marked parser and inspected the generated headings, lists, tables and links. No graphical browser preview or screenshots were executed. No tools were installed.

### Reproduce offline checks

From the repository root, with Python 3.9+, Ruby/Psych and Git:

```sh
python3 -B docs/validation/ask-nico/check-package.py
ruby -e 'require "yaml"; m=YAML.safe_load(File.read("workflow/ask-nico/SKILL.md").split(/^---\s*$\n/)[1]); abort unless m.keys.sort == %w[description disable-model-invocation name] && m["name"] == "ask-nico" && m["description"].is_a?(String) && m["disable-model-invocation"] == true; puts "PASS: YAML metadata and explicit-only Boolean"'
git diff --check
```

The Python checker covers packaged files, limited metadata shape, ordered phases, fences, internal links, isolated copying, catalog/evidence links and three intentionally broken-link probes. It is not a full YAML/Markdown parser; external URLs are not fetched. Negative probes test checker sensitivity, not advisor behavior.

For an existing global Pi installation and Node, without installing anything:

```sh
PI_PACKAGE_ROOT="$(npm root -g)/@earendil-works/pi-coding-agent" node --input-type=module <<'JS'
import assert from 'node:assert/strict';
import {pathToFileURL} from 'node:url';
const {loadSkillsFromDir,formatSkillsForPrompt} = await import(pathToFileURL(process.env.PI_PACKAGE_ROOT+'/dist/core/skills.js'));
const r=loadSkillsFromDir({dir:process.cwd()+'/workflow/ask-nico',source:'validation'});
assert.equal(r.diagnostics.length,0);
assert.equal(r.skills.length,1);
assert.equal(r.skills[0].name,'ask-nico');
assert.equal(r.skills[0].disableModelInvocation,true);
assert.equal(formatSkillsForPrompt(r.skills),'');
assert.match(formatSkillsForPrompt([{...r.skills[0],disableModelInvocation:false}]),/ask-nico/);
console.log('PASS: explicit-only loader metadata and false-flag control');
JS
```

Executed environment: Python 3.14.7, Ruby 2.6.10/Psych, Node 24.21.0 and Git 2.54.0 on macOS. Pi's installed skills documentation and loader declarations were inspected for the metadata contract. No model call, candidate invocation, global installation update or remote mutation is part of these checks.

## Criterion evidence

| Criterion | Delivered coverage and evidence | Limits |
| --- | --- | --- |
| AN1 — Explicit invocation | Metadata and step 1; E1–E4. YAML parse and actual Pi loader exclusion, with false-flag control | Agent behavior and interactive command expansion untested; other runtimes untested |
| AN2 — Discovery | Step 2 reads complete relevant installed entries/references before substantive claims; source identities, catalog/companion limits; E1/E5/E7/E8 | Static scenario analysis, not autonomous discovery execution |
| AN3 — Recommendation | Steps 2–4 apply project rules, explain fit/input/stopping point and prerequisites; E1/E6/E7/E10 | Static instruction coverage; no live restricted service probe |
| AN4 — No execution | Step 3 advisory-only effects, separate execution request; step 4 returns control; E5/E6/E9 | Static guardrail inspection; no executed advisor tool trace |
| AN5 — Missing options | Steps 2–3 distinguish unreadable/unavailable/ambiguous candidates and missing companions; E7/E8 | Static scenario analysis; installation command unrun |
| AN6 — Identity | Opening and steps 2/4 separate documented project choices from personal preferences; E10 | Static instruction coverage, not personality evaluation |

All six criteria have inspected instruction coverage. Runtime behavior remains unverified; metadata testing is deliberately not reported as an agent trial. No application runtime, destructive action, service lifecycle or persistence mechanism is added, so those executable risk categories do not apply. The material instruction risks are unintended activation, unsupported recommendations, authority expansion and workflow execution; the scenarios and independent review inspect those boundaries.

## Documentation and impact

Updated package README/license/validation, repository catalog, one Unreleased Added entry and this evidence. Root README already links to the catalog; no duplicate listing needed. No glossary, ADR, operating policy, #109 commitment, existing skill, or installed copy changed. Upstream inspiration is credited locally with both MIT notices; the inspected reference supplied no exact source revision.

Compatible new functionality: minor release impact, not publication authority. No existing tests were removed, weakened, renamed or moved; one offline packaging checker is added. Baseline and delivered repository CI definitions are absent; no CI jobs changed. CI timing/compute are inapplicable to inspected configuration, and no savings are claimed. External automation is unknown.

Merge publishes source only; it does not install skills, deploy or release. A source revert can remove this package and its catalog/changelog entry but cannot undo separately copied installations. No installation occurred in this delivery. Keep #112 open pending maintainer acceptance and merge. Review reports and gate decisions belong in the PR handoff; they do not grant merge authority.
