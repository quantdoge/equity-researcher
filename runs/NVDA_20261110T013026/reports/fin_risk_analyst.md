# Fin Risk Analyst

- Symbol: NVDA
- Elapsed: 61.1s

---
## NVIDIA Corporation (NVDA) — Financial Risk Assessment
*Data through Q2 FY2027 (period ended 2026‑07‑26); market data through 2026‑09‑30*

---

### 1. Credit Risk Assessment: **INVESTMENT GRADE (Tier 1 — Aa1 / AA)**

NVIDIA carries essentially no credit risk in any conventional sense. Moody's rates it **Aa1 (positive outlook)** and S&P **AA** (issuer and issue level). This is corroborated by every metric in this report: net leverage of 0.07x, interest coverage above 400x, a current ratio of 4.6, and a Z‑Score of ~6.4 against a 2.99 "safe" threshold. LTM FCF of ~$127B exceeds total gross debt ($38.9B) by 3.3x — the company could retire all debt in under four months of cash generation.

The relevant credit question is not survival but the *direction of travel*: NVIDIA raised ~$25B of long‑term debt in a single quarter (LT debt $7.47B → $32.37B), taking net debt from **–$0.42B to +$16.42B**. It remains immaterial to solvency, but it is the first time the balance sheet has been levered and warrants monitoring for what it funds (see Red Flags).

---

### 2. Key Financial Risk Metrics

**Note on basis:** Statement-derived ratios from the tools use FY2026 annual (Jan 2026). I have recomputed leverage/liquidity on the **latest quarter (Q2 FY2027)** and **LTM** basis, as the FY2026 snapshot materially understates debt and overstates net cash.

| Metric | FY2026 (tool) | LTM / Latest Qtr (recomputed) | Assessment |
|---|---|---|---|
| Revenue (LTM) | $215.9B | **$303.0B** | +106% YoY in Q2 |
| EBITDA (LTM, reported) | $144.6B | **$233.9B** | Incl. non‑op gains |
| Operating income (LTM) | $130.4B | **$197.6B** | 65.2% margin |
| Total debt | $11.4B | **$38.9B** | $25B raised in Q2 FY27 |
| Cash & ST investments | $62.6B | **$99.4B** | 13.1% of assets |
| Net debt | –$51.1B | **+$16.4B** | Still ~net‑neutral |
| **Debt / Equity** | 0.07x | **0.17x** | Very low |
| **Debt / Assets** | 0.06x | **0.12x** | Very low |
| **Net Debt / EBITDA** | **–0.35x** | **0.07x** | Negligible |
| **Interest coverage (EBIT/int.)** | **503x** | **~427–497x** | Not a constraint |
| Interest expense (LTM) | — | $0.46B (≈2.5% avg. cost) | Fixed, cheap, LT |
| **Current ratio** | 3.91 | **4.59** | Excellent |
| **Quick ratio** | 3.24 | **3.86** | Excellent |
| Cash ratio | 1.94 | **2.31** | Excellent |
| Working capital | $93.4B | **$154.4B** | Growing |
| **Altman Z‑Score** | **6.75 (Safe)** | **~6.4 (Safe)** | Distress threshold 1.81 |
| **Piotroski F‑Score** | **5 / 9 (Moderate)** | — | See caveat below |
| Equity / Assets | 0.76 | 0.71 | Strong |
| FCF yield (LTM) | 2.21% (FY26 basis) | **2.31%** | Thin — see §4 |

**Piotroski caveat (important):** the F‑Score of 5 is **structurally misleading for a company in hyper‑growth**. Four of the five missed points are base‑effect artifacts: ROA improvement (0 — impossible from a 65%‑margin prior year), asset turnover improvement (0 — falling by construction as capacity and receivables grow faster than sales), gross margin improvement (0 — FY26 GM fell to 71.1% from 75.0%, but has since recovered to ~75.0% for four straight quarters), and leverage (1 — correctly still passing). Read *only* F4 (accruals quality, 0) as a genuine negative signal: FY2026 operating cash flow of $102.7B was below net income of $120.1B.

**Maturity profile:** short‑term debt is only $1.0B against $99.4B of cash. There is **no refinancing cliff**. The nearest maturities are effectively self‑funding.

---

### 3. Market Risk Profile

| Metric | 3‑Year (756d) | 1‑Year (252d) |
|---|---|---|
| Annualised volatility | **43.96%** | **40.22%** |
| Beta vs SPY | **1.83** | **1.78** |
| Max drawdown | **–36.9%** | **–25.3%** |
| Sharpe ratio (rf = 0%) | **0.675** | **0.085** |

Profile beta (longer horizon) is **2.22**. 52‑week range: **$163.89 – $236.00**; last close $228.38.

The critical market‑risk observation: **a ~1.8–2.2 beta against SPY means a 20% index drawdown implies a 36–44% drawdown in NVDA**, before any company‑specific de‑rating. In a market stress event, NVDA is a leveraged expression of the index, not a defensive holding.

More striking is the **collapse in risk‑adjusted return**. The one‑year Sharpe of **0.085** means the past twelve months delivered essentially zero return per unit of risk — despite revenue doubling. The stock is up only ~32% since 2025‑08‑01 ($173.30 → $228.38) through a period in which LTM revenue roughly doubled. That is severe multiple compression: the market has been de‑rating the growth. Volatility at 40–44% is the *ongoing* cost of ownership even in a bullish fundamental tape.

**Sortino ratio: not provided by the tooling — data gap.** Given the Sharpe of 0.085 and –25% to –37% drawdowns, downside deviation has been large.

---

### 4. Downside Scenario Analysis

**Base (LTM):** Revenue $303.0B · Gross margin 74.7% · Opex $28.7B · Operating income $197.6B (65.2%) · Interest $0.46B

**Scenario: –20% revenue (AI capex digestion).** I model two variants because the key swing factor is fixed‑cost absorption in COGS (HBM/TSMC commitments) rather than opex, which is only ~9% of revenue.

| Line item | Base | Case A (–20% rev, GM 68%) | Case B (–20% rev, GM 60%, opex cut) |
|---|---|---|---|
| Revenue | $303.0B | $242.4B | $242.4B |
| Gross profit | $226.2B | $164.8B | $145.4B |
| Operating income | $197.6B | $132.8B | $119.4B |
| Operating margin | 65.2% | **54.8%** | **49.3%** |
| Interest expense | $0.46B | $1.7B | $1.7B |
| **Interest coverage** | 427x | **~78x** | **~70x** |
| EBITDA | $233.9B | $137.3B | $123.9B |
| **Net debt / EBITDA** | 0.07x | **0.12x** | **0.13x** |
| Net income | $192.9B | ~$108.8B | ~$97.5B |
| FCF (est.) | $127.0B | **~$110–125B** | **~$85–95B** |
| Altman Z‑Score | ~6.4 | **~5.2** | **~5.0** |
| Current ratio | 4.59 | **>4.0** | **>4.0** |

**Conclusion: a 20% revenue decline is a non‑event for solvency.** Coverage stays near 70x, net leverage stays at 0.13x, and the Z‑Score remains deep in the safe zone. The true breakeven math is extraordinary: with a 75% gross margin and ~$30B opex, NVDA could lose **~85% of revenue** before interest coverage hits 3x, and **~82%** before becoming cash‑flow breakeven. There is no plausible demand scenario in which this capital structure fails.

**The real downside is equity re‑rating, not default.** At the 2026‑09‑30 close the equity trades at roughly **18x EV/Sales and 24x EV/EBITDA** on LTM figures. A –20% revenue scenario with margin compression to 49–55% would cut EBITDA to ~$124–137B; holding the current multiple would imply ~40% equity downside even though the business remains robustly profitable and debt‑free in substance. **The risk is transferred entirely from the lender to the shareholder.**

---

### 5. Overall Financial Risk Rating: **MODERATE**

This is a deliberately bifurcated rating, and the split is the substance of the assessment:

- **Balance‑sheet / solvency risk: VERY LOW.** Net leverage 0.07x, coverage 400x+, $99.4B cash, Z‑Score 6.4, Aa1/AA ratings, no refinancing cliff. Essentially unbreakable.
- **Market / valuation / concentration risk: HIGH.** Beta 1.8–2.2, volatility 44%, three‑year max drawdown –36.9%, one‑year Sharpe 0.085, 61% revenue concentration in four customers, and an 18x EV/Sales multiple that discounts flawless execution.

The composite is **Moderate** because NVIDIA's financial risk has migrated from the balance sheet to the income‑statement concentration and the equity multiple. Anyone holding NVDA is not exposed to default risk; they are exposed to a 40–50% drawdown if hyperscaler capex pauses or the multiple normalises.

**Data gaps flagged:** no debt maturity schedule beyond ST/LT split; no CDS spreads; Sortino not computed; no peer/industry median comparison available from the toolset; and the company profile price ($178.67 / $4.31T cap) is inconsistent with the 2026‑09‑30 close ($228.38, ~$5.50T cap) — I have used the price history as the more recent source and recomputed market‑based metrics accordingly.

---

### 6. Key Red Flags

1. **Cash conversion has deteriorated sharply — the most important signal in this report.** Q2 FY2027 operating cash flow was **$24.1B against net income of $59.7B (40% conversion)**, driven by a **–$30.7B working capital drain** (receivables +$22.3B, inventory +$5.8B in one quarter). LTM FCF/NI has fallen from 90.8% (FY2024) → 83.5% (FY2025) → 80.5% (FY2026) → **65.8% LTM**. Growth is increasingly being financed on the balance sheet rather than collected in cash.

2. **Receivable days jumped ~14 days in one quarter** (45.4 → 59.6 days QoQ). Combined with the $96.2B quarter (+106% YoY), this is the classic profile that precedes a revenue‑quality disappointment. Monitoring priority.

3. **Extreme customer concentration.** Per the FY2026 10‑K, **four direct customers represented 61% of revenue; the largest was 22% and the second 14%**. Effectively, NVIDIA's cash flow is a derivative of four hyperscaler capex budgets. This is a *demand* concentration risk, not a counterparty credit risk (the customers are AA‑rated), but it is the single largest threat to the earnings stream.

4. **Non‑operating income is inflating EBIT and EBITDA.** LTM EBIT ($230.2B) exceeds operating income ($197.6B) by **$32.6B — 14% of reported EBITDA** — from equity‑investment marks and similar items (Q1 FY2027 alone had a $16.5B gap). My leverage ratios above use operating income for this reason. Any EBITDA‑based metric that ignores this **overstates** true operating earnings power, and it raises the "circular financing" question given NVDA's stakes in AI customers.

5. **A $25B debt raise in a single quarter, unexplained by need.** LT debt rose $7.47B → $32.37B in Q2 FY2027. NVIDIA generates $127B of FCF annually and holds $99B of cash — it has no operational reason to borrow. The likely use (funding ecosystem/customer equity stakes) is precisely the kind of related‑party circularity that would convert a pristine credit into a levered, concentrated one. Verify against the FY2027 10‑K financing cash flows.

6. **Excess inventory purchase obligations are already triggering charges.** Per the Q2 FY2027 filing, provisions for inventory and **excess inventory purchase obligations totaled $1.0B for Q2 and $6.3B for H1 FY2027**. This confirms the off‑balance‑sheet take‑or‑pay exposure I flagged as a gap, and shows it is *already* costing ~4.7% of H1 gross profit. At $31.6B of inventory (up from $21.4B) ahead of the Vera Rubin launch, obsolescence risk through a node transition is live.

7. **Shareholder returns now rival FCF.** LTM buybacks $57.4B + dividends $6.8B = **$64.2B, or 51% of LTM FCF** — while simultaneously borrowing $25B. Buybacks at 18x EV/Sales are a value‑destructive use of capital if the multiple is inflated, and they reduce the buffer that makes the credit bulletproof.

8. **Gross margin has already proven it can compress ~4 points on mix/cost** (75.0% FY2025 → 71.1% FY2026), recovering to ~75.0% in FY2027. The recovery is real, but it demonstrates the sensitivity: HBM cost pass‑through and product mix can move margins materially within a single year.

9. **Valuation is the binding risk.** 18x EV/Sales and 24x EV/EBITDA leave no margin of safety. A one‑year Sharpe of 0.085 during a period of 100%+ revenue growth is the market telling you the multiple, not the business, is the variable that matters.
