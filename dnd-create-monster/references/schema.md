# OpenFray Creature JSON — field reference

Read this reference when the user requests OpenFray output or when using a temporary OpenFray object to lint mechanics internally. It does not define the skill's default Markdown output or the schema of any other tool.

Distilled from `src/schema/creature.ts`, `action.ts`, `primitives.ts` in SirDarcanos/openfray, and from the serialization conventions in `public/compendium/srd-creatures.json`. Compendium files are a JSON **array** of Creature objects.

Rule of the schema: **mechanics live in structured fields; prose lives in `text` and is display-only.** Every number a die roller needs (`toHit`, `damage[].formula`, `save.dc`, `recharge`) must be in its structured field even though it also appears in the prose.

## Creature (top level)

| Field | Type | Notes |
|---|---|---|
| `id` | string | Stable, `source:kebab-name` — `"custom:gloom-stalker"`, `"srd-5.2:mummy"` |
| `source` | string | `"custom"` unless the user names one. Existing: `srd-5.2`, `srd-5.1`, `waking-garden`, `brood-and-bloom`, `kobold-press-tob`… |
| `edition` | `"5.5"` \| `"5.0"` | `"5.5"` for 2024-rules monsters |
| `sourcePage` | number? | Only for published sources |
| `name` | string | No definite article |
| `size` | enum | `Tiny` `Small` `Medium or Small` `Medium` `Large` `Huge` `Gargantuan` |
| `type` | string | lowercase: `"aberration"`, `"undead"`, `"humanoid"`… |
| `alignment` | string? | lowercase: `"chaotic evil"`, `"unaligned"`, `"any alignment"` |
| `description` | string? | Markdown lore, display only. Omit unless supplied |
| `ac` | number | |
| `maxHp` | number | Average of `hpFormula` |
| `hpFormula` | string? | `"9d8+18"` — die from size (Tiny d4, Small d6, Medium d8, Large d10, Huge d12, Gargantuan d20), no spaces |
| `initiative` | number? | Dex mod by default; Dex mod + PB for Legendary Resistance creatures. (The SRD also uses +PB or +2PB on some alert non-legendary monsters — a legal lever, not the default) |
| `speed` | object | `{ "walk": 30, "fly": 60, "swim": …, "climb": …, "burrow": …, "hover": true }` — only present keys |
| `abilities` | object | All six, lowercase keys: `{ "str": 16, "dex": 8, … }` |
| `saves` | object? | **Proficient saves only**, total bonus: `{ "wis": 3 }` |
| `skills` | object? | Proficient only, camelCase keys (`sleightOfHand`, `animalHandling`), total bonus |
| `senses` | object | `passivePerception` required; optional `darkvision`/`blindsight`/`tremorsense`/`truesight` in feet |
| `languages` | string[]? | e.g. `["Common plus two other languages"]`, `["Deep Speech", "telepathy 120 ft."]` |
| `resistances` / `immunities` / `vulnerabilities` | string[]? | **Capitalized** damage types: `["Necrotic", "Poison"]` |
| `conditionImmunities` | string[]? | Capitalized: `["Charmed", "Frightened"]` |
| `gear` | string[]? | 2024 blocks list carried equipment; display only |
| `cr` | number | Fractions as decimals: `0.125`, `0.25`, `0.5` |
| `xp` | number | From the XP table below |
| `xpLair` | number? | Only if a lair XP value exists |
| `traits` | Trait[]? | `{ "name", "text" }` — passive features |
| `actions` / `bonusActions` / `reactions` | Action[]? | |
| `legendaryActions` | object? | `{ "perRound": 3, "perRoundLair": 4, "actions": [Action…] }` |
| `spellcasting` | object? | See below |
| `legendaryResistance` | number? | Uses/day; also written as a trait `"Legendary Resistance (3/Day)"` |
| `legendaryResistanceLair` | number? | |

Do not use `lairActions` or `legendaryCost` for 2024 monsters, and do not use `limitedUse` — recharge/X-per-day lives inline on the action (matches the SRD ingest, which never emits `limitedUse`).

## Action

```json
{
  "id": "rotting-fist",
  "name": "Rotting Fist",
  "kind": "melee",
  "toHit": 5,
  "reach": 5,
  "damage": [
    { "formula": "1d10+3", "type": "bludgeoning" },
    { "formula": "3d6", "type": "necrotic" }
  ],
  "text": "Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Bludgeoning damage plus 10 (3d6) Necrotic damage. …"
}
```

- `id`: kebab-case of the name, unique within the creature.
- `kind`: `melee` | `ranged` | `save` | `utility`. Multiattack is `utility` with `toHit: null`.
- `toHit`: number for attacks, `null` otherwise (the key is always present).
- `reach` (melee, feet) or `range` (`{ "normal": 30, "long": 120 }`, ranged).
- `damage[]`: dice formulas without spaces (`"2d10+8"`); `type` **lowercase** (`acid bludgeoning cold fire force lightning necrotic piercing poison psychic radiant slashing thunder`).
- `save`: for save-based actions — `{ "ability": "wis", "dc": 11, "onSave": "negates" }`. `onSave`: `half` (damage halved) | `none` (nothing happens) | `negates` (rider negated). Attack-with-rider-save actions keep `toHit` and put the rider DC in prose only.
- `recharge`: `{ "type": "dice", "value": 5 }` for "Recharge 5–6"; `{ "type": "perDay", "value": 2 }` for 2/Day; `{ "type": "perRound", "value": 1 }`.
- `text`: 2024 stat-block prose. Attack: `Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Bludgeoning damage.` Save: `Wisdom Saving Throw: DC 11, one creature the mummy can see within 60 feet. Failure: … Success: …` Damage types capitalized in prose. Averages precede formulas: `8 (1d10 + 3)` — formula spaced in prose, unspaced in `damage[].formula`.
- Spell links in prose: `[Command](spell:srd-5.2:command)`.
- Single-cost strong legendary actions end with: `The creature can't take this action again until the start of its next turn.`

## Spellcasting

```json
{
  "ability": "cha",
  "saveDc": 20,
  "toHit": 12,
  "groups": [
    { "usage": { "type": "atWill" }, "spells": [ { "name": "Detect Magic", "ref": "srd-5.2:detect-magic" } ] },
    { "usage": { "type": "perDay", "per": 1 }, "spells": [ { "name": "Fireball", "ref": "srd-5.2:fireball" } ] }
  ]
}
```

- `usage.type: "perDay"` defaults to the 2024 "N/Day **Each**" model. Set `"shared": true` only for a single pool across the whole group (2014-style "1/Day: bless, daylight, hallow" = one casting from the list).
- `usage.type: "slots"` + top-level `slots` map only for 2014/5.1 blocks — never for new 5.5 monsters.
- `ref` when the spell exists in a loaded compendium (`srd-5.2:kebab-name`); omit for spells that don't.

## XP by CR

0→10, 1/8→25, 1/4→50, 1/2→100, 1→200, 2→450, 3→700, 4→1100, 5→1800, 6→2300, 7→2900, 8→3900, 9→5000, 10→5900, 11→7200, 12→8400, 13→10000, 14→11500, 15→13000, 16→15000, 17→18000, 18→20000, 19→22000, 20→25000, 21→33000, 22→41000, 23→50000, 24→62000, 25→75000, 26→90000, 27→105000, 28→120000, 29→135000, 30→155000

Proficiency bonus by CR: ≤4→+2, 5–8→+3, 9–12→+4, 13–16→+5, 17–20→+6, 21–24→+7, 25–28→+8, 29–30→+9. Attack bonuses, save DCs (8 + PB + ability mod), proficient saves and skills must all reconcile with the ability scores and PB — `validate` checks this.
