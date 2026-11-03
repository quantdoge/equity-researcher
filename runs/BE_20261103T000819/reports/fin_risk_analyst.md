# Fin Risk Analyst

- Symbol: BE
- Elapsed: 49.7s

---
# BE (Bloom Energy) — Financial Risk Assessment
**Analyst: Financial Risk Desk | Data as of Q3 2026 (period ended 30-Sep-2026); price $196.25, market cap ~$58.0B**

> **Critical data note:** The automated ratio tools (`calculate_leverage_ratios`, `calculate_liquidity_ratios`, `calculate_altman_z_score`, `calculate_piotroski_f_score`, `calculate_fcf_yield`) anchor on the **FY2025 annual (31-Dec-2025)** filing. BE's financials have transformed materially across the four quarters since. I present both the tool outputs **and** a TTM (Q4'25–Q3'26) restatement built directly from quarterly filings. Where they conflict, the TTM view governs.

---

## 1. Credit Risk Assessment

**Rating: Investment-Grade-like on current balance-sheet metrics — but effectively unrated, with a sub-investment-grade track record.**

BE's solvency profile has inflected sharply. On FY2025 data BE looked leveraged and fragile (net debt/EBITDA **26.8x**, interest coverage **1.35x**, D/E **3.77x**). Nine months later, on TTM 2026 data, it is conservatively financed:

| Metric | FY2025 (tool) | TTM Q3'26 (restated) |
|---|---|---|
| Net debt / EBITDA | 26.8x | **0.48x** |
| EBIT / interest | 1.35x | **15.8x** |
| Debt / equity | 3.77x | **1.42x** |
| Debt / assets | 0.68 | **0.42** |
| Cash | $2.45B | **$2.49B** |
| Net debt | $538M | **$295M** |

The deleveraging is genuine, not cosmetic: it is driven by EBITDA expansion (TTM EBITDA ~$616M; Q3'26 non-GAAP adjusted EBITDA $299M, up from $59M a year earlier) plus a $2.2B 0%-coupon convertible raise (Nov-2030) that pushed cash to ~$2.5B and cut cash interest expense from $10.6M to **$7.5M per quarter**.

**Refinancing cliff: none.** Total debt $2.78B is almost entirely long-dated converts — $2.2B **0% due Nov-2030**, ~$550M **2.50% green converts due Jun-2028**, and 3.00% green converts due 2029. Short-term debt is just **$45.7M**. There is no maturity inside 2027 and no meaningful 2028 wall relative to a $2.5B cash balance. Convertible indentures carry no meaningful financial maintenance covenants.

*Data gaps:* No public credit rating or CDS spread available in my feeds; revolver/term-loan capacity and covenant terms not disclosed in the pulled data.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Net debt/EBITDA | 0.48x | Very conservative |
| Interest coverage (EBIT/int.) | 15.8x | Strong |
| Current ratio | **3.74x** (tool FY25: 5.98x) | Ample |
| Quick ratio | **3.07x** (tool: 4.95x) | Ample; inventory $928M is 18% of current assets |
| Cash ratio | **1.79x** (tool: 3.93x) | $2.49B cash |
| Working capital | **$3.82B** | Positive, expanding |
| Altman Z — book equity | **1.08** (tool FY25: **0.148**) | Distress zone — but distorted |
| Altman Z — market equity | **~8.4** | Safe zone |
| Piotroski F | Tool: **4 (weak, FY25)**; analyst-restated TTM: **~8 (strong)** | Turnaround, one year old |
| FCF yield | **0.76%** TTM (tool FY25: 0.12%) | Thin vs price |
| FCF margin | **11.5%** TTM | Improving but volatile |
| Gross margin trend | 29.2% → 30.8% → 30.0% → 33.4% → **33.8%** | Clear uptrend |
| Operating margin TTM | 14.8% (Q3'26: 18.2% GAAP, 23.1% non-GAAP) | Inflecting |
| Cash runway | Not meaningful — OCF **+$694M** TTM | No burn |

**On the Altman Z-score:** the 0.148 reading is a genuine artifact of BE's **-$3.47B accumulated deficit**, which crushes the x2 term (-0.53) and the book-equity x4 term. Substituting the $58B market cap for book equity lifts Z from ~1.08 to ~8.4. Neither number should be taken at face value: the book version overstates distress (the retained-earnings deficit is a legacy of the 2019–2023 losses, not current earning power), and the market version overstates safety (it embeds a 15x-sales valuation). I treat bankruptcy probability as **low on cash-flow grounds** and disregard the raw Z reading.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **106.6%** — extreme |
| Beta vs SPY (756d) | **2.33** (company-reported 5Y beta: **3.78**) |
| Max drawdown (3Y) | **-52.7%** |
| Sharpe (0% rf, approx) | **1.83** |
| Sortino | Not computed by tool — **data gap** |
| 52-week position | Near highs; added to S&P 500 in 2026 |

This is the dominant risk in the name. A 106% annualised vol with a 2.3–3.8 beta means a **20% S&P drawdown plausibly translates to a 45–75% BE drawdown**. The -52.7% three-year max drawdown was recorded on a far smaller, loss-making base; the equity now carries a much richer multiple, so the drawdown asymmetry is worse, not better. The 1.83 Sharpe is a momentum artifact, not evidence of low risk.

**Valuation as a risk metric:** ~15x TTM revenue (12.9x FY26 guidance midpoint of $4.5B), ~60x midpoint non-GAAP EPS ($3.10–3.40), and roughly 50–95x EV/EBITDA depending on GAAP vs adjusted measure. At this multiple, the equity is priced for sustained triple-digit growth; the margin of safety is in the growth assumption, not the balance sheet.

---

## 4. Downside Scenario: Revenue −20%

Applied to FY2026 guidance midpoint of **$4.5B** → revenue **$3.6B** (still +78% YoY, i.e., a growth *deceleration* shock, not a collapse).

| Line | Base ($4.5B) | Stress (−20%) |
|---|---|---|
| Revenue | $4,500M | $3,600M |
| Gross margin | ~34% | 31% (−300bps mix/absorption) |
| Gross profit | $1,530M | $1,116M |
| Opex (non-GAAP) | ~$700M | ~$700M (sticky) |
| Operating income | ~$1,000M | ~$416M |
| Interest | ~$36M | ~$36M |
| Pre-tax / net (NOL shield) | ~$960M | **~$380M** |
| Non-GAAP EPS | ~$3.25 | **~$1.17** (−64%) |
| Net debt/EBITDA | ~0.2x | ~0.6–0.8x |
| Liquidity | $2.49B cash | $2.49B + WC release of ~$300M |

**Conclusions:**
- **Solvency is essentially unaffected.** BE remains profitable, cash-generative and net-cash-ish through a 20% revenue miss. No covenant, no maturity, no liquidity event.
- **The equity is where the damage lands.** EPS roughly two-thirds lower, and a de-rating from ~60x to a growth-shock multiple of even 25x on $1.17 of EPS implies a share price near **$29** — an ~85% decline. That is the realistic downside, and it is a *valuation* event, not a credit event.
- A **40%** revenue shock still leaves ~$100M of operating income and no refinancing pressure; the converts are equity-linked and long-dated, so even a severe compression is survivable at the enterprise level.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split explicitly:
- **Credit / liquidity / solvency risk: LOW.** Net leverage 0.48x, coverage 15.8x, $2.49B cash, 3.7x current ratio, no maturities before 2028 and none material inside 2030.
- **Market / valuation / equity-price risk: VERY HIGH.** 106% vol, 2.3–3.8 beta, 15x sales, 60x earnings, a business model one-year into profitability and concentrated in a single end-market.

The blended rating is **Moderate**, but the composition matters: this is not a company at risk of failing — it is an equity at risk of halving on a sentiment shift.

---

## 6. Key Red Flags

1. **Cash conversion is deteriorating even as earnings surge.** Q3'26 FCF was **−$181M** versus net income of **+$249M**, driven by a **−$356M working-capital build** and capex jumping to **$154M** in the quarter (vs $23–52M previously). Inventory reached **$928M (+71% YoY)** and receivables **$635M**. TTM FCF of $440M against a $58B cap yields **0.76%** — the company is not yet self-funding its growth from operations at scale.
2. **Earnings quality.** Q3'26 included **$24.8M of non-operating income** (a swing from $30.9M of expense a year prior) and a minimal tax charge; non-GAAP operating income ($286M) exceeds GAAP ($225M) by 27%. Watch for adjusted-versus-GAAP drift.
3. **Equity dilution overhang.** Basic shares 240M → **295M**, diluted **324M (+10%)**. The $2.2B 0% 2030 converts and the 2028/2029 green converts are likely well in the money after the 2026 rally; full conversion could add materially to the count. *Conversion prices not confirmed in my data — flag as a gap.*
4. **Customer and end-market concentration.** Third-party commentary cites **~43% customer concentration** and backlog of ~$20B at the start of 2026 — a backlog figure I could **not independently verify** from filings within this review. Dependence on hyperscaler/AI-datacenter capex is the single largest demand risk.
5. **The turnaround is one year old.** Interest coverage was **1.35x** as recently as FY2025. The improvement has not been tested through a demand cycle, a rate shock, or a hyperscaler capex pause.
6. **Negative retained earnings of $3.47B** keeps book-equity Altman Z in the distress zone (1.08) and leaves limited book cushion — though this is largely a legacy artifact.

**Explicit data gaps:** no credit rating or CDS; no revolver capacity/covenant detail; Sortino not computed; convert conversion prices unconfirmed; customer concentration figure unverified; **peer benchmarking unavailable** — `get_sector_peers` returned broad Industrials conglomerates (GE, CAT, RTX, GEV, UNP, DE, LMT) that are not meaningful comparables for a fuel-cell manufacturer, so no peer leverage benchmarking was performed.
