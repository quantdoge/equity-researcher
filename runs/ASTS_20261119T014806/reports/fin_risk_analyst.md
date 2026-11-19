# Fin Risk Analyst

- Symbol: ASTS
- Elapsed: 57.7s

---
I have enough to complete the assessment. Writing the report now.

---

# AST SpaceMobile (ASTS) — Financial Risk Assessment
**As of Nov 18, 2026 | Price $25.49 | Market cap ≈ $10.4B | Data through Q3 2026 (filed 2026-11-09)**

---

## 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (high-yield / distressed-adjacent)**

The company is a pre-commercial satellite operator whose balance sheet has been transformed by debt-funded capex. Total debt rose from **$173M (YE2024) → $2.24B (YE2025) → $4.12B (Q3'26)** — a 24x increase in 21 months. The entire stack is long-dated convertible paper (coupons 1.625%–4.25%, maturities 2032/2034/2036), which is a genuine mitigating factor: **no near-term refinancing cliff** (short-term debt is only $8.8M, 0.2% of total).

The critical credit insight: **the convertibles are deeply out of the money.** Conversion prices run $96–$120/share vs. a $25.49 stock. Equity-conversion relief is therefore unavailable — economically, **ASTS is carrying $4.1B of straight debt**, all of which must be cash-settled in 2032–2036 against $2.8B of cash today.

There are no financial maintenance covenants typical of leveraged loans, so classic covenant-breach risk is low. The risk here is not default-on-trigger; it is **cumulative cash consumption and terminal repayment capacity**.

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt | $4,118.7M | Up $1.88B in 9 months |
| Cash + ST investments | $2,798.9M | ($3.2B incl. restricted per call) |
| Net debt | $1,319.8M | Swing from -$962M to +$1,320M in 9M |
| Debt / equity | **1.90x** (9/30/26) | vs. 0.94x tool output (YE2025) — stale |
| Debt / assets | **60.8%** | vs. 45% at YE2025 |
| Net debt / EBITDA | **n.m. — EBITDA negative** | TTM EBITDA **-$655M**; no cover exists |
| Interest coverage (TTM) | **-8.3x** | TTM EBIT -$688M / interest $83.3M |
| Interest coverage (FY25) | -7.98x | Tool-confirmed |
| Cash interest run-rate | **~$121M/yr** (Q3'26 ×4) | 85% of TTM revenue |
| Current ratio | **13.65x** (Q3'26) | 16.35x on stale YE2025 data |
| Quick ratio | **13.30x** | Ex-inventory |
| Working capital | **+$2,851M** | Superb — the one unambiguously strong metric |
| Altman Z-Score | **0.605 — DISTRESS zone** | I recomputed on Q3'26: **~0.19** |
| Z-Score (market-cap x4) | **~1.26** | Still distress even crediting equity value |
| Piotroski F-Score | **5 / 9 — Moderate** | F1 (ROA), F2 (op CF), F5 (leverage), F7 (dilution) all fail |
| FCF yield (TTM) | **-17.2%** | TTM FCF -$1,799M / $10.4B cap |
| Cash runway | **~18 months** (≈Q2 2028) | At -$464M/qtr FCF |

**Z-Score caveat:** the model is built for manufacturers and penalises negative retained earnings (-$1,386M) and negative EBIT. It is a poor structural fit for a capex-buildout company. I report it because it is directionally correct and worsened materially — but it should not be read as a literal bankruptcy probability.

## 3. Market Risk Profile — **SEVERE**

| Metric | Value |
|---|---|
| Annualised volatility (3yr) | **101.9%** |
| Beta vs SPY | **2.66** (tool) / 2.85 (profile) |
| Max drawdown (3yr window) | **-80.9%** |
| Sharpe ratio (0% rf) | 0.496 |
| Sortino ratio | **NOT AVAILABLE — data gap** |
| Recent drawdown | **-65.7%** in 68 sessions ($74.31 Aug 12 → $25.49 Nov 18) |

A 2.7 beta means a 20% index drawdown implies a ~54% move here before idiosyncratic risk. Realised evidence confirms it: **-15.4% on Nov 5**, **-10.5% on Oct 9** on 54M shares (4x normal volume — institutional distribution). Volume has stayed elevated (22.6M on Nov 18) on the way down. Risk-adjusted return is poor: a 0.50 Sharpe delivered alongside 102% volatility and an 81% drawdown is not compensation, it is lottery-like dispersion.

## 4. Downside Scenario Analysis — Revenue -20%

TTM revenue is $142.9M. A 20% haircut is **-$28.6M**. At Q3'26 gross margin (40.2%), gross profit falls ~$11.4M:

- EBIT: -$688M → **~-$699M** (coverage -8.4x vs -8.3x)
- Z-Score: essentially unchanged
- **Conclusion: a 20% revenue decline is immaterial to solvency.**

This is the central finding. Revenue is only ~4% of the opex base ($838M TTM). Breakeven at a 40% gross margin requires **~$2.1B of revenue** ($2.4B to also cover interest) — **~15–17x current run-rate**. The company does not have a revenue-elasticity problem; it has a **scale-attainment and financing problem**.

The two scenarios that actually break the credit:

- **Financing-window closure.** Equity issuance has been the funding source (diluted shares: 154.5M → 256M → ~300M, +94% in 21 months). With the stock down 66% in three months and converts struck at $96–$120, both equity and convertible markets are effectively shut. Runway collapses to **~6 quarters**.
- **Capex overrun.** Q2'26 capex peaked at $597.6M. Holding the Q2–Q3 average (~$446M/qtr) for six quarters consumes $2.68B against $2.80B cash — **exhaustion while still adding debt.**

## 5. Overall Financial Risk Rating: **HIGH**

Not *Critical*, because $2.8B unrestricted cash, no 12-month maturities, a 13.7x current ratio, and genuinely inflecting revenue ($14.7M → $42.3M YoY, +187%) provide a real 18-month cushion. But leverage doubled in nine months, the Z-score is in the distress zone on any equity basis, interest now consumes 85% of revenue, and the company is structurally dependent on capital markets it currently cannot access on attractive terms. **Would move to Critical on: cash below ~$1.2B, any convert repurchase, or capex guidance increase without committed funding.**

## 6. Key Red Flags

1. **$4.1B of out-of-the-money convertibles is debt, not equity.** Conversion prices $96–$120 vs. $25.49 spot. No conversion relief; $4.1B cash repayment looms 2032–2036 against $2.8B cash.
2. **Serial dilution is the funding model.** +94% share count in 21 months. Piotroski F7 fails. Per-share value destruction is the hidden cost of the capex program.
3. **Negative gross profit on a TTM basis** (-$8.4M) due to the Q4'25 cost-of-revenue spike ($91.3M vs. $54.3M revenue). Q3'26's 40.2% margin is the honest run-rate — but the trend is not yet proven.
4. **Interest expense tripled in four quarters** ($7.5M → $30.3M). At $121M/yr it now exceeds FY2025 revenue.
5. **Leverage metrics decayed in nine months**: net cash -$962M → net debt +$1,320M; debt/assets 45% → 61%; Z-score 0.605 → ~0.19.
6. **Piotroski's two most important signals fail** — negative ROA (F1) and negative operating cash flow (F2). The F=5 is propped up by improvement-delta items, not absolute profitability.

## 7. Data Gaps (explicitly flagged)

- **Sortino ratio unavailable** — not computable from provided tools.
- **FCF yield tool output used a stale $6.53B market cap** (-17.41% vs. my recomputed -17.2% on $10.44B). I used the profile market cap of $10.44B; note implied shares (~410M) exceed Q3'26 weighted diluted (300M), suggesting further post-quarter issuance — unverified.
- **Net income reconciliation gap:** FY2025 income statement shows -$341.9M vs. cash-flow statement -$461.0M (~$119M unexplained; likely preferred/deemed dividends). Not resolved.
- **Debt maturity-by-year schedule and precise tranche sizes not obtained.** Aggregate $4.12B confirmed; individual tranches (4.25% & 2.375% due 2032, 1.625% due 2034, 2.30% due 2036) inferred from filings/press, not from a single authoritative schedule.
- **Peer benchmarking abandoned as non-informative.** The tool returned GOOG/META/NFLX/DIS/VZ/TMUS — mega-cap, profitable, cash-generative incumbents. No comparable pre-commercial LEO satellite peer was available; leverage ratios are not apples-to-apples.
- **No credit rating or CDS spread data available.** Rating above is my analytical construct, not an agency opinion.
