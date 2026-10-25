# Quant Analyst

- Symbol: ZS
- Elapsed: 166.8s

---
## Zscaler, Inc. (ZS) — Quantitative Factor Analysis

**Sector:** Technology — Software Infrastructure · **Market Cap:** ~$37.7B · **Price:** $231.33 · **Beta (reported):** 0.94

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E −593× (N/M, loss-making); P/B 14.3×; EV/EBITDA 190×; P/FCF 43.5× | **Bottom quintile** (~10th pctile) | **Strong Sell** |
| **Momentum** | 12-1 momentum **+41.0%** | **Top quintile** (~90th+) | **Strong Buy** |
| **Quality** | ROE −2.4%, ROIC −3.0%, GP/Assets 32.7%, Accruals −15.2% (cash-backed); Piotroski F=5 | **Third quartile** | **Neutral / Weak** |
| **Low Vol** | Ann. vol **73.2%**, β≈1.0, max DD 46.3% | **Bottom decile** | **Strong Sell** |
| **Earnings Revision** | Fwd EPS **+50.3%** revision (7.43→11.17); "upgrade" | **Top quintile** (low confidence*) | **Buy** |

\*Revision signal is directionally strong but structurally suspect — see risk flags.

**Reading the factors:** ZS is a textbook high-growth, richly-valued software name. It screens as a *momentum + estimate-revision* candidate and a *value + low-volatility* anti-candidate. Quality is bifurcated: poor on profitability (negative GAAP ROE/ROIC) but excellent on cash conversion (accruals −15%, meaning operating cash flow of ~$1.13B massively exceeds net income of −$63M — earnings quality is high even though the bottom line is a loss). The composite is genuinely conflicted.

---

### 2. Price Statistics (252-day window, vs. SPY)

| Metric | Value |
|--------|-------|
| Annualised return | **+42.6%** |
| Annualised volatility | **74.3%** |
| **Sharpe ratio** | **0.572** |
| **Sortino ratio** | **0.645** |
| **Alpha (annualised)** | **+20.8%** |
| **Beta (vs SPY)** | **1.00** |
| **R² (explanatory power)** | **0.032** |
| Max drawdown | **−46.3%** |

**Interpretation:** The Sharpe (0.57) and Sortino (0.65) are respectable in absolute terms and the +20.8% alpha looks attractive — but the **R² of 0.032 is the critical number**: only ~3% of ZS's return variance is explained by the market. The reported beta of 1.00 is therefore statistically near-meaningless (it's essentially an artifact of an uninformative regression). ZS's returns are driven by idiosyncratic/sector-specific forces, not market beta. The Sortino/Sharpe gap is modest, suggesting volatility is fairly symmetric (limited downside asymmetry despite the −46% peak-to-trough drawdown). A 74% annualised vol means this is a very high-risk single-name position — position-sizing must reflect that.

---

### 3. Composite Quant Signal

> ## **NEUTRAL** (momentum-tilted, high-risk)

**Rationale:** The two strongest live signals — 12-1 momentum (+41%) and upward EPS revisions (+50%) — argue **Buy**. But three of five factors are strongly negative: valuation is extreme on every multiple (bottom-decile value), volatility is among the highest in the sector (73% ann.), and profitability is negative on a GAAP basis. The factors don't cohere — this is not the rare "top value + momentum + quality" triple. A momentum/CTA-style strategy would hold it; a value or quality screen would exclude it. Net call: **Neutral**, suitable only for momentum/quant-tilt or high-risk-tolerance mandates with strict sizing.

---

### 4. Key Quant Risk Flags

- **⚠ Extreme valuation / value trap for growth:** P/E N/M (loss), EV/EBITDA 190×, P/B 14.3×, P/FCF 43.5×. Any multiple compression or growth deceleration triggers violent de-rating — no valuation floor.
- **⚠ Momentum-reversal & crowding risk:** +41% 12-1 momentum in a crowded mega-cap software/AI-security theme; beta/R² confirms heavy idiosyncratic (sentiment-driven) pricing. High reversal risk on any guidance miss.
- **⚠ Volatility & drawdown:** 73% annualised vol and a −46% max drawdown — among the highest-vol names in the Technology peer set. Requires outsized position-size haircut.
- **⚠ Thin, long-dated estimate data (statistical validity):** The +50% revision compares a **2031** EPS estimate ($11.17, only 6 analysts) against a prior **2030** figure ($7.43, just 2 analysts) — a 5-year-out, thinly-covered comparison with wide dispersion ($10.93–$11.67). The revision *direction* is positive but the signal's reliability is low; near-term estimates ($5.60 for FY28, 24 analysts) are the more meaningful anchor. Treat the revision score with caution.
- **⚠ Profitability quality:** Negative ROE/ROIC and a 5/9 Piotroski score — cash generation is strong (accruals −15%) but the company remains unprofitable on GAAP earnings, so "quality" is cash-flow quality rather than earnings quality.

---

**Data caveats:** Sector-rank placements are qualitative estimates — the peer set returned is dominated by mega-cap semis (NVDA, TSM, AVGO) and the ranking is not a computed cross-sectional z-score. Beta/alpha regression has very low explanatory power (R²=0.03), so treat market-relative figures as indicative only.
