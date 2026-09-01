# Balancing against the official books

The yardstick is the SRD 5.2 (2024) bestiary itself, not an abstract table. The method:

1. `scripts/benchmark.py stats <CR>` — the empirical row for that CR plus every SRD creature at it.
2. Pick 2–3 comparables with the same role (brute, skirmisher, artillery, controller, support, solo boss) and `scripts/benchmark.py show <name>` each.
3. Land the new monster inside the envelope the comparables define. Trade along the defensive axis (high AC ↔ low HP) and the offensive axis (accuracy ↔ damage ↔ control); a monster above the curve on one axis sits below it on another.
4. Estimate damage per round yourself: sum the average damage of the multiattack routine (count limited-use novas at partial weight — a Recharge 5–6 breath is ~1/3 of rounds). Compare against what the comparables actually deal, not a formula.

Solo/boss monsters run above the single-monster curve: Legendary Resistance (2/Day at low CR, 3/Day standard), a legendary action budget of 3/round, and HP toward the top of the range. Monsters designed to appear in numbers run lean: fewer riders, no recharge, simpler turns.

## Empirical benchmarks — SRD 5.2, 330 creatures

Medians per CR; HP as median with full range. "hit" = best attack bonus, "DC" = best save DC.

| CR | n | AC | HP | HP range | hit | DC |
|---|---|---|---|---|---|---|
| 0 | 29 | 12 | 3 | 1–13 | +2 | — |
| 1/8 | 19 | 12 | 9 | 5–17 | +4 | — |
| 1/4 | 32 | 12 | 13 | 9–22 | +4 | 10–11 |
| 1/2 | 27 | 12 | 21 | 11–33 | +4 | 11 |
| 1 | 27 | 13 | 26 | 21–45 | +5 | 11 |
| 2 | 42 | 13 | 45 | 27–85 | +5 | 12 |
| 3 | 25 | 15 | 65 | 45–90 | +5 | 12 |
| 4 | 16 | 15 | 76 | 45–120 | +6 | 13 |
| 5 | 25 | 15 | 104 | 67–147 | +7 | 14–15 |
| 6 | 11 | 15 | 123 | 81–152 | +7 | 14–15 |
| 7 | 6 | 17 | 126 | 119–168 | +7 | 14 |
| 8 | 10 | 16 | 136 | 85–184 | +7 | 14–15 |
| 9 | 8 | 16 | 162 | 123–200 | +9/+10 | 16–17 |
| 10 | 6 | 18 | 178 | 136–229 | +9/+10 | 17 |
| 11 | 7 | 17 | 199 | 168–248 | +10 | 17 |
| 12 | 2 | 18 | 174 | 170–178 | +8/+9 | 16–17 |
| 13 | 6 | 18 | 198 | 172–230 | +10/+11 | 18 |
| 14 | 3 | 18 | 195 | 184–228 | +11 | 18 |
| 15 | 4 | 18 | 210 | 187–247 | +11/+12 | 18 |
| 16 | 5 | 19 | 220 | 212–262 | +12 | 19 |
| 17 | 4 | 19 | 250 | 199–356 | +13/+14 | 20–21 |
| 19 | 1 | 19 | 287 | — | +14 | — |
| 20 | 3 | 20 | 333 | 332–337 | +14 | 21–22 |
| 21 | 4 | 21 | 341 | 297–367 | +15 | 22 |
| 22 | 2 | 22 | 423 | 402–444 | +15/+16 | 22–23 |
| 23 | 3 | 22 | 481 | 468–481 | +17 | 24 |
| 24 | 2 | 22 | 526 | 507–546 | +17 | 24 |
| 30 | 1 | 25 | 697 | — | +19 | 27 |

Sparse rows (n ≤ 3) are weak evidence — lean on adjacent CRs and on the comparables. CR 12's dip is an artifact of n=2.

## Norms measured from the SRD 5.2

**Reach** (per attack): Tiny–Medium 5 ft. (10 is rare — 9 of 125 Medium). Large 5 or 10; 15 is exceptional (1 of 106: Aboleth). Huge mostly 10, occasionally 15 (3 of 34). Gargantuan 15 standard; only Kraken and Tarrasque exceed it. Exceed these only with a stated precedent and a body plan that earns it.

**Areas**: SRD creature areas vary too widely to be a norm (Emanation medians 10–30 ft., maxima to 500). Use spells as the yardstick instead — a damaging Sphere sits at 20 ft. from levels 2–5 and reaches 60 only at 6th. Breath-style Cones scale 15 → 30 → 60 → 90 ft. with CR tier.

**Speeds**: 30 ft. walk is the default; 20 for the slow and shambling, 40 for fast skirmishers. Fly usually 1.5–2× walk.

## Frequently forgotten

- Condition immunities that follow from the concept (constructs: Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned — plus Poison immunity; undead: Exhaustion, Poisoned as a floor).
- Passive Perception = 10 + Perception bonus (skill bonus if proficient, else Wis mod).
- A save-proficient stat means the `saves` entry AND the header math must both exist.
- `Medium or Small` for player-species humanoids, not plain `Medium`.
- Fraction CRs are decimals in JSON (`0.25`), fractions in display (`1/4`).
