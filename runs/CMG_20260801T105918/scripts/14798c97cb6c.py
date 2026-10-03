
import json

inc = json.load(open('data/cmg_income_statement_12q.json'))
inc.sort(key=lambda x: x['date'])

print(f"{'Date':<12} {'Rev':>12} {'COGS':>12} {'GP':>12} {'EBIT':>12} {'NI':>12}")
for r in inc:
    print(f"{r['date']:<12} {r['revenue']:>12,.0f} {r['costOfRevenue']:>12,.0f} {r['grossProfit']:>12,.0f} {r['ebit']:>12,.0f} {r['netIncome']:>12,.0f}")
