import json
with open('data/technicalIndicators_relative-strength-index.json') as f:
    rsi = json.load(f)
print("RSI first 3 rows:", rsi[:3])
print("RSI last 3 rows:", rsi[-3:])
with open('data/technicalIndicators_standard-deviation.json') as f:
    std = json.load(f)
print("\nStd dev first 3 rows:", std[:3])
print("Std dev last 3 rows:", std[-3:])
