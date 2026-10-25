# Quant Analyst

- Symbol: ZTS
- Elapsed: 48.0s

---
# ZTS — Quantitative Factor Report
**Zoetis Inc.** | Healthcare – Animal Health (peer group: large-cap Drug Manufacturers) | Price $79.38 | Mkt cap $35.2B | EV $42.4B

---

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 5.0 / 5 | **1 of 7** | Very Bullish |
| **Momentum** | 1.0 / 5 | **7 of 7** | Very Bearish |
| **Quality** | 4.5 / 5 | **2 of 7** | Bullish |
| **Low Vol** | 1.0 / 5 | **7 of 7** | Very Bearish |
| **Earnings Revision** | 3.0 / 5 | 1 of 3 (thin) | Mildly Bullish (low confidence) |

**Value (rank 1/7)** — cheapest name in the large-cap pharma peer set on every metric:

| | ZTS | MRK | GILD | JNJ | AMGN | ABBV | LLY |
|---|---|---|---|---|---|---|---|
| P/E | **13.2** | 20.1 | 23.0 | 23.2 | 30.4 | 120.4 | 54.8 |
| EV/EBITDA | **10.4** | 14.2 | 15.6 | 15.8 | 16.6 | 32.3 | 36.7 |
| P/FCF | **15.4** | 29.6 | 20.7 | 31.5 | 28.9 | 28.4 | 125.8 |

FCF yield 6.5%, dividend yield 2.67%, P/B 10.6. ZTS trades at a ~35% EV/EBITDA discount to the peer median (15.8x).

**Quality (rank 2/7)** — ROE 80.3% (distorted: equity of only $3.33B), gross-profit/assets 0.431 (2nd only to LLY 0.481), accruals ratio −0.0149 (negative accruals = conservative accounting, better than LLY +0.034, JNJ +0.011, MRK +0.013). Piotroski F-Score **5/9** (moderate) — fails on leverage (F5), equity change (F6), asset turnover (F9).

**Momentum (rank 7/7)** — 12-1 momentum computed directly from the price series: **−49.5%** (2025-09-16 close $144.69 → 2026-09-16 close $73.00). 12-month total return −43.5%; YTD 2026 −35.9%; −59.6% from the Feb-2025 close peak ($171.22) to the 1-Oct-2026 trough ($69.10). Peers: MRK +18.1%, ABBV +6.4%, JNJ +4.7%, LLY −5.1%. ⚠️ Note: the momentum tool returned −4.24%, which is irreconcilable with the raw price file over any reasonable window — I treat it as a feed artifact and use the price-derived figure.

**Low Vol (rank 7/7)** — 38.8% annualised vol, highest of the seven; max drawdown 46.7% (tool, 252d) vs peer range 11–23%. Sole mitigant: low beta (0.389 252d / 0.615 504d; profile 0.74).

**Earnings Revision (weak positive)** — consensus 2030 EPS $9.06 vs $8.12 three months prior, **+11.5%**. ⚠️ **Statistically fragile: n = 2 analysts** on that period. More reliable front-year data cuts the other way: 2026E revenue $9.25B (−2.0% vs 2025E $9.44B) and 2026E EPS $6.21 (−2.1% vs 2025E $6.34), i.e. a flat-to-shrinking earnings base. The multiple compression is *not* estimate-driven — it is pure de-rating.

---

## 2. Price Statistics

| Metric | 252d | 504d |
|---|---|---|
| Annualised return | — | **−42.16%** |
| Annualised volatility | 38.79% | 34.06% |
| Beta vs SPY | 0.389 | 0.615 |
| **Alpha (annualised)** | — | **−53.09%** |
| R² vs SPY | — | **0.0486** |
| **Sharpe** | **−1.326** | **−1.238** |
| **Sortino** | — | **−1.273** |
| Max drawdown | 46.69% (tool) / −59.6% (close-to-close, 2025 peak) | — |

**Critical caveat on alpha:** R² of 0.049 means SPY explains under 5% of ZTS return variance. The −53% alpha is a massive residual return, but with that R² the alpha estimate is extremely imprecise — treat it as "unexplained idiosyncratic collapse," not a reliable market-adjusted skill measure.

**Correlations (252d):** SPY 0.13, MRK 0.27, LLY 0.19, JNJ 0.18. ZTS is effectively **decorrelated** from both the market and its sector — this drawdown is company-specific, not a healthcare or macro event.

**Event signature (2 gap-downs drove the decline):**
- 2025-11-04: −13.8% on 11.9M shares (~4x normal)
- 2026-05-07: **−21.5%** on 29.9M shares (~10x normal)
Both are single-day repricings — the risk here is event/guidance risk, not gradual beta drift.

---

## 3. Composite Quant Signal: **NEUTRAL**

Equal-weighted factor composite **2.9 / 5.0**. Momentum-tilted weights (20/20/30/15/15) give **2.8 / 5.0**.

The factor spread is the story: **Value 5.0 and Quality 4.5 against Momentum 1.0 and Low-Vol 1.0**. This is a textbook *fallen-angel / potential value-trap* signature — statistically cheap, fundamentally sound on accounting quality, but in an unbroken downtrend with the worst risk-adjusted profile in its peer group. Sharpe −1.24 with a −43% annualised return means there is no compensation for the volatility being borne. I do not upgrade to Buy on cheapness alone: in this data set, cheap + collapsing momentum + worst-in-class drawdown has not been rewarded.

**What would move me to Buy:** momentum score turning positive (price reclaiming ~$85–90), a front-year (2026/2027) EPS revision series that is genuinely upward — not a 2030 figure backed by 2 analysts — and vol compressing below ~30%.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / trend-break risk (severe).** −49.5% 12-1 momentum, bottom of the 7-name peer group, with the most recent quarter still making lower lows ($79.38 vs $69.10 October trough). No evidence of a base yet.
2. **Event/gap risk, not beta risk.** Two single-day repricings of −13.8% and −21.5% account for most of the drawdown. Low beta (0.39) gives false comfort — the risk is idiosyncratic and unhedgeable by index exposure (SPY correlation 0.13).
3. **Balance-sheet deterioration + buyback-funded distribution.** Total debt rose $6.74B → $9.49B (+41%) in FY25 while equity fell $4.77B → $3.33B. Dividends ($889M) + buybacks ($3,235M) = $4.12B against FCF of $2.28B — a **$1.8B shortfall funded with debt**. Liabilities/equity 3.64x; net debt $7.18B. Piotroski F5 and F6 both fail on this. The 80% ROE is an artifact of a shrinking equity base, not superior profitability — do not read it at face value.
4. **Value-trap / estimate-quality risk.** The optically cheap multiple sits on estimates showing 2026 revenue and EPS *contraction*. Cheap on a shrinking base is not the same as cheap on a growing one.
5. **Small-sample inference.** Earnings-revision signal rests on n = 2 analysts (2030 period); alpha estimate has R² = 0.049. Neither meets a reasonable significance bar. Far-dated 2029–2030 estimates (n = 2–3) should be disregarded.
6. **Liquidity is adequate** — ~4–8M shares/day, $35B cap; no crowding issue. Sector-positioning crowding is low (correlations 0.18–0.27), so a de-crowding unwind is *not* a plausible driver of further weakness — the selling is thesis-driven.
7. **Data caveat:** sector peer-ranking uses the 6 largest Healthcare comparables by market cap; the Momentum tool output for ZTS conflicted with the raw price file and was overridden.
