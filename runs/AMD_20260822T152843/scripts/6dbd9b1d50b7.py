
import json

# Verify: compare netIncome from income statement vs cash flow statement
inc = sorted([r for r in json.load(open('data/statements_income-statement.json')) if r.get('period')=='FY'],
             key=lambda x: x['fiscalYear'], reverse=True)
cf = sorted([r for r in json.load(open('data/statements_cashflow-statement.json')) if r.get('period')=='FY'],
            key=lambda x: x['fiscalYear'], reverse=True)

print("Net Income cross-check (Income Stmt vs Cash Flow):")
for i in range(min(5, len(inc), len(cf))):
    fy = inc[i]['fiscalYear']
    ni_inc = inc[i].get('netIncome')
    ni_cf = cf[i].get('netIncome')
    print(f"  FY{fy}: IS=${ni_inc/1e6:.0f}M, CF=${ni_cf/1e6:.0f}M, diff=${(ni_inc-ni_cf)/1e6:.1f}M")

# Also check if there are any quarterly key-metrics denied issues to note
print("\nNote: Quarterly key-metrics endpoint returned plan_denied; annual key-metrics used instead.")
