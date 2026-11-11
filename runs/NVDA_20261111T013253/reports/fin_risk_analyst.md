# Fin Risk Analyst

- Symbol: NVDA
- Elapsed: 75.0s

---
# NVIDIA (NVDA) — Financial Risk Assessment
**Data as of latest available: FY2027 Q2 (quarter ended 2026-07-26), market data to 2026-09-30. Price $228.38; market cap ≈ $5.52T (24.19B shares).**

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (highest tier)**

**Rating: Investment Grade — S&P 'AA' (upgraded from 'AA-'), Moody's 'Aa1' (positive outlook), short-term 'A-1+'.**

Solvency risk is effectively nil. The company holds **$99.4B cash & short-term investments against $38.9B total debt — a net cash position of ~$60.5B**. Interest coverage is ~500x. The Altman Z-Score sits in the "Safe" zone by a factor of two. There is no refinancing cliff, no covenant risk, and no plausible credit deterioration pathway within a 3-year horizon absent a genuine solvency-level collapse in AI capex (−60%+ and permanent).

**Important methodology flag:** the ratio tools returned figures on the FY2026 *annual* period (Jan-2026), which is three quarters stale. I have recomputed on a TTM / latest-quarter basis throughout. The direction of travel is what matters: **leverage is rising, not falling.**

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 (Jan-26, tool) | Latest / TTM (recomputed) | Assessment |
|---|---|---|---|
| Total debt | $11.41B | **$38.86B** | ⚠️ +203% in one quarter |
| Cash & ST investments | $62.56B | $99.37B | Strong |
| Net debt / (net cash) | $(51.1)B net cash | **$(60.5)B net cash** | Excellent |
| Debt / Equity | 0.07x | **0.17x** | Low but tripled |
| Net debt / EBITDA | −0.35x | **−0.26x** | Net cash |
| Interest coverage (EBIT/int.) | 503x | **~497x** (TTM EBIT $230.2B / int. $0.46B) | No debt-service risk |
| Current ratio | 3.91x | **4.59x** | Very strong |
| Quick ratio | 3.24x | **3.86x** | Very strong |
| Cash ratio | 1.94x | **2.31x** | Very strong |
| Working capital | $93.4B | **$154.4B** | Expanding |
| Altman Z-Score | **6.75 (Safe)** | **~6.36 (Safe)** | Distress zone is 1.81 |
| Piotroski F-Score | **5 / 9 (Moderate)** | 5 / 9 | ⚠️ Weakest signal |
| Equity / Assets | 76% | 71.5% | Deleveraging from earnings |
| FCF yield (TTM) | 2.34% (stale mkt cap) | **2.30%** ($127.0B / $5.52T) | Low — valuation risk |
| P/E (TTM) | — | **~28.6x** | Reasonable for growth |
| Cash runway | **Indefinite** (FCF-positive, net cash) | — | N/A |

**F-Score decomposition (why only 5/9):** loses points on **accruals quality (F4)**, ROA improvement (F3), gross-margin improvement (F8), and asset-turnover improvement (F9). It passes profitability, positive operating cash flow, deleveraging, positive equity change, and no dilution. F4 is the meaningful one — see red flags.

---

## 3. Market Risk Profile — **HIGH (this is the real exposure)**

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3y) | **44.1%** | ~2.9x the market |
| Beta vs SPY | **1.83** | A 20% market drawdown implies ~−37% |
| Max drawdown (3y) | **−36.9%** | Observed, not hypothetical |
| Sharpe ratio | **0.61** | Decent, but return-driven not risk-controlled |
| Current drawdown from 52w high ($235.20, May-2026) | **−2.9%** | Near highs — no valuation cushion |
| 12-month price change | roughly **+34%** (from ~$170) | Momentum intact |

The equity is a **high-beta, high-duration asset**. Note the asymmetry: the balance sheet cannot be impaired, but the *stock* routinely loses a third of its value. Any risk framing that treats NVDA as a defensive "safe" holding is wrong — beta of 1.83 means the market risk, not credit risk, is the binding constraint on position sizing.

---

## 4. Downside Scenario Analysis

Base: TTM revenue $303.0B, gross margin 72.0%, TTM operating income $190.0B (62.7% margin), TTM opex ~$28.2B (largely R&D, fixed), net cash $60.5B.

| Scenario | Revenue | Gross margin | Op. income | Net income | Interest coverage | Net cash | Z-Score |
|---|---|---|---|---|---|---|---|
| **Base (TTM)** | $303.0B | 72.0% | $190.0B | $192.9B | ~497x | +$60.5B | 6.4 |
| **−20% revenue** | $242.4B | 70.0% | **$140.1B** | ~$121.6B | **~140x** | +$60.5B | ~5.5 |
| **−35% revenue** | $197.0B | 65.0% | **$99.5B** | ~$86B | ~100x | +$60B | ~4.5 |
| **−50% (AI capex bust)** | $151.5B | 58.0% | **$59.9B** | ~$51B | ~60x | +$55B | ~3.4 |

**Interpretation: a 20% revenue decline is a non-event for solvency.** Gross profit falls ~21% but opex is only ~9% of revenue, so operating income falls ~26% to $140B — still roughly 5x the operating income of FY2024. Interest coverage remains >100x in every scenario. The Altman Z-Score stays in the Safe zone even at −50% revenue.

**This is structurally the opposite of a typical credit-stress profile:** the company has (a) almost no fixed obligations, (b) negative net debt, (c) a variable-cost-heavy cost structure (foundry-based, no fabs), and (d) $99B of liquidity. In a downturn, working capital *releases* cash rather than consuming it — the $30.7B Q2 working-capital drain of the upcycle would reverse into a substantial inflow. **Downside risk for NVDA is almost entirely a valuation/multiple event, not a financial-distress event.**

**Where the real downside lives:** at 28.6x TTM earnings and 2.3% FCF yield on a $5.5T market cap, a −20% revenue scenario that also compresses the multiple from ~29x to ~15x implies roughly a **−55% to −60% equity decline** — despite a pristine balance sheet. That is the number that matters to a portfolio.

---

## 5. Overall Financial Risk Rating: **LOW** (balance-sheet) / **HIGH** (market & earnings-quality)

**Composite: MODERATE**, split explicitly:
- **Credit/solvency risk: Very Low.** AA/Aa1, net cash, 500x coverage, Z-score 6.4.
- **Liquidity risk: Very Low.** $99B cash, 4.6x current ratio, no maturities that matter.
- **Market risk: High.** 44% vol, 1.83 beta, −37% observed drawdown.
- **Earnings-quality/FCF risk: Moderate and deteriorating.** This is the one area trending the wrong way.

---

## 6. Key Red Flags

1. **⚠️ Cash conversion has broken down — the single most important warning.** Q2 FY2027: net income $59.7B but operating cash flow only **$24.1B** (40% conversion), down from $50.3B the prior quarter. FCF $21.4B = 36% of net income. Driver: **working capital absorbed $30.7B in a single quarter.** For a company whose entire thesis rests on cash generation, a 60% earnings-to-cash gap is material.

2. **⚠️ Receivables ballooning / DSO deterioration.** AR rose to **$63.06B from $38.47B** at FY2026 (+64%) and from $40.71B just one quarter earlier (+55%), while quarterly revenue rose only 18%. **DSO extended to ~60 days from ~45 days.** Independently corroborated in the Q2 FY2027 release and press coverage.

3. **⚠️ Extreme customer concentration.** Reported 10-Q disclosures indicate **~70% of accounts receivable from five customers** (with three customers at ~56%). This is a double risk: revenue concentration *and* collection risk on a rapidly growing AR balance. If one hyperscaler stretches payment terms or pauses orders, both revenue and the receivables book are hit simultaneously.

4. **⚠️ Leverage inflection.** Total debt jumped from **$12.8B to $38.9B in one quarter** (long-term debt $7.5B → $32.4B). Still trivially small versus cash, but this is the first real balance-sheet leverage increase in the company's recent history and warrants monitoring — is this genuine financing need or optimization?

5. **⚠️ Capital returns exceeding free cash flow.** In Q2 FY2027: buybacks **$19.73B** + dividends **$6.05B** = **$25.8B returned against $21.4B of FCF.** The dividend step-up from ~$0.24B to $6.05B/quarter is a large, new, quasi-fixed commitment. Returning more than you generate while simultaneously tripling debt is a combination worth flagging to the committee.

6. **Inventory growing faster than revenue.** $31.6B vs $21.4B at FY2026 (+47%) and +22% QoQ against +18% revenue growth. Days inventory (~120) is stable, so this reads as pre-build for a ramp rather than channel stuffing — but in a demand air-pocket, inventory write-down risk is real given how fast product generations turn over.

7. **Piotroski F-Score of 5/9** is the weakest quantitative score in the set and mathematically reflects items 1, 2 and 6 (accruals, margin trajectory, turnover).

**Data gaps flagged:** (a) All computed ratios from the leverage/liquidity/Z-score/F-score/FCF-yield tools are based on **FY2026 annual data (Jan-2026) and are ~3 quarters stale** — I recomputed manually where possible, but quarterly Altman/Piotroski components are my estimates, not tool output. (b) The balance-sheet tool's `net_debt` field is internally inconsistent with `total_debt` minus `cash`; I used the ratio tool's definition (net cash of $51.1B at FY2026) and recomputed the current net cash of $60.5B myself. (c) Segment-level and customer-level revenue detail, R&D expense line, and the debt maturity schedule were not available from the tools; maturity profile is assumed long-dated given the negligible interest expense. (d) No CDS spread data.

---

### Bottom line for the memo
NVDA presents the **inverse of a typical credit-risk case**: the balance sheet is effectively unbreakable (AA/Aa1, net cash, 500x coverage, Z-score 6.4 safe at any plausible revenue decline), so **any downside thesis built on financial distress is wrong**. The risks that are real and quantifiable are (i) **44% volatility and a 1.83 beta** making this a levered bet on AI capex sentiment with a −37% drawdown already in the record, (ii) **a sharply deteriorating cash-conversion profile** ($30.7B single-quarter working capital drain, DSO 45→60 days, FCF at 36% of net income), and (iii) **70% of receivables concentrated in five customers**. Monitor the next two quarters of DSO and OCF conversion closely — that is the leading indicator that would convert an "earnings quality" concern into an actual demand-sustainability problem.
