import json, math
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

inc_q = sorted(load("lth_income_quarterly.json"), key=lambda r: r["date"])
cf_q  = sorted(load("lth_cashflow_quarterly.json"), key=lambda r: r["date"])
bs_q  = sorted(load("lth_balance_quarterly.json"), key=lambda r: r["date"])
inc_a = sorted(load("lth_income_annual.json"), key=lambda r: r["date"])
cf_a  = sorted(load("lth_cashflow_annual.json"), key=lambda r: r["date"])

ttm_rev   = sum(r["revenue"] for r in inc_q[-4:])
ttm_ebitda= sum(r["ebitda"] for r in inc_q[-4:])
ttm_ebit  = sum(r["ebit"] for r in inc_q[-4:])
ttm_ni    = sum(r["netIncome"] for r in inc_q[-4:])
ttm_epsD  = sum(r["epsDiluted"] for r in inc_q[-4:])
q226 = bs_q[-1]
fin_debt = q226["shortTermDebt"] + q226["longTermDebt"]
lease    = q226["capitalLeaseObligationsCurrent"] + q226["capitalLeaseObligationsNonCurrent"]
cash     = q226["cashAndCashEquivalents"]

# ---------- 4. Current valuation marks (price 45.11, screener mcap) ----------
scr = load("search_search-company-screener.json")
lth_row = [r for r in scr if r["symbol"]=="LTH"][0]
px, mcap = lth_row["price"], lth_row["marketCap"]
ev_fin = mcap + fin_debt - cash
ev_lease = mcap + fin_debt + lease - cash
print("=== CURRENT VALUATION MARKS @ $%.2f (mcap $%.0fM, as of 2026-08-21) ===" % (px, mcap/1e6))
print(f"TTM (Q3'25-Q2'26): rev={ttm_rev/1e6:.0f}M ebitda={ttm_ebitda/1e6:.0f}M (margin {ttm_ebitda/ttm_rev*100:.1f}%) ni={ttm_ni/1e6:.0f}M epsD={ttm_epsD:.2f}")
print(f"EV (fin debt only)      = {ev_fin/1e6:,.0f}M -> EV/EBITDA={ev_fin/ttm_ebitda:.2f}x  EV/Sales={ev_fin/ttm_rev:.2f}x")
print(f"EV (incl. lease oblig.) = {ev_lease/1e6:,.0f}M -> EV/EBITDA={ev_lease/ttm_ebitda:.2f}x  EV/Sales={ev_lease/ttm_rev:.2f}x  [FMP's convention: 15.13x]")
print(f"P/E (TTM) = {mcap/ttm_ni:.1f}x   (px/epsD_ttm = {px/ttm_epsD:.1f}x)")
print(f"net fin debt/EBITDA = {(fin_debt-cash)/ttm_ebitda:.2f}x   lease-incl = {(fin_debt+lease-cash)/ttm_ebitda:.2f}x")

# FY-end anchor comparison (Dec 31, 2025, px 26.58)
mcap_25, cash_25 = 5795263980, 232169000
fd_25 = 1507787000; ol_25 = 2634721000
ev25_fin = mcap_25 + fd_25 - cash_25
ev25_ls  = mcap_25 + fd_25 + ol_25 - cash_25
ebitda_25 = [r["ebitda"] for r in inc_a if r["date"].startswith("2025")][0]
print(f"\nFY25 anchor @ $26.58: EV(fin)={ev25_fin/1e6:,.0f}M -> {ev25_fin/ebitda_25:.2f}x FY25 EBITDA; EV(lease-incl)={ev25_ls/1e6:,.0f}M -> {ev25_ls/ebitda_25:.2f}x")
print(f"Multiple expansion since FY-end: fin {ev_fin/ttm_ebitda/(ev25_fin/ebitda_25)-1:+.1%}, lease-incl {ev_lease/ttm_ebitda/(ev25_ls/ebitda_25)-1:+.1%} (price +{(px/26.58-1)*100:.0f}%)")

# ---------- 5. Owner earnings & FCF quality ----------
print("\n=== FMP OWNER EARNINGS (quarterly, as returned) ===")
oe = sorted(load("lth_owner_earnings.json"), key=lambda r: r["date"])
for r in oe:
    print(f"{r['date']} {r['fiscalYear']} {r['period']}: ownersEarnings={r['ownersEarnings']/1e6:8.1f}M  maintCapex={r['maintenanceCapex']/1e6:9.1f}M  growthCapex={r['growthCapex']/1e6:9.1f}M  oe/sh={r['ownersEarningsPerShare']}")
oe_ttm = sum(r["ownersEarnings"] for r in oe[-4:])
print(f"TTM owner earnings (sum last 4 qtrs, FMP defn) = {oe_ttm/1e6:.1f}M  [caveat: FMP maintenanceCapex line is unstable (sign flips)]")

print("\n=== FCF QUALITY (annual) ===")
for ic, cfr in zip(inc_a[2:], cf_a[2:]):  # 2022+
    yr = ic["date"][:4]
    ocf, capex, fcf, sbc = cfr["operatingCashFlow"], cfr["capitalExpenditure"], cfr["freeCashFlow"], cfr["stockBasedCompensation"] or 0
    print(f"FY{yr}: OCF={ocf/1e6:7.1f}M capex={-capex/1e6:7.1f}M FCF={fcf/1e6:7.1f}M SBC={sbc/1e6:5.1f}M  FCF/EBITDA={fcf/ic['ebitda']*100:6.1f}%  capex/rev={-capex/ic['revenue']*100:5.1f}%  adjFCF(OCF-capex+SBC)={(ocf+capex+sbc)/1e6:7.1f}M")
ocf_t = sum(r["operatingCashFlow"] for r in cf_q[-4:]); capex_t = sum(r["capitalExpenditure"] for r in cf_q[-4:]); sbc_t = sum(r["stockBasedCompensation"] or 0 for r in cf_q[-4:])
print(f"TTM: OCF={ocf_t/1e6:.1f}M capex={-capex_t/1e6:.1f}M FCF={(ocf_t+capex_t)/1e6:.1f}M SBC={sbc_t/1e6:.1f}M adjFCF={(ocf_t+capex_t+sbc_t)/1e6:.1f}M capex/rev={-capex_t/ttm_rev*100:.1f}% FCF/EBITDA={(ocf_t+capex_t)/ttm_ebitda*100:.1f}%")

# ---------- 6. Scores ----------
fs = load("lth_financial_scores.json")[0]
print(f"\n=== FMP FINANCIAL SCORES (on Q2'26 data) ===\nAltman Z = {fs['altmanZScore']:.2f} (grey zone 1.81-2.99)   Piotroski F = {fs['piotroskiScore']}/9")
