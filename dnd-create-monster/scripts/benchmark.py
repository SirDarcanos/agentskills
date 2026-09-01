#!/usr/bin/env python3
"""OpenFray monster benchmarks, comparables, and validation.

Usage:
  benchmark.py stats <CR>          CR benchmark row + all SRD creatures at that CR
  benchmark.py show <name> [...]   dump creature JSON by (fuzzy) name
  benchmark.py validate <file>     lint a creature JSON file (single object or array)

Data source order: local checkout (~/GitHub/openfray, ./openfray, .),
then the copy bundled with this skill, then GitHub raw.
"""

import json
import math
import os
import re
import statistics
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = "https://raw.githubusercontent.com/SirDarcanos/openfray/main/public/compendium/srd-creatures.json"

CANDIDATES = [
    os.path.expanduser("~/GitHub/openfray/public/compendium/srd-creatures.json"),
    "openfray/public/compendium/srd-creatures.json",
    "public/compendium/srd-creatures.json",
    os.path.join(HERE, "..", "references", "srd-creatures.json"),
]

XP = {0: 10, 0.125: 25, 0.25: 50, 0.5: 100, 1: 200, 2: 450, 3: 700, 4: 1100,
      5: 1800, 6: 2300, 7: 2900, 8: 3900, 9: 5000, 10: 5900, 11: 7200,
      12: 8400, 13: 10000, 14: 11500, 15: 13000, 16: 15000, 17: 18000,
      18: 20000, 19: 22000, 20: 25000, 21: 33000, 22: 41000, 23: 50000,
      24: 62000, 25: 75000, 26: 90000, 27: 105000, 28: 120000, 29: 135000,
      30: 155000}

SIZES = {"Tiny", "Small", "Medium or Small", "Medium", "Large", "Huge", "Gargantuan"}
DAMAGE = {"acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
          "piercing", "poison", "psychic", "radiant", "slashing", "thunder"}
KINDS = {"melee", "ranged", "save", "utility"}
ABILITIES = ["str", "dex", "con", "int", "wis", "cha"]
SKILLS = {"acrobatics": "dex", "animalHandling": "wis", "arcana": "int",
          "athletics": "str", "deception": "cha", "history": "int",
          "insight": "wis", "intimidation": "cha", "investigation": "int",
          "medicine": "wis", "nature": "int", "perception": "wis",
          "performance": "cha", "persuasion": "cha", "religion": "int",
          "sleightOfHand": "dex", "stealth": "dex", "survival": "wis"}
HP_DIE = {"Tiny": 4, "Small": 6, "Medium or Small": 8, "Medium": 8,
          "Large": 10, "Huge": 12, "Gargantuan": 20}


def pb_for_cr(cr):
    return max(2, 2 + (math.ceil(cr) - 1) // 4)


def mod(score):
    return (score - 10) // 2


def load_srd():
    for p in CANDIDATES:
        if os.path.exists(p):
            with open(p) as f:
                return json.load(f), p
    with urllib.request.urlopen(RAW, timeout=20) as r:
        return json.load(r), RAW


def parse_cr(s):
    if "/" in s:
        a, b = s.split("/")
        return float(a) / float(b)
    return float(s)


def fmt_cr(cr):
    if 0 < cr < 1:
        return f"1/{int(round(1 / cr))}"
    return str(int(cr))


def best_hit(c):
    hits = [a["toHit"] for a in c.get("actions", []) if a.get("toHit") is not None]
    return max(hits) if hits else None


def best_dc(c):
    dcs = [a["save"]["dc"] for a in c.get("actions", []) if a.get("save")]
    sc = c.get("spellcasting") or {}
    if sc.get("saveDc"):
        dcs.append(sc["saveDc"])
    return max(dcs) if dcs else None


def cmd_stats(cr_str):
    cr = parse_cr(cr_str)
    data, src = load_srd()
    rows = [c for c in data if c.get("cr") == cr]
    print(f"# CR {fmt_cr(cr)} — {len(rows)} SRD 5.2 creatures  (data: {src})")
    if not rows:
        near = sorted({c["cr"] for c in data if c.get("cr") is not None},
                      key=lambda x: abs(x - cr))[:2]
        print(f"None at this CR. Nearest populated: {', '.join(fmt_cr(n) for n in near)}")
        return
    hps = [c["maxHp"] for c in rows]
    hits = [h for h in (best_hit(c) for c in rows) if h is not None]
    dcs = [d for d in (best_dc(c) for c in rows) if d is not None]
    hit_summary = f"{statistics.median(hits):+.0f}" if hits else "—"
    dc_summary = f"{statistics.median(dcs):.0f}" if dcs else "—"
    print(f"AC median {statistics.median(c['ac'] for c in rows):.0f} | "
          f"HP median {statistics.median(hps):.0f} (range {min(hps)}-{max(hps)}) | "
          f"best hit median {hit_summary} | best DC median {dc_summary}")
    print(f"XP {XP.get(cr, '?')} | PB +{pb_for_cr(cr)}")
    print()
    for c in sorted(rows, key=lambda c: c["name"]):
        hit = best_hit(c)
        dc = best_dc(c)
        extras = []
        if c.get("legendaryResistance"):
            extras.append("legendary")
        if c.get("spellcasting"):
            extras.append("caster")
        print(f"  {c['name']:<28} {c['size']:<15} {c['type']:<12} "
              f"AC {c['ac']:>2}  HP {c['maxHp']:>3}  "
              f"hit {f'{hit:+d}' if hit is not None else '  -'}  "
              f"DC {dc if dc is not None else ' -'}  {' '.join(extras)}")


def cmd_show(names):
    data, _ = load_srd()
    for name in names:
        n = name.lower()
        exact = [c for c in data if c["name"].lower() == n]
        found = exact or [c for c in data if n in c["name"].lower()]
        if not found:
            print(f"No SRD creature matching {name!r}", file=sys.stderr)
            continue
        for c in found[:3]:
            print(json.dumps(c, indent=1))


def err(errors, name, msg):
    errors.append(f"[{name}] {msg}")


def check_creature(c, errors, warnings):
    if not isinstance(c, dict):
        err(errors, "<unknown>", "creature must be a JSON object")
        return

    name = c.get("name", "<unnamed>")
    error_count = len(errors)
    for field in ("id", "source", "edition", "name", "size", "type", "ac",
                  "maxHp", "speed", "abilities", "senses", "cr", "xp"):
        if field not in c:
            err(errors, name, f"missing required field '{field}'")
    if len(errors) != error_count:
        return

    if not isinstance(c["id"], str) or not re.fullmatch(r"[a-z0-9.-]+:[a-z0-9-]+", c["id"]):
        err(errors, name, f"id '{c['id']}' not in source:kebab-name form")
    if not isinstance(c["source"], str):
        err(errors, name, "source must be a string")
    elif isinstance(c["id"], str) and not c["id"].startswith(c["source"] + ":"):
        warnings.append(f"[{name}] id prefix doesn't match source '{c['source']}'")
    if c["size"] not in SIZES:
        err(errors, name, f"size '{c['size']}' not in {sorted(SIZES)}")
    if c["edition"] not in ("5.5", "5.0"):
        err(errors, name, f"edition '{c['edition']}' invalid")
    if not isinstance(c["type"], str):
        err(errors, name, "type must be a string")
    elif c["type"] != c["type"].lower():
        warnings.append(f"[{name}] type should be lowercase")
    if name.lower().startswith("the "):
        warnings.append(f"[{name}] name starts with a definite article")

    abilities = c["abilities"]
    if not isinstance(abilities, dict):
        err(errors, name, "abilities must be an object")
        return
    for a in ABILITIES:
        if a not in abilities:
            err(errors, name, f"abilities missing '{a}'")
        elif not isinstance(abilities[a], int) or isinstance(abilities[a], bool):
            err(errors, name, f"ability '{a}' must be an integer")
    if set(abilities) - set(ABILITIES):
        err(errors, name, f"unknown ability keys {set(abilities) - set(ABILITIES)}")
    if len(errors) != error_count:
        return

    cr = c["cr"]
    if not isinstance(cr, (int, float)) or isinstance(cr, bool) or cr not in XP:
        err(errors, name, f"cr {cr!r} is not a supported CR (0, 1/8, 1/4, 1/2, or 1–30)")
        return
    pb = pb_for_cr(cr)
    expected_bonuses = {mod(score) + pb for score in abilities.values()}
    expected_dcs = {8 + bonus for bonus in expected_bonuses}
    valid_xp = (XP[cr], 0) if cr == 0 else (XP[cr],)
    if c.get("xp") not in valid_xp:
        err(errors, name, f"xp {c.get('xp')} != {XP[cr]} for CR {fmt_cr(cr)}")

    # hpFormula sanity
    if c.get("hpFormula"):
        m = re.fullmatch(r"(\d+)d(\d+)([+-]\d+)?", c["hpFormula"])
        if not m:
            err(errors, name, f"hpFormula '{c['hpFormula']}' malformed (no spaces, NdM+K)")
        else:
            n_, d_, k_ = int(m[1]), int(m[2]), int(m[3] or 0)
            avg = math.floor(n_ * (d_ + 1) / 2 + k_)
            if avg != c["maxHp"]:
                err(errors, name, f"maxHp {c['maxHp']} != average {avg} of {c['hpFormula']}")
            if HP_DIE.get(c["size"]) and d_ != HP_DIE[c["size"]]:
                warnings.append(f"[{name}] hp die d{d_} unusual for {c['size']} (expected d{HP_DIE[c['size']]})")
            expected_k = n_ * mod(abilities["con"])
            if k_ != expected_k:
                warnings.append(f"[{name}] hpFormula bonus {k_:+d} != {n_}xCon mod ({expected_k:+d})")

    # initiative rule: 2024 blocks use Dex mod, Dex+PB, or Dex+2PB (expertise)
    dex = mod(abilities["dex"])
    if c.get("initiative") is not None and c["initiative"] not in (dex, dex + pb, dex + 2 * pb):
        warnings.append(f"[{name}] initiative {c['initiative']} not Dex mod ({dex:+d}), "
                        f"+PB ({dex + pb:+d}), or +2PB ({dex + 2 * pb:+d})")

    # saves/skills coherence
    for a, bonus in (c.get("saves") or {}).items():
        if a not in ABILITIES:
            err(errors, name, f"saves key '{a}' invalid")
        elif bonus != mod(abilities[a]) + pb:
            warnings.append(f"[{name}] save {a} {bonus:+d} != mod+PB ({mod(abilities[a]) + pb:+d})")
    for s, bonus in (c.get("skills") or {}).items():
        if s not in SKILLS:
            err(errors, name, f"skills key '{s}' invalid (camelCase of the 18 skills)")
        else:
            base = mod(abilities[SKILLS[s]])
            if bonus not in (base + pb, base + 2 * pb):
                warnings.append(f"[{name}] skill {s} {bonus:+d} != mod+PB ({base + pb:+d}) or expertise ({base + 2 * pb:+d})")
    if "passivePerception" in c.get("senses", {}):
        pp = 10 + (c.get("skills") or {}).get("perception", mod(abilities["wis"]))
        if c["senses"]["passivePerception"] != pp:
            warnings.append(f"[{name}] passivePerception {c['senses']['passivePerception']} != {pp}")

    for lst in ("resistances", "immunities", "vulnerabilities", "conditionImmunities"):
        for v in c.get(lst) or []:
            if v and not v[0].isupper():
                warnings.append(f"[{name}] {lst} entry '{v}' should be capitalized")

    if "lairActions" in c:
        err(errors, name, "lairActions present — 2024 monsters have none")
    if "limitedUse" in c:
        err(errors, name, "top-level limitedUse is invalid — put recharge on an action")

    seen_ids = set()
    groups = [("actions", c.get("actions")), ("bonusActions", c.get("bonusActions")),
              ("reactions", c.get("reactions")),
              ("legendaryActions", (c.get("legendaryActions") or {}).get("actions"))]
    for gname, actions in groups:
        for a in actions or []:
            if not isinstance(a, dict):
                err(errors, name, f"{gname}: action must be a JSON object")
                continue
            aid = f"{gname}/{a.get('name', '?')}"
            for field in ("id", "name", "kind", "toHit", "text"):
                if field not in a:
                    err(errors, name, f"{aid}: missing required field '{field}'")
            action_id = a.get("id")
            if action_id is not None and action_id in seen_ids:
                err(errors, name, f"duplicate action id '{action_id}'")
            if action_id is not None:
                seen_ids.add(action_id)
            if action_id and not re.fullmatch(r"[a-z0-9-]+", action_id):
                err(errors, name, f"{aid}: id '{action_id}' not kebab-case")
            if a.get("kind") not in KINDS:
                err(errors, name, f"{aid}: kind '{a.get('kind')}' invalid")
            if "toHit" not in a:
                err(errors, name, f"{aid}: toHit key required (null for non-attacks)")
            if "limitedUse" in a:
                err(errors, name, f"{aid}: limitedUse is invalid — use recharge")
            to_hit = a.get("toHit")
            if a.get("kind") in ("melee", "ranged") and to_hit is None:
                warnings.append(f"[{name}] {aid}: attack with null toHit")
            elif to_hit is not None and (not isinstance(to_hit, int) or isinstance(to_hit, bool)):
                err(errors, name, f"{aid}: toHit must be an integer or null")
            elif to_hit is not None and to_hit not in expected_bonuses:
                warnings.append(f"[{name}] {aid}: toHit {to_hit:+d} does not match ability mod + PB")
            if a.get("kind") == "melee" and "reach" not in a:
                warnings.append(f"[{name}] {aid}: melee without reach")
            if a.get("kind") == "ranged" and "range" not in a:
                warnings.append(f"[{name}] {aid}: ranged without range")
            for dmg in a.get("damage") or []:
                if dmg.get("type") not in DAMAGE:
                    err(errors, name, f"{aid}: damage type '{dmg.get('type')}' invalid (lowercase)")
                f = dmg.get("formula", "")
                if not re.fullmatch(r"\d+d\d+([+-]\d+)?|\d+", f):
                    err(errors, name, f"{aid}: damage formula '{f}' malformed (no spaces)")
            sv = a.get("save")
            if sv:
                if sv.get("ability") not in ABILITIES:
                    err(errors, name, f"{aid}: save ability invalid")
                if sv.get("onSave") not in ("half", "none", "negates"):
                    err(errors, name, f"{aid}: onSave must be half|none|negates")
                if sv.get("dc") not in expected_dcs:
                    warnings.append(f"[{name}] {aid}: save DC {sv.get('dc')} does not match 8 + ability mod + PB")
            if a.get("kind") == "save" and not sv:
                warnings.append(f"[{name}] {aid}: kind 'save' without save block")
            rc = a.get("recharge")
            if rc:
                if rc.get("type") not in ("dice", "perDay", "perRound"):
                    err(errors, name, f"{aid}: recharge type invalid")
                if not isinstance(rc.get("value"), int) or rc["value"] < 1:
                    err(errors, name, f"{aid}: recharge value must be a positive integer")
                elif rc.get("type") == "dice" and rc["value"] not in range(2, 7):
                    err(errors, name, f"{aid}: dice recharge value must be 2–6")
            if "legendaryCost" in a:
                err(errors, name, f"{aid}: omit legendaryCost for 2024 single-cost actions")

    la = c.get("legendaryActions")
    if la and not la.get("perRound"):
        err(errors, name, "legendaryActions without perRound")

    sc = c.get("spellcasting")
    if sc:
        if sc.get("toHit") is not None and not isinstance(sc["toHit"], int):
            err(errors, name, "spell toHit must be an integer")
        elif sc.get("toHit") is not None and sc["toHit"] not in expected_bonuses:
            warnings.append(f"[{name}] spell toHit {sc['toHit']:+d} does not match ability mod + PB")
        if sc.get("saveDc") is not None and sc["saveDc"] not in expected_dcs:
            warnings.append(f"[{name}] spell saveDc {sc['saveDc']} does not match 8 + ability mod + PB")
        for g in sc.get("groups", []):
            u = g.get("usage", {})
            if u.get("type") not in ("atWill", "perDay", "slots"):
                err(errors, name, f"spell usage type '{u.get('type')}' invalid")
            if u.get("type") == "slots" and c.get("edition") == "5.5":
                warnings.append(f"[{name}] slot-based casting on a 5.5 monster — use atWill/perDay groups")


def cmd_validate(path):
    with open(path) as f:
        data = json.load(f)
    creatures = data if isinstance(data, list) else [data]
    errors, warnings = [], []
    for c in creatures:
        check_creature(c, errors, warnings)
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(creatures)} creature(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "stats":
        cmd_stats(sys.argv[2])
    elif cmd == "show":
        cmd_show(sys.argv[2:])
    elif cmd == "validate":
        cmd_validate(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
