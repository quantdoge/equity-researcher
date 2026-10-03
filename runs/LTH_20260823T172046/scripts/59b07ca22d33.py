import json, math, statistics
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

out = {}

# ---------- 1. Quarterly statements: build TTM ----------
inc_q = sorted(load("lth_income_quarterly.json"), key=lambda r: r["date"])
cf_q  = sorted(load("lth_cashflow_quarterly.json"), key=lambda r: r["date"])
bs_q  = sorted(load("lth_balance_quarterly.json"), key=lambda r: r["date"])

print("=== QUARTERLY INCOME (all 8 rows) ===")
for r in inc_q:
    print(f"{r['date']} {r['period']:3s} rev={r['revenue']/1e6:7.1f} ebitda={r['ebitda']/1e6:7.1f} ebit={r['ebit']/1e6:7.1f} intExp={r['interestExpense']/1e6 if r['interestExpense'] else 0:6.1f} ni={r['netIncome']/1e6:7.1f} epsD={r['epsDiluted']}")

last4 = inc_q[-4:]
ttm = {
    "periods": [r["date"] for r in last4],
    "revenue": sum(r["revenue"] for r in last4),
    "ebitda": sum(r["ebitda"] for r in last4),
    "ebit": sum(r["ebit"] for r in last4),
    "interestExpense": sum(r["interestExpense"] or 0 for r in last4),
    "netIncome": sum(r["netIncome"] for r in last4),
    "incomeTaxExpense": sum(r["incomeTaxExpense"] or 0 for r in last4),
    "incomeBeforeTax": sum(r["incomeBeforeTax"] or 0 for r in last4),
}
print("\nTTM window:", ttm["periods"])
print(f"TTM rev={ttm['revenue']/1e6:.1f}M ebitda={ttm['ebitda']/1e6:.1f}M ebit={ttm['ebit']/1e6:.1f}M intExp={ttm['interestExpense']/1e6:.1f}M ni={ttm['netIncome']/1e6:.1f}M tax={ttm['incomeTaxExpense']/1e6:.1f}M ebt={ttm['incomeBeforeTax']/1e6:.1f}M")

cf4 = cf_q[-4:]
ttm_cf = {
    "ocf": sum(r["operatingCashFlow"] for r in cf4),
    "capex": sum(r["capitalExpenditure"] for r in cf4),
    "sbc": sum(r["stockBasedCompensation"] or 0 for r in cf4),
    "fcf": sum(r["freeCashFlow"] for r in cf4),
}
print(f"TTM OCF={ttm_cf['ocf']/1e6:.1f}M capex={ttm_cf['capex']/1e6:.1f}M fcf={ttm_cf['fcf']/1e6:.1f}M sbc={ttm_cf['sbc']/1e6:.1f}M")
sbc_adj_fcf = ttm_cf["ocf"] + ttm_cf["capex"] + ttm_cf["sbc"]
print(f"TTM SBC-adjusted FCF (OCF - capex + SBC) = {sbc_adj_fcf/1e6:.1f}M")

out["ttm"] = ttm; out["ttm_cf"] = ttm_cf; out["sbc_adj_fcf_ttm"] = sbc_adj_fcf

# FMP TTM cross-check
km_ttm = load("lth_key_metrics_ttm.json")[0]
fmp_ebitda_ttm = (km_ttm["marketCap"] + 4263276000 - 223647000) / km_ttm["evToEBITDATTM"]
print(f"\nFMP key-metrics-ttm: mcap={km_ttm['marketCap']/1e6:.0f}M EV={km_ttm['enterpriseValueTTM']/1e6:.0f}M EV/EBITDA={km_ttm['evToEBITDATTM']:.2f} -> implied TTM EBITDA={fmp_ebitda_ttm/1e6:.1f}M (my quarterly sum: {ttm['ebitda']/1e6:.1f}M)")
