import json

km = json.load(open("data/statements_key-metrics.json"))
mr = json.load(open("data/statements_metrics-ratios.json"))
inc = json.load(open("data/statements_income-statement.json"))
bs  = json.load(open("data/statements_balance-sheet-statement.json"))

def fy(rows, y):
    return next(r for r in rows if str(r.get("fiscalYear")) == str(y))

print("KEY METRICS (FY2025, FY2024, FY2023):")
for f in ["2025","2024","2023"]:
    r = fy(km, f)
    print(f"  {f}: netDebtToEBITDA={r.get('netDebtToEBITDA')}, evToEBITDA={r.get('evToEBITDA')}, "
          f"incomeQuality={r.get('incomeQuality')}, returnOnAssets={r.get('returnOnAssets')}, "
          f"daysOfSalesOutstanding={r.get('daysOfSalesOutstanding')}, averageReceivables={r.get('averageReceivables')}, "
          f"debtToEquity(km n/a), workingCapital={r.get('workingCapital')}")

print()
print("METRICS-RATIOS (FY2025, FY2024):")
for f in ["2025","2024"]:
    r = fy(mr, f)
    print(f"  {f}: debtToAssets={r.get('debtToAssetsRatio')}, debtToEquity={r.get('debtToEquity')}, "
          f"longTermDebtToCapital={r.get('longTermDebtToCapitalRatio')}, interestCoverage={r.get('interestCoverageRatio')}, "
          f"debtServiceCoverage={r.get('debtServiceCoverageRatio')}, effectiveTaxRate={r.get('effectiveTaxRate')}")

print()
print("INCOME STATEMENT full field dump FY2025 / FY2024 (non-null, non-zero):")
for f in ["2025","2024"]:
    r = fy(inc, f)
    print(f"  --- FY{f} ---")
    for k,v in sorted(r.items()):
        if v not in (None, 0) and k not in ("symbol","reportedCurrency","cik","filingDate","acceptedDate","fiscalYear","period","date"):
            print(f"    {k}: {v}")
