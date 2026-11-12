# Quant Analyst

- Symbol: SNDK
- Elapsed: 62.2s

---
## SNDK — Quantitative Factor Scorecard

**Company:** Sandisk Corp. | Technology / Computer Hardware (NAND flash, SSDs) | Mkt cap ≈ $147B (engine) / $135B (profile) | Spinoff listed 2025‑02‑13 → **only 377 trading days of history**

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 12.89 · P/B 9.36 · EV/EBITDA 10.80 · P/FCF 12.82 · Fwd P/E FY27 ≈ **4.2x** | Top quintile on earnings/FCF multiples; mid on book | **Bullish** (with cycle caveat) |
| **Momentum** | 12‑1 (252d) **+3.28%**; 126d **−17.59%**; 63d **−19.36%** | Bottom half — decelerating | **Neutral → Bearish** |
| **Quality** | ROE **72.66%** · ROA 50.8% · ROIC **76.81%** · GP/Assets **0.643** · Accruals **−0.011** · F‑Score **7/9** | Top decile on raw metrics | **Bullish, but low persistence** |
| **Low Vol** | Vol **111.8%** ann. · Beta **3.87** · Max DD **−65.5%** | Bottom decile — worst-in-sector | **Strong Sell** |
| **Earnings Revision** | **−0.73%** (FY2030 EPS 297.84 vs 300.04 3m prior) | n=1 analyst → not measurable | **Neutral / unreliable** |

*Sector ranks are directional, not z-scores — a cross-sectional factor run over the peer set was not executed, so no quintile ranks are asserted.*

---

### 2. Price Statistics (252d, benchmark SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+43.88%** (t ≈ **0.46** → **not significant**) |
| Beta | **3.886** (SE ≈ 0.42, t ≈ 9.2 → significant) |
| R² | **0.25** → 75% idiosyncratic |
| Sharpe | **1.048** (t ≈ 0.84 → not significant) |
| Sortino | **1.776** |
| Annualised return / vol | 116.66% / 111.31% |
| Max drawdown | **−65.46%** |
| 126d Sharpe / Sortino | **−1.191 / −1.958** |
| Provider beta (profile) | 5.647 (vs engine 3.886 — wide disagreement) |

**Correlations (252d):** MU **0.85**, SKHY **0.81**, NVDA 0.43, SPY **0.50**.

---

### 3. Composite Quant Signal: **NEUTRAL** (negative skew; risk‑adjusted view = Sell)

The factor stack is split cleanly down the middle, and the split itself is diagnostic: **cheap + high-quality + negative momentum + extreme beta is the classic cyclical-peak value-trap signature.** Quality and value scores are being manufactured by a NAND upcycle, not by durable franchise economics — ROIC was **−16.3%, −3.9%, −12.2%** in the three prior years versus **+76.8%** in FY2026. FY2027 consensus EPS of $227 vs FY2026's $66.8 (3.4x) embeds a super-cycle continuing; at beta 3.9 that is an asymmetric payoff in the wrong direction. Value is real, but it is *peak* earnings being capitalised.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal in progress** — 252d positive (+3.3%) but 126d (−17.6%) and 63d (−19.4%) both negative and worsening. Cross-sectional momentum screens will flag this as a short/underweight regardless of the 12‑1 reading.
2. **Factor crowding — not a diversifier.** 0.85 correlation with MU and 0.81 with SKHY means SNDK is a leveraged expression of the memory complex, not a standalone name. Any MU/SKHY de-rating transmits almost 1:1.
3. **Beta 3.89 / vol 112% / 65% max drawdown.** R² of just 0.25 means market hedging is inefficient — 75% of variance is unhedgeable stock-specific risk.
4. **Statistical insignificance of the good numbers.** Alpha t‑stat ≈ 0.46 and Sharpe t‑stat ≈ 0.84 on 252 observations: neither is distinguishable from zero. Beta is the only robust estimate. With 377 days of post-spinoff history, all risk statistics carry wide error bars.
5. **Revision score is not investable** — computed on a **single analyst's FY2030** estimate (12–13 analysts cover FY2027/28). A −0.73% "downgrade" is noise.
6. **⚠ Data integrity conflict — read before use.** The OHLC feed closes at **$1,641.11** (2026‑08‑14), while the valuation engine and company profile both price SNDK at **~$948–951** (P/E 12.89 is consistent with trailing EPS ≈ $73.75 at that price). Computing 12‑1 momentum off the raw OHLC series gives roughly **+3,200%**, versus the engine's **+3.28%**; 63d off OHLC gives **+18.7%** versus the engine's **−19.36%**. The two feeds describe different price paths. I have reported engine outputs as primary (they are internally consistent with the fundamentals), but **the momentum and drawdown figures should not be treated as reliable until the price source is reconciled.**
7. **Liquidity is not a constraint** ($135–147B cap, 9–40M shares/day), but recurring 20–40M-share volume spikes coincide with the largest single-day gaps — event/positioning risk, not trading risk.
