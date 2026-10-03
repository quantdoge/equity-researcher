# Quant Analyst

- Symbol: JPM
- Elapsed: 201.2s

---
All inputs are in. Here is the complete quantitative workup on **JPM (JPMorgan Chase & Co.)**.

---

## 1. Factor Scores

Cross-sectional ranks are computed against a **money-center bank cohort of 8** (JPM, BAC, WFC, C, GS, MS, USB, PNC — rank 1 = best). Scores are 0–10, with 10 = strongest.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 5.5 | 4 / 8 | Neutral |
| **Momentum** | 7.5 | 2 / 8 | Positive |
| **Quality** | 5.0 | 4 / 8 | Mixed |
| **Low Vol** | 6.0 | ~4 / 8 | Mildly Positive |
| **Earnings Revision** | 8.0 | n/a (cohort) | Strong Positive |

**Value — Neutral.** P/E **17.11** (only 5th of 8; peers USB 12.9 / WFC 13.1 / PNC 13.6 are cheaper), P/B **2.64**, EV/EBITDA **5.17** (2nd-cheapest after USB 3.16 — attractive at the EV level), dividend yield **1.79%**. P/FCF **−6.49** is not economically meaningful for a bank (negative FCF is structural), so the composite leans on P/E, where JPM carries a mega-bank quality premium.

**Momentum — Positive.** 12–1 month return **+7.45%** (252d lookback, excluding the last 21 trading days). Cohort: BAC +7.62% > **JPM +7.45%** > USB +6.87% > PNC +4.59% > WFC +0.48% > MS −2.17% > GS −4.57% > C −6.74%.

**Quality — Mixed.** ROE **15.74% is #1 of 8** (MS 14.97, GS 13.74, C 6.69); gross profit/assets **3.79%** (3rd). But the accruals ratio is **4.63% — the worst in the cohort** (MS −2.26%, USB −0.06%, BAC 0.52%, PNC 0.44%), flagging lower earnings quality. Piotroski F-Score **4/9 "Weak"**: operating cash flow is deeply negative (−$147.8B FY25), ROA declined, leverage rose, and ROIC has *fallen* 6.85% → 5.56% over two years. ROE also dipped 16.96% → 15.74%.

**Low Vol — Mildly Positive.** Annualized vol **22.44%**, beta **0.77–0.80 vs SPY** — defensive/low-beta profile; max drawdown **−15.47%** over the window. JPM–SPY return correlation 0.45 is below the capital-markets peers (C 0.60, GS 0.66, MS 0.64), consistent with a lower-beta name.

**Earnings Revision — Strong Positive.** Consensus FY2028 EPS estimate revised **up +8.45%** in 3 months ($25.14 → **$27.26**). Consensus ladder: FY25 $20.20 → FY26 $24.77 → FY27 $25.14 → FY28 $27.26. Price targets are being raised across the Street — recent PTs: UBS $400, Goldman $418, Barclays $420, Wells Fargo $390, Morgan Stanley $370, RBC $370 (avg of 19 recent PTs ≈ **$363**, ~+6% vs spot).

---

## 2. Price Statistics (252 trading days, benchmark: SPY, RFR = 0%)

| Statistic | Value |
|---|---|
| Alpha (annualised) | **+1.35%** |
| Beta | **0.772** (regression) / 0.768 (vol tool); profile beta 0.975 |
| R² (vs SPY) | **0.20** |
| Sharpe ratio | **0.545** (Sortino methodology) / 0.731 (simple approx) |
| Sortino ratio | **0.773** |
| Annualised return | +12.29% |
| Annualised volatility | 22.4–22.5% |
| Max drawdown | **−15.47%** |

Note: the two Sharpe figures differ because of conventions (one uses downside-only variance adjustments implicitly); I report Sortino (0.77) as the more informative of the two since JPM's returns are positively skewed in the window. R² of 0.20 means ~80% of JPM's variance is idiosyncratic relative to the broad market — but see the crowding flag below.

---

## 3. Composite Quant Signal: **BUY**

| Factor | Weighted read |
|---|---|
| Earnings revisions +8.45%, broad PT raises | ++ |
| Momentum +7.45%, 2nd in cohort | + |
| Low beta / decent Sortino / positive alpha | + |
| Valuation mid-pack (P/E 17.1) | 0 |
| Accruals 4.6% (worst in cohort), Piotroski 4/9, ROIC declining | − |

The story is a high-quality-franchise re-rate: analysts are systematically upgrading estimates and targets while the stock is only mid-pack on valuation. That earns a **Buy**, not Strong Buy — the quality drag (accruals, declining ROIC, negative operating cash flow) and the fact that the stock already caught a large re-rate tell against conviction sizing at these levels.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** The 12–1 metric (+7.45%) hides a fast recent run: JPM rallied ~+26% from mid-March 2026 to a $365 peak (Aug 12), then faded **−6.1%** to $343. The last-21-days exclusion is doing heavy lifting; short-term trend has rolled over. If the 12–1 momentum rolls negative on the next update, the buy case weakens fast.
2. **Factor crowding — HIGH (sector-wide).** Pairwise return correlations with the bank cohort are high: BAC **0.80**, WFC 0.74, C 0.70, USB 0.69, PNC 0.67, GS 0.63. JPM is not an idiosyncratic alpha story — it is a *bank-cohort* story. A sector drawdown takes JPM with it, despite the low market beta.
3. **Earnings-quality flags.** Accruals ratio 4.63% (highest of 8 peers), Piotroski 4/9 "weak", negative operating cash flow (−$147.8B FY25), ROIC 6.85% → 5.56% (2-yr slide). The reported ROE/#1 rank is partly offset by these — treat income quality with suspicion.
4. **Sample-size caveats.** The FY2028 EPS estimate (the one revised +8.45%) rests on only **7 analysts** with a wide band ($25.42–$30.03); revenue estimate on just 5. The 2025 estimate has only 4. Revision-momentum and estimate statistics for outer years are thin — don't over-weight the +8.4% FY28 number.
5. **Low liquidity — NOT a flag.** $919B market cap, ~2.79B shares, deep two-sided flow. Liquidity is a non-issue; the real risks are the three above.

*Data as of 2026-09-25 close ($343.06), FY2025 financials, 252-trading-day price window.*
