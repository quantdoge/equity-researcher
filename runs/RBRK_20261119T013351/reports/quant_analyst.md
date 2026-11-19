# Quant Analyst

- Symbol: RBRK
- Elapsed: 20.2s

---
# RBRK — Rubrik, Inc. | Quantitative Factor Report

**Sector:** Technology — Software–Infrastructure | **Price:** $110.00 | **Mkt Cap:** ~$21.6–22.6B | **IPO:** 2024-04-25 | **Diluted shares:** 196.5M

> **Sample-size caveat (material):** RBRK IPO'd 2024-04-25, so the entire return history is short. The 252-day regression uses a single, unusually strong trailing year — this is **one regime**, not a full cycle. All price-based statistics below carry elevated estimation error (see beta R² note).

## 1. Factor Scores Table

| Factor | Raw Score | Sector Rank* | Signal |
|--------|-----------|--------------|--------|
| **Value** | P/E −61.8; EV/EBITDA −77.4; P/FCF 85.3; P/B n/a (neg. book −$2.64/sh) | Bottom quintile (est.) | **Bearish / expensive** |
| **Momentum** | +24.2% (12-1, ex-last-21d); 12m total return +127.7% | Top quintile (est.) | **Bullish** |
| **Quality** | GProf/Assets 0.38; ROE 67.1%†; ROIC −56.5%; accruals −0.23 | Middle (distorted) | **Neutral / Moderate** |
| **Low Vol** | Ann. vol 66.9%; β ≈ 1.65; max DD −26.0% | Bottom quintile | **Bearish (high-vol)** |
| **Earnings Revision** | +32.1% (FY2031 EPS $2.04 vs $1.54 prior) | n/a — only 2 analysts | **Bullish but low-confidence** |

*Sector ranks are qualitative estimates. The peer feed returned mega-cap Tech (AAPL/MSFT/NVDA), **not** software comparables — a proper cross-sectional percentile within Software–Infrastructure was **unavailable**, so ranks are inferred from absolute factor levels vs. typical SaaS norms. Treat as directional only.

†**ROE of 67% and the tool's "high" quality signal are artifacts of negative shareholders' equity (book value −$2.64/share).** ROE/ROIC are not economically meaningful here and should be ignored as quality evidence. The genuine quality positives are cash generation (OCF +$283M) and negative accruals (−0.23, conservative accounting). Piper F-Score = **6/9 (Moderate)**, dragged by negative ROA and share dilution (F7=0).

## 2. Price Statistics (252-day window)

| Metric | Value |
|--------|-------|
| Annualised return | **+127.7%** |
| Annualised volatility | **66.9%** |
| Beta vs SPY | **1.65** (regression); 1.081 (profile — stale) |
| **Alpha (annualised)** | **+95.0%** |
| **R² vs SPY** | **0.128** |
| **Sharpe** | **1.90** |
| **Sortino** | **3.12** |
| Max drawdown | −26.0% |

**On the alpha/beta:** the +95% alpha with an R² of only 0.128 means SPY explains just ~13% of RBRK's variance. The beta (1.65) and alpha are **poorly identified** — high standard errors, single-regime sample. The 3.1 Sortino vs 1.9 Sharpe gap shows returns are driven by large up-captures with modest downside; that asymmetry is real but likely flatters the stock until a drawdown cycle validates it.

## 3. Composite Quant Signal

### **NEUTRAL** (positive momentum/quality tilt; valuation is the binding constraint)

- **For (bull case):** Top-quartile momentum (+24% 12-1), strong price trend, positive and improving estimate revisions, +$283M operating cash flow, high Sortino, positive alpha.
- **Against (bear case):** Bottom-quartile value — GAAP-unprofitable (P/E −62, EV/EBITDA −77), negative book equity, 67% vol, β 1.65, +95% alpha resting on a 1-year sample with R² 0.13. The "cheap-looking" quality score is an accounting artifact, not economics.

Momentum is doing all the work; the valuation and low-vol screens are a clear drag. This is a high-beta growth name, not a factor-diversified compounder.

## 4. Key Quant Risk Flags

1. **Momentum reversal / crowded growth:** A +128% 12-month run with 67% vol is highly susceptible to a sharp factor rotation against high-multiple SaaS. Beta 1.65 amplifies any market drawdown.
2. **Valuation as a trapdoor:** No earnings support (negative P/E, EV/EBITDA). Any growth deceleration removes the only leg supporting the multiple. P/FCF of 85 is a rich cash-flow multiple.
3. **Micro sample / weak identification:** 1-year history post-IPO; alpha, beta, Sharpe, and Sortino all carry wide confidence intervals. Beta conflicts across sources (1.08 vs 1.65) — do not anchor to a precise number.
4. **Revision signal is thin:** The +32% revision is on **FY2031** estimates compiled by **only 2 analysts** — 5 years forward. Statistically weak; discount heavily versus a near-term consensus revision.
5. **Liquidity/float:** Adequate at $21B cap; not a liquidity flag, but the **dilution** (F-Score F7 = 0, 196M diluted shares) is a persistent per-share drag.
6. **Comparable-set gap:** No true software-peer cross-section was available; sector percentiles above are estimates, not computed z-scores.

**Bottom line:** A statistically *strong* trailing price/factor record built on a single year of history — treat with scepticism. Quantitatively this is a **momentum trade with negative value and volatility exposure**, appropriately sized as high-beta, not a core quality holding.
