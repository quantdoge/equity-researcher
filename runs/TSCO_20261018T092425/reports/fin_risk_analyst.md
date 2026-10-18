# Fin Risk Analyst

- Symbol: TSCO
- Elapsed: 76.1s

---
## TSCO — Tractor Supply Company | Financial Risk Assessment
*Fiscal year ended 2025-12-27 (10-K filed 2026-02-19). All figures USD, from tools unless noted.*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (lower tier, ~BBB indicative)**

No agency rating, CDS spread, or bond-level data was available from the tools — the rating below is **inferred from fundamentals only**. Leverage is moderate and coverage is strong, but the direction of travel is wrong: gross debt rose **+$518M** in FY25 while shareholders were returned **115% of free cash flow**. Net leverage 2.93x is comfortable, not fortress-level, for a discretionary retailer.

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Revenue ($M) | 15,524.0 | 14,883.2 | 14,555.7 | +4.3% y/y |
| Gross margin | **33.24%** | 36.26% | 35.92% | **−302bp — major red flag** |
| Operating margin | 9.45% | 9.86% | 10.16% | compressing |
| EBITDA ($M) | 1,961.4 | 1,914.7 | 1,872.0 | +2.4% |
| Interest expense ($M) | 69.1 | 54.6 | 46.5 | **+26% y/y** |
| Total debt ($M) | 5,942.9 | 5,424.4 | — | +$518M |
| Net debt ($M) | 5,748.8 | 5,173.0 | — | +$576M |
| **Net debt / EBITDA** | **2.93x** | 2.70x | — | Rising |
| Gross debt / EBITDA | 3.03x | 2.83x | — | Rising |
| **EBIT / interest** | **21.2x** | 26.9x | 31.8x | Strong but halving pace |
| EBITDA / interest | 28.4x | 35.1x | 40.2x | Strong |
| Debt / equity (book) | 2.30x | 2.39x | — | Stable |
| Debt / assets | 54% | 55% | — | Lease-inclusive |
| **Altman Z-Score** | **3.11 (Safe)** | — | — | Book-equity version; market-cap version ≈ **4.2–4.8 (deep Safe)** |
| **Piotroski F-Score** | **6 / 9 (Moderate)** | — | — | Fails ROA Δ, GM Δ, asset-turnover Δ |
| Current ratio | 1.34 | 1.43 | — | Adequate |
| **Quick ratio** | **0.16** | — | — | Structural (inventory 88% of CA) |
| Cash ratio | 0.07 | 0.10 | — | Thin absolute liquidity |
| Cash ($M) | 194.1 | 251.5 | — | 1.25% of revenue |
| Working capital ($M) | +893.3 | +990.7 | — | Positive |
| Equity / assets | 24% | 23% | — | Levered, normal for retail |
| OCF ($M) | 1,635.3 | 1,420.8 | 1,334.0 | +15% y/y |
| Capex ($M) | 894.8 | 784.0 | 753.9 | 5.8% of sales |
| **FCF ($M)** | **740.5** | 636.8 | 580.2 | Improving |
| Dividends + buybacks ($M) | 848.9 | 1,057.1 | 1,068.3 | **115% of FCF** |
| FCF margin | 4.77% | 4.28% | 3.99% | Improving |
| **FCF yield** | **4.2%** | — | — | See valuation caveat |

**Liquidity assessment:** Cash runway is not the right lens — TSCO is FCF-positive ($740M) and has no operating burn. The real liquidity dependence is on **revolver access plus inventory turns**, given only $194M of cash against $2,614M of current liabilities. Lease-adjusted debt of ~$5.9B against $1.76B of reported long-term debt implies **~$4.18B sits in lease/finance obligations and other debt-like items**. **Data gap:** no debt maturity schedule was returned — I cannot size the refinancing cliff. This is the single most important missing input; with interest expense up 26% y/y, the refinancing rate matters.

### 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **30.2%** |
| Beta vs SPY | **0.53** (profile: 0.51) |
| **Max drawdown (3y)** | **−52.7%** |
| Sharpe ratio | **−0.53** (0% rf) |

Low beta (0.53) makes TSCO look defensive, but **30% realised vol against a 0.53 beta means the risk is idiosyncratic, not market-driven** — you are not compensated by the beta framework. The negative Sharpe confirms shareholders have earned nothing for that volatility over three years. The tape corroborates the fundamental deterioration: the stock closed CY2025 at $49.05, down from a $61.18 August-2025 high, and the tool-implied live price (~$33.16) is **~46% below that high** — the market has already begun pricing the margin-compression story. **Data conflict flagged:** price history (adj_close = close, no dividend adjustment) ends at $49.05 on 2025-12-31, while profile/market-cap data implies ~$33.16. This creates a $17.6B vs ~$26.0B market-cap gap, and therefore an FCF yield of **4.2% or 2.85%** depending on which is right (EV/EBITDA 11.9x vs 16.2x). The bear case is that the lower price is correct and reflects post-year-end de-rating.

### 4. Downside Scenario Analysis — Revenue −20% ($15,524M → $12,420M)

Holding gross margin at 33.2% and treating SG&A ($3,693M) as fixed (no cost action):

| Line | Base FY25 | **−20% revenue, no cost cuts** | −20% with 5% SG&A cut |
|---|---|---|---|
| Revenue | 15,524 | 12,420 | 12,420 |
| Gross profit | 5,160 | 4,128 | 4,128 |
| SG&A | 3,693 | 3,693 | 3,508 |
| EBIT | 1,467 | **435** | 620 |
| EBITDA | 1,961 | **929** | 1,114 |
| EBIT / interest | 21.2x | **6.3x** | 9.0x |
| **Net debt / EBITDA** | 2.93x | **6.19x** | 5.16x |
| Altman Z (book) | 3.11 | **~2.5 (Grey)** | ~2.7 (Grey) |
| Approx. FCF (capex cut to $450M maintenance) | 740 | **~350** | ~535 |
| Dividend coverage | 1.52x | **0.71x** | 1.09x |

**Findings:** A 20% revenue decline consumes the entire operating cushion and lands net leverage at **6.2x** — squarely in sub-investment-grade territory, with the Z-score crossing into the grey zone. **The dividend is not covered in this scenario** (0.71x), forcing either a cut, a revolver draw, or both; buybacks would be eliminated immediately. Because COGS is largely variable but SG&A and rent are not, the operating leverage is brutal: a 20% sales drop produces a **70% EBIT decline**.

**Tail case (−30% revenue, ~$10,867M):** EBIT turns **negative (~−$80M)**, EBITDA ~$409M, net debt/EBITDA **~14x**, interest coverage negative — a **covenant breach** and genuine refinancing failure risk. This is a low-probability, high-severity path, but it is the scenario in which an investment-grade rating does not survive.

### 5. Overall Financial Risk Rating: **MODERATE**

Balance-sheet solvency is not in question today: 2.93x net leverage, 21x interest coverage, Z-score 3.11 (4.2+ on market equity), positive and growing FCF. What keeps this from "Low" is the **combination of a 302bp gross-margin collapse, debt-funded buybacks (115% of FCF returned), rising interest cost (+26%), and a quick ratio of 0.16 with $194M of cash**. The company is one weak demand cycle away from 6x leverage. The risk here is *trajectory*, not *level*.

### 6. Key Red Flags

1. **Gross margin down 302bp to 33.24%** — the largest single deterioration in the dataset, and the driver of the Piotroski score stalling at 6/9 (fails all three trend tests: ROA Δ, GM Δ, asset turnover Δ).
2. **Shareholder returns exceed free cash flow** — $849M returned vs $740M FCF, with total debt up $518M. Buybacks and dividends are being partly debt-funded at the same time capex rises to 5.8% of sales.
3. **Interest expense +26% y/y** (46.5 → 54.6 → 69.1) — the fastest-growing line item on the P&L; coverage has fallen from 31.8x to 21.2x in two years.
4. **Liquidity structure** — 0.16 quick ratio and $194M cash (2% of liabilities); the company is operationally dependent on inventory liquidation and revolver capacity in any stress.
5. **Revenue growth (+4.3%) is being purchased with margin**, not earned — operating income was flat ($1,467M vs $1,468M) despite $641M of incremental sales.
6. **Market has already de-rated the stock ~46% from its Aug-2025 high on 30% vol** — if the ~$33 level is accurate, the equity is pricing in exactly the downside case modelled above.

**Explicit data gaps:** (a) no debt maturity schedule / revolver capacity — refinancing cliff unquantified; (b) no agency rating or CDS spread; (c) no true peer leverage comps (sector feed returned mega-caps: AMZN, TSLA, HD — not comparable specialty retailers); (d) yield-curve tool failed (one attempt, not retried); (e) price/market-cap conflict between price history ($49.05) and profile data ($33.16) leaves FCF yield ambiguous at 2.85%–4.2%.
