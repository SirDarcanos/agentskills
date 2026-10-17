# Native plugin maintenance

This is the maintainer procedure for the complete `agentskills` / **Agent Skills** plugin. For user installation, updates, migration and recovery, read the [installation guide and support matrix](installation.md). The support matrix records #168's live local-simulation results and remaining public-delivery/session gaps. Neither packaging checks nor these simulations alone make 2.0.0 ready.

## Package boundary

The authoritative procedures remain in `models/`, `workflow/` and `writing/`. Both manifests list each skill directory once, derived from `*/SKILL.md` rather than a fixed count:

- [Claude-compatible manifest](../.claude-plugin/plugin.json), also usable by Copilot CLI and VS Code.
- [Codex compatibility manifest](../.codex-plugin/plugin.json), with OpenAI presentation metadata. This supported layout avoids a second flattened `skills/` tree. Skill-local `agents/openai.yaml` is optional for these instruction-only skills; no tool dependencies or onboarding workflow are added.
- [Claude marketplace](../.claude-plugin/marketplace.json) and [Codex marketplace](../.agents/plugins/marketplace.json), each exposing one full-collection plugin named `agentskills`.

The plugin root is the repository root at the selected release tag. Git-based installation retains the grouped directories and all package resources/notices. There are no generated copies of skill procedures, symlink farms, hooks, MCP servers, dependencies or install scripts. Model-related instructions remain inert until separately invoked under their existing gates. Existing `npx skills` discovery and standalone package paths remain unchanged; native invocation names can differ.

## Check or regenerate metadata

Use Python 3.10+ from the repository root; Git is needed by the disposable release tests. The checks use the standard library and perform no network access, installation or inference.

```sh
python3 -B scripts/native_plugins.py check
python3 -B -m unittest discover -s scripts -p 'test_native_plugins.py' -v
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
```

The last two commands require an already available Claude Code client. They validate metadata, not native installation. To refresh inventory without changing the candidate version, run `python3 -B scripts/native_plugins.py prepare 2.0.0` (substitute the current manifest version). Never edit generated skill lists independently.

For a disposable resource/isolation check, export to a **new, nonexistent** path outside installed skill directories:

```sh
python3 -B scripts/native_plugins.py export /tmp/agentskills-package-check
```

Choose a different nonexistent destination if that path exists. Export copies all three source groups, manifests, catalogs and the collection notice; it compares every package file's bytes and permission mode. It checks copied instructions' reachable relative Markdown resources without needing source Git metadata, issues or repository documentation. It neither runs packaged scripts nor proves every natural-language branch portable. Remove only your owned scratch export when finished.

`check` rejects omitted/duplicate registrations, missing package notices or linked resources, cross-package instruction links, manifest/catalog drift, unpinned/development plugin selectors, and additional plugin-root auto-discovery effects. The tests also corrupt resources/modes and exercise failed publication checks. These are focused checks, not general security or skill-behavior certification.

## Prepare a candidate, then advance the released channel

The manifest version describes the candidate being developed. Catalog entry versions describe their selected public release. A newer candidate may intentionally coexist with the preceding catalog version; each catalog version must agree with its tag selector and with the manifests at that published tag. Advancing a candidate version alone must not advance the channel.

1. With implementation scope approved, run `python3 -B scripts/native_plugins.py prepare VERSION`. This synchronizes both candidate manifests and derives the full inventory. It leaves both catalog selectors unchanged. Run the offline checks and Claude validators above, inspect the diff and preserve notices. Commit/push/review under the [repository workflow](agents/workflow.md).
2. Before release readiness, obtain #168's required isolated live fresh-install/update evidence. Its disposable release simulation must test the catalogs and native clients separately from these unit fixtures. Neither preparation nor a static pass authorizes a release.
3. Only with explicit maintainer approval, publish collection tag `vVERSION` and its stable GitHub release through the repository's release procedure. The tagged commit must contain both manifests at `VERSION`. Do not move an existing released tag. These maintenance commands do not create tags, releases, branches or assets.
4. After publication, run `python3 -B scripts/native_plugins.py select VERSION`. This reads GitHub through authenticated `gh api`, checks that `vVERSION` is the latest published, non-draft, non-prerelease release, and reads both tagged manifests to confirm identity/version **before writing either catalog**. It then advances the two selectors together. A network/API failure or mismatch stops selection without substituting `main`.
5. Run `python3 -B scripts/native_plugins.py check --published`, the offline tests and both validators. Review and integrate the catalog-only channel change on `main` under normal PR/merge authority. Until integration, clients still see the previous public release. Keep this promotion focused so it need not wait for unrelated development.
6. Refresh each client's marketplace/catalog, then separately update the installed plugin using that client's supported operation. Inspect installed version, inventory and resources after any required restart/reload. A catalog update is not evidence that an installed plugin was updated. Record failures and observed state; preserve the working release selector rather than clearing users' caches or configuration.

**Initial bootstrap:** the committed catalogs target `v2.0.0`, which has not been published at implementation time. There is no previous native release to serve. They are prepublication metadata, not an available released channel; installation fails until the tag exists and must never fall back to development. `check --published` must remain failing until 2.0.0 is actually the latest stable release. Complete live simulated acceptance and the separately approved release before recommending this channel. Subsequent `prepare` operations keep the last selected release available while work continues on `main`.

If interrupted during local metadata writes, inspect both catalog files and rerun `check` before committing or retrying; one-file/version drift is rejected. Re-run `select VERSION` only after checking its current publication gate. If publication succeeded but channel promotion did not, the old channel remains usable; resume promotion rather than republishing or retagging. Removing or rewriting a public release/tag invalidates the source contract and needs explicit maintainer handling, not an automatic fallback.

## Client contract for installation documentation and live validation

The following commands have documentation/source support and the bounded live evidence noted below, **not permission to install the unpublished public bootstrap now**. The marketplace is tracked from the repository default branch so later catalog promotions can be discovered; the catalog's plugin source is separately pinned to `vVERSION`.

| Client | Install/catalog operations | Installed update and invocation | Evidence boundary |
| --- | --- | --- | --- |
| Claude Code | `claude plugin marketplace add SirDarcanos/agentskills`; `claude plugin install agentskills@agentskills` | `claude plugin marketplace update agentskills`, then `claude plugin update agentskills@agentskills`; skill `/agentskills:work-on` | On 2.1.263, strict validators, fresh install and simulated 2.0.0 → 2.0.1 update passed. Catalog refresh left the installed version unchanged; explicit update requested restart. New `plugin details` processes discovered all 32 skills. Exact resources/modes/notices matched the tags. Interactive namespaced selection/reload, minimum version and public transport remain unverified. |
| Codex CLI | `codex plugin marketplace add SirDarcanos/agentskills`; `codex plugin add agentskills@agentskills`. `/plugins` is the documented browser alternative, not live-tested here. | On 0.163.0, `codex plugin marketplace upgrade agentskills` refreshed the catalog **and updated the configured installed plugin**. Repeated `codex plugin add agentskills@agentskills` also reinstalled the selected version. Native skill name `agentskills:work-on`, used as `$agentskills:work-on`; no `codex plugin update` command is assumed. | On 0.163.0, fresh install and simulated 2.0.0 → 2.0.1 update passed with exact resources/modes/notices. A fresh metadata-only native `skills/list` process found all 32 enabled namespaced plugin skills. Interactive selection/new-chat use, minimum version and public transport remain unverified. |
| Copilot CLI / VS Code | Reuse the Claude-compatible manifest/catalog and pinned Git source. | Use each client's own plugin management UI/commands, not Claude/Codex commands. | First-party documentation-backed compatibility only; #167 owns complete guidance. No live acceptance claim. |

Claude marketplace auto-update is user-controlled; this repository cannot promise it is enabled. Codex marketplace refresh and configured-plugin refresh can also differ by client/version. Keep both observations distinct in the user support matrix. Gemini direct installation/manual updates and the general editable `npx` route remain #167's user-documentation scope; neither uses an invented universal plugin updater.

## Sources and limits

Inspected first-party documentation:

- [Claude manifest/path rules](https://code.claude.com/docs/en/plugins/manifest-reference), [marketplace sources and ref selectors](https://code.claude.com/docs/en/plugins/marketplace-reference), [hosting/version and update behavior](https://code.claude.com/docs/en/plugins/host-marketplace).
- [OpenAI plugin packaging and Git-backed marketplace selectors](https://developers.openai.com/plugins/build/plugins), [skill resources and optional tool metadata](https://developers.openai.com/plugins/build/skills), [Codex installation/new-chat example](https://developers.openai.com/learn/developers-codex-plugin).
- [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) and [VS Code agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins).

Codex source inspected at `ce0323f2f2d3b25e82806cd555237da3db4e1897`: [legacy manifest paths](https://github.com/openai/codex/blob/ce0323f2f2d3b25e82806cd555237da3db4e1897/codex-rs/core-plugins/src/manifest.rs), [marketplace source/ref and policy parser](https://github.com/openai/codex/blob/ce0323f2f2d3b25e82806cd555237da3db4e1897/codex-rs/core-plugins/src/marketplace.rs), [CLI add/reinstall tests](https://github.com/openai/codex/blob/ce0323f2f2d3b25e82806cd555237da3db4e1897/codex-rs/cli/tests/plugin_cli.rs), and [skill namespace resolver](https://github.com/openai/codex/blob/ce0323f2f2d3b25e82806cd555237da3db4e1897/codex-rs/ext/skills/src/loader/namespace.rs). These are upstream implementation evidence, not a tested installed-client version or a required consumer history read.

The unit fixture suite uses local Git tags and an in-memory published-release response; it does not execute native clients. Separately, #168 executed the native clients against an isolated Git release simulation, including cache/refresh behavior and unpublished-change exclusion. See the [support matrix](installation.md#support-and-evidence) for versions, source identity, test boundary and remaining gates. Neither kind of evidence verifies public 2.0.0 availability. Keep failed/unrun observations visible and obtain the relevant approval before public delivery or interactive session checks; do not advance a release selector or claim readiness from a static or simulated pass.
