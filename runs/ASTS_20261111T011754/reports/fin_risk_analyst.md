# Fin Risk Analyst

- Symbol: ASTS
- Elapsed: 226.5s

---
I have sufficient data. Here is the assessment.

---

# AST SpaceMobile, Inc. (ASTS) — Financial Risk Assessment

**Sector:** Communication Services / Telecommunications Services · **Market cap:** ~$13.76B · **Last price:** $33.69 · **Business:** pre-scale satellite-direct-to-cell network (BlueBird constellation)

> ⚠️ **Data-integrity note up front:** the price-history series returned by my feed ends **2026-02-20** ($80.20 close), while the company profile and filing search reflect **~Nov 2026** ($33.69). The risk statistics below (vol, beta, drawdown) were computed by the tool on its full 504-day window and are consistent with the later price. I use the **profile's $13.76B market cap / $33.69 price** as current and flag the ~58% interim decline as a data-confirmed move rather than a computed one.

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade — Speculative / Pre-Scale Growth Credit** (no public agency rating; CDS unavailable)

ASTS is **not** a conventional credit story. It has essentially no operating earnings to service debt — FY2025 EBIT was **–$421M** and EBITDA **–$370M** — yet it carries **$2.24B of debt** against **$2.34B of cash**. The debt is entirely **low-coupon convertible senior unsecured notes** (coupons of 1.625%, 2.375% and 4.25%, maturities laddered ~2030/2032/2034, with 2032 notes partially repurchased in 2025 and $1.15B of 2034 notes issued July 2026). Three consequences:

- **Interest coverage is negative and meaningless as a default metric.** EBIT/interest = **–7.98x** on $36.1M of interest expense (~1.6% average coupon). The company can *pay* its coupon out of cash; it cannot pay it out of earnings. Coverage is funded by the balance sheet, not the P&L.
- **No financial maintenance covenants.** Convertible notes of this type carry conversion-price and change-of-control provisions, not leverage or coverage tests. **Covenant-breach risk is therefore low** — the risk is dilution and refinancing, not technical default.
- **Near-term default risk is low, medium-term is real.** Net cash at FY2025 was **–$97M net debt** (i.e. net cash). Post the 2026 raises and repurchases, total debt is **~$2.22B** against **~$3.2B cash** at 9/30/26 — roughly **$1.0B net cash**. That is a genuine cushion. But the maturity wall sits in **2030–2034** with the stock at $33.69, far **below** conversion prices ($79.57 on the 2034s, ~$120 on 2032 tranches). The notes are deep out-of-the-money, so they behave as **cash-settled debt**, not quasi-equity. That converts a dilution problem into a **refinancing cliff**.

**Verdict:** solvent today, structurally dependent on capital markets. Credit quality is contingent on execution, not on the current balance sheet.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Read |
|---|---|---|
| **Leverage** | | |
| Total debt (FY25) | $2,239.5M | All convertible notes |
| Total debt (Q3'26, per schedule) | ~$2,219.6M | Repurchases offset new issuance |
| Debt / equity | **0.94x** | Moderate on book; high vs. earnings |
| Debt / assets | **0.45x** | 45% asset-financed by debt |
| Net debt / EBITDA | **0.26x** | Not meaningful — EBITDA is negative; company is **net cash** |
| **Coverage** | | |
| EBIT / interest | **–7.98x** | No earnings-based debt service capacity |
| Operating margin | **–405.7%** | Revenue base is still negligible |
| **Liquidity** | | |
| Current ratio | **16.35x** | Exceptional — cash-rich, minimal current liabilities |
| Quick ratio | **16.27x** | Inventory negligible |
| Cash ratio | **15.54x** | Cash $2,335.7M vs. current liabilities $150.3M |
| Working capital | **$2,308.2M** | 94% of current assets is cash |
| Cash / total liabilities | **0.89x** | Cash covers 89% of *all* liabilities |
| Equity / assets | **0.48x** | |
| Assets / liabilities | **1.91x** | |
| **Distress scores** | | |
| Altman Z-Score (book equity) | **0.605 — Distress** | Mechanically penalized by pre-revenue losses |
| Altman Z-Score (market-cap X4) | **~3.20 — lower edge of safe zone** | Using $13.76B mkt cap |
| Altman Z-Score (at $8.62B mkt cap) | **~2.03 — grey zone** | Sensitivity to market cap |
| Piotroski F-Score | **5 / 9 — Moderate** | See component detail |
| **FCF** | | |
| FCF FY2025 | **–$1,136.3M** | Capex-driven, not opex-driven |
| FCF yield (on $13.76B) | **–8.3%** | Tool printed –13.18% on a stale $8.62B cap |
| Revenue FY2025 | $70.9M | +1,505% YoY (from $4.4M) |

**Piotroski component detail:** positive ROA ✗ · positive operating CF ✗ · ROA improvement ✓ · accruals quality ✓ · lower leverage ✗ · positive equity change ✓ · no dilution ✗ · gross margin improvement ✓ · asset-turnover improvement ✓.

The **5/9 masks two opposing stories**. The ✗ marks on ROA and operating cash flow are structural (pre-profitability), but the ✗ on **leverage** and **dilution** are *choices* — the company levered up 13x and diluted shares ~60% in a single year. The ✓ marks on margin and asset turnover are real: gross margin went from **–133%** in FY2024 to **+53.4%** in FY2025 as revenue became commercial.

**Critical operating trend most analysts miss:** *operating* cash burn is **narrowing** (–$156M FY22 → –$149M FY23 → –$126M FY24 → **–$71.5M** FY25), while *total* FCF is **exploding** (–$214M → –$268M → –$300M → **–$1,136M**). The deterioration is **entirely capital expenditure**: capex went from $174M (FY24) to **$1,065M** (FY25), a 6.1x step-up. This is a deliberate build-out, not operational decay — an important distinction, but it does not reduce the funding requirement.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualized volatility (504d) | **103.67%** |
| Beta vs. SPY (computed) | **3.428** |
| Beta (provider 5-yr regression) | 2.847 |
| Max drawdown (504d) | **–77.31%** |
| Sharpe ratio (0% rf) | **0.716** |

This is a **top-decile risk profile**. At 104% annualized vol, one-day 95% VaR is roughly **–10.7%** and one-day 99% VaR roughly **–15.2%**. A beta of 3.43 means a **10% S&P drawdown mechanically implies ~34% downside** in ASTS — before any company-specific news. The observed 77.31% peak-to-trough drawdown is not a tail scenario; it is the realized base case within the measurement window. The 0.716 Sharpe is respectable only because the trailing period captured a very large rally; it is not evidence of risk-adjusted quality, it is evidence of high variance with positive drift.

The price path confirms this: the stock ran from ~$2 to a 2026 high near **$130**, and now trades at **$33.69** — a **~74% decline from peak**. Liquidity in the shares is adequate (recent daily volume 8–30M shares), so the risk is valuation volatility, not exit liquidity.

---

## 4. Downside Scenario Analysis

**The key framing:** a 20% revenue decline is **not** the binding risk for this company. FY2025 revenue of $70.9M is **0.5% of market cap** and **6% of annual cash burn**. Cutting revenue 20% destroys ~$14M of gross profit against a $1.1–1.8B annual cash outflow. The real downside case is a **financing/execution shock**, so I model revenue stress alongside capex and funding stress.

| Scenario | Revenue | Capex | FCF | Cash end | Runway |
|---|---|---|---|---|---|
| **Base FY2026E** | $175M (guidance mid) | ~$1.55B | ~–$1.80B | ~$3.2B → ~$1.4B | ~21 mo |
| **A. Revenue –20%** | $140M | ~$1.55B | ~–$1.83B | ~$1.37B | ~20 mo |
| **B. –20% rev + 30% capex overrun** | $140M | ~$2.0B | ~–$2.28B | ~$0.92B | ~14 mo |
| **C. Guidance miss + 12-mo launch delay** | ~$100M | ~$1.9B | ~–$2.2B | ~$1.0B | ~13 mo |
| **D. Market shock (SPY –20%, β 3.43)** | – | – | – | – | equity –68% |

**Scenario A — Revenue –20%.** Gross profit falls from ~$87M to ~$70M; operating loss widens ~$17M to ~–$390M; net loss ~–$450M; FCF ~–$1.83B. Cash runway shortens from ~21 to ~20 months. **Financially immaterial** — the company's solvency does not hinge on revenue at this stage. The revenue line matters for *narrative and valuation*, not for *liquidity*.

**Scenario B — Revenue stress plus capex overrun.** This is where it bites. A 30% capex overrun (plausible given Q3'26 guidance of $350–425M per quarter and
