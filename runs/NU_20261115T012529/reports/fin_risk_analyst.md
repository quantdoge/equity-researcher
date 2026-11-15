# Fin Risk Analyst

- Symbol: NU
- Elapsed: 60.5s

---
## NU HOLDINGS LTD. (NYSE: NU) — FINANCIAL RISK ASSESSMENT
*As of 15-Nov-2026. Latest reported period: Q3 2026 (filed 12-Nov-2026); latest full year: FY2025.*

**Framework note:** NU is a bank (Brazilian digital lender), so standard industrial credit screens (Altman Z, EBIT/interest, net debt/EBITDA) are structurally misleading here. I report them because the mandate requires it, but I weight bank-appropriate metrics — equity/assets, allowance coverage, NPL formation, deposit funding, PPI vs. provisions — more heavily.

---

### 1. Credit Risk Assessment: **SUB-INVESTMENT GRADE**

| Rating | Level | Outlook |
|---|---|---|
| Moody's — Nu Holdings | **Ba2** | Stable |
| Moody's — Nu Financeira | **Ba1** | Stable |
| S&P — Nu Holdings / Nu Financeira | **BB** | Stable |
| S&P (Brazil national scale) | brAAA | — |

Two notches below investment grade. The rating is a *sovereign-and-jurisdiction* constraint story, not a company-solvency story: the operating business earns a brAAA local rating while the group carries Brazil transfer/convertibility risk. CDS spreads were not available from our data sources (gap).

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Q3'26 | Read |
|---|---|---|---|---|---|
| Debt/equity (ex-deposits) | 0.18 | 0.12 | 0.46 | 0.21 | Low — total debt only $3.0bn |
| Liabilities / equity (all-in) | 5.8x | 5.5x | 5.6x | **5.1x** | Normal bank leverage |
| Equity / assets | 14.8% | 15.3% | 15.1% | **16.4%** | Strong vs. global banks (8–12%) |
| Net debt / EBITDA | net cash | net cash | net cash (−$10.9bn) | net cash (−$19.3bn) | N/M for a bank |
| Interest coverage (EBIT/int.) | 0.76 | 0.99 | **0.84** | ~0.86 | **Artifact** — see note |
| Altman Z-Score | — | — | **0.22 ("Distress")** | — | **Not valid** for a bank |
| Piotroski F-Score | — | — | **4 / 9 (Weak)** | — | Mixed; see note |
| Current ratio | 1.08 | 0.96 | 0.59 | 0.89 | Not meaningful for a bank |
| Cash + ST investments | $22.0bn | $23.1bn | $16.1bn | **$38.1bn** | 80% of deposits |
| NPL 90+ | — | — | — | **7.3%** (6.9% Q2, 6.7% Q3'25) | **Deteriorating** |
| Stage 3 / gross loans | — | — | 6.2% (Dec) | **8.4%** | **+220bp in 9M** |
| Allowance / 90+ NPL | — | — | — | **234%** | Exceptional buffer |
| ROE (annualised) | ~17% | ~27% | ~27% | **~32%** | Best-in-class |

**Why three of the tool metrics are unreliable, stated explicitly:**
- **Altman Z = 0.22 (distress zone)** is a false signal. X1 (working capital/assets) is structurally negative for a deposit-funded lender (−0.33), and X4 uses *book* equity ($14.3bn) instead of the $64bn market cap. Re-running X4 on market value would roughly triple that component. Do not treat NU as bankruptcy-risk on this basis.
- **Interest coverage 0.84** compares EBIT to *cost of deposits*, which for a bank is an operating expense, not a financing claim. Interest expense ($4.58bn FY25) sits below operating income by construction in bank P&L structure. The economically correct coverage is **pre-provision profit vs. provisions**: annualised PPI ≈ **$12bn** against an annualised ECL charge ≈ **$6.7bn** — coverage of **~1.8x**.
- **Current ratio 0.59** classifies demand deposits as current liabilities; universal banks always fail this test. Liquidity is assessed below instead.

**Piotroski F-Score 4/9** — points lost on leverage (F5), no-dilution (F7), gross margin (F8), asset turnover (F9), and ROA improvement (F3). The leverage and dilution flags are structural/benign for a growing bank (share count has been flat at ~4.84bn since 2022 — F7 is a technicality of SBC issuance). Gross margin and asset turnover declines are *real*: they reflect cost of deposits and provisions rising faster than earning assets.

**FCF sustainability:** FY2025 FCF $3.49bn, **yield 5.4%**, FCF margin rising 14.2% → 14.2% → 20.0% → **22.0%** (2022–2025). Improvement is genuine, but note that for a lender OCF is dominated by loan-book working-capital flows (−$6.07bn in FY25); this is *loan-growth absorption*, not discretionary cash. NU pays no dividend and buys back no stock — 100% of earnings is retained into capital, which is the correct policy at this growth rate but means zero shareholder cash return.

---

### 3. Market Risk Profile

| Metric | Value | Note |
|---|---|---|
| Beta vs S&P 500 | **0.97** | Reported beta; understates true risk (see below) |
| 52-week high / low | **$18.98** (29-Jan-26) / **$11.20** (3-Jun-26) | — |
| Peak-to-trough (52wk) | **−41.0%** | Current $13.22, −30.7% YTD, −30% off high |
| Max drawdown (3yr), annualised vol, Sharpe, Sortino | **NOT AVAILABLE** | Volatility endpoint gated on our data plan; retry failed. Gap. |

The 0.97 beta is misleading. NU's dominant risk factor is not the S&P — it is **Brazilian political and rate cycles**, evidenced by a **−20.5% single-day move** following the Brazilian election. Effective downside participation in an EM risk-off event is materially higher than the beta implies; treat this as a high-beta instrument to Brazilian country risk regardless of its US listing and USD reporting.

---

### 4. Downside Scenario Analysis

Base (Q3'26 annualised): revenue ~$22.4bn, pre-tax income ~$5.4bn, net income ~$4.4bn, equity $14.3bn, ROE ~32%.

**Scenario A — Revenue −20% (severe Brazil recession, margin compression)**
Revenue −$4.5bn. Assuming ~30% variable-cost flex in cost of revenue (deposit costs partly follow the loan book) and ~25% opex flex:
- Pre-tax income falls to roughly **−$1.5bn to −$2.0bn**
- Net income ≈ **−$1.2bn to −$1.6bn**; ROE swings from +32% to roughly **−10%**
- Equity/asset declines from 16.4% to ~15%; still solvent, still above regulatory minimums
- Capital generation stops entirely; growth must be curtailed

**Scenario B — Credit shock (the binding constraint): ECL +50%**
ECL $6.7bn → $10.0bn annualised (−$3.3bn pre-tax): net income falls to ~**$1.0bn**, ROE ~**7%**. Profitable but de-rated.
**ECL doubling (+100%, $13.4bn)**: pre-tax ≈ **−$2.6bn**, ROE ≈ **−20%**, consuming ~$2.6bn of the $14.3bn equity base in one year.

**Survivability verdict:** one year of pre-provision profit (~$12bn) covers **1.7x the entire existing allowance** ($7.09bn) and **1.0x** a full doubling of credit costs. Even in Scenario B-doubling, NU absorbs the loss from earnings plus retained capital without approaching a covenant or regulatory breach. The 2022 stress test is the empirical precedent: revenue $4.5bn, net loss −$365m, and the franchise emerged with 27% ROE two years later.

**Refinancing cliff: none.** Total debt is only $3.0bn against $38.1bn of cash and short-term investments and $47.5bn of deposits. There is no near-term maturity wall that matters. Deposit cost is 87% of interbank rates — a funding *pricing* risk, not a funding *availability* risk.

---

### 5. Overall Financial Risk Rating: **MODERATE** (trend: deteriorating)

**Survivability: high.** Net cash, 16.4% equity/assets, 234% NPL coverage, 80% cash coverage of deposits, $12bn PPI, no maturity cliff, and proven crisis navigation in 2022.

**What keeps it from "Low":** (i) credit quality is deteriorating at a pace that outruns revenue growth; (ii) the book is 92% unsecured; (iii) sub-investment-grade rating with Brazil sovereign linkage; (iv) a −41% trailing drawdown and −20.5% single-day political shock demonstrate real capital-markets risk.

---

### 6. Key Red Flags

1. **Stage 3 loans 6.2% → 8.4% of gross loans in nine months** (+220bp). NPL 90+ rising sequentially two quarters running (6.7% → 6.9% → 7.3%). The 15–90 day leading indicator ticked *up* to 4.9% in Q3 — formation is not decelerating.
2. **Provisions growing 70.7% YoY vs. revenue +39.5%.** Pre-tax margin compressed 3.6pts (26.8% → 23.2%). Risk-adjusted NIM slipped to 12.1% from 12.4%. This is the classic early-stage credit-cycle signature.
3. **92% unsecured concentration.** Cards $27.2bn + unsecured personal loans $11.0bn of a $41.6bn book; secured lending is only $3.4bn (8%). Loss severity in a downturn is structurally high.
4. **Sub-investment-grade (Ba2/BB) with no IG funding cushion**, and single-country deposit concentration (Brazil $38.6bn of $47.5bn). A sovereign downgrade mechanically pressures both funding cost and the rating.
5. **Currency translation.** Revenue is BRL-earning, reported in USD; BRL depreciation directly compresses reported earnings and the USD equity base.
6. **Data-quality flag:** the Q2'26 balance sheet from our feed is internally inconsistent (total debt $42.0bn, short-term debt $39.5bn, current assets $9.8bn) versus ~$3bn of debt in Q1'26 and Q3'26. I excluded the Q2 balance sheet from all ratios above. Any model built on that field will be wrong.

### Explicit Data Gaps
- **Capital adequacy / CET1 ratio: not obtained.** The 20-F confirms the Brazilian minimum total solvency ratio is 9%, but NU's actual CAR was not disclosed in any source I could access. This is the single most important missing input for a bank and should be sourced from the Q3'26 6-K or the company's IR capital-disclosure page before finalising the memo.
- **Volatility, 3-year max drawdown, Sharpe, Sortino:** unavailable — the price-volatility endpoint is not licensed on our plan and the single retry failed.
- **CDS spreads, peer multiples:** not gathered within budget.
- Altman Z and interest coverage are reported per mandate but are not valid measures for this issuer; treat as informational only.
