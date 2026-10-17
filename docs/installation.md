# Install, update and migrate Agent Skills

Choose one route per agent. Native plugins install the **complete collection** from `workflow/`, `writing/` and `models/` as **Agent Skills**, plugin identifier `agentskills`. The [skill catalog](skills.md) describes individual requirements. Bundling model skills does not invoke them.

> **Prepublication:** the native catalogs currently select `v2.0.0`, which is not published. Do not run the native install examples yet: they cannot fetch that release. Claude Code/Codex live fresh-install and update verification, supported client versions and 2.0.0 readiness remain pending [#168](https://github.com/SirDarcanos/agentskills/issues/168). Use the [general route](#general-route-and-editable-copies) meanwhile. After publication and catalog promotion, native plugins are the recommended full-collection route for Claude Code and Codex CLI.

Installation supplies instructions and resources, not dependencies, credentials, model services or permissions. It does not set up a project, start services or grant approval to execute scripts. Review sources and client trust prompts before confirming installation. Local project policy and each skill's invocation gates still apply.

## Support and evidence

This matrix records the current boundary, not a universal compatibility promise. Client commands below are documentation-backed unless explicitly marked upstream-source-backed. A minimum version is **not established** for any client yet; use a client exposing the documented plugin/skill manager and inspect its help before proceeding. A missing command blocks that route; it is not a reason to edit caches or silently switch to development content.

| Client / route | Documentation or source support | Static/offline evidence | Live install/update evidence and reload |
| --- | --- | --- | --- |
| Claude Code plugin | Official CLI, catalog and namespaced skills docs | Both strict metadata validators passed on Claude Code **2.1.263**; this is not an install-tested minimum. Shared inventory/resource and release-selector checks pass. | **Pending #168**: fresh install, update, full discovery and release isolation. Start a new session after changes; current docs also support `/reload-plugins`. |
| Codex CLI plugin | Official packaging/browser docs; add/reinstall/remove and expected namespace also backed by upstream source | Shared manifest/inventory/resource and selector checks; no installed Codex client tested | **Pending #168**: exact released-client commands, minimum version, namespace, install/update and release isolation. Start a new chat after installation. |
| Copilot CLI plugin | Official Claude-compatible manifest/catalog and management reference | Shared Claude-compatible metadata checked; no Copilot parser/runtime check | **Documentation-only**; minimum version pending verification. Start a new session after changes; check discovery. |
| VS Code plugin | Official Claude-compatible plugin and marketplace guidance | Shared metadata checked; no VS Code runtime check | **Documentation-only**; minimum version and reload behavior pending verification. Reload the window if discovery has not refreshed. |
| Gemini CLI direct skills | Official skill management docs; grouped-path/overwrite behavior checked in upstream implementation | Standalone source/resources preserved; Gemini discovery not executed | **Documentation-only**; minimum version pending verification. Run `/skills reload` after changes. No plugin or automatic updater is claimed. |
| `npx skills` / manual copies | Existing general, selectable and editable route | Grouped standalone package layout preserved | Installation/discovery not exercised in this change; reload according to your agent. No native release-channel guarantee. |

The [maintainer procedure](native-plugins.md) owns packaging checks and release-source/version maintenance. Offline fixtures model two releases and exclude an unpublished change; they do not test client caches, refresh timing or an already published 2.0.0. Claude/Codex must each pass the isolated live gate before 2.0.0 is ready. Copilot, VS Code and Gemini may remain documentation-only.

## Releases, catalogs and installed versions

A **catalog refresh** fetches the marketplace's current listing. A **plugin update** changes the installed package. Check both: a refreshed listing alone does not prove the installed version changed.

Native marketplace registration tracks this repository's default branch **for catalog discovery only**. Each catalog entry separately selects an immutable `vVERSION` release tag for plugin content. After a published release is promoted under the maintainer procedure, a catalog refresh can discover it, then the client can update the installed plugin. An unreleased skill edit on `main` is not that released plugin. Candidate manifest versions in a development checkout are not evidence of availability. Never work around a missing release by installing the repository root from `main` as though it were the stable channel.

The bootstrap has no previous native release: until `v2.0.0` exists and its release checks pass, a fetch failure is expected. Later channel-promotion delays can leave clients on the preceding published version. Check the [published releases](https://github.com/SirDarcanos/agentskills/releases), catalog offer and installed version before reporting an update failure. Automatic update behavior differs by client, as described below.

## Claude Code

**After the prepublication gate above is cleared:**

1. In your terminal, register the catalog and install its full-collection entry (user scope):

   ```sh
   claude plugin marketplace add SirDarcanos/agentskills
   claude plugin install agentskills@agentskills --scope user
   ```

   This uses `.claude-plugin/marketplace.json`, not a direct development-root install. If GitHub SSH is unavailable, the hosting docs recommend setting `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` in your shell environment for installs and later updates; no credential replacement is required.
2. Start a new Claude Code session, or use `/reload-plugins` on clients that support it. In `/plugin`, inspect Installed and any Errors. Plugin skills use a namespace: invoke **`/agentskills:setup-project`**, then, when wanted, **`/agentskills:work-on`**. The standalone `/work-on` spelling elsewhere in this repository is not the plugin command.
3. To update, refresh the listing, then update the installed copy at the same scope:

   ```sh
   claude plugin marketplace update agentskills
   claude plugin update agentskills@agentskills --scope user
   ```

   Restart/reload and inspect the installed version and skill list again. Third-party marketplace background auto-update is off by default in current documentation; enable it deliberately under `/plugin` → Marketplaces → agentskills → Enable auto-update if desired. Do not assume it is enabled.
4. To stop using this plugin, choose the supported action deliberately:

   ```sh
   claude plugin disable agentskills@agentskills --scope user
   # To enable again:
   claude plugin enable agentskills@agentskills --scope user
   # To uninstall instead:
   claude plugin uninstall agentskills@agentskills --scope user
   ```

   Substitute the actual scope if you chose project/local installation. Do not remove the marketplace as a refresh shortcut: current Claude behavior can uninstall its plugins. On failure, inspect `/plugin` Errors and installed state before retrying the relevant install or update command; follow [recovery](#failed-or-interrupted-operations).

## Codex CLI

**Pending released-client verification:** these are the intended native steps after publication, not a claim that an installed Codex version has passed them. Check `codex plugin --help` and `codex plugin marketplace --help`; if the commands or browser are missing, use the general route until #168 establishes a supported client. Do not invent a `codex plugin update` command.

1. Register the repository-hosted `.agents/plugins/marketplace.json` catalog:

   ```sh
   codex plugin marketplace add SirDarcanos/agentskills
   ```

2. Start Codex, open **`/plugins`**, find **Agent Skills** in the `agentskills` marketplace and select Install plugin. Start a **new chat**. Upstream CLI tests also cover terminal installation with `codex plugin add agentskills@agentskills`; confirm availability in your client before using it.
3. Inspect the installed entry/version and available skills. The upstream namespace resolver yields **`$agentskills:work-on`** (and `$agentskills:setup-project`); actual released-client selection remains pending #168. Use the skill picker to confirm the exposed name rather than assuming Claude's slash syntax.
4. Refresh the catalog with `codex plugin marketplace upgrade agentskills`. Upstream tests cover repeating `codex plugin add agentskills@agentskills` to reinstall from the refreshed catalog. **The installed-version transition is still pending live verification**: check client help/browser options, preserve existing edits, then use the supported reinstall/update action and start a new chat. A catalog upgrade alone is not an installed-plugin update. No automatic-update timing is promised.
5. To disable without removal, the documented config form is `[plugins."agentskills@agentskills"]` with `enabled = false` in the applicable Codex `config.toml`; preserve other settings and check project overrides. Re-enable with `true`. Upstream CLI tests cover `codex plugin remove agentskills@agentskills` for removal; confirm local help first. Inspect the plugin list/browser after any change. If install/update fails, preserve observed configuration and version, then retry only the failed supported step after diagnosing the error.

## Copilot CLI

**Documentation-only; wait for the released channel to exist.** The existing Claude-compatible manifest is used without an Agent Plugins schema conversion.

1. In the terminal, register the marketplace and install its entry (not `OWNER/REPO` as a direct plugin):

   ```sh
   copilot plugin marketplace add SirDarcanos/agentskills
   copilot plugin install agentskills@agentskills
   copilot plugin list
   ```

2. Start a new session and inspect available skills. Use the client's skill picker or ask by skill name, such as `work-on`; no Claude/Codex namespace is promised. Project or personal skills with the same `name` take precedence over plugin skills in current Copilot documentation, so check for silently shadowed entries.
3. Update the catalog and installed plugin separately, then start a new session and check version/discovery:

   ```sh
   copilot plugin marketplace update agentskills
   copilot plugin update agentskills@agentskills
   copilot plugin list
   ```

   The documented first-party auto-update behavior for the built-in `awesome-copilot` marketplace is not a guarantee for this third-party marketplace. Use the explicit operations above.
4. Use `copilot plugin disable agentskills@agentskills` to deactivate, `copilot plugin enable agentskills@agentskills` to reactivate, or `copilot plugin uninstall agentskills@agentskills` to remove. Managed policy may prevent local changes; report that restriction rather than bypassing it. On errors, inspect list/state and `copilot plugin <subcommand> --help`, then retry the failed step without forced marketplace removal.

## VS Code

**Documentation-only; wait for the released channel to exist.** Use the Claude-compatible catalog, not a direct source install of development `main`.

1. Ensure agent plugins are enabled (`chat.plugins.enabled`). Add `SirDarcanos/agentskills` to the existing **`chat.plugins.marketplaces`** array in settings, preserving other entries:

   ```json
   "chat.plugins.marketplaces": ["SirDarcanos/agentskills"]
   ```

2. In Extensions, search **`@agentPlugins`**, find **Agent Skills** from this marketplace, review the source/trust prompt and select Install. Confirm it in Agent Plugins - Installed and **Chat: Configure Skills**. Use the displayed skill names; Claude's `/agentskills:…` and Codex's `$agentskills:…` syntax are not promised here.
3. Run **Extensions: Check for Extension Updates**. Current docs describe a 24-hour check when `extensions.autoUpdate` is enabled; updating refreshes cloned marketplaces and checks external plugin versions. Inspect the installed version, not just the catalog listing, and apply any offered Update action. Reload the window if skills have not refreshed. Exact behavior for this package remains untested.
4. From Agent Plugins - Installed, use the plugin's context menu to Disable (globally or for this workspace), Enable, or Uninstall. Manage it in the interface where you installed it: current docs warn that `/plugin` chat commands and the Agent Customizations editor have separate inventories. VS Code can also discover Copilot CLI installs; inspect those before adding another copy.
5. If installation fails, retry through the same interface after inspecting the repository/revision/path error. VS Code validates incomplete caches itself; do not manually delete or edit its plugin cache. If retry still fails with a valid source, use **Help: Report Issue** and include sanitized observed state.

## Gemini CLI: direct skills, not a plugin

This is a separate direct-install route with **manual updates**, not a native marketplace subscription. It does not inherit the plugin's release selector. The unqualified repository URL installs source content, which can be unreleased.

1. Inspect `gemini skills install --help` and existing `/skills list`. Preserve same-named copies first: the upstream installer **overwrites existing destinations**, and a multi-skill install can leave a partial result if interrupted. Do not use it over local edits without a verified backup and explicit replacement choice.
2. For an unmodified installation, use the documented Git-repository installer with the grouped subpath (example: one workflow skill):

   ```sh
   gemini skills install https://github.com/SirDarcanos/agentskills --path workflow/shape-work --scope user
   ```

   `--path` support is upstream-source-backed; confirm it in local help. Repeat for desired complete skill packages from the catalog, including required companions. For a specific published version, download/extract that release into a new staging directory and install the local package path instead, for example `gemini skills install ./agentskills-release/workflow/shape-work --scope user`. Replace the illustrative staging path with your actual reviewed source. No full-collection plugin or recursive grouped-root discovery is assumed.
3. Run `/skills reload`, then `/skills list`, checking names and resolved sources. Workspace skills override user skills; `.gemini/skills` and `.agents/skills` aliases can both matter. Use skill names in requests, respecting explicit-invocation gates; `/skills` is a manager, not `/agentskills:…` invocation.
4. To update, manually select a newer source/release, compare complete packages, preserve edits, then rerun the install for each approved replacement. There is no automatic release-channel refresh. Reload and verify every intended skill/resource; stop if only some updated.
5. Use `/skills disable shape-work` or `/skills enable shape-work` in-session. To remove an approved user copy, use `gemini skills uninstall shape-work` (choose the matching `--scope` if needed). Confirm the resolved target before removal, especially when a workspace copy shadows it. On failure, inventory which packages actually changed before retrying; do not treat the collection as atomically updated.

## General route and editable copies

Use a skills-capable agent plus Node.js/`npx` for the existing selectable installer:

```sh
npx skills add SirDarcanos/agentskills
```

Choose the agent, destination and desired skills, including compatible companions. Check prompts before replacing same-named skills. This source route is useful now and for editable copies; it is **not** the release-pinned native plugin channel. Inspect installer help before selecting update/removal operations; no automatic updater is promised. Before rerunning installation, compare and back up locally modified packages.

For manual installation, copy the **whole skill directory**, such as `workflow/shape-work/`, including references, scripts, assets and license notices. Keep the other required companions too. Do not copy only `SKILL.md`. To update, compare and deliberately replace complete packages from a chosen revision; to retire one, remove only the specific approved copy/link after backup. Repository merges do not refresh separate copies. Prefer this route when you intend to edit instructions: edits inside native plugin caches can be replaced by updates.

## Migrate existing copies safely

1. **Identify what loads today.** Inspect your agent's installed/plugin list, skill picker, project roots and user roots. Common locations include project/user `.agents/skills`, `.claude/skills`, `.github/skills`, `~/.copilot/skills`, and `.gemini/skills`; these are discovery leads, not an exhaustive deletion list. Inspect Codex's configured skill locations and plugin config too. Record copy versus symlink, resolved source, installer, scope, version or unknown provenance, and other agents sharing the location. A same-named skill is not proof of the same source.
2. **Preserve modifications before replacement.** Compare whole packages with the known source where possible. Back up hidden files, references, scripts, assets, notices, modes, links and relevant registrations to a private location outside active discovery roots. Check that the backup can be restored. Keep local additions/deletions; unknown provenance is not permission to overwrite. Shared symlink sources must remain intact for other agents.
3. **Choose one active route per agent.** Select native full collection after its gate clears, or standalone/npx for selective/editable copies. Stage and inspect the replacement and its companions before retiring old copies. Keep backups until discovery and resources have been checked. Do not migrate to an unavailable bootstrap.
4. **Resolve duplicates deliberately.** Use the client's supported disable/uninstall action for the exact old plugin, or deliberately move an approved standalone copy outside every discovery root. For a shared link, change only the approved link, not its source. Do not delete all skill folders or installer caches. Namespaces can make two copies visible in Claude/Codex; Copilot can silently prefer local skills, and Gemini prefers workspace over user skills. Confirm the resolved source, not merely the name.
5. **Verify before calling migration complete.** Restart/reload as specified above, inspect every intended skill and required companion, installed version and accessible resources. Confirm old copies no longer compete. If a conflict or missing resource remains, keep backups and the last known working route; report the remaining target rather than silently deleting it. Native uninstall does not clean up independent npx/manual copies.

For an agent performing a separately approved installed-copy transaction, the [migration runbook](agents/installed-skill-migration.md) adds exact-target approval, journaling and rollback checks. Reading this guide grants no automatic cleanup/replacement authority.

## Failed or interrupted operations

1. Stop dependent use and record the client version, command/interface, selected source, scope, error and observed installed/catalog versions. Redact tokens and private paths before sharing. Inspect actual state: a timeout is not proof that nothing changed.
2. Check whether the release exists, the catalog has refreshed, the client supports the command and policy/network access permits it. Keep the last working installation and local edits. A missing bootstrap release is resolved by publication, not a fallback to `main`.
3. Retry only the failed supported step after reconciliation. Use the same manager and intended scope. Never clear all configuration, credentials, caches or skill directories as a generic repair. If the client cannot establish state, stop with that uncertainty.
4. If replacement damaged local edits or only partly updated packages, restore only your approved targets from the verified backup, preserving intervening edits and shared sources. Refresh discovery and inspect the restored result. Keep unresolved conflicts and partial recovery visible; do not call an unverified rollback successful.

## First-party references

Command facts were checked on 2026-10-17; client documentation can change. These are documentation/source checks, not executed installation walkthroughs.

- Claude Code: [CLI operations](https://code.claude.com/docs/en/plugins/cli-reference), [skill namespace](https://code.claude.com/docs/en/plugins/components), [hosting and update behavior](https://code.claude.com/docs/en/plugins/host-marketplace).
- Codex: [packaging and marketplace management](https://developers.openai.com/plugins/build/plugins), [plugin browser/new-chat example](https://developers.openai.com/learn/developers-codex-plugin). [Maintainer evidence](native-plugins.md#sources-and-limits) pins the upstream CLI and namespace source used for provisional commands.
- [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).
- [VS Code agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins).
- Gemini CLI: [skill management](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md), [installer command](https://github.com/google-gemini/gemini-cli/blob/main/packages/cli/src/commands/skills/install.ts), [overwrite implementation](https://github.com/google-gemini/gemini-cli/blob/main/packages/cli/src/utils/skillUtils.ts).
