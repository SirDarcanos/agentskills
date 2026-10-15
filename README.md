# Agent skills for turning ideas into software

[![skills.sh](https://skills.sh/b/SirDarcanos/agentskills)](https://skills.sh/SirDarcanos/agentskills)

The skills I use to take an idea through planning, coding, checks, and review. Describe what you want to your coding agent; these instructions help it work through the steps and bring important decisions back to you.

You don't need to know how to design a database or write a test. You decide what the software should do, answer questions, and try the result.

## Get started

You'll need a coding agent that supports skills, plus Node.js and `npx` for installation.

**1. Install from your terminal:**

```bash
npx skills add SirDarcanos/agentskills
```

Choose your agent, installation destination, and the workflow skills, including `setup-project`. Check before replacing same-named skills. Writing and model skills are optional; additional models aren't needed for the delivery workflow.

**2. Set up your project in your agent:**

```text
/setup-project
```

It checks the project, asks how you want to work, and proposes changes for your approval. For GitHub projects, it also coordinates repository, security, and issue-tracker setup. Run it when establishing or updating project conventions, not before every feature.

**3. Describe your idea:**

```text
/shape-work I want people to book places in my classes.
```

Answer the questions and agree on what to build. Then ask the agent to deliver it:

```text
/work-on the booking tool we agreed on
```

`work-on` handles the technical steps, relevant checks, independent review, and a plain-language change report. Read what was checked, note any gaps, and try the result yourself.

Slash commands go in your agent, not your terminal; support varies by runtime. Skills may require companions and tools: see the [setup requirements](workflow/setup-project/README.md#install-and-requirements) and [delivery requirements](workflow/work-on/README.md#install-and-dependencies). Installation supplies instructions, not missing tools or permissions.

## Pick the work you need

You can name a skill directly or describe the job in ordinary language. You don't need to run every skill for every change.

| Your situation | Start with |
| --- | --- |
| You need to work out what to build | [`shape-work`](workflow/shape-work/) |
| You have one clear change or an existing issue | [`work-on`](workflow/work-on/) — give it the request, issue number, or URL. |
| Larger work needs a lasting agreement and tasks | [`write-spec`](workflow/write-spec/), then [`write-tickets`](workflow/write-tickets/) when a breakdown is useful. Approve tracker changes before publication. |
| You want to deliver a specification across its tasks | [`work-on-spec`](workflow/work-on-spec/) — give it the spec reference. It needs tracker access, separate coding-agent capability, and permission to use it. |
| You want a review of existing changes | [`review-delivery`](workflow/review-delivery/) |

For a small change, go straight to `work-on`. It brings in specialists when needed; you don't have to manage each handoff.

### Bugs

Describe what you expected, what happened, and how to reproduce it if you know. The agent can load [`investigate-bug`](workflow/investigate-bug/) when it recognizes a bug needs diagnosis, or you can ask directly:

```text
/investigate-bug Cancelling a booking doesn't free up a place in the class.
```

It investigates the cause and prepares evidence for a fix, with approval before tracker changes. An investigation-only request stops before repair. Ask `work-on` to deliver the resulting ticket when you're ready; it reuses current diagnosis evidence.

### Moving to another session

```text
/handoff Continue investigating the booking cancellation bug.
```

[`handoff`](workflow/handoff/) runs only when requested. Give the next agent the returned file path. For later resumption, supply an approved durable destination: temporary files can disappear. It writes context, not permission to start the next task.

## What to expect

The agent should report missing tools, permissions, checks, or required independent review—not treat them as completed. Building does not grant permission to merge, deploy, or release. Skills and reviews can still miss problems; use qualified technical review for software handling sensitive data, money, or other high-stakes operations.

## More

[All skills and their requirements](docs/skills.md) · [Validation evidence and limits](docs/validation/composable-acceptance/README.md) · [Replacing installed skills](docs/agents/installed-skill-migration.md) · [MIT license](LICENSE)

Copy complete skill directories when installing manually, including their references and license notices. Repository updates don't refresh installed copies.

---

These skills were largely inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills). Thanks, Matt, for sharing your work. Adapted packages retain their attribution and license notices.
