# Quant Analyst

- Symbol: ICON
- Elapsed: 11.3s

---
I have all requested metrics. One critical finding up front before the tables: **"ICON" resolves to Icon Energy Corp.** — a Greek dry-bulk shipping microcap (IPO July 2024, two vessels, ~$0.95/share, sub-$2M market cap) — **not ICON plc, the clinical-research CRO** that most "ICON" queries intend. All figures below are for the shipping microcap, and the data-quality caveats dominate any interpretation.

---

## 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| **Value** | P/E n/a (loss), P/B 0.05, EV/EBITDA 10.4, P/FCF n/a (neg), DY 16.3% | n/a — microcap outlier | **Neutral/Neg** — optically cheap on P/B but losses make it uninterpretable; EV/EBITDA is not cheap; 16% yield is a distress flag, not income |
| **Momentum (12‑1)** | +0.01% | Bottom decile | **Neutral** — dead flat, no trend |
| **Quality** | ROE −19.6%, GP/Assets 0.043, Accruals −8.6%, Piotroski 5/9 | Low | **Sell** — negative ROE, weak asset productivity; F-score "moderate" only |
| **Low Vol** | 95% annualized vol, β 1.34–5.45, 66% max DD | Worst in class | **Strong Sell** — this is a *high*-vol name; anti-factor |
| **Earnings Revision** | +16.3% (2027 FY EPS −1.41 → −1.18) | n/a | **Weak Buy** — direction up, but still a loss; low-confidence, far-dated |

## 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| Annualized return | −42.1% | 252d |
| Alpha (annualized) | **−96.3%** | ⚠️ **Not credible** — R² = 0.034 |
| Beta (vs SPY) | 1.34 (calc) / 5.45 (profile) | ⚠️ Sources disagree |
| R² | 0.034 | **3% of variance explained** — regression is noise |
| Sharpe | −0.44 (calc) / −0.75 (vol tool) | Negative, source-dependent |
| Sortino | −0.77 | Heavy downside dispersion |
| Annualized vol | 95–96% | Extreme |
| Max drawdown | −66.1% | |

## 3. Composite Quant Signal: **SELL / AVOID** (low confidence)

The single unambiguous, statistically defensible reading: **exceptionally high volatility with negative risk-adjusted returns**. Everything else — value, momentum, alpha — is either noise or distorted by negative earnings and a sub-1-year history. No factor screen endorses this name; two of five (Quality, Low-Vol) are outright negative.

## 4. Key Quant Risk Flags

- **⚠️ Sample-size invalidity:** IPO 2024‑07‑12 → ~1 year of history. A 252‑day 12‑1 momentum window is at the edge of feasibility; the alpha/beta and Sharpe figures are **not statistically significant**. Do not act on the −96% alpha — R² 0.034 says the model explains nothing.
- **⚠️ Liquidity/microcap:** Market cap ~$0.4–1.2M (sources conflict), price $0.95. Extremely thin, wide spreads — factor signals are unexecutable at size and prone to price-stale artifacts.
- **⚠️ Distress decomposition:** 16% dividend yield + P/B 0.05 + negative ROE + EV/EBITDA 10.4 is the classic signature of value-trap/distress pricing, not cheapness.
- **Beta instability:** 1.34 vs 5.45 across sources — no reliable market-sensitivity estimate.
- **Factor crowding:** N/A — the stock is too small to appear in institutional factor baskets.

**Bottom line:** On the numbers, ICON fails on quality, fails hard on volatility, and generates negative risk-adjusted return. The value optics are a mirage created by losses. If your mandate actually intended **ICON plc (ICLR)**, re-run on the correct ticker — this analysis does not apply to it.

*Note: I did not spend further budget on peer/sector factor scores; within "Industrials / Marine Shipping" this is a 2-vessel microcap whose rank would be dominated by size/liquidity artifacts rather than signal.*
