# Quant Analyst

- Symbol: TSEM
- Elapsed: 92.8s

---
## TSEM — Tower Semiconductor Ltd. | Quantitative Factor Report

**Prices as of 2026-06-01: $252.53** (mkt cap ~$28.7B, 113.6M diluted sh)

### ⚠️ Data-integrity flags (read first — they change several numbers)

1. **Stale price in the valuation module.** `calculate_valuation_ratios` and the company profile both used **$133.42** — the 2026-01-21 close, ~5 months stale. Actual last close is **$252.53 (1.89×)**. All multiples below are restated to the live price.
2. **Broken return series in the momentum/Sharpe tool family.** `momentum_score` returns **−20.67%** (252d) and **+4.8%** (126d); raw OHLCV shows **+527%** trailing-12m and **+126%** over the last 126 trading days. The tool's return inputs do not reconcile with the price file, so its Sharpe/Sortino/alpha are unreliable. I recompute from raw closes below.
3. **`earnings_revision_score` compares different fiscal years** (FY2029 $14.255 vs FY2028 $10.860) — that "+31.26%" is *
