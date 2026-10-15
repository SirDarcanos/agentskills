# Ask Nico

Ask which installed skill or workflow fits your situation. [SKILL.md](SKILL.md) inspects relevant entries and project rules, explains a recommendation, and leaves execution to you.

## Use and requirements

Invoke `ask-nico` explicitly, for example:

```text
Use ask-nico: I have an approved ticket; which installed workflow should I use next?
/skill:ask-nico I only want a diagnosis, not a fix. What fits?
```

The second form is Pi's skill command; other runtimes may use different explicit invocation syntax. Generic workflow questions and other skills do not activate this advisor. The name is a label, not a claim to speak for Nicola Mustone or predict personal preferences.

Requires read access to the runtime's discoverable installed skill entries and relevant project instructions. No mandatory companion, model service, fixed catalog or installation layout. External installed skills may be recommended after inspection, but no recommended skill or companion is invoked. Unreadable, unavailable or ambiguous candidates and project restrictions are reported.

## Install

After approving installation, copy this entire directory, including its [license](LICENSE) and references, into your runtime's skill discovery location, or use:

```sh
npx skills add SirDarcanos/agentskills --skill ask-nico
```

The installation command has not been exercised in this delivery. Repository delivery does not replace or retire existing reference installations.

`disable-model-invocation: true` requests explicit-only discovery in runtimes supporting that metadata; the entry also checks user invocation. YAML parsing is not evidence of runtime enforcement. Unsupported or untested runtimes remain verification gaps; the advisor must not run automatically.

## Validation and source credit

Read [validation](references/validation.md) when modifying the package. Repository evidence at `docs/validation/ask-nico/README.md` records package checks and scenario coverage; it is not required by a copied installation.

Substantially inspired by Matt Pocock's `ask-matt` reference skill: read skill entries before giving routing advice, and use a user-invoked advisor to make workflows discoverable. This package replaces its fixed flow map with installed-catalog discovery, project authority checks and a recommendation-only boundary under #109/#112. No phase-boundaries procedure or upstream workflow map is copied.

Upstream: [Matt Pocock's skills](https://github.com/mattpocock/skills), distributed under the [MIT license](https://github.com/mattpocock/skills/blob/main/LICENSE). The inspected reference copy supplied no exact source revision or bundled license; these links identify the upstream project, not an asserted revision. The package [LICENSE](LICENSE) retains Matt Pocock's notice alongside Nicola Mustone's.
