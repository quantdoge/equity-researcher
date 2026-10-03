import json

# Check key-metrics file
with open('data/statements_key-metrics.json') as f:
    km = json.load(f)
print("key-metrics symbols:", [r['symbol'] for r in km])

# Check metrics-ratios file
with open('data/statements_metrics-ratios.json') as f:
    mr = json.load(f)
print("metrics-ratios symbols:", [r['symbol'] for r in mr])

# Check financial-statement-growth file
with open('data/statements_financial-statement-growth.json') as f:
    fsg = json.load(f)
print("financial-statement-growth symbols:", [r['symbol'] for r in fsg])

# Check treasury rates
with open('data/economics_treasury-rates.json') as f:
    tr = json.load(f)
print("treasury rates latest:", tr[-1])
