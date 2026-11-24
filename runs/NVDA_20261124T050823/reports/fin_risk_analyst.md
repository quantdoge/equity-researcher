# Fin Risk Analyst

- Symbol: NVDA
- Elapsed: 67.4s

---
## NVDA — Financial Risk Assessment
*Data as of FY2026 (period ended 2026-01-25) plus quarterly through Q3 FY2027 (2026-10-25). Price/market data ~2026-11-24.*

---

### 1. Credit Risk Assessment → **INVESTMENT GRADE (Aa1 / Prime-1)**

NVIDIA is a **net-cash company with no meaningful credit risk**. Moody's affirmed Aa1 senior unsecured and Prime-1 CP ratings in Aug 2026; the outlook was cut to **stable from positive in Nov 2026 on governance concerns following CEO Jensen Huang's ouster** (see §6 — flagged as unverified, sources paywalled).

- Total debt $11.41B vs. cash & ST investments **$62.56B → net cash ~$51.1B**
- Net debt / EBITDA: **−0.35x** (negative = net cash)
- Interest coverage: **503x** (tool); **547x** on reported interest expense of $259M ($141.7B EBIT)
- Debt / equity **0.07**, debt / assets **0.06**
- Altman Z-Score **6.75 — Safe zone** (and understated: x4 uses book equity of $157.3B, not the ~$4.0T market cap; market-cap-based Z would be far higher)

There is no refinancing cliff: short-term debt is **$0.999B** against $62.6B of cash. A covenant breach is not a realistic scenario.

---

### 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Revenue (FY26) | $215.9B (+65% YoY) | Explosive growth |
| Gross margin | 71.1% (vs 75.0% FY25) | **−392bp — compressing** |
| Operating margin | 60.4% | Exceptional |
| Net debt / EBITDA | **−0.35x** | Net cash |
| Debt / equity | 0.07 | Negligible |
| EBIT / interest | **503x** | No credit stress |
| Current ratio | **3.91** | Very strong |
| Quick ratio | 3.24 | Very strong |
| Cash ratio | 1.94 | Very strong |
| Working capital | $93.4B | — |
| Altman Z-Score | **6.75** | Safe (>2.99) |
| Piotroski F-Score | **5 / 9** | Moderate — see caveat |
| FCF (FY26) | $96.7B | — |
| FCF yield (trailing) | **2.39%** | Thin on trailing |
| FCF / Net income | 80.5% (vs 83.5% FY25) | Mild deterioration |

**Piotroski caveat (important):** the F-Score of 5 is a *growth-accounting artifact*, not deterioration. It loses points on ROA improvement, gross-margin improvement, asset-turnover improvement, and accruals quality — all because the asset base grew 85% and margins normalized off an unsustainable peak. The company still scores full marks on positive ROA, positive operating cash flow, lower leverage, positive equity change, and no dilution.

**Working capital is the one real leak:** change in WC was **−$15.9B** in FY26 vs −$9.4B in FY25. Inventory days rose to ~125 (from ~113) and DSO held ~65. Cash conversion is being taxed by growth, not by collections failure.

---

### 3. Market Risk Profile — **this is where the risk actually lives**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **50.12%** |
| Beta vs SPY | **2.04** (profile: 2.25) |
| Max drawdown (3y) | **47.53%** |
| Sharpe (0% rf) | **0.533** |
| Market cap | ~$3.98T |

- At beta ~2.0–2.25, a 20% S&P drawdown implies roughly a **40–45% NVDA drawdown** on historical sensitivity — consistent with the observed 47.5% max DD.
- The Sharpe of 0.533 is computed at a 0% risk-free rate. Against the **actual 2Y/10Y of 4.74% / 5.13%**, excess-return Sharpe is materially lower — the equity is being paid for its volatility with only modest risk-adjusted compensation.
- The yield curve is **not inverted** (2s10s +39bp), so macro recession signaling is muted — but note the 5.13% 10Y is a high discount rate, which is precisely what punishes a 2.4% trailing FCF yield.

---

### 4. Downside Scenario Analysis — Revenue −20%

*Base: FY26 revenue $215.9B, R&D $18.5B (derived), SGA $4.58B. Assume GM compresses to 65% on pricing pressure and take-or-pay underutilisation; opex held flat.*

| Line item | Base FY26 | Revenue −20% | Severe: −40% | Stress: −55% |
|---|---|---|---|---|
| Revenue | $215.9B | $172.8B | $129.6B | $97.2B |
| Gross margin | 71.1% | 65.0% | 58.0% | 50.0% |
| Gross profit | $153.5B | $112.3B | $75.1B | $48.6B |
| Opex | $23.1B | $23.1B | $21.2B | $19.6B |
| **Operating income** | **$130.4B** | **$89.2B** | **$52.0B** | **$29.0B** |
| Operating margin | 60.4% | **51.6%** | **40.1%** | **29.8%** |
| EBITDA | $144.6B | ~$92B | ~$55B | ~$32B |
| Net debt / EBITDA | −0.35x | **~−0.55x** | more negative | more negative |
| Est. FCF | $96.7B | **~$80–85B** | **~$45B** | **~$22B** |
| FCF yield (on $4.0T) | 2.4% | ~2.1% | ~1.1% | ~0.6% |

**The critical finding:** a 20% revenue decline produces *no financing stress whatsoever* — the company remains net cash, covers interest 300x+, and generates ~$80B+ of FCF. **Operating income does not reach zero until revenue falls roughly 75–80%** (to ~$45–50B). Solvency is effectively unassailable.

**The real downside is valuation, not solvency.** At a $4.0T market cap and a 2.4% trailing FCF yield, a de-rating from ~40x to ~20x earnings does more damage than any plausible revenue shock. In the −40% case, FCF yield stays under 1.5% — the equity has no valuation floor from cash generation at current prices.

**Offsetting note:** on the **latest quarter (Q3 FY27) annualised**, revenue is ~$463B and net income ~$261B — implying a ~6.6% earnings yield and ~5%+ run-rate FCF yield. The trailing multiple materially understates current cash generation, but that run-rate is exactly what the downside case is testing.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Decomposed, because a single blended label misleads here:

| Axis | Rating | Rationale |
|---|---|---|
| Credit / solvency risk | **LOW** | Net cash $51B, Aa1/P-1, Z-score 6.75, 503x coverage |
| Liquidity risk | **LOW** | Current 3.91, cash/liabilities 1.26, no ST refinancing need |
| **Market / equity risk** | **HIGH** | 50% vol, beta 2.0–2.25, 47.5% max DD, thin trailing FCF yield |
| **Governance / key-man risk** | **ELEVATED** | See red flag #1 |

NVDA cannot be killed by its balance sheet. It can lose 40–50% of equity value in a market or sentiment event, and has already done so once in the last three years.

---

### 6. Key Red Flags

1. **Governance / key-man shock (UNVERIFIED — verify immediately).** Moody's cut the outlook to stable from positive in Nov 2026 citing governance concerns following **Jensen Huang's ouster**. Multiple outlets (Bloomberg, Yahoo, StreetInsider) corroborate, but both primary URLs returned 401/403 and I could not confirm from a primary source. **The company profile feed still lists Jensen Huang as CEO**, which is either stale or inconsistent with the reporting. For a company this dependent on one person's roadmap execution and customer relationships, a CEO transition is a first-order credit and equity risk. *Treat as the most important open item in this report.*
2. **Customer concentration.** FY2026: **two customers = 36% of revenue** (Reuters); H1 FY26 disclosures show 20% and 15% direct customers. Claims circulating that the top 4 customers reached ~61% of FY26 revenue, alongside vendor-financing/backstop arrangements for customers' debt, are **unverified** but directionally consistent with hyperscaler-driven demand. A single hyperscaler capex pause is the true −20% trigger.
3. **Off-balance-sheet purchase obligations — the largest unmeasured risk.** Take-or-pay commitments for HBM and CoWoS capacity are not in the data I could retrieve. In a severe downturn these convert from a margin problem into a cash problem, and they are the one mechanism that could break the FCF floor shown in §4.
4. **Gross margin compression: −392bp YoY (75.0% → 71.1%).** Consistent with mix shift and rising input costs. If this trend persists at ~400bp/yr, the margin of safety narrows faster than revenue growth suggests.
5. **Cash conversion softening.** FCF/NI 80.5% (from 83.5%); WC drag doubled to −$15.9B. Growth is consuming more cash per dollar of earnings.
6. **Valuation-as-risk.** 2.39% trailing FCF yield against a 5.13% 10Y Treasury means the equity offers a *negative* spread to risk-free on trailing cash flow. Any rise in the discount rate is an immediate multiple risk.

---

### 7. Data Gaps (explicit)

- **Blocked primary sources:** Reuters (401) and StreetInsider (403) — the CEO-departure/governance item is corroborated only via search-result snippets.
- **No debt maturity schedule** — only ST $0.999B / LT $7.469B. `total_debt` of $11.41B does not reconcile to those two lines (~$2.9B of lease/other debt unaccounted).
- **Net debt field conflict:** the balance sheet returns `net_debt` = +$0.807B, while total debt less cash = **−$51.1B net cash**. I used the latter; the reported figure appears to net against something other than cash.
- **No quarterly cash flow statements** — latest-quarter FCF is inferred from net income, not measured.
- **No peer multiples / CDS spreads** — the sector-peer tool returns tickers only, so no relative leverage comparison was possible.
- **No purchase-obligation or off-balance-sheet commitment data** — the single most important gap for stress-testing the downside case.

**Bottom line:** A fortress balance sheet with effectively zero credit risk, attached to an equity with high market risk, elevated single-name/governance risk, and a valuation that provides no cash-flow downside protection. The risk in NVDA is *price*, not *solvency*. Quantify the exposure through position sizing and beta (2.0–2.25), not through credit analysis.
