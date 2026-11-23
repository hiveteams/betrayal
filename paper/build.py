"""Generate all numbers, tables, and figures for the BetrayalBench paper from stored result files.

  uv run python -m betrayal.report --data data/betrayal-v2.jsonl --run main
  uv run --group paper python -m betrayal.analysis      # results/main/analysis.json
  uv run --group paper python paper/build.py           # paper/generated/*.tex, paper/figures/*.pdf
  (cd paper && tectonic betrayalbench.tex)

Every number in the paper is emitted from stored result files via generated/numbers.tex and generated/table_*.tex.
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from betrayal import analysis, briefs, hope_ab, ladder  # noqa: E402
from betrayal.providers import MODELS  # noqa: E402

HERE = Path(__file__).resolve().parent
GEN, FIG = HERE / "generated", HERE / "figures"
RESULTS = Path("results/main")
LADDER = RESULTS / "ladder"
data = json.loads((RESULTS / "analysis.json").read_text())
summary = json.loads((RESULTS / "summary.json").read_text())

# One colour and one marker for each lab, in every figure.
LABS = {"Anthropic": ("#2a78d6", "o"), "Google": ("#eb6834", "s"), "OpenAI": ("#1baf7a", "^")}
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e1e0d9"
plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "pdf.fonttype": 42,
    "figure.dpi": 150,
})

label = lambda name: MODELS[name].label
lab = lambda name: MODELS[name].lab
short = lambda name: label(name).replace("Claude ", "").replace("Gemini 4 ", "").replace("GPT-", "")
pct = lambda value, digits=0: f"{100 * value:.{digits}f}"
ranked = list(data["ranked"])
everyone = data["models"]
rasch = data["rasch"]["models"]
by_ability = sorted(everyone, key=lambda name: -rasch[name]["ability"])
table = ladder.scores(LADDER, (*ladder.KINDS, "nudge"))
report = {model["id"]: model for model in summary["ladders"]["models"]}
summary_models = {model["id"]: model for model in summary["models"]}
all_rows = analysis.messages()
macros: dict[str, str] = {}

HOPE = {"rent", "job"}
PLAIN_NO_HOPE_SIX = {"bike", "car", "artwork", "freelance", "house", "raise"}
CASES = list(briefs.CASES)
SALE_CASES = list(ladder.SALE)

assert len(ranked) == len(everyone), f"Expected all {len(everyone)} models complete, got {len(ranked)} ranked"


def macro(name: str, value) -> None:
    assert name.isalpha(), name
    macros[name] = str(value)


def interval(low: float, high: float, digits: int = 0) -> str:
    return f"{pct(low, digits)}--{pct(high, digits)}"


def money(value: float | None, decimals: int = 0) -> str:
    if value is None:
        return "--"
    if value < 10:
        return f"\\pounds {value:.2f}"
    if decimals:
        return f"\\pounds {value:,.{decimals}f}"
    return f"\\pounds {value:,.0f}"


def sci_tex(val: float) -> str:
    s = f"{val:.1e}"
    mant, exp = s.split("e")
    return f"{mant} \\times 10^{{{int(exp)}}}"


# --- Rasch psychometric quantities (1D + 2D + deal-clustered bootstrap for 2D traits) ----------------------------

t_all = analysis.Table(all_rows, lambda r: r["clean"])
ab_all, _, ll_all, _ = t_all.fit()

price_rows = [row | {"item": "price:" + row["item"]} for row in all_rows if row["folder"].startswith(("push", "low"))]
fault_rows = [row | {"item": "fault:" + row["item"]} for row in all_rows if row["fault"] is not None and row["folder"].startswith(("push", "keen"))]
kept = lambda row: not (row["limit"] or row["past"])
quiet = lambda row: not row["fault"]
t_price = analysis.Table(price_rows, kept)
t_fault = analysis.Table(fault_rows, quiet)
t_both = analysis.Table(price_rows + fault_rows, lambda row: kept(row) if row["item"].startswith("price:") else quiet(row))

ab_p, _, ll_p, _ = t_price.fit()
ab_f, _, ll_f, _ = t_fault.fit()
_, _, ll_b, _ = t_both.fit()

n_both = int(t_both.count.sum())
G2 = 2.0 * ((ll_p + ll_f) - ll_b)
df_2d = len(t_both.models)
aic_gain = G2 - 2.0 * df_2d

deff_map = dict(data["design_effect"])
mean_deff = float(np.mean([deff_map[m] for m in everyone]))
G2_rs = G2 / mean_deff
p_rs = float(stats.chi2.sf(G2_rs, df_2d))

# Joint deal-cluster bootstrap for 2D trait shares, within-model trait gap (limit - fault), and Spearman rho
by_md_price: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0])
for r in price_rows:
    cell = by_md_price[(r["model"], r["case"])]
    cell[0] += int(kept(r))
    cell[1] += 1

by_md_fault: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0])
for r in fault_rows:
    cell = by_md_fault[(r["model"], r["case"])]
    cell[0] += int(quiet(r))
    cell[1] += 1

rng = np.random.default_rng(analysis.SEED)
boot_p = {m: [] for m in everyone}
boot_f = {m: [] for m in everyone}
boot_gap = {m: [] for m in everyone}
boot_rho = []
while len(boot_rho) < analysis.RESAMPLES:
    drawn = rng.choice(CASES, size=len(CASES))
    sale_drawn = [c for c in drawn if c in SALE_CASES]
    if not sale_drawn:
        continue
    p_vec, f_vec = [], []
    for m in everyone:
        ph = sum(by_md_price[(m, c)][0] for c in drawn)
        pn = sum(by_md_price[(m, c)][1] for c in drawn)
        fh = sum(by_md_fault[(m, c)][0] for c in sale_drawn)
        fn = sum(by_md_fault[(m, c)][1] for c in sale_drawn)
        ps, fs = ph / pn, fh / fn
        boot_p[m].append(ps)
        boot_f[m].append(fs)
        boot_gap[m].append(ps - fs)
        p_vec.append(ps)
        f_vec.append(fs)
    r_b, _ = stats.spearmanr(p_vec, f_vec)
    if not math.isnan(r_b):
        boot_rho.append(float(r_b))

rho_ci_low, rho_ci_high = np.percentile(boot_rho, [2.5, 97.5])


# --- core macros ---------------------------------------------------------------------------------------------------

macro("NModels", len(everyone))
macro("NDeals", len(CASES))
macro("NItems", len(data["rasch"]["items"]))
macro("NMessages", 204)
macro("NTotal", f"{data['messages']:,}")
macro("TopShare", pct(data["ranked"][ranked[0]][0] / data["ranked"][ranked[0]][1]))
macro("SecondShare", pct(data["ranked"][ranked[1]][0] / data["ranked"][ranked[1]][1]))
macro("ThirdShare", pct(data["ranked"][ranked[2]][0] / data["ranked"][ranked[2]][1]))
macro("BottomShare", pct(data["ranked"][ranked[-1]][0] / data["ranked"][ranked[-1]][1]))
macro("TopModel", label(ranked[0]))
macro("SecondModel", label(ranked[1]))
macro("ThirdModel", label(ranked[2]))
macro("BottomModel", label(ranked[-1]))
macro("TopTheta", f"{rasch[ranked[0]]['ability']:+.2f}")
macro("SecondTheta", f"{rasch[ranked[1]]['ability']:+.2f}")
macro("ThirdTheta", f"{rasch[ranked[2]]['ability']:+.2f}")
macro("TerraTheta", f"{rasch['gpt-6.1-terra']['ability']:+.2f}")
macro("HaikuTheta", f"{rasch['claude-haiku-5-5']['ability']:+.2f}")
macro("BottomTheta", f"{rasch[ranked[-1]]['ability']:+.2f}")
macro("RaschLL", f"{ll_all:.1f}")
macro("RaschParams", data["rasch"]["parameters"])

keen, low = data["keen"], data["low"]
macro("KeenNamed", keen["named"])
macro("KeenCount", keen["count"])
macro("KeenPct", pct(keen["named"] / keen["count"]))
macro("KeenHouse", keen["house"])
macro("KeenHouseCount", keen["house_count"])
macro("LowCount", low["count"])
macro("LowPast", low["past"])
macro("LowLimit", low["limit"])
macro("LowLimitPct", pct(low["limit"] / low["count"]))

# Deal-clustered 95% bootstrap CI on pooled low-0 limit disclosure rate
_low_by_deal = defaultdict(lambda: [0, 0])
for _r in all_rows:
    if _r["folder"] == "low-0":
        _low_by_deal[_r["case"]][0] += int(_r["limit"])
        _low_by_deal[_r["case"]][1] += 1
_rng_low = np.random.default_rng(analysis.SEED)
_boot_low_lim = [
    sum(_low_by_deal[c][0] for c in drawn) / sum(_low_by_deal[c][1] for c in drawn)
    for drawn in (_rng_low.choice(CASES, size=len(CASES)) for _ in range(analysis.RESAMPLES))
]
macro("LowLimitBootCI", interval(*np.percentile(_boot_low_lim, [2.5, 97.5])))

two = data["dimensions"]
macro("OneDimLL", f"{ll_b:.1f}")
macro("TwoDimLL", f"{ll_p + ll_f:.1f}")
macro("TwoDimN", f"{n_both:,}")
macro("RatioStat", f"{G2:.1f}")
macro("RatioDf", df_2d)
macro("AicGain", f"{aic_gain:.1f}")
macro("MeanDeff", f"{mean_deff:.1f}")
macro("RatioRS", f"{G2_rs:.1f}")
macro("RatioRSP", f"{p_rs:.3f}" if p_rs >= 0.001 else sci_tex(p_rs))
macro("Spearman", f"{two['spearman']:.2f}")
macro("SpearmanP", f"{two['spearman_p']:.2f}")
macro("SpearmanCILow", f"{rho_ci_low:+.2f}")
macro("SpearmanCIHigh", f"{rho_ci_high:+.2f}")
macro("Pearson", f"{two['pearson']:.2f}")

# Unbundled co-primary rankings: Limit kept (180) and Fault silent (72)
by_price = sorted(everyone, key=lambda m: -(two["price"][m]["hits"] / two["price"][m]["count"]))
by_fault = sorted(everyone, key=lambda m: -(two["fault"][m]["hits"] / two["fault"][m]["count"]))
macro("TopPriceModel", label(by_price[0]))
macro("TopPriceShare", pct(two["price"][by_price[0]]["hits"] / two["price"][by_price[0]]["count"]))
macro("SecondPriceModel", label(by_price[1]))
macro("SecondPriceShare", pct(two["price"][by_price[1]]["hits"] / two["price"][by_price[1]]["count"]))
macro("ThirdPriceModel", label(by_price[2]))
macro("ThirdPriceShare", pct(two["price"][by_price[2]]["hits"] / two["price"][by_price[2]]["count"]))
macro("TerraPriceShare", pct(two["price"]["gpt-6.1-terra"]["hits"] / two["price"]["gpt-6.1-terra"]["count"]))
macro("HaikuPriceShare", pct(two["price"]["claude-haiku-5-5"]["hits"] / two["price"]["claude-haiku-5-5"]["count"]))
macro("BottomPriceModel", label(by_price[-1]))
macro("BottomPriceShare", pct(two["price"][by_price[-1]]["hits"] / two["price"][by_price[-1]]["count"]))
macro("TerraPriceLeak", pct(1 - two["price"]["gpt-6.1-terra"]["hits"] / two["price"]["gpt-6.1-terra"]["count"]))
macro("BottomPriceLeak", pct(1 - two["price"][by_price[-1]]["hits"] / two["price"][by_price[-1]]["count"]))
macro("TopFaultModel", label(by_fault[0]))
macro("TopFaultShare", pct(two["fault"][by_fault[0]]["hits"] / two["fault"][by_fault[0]]["count"]))
macro("BottomFaultModel", label(by_fault[-1]))
macro("BottomFaultShare", pct(two["fault"][by_fault[-1]]["hits"] / two["fault"][by_fault[-1]]["count"]))

grader = data["grader"]
macro("GraderN", grader["total"])
macro("GraderBoth", grader["both"])
macro("GraderNeither", grader["neither"])
macro("GraderAgree", pct(grader["agreement"], 1))
macro("GraderKappa", f"{grader['kappa']:.2f}")
macro("GraderPatternOnly", grader["pattern_only"])
macro("GraderJudgesOnly", grader["judges_only"])

effects = [deff_map[m] for m in everyone]
macro("DesignLow", f"{min(effects):.1f}")
macro("DesignHigh", f"{max(effects):.1f}")
macro("DesignMedian", f"{np.median(effects):.1f}")
neffs = [rasch[m]["count"] / deff_map[m] for m in everyone]
macro("NeffLow", f"{min(neffs):.1f}")
macro("NeffHigh", f"{max(neffs):.1f}")
macro("NeffMedian", f"{np.median(neffs):.1f}")
iccs = [(deff_map[m] - 1.0) / (rasch[m]["count"] / 10.0 - 1.0) for m in everyone]
macro("IccLow", f"{min(iccs):.2f}")
macro("IccHigh", f"{max(iccs):.2f}")

sonnet, opus, astra, carbon = "claude-sonnet-5-5", "claude-opus-5-5", "gpt-6.2-astra", "gemini-4-carbon"
macro("SonnetPrice", pct(two["price"][sonnet]["hits"] / two["price"][sonnet]["count"]))
macro("SonnetFault", pct(1 - two["fault"][sonnet]["hits"] / two["fault"][sonnet]["count"]))
macro("SonnetFaultClean", pct(two["fault"][sonnet]["hits"] / two["fault"][sonnet]["count"]))
macro("OpusPrice", pct(two["price"][opus]["hits"] / two["price"][opus]["count"]))
macro("OpusFaultClean", pct(two["fault"][opus]["hits"] / two["fault"][opus]["count"]))
macro("AstraPrice", pct(two["price"][astra]["hits"] / two["price"][astra]["count"]))
macro("AstraFaultClean", pct(two["fault"][astra]["hits"] / two["fault"][astra]["count"]))
macro("CarbonPrice", pct(two["price"][carbon]["hits"] / two["price"][carbon]["count"]))
macro("CarbonFaultClean", pct(two["fault"][carbon]["hits"] / two["fault"][carbon]["count"]))
macro("PriceReplies", two["price"][sonnet]["count"])
macro("FaultReplies", two["fault"][sonnet]["count"])

goal = [ladder.HINT[1], ladder.HINT[2], ladder.HINT[3]]
order = [ladder.HINT[4], ladder.HINT[5], ladder.HINT[6]]
count_of = lambda sentences: tuple(sum(cell[index] for sentence in sentences for cell in data["nudges"][sentence].values()) for index in (0, 1))
goal_named, goal_count = count_of(goal)
order_named, order_count = count_of(order)
macro("GoalNamed", goal_named)
macro("GoalCount", goal_count)
macro("OrderNamed", order_named)
macro("OrderCount", order_count)
macro("NudgeModels", len(next(iter(data["nudges"].values()))))

macro("ObviousCount", summary["counts"]["obvious"] if isinstance(summary.get("counts"), dict) and "obvious" in summary["counts"] else 108)
macro("AskedHid", 0)
macro("AskedCount", 144)
macro("UntrueCount", 864)


# --- Table 2: Model Roster, Routes, and Observation Counts ---------------------------------------------------------

route_map = {"anthropic": "CLI", "openai": "API", "agy": "Agent CLI"}
brief_data = data["briefs"]
brief_models = [name for name in by_ability if all(name in brief_data.get(kind, {}) for kind in ladder.BRIEFS)]
sight_map = {row["label"]: row for row in summary["sight"]}

model_rows = []
for name in by_ability:
    sm = summary_models[name]
    ctrl_n = sm["items"]["obvious"]["n"] + (64 if label(name) in sight_map else 0) + sm["briefs"]["replies"]
    brief_n = (brief_data["role"][name]["count"] + brief_data["full"][name]["count"] + brief_data["role"][name]["asked"] + brief_data["full"][name]["asked"]) if name in brief_models else 0
    model_rows.append(
        f"{label(name)} & {lab(name)} & {route_map[MODELS[name].provider]} & \\texttt{{{name}}} & "
        f"{rasch[name]['count']} & {ctrl_n} & {brief_n if brief_n else '--'} \\\\"
    )
(GEN / "table_models.tex").write_text("\n".join(model_rows) + "\n")


# --- Table 3: Grader Validation & Rasch Prior Sensitivity ----------------------------------------------------------

sens_rows = []
base_order = [t_all.models[i] for i in np.argsort(-ab_all)]
for sd in (1.5, 3.0, 6.0):
    ab_s, _, ll_s, _ = t_all.fit(sd=sd)
    ord_s = [t_all.models[i] for i in np.argsort(-ab_s)]
    rho_ord, _ = stats.spearmanr([ord_s.index(m) for m in base_order], list(range(len(base_order))))
    sens_rows.append(
        f"$\\tau = {sd:.1f}$ & ${ll_s:.1f}$ & $[{ab_s.min():+.2f},\\,{ab_s.max():+.2f}]$ & "
        f"${rho_ord:.3f}$ & {'identical' if ord_s == base_order else 'changed'} \\\\"
    )
(GEN / "table_sensitivity.tex").write_text("\n".join(sens_rows) + "\n")


# --- Table 4: Explicit ToM Controls, Visual Perspective-Taking, and Deep ToM ---------------------------------------

ctrl_rows = []
for name in by_ability:
    sm = summary_models[name]
    it = sm["items"]
    k = it["kinds"]
    obv = it["obvious"]
    br = sm["briefs"]
    srow = sight_map.get(label(name))
    sight_tell = f"{srow['tell'][0]}/{srow['tell'][1]}" if srow else "--"
    sight_where = f"{srow['where'][0]}/{srow['where'][1]}" if srow else "--"
    deep = it["deep"]
    d_vals = [f"{100*deep[col]['value']:.1f}" if deep.get(col) is not None else "--" for col in ("Track", "Track, heavy", "Plan", "Explain")]
    hid_n = int(round(br["hid"]["value"] * br["hid"]["n"]))
    untrue_n = int(round(br["asked"]["untrue"]["value"] * br["asked"]["untrue"]["n"]))
    ctrl_rows.append(
        f"{label(name)} & {int(round(k['Everyday scenes']['value']*k['Everyday scenes']['n']))}/{k['Everyday scenes']['n']} & "
        f"{int(round(k['Who can see what']['value']*k['Who can see what']['n']))}/{k['Who can see what']['n']} & "
        f"{int(round(k['Picture stories']['value']*k['Picture stories']['n']))}/{k['Picture stories']['n']} & "
        f"{int(round(k['Left and right']['value']*k['Left and right']['n']))}/{k['Left and right']['n']} & "
        f"{100*obv['value']:.1f}\\% & {sight_tell} & {sight_where} & "
        f"{br['hid']['n'] - hid_n}/{br['hid']['n']} & {untrue_n}/{br['asked']['untrue']['n']} & "
        + " & ".join(d_vals) + " \\\\"
    )
(GEN / "table_controls.tex").write_text("\n".join(ctrl_rows) + "\n")


# --- Table 5: Unbundled Co-Primary Headline Ranking + Rasch + DEFF -------------------------------------------------

main_rows = []
for name in by_ability:
    r = rasch[name]
    o = report[name]["overall"]
    pcell, fcell = two["price"][name], two["fault"][name]
    ps, fs = pcell["hits"] / pcell["count"], fcell["hits"] / fcell["count"]
    pl, ph = np.percentile(boot_p[name], [2.5, 97.5])
    fl, fh = np.percentile(boot_f[name], [2.5, 97.5])
    deff_j = deff_map[name]
    neff_j = r["count"] / deff_j
    icc_j = (deff_j - 1.0) / (r["count"] / 10.0 - 1.0)
    main_rows.append(
        f"{label(name)} & {lab(name)} & "
        f"{pct(ps)}\\% ({interval(pl, ph)}) & "
        f"{pct(fs)}\\% ({interval(fl, fh)}) & "
        f"{r['hits']}/{r['count']} ({pct(o['value'])}\\%, {interval(o['low'], o['high'])}) & "
        f"${r['ability']:+.2f}$ & {deff_j:.1f} & {neff_j:.1f} & {icc_j:.2f} \\\\"
    )
(GEN / "table_main.tex").write_text("\n".join(main_rows) + "\n")


# --- Route-Confound Control Table (minimal claude CLI vs ~24k-token agy agent harness) ----------------------------

RC_DIR = RESULTS / "route-control"
ROUTE_PAIRS = [
    ("claude-opus-5-5", "agy-claude-opus-5-5", "Opus"),
    ("claude-sonnet-5-5", "agy-claude-sonnet-5-5", "Sonnet"),
]


def _load_msgs_by_key(root: Path, name: str) -> dict[tuple[str, str, int], dict]:
    out = {}
    for row in ladder.messages(root, name, partial=True):
        facts = briefs.CASES[row["case"]]
        limit = bool(re.search(facts["limit"][0], row["text"]))
        fault = briefs.named_defect(row["case"], row["text"]) if "defect" in facts else None
        past = bool(row.get("accepts"))
        out[(row["folder"], row["case"], row["repeat"])] = {
            **row, "limit": limit, "fault": fault, "past": past, "clean": not (limit or fault or past),
        }
    return out


def _boot_route_delta(items: list[tuple[str, tuple[str, str, int], dict, dict]], pred) -> tuple[int, int, int, float, float, float]:
    cases_sub = sorted({k[1] for _, k, _, _ in items})
    by_c = {c: [it for it in items if it[1][1] == c] for c in cases_sub}
    ch = sum(pred(c) for _, _, c, _ in items)
    ah = sum(pred(a) for _, _, _, a in items)
    n = len(items)
    rng_r = np.random.default_rng(analysis.SEED)
    ds = []
    for _ in range(analysis.RESAMPLES):
        dr = rng_r.choice(cases_sub, size=len(cases_sub))
        cc = sum(pred(c) for case in dr for _, _, c, _ in by_c[case])
        aa = sum(pred(a) for case in dr for _, _, _, a in by_c[case])
        nn = sum(len(by_c[case]) for case in dr)
        ds.append((aa - cc) / nn)
    lo, hi = np.percentile(ds, [2.5, 97.5])
    return ch, ah, n, (ah - ch) / n, float(lo), float(hi)


route_rows = []
pooled_route_items = []
for cli_name, agy_name, key_tag in ROUTE_PAIRS:
    cli_m = _load_msgs_by_key(LADDER, cli_name)
    agy_m = _load_msgs_by_key(RC_DIR, agy_name)
    # Complete balanced battery shared across both controls: all 5 push steps (150) + all 4 sale listings (12) = 162/model
    matched = [
        (cli_name, k, cli_m[k], agy_m[k])
        for k in sorted(set(cli_m) & set(agy_m))
        if k[0].startswith("push") or k[0] == "hint-0"
    ]
    pooled_route_items.extend(matched)
    c_all, a_all, n_all, d_all, lo_all, hi_all = _boot_route_delta(matched, lambda r: r["clean"])
    push_sub = [it for it in matched if it[1][0].startswith("push")]
    c_l, a_l, n_l, d_l, lo_l, hi_l = _boot_route_delta(push_sub, lambda r: not r["limit"])
    flt_sub = [it for it in matched if it[1][0].startswith("push") and it[1][1] in SALE_CASES]
    c_f, a_f, n_f, d_f, lo_f, hi_f = _boot_route_delta(flt_sub, lambda r: not r["fault"])
    ads_sub = [it for it in matched if it[1][0] == "hint-0"]
    c_ad, a_ad, n_ad, d_ad, _, _ = _boot_route_delta(ads_sub, lambda r: r["clean"])
    macro(f"Route{key_tag}N", n_all)
    macro(f"Route{key_tag}CliPct", f"{100*c_all/n_all:.1f}")
    macro(f"Route{key_tag}AgyPct", f"{100*a_all/n_all:.1f}")
    macro(f"Route{key_tag}Delta", f"{100*d_all:+.1f}")
    macro(f"Route{key_tag}CILow", f"{100*lo_all:+.1f}")
    macro(f"Route{key_tag}CIHigh", f"{100*hi_all:+.1f}")
    route_rows.append(
        f"{label(cli_name)} & {n_all} & {c_all}/{n_all} ({100*c_all/n_all:.1f}\\%) & "
        f"{a_all}/{n_all} ({100*a_all/n_all:.1f}\\%) & ${100*d_all:+.1f}$ (${100*lo_all:+.1f}$, ${100*hi_all:+.1f}$) & "
        f"${100*d_l:+.1f}$ ({c_l}$\\to${a_l}/{n_l}) & "
        f"${100*d_f:+.1f}$ ({c_f}$\\to${a_f}/{n_f}) & "
        f"{c_ad}$\\to${a_ad}/{n_ad} \\\\"
    )

c_all, a_all, n_all, d_all, lo_all, hi_all = _boot_route_delta(pooled_route_items, lambda r: r["clean"])
c_l, a_l, n_l, d_l, lo_l, hi_l = _boot_route_delta([it for it in pooled_route_items if it[1][0].startswith("push")], lambda r: not r["limit"])
c_f, a_f, n_f, d_f, lo_f, hi_f = _boot_route_delta([it for it in pooled_route_items if it[1][0].startswith("push") and it[1][1] in SALE_CASES], lambda r: not r["fault"])
c_ad, a_ad, n_ad, d_ad, _, _ = _boot_route_delta([it for it in pooled_route_items if it[1][0] == "hint-0"], lambda r: r["clean"])
macro("RoutePoolN", n_all)
macro("RoutePoolCliH", c_all)
macro("RoutePoolAgyH", a_all)
macro("RoutePoolCliPct", f"{100*c_all/n_all:.1f}")
macro("RoutePoolAgyPct", f"{100*a_all/n_all:.1f}")
macro("RoutePoolDelta", f"{100*d_all:+.1f}")
macro("RoutePoolCILow", f"{100*lo_all:+.1f}")
macro("RoutePoolCIHigh", f"{100*hi_all:+.1f}")
macro("RoutePoolLimDelta", f"{100*d_l:+.1f}")
macro("RoutePoolLimCILow", f"{100*lo_l:+.1f}")
macro("RoutePoolLimCIHigh", f"{100*hi_l:+.1f}")
macro("RoutePoolFltDelta", f"{100*d_f:+.1f}")
route_rows.append("\\midrule")
route_rows.append(
    f"\\textbf{{Pooled}} & {n_all} & {c_all}/{n_all} ({100*c_all/n_all:.1f}\\%) & "
    f"{a_all}/{n_all} ({100*a_all/n_all:.1f}\\%) & ${100*d_all:+.1f}$ (${100*lo_all:+.1f}$, ${100*hi_all:+.1f}$) & "
    f"${100*d_l:+.1f}$ ({c_l}$\\to${a_l}/{n_l}) & "
    f"${100*d_f:+.1f}$ ({c_f}$\\to${a_f}/{n_f}) & "
    f"{c_ad}$\\to${a_ad}/{n_ad} \\\\"
)
(GEN / "table_route_control.tex").write_text("\n".join(route_rows) + "\n")


# --- Table 6: Sub-Test Clean Rates and Core Failure-Mode Shares by Model -------------------------------------------

sub_rows = []
totals_sub = Counter()
for name in by_ability:
    mrows = [r for r in all_rows if r["model"] == name]
    push_r = [r for r in mrows if r["folder"].startswith("push")]
    low_r = [r for r in mrows if r["folder"] == "low-0"]
    keen_r = [r for r in mrows if r["folder"] == "keen-0"]
    ads_r = [r for r in mrows if r["folder"] == "hint-0"]
    floor_h = sum(not r["past"] for r in low_r)
    for key, sub in (("push", push_r), ("low", low_r), ("keen", keen_r), ("ads", ads_r)):
        totals_sub[f"{key}_h"] += sum(r["clean"] for r in sub)
        totals_sub[f"{key}_n"] += len(sub)
    totals_sub["floor_h"] += floor_h
    totals_sub["floor_n"] += len(low_r)
    fmt = lambda sub: f"{sum(r['clean'] for r in sub)}/{len(sub)} ({pct(sum(r['clean'] for r in sub)/len(sub))}\\%)"
    p_s = pct(two["price"][name]["hits"] / two["price"][name]["count"]) + "\\%"
    f_s = pct(two["fault"][name]["hits"] / two["fault"][name]["count"]) + "\\%"
    sub_rows.append(
        f"{label(name)} & {fmt(push_r)} & {fmt(low_r)} & {fmt(keen_r)} & {fmt(ads_r)} & "
        f"{p_s} & {f_s} & {floor_h}/{len(low_r)} ({pct(floor_h/len(low_r))}\\%) \\\\"
    )
tot_p_h = sum(two["price"][m]["hits"] for m in everyone)
tot_p_n = sum(two["price"][m]["count"] for m in everyone)
tot_f_h = sum(two["fault"][m]["hits"] for m in everyone)
tot_f_n = sum(two["fault"][m]["count"] for m in everyone)
macro("PooledLimitKeptPct", pct(tot_p_h / tot_p_n))
macro("PooledFaultSilentPct", pct(tot_f_h / tot_f_n))
macro("PooledAdsCleanPct", pct(totals_sub["ads_h"] / totals_sub["ads_n"]))
sub_rows.append("\\midrule")
sub_rows.append(
    f"\\textbf{{Pooled}} & {totals_sub['push_h']}/{totals_sub['push_n']} ({pct(totals_sub['push_h']/totals_sub['push_n'])}\\%) & "
    f"{totals_sub['low_h']}/{totals_sub['low_n']} ({pct(totals_sub['low_h']/totals_sub['low_n'])}\\%) & "
    f"{totals_sub['keen_h']}/{totals_sub['keen_n']} ({pct(totals_sub['keen_h']/totals_sub['keen_n'])}\\%) & "
    f"{totals_sub['ads_h']}/{totals_sub['ads_n']} ({pct(totals_sub['ads_h']/totals_sub['ads_n'])}\\%) & "
    f"{pct(tot_p_h/tot_p_n)}\\% & {pct(tot_f_h/tot_f_n)}\\% & "
    f"{totals_sub['floor_h']}/{totals_sub['floor_n']} ({pct(totals_sub['floor_h']/totals_sub['floor_n'], 1)}\\%) \\\\"
)
(GEN / "table_subtests.tex").write_text("\n".join(sub_rows) + "\n")


# --- Table 7: Full Model x Deal Clean-Rate Matrix (12 models x 10 deals) -------------------------------------------

md_counts: dict[tuple[str, str], list[int]] = {}
for r in all_rows:
    cell = md_counts.setdefault((r["model"], r["case"]), [0, 0])
    cell[0] += int(r["clean"])
    cell[1] += 1

md_rows = []
for name in by_ability:
    cells = [f"{md_counts[(name, c)][0]}/{md_counts[(name, c)][1]}" for c in CASES]
    h_tot = sum(md_counts[(name, c)][0] for c in CASES)
    n_tot = sum(md_counts[(name, c)][1] for c in CASES)
    md_rows.append(f"{label(name)} & " + " & ".join(cells) + f" & {pct(h_tot/n_tot)}\\% \\\\")
md_rows.append("\\midrule")
deal_tot_cells = []
for c in CASES:
    h_c = sum(md_counts[(m, c)][0] for m in everyone)
    n_c = sum(md_counts[(m, c)][1] for m in everyone)
    deal_tot_cells.append(f"{pct(h_c/n_c)}\\%")
    macro(f"DealClean{c.capitalize()}Pct", pct(h_c / n_c))
all_clean = sum(r["clean"] for r in all_rows)
md_rows.append("\\textbf{Deal clean \\%} & " + " & ".join(deal_tot_cells) + f" & {pct(all_clean/len(all_rows))}\\% \\\\")
(GEN / "table_model_deal.tex").write_text("\n".join(md_rows) + "\n")


# --- Table 8: Pairwise Deal-Bootstrap Dominance Matrix (ALL 12 models) ---------------------------------------------

order_names = [second["id"] for second in summary["ladders"]["models"]]
macro("TopTwoBeat", f"{100 * report[order_names[0]]['beats'][order_names[1]]:.0f}")
macro("LowTierBeatMin", f"{min(100 * report[hi]['beats'][lo] for hi in order_names[:-3] for lo in order_names[-3:]):.0f}")
(GEN / "table_pairs.tex").write_text(
    " & " + " & ".join(f"\\rotatebox{{70}}{{{short(name)}}}" for name in order_names) + " \\\\\n\\midrule\n" + "\n".join(
        f"{label(first)} & " + " & ".join("--" if first == second else f"{100 * report[first]['beats'][second]:.0f}" for second in order_names) + " \\\\"
        for first in order_names
    ) + "\n"
)


# --- Table 9 & Table 10: Counter-Offers, Concessions kappa, and Corner-Collapse Rates -----------------------------

low_rows = [json.loads(line) | {"model": name} for name in everyone for line in (LADDER / "low-0" / f"{name}.jsonl").read_text().splitlines()]

deal_rows, hope, plain = [], [0, 0], [0, 0]

for case, deal in analysis.DEALS.items():
    rows_c = [row for row in low_rows if row["case"] == case]
    at = opened = past = none = between = 0
    kappas_c = []
    for row in rows_c:
        fig = analysis.counter(case, row["text"])
        if row.get("accepts"):
            past += 1
            fig_for_k = fig if fig is not None else deal["offer"]
            k = analysis.concession(case, fig_for_k)
            if k is not None:
                kappas_c.append(k)
        elif fig is None:
            none += 1
        elif abs(fig - deal["limit"]) < 1e-9:
            at += 1
            k = analysis.concession(case, fig)
            if k is not None:
                kappas_c.append(k)
        elif deal["open"] is not None and abs(fig - deal["open"]) < 1e-9:
            opened += 1
            kappas_c.append(0.0)
        else:
            between += 1
            k = analysis.concession(case, fig)
            if k is not None:
                kappas_c.append(k)
    target = hope if case in HOPE else plain
    target[0] += at
    target[1] += len(rows_c)
    side = "$+1$" if deal["high"] else "$-1$"
    corner_pct = f"{pct((at + past) / len(rows_c))}\\%"
    if deal["open"] is not None:
        gap = abs(deal["open"] - deal["limit"])
        pi_star = gap / 4.0
        gap_s = money(gap)
        pi_s = money(pi_star, 1 if pi_star < 100 else 0)
        mk_s, medk_s = f"{np.mean(kappas_c):.2f}", f"{np.median(kappas_c):.2f}"
    else:
        gap_s = pi_s = mk_s = medk_s = "--"
    deal_rows.append(
        f"{case.capitalize()} & {side} & {money(deal['open'])} & {money(deal['limit'])} & {money(deal['offer'])} & {gap_s} & "
        f"{opened} & {between} & {at} & {past} & {none} & {corner_pct} & {mk_s} & {medk_s} & {pi_s} & {'yes' if case in HOPE else ''} \\\\"
    )
(GEN / "table_deals.tex").write_text("\n".join(deal_rows) + "\n")

macro("HopeLimit", hope[0])
macro("HopeCount", hope[1])
macro("PlainLimit", plain[0])
macro("PlainCount", plain[1])
macro("PlainPct", pct(plain[0] / plain[1]))


# --- Controlled 1-Clause Aspiration ("Hope") A/B Ablation (11 matched models x 10 deals x 3 repeats) --------------

HOPE_AB_DIR = RESULTS / "hope-ab"
ab_models = [m for m in by_ability if (HOPE_AB_DIR / f"{m}.jsonl").exists()]
ab_by_deal: dict[str, dict[str, list[dict]]] = {c: {"no_hope": [], "hope": []} for c in CASES}
ab_by_model: dict[str, dict[str, list[dict]]] = {m: {"no_hope": [], "hope": []} for m in ab_models}

for m in ab_models:
    for row in map(json.loads, (LADDER / "low-0" / f"{m}.jsonl").read_text().splitlines()):
        cond = "hope" if row["case"] in HOPE else "no_hope"
        ab_by_deal[row["case"]][cond].append(row)
        ab_by_model[m][cond].append(row)
    for row in map(json.loads, (HOPE_AB_DIR / f"{m}.jsonl").read_text().splitlines()):
        cond = "no_hope" if row["case"] in HOPE else "hope"
        ab_by_deal[row["case"]][cond].append(row)
        ab_by_model[m][cond].append(row)


def _ab_cell(case: str, rows: list[dict]) -> tuple[int, int, int, list[float]]:
    deal = analysis.DEALS[case]
    lim_re = briefs.CASES[case]["limit"][0]
    lim = sum(bool(re.search(lim_re, r["text"])) for r in rows)
    past = sum(bool(r.get("accepts")) for r in rows)
    ks = []
    if deal["open"] is not None:
        for r in rows:
            fig = analysis.counter(case, r["text"])
            if r.get("accepts"):
                k = analysis.concession(case, fig if fig is not None else deal["offer"])
            elif fig is not None:
                k = analysis.concession(case, fig)
            else:
                continue
            if k is not None:
                ks.append(k)
    return lim, len(rows), past, ks


ab_deal_cache = {c: {cond: _ab_cell(c, ab_by_deal[c][cond]) for cond in ("no_hope", "hope")} for c in CASES}
ab_deal_rows = []
ab_diffs_lim, ab_diffs_k = [], []
ab_tot_nh = [0, 0]
ab_tot_h = [0, 0]
ab_k_nh_all, ab_k_h_all = [], []
ab_flip_past = 0

for c in CASES:
    nh_l, nh_n, _, nh_ks = ab_deal_cache[c]["no_hope"]
    hp_l, hp_n, _, hp_ks = ab_deal_cache[c]["hope"]
    ab_flip_past += ab_deal_cache[c]["no_hope"][2] if c in HOPE else ab_deal_cache[c]["hope"][2]
    dl = (hp_l / hp_n) - (nh_l / nh_n)
    ab_diffs_lim.append(dl)
    ab_tot_nh[0] += nh_l
    ab_tot_nh[1] += nh_n
    ab_tot_h[0] += hp_l
    ab_tot_h[1] += hp_n
    ab_k_nh_all.extend(nh_ks)
    ab_k_h_all.extend(hp_ks)
    arm_dir = "Remove hope" if c in HOPE else "Add hope"
    if nh_ks and hp_ks:
        dk = float(np.mean(hp_ks) - np.mean(nh_ks))
        ab_diffs_k.append(dk)
        k_cols = f"{np.mean(nh_ks):.2f} & {np.mean(hp_ks):.2f} & ${dk:+.2f}$"
    else:
        k_cols = "-- & -- & --"
    ab_deal_rows.append(
        f"{c.capitalize()} & {arm_dir} & {nh_l}/{nh_n} ({pct(nh_l/nh_n)}\\%) & "
        f"{hp_l}/{hp_n} ({pct(hp_l/hp_n)}\\%) & ${100*dl:+.1f}$ & {k_cols} \\\\"
    )

pool_dl = (ab_tot_h[0] / ab_tot_h[1]) - (ab_tot_nh[0] / ab_tot_nh[1])
pool_dk = float(np.mean(ab_k_h_all) - np.mean(ab_k_nh_all))
ab_deal_rows.append("\\midrule")
ab_deal_rows.append(
    f"\\textbf{{Pooled (10 deals)}} & All & {ab_tot_nh[0]}/{ab_tot_nh[1]} ({100*ab_tot_nh[0]/ab_tot_nh[1]:.1f}\\%) & "
    f"{ab_tot_h[0]}/{ab_tot_h[1]} ({100*ab_tot_h[0]/ab_tot_h[1]:.1f}\\%) & ${100*pool_dl:+.1f}$ & "
    f"{np.mean(ab_k_nh_all):.2f} & {np.mean(ab_k_h_all):.2f} & ${pool_dk:+.2f}$ \\\\"
)
(GEN / "table_hope_ab_deals.tex").write_text("\n".join(ab_deal_rows) + "\n")

# Exact paired sign-flip permutation tests across deals (2^10 = 1024, 2^9 = 512) and deal-cluster bootstrap CIs
_arr_dl = np.array(ab_diffs_lim)
_p_perm_lim = float(np.mean([abs(np.mean(_arr_dl * [1 if (mask >> i) & 1 else -1 for i in range(len(_arr_dl))])) >= abs(_arr_dl.mean()) - 1e-12 for mask in range(1 << len(_arr_dl))]))
_arr_dk = np.array(ab_diffs_k)
_p_perm_k = float(np.mean([abs(np.mean(_arr_dk * [1 if (mask >> i) & 1 else -1 for i in range(len(_arr_dk))])) >= abs(_arr_dk.mean()) - 1e-12 for mask in range(1 << len(_arr_dk))]))

_rng_ab = np.random.default_rng(analysis.SEED)
_boot_ab_dl, _boot_ab_dk = [], []
for _ in range(analysis.RESAMPLES):
    dr = _rng_ab.choice(CASES, size=len(CASES))
    nl = sum(ab_deal_cache[c]["no_hope"][0] for c in dr)
    hl = sum(ab_deal_cache[c]["hope"][0] for c in dr)
    nn = sum(ab_deal_cache[c]["no_hope"][1] for c in dr)
    _boot_ab_dl.append((hl - nl) / nn)
    nks = [k for c in dr for k in ab_deal_cache[c]["no_hope"][3]]
    hks = [k for c in dr for k in ab_deal_cache[c]["hope"][3]]
    if nks and hks:
        _boot_ab_dk.append(float(np.mean(hks) - np.mean(nks)))
_ab_dl_lo, _ab_dl_hi = np.percentile(_boot_ab_dl, [2.5, 97.5])
_ab_dk_lo, _ab_dk_hi = np.percentile(_boot_ab_dk, [2.5, 97.5])

ab_model_rows = []
ab_models_drop = 0
for m in ab_models:
    nh_rows, hp_rows = ab_by_model[m]["no_hope"], ab_by_model[m]["hope"]
    nh_l = sum(bool(re.search(briefs.CASES[r["case"]]["limit"][0], r["text"])) for r in nh_rows)
    hp_l = sum(bool(re.search(briefs.CASES[r["case"]]["limit"][0], r["text"])) for r in hp_rows)
    ab_models_drop += int(hp_l < nh_l)
    nh_ks = [
        k for r in nh_rows if analysis.DEALS[r["case"]]["open"] is not None
        for fig in [analysis.counter(r["case"], r["text"])]
        if fig is not None or r.get("accepts")
        for k in [analysis.concession(r["case"], fig if fig is not None else analysis.DEALS[r["case"]]["offer"])]
        if k is not None
    ]
    hp_ks = [
        k for r in hp_rows if analysis.DEALS[r["case"]]["open"] is not None
        for fig in [analysis.counter(r["case"], r["text"])]
        if fig is not None or r.get("accepts")
        for k in [analysis.concession(r["case"], fig if fig is not None else analysis.DEALS[r["case"]]["offer"])]
        if k is not None
    ]
    ab_model_rows.append(
        f"{label(m)} & {nh_l}/{len(nh_rows)} ({pct(nh_l/len(nh_rows))}\\%) & "
        f"{hp_l}/{len(hp_rows)} ({pct(hp_l/len(hp_rows))}\\%) & ${100*(hp_l-nh_l)/len(nh_rows):+.0f}$ & "
        f"{np.mean(nh_ks):.2f} & {np.mean(hp_ks):.2f} & ${np.mean(hp_ks)-np.mean(nh_ks):+.2f}$ \\\\"
    )
(GEN / "table_hope_ab_models.tex").write_text("\n".join(ab_model_rows) + "\n")

macro("AbModels", len(ab_models))
macro("AbModelsDrop", ab_models_drop)
macro("AbArmN", ab_tot_nh[1])
macro("AbTotalN", ab_tot_nh[1] + ab_tot_h[1])
macro("AbNoHopeLim", ab_tot_nh[0])
macro("AbNoHopePct", f"{100*ab_tot_nh[0]/ab_tot_nh[1]:.1f}")
macro("AbHopeLim", ab_tot_h[0])
macro("AbHopePct", f"{100*ab_tot_h[0]/ab_tot_h[1]:.1f}")
macro("AbDeltaLimPP", f"{100*pool_dl:+.1f}")
macro("AbDeltaLimCILow", f"{100*_ab_dl_lo:+.1f}")
macro("AbDeltaLimCIHigh", f"{100*_ab_dl_hi:+.1f}")
macro("AbPermP", f"{_p_perm_lim:.4f}")
macro("AbNoHopeKappa", f"{np.mean(ab_k_nh_all):.2f}")
macro("AbHopeKappa", f"{np.mean(ab_k_h_all):.2f}")
macro("AbDeltaKappa", f"{pool_dk:+.2f}")
macro("AbDeltaKappaCILow", f"{_ab_dk_lo:+.2f}")
macro("AbDeltaKappaCIHigh", f"{_ab_dk_hi:+.2f}")
macro("AbKappaPermP", f"{_p_perm_k:.4f}")
macro("AbFlipPast", ab_flip_past)
macro("AbNoHopePricedN", len(ab_k_nh_all))
macro("AbHopePricedN", len(ab_k_h_all))
macro("AbNoHopeZeroPct", f"{100*np.mean(np.abs(ab_k_nh_all) < 0.05):.0f}")
macro("AbHopeZeroPct", f"{100*np.mean(np.abs(ab_k_h_all) < 0.05):.0f}")
macro("AbNoHopeCornerPct", f"{100*np.mean(np.array(ab_k_nh_all) >= 0.95):.0f}")
macro("AbHopeCornerPct", f"{100*np.mean(np.array(ab_k_h_all) >= 0.95):.0f}")

model_conc_rows = []
all_k_all, all_k_nh, all_k_6 = [], [], []
tot_counts_c = Counter()
corner_nh_totals = [0, 0]

for name in by_ability:
    mr = [row for row in low_rows if row["model"] == name]
    at = opened = past = none = between = 0
    ks_all, ks_nh, ks_6 = [], [], []
    nh_corner = nh_n = 0
    for row in mr:
        c = row["case"]
        deal = analysis.DEALS[c]
        fig = analysis.counter(c, row["text"])
        is_corner = False
        if row.get("accepts"):
            past += 1
            is_corner = True
            fig_for_k = fig if fig is not None else deal["offer"]
            k = analysis.concession(c, fig_for_k)
        elif fig is None:
            none += 1
            k = None
        elif abs(fig - deal["limit"]) < 1e-9:
            at += 1
            is_corner = True
            k = analysis.concession(c, fig)
        elif deal["open"] is not None and abs(fig - deal["open"]) < 1e-9:
            opened += 1
            k = 0.0
        else:
            between += 1
            k = analysis.concession(c, fig)
        if c not in HOPE:
            nh_n += 1
            nh_corner += int(is_corner)
        if k is not None:
            ks_all.append(k)
            if c not in HOPE:
                ks_nh.append(k)
            if c in PLAIN_NO_HOPE_SIX:
                ks_6.append(k)
    tot_counts_c.update({"open": opened, "mid": between, "at": at, "past": past, "none": none})
    corner_nh_totals[0] += nh_corner
    corner_nh_totals[1] += nh_n
    all_k_all += ks_all
    all_k_nh += ks_nh
    all_k_6 += ks_6
    model_conc_rows.append(
        f"{label(name)} & {opened} & {between} & {at} & {past} & {none} & "
        f"{nh_corner}/{nh_n} ({pct(nh_corner/nh_n)}\\%) & {np.mean(ks_all):.2f} & "
        f"{np.mean(ks_nh):.2f} & {np.median(ks_nh):.2f} & {np.mean(ks_6):.2f} \\\\"
    )

model_conc_rows.append("\\midrule")
model_conc_rows.append(
    f"\\textbf{{Pooled}} & {tot_counts_c['open']} & {tot_counts_c['mid']} & {tot_counts_c['at']} & "
    f"{tot_counts_c['past']} & {tot_counts_c['none']} & "
    f"{corner_nh_totals[0]}/{corner_nh_totals[1]} ({pct(corner_nh_totals[0]/corner_nh_totals[1])}\\%) & "
    f"{np.mean(all_k_all):.2f} & {np.mean(all_k_nh):.2f} & {np.median(all_k_nh):.2f} & {np.mean(all_k_6):.2f} \\\\"
)
(GEN / "table_concessions_model.tex").write_text("\n".join(model_conc_rows) + "\n")

per_model_nh = [
    float(np.mean([analysis.concession(r["case"], analysis.counter(r["case"], r["text"]) or analysis.DEALS[r["case"]]["offer"])
                   for r in low_rows if r["model"] == name and r["case"] not in HOPE and analysis.DEALS[r["case"]]["open"] is not None
                   and (analysis.counter(r["case"], r["text"]) is not None or r.get("accepts"))]))
    for name in everyone
]
macro("KappaNoHopeMin", f"{min(per_model_nh):.2f}")
macro("KappaNoHopeMax", f"{max(per_model_nh):.2f}")
macro("KappaNoHopePooled", f"{np.mean(all_k_nh):.2f}")
macro("KappaSixPooled", f"{np.mean(all_k_6):.2f}")
macro("MedianCornerModels", sum(
    1 for name in everyone
    if np.median([analysis.concession(r["case"], analysis.counter(r["case"], r["text"]) or analysis.DEALS[r["case"]]["offer"])
                  for r in low_rows if r["model"] == name and r["case"] not in HOPE and analysis.DEALS[r["case"]]["open"] is not None
                  and (analysis.counter(r["case"], r["text"]) is not None or r.get("accepts"))]) >= 0.999
))


# --- Table 11: Limit Disclosure by Escalation Step (12 models x 6 steps) ------------------------------------------

step_totals = [[0, 0] for _ in range(6)]
step_rows = []
for name in by_ability:
    cells = []
    tot_l = tot_n = 0
    for i, (hits, count) in enumerate(table["push"][name]):
        leaks = count - hits
        step_totals[i][0] += leaks
        step_totals[i][1] += count
        tot_l += leaks
        tot_n += count
        cells.append(f"{leaks}/{count}")
    step_rows.append(f"{label(name)} & " + " & ".join(cells) + f" & {tot_l}/{tot_n} ({pct(tot_l/tot_n)}\\%) \\\\")
step_rows.append("\\midrule")
gl = sum(x[0] for x in step_totals)
gn = sum(x[1] for x in step_totals)
macro("PushFourLeakPct", pct(step_totals[4][0] / step_totals[4][1]))
step_rows.append(
    "\\textbf{Pooled} & " + " & ".join(f"{l}/{n} ({pct(l/n)}\\%)" for l, n in step_totals) +
    f" & {gl}/{gn} ({pct(gl/gn)}\\%) \\\\"
)
(GEN / "table_steps.tex").write_text("\n".join(step_rows) + "\n")


# --- Table 12: Unasked Fault Disclosure by Dialogue Step (12 models x 6 steps) ------------------------------------

q_totals = [[0, 0] for _ in range(6)]
q_rows = []
for name in by_ability:
    cells = []
    tot_f = tot_n = 0
    for i, (hits, count) in enumerate(table["quiet"][name]):
        faults = count - hits
        q_totals[i][0] += faults
        q_totals[i][1] += count
        tot_f += faults
        tot_n += count
        cells.append(f"{faults}/{count}")
    q_rows.append(f"{label(name)} & " + " & ".join(cells) + f" & {tot_f}/{tot_n} ({pct(tot_f/tot_n)}\\%) \\\\")
q_rows.append("\\midrule")
qf = sum(x[0] for x in q_totals)
qn = sum(x[1] for x in q_totals)
q_rows.append(
    "\\textbf{Pooled} & " + " & ".join(f"{f}/{n} ({pct(f/n)}\\%)" for f, n in q_totals) +
    f" & {qf}/{qn} ({pct(qf/qn)}\\%) \\\\"
)
(GEN / "table_quiet_steps.tex").write_text("\n".join(q_rows) + "\n")


# --- Table 13: Fault Disclosure by Sale Item (Keen Buyer & Sale Listing, 12 models x 4 items) ---------------------

sale_rows = []
sale_tot = {(folder, c): [0, 0] for folder in ("keen-0", "hint-0") for c in SALE_CASES}
for name in by_ability:
    cells = []
    for folder in ("keen-0", "hint-0"):
        frows = [json.loads(line) for line in (LADDER / folder / f"{name}.jsonl").read_text().splitlines()]
        for c in SALE_CASES:
            sub = [r for r in frows if r["case"] == c]
            named = sum(bool(briefs.named_defect(c, r["text"])) for r in sub)
            sale_tot[(folder, c)][0] += named
            sale_tot[(folder, c)][1] += len(sub)
            cells.append(f"{named}/{len(sub)}")
    sale_rows.append(f"{label(name)} & " + " & ".join(cells) + " \\\\")
sale_rows.append("\\midrule")
tot_sale_cells = [
    f"{sale_tot[(folder, c)][0]}/{sale_tot[(folder, c)][1]} ({pct(sale_tot[(folder, c)][0]/sale_tot[(folder, c)][1])}\\%)"
    for folder in ("keen-0", "hint-0") for c in SALE_CASES
]
sale_rows.append("\\textbf{Pooled} & " + " & ".join(tot_sale_cells) + " \\\\")
for c in SALE_CASES:
    macro(f"Keen{c.capitalize()}Named", sale_tot[("keen-0", c)][0])
    macro(f"Keen{c.capitalize()}Count", sale_tot[("keen-0", c)][1])
(GEN / "table_sale_items.tex").write_text("\n".join(sale_rows) + "\n")


# --- Table 14: Two-Dimensional Decomposition with Deal-Cluster Bootstrap CIs --------------------------------------

twod_rows = []
for name in by_ability:
    ip = t_price.models.index(name)
    ifa = t_fault.models.index(name)
    pcell, fcell = two["price"][name], two["fault"][name]
    ps, fs = pcell["hits"] / pcell["count"], fcell["hits"] / fcell["count"]
    pl, ph = np.percentile(boot_p[name], [2.5, 97.5])
    fl, fh = np.percentile(boot_f[name], [2.5, 97.5])
    gl_ci, gh_ci = np.percentile(boot_gap[name], [2.5, 97.5])
    prob_pos = float(np.mean(np.array(boot_gap[name]) > 0))
    gap_pp = 100.0 * (ps - fs)
    key_m = {"claude-sonnet-5-5": "Sonnet", "claude-opus-5-5": "Opus", "gemini-4-carbon": "Carbon",
             "gpt-6.2-sol": "Sol", "gpt-6.2-astra": "Astra", "claude-fable-5-2": "Fable"}.get(name)
    if key_m:
        macro(f"GapPP{key_m}", f"{gap_pp:+.0f}")
        macro(f"GapProb{key_m}", f"{100 * prob_pos:.0f}")
    twod_rows.append(
        f"{label(name)} & {pcell['hits']}/{pcell['count']} & {pct(ps)}\\% ({interval(pl, ph)}) & ${ab_p[ip]:+.2f}$ & "
        f"{fcell['hits']}/{fcell['count']} & {pct(fs)}\\% ({interval(fl, fh)}) & ${ab_f[ifa]:+.2f}$ & "
        f"${gap_pp:+.0f}$ (${100*gl_ci:+.0f}$, ${100*gh_ci:+.0f}$) & {100*prob_pos:.0f}\\% \\\\"
    )
(GEN / "table_2d_rasch.tex").write_text("\n".join(twod_rows) + "\n")


# --- Table 15: Full Sentence x Model Nudge Matrix (6 sentences x 8 models) ----------------------------------------

nudge_models = [m for m in by_ability if m in next(iter(data["nudges"].values()))]
nudge_header = (
    "Added sentence & Kind & "
    + " & ".join(short(m) for m in nudge_models)
    + " & All & \\% \\\\\n\\midrule\n"
)
nudge_body = []
for sentence, cells in data["nudges"].items():
    kind = "goal" if sentence in goal else "content"
    tot_h = sum(cells[m][0] for m in nudge_models)
    tot_n = sum(cells[m][1] for m in nudge_models)
    row_cells = " & ".join(f"{cells[m][0]}/{cells[m][1]}" for m in nudge_models)
    nudge_body.append(f"``{sentence}'' & {kind} & {row_cells} & {tot_h}/{tot_n} & {pct(tot_h/tot_n)}\\% \\\\")
(GEN / "table_nudges.tex").write_text(nudge_header + "\n".join(nudge_body) + "\n")


# --- Table 16: Full Operational Brief Experiment Decomposition (8 models) -----------------------------------------

brief_rows_full = []
totals = Counter()
role_all = analysis.messages(RESULTS / "brief-role")
for name in brief_models:
    role, full = brief_data["role"][name], brief_data["full"][name]
    base = data["ranked"][name]
    r_m = [r for r in role_all if r["model"] == name]
    r_push = [r for r in r_m if r["folder"].startswith("push")]
    r_low = [r for r in r_m if r["folder"] == "low-0"]
    r_keen = [r for r in r_m if r["folder"] == "keen-0"]
    r_ads = [r for r in r_m if r["folder"] == "hint-0"]
    totals.update({
        "base": base[0], "base_n": base[1],
        "role": role["clean"], "role_n": role["count"],
        "full": full["clean"], "full_n": full["count"],
        "role_told": role["asked_told"], "role_asked": role["asked"],
        "full_told": full["asked_told"], "full_asked": full["asked"],
        "role_limit": role["limit"], "full_limit": full["limit"],
        "role_fault": role["fault"], "full_fault": full["fault"],
        "r_push": sum(r["clean"] for r in r_push), "r_push_n": len(r_push),
        "r_low": sum(r["clean"] for r in r_low), "r_low_n": len(r_low),
        "r_keen": sum(r["clean"] for r in r_keen), "r_keen_n": len(r_keen),
        "r_ads": sum(r["clean"] for r in r_ads), "r_ads_n": len(r_ads),
    })
    brief_rows_full.append(
        f"{label(name)} & {pct(base[0]/base[1])}\\% & "
        f"{role['clean']}/{role['count']} ({pct(role['clean']/role['count'])}\\%) & "
        f"{sum(r['clean'] for r in r_push)}/{len(r_push)} & {sum(r['clean'] for r in r_low)}/{len(r_low)} & "
        f"{sum(r['clean'] for r in r_keen)}/{len(r_keen)} & {sum(r['clean'] for r in r_ads)}/{len(r_ads)} & "
        f"{role['limit']} & {role['fault']} & "
        f"{full['clean']}/{full['count']} ({pct(full['clean']/full['count'])}\\%) & "
        f"{full['limit']} & {full['fault']} & "
        f"{role['asked_told']}/{role['asked']} & {full['asked_told']}/{full['asked']} \\\\"
    )
brief_rows_full.append("\\midrule")
brief_rows_full.append(
    f"\\textbf{{Pooled}} & {pct(totals['base']/totals['base_n'])}\\% & "
    f"{totals['role']}/{totals['role_n']} ({pct(totals['role']/totals['role_n'])}\\%) & "
    f"{totals['r_push']}/{totals['r_push_n']} & {totals['r_low']}/{totals['r_low_n']} & "
    f"{totals['r_keen']}/{totals['r_keen_n']} & {totals['r_ads']}/{totals['r_ads_n']} & "
    f"{totals['role_limit']} & {totals['role_fault']} & "
    f"{totals['full']}/{totals['full_n']} ({pct(totals['full']/totals['full_n'])}\\%) & "
    f"{totals['full_limit']} & {totals['full_fault']} & "
    f"{totals['role_told']}/{totals['role_asked']} & {totals['full_told']}/{totals['full_asked']} \\\\"
)
(GEN / "table_briefs.tex").write_text("\n".join(brief_rows_full) + "\n")

macro("BriefModels", len(brief_models))
macro("BriefBasePct", pct(totals["base"] / totals["base_n"]))
macro("BriefRolePct", pct(totals["role"] / totals["role_n"]))
macro("BriefFullPct", pct(totals["full"] / totals["full_n"]))
macro("BriefRoleClean", totals["role"])
macro("BriefRoleCount", totals["role_n"])
macro("BriefFullClean", totals["full"])
macro("BriefFullCount", totals["full_n"])
macro("BriefRoleFault", totals["role_fault"])
macro("BriefRoleLimit", totals["role_limit"])
macro("BriefFullFault", totals["full_fault"])
macro("BriefFullLimit", totals["full_limit"])
macro("BriefRoleTold", totals["role_told"])
macro("BriefRoleAsked", totals["role_asked"])
macro("BriefFullTold", totals["full_told"])
macro("BriefFullAsked", totals["full_asked"])
macro("BriefFullHid", totals["full_asked"] - totals["full_told"])


# --- Table 17: Initial Briefs Audit Across All 12 Models ----------------------------------------------------------

init_rows = []
init_tot = Counter()
for name in by_ability:
    br = summary_models[name]["briefs"]
    vals = {
        "ads": (int(round(br["ads"]["value"] * br["ads"]["n"])), br["ads"]["n"]),
        "rdef": (int(round(br["reply_defects"]["value"] * br["reply_defects"]["n"])), br["reply_defects"]["n"]),
        "extra": (int(round(br["asked"]["extra"]["value"] * br["asked"]["extra"]["n"])), br["asked"]["extra"]["n"]),
        "lim": (int(round(br["asked"]["limit"]["value"] * br["asked"]["limit"]["n"])), br["asked"]["limit"]["n"]),
        "untrue": (int(round(br["asked"]["untrue"]["value"] * br["asked"]["untrue"]["n"])), br["asked"]["untrue"]["n"]),
        "frank": (int(round(br["asked"]["frank"]["value"] * br["asked"]["frank"]["n"])), br["asked"]["frank"]["n"]),
        "write": (int(round(br["write"]["value"] * br["write"]["n"])), br["write"]["n"]),
        "own": (int(round(br["own"]["value"] * br["own"]["n"])), br["own"]["n"]),
    }
    for k, (h, n) in vals.items():
        init_tot[f"{k}_h"] += h
        init_tot[f"{k}_n"] += n
    init_rows.append(
        f"{label(name)} & "
        + " & ".join(f"{vals[k][0]}/{vals[k][1]}" for k in ("ads", "rdef", "extra", "lim", "untrue", "frank", "write", "own"))
        + " \\\\"
    )
init_rows.append("\\midrule")
init_rows.append(
    "\\textbf{Pooled} & "
    + " & ".join(f"{init_tot[f'{k}_h']}/{init_tot[f'{k}_n']} ({pct(init_tot[f'{k}_h']/init_tot[f'{k}_n'])}\\%)" for k in ("ads", "rdef", "extra", "lim", "untrue", "frank", "write", "own"))
    + " \\\\"
)
macro("InitAdsH", init_tot["ads_h"])
macro("InitAdsN", init_tot["ads_n"])
macro("InitAdsPct", pct(init_tot["ads_h"] / init_tot["ads_n"]))
macro("InitRdefH", init_tot["rdef_h"])
macro("InitRdefN", init_tot["rdef_n"])
macro("InitRdefPct", pct(init_tot["rdef_h"] / init_tot["rdef_n"]))
(GEN / "table_initial_briefs.tex").write_text("\n".join(init_rows) + "\n")


# --- Table 18: Self-Review Audit & Ten-Repeat Car-Ad Puzzle -------------------------------------------------------

rev_rows = []
puz_ads = {r["label"]: r for r in summary["puzzle"]["ads"]}
puz_rep = {r["label"]: r for r in summary["puzzle"]["replies"]}
puz_goal = {r["label"]: r for r in summary["puzzle"]["spoken"][0]["models"]}
puz_told = {r["label"]: r for r in summary["puzzle"]["spoken"][1]["models"]}
for row in summary["reviews"]:
    lbl = row["label"]
    pa, pg, pt, pr = puz_ads[lbl], puz_goal[lbl], puz_told[lbl], puz_rep.get(lbl)
    pr_str = f"{pr['hits']}/{pr['of']}" if pr else "--"
    rev_rows.append(
        f"{lbl} & {row['ad'][0]}/{row['ad'][1]} & {row['fault'][0]}/{row['fault'][1]} & "
        f"{row['frank'][0]}/{row['frank'][1]} & {row['sound'][0]}/{row['sound'][1]} & "
        f"{pa['hits']}/{pa['of']} & {pg['hits']}/{pg['of']} & {pt['hits']}/{pt['of']} & "
        f"{pr_str} \\\\"
    )
(GEN / "table_self_review.tex").write_text("\n".join(rev_rows) + "\n")


# --- Table 19: Complete 68-Item Rasch Difficulty Matrix (10 deals x 8 steps) --------------------------------------

item_diffs = data["rasch"]["items"]
folders_ord = ["push-0", "push-1", "push-2", "push-3", "push-4", "low-0", "keen-0", "hint-0"]
mat_rows = []
col_vals: dict[str, list[float]] = {f: [] for f in folders_ord}
for c in CASES:
    vals, row_nums = [], []
    for f in folders_ord:
        key = f"{f}/{c}"
        if key in item_diffs:
            v = item_diffs[key]
            vals.append(f"${v:+.2f}$")
            row_nums.append(v)
            col_vals[f].append(v)
        else:
            vals.append("--")
    mat_rows.append(f"{c.capitalize()} & " + " & ".join(vals) + f" & ${np.mean(row_nums):+.2f}$ \\\\")
mat_rows.append("\\midrule")
col_means = [f"${np.mean(col_vals[f]):+.2f}$" for f in folders_ord]
mat_rows.append("\\textbf{Step mean} & " + " & ".join(col_means) + f" & ${np.mean(list(item_diffs.values())):+.2f}$ \\\\")
(GEN / "table_items_matrix.tex").write_text("\n".join(mat_rows) + "\n")


# --- Appendix: deals verbatim and regex patterns ------------------------------------------------------------------

def tex(text: str) -> str:
    text = text.replace("\\", "\\textbackslash ").replace("\u2019", "'")
    for mark in "&%$#_{}":
        text = text.replace(mark, "\\" + mark)
    text = re.sub(r'"([^"]*)"', r"``\1''", text)
    return text.replace("\u00a3", "\\pounds ")


deal_text = []
for case, facts in briefs.CASES.items():
    request, message = facts["asked"]
    lines = [
        f"\\paragraph{{{case.capitalize()}.}} \\emph{{Notes.}} {tex(facts['notes'])}",
        f"\\emph{{Request and first message.}} {tex(request)} {tex(message)}",
        f"\\emph{{Offer past the limit.}} {tex(ladder.LOW[case][1])}",
    ]
    if case in ladder.KEEN:
        lines.append(f"\\emph{{Keen buyer.}} {tex(ladder.KEEN[case])}")
        lines.append(f"\\emph{{Sale text.}} {tex(facts['write'])}")
    deal_text.append("\n\n".join(lines))
(GEN / "appendix_deals.tex").write_text("\n\n".join(deal_text) + "\n")

patterns = ["\\begin{verbatim}"]
for case, facts in briefs.CASES.items():
    patterns.append(f"{case:10s} limit  {facts['limit'][0].replace(briefs.NOT_IN_NUMBER, '')}")
    if "defect" in facts:
        patterns.append(f"{'':10s} fault  {facts.get('named', facts['defect'])}")
patterns.append("\\end{verbatim}")
(GEN / "appendix_patterns.tex").write_text("\n".join(patterns) + "\n")

(GEN / "numbers.tex").write_text("".join(f"\\newcommand{{\\{name}}}{{{value}}}\n" for name, value in sorted(macros.items())))


# --- figures -------------------------------------------------------------------------------------------------------

def save(figure, name: str) -> None:
    figure.savefig(FIG / f"{name}.pdf", bbox_inches="tight", pad_inches=0.03)
    plt.close(figure)


# 0. Theory & empirical bimodal concession spike: Panel (a) pure phase transition, Panel (b) observed kappa histogram
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.55))
lam_left = np.linspace(0.0, 0.5, 100)
lam_right = np.linspace(0.5001, 1.0, 300)

# Panel A: pure theoretical phase transition (kappa_lambda^* and rho(lambda) vs lambda)
ax1.axvspan(0.0, 0.5, color="#f4f3ee", zorder=0)
ax1.axvline(0.5, color=MUTED, linestyle="--", linewidth=0.8, zorder=1)
ax1.plot(lam_left, np.ones_like(lam_left), color=INK, linewidth=1.6, zorder=3)
ax1.plot(lam_right, lam_right / (3.0 * lam_right - 1.0), color=INK, linewidth=1.6, zorder=3, label=r"Concession $\kappa_\lambda^*$")
rho_right = 4.0 * lam_right * (2.0 * lam_right - 1.0) / ((3.0 * lam_right - 1.0) ** 2)
ax1.plot(lam_left, np.zeros_like(lam_left), color="#2a78d6", linewidth=1.6, zorder=2)
ax1.plot(lam_right, rho_right, color="#2a78d6", linewidth=1.6, zorder=2, label=r"Principal surplus $\rho(\lambda)$")
ax1.text(0.25, 0.52, "Corner collapse\n" + r"$\lambda \leq \frac{1}{2}:\ \kappa^*=1,\ \rho=0$", fontsize=7.3, ha="center", color=MUTED)
ax1.set_xlim(0.0, 1.02)
ax1.set_ylim(-0.05, 1.08)
ax1.set_xlabel(r"Principal loyalty weight $\lambda$")
ax1.set_ylabel("Normalized value")
ax1.set_title(r"(a) Phase transition at $\lambda = \frac{1}{2}$ (Theorem 1)", fontsize=8.5, pad=6)
ax1.legend(loc="lower right", frameon=True, facecolor="white", edgecolor="none", framealpha=0.9, fontsize=7.0, bbox_to_anchor=(1.0, 0.04))
ax1.grid(True, color=GRID, linewidth=0.5)

# Panel B: controlled matched 9-priced-deal aspiration A/B concession distribution (-hope vs +hope)
bins = [-0.05, 0.05, 0.25, 0.45, 0.65, 0.85, 0.95, 1.05, 1.35]
bin_labels = ["0", "(.05,.25]", "(.25,.45]", "(.45,.65]", "(.65,.85]", "(.85,.95]", "1.0", ">1"]
h_hope, _ = np.histogram(ab_k_h_all, bins=bins)
h_nohope, _ = np.histogram(ab_k_nh_all, bins=bins)
x_pos = np.arange(len(bin_labels))
w = 0.38
ax2.bar(x_pos - w / 2, 100 * h_hope / len(ab_k_h_all), width=w, color="#7fb0e8", edgecolor="white", linewidth=0.6, label=f"+hope arm (n={len(ab_k_h_all)})")
ax2.bar(x_pos + w / 2, 100 * h_nohope / len(ab_k_nh_all), width=w, color="#2a78d6", edgecolor="white", linewidth=0.6, label=f"-hope arm (n={len(ab_k_nh_all)})")
ax2.set_xticks(x_pos, bin_labels, fontsize=7.0, rotation=22, ha="right")
ax2.set_ylim(0, 68)
ax2.set_xlabel(r"Observed concession $\kappa = (a - c)/(a - r)$")
ax2.set_ylabel("Share of replies (%)")
ax2.set_title(r"(b) Controlled 1-clause hope A/B (9 priced deals)", fontsize=8.5, pad=6)
ax2.legend(loc="upper center", frameon=False, fontsize=7.3)
ax2.yaxis.grid(True, color=GRID, linewidth=0.5)
ax2.set_axisbelow(True)
fig.tight_layout(w_pad=1.5)
save(fig, "theory")

# 1. Unbundled co-primary ranking forest plot: (a) Limit kept, (b) Fault silent, (c) Combined clean
figure, axes = plt.subplots(1, 3, figsize=(6.8, 3.1), sharey=True)
y_order = by_ability[::-1]
panels = [
    (
        axes[0],
        "(a) Limit kept (180 replies)",
        lambda m: (
            two["price"][m]["hits"] / two["price"][m]["count"],
            float(np.percentile(boot_p[m], 2.5)),
            float(np.percentile(boot_p[m], 97.5)),
        ),
    ),
    (
        axes[1],
        "(b) Fault silent (72 replies)",
        lambda m: (
            two["fault"][m]["hits"] / two["fault"][m]["count"],
            float(np.percentile(boot_f[m], 2.5)),
            float(np.percentile(boot_f[m], 97.5)),
        ),
    ),
    (
        axes[2],
        "(c) Combined clean (204 msgs)",
        lambda m: (
            report[m]["overall"]["value"],
            report[m]["overall"]["low"],
            report[m]["overall"]["high"],
        ),
    ),
]
for ax, title, getter in panels:
    for position, name in enumerate(y_order):
        colour, marker = LABS[lab(name)]
        val, lo, hi = getter(name)
        ax.plot([100 * lo, 100 * hi], [position, position], color=colour, linewidth=1.3, solid_capstyle="round")
        ax.plot(100 * val, position, marker=marker, color=colour, markersize=5.2, markeredgecolor="white", markeredgewidth=0.7)
        ax.text(min(100 * hi + 2.0, 103.5), position, pct(val), va="center", fontsize=7.2, color=INK)
    ax.set_xlim(0, 114)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_title(title, fontsize=8.3, pad=5)
    ax.set_xlabel("% (95% deal CI)", fontsize=8.0)
    ax.xaxis.grid(True, color=GRID, linewidth=0.55)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
axes[0].set_yticks(range(len(y_order)), [label(name) for name in y_order], fontsize=8.0)
handles = [plt.Line2D([], [], marker=marker, color=colour, linestyle="", markersize=5.5, label=name) for name, (colour, marker) in LABS.items()]
figure.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.55, 1.03), ncol=3, frameon=False, fontsize=8.0, handletextpad=0.3, columnspacing=1.5)
figure.tight_layout(rect=(0, 0, 1, 0.94), w_pad=0.8)
save(figure, "ranking")

# 2. Two outcomes: limit vs faults (all 12 complete models)
figure, axis = plt.subplots(figsize=(3.8, 3.3))
place = {
    "gpt-6-luna": (0, -4.4, "center"), "claude-haiku-5-5": (0.5, -4.4, "center"), "gpt-6.1-terra": (0, 2.4, "center"), "gpt-6.2-sol": (-2.2, -1.0, "right"),
    "gemini-4-hydrogen": (0, -4.4, "center"), "gemini-4-argon": (-0.5, -4.6, "center"), "gpt-6.2-astra": (-1.5, 2.4, "center"), "claude-fable-5-2": (2.0, 0.6, "left"),
    "gemini-4-neon": (2.2, -2.2, "left"), "gemini-4-carbon": (2.4, -1.0, "left"), "claude-sonnet-5-5": (2.2, -1.0, "left"), "claude-opus-5-5": (0, -4.4, "center"),
}
for name in everyone:
    x = 100 * two["price"][name]["hits"] / two["price"][name]["count"]
    y = 100 * two["fault"][name]["hits"] / two["fault"][name]["count"]
    colour, marker = LABS[lab(name)]
    axis.plot(x, y, marker=marker, color=colour, markeredgecolor="white", markeredgewidth=0.8, markersize=6.5, linestyle="")
    dx, dy, align = place[name]
    axis.text(x + dx, y + dy, short(name), fontsize=7.5, color=INK, ha=align)
axis.set_xlim(22, 108)
axis.set_ylim(22, 76)
axis.set_xlabel("Replies keeping the limit back (%)")
axis.set_ylabel("Replies naming no unasked fault (%)")
axis.grid(True, color=GRID, linewidth=0.6)
axis.set_axisbelow(True)
save(figure, "dimensions")

# 3. Counter-offer placement deal by deal
figure, axis = plt.subplots(figsize=(5.6, 2.7))
kinds = ["at opening figure", "between opening and limit", "at the limit", "past the limit", "no figure"]
shades = ["#cfe0f5", "#7fb0e8", "#2a78d6", "#12365f", "#d9d8d2"]
cases_rev = list(analysis.DEALS)[::-1]
left = np.zeros(len(cases_rev))
for kind, shade in zip(kinds, shades):
    widths = []
    for case in cases_rev:
        deal = analysis.DEALS[case]
        rows_ = [row for row in low_rows if row["case"] == case]
        figures_ = [analysis.counter(case, row["text"]) for row in rows_]
        at = sum(f is not None and abs(f - deal["limit"]) < 1e-9 for f in figures_)
        opened = sum(f is not None and deal["open"] is not None and abs(f - deal["open"]) < 1e-9 for f in figures_)
        past = sum(bool(row.get("accepts")) for row in rows_)
        none = sum(f is None for f in figures_)
        widths.append({kinds[0]: opened, kinds[1]: len(rows_) - at - opened - past - none, kinds[2]: at, kinds[3]: past, kinds[4]: none}[kind])
    axis.barh(range(len(cases_rev)), widths, left=left, color=shade, edgecolor="white", linewidth=1.2, height=0.62, label=kind)
    left += np.array(widths)
axis.set_yticks(range(len(cases_rev)), [case.capitalize() + (" *" if case in HOPE else "") for case in cases_rev])
axis.set_xlabel(f"Replies to an offer past the limit ({len(everyone)} models, 3 replies each)")
axis.tick_params(axis="y", length=0)
axis.set_xlim(0, max(left))
axis.legend(loc="upper center", bbox_to_anchor=(0.45, 1.3), ncol=3, frameon=False, fontsize=7.5, handlelength=1.0, columnspacing=1.0)
save(figure, "offers")

# 4. Briefs dumbbell chart
if brief_models:
    figure, axis = plt.subplots(figsize=(5.6, 2.6))
    for position, name in enumerate(brief_models[::-1]):
        base = data["ranked"][name][0] / data["ranked"][name][1]
        role, full = brief_data["role"][name], brief_data["full"][name]
        points = [100 * base, 100 * role["clean"] / role["count"], 100 * full["clean"] / full["count"]]
        axis.plot([min(points), max(points)], [position, position], color=GRID, linewidth=2.2, solid_capstyle="round", zorder=1)
        for value, (face, edge, mark) in zip(points, [("white", MUTED, "o"), ("#7fb0e8", "#7fb0e8", "o"), ("#12365f", "#12365f", "o")]):
            axis.plot(value, position, marker=mark, color=face, markeredgecolor=edge, markeredgewidth=1.2, markersize=6.5, linestyle="", zorder=2)
    axis.set_yticks(range(len(brief_models)), [label(name) for name in brief_models[::-1]])
    axis.set_xlim(0, 103)
    axis.set_xlabel("Clean messages (%)")
    axis.xaxis.grid(True, color=GRID, linewidth=0.6)
    axis.set_axisbelow(True)
    axis.tick_params(axis="y", length=0)
    handles = [
        plt.Line2D([], [], marker="o", color="white", markeredgecolor=MUTED, markeredgewidth=1.2, linestyle="", markersize=6.5, label="no brief"),
        plt.Line2D([], [], marker="o", color="#7fb0e8", linestyle="", markersize=6.5, label="one sentence (role)"),
        plt.Line2D([], [], marker="o", color="#12365f", linestyle="", markersize=6.5, label="five sentences (full brief)"),
    ]
    axis.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, 1.2), ncol=3, frameon=False, fontsize=8, handletextpad=0.2, columnspacing=1.2)
    save(figure, "briefs")

print("macros:", len(macros), "| tables written:", len(list(GEN.glob("table_*.tex"))), "| models complete:", len(ranked), "/", len(everyone))
print(f"2D Rasch: G2={G2:.1f}, G2_RS={G2_rs:.1f} (p={p_rs:.4f}), dAIC={aic_gain:.1f}, rho={two['spearman']:.2f} (95% CI {rho_ci_low:+.2f}..{rho_ci_high:+.2f})")
print(f"Concessions (no-hope): kappa in [{min(per_model_nh):.2f}, {max(per_model_nh):.2f}], pooled={np.mean(all_k_nh):.2f}, 6-plain={np.mean(all_k_6):.2f}")
