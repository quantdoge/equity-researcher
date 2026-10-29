# Quant Analyst

- Symbol: GMAB
- Elapsed: 113.0s

---
## Correction to my own process note
My first-pass read that the price feed was "corrupt" was wrong — the OHLCV series I pulled (ending 2026‑06‑01) is simply **stale**; the risk/valuation tools run on data through ~Nov 2026. External confirmation: 52‑week range **$23.62–$59.97**, market cap **$35.23B** (614.9M sh × $57.29 ✓), 1Y return ~97%. The risk statistics are internally consistent and usable (regression R² = 0.0521 → √ = 0.228, which matches the measured GMAB–SPY correlation of **0.2272** exactly).

---

# GMAB — Genmab A/S (ADR) | Quantitative Factor Report
**Price $57.29 | Mkt cap $35.2B | Healthcare / Biotechnology | Denmark (DKK reporter, USD ADR)**

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **10/100** | **5 of 6** (bottom quintile) | **Strong Sell** |
| **Momentum** | **92/100** | **1 of 7** (top quintile) | **Strong Buy** |
| **Quality** | **38/100** | 4 of 6 | **Sell** |
| **Low Vol** | **30/100** | 5 of 6 | **Sell** |
| **Earnings Revision** | **35/100** (low confidence — see caveat) | 5 of 6 | **Sell / Neutral** |

**Value — 10/100.** P/E **37.2x**, EV/EBITDA **29.6x**, P/FCF **31.2x**, P/B **6.15x**, no dividend. vs peer group (AMGN 31.8/17.2, GILD 23.5/15.8, MRK 19.4/13.8, AZN 25.9/14.6): GMAB's EV/EBITDA carries a **~86% premium to the peer median of 15.9x**, and P/FCF is the **highest in the peer set**. Only ABBV screens worse (120.7x P/E, negative ROE). NVO's printed 1.66x P/E is a data error and was excluded.

**Momentum — 92/100.** 12‑1 momentum **+25.73%**, #1 of 7 and a **~10pt lead** over the next name (MRK 15.77%, AMGN 15.76%, GILD 15.05%, ABBV 2.14%, AZN −4.02%, NVO −22.54%). Genuinely strong, but see the reversal flag.

**Quality — 38/100.** ROE 16.5%, ROA 7.5%, gross profit/assets 26.6%, accruals **−1.74%** (cash earnings exceed accounting earnings — the one clean positive). Against it: **Piotroski F‑Score 4/9 ("Weak")**, 5 of 9 components failing (ROA improvement, leverage, equity change, gross margin, asset turnover), and a clear **ROIC decay: 22.5% (2022) → 16.4% (2023) → 17.8% (2024) → 11.1% (2025), −1,137bp in three years.**

**Low Vol — 30/100.** Annualised vol **48.2%** — roughly **2x** large-cap pharma. Beta **0.844** (below market, mildly favourable) but nearly meaningless at R² 5%. Net: ranks poorly.

**Earnings Revision — 35/100 (⚠ invalid tool output).** The revision engine reported "+8.61% upgrade," but that is an artifact: it compared the **FY2030** consensus EPS ($3.133) against the **FY2029** figure ($2.885). Those are two *different* forecast periods — it is measuring forecast growth, not revision. It is also computed on just **5 analysts** (vs 12 on FY2028). **Discard it.** The valid revision evidence is bearish:
- FY2026E EPS **$1.18 vs FY2025A $1.54 = −23%**, on **+20% revenue** → net margin 25.9% → 18.1% (−780bp).
- Sell-side targets were **cut four times through 2026**: Wainwright 41→39→40→38, Guggenheim 45→40, before Guggenheim's Oct-2026 raise to $58.
- **Current price $57.29 sits at/above essentially every outstanding target** (consensus ~$41–43, i.e. **−25% to −28% to consensus**).

## 2. Price Statistics (252 trading days)

| Metric | Value |
|---|---|
| Annualised return | **+86.69%** |
| Annualised volatility | **48.2%** |
| Beta vs SPY | **0.844** (profile states 0.645 — see conflicts) |
| Alpha (annualised) | **+72.89%** — *t ≈ 1.55, NOT significant* |
| R² vs SPY | **0.052** (corr 0.227) |
| Sharpe (0% rf) | **1.79** (alt calc 1.84) |
| Sortino (0% rf) | **4.30** |
| Max drawdown | **−30.67%** |

**Interpretation.** The Sharpe of 1.79 looks excellent but is **statistically fragile**: over a single year the standard error of an annualised Sharpe is ≈1.0, so the t-stat is only ~1.8 — not distinguishable from zero at 5%. The Sortino/Sharpe ratio of **2.4x** signals returns are driven by a small number of large **positive** outliers, i.e. event/clinical-trial luck rather than repeatable risk-adjusted edge. A 48% vol with a 30.7% drawdown also implies a **~1.6x return/vol drag** on any drawdown-based risk budget.

## 3. Composite Quant Signal

### **NEUTRAL — score 43/100, with negative skew (Hold / do not add)**

Weighting (V 25%, M 25%, Q 20%, LV 15%, Rev 15%): 2.5 + 23.0 + 7.6 + 4.5 + 5.3 = **42.9**

This is the textbook **"expensive momentum"** archetype: rank #1 momentum bolted onto bottom-quintile value, deteriorating quality, high volatility, and a price sitting *above* consensus. Momentum is doing 100% of the work; every other factor is a headwind. Not a short (momentum is real and trending), but not a quant buy — there is no factor support beneath the price.

## 4. Key Quant Risk Flags

1. **Momentum reversal / crowding (highest severity).** +87% 1Y, at the 52‑week high, highest-momentum name in the peer group by a wide margin, and **trading 25–28% above consensus target**. Momentum crashes cluster in high-vol, high-idiocyncratic-risk names exactly like this (48% vol, R² 5%).
2. **Beta is a false comfort.** Beta 0.844 understates risk: with R² = 0.052, only **5%** of variance is market-explained. Size positions on **total volatility**, not beta — a beta-based sizing rule would over-allocate ~2x.
3. **Valuation has no valuation floor.** 29.6x EV/EBITDA and 48.6x FY2026E EPS at the top of a ~90% one-year run leaves no margin of safety; the multiple, not the earnings, is the risk.
4. **Earnings air pocket in the near term.** FY2026E EPS −23% YoY despite +20% revenue growth. The bull case is entirely back-end loaded (FY2028E $2.67, FY2030E $3.13 → 21.5x / 18.3x).
5. **Quality decay.** ROIC halved in three years; F‑Score 4/9. This is a *worsening* quality profile, not a stable one.
6. **Negative skew to estimates.** Four PT cuts vs one raise through 2026; street range for FY2028E EPS is **$1.68–$3.27** (a ~2x spread) — consensus is unusually disperse, so "beat" outcomes are noisy.

## 5. Data Quality Caveats (material — read before using these numbers)

- **Earnings revision factor is unusable.** The engine compared FY2030 vs FY2029 EPS, not the same period 3 months apart. Treated as 35/100 by judgement, not measurement. A true same-period revision series is unavailable.
- **Cross-period currency inconsistency.** FY2024 and FY2023 income statements are filed in **DKK**, FY2025 in **USD**, with inconsistent implied FX rates (revenue ratio 5.78 vs net-income ratio 8.14). All FY2024→FY2025 trend items (ROE change, ROA improvement, gross-margin improvement, asset-turnover improvement) are **partly translation artifacts** and should be treated as directional only. The ROIC/ROE decline is real in substance (USD net income ~$1.23B → $964M, −21%) but the precise magnitude is not reliable.
- **Beta conflict:** company profile 0.645 vs regression 0.844. Regression value used.
- **Sharpe conflict:** 1.794 vs 1.843 across two tools (same underlying vol) — minor, immaterial.
- **Excluded peer:** NVO value multiples (P/E 1.66, EV/EBITDA 1.75) are erroneous and were dropped from ranks.
- **Sample size:** all risk statistics rest on **252 observations / 1 year**. Sharpe, Sortino, alpha and max-drawdown are **not** statistically robust at this N. A 3–5 year window is required before any of these are load-bearing.
- **Liquidity is NOT a constraint**: avg volume ~3.7M shares (~$200M/day) on a $35B cap; note the occasional 5–8x volume spikes (e.g., 784% of average) consistent with event-driven flow. Structural risks are ADR ratio (1 ADR ≠ 1 ordinary share) and the DKK home listing, which create tracking-basis risk not captured by any factor here.
