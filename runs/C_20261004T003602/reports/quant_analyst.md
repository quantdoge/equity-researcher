# Quant Analyst

- Symbol: C
- Elapsed: 100.6s

---
All data collected. The cross-sectional rank tools only cover a 25-name mega-cap universe (C not included), so I'll flag that gap and rank C qualitatively against its bank peer set instead. Writing the report now.

---

# Citigroup Inc. (C) — Quantitative Factor Report

**Sector:** Financial Services (Banks – Diversified) | **Price:** $128.50 | **Mkt Cap:** ~$220B | Data window: 252 trading days

## 1. Factor Scores

| Factor | Score | Universe Rank | Signal |
|--------|-------|---------------|--------|
| Value | **6/10** — P/B 1.12×, P/E 18.4×, EV/EBITDA 11.6×, Div yield 1.92% | n/a (see gap) | **Positive** |
| Momentum | **2/10** — 12-1m return **−3.3%** | n/a (see gap) | **Negative** |
| Quality | **2/10** — ROE 6.7%, ROIC 2.1%, gross profit/assets 2.8%, accruals 3.1%, F-Score 4/9 | n/a (see gap) | **Negative** |
| Low Vol | **2/10** — Ann. vol **30.9%**, beta 1.42 vs SPY | n/a (see gap) | **Negative** |
| Earnings Revision | **8/10** — FY30 EPS est. raised +14.4% (18.30 vs 16.00 3m ago); EPS path rising 2027→2030 (12.78/14.81/16.00/18.30) | Top-quartile | **Positive** |

**Cross-sectional gap:** The factor rank endpoint covers a 25-name mega-cap universe from which C is absent; sector-relative z-scores were not computable. Against the visible big-bank set (JPM, BAC, WFC, GS, MS), C's ROE (~6.7%) is the lowest, its P/B (~1.1×) the cheapest, and its beta the highest — consistent with a "cheap but lower-quality, higher-beta" profile.

## 2. Price Statistics (1Y, benchmark SPY)

| Metric | Value |
|--------|-------|
| Alpha (ann.) | **−7.8%** |
| Beta | **1.43** (R² = 0.36) |
| Sharpe | **0.40** |
| Sortino | **0.58** |
| Ann. return / vol | +12.3% / 30.9% |
| Max drawdown | **−14.8%** |

## 3. Composite Quant Signal: **NEUTRAL**

**Scoring logic:** Estimate-revision momentum is the single most predictive input and it is strongly positive (+14.4%, consistently rising EPS path, 5 of 6 recent price-target actions at/above current price — Evercore $140, HSBC $164, Argus $150, avg target ≈$149 vs $128.50 price). Valuation is reasonable on P/B. However, price momentum is negative (−3.3% 12-1), quality is weak (ROE 6.7%, F-Score 4 "weak", accruals 3.1%), and the stock carries high beta/vol with negative alpha (−7.8%). Positives and negatives largely offset → **Neutral**, tilting positive only if estimate upgrades continue to convert into reported EPS.

## 4. Key Quant Risk Flags

- **Momentum reversal risk:** 12-1 momentum negative yet trailing 1Y return +12.3% — recent strength sits on top of an extended down-leg; short-term reversal sensitivity is elevated (Sortino 0.58 < Sharpe implies fat left tail).
- **Factor crowding / beta exposure:** Correlation high with MS (0.75), BAC (0.73), JPM (0.69) — a bank-sector drawdown hits C hardest given beta 1.42. R² vs SPY only 0.36 — idiosyncratic capital-markets exposure is large.
- **Earnings-quality flags:** FCF per valuation screen is **negative** (P/FCF −3.2; bank working-capital artifact, but abnormal CFO volatility across years); Piotroski F-Score 4 (weak, driven by negative op-CF and rising leverage components).
- **Small-sample revision data:** The +14.4% upgrade and FY29/FY30 estimates rest on only **4 covering analysts** (11–13 for nearer years) — revision signal is directionally reliable but statistically thin; do not overweight.

**Gaps/limitations:** Peer-relative sector ranks unavailable (factor universe excludes C). Funded FCF metrics are unreliable for diversified banks — treat P/FCF as noise.
