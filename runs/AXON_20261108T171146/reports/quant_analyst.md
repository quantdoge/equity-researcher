# Quant Analyst

- Symbol: AXON
- Elapsed: 65.4s

---
# AXON (Axon Enterprise) — Quantitative Factor Report

**Composite Quant Signal: SELL / Underweight** (high-duration growth, broken momentum, extreme valuation, negative ROIC)

⚠️ **Data integrity warning first.** Two internal contradictions must be resolved before acting:
1. `get_price_history` shows a **2025-12-31 close of $567.93**; the profile/valuation feed reports **$313.00**. The $313 figure appears stale. At $567.93, P/E is 376x GAAP, not 207x.
2. Diluted shares of **100.0M** in the valuation tool are inconsistent — FY25 net income $124.9M ÷ diluted EPS $1.51 implies **~82.7M** shares. Reported market cap ($25.4B) is ~44% too low. **Multiples below are recomputed at $567.93 × 80.4M basic shares = $45.7B market cap.**

---

## 1. Factor Scores

| Factor | Score | Sector Rank (of 4 A&D) | Signal |
|---|---|---|---|
| **Value** | **1 / 5** | **4th (worst)** | Strong negative |
| **Momentum** | **2 / 5** | **4th** | Negative |
| **Quality** | **2 / 5** | **3rd** | Weak / mixed |
| **Low Vol** | **1 / 5** | **4th** | Strong negative |
| **Earnings Revision** | **3 / 5** | n/a | Unverifiable (see note) |

### Value — Bottom decile
| Metric | AXON @ $567.93 | @ $313 (stale) | LMT | RTX | GD |
|---|---|---|---|---|---|
| P/E (GAAP FY25) | **376x** | 207x | 26.4x | 38.2x | 22.9x |
| P/E (2026E $7.68) | **74x** | — | — | — | — |
| P/E (2027E $10.57) | **54x** | — | — | — | — |
| EV/EBITDA (trailing $196M) | **~234x** | 160x | 17.1x | 19.4x | 16.5x |
| EV/EBITDA (2026E $1.02B) | **~45x** | — | — | — | — |
| P/FCF (FCF $75M) | **608x** | 417x | 19.0x | 34.5x | 24.5x |
| P/B (BVPS $32.43) | **17.5x** | 9.7x | — | — | — |

FCF yield **0.16%**; SBC-adjusted FCF yield **−1.2%**. Peer set trades at 16–19x EV/EBITDA — AXON is **~2.5x the group on forward EBITDA and ~12x on trailing**. No value support at any horizon.

### Momentum — Negative, and the tape is broken
- Tool: 12-1 momentum **−19.5%** (signal: negative). My OHLCV recompute (12/31/24 $594.32 → 12/02/25 $537.75): **−9.5%**. Direction agrees; magnitude disputed.
- **Calendar 2025 total return: −4.4%** ($594.32 → $567.93).
- Path: $496.65 (Feb 25) → **$870.97 peak (Aug 7), +75%** → **$519.61 (Nov 20), −40%**. Current price is **35% below the August peak**.
- Peers are also negative (LMT −10.7%, RTX −13.0%, GD −12.9%) — this is a **sector-wide de-rating, not stock-specific**, but AXON ranks last even so.
- Short-term: **+5.6% over the last month** (537.75 → 567.93) = tentative stabilization.

### Quality — Superficially improving, structurally weak
| Metric | FY25 | FY24 | FY23 | FY22 |
|---|---|---|---|---|
| ROE | **3.85%** | 16.2% | 10.9% | 11.6% |
| ROIC (approx) | **−1.2%** | 1.6% | 6.9% | 4.7% |
| Gross profit / assets | **23.7%** | — | — | — |
| Accruals ratio | **−1.2%** | — | — | — |
| Piotroski F-Score | **5 / 9** | — | — | — |

Positives: gross profit/assets of **23.7%** beats LMT (12.7%) and GD (13.9%) — best in the subset on the Novy-Marx measure; negative accruals (−1.2%) = clean earnings. Negatives: **ROIC of −1.2% is below any reasonable WACC**, GAAP operating income **−$62M** (op margin −2.2%), and F-Score fails on ROA trend, leverage, dilution, and asset turnover. ROE ranks last vs GD 16.4% and RTX 10.0%.

**SBC is the core problem:** $634M in FY25 = **23% of revenue**, up 66% y/y, and **8.5x free cash flow** ($75M). SG&A rose 39% to $1.03B. The "earnings" here are largely a stock-compensation-funded growth investment.

### Low Volatility — Worst in class
Annualized vol **69.6%**, beta **1.55**, max drawdown **−51.5%** (tool) vs **−40.3%** on my close-basis recompute (peak $870.97 → $519.61). Either reading is disqualifying for a low-vol factor.

### Earnings Revision — ⚠️ **Metric is invalid as reported**
The tool reports **+30.57% revision** by comparing the **2028E** estimate ($13.796) against the **2027E** estimate ($10.566). That is inter-period growth, *not* a 3-month revision of the same forward period. **Discard the "upgrade" signal.**

Estimate ladder (what I can actually verify — one snapshot, no revision history available):
| Period | EPS | Analysts | Implied growth |
|---|---|---|---|
| 2025A/cons. | $6.31 | 13 | — |
| 2026E | $7.68 | 10 | +21.7% |
| 2027E | $10.57 | 12 | +37.6% |
| 2028E | $13.80 | **4** | +30.6% |

FY25 revenue $2.780B vs $2.738B consensus = **+1.5% beat**. Growth is intact; 2028E dispersion is wide ($8.80–$17.08, ±30%) on only 4 analysts. **Gap: true revision direction unavailable — no upward-revision confirmation.**

---

## 2. Price Statistics

| Statistic | Value | Comment |
|---|---|---|
| Annualized return (1Y) | **−19.59%** (tool) / −4.4% (2025 calendar, OHLCV) | Conflict flagged |
| Annualized volatility | **69.4–69.6%** | ~4.4x market |
| Beta vs SPY | **1.562** (OLS) / 1.554 (vol tool) / 1.468 (profile, 5Y) | Range 1.47–1.56 |
| **Alpha (annualized)** | **−47.67%** | **Not statistically significant** |
| R² | **0.1013** | **90% idiosyncratic** |
| Sharpe ratio | **−0.282** | Negative |
| Sortino ratio | **−0.408** | Sortino worse than Sharpe → fat left tail |
| Max drawdown | **−51.53%** (tool) / −40.3% (OHLCV closes) | |

**Statistical significance caveat:** with R² = 0.10, residual vol ≈ 66% annualized, so the standard error on annualized alpha is ≈ 66% and the implied **t-stat is ≈ −0.7**. The −47.7% alpha is **statistically indistinguishable from zero**. Beta 1.55 is likewise estimated with low precision — this stock cannot be reliably hedged with index beta at this R².

---

## 3. Composite Quant Signal: **SELL**

| Factor | Weight | Score (1-5) | Contribution |
|---|---|---|---|
| Value | 25% | 1 | −1.00 |
| Momentum | 25% | 2 | −0.50 |
| Quality | 25% | 2 | −0.50 |
| Low Vol | 15% | 1 | −0.60 |
| Revision | 10% | 3 | 0.00 |
| **Weighted** | | | **≈ 1.7 / 5** |

**Rationale:** valuation offers zero cushion (74x 2026E EPS, 45x forward EBITDA, 0.16% FCF yield) while momentum has broken (−40% drawdown), quality is cash-negative after SBC, and volatility is the highest in the peer group. The bull case is entirely a duration bet: if the 2026–2028 ramp delivers, the multiple compresses 74x → 54x → 41x, which is the only path to a positive expected return.

**Quant verdict: Sell / Underweight.** Not a "broken business" (revenue +33% y/y, gross margin 59.7%, negative accruals) — a **broken multiple with a broken tape**.

---

## 4. Key Quant Risk Flags

1. **Data-integrity risk (highest priority).** Price conflict ($313 vs $567.93), share count off by ~20%, and a revision metric that compares mismatched periods. **Every multiple in this report could be wrong by a factor of ~1.8.** Re-verify the quote and share count before sizing any position.
2. **Momentum reversal / falling-knife risk.** −40% from the August peak; the **Nov 5 gap (−9.4% on 4.9M shares, ~8x ADV)** signals an unresolved information shock (note: FY25 GAAP operating income turned negative with a $292M SG&A jump). One month of +5.6% is not a confirmed base.
3. **Earnings quality / dilution.** SBC of $634M > FCF of $75M. SBC-adjusted FCF **−$559M**. Working capital drag **−$482M**. Piotroski fails on dilution and leverage. Structural 6%+/yr shareholder dilution with buybacks at zero.
4. **Volatility & left-tail.** 69.6% vol, beta 1.55, Sortino (−0.41) below Sharpe (−0.28) — losses are larger and more frequent than the vol suggests. Equal-risk sizing requires roughly **one-third** of a market-vol position.
5. **Factor crowding / de-crowding.** A consensus long-duration growth holding that has just lost its momentum score. Systematic momentum-driven de-crowding is a live, self-reinforcing risk not captured by fundamentals.
6. **Unhedgeable alpha.** R² = 0.10 means index beta hedging explains almost nothing; alpha's t-stat ≈ −0.7 is insignificant. Any view here is an outright single-stock bet, not a spread.
7. **Small-sample estimates.** 2028E EPS rests on **4 analysts** with a $8.80–$17.08 range. 2027E: 12 analysts. Treat the long-dated growth ramp as low-confidence.

### Gaps acknowledged
- No true estimate-revision time series (single snapshot only) — the revision factor is **unscored** rather than scored 3.
- No peer-level data for GEV/ETN/PH/CAT; sector ranks use a 4-name A&D subset (AXON, LMT, RTX, GD).
- Balance sheet not retrieved, so net debt and EV are estimated (net debt ≈ +$0.2B, minor).
- Vol/Sharpe/Sortino/alpha/drawdown are tool outputs on a price series that conflicts with the OHLCV feed; my independent recomputes are shown alongside (momentum −9.5%, max DD −40.3%, calendar return −4.4%).
