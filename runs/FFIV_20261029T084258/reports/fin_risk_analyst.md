# Fin Risk Analyst

- Symbol: FFIV
- Elapsed: 30.3s

---
# FFIV (F5, Inc.) — Financial Risk Assessment

**Sector:** Technology / Software – Infrastructure | **Price (profile):** $365.53 | **Market cap:** ~$20.7B | **Net cash:** $1.38B
**Fiscal reference:** FY2026 (period ended 2026-09-30)

> **Data note:** The `calculate_price_volatility` tool is not available on the current subscription (FMP `dividend-adjusted` endpoint). Market-risk metrics below are **computed manually** from 3+ years of daily OHLCV (Jan-2023 → Feb-2026), sampled at month-ends (37 monthly returns, annualised by √12). There is also a **price inconsistency**: the company profile reports $365.53 while the latest price-history close is $278.39 (2026-02-20) — a +31% gap. Market-risk metrics use the price-history window; valuation ratios use the profile market cap.

---

## 1. Credit Risk Assessment

### **Rating: INVESTMENT GRADE (effectively AAA-profile balance sheet)**

F5 carries **$212M of total debt** against **$1.59B of cash** — a **net cash position of $1.378B**. Debt/equity is **0.05** and debt/assets **0.03**. Critically, the FY26 balance sheet shows **$0 short-term debt and $0 long-term debt**; the $212M "total debt" is operating-lease-type obligation, not funded borrowings. There is **no refinancing cliff** and no debt maturity schedule of consequence.

The income statement reports **interest expense of $0**, so the standard interest-coverage ratio returns `null`. This is not a data failure that hides weakness — it is a structural absence of interest burden. Coverage is effectively **infinite**; a -20% revenue shock would not create a solvency event.

This is a rare credit profile: an unencumbered, net-cash, high-gross-margin software company. Bankruptcy probability is negligible on any fundamental basis.

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|---|
| **Leverage** | | | | | |
| Total debt / equity | 0.05 | 0.14 | 0.15 | 0.19 | Deleveraging every year |
| Net debt / EBITDA | **−1.45x** | −0.96x | −0.79x | −0.43x | Net cash, improving |
| Debt / assets | 0.03 | 0.08 | 0.08 | 0.10 | Negligible |
| **Coverage** | | | | | |
| EBIT / interest | n/a (int. exp = $0) | n/a | n/a | n/a | **Effectively infinite** |
| **Liquidity** | | | | | |
| Current ratio | 1.73 | 1.54 | 1.39 | 1.23 | Improving trend |
| Quick ratio | 1.59 | 1.50 | 1.34 | 1.20 | No inventory dependence |
| Cash ratio | 0.88 | 0.83 | 0.72 | 0.55 | $1.59B cash |
| Cash / total liabilities | 0.52 | 0.49 | 0.43 | 0.33 | Strong |
| Working capital | $1.328B | $0.869B | $0.587B | $0.345B | Nearly 4x'd in 3 yrs |
| **Solvency scores** | | | | | |
| Altman Z-Score | **2.68** (Grey) | — | — | — | ⚠️ Misleading — see below |
| Altman Z (market-cap adjusted) | **~6.0** (Safe) | — | — | — | x4 = 6.77, not 1.31 |
| Piotroski F-Score | **6 / 9** (Moderate) | — | — | — | Solid, not pristine |
| Assets / liabilities | 2.31 | 2.32 | 2.26 | 2.14 | Stable |

**On the Altman Z-Score:** the tool's 2.683 "Grey" reading is an **artifact of using book equity**. The model deliberately substitutes book equity for market cap in x4, which for FFIV is severely punitive: book equity is only $4.01B versus $20.7B market cap, largely because ~$1.95B of cumulative buybacks have shrunk the equity account. Substituting market cap, x4 rises from 1.31 to **6.77**, lifting the Z-score to approximately **6.0 — deep in the safe zone**. I treat the 2.68 reading as non-informative for this company.

**Piotroski 6/9** is the more honest signal. Points lost on **ROA improvement (F3 = 0)**, **lower leverage (F5 = 0)**, and **asset turnover improvement (F9 = 0)** — all mechanical consequences of a rising cash pile (which dilutes asset turnover and ROA denominators) rather than deterioration. Earned all 4 profitability points and 2 of 3 efficiency points. No solvency-relevant weakness.

---

## 3. Market Risk Profile

| Metric | Value | Context |
|---|---|---|
| **Annualised volatility** | **~26.8%** | In line with large-cap software; moderate |
| **Beta (vs market, 5Y)** | **1.03** | Essentially market-neutral sensitivity |
| **Max drawdown (3Y)** | **−34.6%** (close-to-close) | Peak $342.58 (2025-10-08) → trough $223.99 (2025-11-19) |
| **Sharpe ratio** | **~0.91** | 24.3% annualised return / 26.8% vol (0% RF) |
| **Sortino ratio** | **~1.46** | Downside dev 16.7% — 13 down months of 37 |
| **3Y price CAGR** | **+23.2%** | $144.85 → $278.39 |

**Interpretation:** Beta of 1.03 means FFIV offers **no meaningful diversification against a market drawdown** — it falls roughly in line with the index. But the volatility profile is the more notable feature: at ~27%, FFIV is **below** typical high-growth infrastructure software (often 35–45%), reflecting a mature, cash-generative business with a hardware component and a large buyback absorbing float.

The **−34.6% drawdown in Oct–Nov 2025** is the critical tail observation. Note the concentration of that move: **2025-10-16 alone fell from $330.75 to $295.35 (−10.7%) on 3.0M shares**, and **2025-10-28 fell a further −7.9%**. This was a single-event repricing (earnings/guidance shock), not a slow bleed. The stock then recovered from $224 to $278 (+24%) within three months, and the profile price of $365 implies a further ~31% advance — meaning the drawdown has been fully erased. **Gap risk around earnings is the dominant market risk for this name, not leverage.**

**Sortino > Sharpe** confirms downside volatility is materially lower than total volatility — the fat tail is to the upside, and negative months are less severe than positive ones.

---

## 4. Downside Scenario Analysis

Base FY26: Revenue $3,417M · Gross margin 82.2% · Op income $818M (23.9%) · Net income $722M · FCF $869M · Net cash $1,378M

| Scenario | Revenue | Gross Profit | Op Income (% mgn) | Net Income | FCF (% mgn) | Cash Position |
|---|---|---|---|---|---|---|
| **Base** | $3,417M | $2,809M | $818M (23.9%) | $722M | $869M (25.4%) | +$1.38B net cash |
| **−20% revenue** | $2,733M | $2,247M | **$256M (9.4%)** | ~$200M | **~$490M (17.9%)** | +$1.38B net cash |
| **−20%
