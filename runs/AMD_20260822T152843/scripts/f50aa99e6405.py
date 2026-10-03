import json, os

# Load all relevant AMD files
files = {
    "balance_sheet": "data/amd_balance_sheet.json",
    "income_statement": "data/statements_income-statement.json",
    "cashflow_statement": "data/statements_cashflow-statement.json",
    "key_metrics": "data/amd_key_metrics_a.json",
    "metrics_ratios_ttm": "data/amd_metrics_ratios_ttm.json",
    "financial_scores": "data/amd_financial_scores.json",
}

for name, path in files.items():
    with open(path, "r") as f:
        data = json.load(f)
    print(f"\n=== {name} ===")
    if isinstance(data, list):
        print(f"Rows: {len(data)}")
        if data:
            print(f"Fields: {list(data[0].keys())}")
            # Show fiscal years if available
            years = [row.get("fiscalYear") or row.get("date") for row in data]
            print(f"Years/dates: {years}")
    elif isinstance(data, dict):
        print(f"Keys: {list(data.keys())}")
        if "fiscalYear" in data:
            print(f"Year: {data['fiscalYear']}")
        if "date" in data:
            print(f"Date: {data['date']}")
    else:
        print(data)
