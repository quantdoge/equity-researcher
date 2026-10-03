
import json
import os
from datetime import datetime
import math

# Load all available datasets
files = {
    'quote': 'data/amd_quote.json',
    'key_metrics_a': 'data/amd_key_metrics_a.json',
    'metrics_ratios_ttm': 'data/amd_metrics_ratios_ttm.json',
    'financial_scores': 'data/amd_financial_scores.json',
    'dcf_advanced': 'data/amd_dcf_advanced.json',
    'dcf_levered': 'data/amd_dcf_levered.json',
    'owner_earnings': 'data/amd_owner_earnings.json',
    'income_statement': 'data/amd_income_statement.json',
    'balance_sheet': 'data/amd_balance_sheet.json',
    'cash_flow': 'data/statements_cashflow-statement.json',
    'price_history': 'data/chart_historical-price-eod-dividend-adjusted.json',
    'financial_growth': 'data/statements_financial-statement-growth.json',
    'income_growth': 'data/statements_income-statement-growth.json',
    'metrics_ratios': 'data/statements_metrics-ratios.json',
    'income_statement_full': 'data/statements_income-statement.json',
}

data = {}
for name, path in files.items():
    if os.path.exists(path):
        with open(path, 'r') as f:
            data[name] = json.load(f)
        print(f"Loaded {name}: {len(data[name])} rows")
    else:
        print(f"MISSING {name}: {path}")

# Check schemas
print("\n=== SCHEMA CHECK ===")
for name, rows in data.items():
    if isinstance(rows, list) and len(rows) > 0:
        print(f"{name}: {list(rows[0].keys())[:10]}... ({len(rows)} rows)")
    elif isinstance(rows, dict):
        print(f"{name}: dict keys = {list(rows.keys())[:10]}...")
