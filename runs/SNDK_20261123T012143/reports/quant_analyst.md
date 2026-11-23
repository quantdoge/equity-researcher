# Quant Analyst

- Symbol: SNDK
- Elapsed: 43.5s

---
## SNDK (SanDisk) — Quantitative Factor Report

**Data-integrity caveat up front:** the raw price-history endpoint returns a series on a different scale (~$5.6 → $218) than the analytics engine's quoted price ($79.24), and EPS estimates ($28–37) are quoted on yet a third scale vs. price. I therefore rely on the **internally self-consistent analytics tools** (valuation ratios, factor scores, risk stats) for all numbers, use the price path only for *shape*, and flag forward-multiple math as unreliable.

---

### 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank* | Signal |
|--------|-------------|--------------|--------|
| **Value** | P/E 8.6 · EV/EBITDA 7.1 · P/FCF 8.6 · P/B 6.2 | **2 of 4** (memory peers) | **Strongly attractive** — top-quartile |
| **Momentum** (12-1) | **−18.98%** | **2 of 4** (all negative) | **Negative** — bottom quintile vs market |
| **Quality** | ROE 72.7% · GP/Assets 0.643 · Accruals −0.011 | **1–2 of 4** | **High** (Novy-Marx/serial quality top bucket) |
| **Low Vol** | Vol 112% · β 4.01 · MaxDD 72.9% | **4 of 4 (worst)** | **Very poor** — bottom decile |
| **Earnings Revision** | −1.07% (fwd 2030, **n=1 analyst**) | n/a | **Mild downgrade — statistically meaningless** |

\*Sector rank = NAND/storage peer set (SNDK, MU, WDC, STX). The API "Technology" sector list is dominated by mega-cap software and is not a valid comparison group.

**Peer valuation spread (lower = cheaper):**

| | P/E | EV/EBITDA | P/FCF | 12-1 Mom |
|---|---|---|---|---|
| **SNDK** | **8.6** | **7.1** | **8.6** | −19.0% |
| MU | 8.0 | 5.9 | 11.5 | −7.6% |
| WDC | 10.8 | 19.9 | 28.5 | −29.5% |
| STX | 32.9 | 25.3 | 33.7 | −31.5% |

SNDK screens as the **second-cheapest on earnings/EBITDA and the cheapest on FCF** among memory/storage names, while carrying the **highest quality and highest beta** of the group. Piotroski **F-Score 7/9** (moderate‑strong; dinged on leverage and share dilution).

**Quality is cyclically inflated, not structural.** ROIC history: **−16.3% (FY23) → −3.9% (FY24) → −12.2% (FY25) → +76.8% (FY26)**. A 76.8% ROIC and 72.7% ROE are textbook NAND-cycle peak earnings. The value factor is being computed on **peak-cycle "E"** — this is the classic value-trap geometry in memory.

---

### 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+57.4%** |
| Beta (vs SPY) | **4.04** (profile β 5.65) |
| R² | **0.297** — only 30% of variance is market |
| Annualised return | +62.5% |
| Annualised volatility | **113.2%** |
| **Sharpe** | **0.55** |
| **Sortino** | **0.93** |
| Max drawdown | **−72.9%** |

**Statistical significance — the honest read:**
- **Alpha is NOT significant.** Residual (idiosyncratic) vol after removing market ≈ 95% annualised. On ~1 year of data, SE of annualised alpha ≈ 95% → **t-stat ≈ 0.6**. The "+57% alpha" is a leveraged, one-directional memory-sector rally, not demonstrable manager/skill alpha.
- **Sharpe of 0.55 is not distinguishable from zero.** SE of Sharpe on a 1-year sample ≈ 1.0. Sortino 0.93 (higher downside dispersion than the headline suggests) confirms fat left-tail.
- **R² 0.30 with β 4.0** means SNDK is a high-octane sector bet whose real driver is NAND pricing, not the equity market.

**Correlation structure (crowding flag):**

| | SNDK | MU | WDC | STX | SPY |
|---|---|---|---|---|---|
| SNDK | 1.00 | **0.85** | 0.75 | 0.75 | 0.54 |

SNDK is **0.85-correlated with Micron** — economically it is a **levered MU/NAND factor certificate**, not a diversifier.

---

### 3. Composite Quant Signal: **BUY — HIGH RISK (speculative, small sizing)**

Top-quintile **Value + Quality** simultaneously is rare and genuinely attractive on trailing numbers. But the signal is *not* a clean quant buy: it is offset by (a) negative momentum, (b) the worst low-volatility profile in the peer group, (c) peak-cycle earnings that mechanically mean-revert, and (d) a statistically insignificant alpha/Sharpe. Net: an attractive **cyclical value bet**, not a risk-adjusted compounder. **Neutral for a long-only core portfolio; Buy only for a factor-aware investor explicitly taking NAND-cycle beta.**

---

### 4. Key Quant Risk Flags

1. **Peak-cycle earnings / value-trap risk (highest priority).** ROIC swung from −12% to +77% in one year. P/E 8.6 is cheap only if FY26 "E" holds; a NAND downcycle resets earnings negative, as in FY23–FY25. Trailing value factor is **circularly inflated by peak EPS.**
2. **Extreme beta & tail risk.** β 4.0, 113% annualised vol, **73% max drawdown** on record. Position sizing must reflect a ~4x market-risk load; a 25% market drawdown historically maps to a >70% SNDK drawdown.
3. **Factor crowding / concentration.** 0.85 correlation with MU, 0.75 with WDC/STX. Any "value in semis" or "memory" factor book is effectively one trade; correlated drawdown risk is severe. Not a diversifier.
4. **Momentum reversal risk — currently in drawdown.** 12-1 momentum −19%, and the recent price path shows a sharp pullback off the June peak. Entering a high-beta name against negative momentum raises near-term timing risk.
5. **Thin/unreliable estimate data.** Revision score rests on **n=1 analyst** for the forward period; peer forward estimates are on a mismatched scale — treat the −1.07% revision and any forward-multiple derived from it as **non-informative**. Sample size insufficient for significance.
6. **One-year sample.** All risk stats (α, Sharpe, Sortino, β, DD) derive from ~252 observations — the beta and drawdown are robust in direction but the alpha/Sharpe levels are **statistically fragile**.
7. **Liquidity** is adequate (mega-cap, ~$90–98B mkt cap; heavy volume) — not a liquidity flag, but note the market-cap figures across endpoints also disagree ($90.2B vs $98.3B), reinforcing the data-quality warning.
