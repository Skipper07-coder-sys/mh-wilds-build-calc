# Bow: max-DPS build vs the current meta

**Game version:** Monster Hunter Wilds TU4, patch v1.041 (released 2026-02-17). That is still the latest content patch as of 2026-10-10. v1.041 made no Bow balance changes ([MP1st patch notes](https://mp1st.com/title-updates-and-patches/monster-hunter-wilds-new-update-1-041-adds-content)), and the next expansion (Ascendance) is scheduled for 2027.
**Weapon:** Calamitous Angel (Gogma Artian Bow), Dragon, Element Focus.
**Date:** 2026-10-10

> **Oracle status:** these numbers have **not yet been checked in mhwildshub.com/builder**. That site was blocked by the cloud environment this work ran in. The numbers come from the project's Math Hunter engine port (`TOOLS/damage_calc/mh_faithful/mhport.py`), which matches Math Hunter live on all 18 fixture rows (3 of them Bow) to the displayed decimal. Every build below has a Math Hunter link, so you can check any number. The mhwildshub check is the next step.

---

## TL;DR

| | Build | Realistic panel avg | vs best meta | Stamina (no meal) |
|---|---|---:|---:|---|
| ⭐ **Max DPS** | **Latent Arkvulcan** (new) | **467.4** | **+2.8%** | Con 5 / Stam Surge 3 |
| 🛡 **Robust pick** | **Gog 4P Tuned** (new) | 460.1 | +1.2% | Con 5 / Stam Surge 3 |
| Ceiling | Latent Arkvulcan, no stamina skills | 481.9 | +6.0% | none (unplayable for dash-dance) |
| Best meta | Tidus Gore/Gog DPS | 454.5 | — | Con 2 / SS 0 |

- **Latent Arkvulcan** is the highest-damage build that still runs dash-dance without food. It trades Mutual Hostility II's barrier for **Latent Power 5 + Critical Boost 3 + Lord's Soul (Guts)**. Its lead depends on how often Latent Power is up (see the uptime section).
- **Gog 4P Tuned** keeps the meta frame (Gogmapocalypse 4pc → Mutual Hostility II barrier). It swaps in a Weakness Exploit III charm and better decorations, giving +2.6% over Tidus's Gog 4P Con 5. It holds up best when uptime is poor: 440.3 pessimistic, a hair behind Gore/Gog Tuned's 440.9 and ahead of every meta build.
- All margins are 1–4%, about the same size as the uptime assumptions. These are small edges, not a different tier.

---

## Scoring setup

- **Engine:** Math Hunter `calculations.js`, ported to Python (`mhport.py`, 18/18 fixtures at 0.00% error).
- **Combo:** Dash Dance (Math Hunter's Bow steady-state loop, 3.11 s per cycle). Coating = Unequip, which is Math Hunter's default. Pierce/Close coatings would scale every build roughly equally.
- **Panel:** 10 monster heads (Arkveld, Gore Magala, Zoh Shia, Gogmazios, Jin Dahaad, Nu Udra, Uth Duna, Rey Dau, Mizutsune, Rathalos). The Dragon element is used on all of them. Score = mean damage per Dash Dance cycle.
- **No food or items** in the score. Hunter Rank, High Rank, all armor transcended.
- **Three uptime profiles.** The uptime sliders are the main way a build can look better on paper than it plays:

| Slider (skills it gates) | MH default | **Realistic** (headline) | Pessimistic |
|---|---:|---:|---:|
| Enrage (Agitator, Mutual Hostility) | 100 | 60 | 40 |
| Latent Power | 100 | 50 | 25 |
| Peak Performance (full HP) | 100 | 80 | 60 |
| Counterstrike (after being hit) | 100 | 40 | 20 |
| Adrenaline Rush (after perfect evade) | 100 | 60 | 40 |
| Frenzy cure (Antivirus / Black Eclipse) | 100 | 50 | 30 |
| Maximum Might | 100 | 0 | 0 |
| Resentment (red HP) | 100 | 20 | 0 |

The realistic and pessimistic numbers are **my estimates**, not measured values. Maximum Might is set to 0 because dash-dance spends stamina all the time.

---

## Full comparison

All numbers are mean damage per Dash Dance cycle across the 10-monster panel. **Gore 100%** is Gore Magala's head at MH-default uptime, which is the scenario earlier Math Hunter screenshots in this project used. DPS ≈ value ÷ 3.11 s.

| Build | Source | Realistic | MH default | Pessimistic | Gore 100% | Con / SS |
|---|---|---:|---:|---:|---:|---|
| ⭐ **Latent Arkvulcan** | this doc | **467.4** | 529.8 | 439.1 | 519.9 | 5 / 3 |
| 🛡 **Gog 4P Tuned** | this doc | 460.1 | 502.2 | 440.3 | 515.7 | 5 / 3 |
| Gore/Gog Tuned | this doc | 461.1 | 501.5 | **440.9** | 507.6 | 5 / 3 |
| Tidus — Gore/Gog DPS | [Tidus, "AT Arkveld Endgame Builds – TU 4.5 Bow Sets"](https://www.youtube.com/watch?v=fF_4I4Mtoa4) (Build 3) | 454.5 | 530.1 | 421.8 | 527.9 | 2 / 0 |
| Tidus — Gog 4P DPS | same video (Build 1) | 453.4 | 497.0 | 430.8 | 509.9 | 3 / 2 (+Black Belt meal) |
| Tidus — Gog 4P Con 5 | same video (Build 2) | 448.3 | 486.0 | 428.0 | 500.8 | 5 / 3 |
| Mobalytics TU4 Endgame Bow | [Mobalytics, updated 2026-01-09](https://mobalytics.gg/mhw/builds/endgame-bow-meta) | 444.8 | 478.6 | 425.1 | 490.3 | 5 / 3 |
| Speedrun "Proof of a Hero" frame | project ingest of speedrun screenshots, 2026-05-19 | 455.6 | 531.1 | 423.9 | 514.1 | 4 / 0 |
| Gore-bow experimental | project, user-designed 2026-05-19 | 451.4 | 517.8 | 424.2 | 516.9 | 5 / 0 |

**How the meta builds were reconstructed:**
- Tidus builds come from the video's screenshots (transcribed in `RESEARCH/ingested/bow-tidus-builds-at-arkveld-2026-05-19.md`). Build 2's link is the user-verified one. Builds 1 and 3 were rebuilt from the piece and decoration tables, so their resolved skills differ by about one level from the video in a few places (Build 1: Burst 3 vs 5; Build 3: Constitution 2 vs 3).
- Mobalytics lists a Fire bow. I converted it to Dragon (Dragon/Bandolier jewel) so it shares the panel. Its empty slots are filled with the Tenderizer, Physique and Refresh jewels the guide itself recommends.
- **Reading the table:** at MH-default 100% uptime, the Gore/Gog and speedrun frames tie Latent Arkvulcan. They get there by skipping Stamina Surge and most Constitution. Once enrage, Counterstrike and Adrenaline Rush are not always up, the stamina-legal new builds pull ahead.

---

## ⭐ Build 1: Latent Arkvulcan (max DPS, no meal needed)

[Open in Math Hunter](https://www.mathhunter.ca/bow.html?id=calamitousangel;dragonattackinfusion;dragonattackinfusion;dragonattackinfusion;attackboostex;attackboostex;attackboostiii;attackboostiii;attackboostiii;arkvulcanhelmgamma;gogmaziosmailbeta;arkvulcanvambracesgamma;gogmazioscoilalpha;gogmaziosgreavesalpha;latentpower;3;;;;;dragonopenerjewel;criticaljeweliii;spreadjewel;refreshjewel;physiquejewel;;throttlejewel;counterjewel;;physiquejewel;;;refreshjewel;physiquejewel;physiquejewel;throttlejewel;refreshjewel;physiquejewel;;;;elementfocus;rathalossflare;lordssoul;2;2;2;2;2;?)

**Weapon:** Calamitous Angel, Dragon, **Element Focus**
- Infusions: 3× Dragon Attack Infusion
- Reinforcements: Attack Boost EX ×2, Attack Boost III ×3. Respects the max-2-EX-per-type rule.
- Gogma roll: **Rathalos's Flare** (set) + **Lord's Soul** (group)
- Weapon decorations: Dragon/Opener Jewel [3], Critical Jewel III [3], Spread Jewel [3]

| Slot | Piece | Decorations |
|---|---|---|
| Head | Arkvulcan Helm γ | Refresh [2], Physique [1], *free* |
| Chest | Gogmazios Mail β | Throttle [3], Counter [2], *free* |
| Arms | Arkvulcan Vambraces γ | Physique [1], *free*, *free* |
| Waist | Gogmazios Coil α | Refresh [2], Physique [1], Physique [1] |
| Legs | Gogmazios Greaves α | Throttle [3], Refresh [2], Physique [1] |
| Charm | **Latent Power Charm III** (craftable) | — |
| Mantle | Evasion Mantle | — |

The four *free* slots add no damage in this build. Use them for comfort, such as Divine Blessing or resistances.

**Skills:** Weakness Exploit 5 · **Latent Power 5** · Constitution 5 · Stamina Surge 3 · Critical Boost 3 · Dragon Attack 3 · Peak Performance 3 · Adrenaline Rush 2 · Burst 2 · Flayer 2 · Speed Eating 2 · Agitator 1 · Counterstrike 1 · Opening Shot 1 · Spread/Power Shots 1 · Aquatic Mobility 1
**Set bonuses:** Gogmapocalypse 3 → **Mutual Hostility I** · Rathalos's Flare 2 → **Scorcher I** · Arkveld's Hunger 2 → **Hasten Recovery I** (HP on hit) · Lord's Soul 3 → **Guts** (survive one lethal hit) and +5% raw

**Why it wins:** Latent Power 5 adds +50% affinity. Together with Weakness Exploit and Critical Boost 3 (crit hits ×1.34), the build gets crit value that Gog 4P frames, sitting near 0% affinity, never reach. Lord's Soul supplies a ×1.05 raw multiplier plus Guts, which partly makes up for losing the Mutual Hostility II barrier.

---

## 🛡 Build 2: Gog 4P Tuned (meta frame, keeps the barrier)

[Open in Math Hunter](https://www.mathhunter.ca/bow.html?id=calamitousangel;dragonattackinfusion;dragonattackinfusion;dragonattackinfusion;attackboostex;attackboostex;elementboostex;elementboostex;attackboostiii;gebonyhelmbeta;gogmaziosmailbeta;grathalosvambracesbeta;gogmazioscoilalpha;gogmaziosgreavesbeta;weaknessexploit;3;;;;;dragonopenerjewel;spreadjewel;chargejeweliii;flawlessjewel;physiquejewel;;counterjewel;refreshjewel;;tenderizerjewel;counterjewel;physiquejewel;refreshjewel;physiquejewel;physiquejewel;flawlessjewel;refreshjewel;physiquejewel;;;;elementfocus;gogmapocalypse;;2;2;2;2;2;?)

**Weapon:** Calamitous Angel, Dragon, Element Focus. Infusions: 3× Dragon Attack. Reinforcements: Attack Boost EX ×2, Element Boost EX ×2, Attack Boost III. Gogma roll: **Gogmapocalypse**. Weapon decorations: Dragon/Opener [3], Spread [3], Charge Jewel III [3].

| Slot | Piece | Decorations |
|---|---|---|
| Head | G. Ebony Helm β | Flawless [2], Physique [1] |
| Chest | Gogmazios Mail β | Counter [2], Refresh [2] |
| Arms | G. Rathalos Vambraces β | Tenderizer [3], Counter [2], Physique [1] |
| Waist | Gogmazios Coil α | Refresh [2], Physique [1], Physique [1] |
| Legs | Gogmazios Greaves β | Flawless [2], Refresh [2], Physique [1] |
| Charm | **Weakness Exploit Charm III** (craftable) | — |

**Skills:** Weakness Exploit 5 · Peak Performance 5 · Constitution 5 · Stamina Surge 3 · Burst 4 · Charge Master 3 · Dragon Attack 3 · Adrenaline Rush 2 · Counterstrike 2 · Speed Eating 2 · Agitator 1 · Opening Shot 1 · Spread/Power Shots 1
**Set bonuses:** Gogmapocalypse 4 → **Mutual Hostility II** (+30% element, +40 flat element and a 75-HP barrier while the monster is enraged) · Ebony Odogaron's Power 2 → Burst Boost I · Rathalos's Flare 2 → Scorcher I

**Change from Tidus Gog 4P Con 5:** the Agitator III charm becomes **Weakness Exploit III**. Weakness Exploit is then capped from the charm alone, which frees three Tenderizer slots for Peak Performance 5 (Flawless) and Counterstrike 2. Agitator drops to 1. Agitator only pays while enraged, so the swap gains the most when enrage uptime is low. Result: **+2.6%** realistic, **+2.9%** pessimistic over the build it replaces.

---

## The damage maths (Latent Arkvulcan, Gore Magala head, realistic uptime)

The engine applies Math Hunter's formula hit by hit across the Dash Dance cycle (`MH_FORMULA.md`). These are the build-level inputs it produced:

**1. Raw**
```
preRaw        = 190 (base) + 66 (3× Dragon Attack Infusion + reinforcements + focus)   = 256
trueRaw       = preRaw × 1.05 (Lord's Soul 3pc)                                         = 268.8
fixedAdditions (uptime-weighted flat raw):
    Peak Performance 3   10 × 0.80 = 8
    Adrenaline Rush 2    15 × 0.60 = 9
    Counterstrike 1      10 × 0.40 = 4
    Agitator 1            4 × 0.60 = 2
    Opening Shot 1                  5      ← MH applies this to every shot; in game it is the first shot only (overstated)
                                   ---- 28   (44 at MH-default 100%)
attack used   = round(trueRaw) + fixedAdditions + Burst addition       = 269 + 28 + Burst
```

**2. Affinity and crit**
```
affinity      = 27%  (realistic)   /   53% at 100% uptime
              difference = Latent Power 5 (+50% × 0.50 uptime) + Agitator (+3% × 0.60)
crit dmg      = 0.25 base + 0.09 (Critical Boost 3) = 0.34
crit factor   = 1 + 0.34 × 0.27 = 1.092   (1.180 at 100% uptime)
```

**3. Per hit** (Math Hunter, `calculations.js` ~7678)
```
raw hit  = round( attack × bowCriticalRange × crit factor × hitzone/100 × MV/100 × Spread/Power Shots 1.05 )
ele hit  = min( (dragon × Dragon Attack 3 × Mutual Hostility I) + flat additions, element cap )
           × element hitzone × crit-element factor
```

**4. One Dash Dance cycle on Gore Magala's head**

| Component | Realistic | MH default (100%) |
|---|---:|---:|
| Raw | 347.3 | 393.2 |
| Dragon element | 93.3 | 100.3 |
| Scorcher I | 18.1 | 18.7 |
| Flayer | 6.9 | 7.7 |
| **Total per cycle** | **465.7** | **519.9** |
| ≈ DPS (÷ 3.11 s) | ≈ 150 | ≈ 167 |

For comparison, Gog 4P Tuned on the same target is **478.0 realistic** (raw 303.1 / element 156.0 / Scorcher 18.9). It wins on Gore Magala because Mutual Hostility II's element boost lands well on a dragon-weak head. Latent Arkvulcan wins the 10-monster average because its raw and crit lead carries over to targets with weaker dragon hitzones.

---

## Skills with uptime conditions ⚠️

Change in panel average when each slider goes from realistic to 0% or to 100%:

| Condition | Skills it gates | Latent Arkvulcan (0% / 100%) | Gog 4P Tuned (0% / 100%) |
|---|---|---:|---:|
| **Monster enraged** | Agitator, Mutual Hostility I/II (and its barrier) | −20.4 / +15.0 | **−29.7 / +20.5** |
| **Latent Power active** (triggers after about 2 min in the fight or after taking 130 HP of damage, per Mobalytics; limited duration, 50 s cooldown at Lv 3+) | Latent Power | **−27.3 / +27.7** | — |
| **Full HP** | Peak Performance | −10.1 / +2.8 | −18.0 / +4.5 |
| **Perfect evade** | Adrenaline Rush | −11.2 / +7.9 | −10.2 / +6.9 |
| **After being hit** | Counterstrike | −5.1 / +7.9 | −6.6 / +10.1 |
| Consecutive hits | Burst, Burst Boost | MH assumes full Burst (no slider) | same |
| First shot only | Opening Shot | overstated by MH | same |
| Wounded part | Flayer | MH models it as on | — |

**What this means:**
- **Latent Power is the swing skill.** At 25% Latent uptime, Latent Arkvulcan falls to roughly a tie with Gog 4P Tuned (see the pessimistic column). Treat it as the max-DPS build for long fights and Gog 4P Tuned as the safer default.
- **Gog 4P depends most on enrage.** Mutual Hostility II is worth about 30 points per cycle, and only while the monster is enraged.
- **Uptime-free damage:** Weakness Exploit (weak-point hits), Critical Boost, Dragon Attack, Charge Master, Spread/Power Shots, Lord's Soul's ×1.05 and Scorcher.

---

## Reproduce

```bash
# from the project folder (MHWilds/), after copying tools/bow_opt.py into TOOLS/
python3 TOOLS/bow_opt.py "<seed Math Hunter link>" '{"Constitution":5,"Stamina Surge":3}' out.json
UPTIME=full python3 TOOLS/bow_opt.py ...   # MH-default 100% uptime
```

`tools/bow_opt.py` runs a coordinate-descent search. It covers every R5+ armor piece per slot, craftable charms, Artian infusions, reinforcements (max 2 EX per type), Gogma focus, set and group rolls, and a greedy decoration fill, all scored by the Math Hunter port. Seeds were Tidus Gog 4P Con 5, the Gore-bow experimental and the speedrun frame. The full results are in `tools/bow-compare-2026-10-10.json`.

## Known gaps

- **mhwildshub.com/builder** has not checked these numbers yet. It was blocked in this environment.
- Charms are craftable only. A god (Timeworn or appraised) charm would lift every build. Tidus's acceptance criteria are in the project's Bow ingest.
- Agitator Charm III and Weakness Exploit Charm III are missing from Math Hunter's charm table, but Math Hunter's links accept them. Both are v1.041 craftables according to Tidus and Mobalytics.
- The panel uses Dragon on every monster. In real hunts you would switch element per monster.
