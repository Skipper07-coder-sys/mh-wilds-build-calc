"""Bow max-DPS local search on the MH-faithful engine (mhport).
Score = mean Dash Dance total over a monster/hitzone panel, MH default UI state.
"""
import sys, os, json, itertools, random, re
HERE = os.path.dirname(__file__)
sys.path[:0] = [os.path.join(HERE, "build_solver"), os.path.join(HERE, "damage_calc/mh_faithful"),
                os.path.join(HERE, "mathhunter")]
import mh_model as M, mhport as MP, build_link as BL

D = M.DB
PARTS = ["helm", "mail", "vambraces", "coil", "greaves"]
TABLE = {"helm": M.HELMS, "mail": M.MAIL, "vambraces": M.VAMB, "coil": M.COILS, "greaves": M.GREAVES}
PANEL = [("Arkveld", "Head"), ("Gore Magala", "Head"), ("Zoh Shia", "Head"), ("Gogmazios", "Head"),
         ("Jin Dahaad", "Head"), ("Nu Udra", "Head"), ("Uth Duna", "Head"), ("Rey Dau", "Head"),
         ("Mizutsune", "Head"), ("Rathalos", "Head")]
SEARCH_PANEL = [("Arkveld", "Head"), ("Gore Magala", "Head"), ("Rey Dau", "Head"), ("Zoh Shia", "Head")]
FULL_UP = {"Rage": 100, "CS": 100, "AdR": 100, "Peak": 100, "MM": 100, "Cure": 100, "Res": 100, "LP": 100, "Bolt": 100}
# Realistic uptime profile (our estimate, documented in the write-up)
REAL_UP = {"Rage": 60, "CS": 40, "AdR": 60, "Peak": 80, "MM": 0, "Cure": 50, "Res": 20, "LP": 50, "Bolt": 50}
UP = REAL_UP if os.environ.get("UPTIME", "real") == "real" else FULL_UP

def scenario(mon, part, up=None):
    return {"rank": "High Rank", "combo": "Dash Dance", "monster": mon, "quest": "default",
            "target_hitzone": part, "enrage_pct": 100, "wounded": False, "bow_coating": "Unequip",
            "uptime_sliders_pct": dict(up or UP), "buffs": {}}

def url(b):
    return BL.build_url({"weapon_type": "bow", "weapon": "Calamitous Angel",
        "infusions": b["inf"], "reinforcements": b["reinf"], "armor": b["armor"],
        "talisman": b["charm"], "decos": b["decos"], "focus": b["focus"],
        "set_bonus": b["wset"], "group_skill": b["wgrp"], "transcend": {p: True for p in PARTS}})

def score(b, panel=SEARCH_PANEL, up=None, detail=False):
    u = url(b)
    out = {}
    for mon, part in panel:
        out[f"{mon} {part}"] = MP.compute({"mh_link": u, "scenario": scenario(mon, part, up)})
    avg = sum(v["total"] for v in out.values()) / len(out)
    return (avg, out) if detail else avg

# ---- deco candidates: skills the calc actually reads, plus stamina floor skills
SRC = open(os.path.join(HERE, "damage_calc/mh_faithful/mhport.py")).read()
FLOOR_SKILLS = {"Constitution", "Stamina Surge"}
def relevant(rec):
    for i in (1, 2):
        s = rec.get(f"skill{i}")
        if s and (s in SRC or s in FLOOR_SKILLS or s in {"Charge Master", "Spread/Power Shots", "Tetrad Shot", "Dragon Attack"}):
            return True
    return False
ADECO = [r for r in D["equipmentdecorations"] if r.get("name") and relevant(r)]
WDECO = [r for r in D["weapondecorations"] if r.get("name") and relevant(r)]

def slots_of(part, name):
    rec = TABLE[part][name]
    return [s for s in M._eff_slots(rec, True) if s]

def skills_of(b):
    return M.resolve(url(b))

def floor_ok(b, floor):
    sk = skills_of(b)["skills"]
    return all(sk.get(k, 0) >= v for k, v in floor.items())

def fill_decos(b, floor=None, panel=SEARCH_PANEL):
    """Greedy deco fill: floor skills first (cheapest slots), then best marginal score."""
    b = json.loads(json.dumps(b))
    free = []  # (size, part, idx)
    for p in PARTS:
        for i, s in enumerate(slots_of(p, b["armor"][p])):
            free.append((s, p, i))
    b["decos"] = {p: ["", "", ""] for p in PARTS}
    b["decos"]["weapon"] = ["", "", ""]
    wfree = [(3, "weapon", i) for i in range(3)]
    # floor
    if floor:
        for _ in range(20):
            sk = skills_of(b)["skills"]
            need = [k for k, v in floor.items() if sk.get(k, 0) < v]
            if not need:
                break
            best = None
            for slot in sorted(free):
                for d in ADECO:
                    if d["slotlevel"] <= slot[0] and need[0] in (d.get("skill1"), d.get("skill2")):
                        c = (slot[0], -d.get("skill1level", 0), d["name"], slot)
                        best = c if best is None or c < best else best
                if best:
                    break
            if not best:
                return None
            _, _, dn, slot = best
            b["decos"][slot[1]][slot[2]] = dn
            free.remove(slot)
    # weapon slots then armor slots, largest first, greedy by marginal score
    for pool, cands in ((wfree, WDECO), (sorted(free, reverse=True), ADECO)):
        for slot in pool:
            base = score(b, panel)
            best, bestv = None, base
            for d in cands:
                if d["slotlevel"] > slot[0]:
                    continue
                b["decos"][slot[1]][slot[2]] = d["name"]
                v = score(b, panel)
                if v > bestv + 1e-9:
                    best, bestv = d["name"], v
            b["decos"][slot[1]][slot[2]] = best or ""
    return b

CHARMS = []
for t in D["talismans"]:
    if t.get("name") and t.get("skill1") and t.get("skill1") in SRC and not t.get("skill2"):
        CHARMS.append([(t["skill1"], t["skill1level"])])
# keep the top level of each skill only
_top = {}
for c in CHARMS:
    s, l = c[0]
    _top[s] = max(_top.get(s, 0), l)
_top["Agitator"] = 3; _top["Weakness Exploit"] = 3  # v1.041 craftable III charms (Tidus 2026-05 / mobalytics TU4); missing from MH DB table
CHARMS = [[(s, l)] for s, l in _top.items()]

REINF_SETS = []
EXS = ["Attack Boost EX", "Affinity Boost EX", "Element Boost EX"]
NONEX = ["Attack Boost III", "Affinity Boost III", "Element Boost II"]
for combo in itertools.combinations_with_replacement(EXS + NONEX, 5):
    if all(combo.count(e) <= 2 for e in EXS):
        REINF_SETS.append(list(combo))
INF_SETS = [list(c) for c in itertools.combinations_with_replacement(
    ["Dragon Attack Infusion", "Dragon Affinity Infusion"], 3)]
FOCI = [r["name"] for r in D["gogmabow"] if r.get("name")]
WSETS = [r["name"] for r in D["gogmasetbonusskills"]]
WGRPS = [r["name"] for r in D["gogmagroupskills"]]

def piece_ok(part, rec):
    if rec.get("rarity", 0) < 5:
        return False
    try:
        BL.slug(rec["name"])
    except KeyError:
        return False
    return True

def coord_descent(b, floor=None, rounds=3, log=print):
    b = fill_decos(b, floor)
    cur = score(b)
    for r in range(rounds):
        improved = False
        # weapon config
        for key, opts in (("focus", FOCI), ("wset", WSETS), ("wgrp", WGRPS), ("inf", INF_SETS), ("reinf", REINF_SETS)):
            for o in opts:
                c = dict(b); c[key] = o
                v = score(c)
                if v > cur + 1e-6 and (not floor or floor_ok(c, floor)):
                    b, cur, improved = c, v, True
        # charm
        for ch in CHARMS:
            c = dict(b); c["charm"] = ch
            c = fill_decos(c, floor)
            if c is None: continue
            v = score(c)
            if v > cur + 1e-6:
                b, cur, improved = c, v, True
                log(f"  charm -> {ch} {cur:.2f}")
        # armor
        for p in PARTS:
            for name, rec in TABLE[p].items():
                if not name or name == b["armor"][p] or not piece_ok(p, rec):
                    continue
                c = json.loads(json.dumps(b)); c["armor"][p] = name
                c["decos"][p] = ["", "", ""]
                # quick screen: keep other decos, greedy-fill only this piece
                q = quick_fill_part(c, p)
                if score(q) <= cur - 8:
                    continue
                c = fill_decos(c, floor)
                if c is None: continue
                v = score(c)
                if v > cur + 1e-6:
                    b, cur, improved = c, v, True
                    log(f"  {p} -> {name} {cur:.2f}")
        log(f"round {r}: {cur:.2f}")
        if not improved:
            break
    return b, cur

def quick_fill_part(b, p):
    b = json.loads(json.dumps(b))
    for i, s in sorted(enumerate(slots_of(p, b["armor"][p])), key=lambda x: -x[1]):
        best, bestv = "", score(b)
        for d in ADECO:
            if d["slotlevel"] > s: continue
            b["decos"][p][i] = d["name"]
            v = score(b)
            if v > bestv: best, bestv = d["name"], v
        b["decos"][p][i] = best
    return b

def from_url(u):
    P = M.parse_id(u)
    t = P["raw_tokens"]
    S = M.SLUG2NAME
    g = lambda x: S.get(x, x) if x not in ("", "?") else ""
    ch = []
    for i in (14, 16, 18):
        if t[i]: ch.append((g(t[i]), int(t[i + 1])))
    return {"inf": [g(x) for x in P["infusions"]], "reinf": [g(x) for x in P["reinf"]],
            "armor": dict(P["armor"]), "charm": ch,
            "decos": {k: list(v) for k, v in P["decos"].items()},
            "focus": g(P["focus"]), "wset": P["wset"], "wgrp": P["wgrp"]}

if __name__ == "__main__":
    seed_url = sys.argv[1]
    floor = json.loads(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    outp = sys.argv[3]
    b = from_url(seed_url)
    print("seed", score(b))
    b, v = coord_descent(b, floor)
    full, det = score(b, PANEL, detail=True)
    json.dump({"build": b, "search_score": v, "panel_avg": full, "url": url(b),
               "per": {k: x["total"] for k, x in det.items()},
               "skills": skills_of(b)["skills"],
               "set": {k: list(v) for k, v in skills_of(b)["active_setbonus"].items()},
               "grp": {k: list(v) for k, v in skills_of(b)["active_groupskill"].items()}},
              open(outp, "w"), indent=1, default=str)
    print("DONE", v, full, url(b))
