# Resolve merge conflicts

Resolve an active Git merge or rebase while preserving compatible intentions and unrelated work. The agent can load [SKILL.md](SKILL.md) during already-authorized integration without a separate command. It pauses for incompatible product rules, unsafe checks or missing completion permission.

## Requirements and use

Requires Git, file/history inspection, scoped editing and the target project's relevant checks. No companion skills, GitHub access or additional models are required; missing remote intent evidence is reported when material. Project policy and the original task decide which integration may finish. Abort, discard, skip, push and merge-to-main remain separately authorized.

After approving installation, copy this complete directory, including its [license](LICENSE), references and scripts, or use:

```sh
npx skills add SirDarcanos/agentskills --skill resolve-merge-conflicts
```

Installation has not been exercised here. Repository delivery does not update the existing `resolving-merge-conflicts` reference installation or retire it.

## Validate

With Python 3.9+ and Git, from the repository root:

```sh
python3 -B workflow/resolve-merge-conflicts/scripts/check-fixtures.py
```

The script uses disposable local repositories and synthetic identities without network, dependencies or global Git configuration changes. Follow [validation](references/validation.md) for acceptance mapping and limits. These are scripted Git checks, not autonomous agent-adherence tests.

## Source credit

Inspired by Matt Pocock's `resolving-merge-conflicts` reference skill: inspect state, trace intent, resolve, check and complete integration. Its reference-copy rules to always resolve and broadly stage are deliberately replaced with bounded authority, protected work and decision pauses. Upstream [source tree at revision `49dd158`](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336) and [MIT license](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE); that revision's tree no longer contains the conflict skill, so it is not claimed as the exact revision of the inspected reference copy. The package [LICENSE](LICENSE) retains Matt Pocock's notice alongside Nicola Mustone's for this implementation.
