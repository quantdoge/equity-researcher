import json
inc = json.load(open("data/statements_income-statement.json"))
print("fiscalYear types/values:", [(r["date"], repr(r.get("fiscalYear")), repr(r.get("period"))) for r in inc[:3]])