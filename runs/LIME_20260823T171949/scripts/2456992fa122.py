import json

# ============================================================================
# LIME (Neutron Holdings, NASDAQ) - valuation & DCF
# ALL INPUTS ARE EXTERNAL (web/S-1-cited, supplied by the analyst in the
# request). NOT fetched from FMP - FMP has no statements for this Jul-2026
# IPO (prior lime_income_q/balance_q/cashflow_q calls in this workspace
# returned no data). Every number below is computed here from those inputs.
# $M unless noted. Shares in millions.
# ============================================================================

P0      = 41.06           # current price ($)                       [external]
MKTCAP  = 2628.904932     # market cap ($M) = $2,628,904,932        [external]
IPO_PX  = 25.00           # IPO price, Jul 1 2026                   [external]
REF_PX  = 34.30           # Q2-earnings-day reference price         [external]
REV     = {"2023": 522.0, "2024": 686.6, "2025": 886.7, "2026E": 1070.0}  # [external]
EBITDA  = {"2025": 218.1, "2026E": 275.0}   # adj EBITDA ($M)       [external]
FCF25   = 103.8           # 2025 FCF ($M)                           [external]
SHARES  = 65.0            # shares outstanding (M)      [ASSUMPTION - flagged]
EV      = MKTCAP          # net debt ~= 0 post-IPO      [ASSUMPTION - flagged]

N       = 10              # DCF horizon, years
G_TERM  = 0.035           # terminal growth
G1, G10 = 0.25, 0.035     # yr-1 and yr-10 FCF growth rates
WACCS   = [0.10, 0.115, 0.13]
BASES   = {"A": 103.8, "B": 218.0}

out = {}

# --- 1. price change ---
out["1_price_change_pct"] = {
    "IPO->current":  round((P0/IPO_PX - 1)*100, 2),
    "REF->current":  round((P0/REF_PX - 1)*100, 2),
}

# --- 2. revenue CAGR ---
out["2_rev_cagr_pct"] = {
    "2023->2025 (2y)":  round(((REV["2025"]/REV["2023"])**0.5  - 1)*100, 2),
    "2023->2026E (3y)": round(((REV["2026E"]/REV["2023"])**(1/3) - 1)*100, 2),
}

# --- 3. adj EBITDA margin ---
out["3_adj_ebitda_margin_pct"] = {
    "2025":  round(EBITDA["2025"]/REV["2025"]*100, 2),
    "2026E": round(EBITDA["2026E"]/REV["2026E"]*100, 2),
}

# --- 4. Rule of 40 (2025) ---
g25 = (REV["2025"]/REV["2024"] - 1)*100
fcm = FCF25/REV["2025"]*100
out["4_rule_of_40_2025"] = {
    "rev_growth_pct": round(g25, 2),
    "fcf_margin_pct": round(fcm, 2),
    "total":          round(g25 + fcm, 2),
}

# --- 5. implied serviceable market ---
out["5_implied_sam_$M"] = {
    f"at {int(s*100)}% share": round(REV["2025"]/s, 1) for s in (0.27, 0.25, 0.29)
}

# --- 6. multiples ---
out["6_multiples_x"] = {
    "P/S trailing 2025":  round(MKTCAP/REV["2025"], 2),
    "P/S forward 2026E":  round(MKTCAP/REV["2026E"], 2),
    "EV/adjEBITDA 2025":  round(EV/EBITDA["2025"], 2),
    "EV/adjEBITDA 2026E": round(EV/EBITDA["2026E"], 2),
    "P/FCF 2025":         round(MKTCAP/FCF25, 2),
    "EV/Revenue 2025":    round(EV/REV["2025"], 2),
}

# --- 7. DCF ---
# Primary reading: Year-1 FCF = base x 1.25 (the +25% growth APPLIES in yr 1);
# growth then declines linearly to +3.5% in yr 10 (step -2.3889 pp/yr).
# End-of-year discounting; TV = FCF_10 x (1+g)/(WACC-g), discounted 10 yrs.
def dcf(base, wacc, y1_fcf_is_base=False):
    if y1_fcf_is_base:  # alternative reading: FCF_1 = base, +25% starts yr 2
        gs   = [G1 - (G1 - G10)*i/8 for i in range(9)]      # 9 rates, yrs 2-10
        fcfs = [base]
        for g in gs:
            fcfs.append(fcfs[-1]*(1+g))
    else:               # primary reading: 10 rates, yrs 1-10
        gs   = [G1 - (G1 - G10)*i/9 for i in range(10)]
        fcfs, f = [], base
        for g in gs:
            f *= (1+g)
            fcfs.append(f)
    pv_fcf = sum(f/(1+wacc)**(t+1) for t, f in enumerate(fcfs))
    tv     = fcfs[-1]*(1+G_TERM)/(wacc - G_TERM)
    pv_tv  = tv/(1+wacc)**N
    iv     = pv_fcf + pv_tv          # equity value = EV (net debt ~ 0)
    return {"growth_pct":      [round(g*100, 2) for g in gs],
            "fcf_$M":          [round(f, 1) for f in fcfs],
            "pv_fcf_$M":       round(pv_fcf, 1),
            "tv_$M":           round(tv, 1),
            "pv_tv_$M":        round(pv_tv, 1),
            "value_$M":        round(iv, 1),
            "iv_per_share_$":  round(iv/SHARES, 2),
            "prem_disc_pct":   round((iv/SHARES/P0 - 1)*100, 1)}

tbl = {}
for b, base in BASES.items():
    for w in WACCS:
        tbl[f"base {b} (${base:.1f}M) | WACC {w*100:.1f}%"] = dcf(base, w)
out["7_dcf_primary"] = tbl

out["7_dcf_alt_iv_per_share_$"] = {
    f"base {b} | WACC {w*100:.1f}%": dcf(base, w, y1_fcf_is_base=True)["iv_per_share_$"]
    for b, base in BASES.items() for w in WACCS
}

# --- 8. exit-multiple check (undiscounted spot check) ---
out["8_exit_multiple_check"] = {
    f"{m}x": {"EV_$M":     round(EBITDA["2026E"]*m, 1),
              "px_$":      round(EBITDA["2026E"]*m/SHARES, 2),
              "vs_px_pct": round((EBITDA["2026E"]*m/SHARES/P0 - 1)*100, 1)}
    for m in (10, 15, 20)}

# --- consistency: shares implied by given price & market cap ---
out["implied_shares_from_price_M"] = round(MKTCAP/P0, 2)
out["mktcap_if_65M_shares_$M"]     = round(P0*SHARES, 1)

print(json.dumps(out, indent=1))

# save a clean named copy of this script in the run workspace root
import os, shutil, glob
me = max(glob.glob("scripts/*.py"), key=os.path.getmtime)
shutil.copyfile(me, "lime_valuation.py")