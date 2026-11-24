# Fin Risk Analyst

- Symbol: BURL
- Elapsed: 60.3s

---
## Financial Risk Assessment — Burlington Stores, Inc. (BURL)

**Sector:** Consumer Cyclical / Apparel-Retail (off-price) · **Market cap:** $14.77bn · **Price:** $235.16 · **FY2025 (ended 1/31/26) results filed 3/19/26** · Yield curve as of 11/24/26

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE**

| Item | Reading | Assessment |
|---|---|---|
| S&P issuer rating | **BB+** (crossover-tier high yield) | One notch below IG; S&P projects adjusted leverage improving to **2.3x (2026E) / 2.2x (2027E)** |
| Interest coverage (EBIT/interest) | **11.89x** | Strong; not a credit concern |
| Net debt/EBITDA (as reported) | **3.66x** | Looks elevated — **but see the lease distortion below** |
| Net *financial* debt/EBITDA (ex-op-leases) | **~0.65x** | Genuinely low leverage |

**Critical analytical adjustment:** Reported `total_debt` of $6,005m is *not* financial debt. Short-term ($70.6m) + long-term ($2,011.7m) debt = **$2,082m**; the residual **~$3,923m is operating lease liabilities**. Interest expense of only $71.0m on the reported $6.0bn would imply a 1.2% coupon — impossible. At $2.08bn it implies **~3.4%**, consistent with the actual notes. Netting cash of $1,232.5m, true **net financial debt is just ~$850m**, or **0.65x EBITDA**. This is a well-capitalized balance sheet wearing an accounting costume.

**Refinancing/cliff risk:** Debt structure is a **$2.0bn senior notes/term stack plus an asset-based ABL revolver** (historically undrawn; S&P's default waterfall assumes ~$550m drawn at 60% utilization — that is a *default-scenario* figure, not current borrowing). Notably, the revolver has historically carried **no outstanding revolving loans**, so near-term maturities are modest. Context: the curve is now **2Y 4.74% / 10Y 5.13%** (no inversion) — refinancing into 5%+ term money from ~3.4% legacy coupons implies a meaningful step-up in interest cost, though off a very small base ($71m).

**Verdict:** Credit quality is sound. BB+ reflects the sector's cyclicality and the lease-adjusted stack, not distress. **Upgrade trajectory toward IG is plausible** given 0.65x net financial leverage and improving EBITDA margins.

---

### 2. Key Financial Risk Metrics Table

| Metric | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|
| Revenue ($m) | 11,566.9 | 10,634.8 | 9,727.5 | 8,702.6 |
| EBITDA ($m) | 1,305.0 | 1,091.9 | 851.2 | 644.4 |
| EBITDA margin | **11.28%** | 10.27% | 8.75% | 7.40% |
| EBIT ($m) | 887.2 | 744.3 | 544.2 | 374.0 |
| Net income ($m) | 610.2 | 503.6 | 339.6 | 230.1 |
| Operating CF ($m) | 1,231.4 | 863.4 | 868.7 | 596.4 |
| Capex ($m) | (1,059.8) | (892.0) | (517.3) | (451.1) |
| **Free cash flow ($m)** | **171.6** | **(28.6)** | 351.5 | 145.3 |
| Interest expense ($m) | 71.0 | 69.5 | 78.4 | 66.5 |
| Buybacks ($m) | (278.4) | (256.3) | (243.2) | (316.9) |

**Leverage & solvency**

| Metric | Value | Read |
|---|---|---|
| Debt/Equity (book) | 3.32x | Looks high, but equity is buyback-depleted |
| Debt/Assets | 0.61 | Lease-inclusive |
| Net debt/EBITDA (reported) | 3.66x | Lease-inclusive |
| Net financial debt/EBITDA | 0.65x | **True economic leverage** |
| Equity/Assets | 0.18 | Thin book equity (structural) |
| Interest coverage | 11.89x | Comfortable |

**Liquidity**

| Metric | Value | Read |
|---|---|---|
| Current ratio | 1.23 | Adequate |
| Quick ratio | 0.65 | Weak *by design* — inventory-funded retail |
| Cash ratio | 0.55 | Strong |
| Cash | $1,232.5m | ~10.7% of revenue |
| Working capital | +$522.3m | Positive |
| Assets/Liabilities | 1.22 | Modest cushion |
| Cash → liabilities | 0.15 | Low, but cash covers **~2.4yrs** of interest + maintenance capex |

**Scores:** Altman **Z = 1.954 (grey zone)** · Piotroski **F = 8/9 (strong)**

Two caveats on Z-Score: (a) it uses **book** equity of $1.81bn, whereas market cap is $14.77bn — substituting market value would raise x4 roughly 8x and push Z firmly into the safe zone; (b) it penalizes lease liabilities as debt without crediting the corresponding rent-free operating model. **I treat the 1.954 as mechanically misleading and not a bankruptcy signal.** The F-Score of 8/9 corroborates: profitability, cash generation, accruals quality, deleveraging, no dilution, and gross-margin improvement all pass (only asset-turnover improvement fails) — corroborated by EBITDA margin expanding every year from 7.4% → 11.3%.

---

### 3. Market Risk Profile — **HIGH**

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **40.14%** | ~2.5-2.7x market volatility |
| Beta vs SPY (756d, calculated) | **0.949** | ~Market-like |
| Beta (vendor profile) | 1.502 | **Conflict — flagged** |
| Max drawdown (3yr) | **−38.93%** | Severe peak-to-trough |
| Sharpe ratio (0% Rf) | **0.068** | Effectively zero excess return |

**Note on the beta conflict:** vendor beta of 1.502 vs. 0.949 computed over 756 days. The high 40% volatility against a sub-1.0 beta implies a large **idiosyncratic** risk component — BURL moves on its own news (comps, margins, tariffs), not on the market. For risk-management purposes, **treat downside risk as driven by company-specific earnings volatility, not market beta** — diversification will not protect you here.

**The Sharpe of 0.068 is worse than it appears:** that figure assumes a 0% risk-free rate. Against an actual ~4.7% T-bill, a 40%-vol stock generating near-zero excess return implies **negative risk-adjusted return over 3 years**. Investors have been paid nothing for substantial volatility.

---

### 4. Downside Scenario Analysis — Revenue −20%

Stress: revenue to **$9,253m**, gross margin −150bps to 42.4% (promotional markdowns), SG&A down only 10% (store payroll/occupancy is semi-fixed), D&A unchanged.

| Line | Base FY2025 | Stressed | Δ |
|---|---|---|---|
| Revenue | 11,566.9 | 9,253.5 | −20.0% |
| Gross profit | 5,080.0 (43.9%) | 3,925.3 (42.4%) | −22.7% |
| SG&A | 3,817.2 | 3,435.5 | −10.0% |
| D&A | 417.9 | 417.9 | — |
| **EBIT** | 887.2 | **71.9** | **−91.9%** |
| EBITDA | 1,305.0 | **489.8** | −62.5% |
| Interest | 71.0 | 71.0 | — |
| **EBIT coverage** | 11.89x | **1.01x** | Near breakeven |
| Net income | 610.2 | **~$0** | −100% |
| Net financial debt/EBITDA | 0.65x | **1.73x** | Still fine |
| Net debt/EBITDA (reported) | 3.66x | **9.74x** | Covenant-pressure zone |

**What actually breaks:** operating leverage is brutal — a 20% revenue decline destroys **92% of EBIT** because 33% of revenue sits in semi-fixed SG&A. EBIT coverage falls from 11.9x to ~1.0x, breaching an incurrence-style leverage test and forcing the **$278m buyback program to halt**.

**What does *not* break — the survival case:** Even here, the company generates cash. Stressed OCF = ~$0 net income + $418m D&A + ~$107m SBC + ~$200m inventory release ≈ **$725m**; cutting capex to maintenance (~$550m) still yields **~$175m of positive FCF**. Add $1,232m of cash and an undrawn ABL. **This company survives a 20% revenue decline without needing external capital.** Management's discretionary lever — capex ran $1,060m in FY2025 against ~$450-550m of maintenance need — is the release valve.

---

### 5. Overall Financial Risk Rating — **MODERATE**

Split verdict: **credit risk LOW**, **market risk HIGH**, **FCF sustainability MODERATE**. The balance sheet is sound and the business model is genuinely resilient in a downturn; the risk is that shareholders are being handed near-zero free cash flow and 40% volatility in exchange for excellent headline growth.

---

### 6. Key Red Flags

1. **⚠️ Buybacks exceed free cash flow.** FY2025: $278m repurchased vs **$172m FCF**; FY2024: $256m repurchased vs **−$29m FCF**. Total debt rose **$634m** year-over-year. Shareholder returns are being **funded with borrowed money** — the single clearest deterioration signal in this dataset.
2. **⚠️ Structurally weak FCF despite record EBITDA.** EBITDA up 103% since FY2022, yet FCF yield is **1.14%** and FY2024 FCF was negative. Growth capex (~$1.06bn) absorbs ~86% of operating cash flow. Earnings quality is high; *cash* conversion is poor.
3. **⚠️ Operating leverage is extreme** — 33% of revenue in semi-fixed SG&A means a modest sales miss collapses EBIT (see scenario: −20% revenue → −92% EBIT).
4. **Quick ratio 0.65 / equity-to-assets 0.18** — liquidity and equity cushions are inventory- and lease-dependent; little absolute cushion if inventory must be liquidated at distressed prices.
5. **Negative risk-adjusted returns:** Sharpe 0.068 at a 0% Rf, 40% volatility, −39% drawdown. High idiosyncratic risk not compensated.
6. **Sub-investment-grade into a 5%+ rate environment** — refinancing the ~$2.1bn stack at 10Y 5.13% raises interest cost and constrains the buyback that is already debt-funded.
7. **Covenant trigger in stress:** lease-inclusive leverage of 9.7x under a 20% revenue shock would trip incurrence covenants and lock out buybacks/acquisitions.

---

### Data Gaps (explicit)

- **Debt maturity schedule by year — not obtained.** S&P research page returned **HTTP 403**; FMP does not break maturities out. Cannot confirm the exact near-term wall; ABL revolver size and springing-covenant thresholds also unconfirmed.
- **Moody's / Fitch ratings not verified** — only S&P BB+ retrieved.
- **CDS spreads unavailable** — no direct market-implied default pricing.
- **Sortino ratio not returned** by the volatility tool.
- **Peer comparison unavailable** — `get_sector_peers` returned AMZN, TSLA, HD, TM, BABA, MCD (mega-cap composites), which are **not valid comparables** for an off-price apparel retailer. Proper comps (ROST, TJX, Burlington peers) were not obtainable within budget.
- **Beta conflict unresolved** (1.502 vendor vs 0.949 calculated) — both reported.
- Quarterly trends not reviewed; all analysis is on annual data through the 1/31/26 fiscal year.

*Bottom line: I would underwrite the credit comfortably at BB+ and view the equity risk as elevated — not because the company is fragile, but because it is converting an outstanding operating turnaround into almost no free cash flow while borrowing to buy back stock.*
