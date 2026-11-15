# Quant Analyst

- Symbol: ALNY
- Elapsed: 55.7s

---
## ALNY — Quantitative Factor Report
**Alnylam Pharmaceuticals | Healthcare / Biotechnology | Price $165.04 (13-Nov-2026) | Mkt cap $22.1B**

> **Data integrity note first — this matters.** Three tool outputs conflict with the raw price series. I resolved them against the OHLCV data and cross-checked with independently posted price targets, and I report verified figures below:
> - `calculate_momentum_score` returned **+7.27%**. Verified from raw closes: **−63.6%**. The tool is wrong.
> - `calculate_price_volatility` max drawdown **55.3%**. Verified peak-to-trough: **−69.6%** ($491.22 → $149.18). Tool understates.
> - Sortino (−1.19) is *less* negative than Sharpe (−1.26), which is mathematically impossible (downside deviation ≤ total SD). Both are unreliable in level; treat as "deeply negative, ≈ −1.1 to −1.3."

---

### 1. Factor Scores Table

Sector ranks are within a 5-name comparable set (ALNY, LLY, MRK, GILD, AMGN); **NVO excluded — its feed data is broken** (P/E 1.81, EV/EBITDA 1.84 for Novo Nordisk is not credible; likely ADR/currency unit mismatch). Rank 1 = best.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 70.8 · P/B 28.2 · EV/EBITDA 32.6 · P/FCF 47.8 · no div | **4 / 5** (only LLY dearer) | **Negative — expensive** |
| **Momentum** | 12−1 ≈ **−47%**; 1-yr **−63.6%** | **5 / 5** (worst) | **Strong Negative** |
| **Quality** | ROIC 24.3% · ROE 39.8% · ROA 6.3% · GP/Assets 0.61 · Accruals **−4.2%** · F-Score 7/9 | **3 / 5** | **Positive** (ROA is the drag) |
| **Low Vol** | Vol **58.8%** ann. · Beta 0.543 · Max DD −69.6% | **5 / 5** (highest vol) | **Strong Negative** |
| **Earnings Revision** | +16.45% vs 3-mo prior, but on **FY2030** consensus (n=7) | n/a | **Weak Positive — low confidence** |

**Peer detail (why the ranks fall where they do):**

| | P/E | P/B | EV/EBITDA | P/FCF | ROIC | ROA | Vol | 12-1 Mom |
|---|---|---|---|---|---|---|---|---|
| **ALNY** | 70.8 | 28.2 | 32.6 | 47.8 | 24.3% | 6.3% | **58.8%** | **−47%** |
| LLY | 62.9 | 48.9 | 42.0 | 144.5 | 43.0% | 18.4% | — | — |
| MRK | 20.3 | 7.0 | 14.4 | 30.0 | 22.8% | 13.3% | — | +14.4% |
| GILD | 24.8 | 9.3 | 16.7 | 22.3 | 24.6% | 14.4% | 27.6% | +20.0% |
| AMGN | 32.7 | 29.2 | 17.6 | 31.2 | 16.9% | 8.5% | 28.2% | +7.5% |

**Quality caveat (important):** ALNY's ROE of 39.8% is not a quality signal. Book value is $5.86/share against a $165 price (P/B 28.2), so the equity denominator is near-zero and ROE history is pure noise: **−414.6%, +199.5%, +714.9%, +39.8%** over four years. Use ROIC (24.3%) and ROA (6.3%). **ROA ranks dead last of five** — the strong ROIC is flattered by a low capital base, not superior asset productivity.

**Forward value is the one genuinely constructive number** — but the near-term multiple is a trap:
- FY2026E EPS $18.42 → 8.96x. **Do not use this.** Implied net income $3.01B on $5.44B revenue = **55% net margin**, versus FY2025 actual $313.7M on $3.75B (8.4%). This is a one-time item (settlement/milestone), not earnings power.
- FY2027E $8.96 → **18.4x**; FY2028E $11.19 → **14.8x**. On that basis ALNY screens *cheaper* than MRK (20.3x trailing).
- But the estimate curve is non-monotonic ($18.42 → $8.96 → $11.19) and dispersion is enormous: FY2028E range **$5.24–$27.46 (5.2x spread)**, FY2026E range $8.12–$22.60. This is not a consensus; it is a scatter plot.

**Revision score caveat:** the +16.45% revision is measured on **FY2030 EPS with only 7 analysts** — a four-year-distant, thin-sample estimate. It is the weakest possible form of revision signal. The higher-frequency, better-evidenced revision data points the other way: on 30-Oct-2026 UBS, BMO, Wells Fargo/BofA, RBC and Raymond James all **cut price targets**, and Stifel **downgraded to Hold** (PT $225). I would not underwrite a buy case on the revision factor.

---

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (ann., 252d, vs SPY) | **−77.3%** |
| Beta (252d, vs SPY) | **0.546** |
| R² vs SPY | **0.0175** — only **1.75%** of variance is market |
| Annualised volatility | **58.8%** |
| Sharpe (0% rf) | **−1.26** (tool) / −1.08 (my calc from verified return) |
| Sortino (0% rf) | **−1.19** ⚠️ inconsistent — see note above |
| Max drawdown | **−69.6%** verified ($491.22 on 20-Oct-25 → $149.18 on 10-Nov-26); tool said −55.3% |
| 1-yr total return | **−63.6%** ($453.97 → $165.04) |
| Last 3 sessions | **+10.6%** off the low ($149.18 → $165.04) |

**The beta of 0.546 is a statistical artifact and should not be used for risk sizing.** With R² = 0.0175, beta explains essentially nothing. Total volatility (58.8%) is **2.1x** the peer group (GILD 27.6%, AMGN 28.2%). The risk here is 98% idiosyncratic, and it is event-driven, not gradual:

- **09-Jul-26:** opened $378.49, closed $312.79 — intraday reversal on 5.9M shares.
- **30-Jul-26: −28.3%** ($286.62 → $205.48, 9.8M shares) — Q2 earnings "one-two punch": Amvuttra/Onpattro sales weakness and slowing new-prescription growth.
- **29-Oct-26: −25.1%** ($232.40 → $174.00, 11.8M shares) — Q3 results with a **cut to 2026 TTR franchise sales expectations**; a securities-fraud investigation tied to that cut is now an overhang.

Alpha of −77% against beta 0.55 means the stock lost money *while the market was up*. That is not a valuation de-rating that mean-reverts on a schedule; it is a franchise-expectation reset.

---

### 3. Composite Quant Signal: **SELL**

Not Strong Sell, for three specific reasons: (1) quality is genuinely above-median on ROIC/accruals/F-Score, (2) the stock now trades at ~15–18x FY27/28E versus 20x for MRK, and (3) sell-side targets posted 30-Oct cluster at **$225–$350** (median ≈ $300, ~+82% vs spot). Momentum, volatility and value are all bottom-of-peer-group, and momentum carries the largest empirical weight — hence Sell rather than Neutral.

**Honest limitation:** a five-factor model has very limited predictive power on a company whose returns are driven by discrete clinical/commercial disclosure events. The −63.6% drawdown is not a factor signature; it is two earnings disappointments. Factor scores describe the damage, they do not forecast the next catalyst.

---

### 4. Key Quant Risk Flags

1. **Negative-momentum persistence.** 12−1 of ≈ −47% and 1-yr −63.6% with the stock making new lows as recently as 10-Nov-26. Historically the worst decile for forward 12-month returns. The +10.6% three-day bounce is not yet a reversal — it is within one standard deviation of noise at 58.8% vol.

2. **Binary event risk dominates the model.** R² 0.0175 means diversification logic fails. Three separate >18% single-day moves in five months. Position sizing must be vol-targeted off 58.8% *realised* vol, not the 0.546 beta.

3. **Estimate dispersion is extreme.** FY2028E EPS spans $5.24–$27.46. Any P/E-based valuation, forward or trailing, is not statistically meaningful. FY2026E is contaminated by a one-time gain (55% implied net margin).

4. **ROE is unusable; equity base is minimal.** BVPS $5.86, P/B 28.2. The ROE series (−415% to +715%) is a denominator artifact. A screen that ranks ALNY highly on ROE is being fooled.

5. **Not a liquidity or crowding problem — the reverse.** ADV ~1.5–2M shares (~$250–330M), spiking to 7–12M on event days. The stock has been *abandoned* rather than crowded, which is why the gap between spot ($165) and median target (~$300) is so wide. That gap is a disagreement about the TTR franchise, not a mispricing a factor model can arbitrage.

6. **Governance/legal overhang.** A securities-fraud investigation tied to the 2026 TTR guidance cut is unresolved. This is not captured by any factor in this framework and is a legitimate reason to discount the analyst-target upside.
