# Fin Risk Analyst

- Symbol: NTNX
- Elapsed: 57.2s

---
## NTNX (Nutanix, Inc.) — Financial Risk Assessment
*Data as of Q1 FY27 (quarter ended 10/31/2026, filed 11/24/2026) and closing price $46.30 on 11/25/2026. Fiscal year ends July 31. Yield curve as of 11/27/2026 (10Y 5.13%).*

### 1. Credit Risk Assessment — Rating: **Investment Grade (unrated; balance-sheet equivalent BBB-/BB+)**

Nutanix is a **net-cash** company with strong coverage and no near-term solvency question. FY2026 (ended 7/31/26) delivered revenue of $2,853.5M (+12.4% y/y), GAAP operating income of $278.9M (9.8%), and FCF of $840.7M (29.5% margin). Q1 FY27 accelerated: revenue $772.4M (+15.2% y/y), GAAP operating margin 18.5%, non-GAAP 32.1%, FCF $209.3M, ARR $2.63B (+15–16%).

Leverage is low in economic terms. Gross debt is $1,556.3M, but against cash + short-term investments of $2,467.8M the company holds roughly **$843M of net cash** (7/31/26: net cash $842.7M per the leverage calc). Gross debt/EBITDA on FY26 GAAP EBITDA of $400.6M is 3.9x, but GAAP EBITDA is depressed by $357.7M of SBC; on a cash-EBITDA basis leverage is ~2.0x, and net-cash on any basis. Interest coverage is **31.0x** (tool; 36.7x on EBIT $329.9M / interest $9.0M) because the capital structure is 0.25%/0.50% coupon convertible notes, not fixed-rate term debt.

Two caveats. First, **the credit is not formally rated and there is no CDS market** — a genuine data gap; the "investment grade" label is my balance-sheet inference, not a rating agency opinion. Second, **the equity book was negative ($-694.5M) at 7/31/26 and only turned positive (+$702.6M) in Q4 FY26/Q1 FY27** because of an apparent large **deferred-tax-asset valuation-allowance release**: Q4 FY26 GAAP operating income was $70.0M but net income was $1,269.6M. FY26 "EPS of $5.57" is therefore not a cash-earnings number, and D/E of 2.16x and equity/assets of 0.14 are artifacts of an accumulated deficit (-$3.71B retained earnings), not distress.

### 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | FY2026 | Q1 FY27 |
|---|---|---|---|---|
| Revenue ($M) | 2,148.8 | 2,537.9 | 2,853.5 | 772.4 |
| Rev growth | +15.4% | +18.1% | +12.4% | +15.2% |
| Gross margin | 84.9% | 86.8% | 86.8% | 87.5% |
| GAAP op margin | 0.4% | 6.8% | 9.8% | 18.5% |
| FCF ($M) | 597.7 | 750.2 | 840.7 | 209.3 |
| FCF margin | 27.8% | 29.6% | 29.5% | 27.1% |
| SBC ($M) | 333.8 | 351.6 | 357.7 | 83.8 |
| Cash + ST inv ($M) | 994.3 | 1,992.7 | 2,361.5 | 2,467.8 |
| Total debt ($M) | 695.2 | 1,482.8 | 1,518.7 | 1,556.3 |
| Net debt ($M) | +39.9 | +713.3 | net cash ~-843 | net cash ~-912 |
| Debt/equity | n/m (neg eq) | n/m | 2.16x | 1.89x |
| Debt/assets | 0.32x | 0.45x | 0.30x | 0.30x |
| Interest coverage | ~0.4x (distorted) | 11.2x | 31.0x | n/m (int. ~$0) |
| Current ratio | 1.06x | 1.72x | 1.71x | 1.45x |
| Cash ratio | 0.80x | 1.41x | 1.40x | 1.15x |
| **Altman Z** | — | — | **0.13 (Distress)** | — |
| **Piotroski F** | — | — | **6 / 9 (Moderate)** | — |
| FCF yield | — | — | **6.2%** (6.7% at current cap) | — |

F-score composition (6/9): positives on ROA, operating cash flow, ROA improvement, lower leverage, positive equity change, no dilution; fails on accruals quality (F4), gross-margin improvement (F8), and asset-turnover improvement (F9). The accruals failure is the tax-benefit artifact; F8/F9 reflect the revenue mix shift rather than deterioration.

**Altman Z of 0.131 is a false positive and I would not act on it.** It is driven mechanically by x2 (retained earnings/assets = -0.73) and x4, which the tool scores on *book* equity (0.16). Substituting market cap ($12.63B / liabilities $4.37B = 2.89), the Z rises to roughly 1.5 — still below the 1.81 cutoff, but for an asset-light, negative-working-capital software company whose deficit stems from pre-2021 losses plus SBC, Z-score has poor discriminating power. Cash coverage, coverage ratios, and FCF are the relevant tests here, and all pass.

Liquidity: the current ratio slipped from 1.71x (7/31/26) to 1.45x at 10/31/26 because **short-term debt jumped from $35.7M to $498.7M**. Even if the entire short-term balance came due within twelve months, cash + ST investments of $2,467.8M cover it 4.9x and cover total debt 1.59x. Cash runway is not a meaningful constraint while FCF is positive ~$200M/quarter.

### 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3y daily) | **45.85%** |
| Beta vs SPY (3y daily, calculated) | **1.165** |
| Beta (profile, 5y monthly) | 0.638 |
| Max drawdown (3y) | **-58.58%** |
| Sharpe (3y, rf = 0%) | **-0.01** |

The equity is a high-beta, high-volatility instrument: a one-standard-deviation year is ±46%, and the security has drawn down nearly 59% within three years. The three-year Sharpe of approximately zero means the stock has delivered roughly no return for volatility far above the market — and with the 10Y at 5.13%, holding NTNX over that window destroyed risk-adjusted value versus Treasuries.

Momentum has deteriorated sharply. From a 10/12/2026 close of $74.14 (intraday high $75.98), the stock is down ~39% to $46.30. **On 11/25/2026 it fell 15.2% on 13.6M shares (~5x normal volume)** after Q1 beats: CEO Rajiv Ramaswami announced he will step down, and FY27 guidance of $3.180–3.230B revenue (implying 11–13% growth vs 15.2% just delivered) and Q2 guidance of $820–830M came in ~1.3% below consensus, alongside a more "measured" FCF outlook. That is a leadership/execution risk event, not a credit event — but it materially widens the equity's risk premium and, at 5.1% risk-free rates, leaves little room for multiple support if growth decelerates further. Note the beta discrepancy between sources (1.165 on 3y daily vs 0.638 on 5y monthly); I weight the calculated 3y figure for near-term risk.

### 4. Downside Scenario: Revenue −20%

Applied to a FY27E base of ~$3,205M (guidance midpoint), with 87.5% gross margin and annualised GAAP opex of ~$2,133M:

| Line | Base FY27E | −20% Revenue | −35% Severity |
|---|---|---|---|
| Revenue | $3,205M | $2,564M | $2,083M |
| Gross profit (87.5%) | $2,804M | $2,244M | $1,823M |
| Opex (flat / -10% / -20%) | $2,133M | $1,920M–2,133M | $1,706M |
| GAAP op income | ~$670M | **+$111M to +$324M** | **~+$117M** |
| FCF (est.) | ~$750–850M | **~$250–350M (10–14% margin)** | ~$0–100M |
| Interest coverage | >50x | **9x–27x** | ~10x |
| Cash + ST inv | $2.47B | ~$2.4B | ~$2.2B |
| Net debt position | net cash ~$0.9B | **still net cash** | **still net cash** |

The structural reason the downside is contained: an 87.5% gross margin plus a subscription/renewal revenue base means a 20% revenue shock is absorbed largely in gross profit, not in a liquidity hole, and SBC-heavy opex flexes. **Even at −35% revenue the company remains GAAP profitable, FCF-positive-to-breakeven, and in a net-cash position.** There is no covenant risk of consequence: the outstanding debt is unsecured low-coupon convertible notes (notably $862.5M of 0.50% notes due December 2029), which do not carry the maintenance covenants a leveraged loan would. The real downside transmission channel is **equity valuation and dilution**, not solvency: at $46.30 the converts appear out of the money (basic 271.7M vs diluted 294.6M shares), so a further decline dilutes nobody but also removes the cheap-financing option, and any refinancing in a 5.1% 10Y environment would raise cash interest from ~$9M to $40M+ annually on $1.3B — still only ~6% of current FCF.

### 5. Overall Financial Risk Rating: **Low-to-Moderate** (credit: Low; market/equity risk: High)

On the three lenses asked of me: **credit risk is Low** (net cash, 31x coverage, 30% FCF margins, no maturities before Dec 2029), **liquidity risk is Low** (current ratio 1.45x, cash covers total debt 1.6x, positive quarterly FCF), and **market risk is High** (46% vol, 1.17 beta, −59% max drawdown, ~0 Sharpe, plus a fresh CEO-succession overhang). Net, the company can comfortably survive a prolonged downturn; the shareholder cannot necessarily survive a prolonged multiple compression.

### 6. Key Red Flags & Data Gaps

**Red flags**
1. **CEO departure announced with soft FY27 guidance** (11/25/26, -15.2% on 5x volume). Execution/leadership risk on top of a decelerating growth profile (18.1% → 12.4% → guided 11–13%).
2. **Earnings quality:** FY26 net income of $1,506.8M vastly exceeds GAAP operating income of $278.9M; Q4 FY26 net income $1,269.6M vs operating income $70.0M. This looks like a one-time deferred-tax valuation-allowance release, not operating earnings *(inferred — not verifiable from the data feeds; flagging explicitly)*. Reported EPS $5.57 and D/E 2.16x should both be disregarded.
3. **Short-term debt reclassification:** $35.7M → $498.7M between 7/31/26 and 10/31/26. Composition unconfirmed; the identified converts mature Dec 2029, so this likely reflects either a separate maturity or classification of convertible notes as current. Not a liquidity threat given $2.47B cash, but unresolved.
4. **SBC at 12.5% of revenue** ($357.7M FY26) — FCF margin falls from 29.5% to ~16.9% ($483M) on a fully loaded basis. The F-score's accrual and dilution flags are consistent with this.
5. **High rates:** 10Y at 5.13% (2s10s +39bp, no inversion) raises both the discount rate on a 30x-ish FCF multiple stock and future refinancing cost.
6. FY2024 interest expense of $169.4M versus $64.1M in FY2023 and $19.7M in FY2025 appears anomalous (likely induced-conversion/note-settlement charges), which distorts coverage ratios across that window.

**Data gaps:** no credit rating or CDS spread (unrated issuer); no covenant or debt-maturity-schedule detail; conversion prices of the 2029 notes unknown; the FY26 tax-benefit item is inferred; peer multiples unavailable — the sector-peer feed returns only mega-caps (AAPL, MSFT, NVDA, TSM, AVGO), which are not valid comparables for a ~$12.6B infrastructure-software name; beta inconsistent across sources (1.165 calculated vs 0.638 reported).

**Bottom line for the memo:** NTNX's balance sheet is not the risk. With net cash of ~$843M, 31x interest coverage, a 29.5% FCF margin and no maturity wall before 2029, the company survives a 20% (even 35%) revenue decline while remaining profitable and net-cash. The risk is entirely in the equity: 46% volatility, a 1.17 beta, a 59% three-year drawdown, a zero Sharpe against 5.1% risk-free yields, and now a CEO transition landing alongside decelerating growth. Underwrite this as an **equity-duration risk, not a credit risk.**
