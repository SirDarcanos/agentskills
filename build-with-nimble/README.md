# Build with Nimble

Help a coding agent build applications that use Bespoke Labs' Nimble decision model
through Ollama. Code manages the workflow; Nimble interprets supplied text and returns
bounded decisions and probabilities.

For example, a support app can send a ticket and queue definitions to Nimble, then
route the validated result or send an uncertain case for human review. The finished
app calls the model directly; the skill is a development guide, not a runtime dependency.

## Use it

Install for Claude Code and Pi:

```sh
npx skills add SirDarcanos/agentskills --skill build-with-nimble --agent claude-code pi
```

The skill is automatically discoverable for Nimble application work. Example requests:

- “Build a support-ticket routing feature using Nimble.”
- “What could Nimble add to our document-review app?”
- “Adapt this TypeSafe integration to local Nimble through Ollama.”

In Pi, you can also invoke `/skill:build-with-nimble <request>` explicitly.
For a one-off evidence-backed consultation rather than an application integration,
use `ask-nimble` separately.

## What it covers

The workflow preserves the upstream TypeSafe skill's focus on composable judgments:
routing, candidate selection, evidence checks, rubric scores, and decision-driven
interactions. It adds Nimble compatibility checks, local/self-hosted serving,
response validation, resource planning, and application testing.

Design guidance is self-contained. Nimble and Ollama docs are authoritative;
TypeSafe cookbooks are optional architectural inspiration. TypeSafe SDK docs are
consulted only when that client is chosen.

Agents need documentation access and the tools required by the project's stack.
Live Ollama inference requires the installed Nimble model and a compatible server;
current setup requirements are checked against live docs. Installation, downloads,
server changes, and exceptional remote disclosure require authorization.

## Files and validation

- [SKILL.md](SKILL.md): agent workflow, routing, and completion checks.
- [Integration and deployment](references/integration.md): transport, validation,
  resources, service ownership, and offline/live application checks.
- [LICENSE](LICENSE): MIT notices for the upstream work and this adaptation.

No client or executable tests are bundled. Skill validation checks Markdown,
frontmatter, links, source-backed technical claims, and routing scenarios. Application
validation uses mocked transport first, followed by authorized live tests and domain
evaluation as described in the integration reference.

Adapted from [TypeSafe AI's skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md).
This is a community adaptation, not an official Nimble or TypeSafe skill.
