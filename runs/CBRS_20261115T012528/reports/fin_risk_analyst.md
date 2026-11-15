# Fin Risk Analyst

- Symbol: CBRS
- Elapsed: 50.5s

---
## CEREBRAS SYSTEMS INC. (CBRS) — Financial Risk Assessment

**Snapshot:** AI infrastructure / semiconductors, 708 employees, IPO 14-May-2026, price $108.72, market cap $24.63B. FY2025 annuals plus Q1–Q3 2026 quarterlies are the basis; no FY2026 annual yet.

> **Critical data-integrity caveat before any number:** the pre-computed ratio tools all ran on the **FY2025 annual** filing, which classifies the redeemable convertible preferred stock (~$1.93B) as a **liability**, producing *negative* book equity (equity −$578.7M, debt/equity −0.45, equity/assets −0.25). The **Q4-2025 quarterly** presents the same balance sheet with that preferred classified in equity (equity **+$1,354.7M**). Post-IPO (Q2-2026) the preferred converted, and equity is **+$9,158.9M**. **Every trailing tool output below is therefore stale and directionally wrong** — I recompute on Q3-2026 where it matters and label each figure.

---

## 1. Credit Risk Assessment — **Investment Grade** (balance sheet) / *Sub-Investment Grade* (earnings coverage)

This is a **net-cash company**, not a leveraged one. It is not a default-risk story; it is a cash-consumption and equity-dilution story.

| Q3-2026 (30-Sep-26) | Value |
|---|---|
| Cash & ST investments | **$7,360.8M** |
| Total debt | $1,450.2M (ST $706.5M, LT $122.6M, ~$621M leases) |
| **Net cash** | **+$5,910.6M** |
| Debt / equity | **0.16x** (tool: −0.45x — invalid) |
| Net cash / market cap | 24.0% |
| Cash / market cap | 29.9% |
| Current ratio | 5.27x (tool's 2.15x is FY2025) |
| Altman Z (recomputed, book equity) | ~2.4 grey zone; ~5.7 with market cap in x4 |

**Interest coverage is negative and cannot be computed meaningfully:** TTM EBIT −$632.6M vs TTM interest $37.5M (≈$74M annualised, ~5.1% on $1.45B). Interest is serviced from the cash pile, not from operations, and represents ~1.0% of cash — immaterial. **No credit rating or CDS spread is available** (recent IPO, no public issue). No refinancing cliff: the $706.5M current debt is 9.6% of cash and coverable on demand.

**The earnings quality problem is real.** FY2025 net income of **+$237.8M** coexists with **operating income of −$145.3M**. The swing is a ~$383M **non-operating gain in Q2-2025** (Q2-25 net income +$309.5M against operating cash flow of **−$68.9M**). Reported FY2025 EBIT of +$244.9M vs operating income of −$145.3M confirms the gap. That profit is non-recurring; do not underwrite it.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (annual) | TTM / Q3-2026 | Tool output (stale) |
|---|---|---|---|
| Revenue | $510.0M | $755.8M TTM | — |
| Gross margin | 39.0% | 26.3% (9M-26) | — |
| Operating margin | −28.5% | **−99.3%** TTM | −28.48% |
| EBITDA (GAAP) | +$279.3M *(gain-inflated)* | **−$590.1M** | — |
| Debt / equity | n/a (neg. equity) | **0.16x** | −0.45 |
| Net debt / EBITDA | n/a | Net cash; NM | −3.03x |
| Interest coverage (EBIT/int.) | 0 (no interest) | **Negative / NM** | null |
| Current ratio | 2.15x | 5.27x | 2.15x |
| Quick ratio | 2.06x | 5.19x | 2.06x |
| Altman Z | — | ~2.4 / ~5.7 | **0.327 "Distress"** |
| Piotroski F | — | — | **5 / 9 "Moderate"** |
| FCF | −$392.8M | **−$1,435.0M (9M-26)** | — |
| FCF yield | −1.68% | **−7.8% run-rate** | −1.68% |

**Piotroski detail (F=5):** profitability 2/4, leverage/liquidity 3/3, efficiency 0/2. The two zeros that matter — **F2 positive operating cash flow = 0** (OCF −$10.5M against +$237.8M net income: a severe accrual gap) and **F9 asset turnover improvement = 0**. F7 "no dilution = 1" is already wrong for 2026: diluted shares went **226.5M → 238.9M (+5.5%)** in two quarters, with **$541.7M of SBC in 9M-2026**.

---

## 3. Market Risk Profile — **severe**

| Measure | Value |
|---|---|
| Annualised volatility (252d) | **113.8%** |
| Beta vs SPY | **2.81** (profile states 1.85) |
| Max drawdown | **−73.7%** |
| Sharpe (0% rf) | **−1.27** |
| IPO first-day close | $311.07 (intraday high $386.34) |
| Trough close | $81.71 (05-Nov-26) |
| Current vs peak | **−65%** (from first close); −27% above trough |

A 2.81 beta on 114% vol means a 20% SPY drawdown plausibly maps to a **45–60%** CBRS drawdown on beta alone, plus idiosyncratic gap risk (single days of −11.0% and +11.2% in November). Sharpe of −1.27 reflects a pure momentum/repricing regime in seven months of trading — **there is no 3-year history**, so max drawdown and Sharpe are measured over only ~125 sessions. Sortino is **not available** (no downside-deviation output from the tool) — flagged as a gap.

---

## 4. Downside Scenario: revenue −20%

Base: TTM revenue $755.8M, gross margin 26.3%, annualised opex ~$1,160M (9M-26 SG&A $296.7M + R&D/other), capex run-rate $1,395M, FCF ~−$1.9B.

- **Revenue $604.6M** (−20%); gross profit falls ~$39.7M to ~$159M.
- With 10% opex flex → operating loss widens from −$750M to **≈−$885M**; with no flex, **≈−$1,000M**.
- **Cash runway:** $7,360.8M ÷ −$478.3M/qtr (9M-26 average FCF burn) = **~3.8 years**; at Q3's −$838.6M/qtr pace = **~2.2 years**; on net cash only, **~3.1 years**. Cutting capex to zero extends runway to **~5.4 years** (Q3 OCF alone −$341.4M/qtr).
- **Covenant risk: none identified** — no material funded debt, no disclosed maintenance covenants. The binding constraint is **equity dilution, not solvency**: ~11%/yr share growth plus a probable future raise would be the mechanism of loss.
- **The realistic downside is worse than −20%.** Q3-2026 disclosure shows **OpenAI 34% and MBZUAI (G42-affiliated) 38% of revenue — 72% from two customers.** Losing MBZUAI alone is a **−38%** revenue event. Against that, **RPO is $26.1B** (~35x TTM revenue) and 700 MW under contract — a genuine contractual backstop that materially offsets near-term demand risk, though RPO quality and cancellation terms are unverified (gap).

---

## 5. Overall Financial Risk Rating: **HIGH**

Split explicitly, because a single word hides the truth: **solvency risk = LOW** (net cash $5.9B, D/E 0.16x, current ratio 5.3x, no near-term maturities). **Liquidity/burn risk = MODERATE** (2.2–3.8 years runway, but capex is discretionary and RPO is large). **Equity/market risk = HIGH-to-CRITICAL** (114% vol, 2.81 beta, −74% drawdown, −7.8% FCF yield, 72% customer concentration, dilutive). Net: **High**. A credit analyst would be comfortable; an equity holder is taking venture-style risk in a public vehicle.

---

## 6. Key Red Flags

1. **Gross margin collapse: 44.6% (Q1-26) → 14.2% (Q2-26) → 20.0% (Q3-26)** vs 39.0% FY2025. Mix is shifting to low-margin hardware/cloud buildout. Even ex-SBC, Q3 adjusted EBITDA is only ~+$13M on $210.8M revenue.
2. **Customer concentration 72% (OpenAI 34% + MBZUAI 38%)** — with Middle East/export-licence political exposure on the larger of the two.
3. **Accrual quality: net income +$237.8M vs OCF −$10.5M in FY2025**; profit driven by a non-recurring ~$383M non-operating gain. Piotroski F2 = 0.
4. **Receivables ballooning: DSO 53 days (FY2025) → 109 days (Q3-26)**, plus $146.1M inventory and a −$432.3M working-capital drain in Q3 alone. Collection/quality-of-revenue signal.
5. **Cash burn accelerating: FCF −$119.6M → −$476.7M → −$838.6M** across Q1→Q3 2026.
6. **Dilution: +5.5% diluted shares in two quarters, $541.7M SBC in 9M-26.** The "no dilution" F-score point is obsolete.
7. **Valuation leaves no cushion:** 32.6x TTM sales, 24.8x EV/sales, 2.7x book — 65% below IPO despite revenue +55% YoY. Multiple compression, not fundamentals, has been the driver.

**Data gaps (explicit):** no credit rating/CDS; no debt maturity ladder or covenant detail (only ST/LT split); no Sortino ratio; no 3-year price history (IPO May-2026, so drawdown/Sharpe/beta are short-window and unstable); FY2025 annual vs Q4-2025 quarterly balance sheets are irreconcilable on preferred-stock classification — **all tool-sourced leverage, Z-score and liquidity figures in this note should be treated as superseded by the Q3-2026 recomputations**; RPO terms, backlog cancellability, and capex commitments are unverified.
