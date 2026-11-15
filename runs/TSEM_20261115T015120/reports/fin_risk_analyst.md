# Fin Risk Analyst

- Symbol: TSEM
- Elapsed: 72.4s

---
## TSEM — Tower Semiconductor Ltd. Financial Risk Assessment
*Data as of 2026-11-15. Price $146.89; market cap $16.67bn; shares ~113.6m. FY2025 annuals + TTM built from Q4'25–Q3'26 quarters (FY2026 10-K not yet filed).*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-like balance sheet)**

Tower carries essentially no financial leverage. FY2025 total debt was **$161.5m** (ST $28.1m / LT $133.4m) against **$1.152bn cash & ST investments** — a **net cash position of ~$990m** (net debt/EBITDA **−1.82x**). Interest expense is **$0** in every quarter from Q4'25 through Q3'26, so the reported interest-coverage ratio is **not meaningful (null)** — the company is a net interest *recipient*, not payer. There is no covenant, refinancing, or maturity-cliff risk of any consequence: total debt is ~5% of assets and ~0.3x TTM EBITDA, and cash alone covers **2.76x total liabilities**.

| Metric | Value | Read |
|---|---|---|
| Debt/Equity | 0.06x | Negligible |
| Debt/Assets | 0.05x | Negligible |
| Net Debt/EBITDA | **−1.82x** (net cash) | Fortress |
| Interest Coverage | **NM** (interest expense $0) | No fixed-charge burden |
| Altman Z-Score | **5.41** (Safe zone; >2.99) | Distress probability very low |
| Piotroski F-Score | **6/9** (Moderate) | Held back by dilution & margin trend |
| Equity/Assets | 0.87 | Equity-funded |

**Z-score caveat:** the model's X2 (retained earnings/total assets) returned **0.0** because the feed reports `retained_earnings = 0` for FY2025 — a data artifact, not reality (equity of $2.90bn with no dividend history). Substituting equity for X2 (~0.87) lifts the Z-score to roughly **6.5**, so the "Safe" conclusion holds either way.

---

### 2. Key Financial Risk Metrics

**Liquidity — exceptional**
- Current ratio **6.48x**; quick ratio **5.51x**; cash ratio **4.37x**
- Working capital **$1.446bn**; assets/liabilities **7.95x**
- Cash **$1.152bn** vs total liabilities **$418m**

**Cash runway:** not a meaningful constraint. TTM operating cash flow **+$905m**; even in a scenario with zero operating cash generation, $1.15bn of cash plus undrawn capacity covers ~2.5 years *at the current $650m annual capex run-rate*.

**FCF sustainability — the one genuinely weak link**
- FY2025 FCF **−$41.1m** (OCF $395m vs capex $437m); FCF yield **−0.25%** (reported)
- TTM capex **$649m** = ~35% of TTM revenue, funding the $650m capacity/SiPho programme
- TTM reported FCF **+$255m**, but **$356m of the Q1'26 operating cash flow was a working-capital inflow** (likely customer prepayments/advances). **Excluding that swing, TTM FCF is approximately −$100m.** Cash conversion is capex-constrained, not demand-constrained.
- D&A is ramping fast: $77.8m (Q4'25) → **$90.5m (Q3'26)**, i.e. ~$360m/yr annualised and rising as new capacity qualifies. Gross margin is nonetheless *expanding* (26.7% → **34.0%**), so the margin structure is improving despite the depreciation drag.

**Operating trend (TTM: $1.840bn revenue, $708m EBITDA, $373m EBIT, $356m net income):** revenue +17.5% vs FY2025, EBITDA margin 38.5%. Q3'26 was a record quarter ($526m revenue, $1.05 diluted EPS) with Q4'26 guided to **$600m** and FY2026 to ~**$2bn**. This is a *strengthening*, not deteriorating, credit.

---

### 3. Market Risk Profile — **the dominant risk in this name**

| Metric | Value |
|---|---|
| Annualised volatility (3Y daily) | **69.9%** |
| Beta vs SPY (3Y daily) | **2.14** |
| Beta (provider profile) | 0.95 |
| Max drawdown (3Y) | **−58.7%** |
| Sharpe ratio | 1.18 |

**Beta conflict — flagged:** the computed 3Y daily beta (**2.14**) and the provider's profile beta (**0.95**) disagree materially, almost certainly because they use different windows/frequencies (weekly vs daily, 5Y vs 3Y). Either way, realised behaviour in 2026 is unambiguous: the stock ran from **$121.74 (Jan 2)** to a **$316.85 close on 2026-06-22** (+160%), then fell to **$146.89** — a **−53.6% drawdown from the June peak**, including a brutal −36% from $258 (Oct 6) to $131 (Nov 5). Volatility of ~70% with 2x market sensitivity means a market drawdown of 15% plausibly translates to a 25–35% hit here.

Critically, **the November de-rating was not a credit event**: it coincided with (11/02 filing) record Q3 revenue, 34% gross margin, and record Q4 guidance. This is multiple compression on an AI-optics/silicon-photonics narrative stock, not balance-sheet deterioration. At $146.89 the valuation is still demanding: **~23x EV/TTM EBITDA, ~47x TTM earnings**, on a business that is barely FCF-positive after capex.

---

### 4. Downside Scenario Analysis — revenue −20%

Base: FY2025 revenue $1.566bn, cost of revenue $1.202bn (of which I estimate ~$960m fixed fab overhead + depreciation, ~$242m variable). Revenue **−20% → $1.253bn**:

| Line | Base FY2025 | −20% revenue | Comment |
|---|---|---|---|
| Revenue | 1,566 | **1,253** | |
| Gross profit | 364 (23.2%) | **~99 (7.9%)** | Fixed-cost absorption collapse |
| Opex (SG&A + R&D) | ~170 | ~153 (−10% cost action) | |
| Operating income | 194 | **~−54** | Operating deleverage |
| Net interest | +~35 (income) | +~35 | Net cash cushions |
| Net income | 220 | **~−15 to +5** | Roughly breakeven |
| OCF | 395 | **~250–290** | D&A (~$310m) covers the loss |
| FCF (capex held $437m) | −41 | **~−150** | Flex capex down → FCF ≈ breakeven |

**Conclusion:** a 20% revenue decline produces an operating loss but *not* a liquidity problem — OCF stays strongly positive because D&A is ~20% of revenue, net cash is ~$1bn, and capex is discretionary (Tower has already flexed it repeatedly). Adding back the TTM capex of $649m, the true "survival" picture under stress is: no covenant, no maturity wall, no going-concern language possible at this capital structure.

**Piotroski lens on the deterioration already visible:** F3 (ROA improvement) = 0, F7 (no dilution) = 0 — shares rose from 111.2m to 113.6m — and F8 (gross-margin improvement) = 0 on the FY2024→FY2025 comparison. Note F8 has since *reversed* positive at the quarterly level (34.0% in Q3'26), so the F-Score of 6 likely understates current momentum.

---

### 5. Overall Financial Risk Rating: **LOW** *(balance sheet)* / **HIGH** *(equity market risk)*

**Composite: LOW-to-MODERATE financial risk, with HIGH market/valuation risk.**

Tower is one of the least levered semiconductor manufacturers in the market: net cash equal to ~6% of market cap, 6.5x current ratio, Z-score comfortably in the safe zone, and no interest burden. Survival risk over any realistic horizon is negligible. What *can* hurt an investor is not insolvency but (a) a ~70%-vol, 2x-beta equity that already demonstrated a 54% drawdown in five months, and (b) a valuation (23x EV/EBITDA, 47x earnings, ~0% sustainable FCF yield) that embeds the AI/silicon-photonics capacity ramp succeeding.

---

### 6. Key Red Flags

1. **Negative structural FCF on a ~$650m capex programme.** Capex is 35% of revenue; reported FCF of −$41m in FY2025 and ~−$100m TTM ex-working-capital. Growth is being bought, not harvested. If the SiPho/AI cycle turns mid-build, the returns on that capital are at risk even if solvency is not.
2. **Working-capital-dependent cash flow.** The $356m Q1'26 WC inflow flatters TTM OCF materially. Customer prepayments are a **refundable/earn-out obligation**, not free cash; if volumes disappoint, that reverses as a cash outflow.
3. **Severe valuation compression already underway.** −53.6% from the 2026-06-22 peak with no fundamental deterioration signals a de-rating regime; the stock is a sentiment-driven instrument, not a defensive holding.
4. **Geographic/operational concentration.** Israel-based with fabs in Migdal Haemek and Japan; single-region geopolitical and supply-chain exposure is not diversifiable at the asset level.
5. **Rising depreciation drag.** Quarterly D&A up 16% in three quarters to $90.5m. Reported margins will face a headwind as new capacity qualifies, even if gross margins hold.
6. **Dilution.** Share count up ~2.2% since FY2024 (F7 = 0); buybacks and dividends are $0.

**Data gaps (explicit):** interest coverage unavailable/null (zero interest expense — NM); R&D expense not broken out in the feed (opex derived as gross profit less operating income); no debt maturity-by-year schedule, credit rating, or CDS spread available; no FY2026 annual statements (TTM is a construction from quarterly rows); peer set returned only mega-caps (NVDA, TSM, AVGO, MU, AMD) with no comparable specialty-foundry multiples; price history retrieved for calendar 2026 only, with vol/beta/drawdown taken from the 3Y model window.

**Disclaimer:** This is a risk analytics assessment, not investment advice.
