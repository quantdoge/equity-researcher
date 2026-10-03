import json

inc = json.load(open("data/statements_income-statement.json"))
bs  = json.load(open("data/statements_balance-sheet-statement.json"))
cf  = json.load(open("data/statements_cashflow-statement.json"))

def by_fy(rows, fy):
    for r in rows:
        if str(r.get("fiscalYear")) == str(fy):
            return r
    return None

i25, i24, i23 = by_fy(inc,2025), by_fy(inc,2024), by_fy(inc,2023)
b25, b24, b23 = by_fy(bs,2025), by_fy(bs,2024), by_fy(bs,2023)
c25, c24, c23 = by_fy(cf,2025), by_fy(cf,2024), by_fy(cf,2023)

def fmt(v):
    if v is None: return f"{'None':>16s}"
    if isinstance(v,(int,float)): return f"{v:>16,.2f}"
    return f"{str(v)[:16]:>16s}"

def show(name, rows, keys):
    print("="*110)
    print(name)
    hdr = f"{'field':45s}" + "".join(f"{r['date'][:4]:>18s}" for r in rows)
    print(hdr)
    for k in keys:
        line = f"{k:45s}" + "".join(fmt(r.get(k)) for r in rows)
        print(line)

show("INCOME STATEMENT", [i25,i24,i23], [
 "revenue","costOfRevenue","grossProfit","sellingGeneralAndAdministrativeExpenses",
 "generalAndAdministrativeExpenses","sellingAndMarketingExpenses","otherExpenses",
 "operatingExpenses","costAndExpenses","interestIncome","interestExpense","netInterestIncome",
 "depreciationAndAmortization","ebitda","ebit","operatingIncome",
 "incomeBeforeTax","incomeTaxExpense","netIncome","netIncomeFromContinuingOperations",
 "eps","epsDiluted","weightedAverageShsOut","weightedAverageShsOutDil"])

show("BALANCE SHEET", [b25,b24,b23], [
 "netReceivables","accountsReceivables","otherReceivables","totalCurrentAssets",
 "shortTermInvestments","longTermInvestments","cashAndCashEquivalents",
 "cashAndShortTermInvestments","propertyPlantEquipmentNet","totalAssets",
 "totalPayables","accountPayables","accruedExpenses","shortTermDebt",
 "capitalLeaseObligationsCurrent","longTermDebt","capitalLeaseObligationsNonCurrent",
 "capitalLeaseObligations","otherCurrentLiabilities","totalCurrentLiabilities",
 "otherNonCurrentLiabilities","deferredTaxLiabilitiesNonCurrent","totalNonCurrentLiabilities",
 "totalLiabilities","totalStockholdersEquity","totalDebt","netDebt"])

show("CASH FLOW", [c25,c24,c23], [
 "netIncome","depreciationAndAmortization","netCashProvidedByOperatingActivities",
 "operatingCashFlow","capitalExpenditure","freeCashFlow","commonStockRepurchased",
 "interestPaid","incomeTaxesPaid","stockBasedCompensation","changeInWorkingCapital"])
