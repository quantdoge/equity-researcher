
import json

# Quick verification of key numbers
inc = sorted([r for r in json.load(open('data/statements_income-statement.json')) if r.get('period')=='FY'],
             key=lambda x: x['fiscalYear'], reverse=True)
bs = sorted([r for r in json.load(open('data/amd_balance_sheet.json')) if r.get('period')=='FY'],
            key=lambda x: x['fiscalYear'], reverse=True)

print("Revenue history (annual):")
for r in inc:
    print(f"  FY{r['fiscalYear']}: ${r.get('revenue',0)/1e9:.2f}B")

print("\nBalance sheet equity history:")
for r in bs:
    print(f"  FY{r['fiscalYear']}: Equity=${r.get('totalStockholdersEquity',0)/1e9:.2f}B, Debt={r.get('totalDebt',0)/1e9:.2f}B")

# Verify 2021 ROE
ni_2021 = next((r.get('netIncome') for r in inc if r['fiscalYear']=='2021'), None)
eq_2021 = next((r.get('totalStockholdersEquity') for r in bs if r['fiscalYear']=='2021'), None)
if ni_2021 and eq_2021:
    print(f"\n2021 Net Income=${ni_2021/1e9:.2f}B, Equity=${eq_2021/1e9:.2f}B")
    print(f"2021 ROE (computed) = {ni_2021/eq_2021*100:.1f}%")

# Verify DCF values
dcf = json.load(open('data/amd_dcf_advanced.json'))[0]
print(f"\nDCF Advanced raw: {dcf}")

# Verify 2020 revenue
rev_2020 = next((r.get('revenue') for r in inc if r['fiscalYear']=='2020'), None)
print(f"\n2020 Revenue: ${rev_2020/1e9:.2f}B" if rev_2020 else "2020 Revenue not found")
