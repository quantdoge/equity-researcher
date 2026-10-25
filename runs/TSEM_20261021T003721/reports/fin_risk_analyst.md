# Fin Risk Analyst

- Symbol: TSEM
- Elapsed: 71.4s

---
## TOWER SEMICONDUCTOR (TSEM) — FINANCIAL RISK ASSESSMENT

**Company:** Independent analog/mixed-signal foundry, Israel (Migdal Haemek), FY-end Dec. Market cap ≈ $20.7B, price $183.78, 5,613 employees.
*All figures USD; FY2025 = period ended 2025-12-31.*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (balance-sheet basis)**

Tower carries **net cash of $990.4M** (total debt $161.5M vs. cash & ST investments $1,151.9M). Net debt/EBITDA is **–1.82x**. There is no meaningful credit risk in the conventional sense: debt is 5% of assets and 6% of equity, equity funds 87% of the balance sheet, and interest expense fell to **zero** in FY2025 (from $5.9M in FY2024) as debt was repaid. FY2025 EBIT of $240.4M against ~nil interest makes interest coverage effectively **infinite/not meaningful** (FY2024 coverage was 41x on $5.9M interest).

Altman Z-Score of **5.41** puts TSEM deep in the safe zone (>2.99) — and this *understates* true safety: the model's x2 (retained earnings/assets) reads **0.0** due to a null retained-earnings field, and x4 uses book rather than market equity. Both errors are conservative in the *wrong* direction, so treat Z as a floor.

**Caveat:** no agency credit rating or CDS spread is available from the data feed — that is a genuine gap, not evidence of strength. My grade rests on reported balance-sheet data only.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Total debt | $161.5M | $180.8M | $231.6M | Deleveraging |
| Cash & ST inv. | $1,151.9M | $1,218.2M | $1,235.2M | Declining 3 yrs |
| Net debt (cash) | **–$990.4M** | –$1,037.4M | –$1,003.6M | Net cash |
| Debt / equity | 0.06x | 0.07x | 0.10x | Very low |
| Net debt / EBITDA | –1.82x | –2.30x | –1.18x | Net cash |
| Interest coverage | n.m. (nil interest) | 41x | 133x | No burden |
| Current ratio | 6.48x | 6.18x | 6.17x | Exceptional |
| Quick ratio | 5.51x | — | — | Exceptional |
| Cash ratio | 4.37x | — | — | Exceptional |
| Working capital | $1,445.9M | $1,475.2M | $1,432.3M | Ample |
| Altman Z | **5.41** (Safe) | — | — | Safe zone |
| Piotroski F | **6 / 9** (Moderate) | — | — | Middling |
| Gross margin | 23.2% | 23.6% | 24.8% | **Compressing** |
| Operating margin | 12.4% | 13.3% | 38.5%* | Weak ex-one-off |
| EBITDA margin | 34.7% | 31.4% | 59.6%* | Capex-heavy model |
| FCF | **–$41.1M** | +$12.5M | +$232.1M* | **Deteriorating** |
| FCF yield | **–0.2%** | — | — | Nil/negative |

*\*FY2023 includes the large one-off Intel Foundry termination payment (~$353M) — FY2023 margins and FCF are not comparable. This base effect is why Piotroski F3 (ROA improvement) scores 0.*

**Piotroski detail (6/9):** Earned — positive ROA, positive operating cash flow, accrual quality, lower leverage, positive equity change, asset-turnover improvement. Lost — no ROA improvement (2023 base effect), **share dilution** (113.6M vs 111.2M shares), no gross-margin improvement.

---

### 3. Market Risk Profile — **HIGH**

| Measure | Value | Note |
|---|---|---|
| Annualised vol (756d) | 67.0% | |
| Annualised vol (504d) | 72.9% | |
| Annualised vol (252d) | **87.7%** | Unstable across windows |
| Beta vs SPY (756d / 252d) | 2.04 / 3.05 | **Inconsistent** |
| Beta vs SMH (504d) | 1.31 | Sector beta more credible |
| Static beta (profile) | 0.889 | Conflicts with computed |
| Max drawdown | **45.8%** | 42.0% on shorter windows |
| Sharpe (756d / 252d) | 1.37 / 1.05 | Decent but vol-driven |
| Sortino | not available | Data gap |

**⚠ Data-integrity flag:** the price series produces wildly inconsistent risk statistics — volatility of 67% / 73% / 88% and beta of 0.89 / 1.31 / 2.04 / 3.05 depending on window and benchmark. A 88% realised vol is implausible for a $20B foundry with 0.89 static beta; this pattern is consistent with a price-adjustment discontinuity (corporate action or stale/bad adj_close) rather than genuine risk. **I would not underwrite the 2.04–3.05 beta figures.** The robust observations are directional: TSEM is a high-beta semiconductor cyclical carrying a **~42–46% peak-to-trough drawdown** in the last three years. Plan for a 40%+ drawdown scenario, and re-derive vol/beta from a clean price series before using these in a risk model.

---

### 4. Downside Scenario: Revenue –20%

Revenue $1,566.1M → **$1,253M**. Foundry COGS ($1,202M, 76.8% of revenue) is fixed-cost heavy, so decremental margins are poor — I assume a ~35% contribution margin on lost revenue, consistent with fab-utilisation leverage.

| Line | Base FY2025 | **–20% revenue** | –35% (severe) |
|---|---|---|---|
| Revenue | $1,566M | $1,253M | $1,018M |
| Gross profit | $364M (23.2%) | ~$255M (20.4%) | ~$176M (17.3%) |
| Opex (SG&A $83M + R&D ~$87M) | ~$170M | ~$165M | ~$160M |
| **EBIT** | **$194M** | **~$90M** | **~$16M** |
| EBITDA (+$303M D&A) | $543M | ~$390M | ~$320M |
| Interest expense | $0 | ~$0 | ~$0 |
| Net income (est.) | $220M | ~$100M | ~$40M |
| FCF (capex held at $437M) | –$41M | **~–$150M** | ~–$230M |
| Net cash position | $990M | **~$840M** | ~$760M |

**Verdict: the company survives comfortably.** Even in the severe case, EBITDA stays ~$320M, interest cost is zero, and cash of $1.15B is never at risk. Cash runway under a –20% scenario with full capex is roughly **6–7 years**; at the trough the company could defer capex (currently 27.9% of revenue) and turn FCF positive within one to two quarters. **No covenant breach is plausible** — net cash, 6.5x current ratio, and no secured leverage.

The real downside is **equity, not solvency.** With EBIT down ~55% in the –20% case and ~92% in the severe case, and a stock that has historically drawn down 42–46%, a 20% revenue shock maps to a plausible **40–55% equity drawdown**. That is a market-risk event, not a credit event.

---

### 5. Overall Financial Risk Rating: **LOW**

Split assessment, because the aggregate number hides the two-sided risk:
- **Credit risk: Low.** Net cash, Z 5.41, coverage n.m., 6.5x current ratio.
- **Liquidity risk: Low.** $1.15B cash, $1.45B working capital, $28M of debt due short-term.
- **Market risk: High.** 42–46% max drawdown, high beta, cyclical end-markets.
- **FCF sustainability: Moderate-to-High concern.** FCF has fallen from +$232M (FY2023) to **–$41M**, with capex at 110% of operating cash flow.

---

### 6. Key Red Flags

1. **FCF has deteriorated for three straight years:** +$232M → +$12.5M → **–$41.1M**. Capex of $436.6M now *exceeds* operating cash flow of $395.5M. The company is funding growth entirely from the balance sheet, and cash has fallen $83M since FY2023. Sustainable while net cash is ~$1B — but it means the business does not currently self-fund.
2. **Structural gross-margin erosion:** 27.8% → 24.8% → 23.6% → **23.2%** over four years (–460bps). Combined with D&A at 19.4% of revenue, this is a capital-intensive model earning thin incremental returns.
3. **No revenue growth:** FY2025 revenue of $1,566M remains **below the FY2022 level of $1,678M** (–6.6%). Four years of flat-to-down top line is the single most important fundamental risk here, and it is a demand/mix issue the balance sheet cannot fix.
4. **Earnings quality / base effects:** FY2023 net income of $518M and 38.5% operating margin include the one-off Intel termination payment. Reported three-year growth rates and Piotroski comparisons are distorted — always normalise.
5. **Modest dilution:** shares outstanding 109.3M → 113.6M (+3.9% since FY2022), penalising the Piotroski score.
6. **Unstable market-risk data** (see §3): do not use the computed 2.04–3.05 beta or 67–88% volatility without re-deriving from a clean series. This is a tooling gap, and it materially affects any cost-of-equity or VaR work.

**Explicit data gaps:** (a) no debt maturity schedule beyond current/non-current split — refinancing-cliff analysis incomplete; (b) no credit rating or CDS spreads; (c) interest coverage null in FY2025 (nil interest expense); (d) retained earnings reported as 0 for FY2025, understating Altman Z; (e) Sortino ratio unavailable; (f) market-risk statistics internally inconsistent across windows/benchmarks.

**Bottom line:** TSEM is one of the least credit-risky names in semis — a net-cash, high-liquidity, safe-zone balance sheet that can absorb a 20% revenue decline without touching its cash pile. The risk is entirely on the equity and cash-generation side: a capital-intensive, sub-scale foundry whose revenue has gone nowhere in four years while it burns its own cash on capex. Underwrite it as a high-volatility cyclical with a fortress balance sheet, not as a credit story.
