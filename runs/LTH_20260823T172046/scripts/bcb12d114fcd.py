import json, os

def load(p):
    with open(p) as f:
        return json.load(f)

# 1) Income statement - the core series
inc = load("data/lth_income_annual.json")
print("=== INCOME STATEMENT (annual) ===")
for r in sorted(inc, key=lambda x: x["date"]):
    print(f"{r['date']}  rev={r['revenue']/1e6:9.1f}M  ebitda={r['ebitda']/1e6:8.1f}M  opinc={r['operatingIncome']/1e6:8.1f}M  ni={r['netIncome']/1e6:8.1f}M  epsD={r['epsDiluted']}")

print()
cf = load("data/lth_cashflow_annual.json")
print("=== CASH FLOW (annual) ===")
for r in sorted(cf, key=lambda x: x["date"]):
    print(f"{r['date']}  ocf={r['operatingCashFlow']/1e6:8.1f}M  capex={r['capitalExpenditure']/1e6:9.1f}M  fcf={r['freeCashFlow']/1e6:8.1f}M  sbc={r['stockBasedCompensation']/1e6:6.1f}M  intPaid={r.get('interestPaid')}")

print()
bs = load("data/lth_balance_annual.json")
print("=== BALANCE SHEET (annual) ===")
for r in sorted(bs, key=lambda x: x["date"]):
    print(f"{r['date']}  cash={r['cashAndCashEquivalents']/1e6:7.1f}M  totalDebt={r['totalDebt']/1e6:8.1f}M  netDebt={r['netDebt']/1e6:8.1f}M  ltd={r['longTermDebt']/1e6:8.1f}M  equity={r['totalStockholdersEquity']/1e6:8.1f}M")

print()
ev = load("data/lth_enterprise_values.json")
print("=== ENTERPRISE VALUES ===")
for r in sorted(ev, key=lambda x: x["date"]):
    print(f"{r['date']}  px={r['stockPrice']:7.2f}  mcap={r['marketCapitalization']/1e6:8.1f}M  ev={r['enterpriseValue']/1e6:9.1f}M")
