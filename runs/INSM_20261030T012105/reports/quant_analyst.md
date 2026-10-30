# Quant Analyst

- Symbol: INSM
- Elapsed: 18.4s

---
Data collection complete. I have the full factor suite, two benchmark regressions (SPY and XBI), 1yr and 2yr risk metrics, and genuine biotech comparables (VRTX, ALNY). Writing the report.

---

# INSM (Insmed Incorporated) — Quantitative Factor Analysis

**Sector:** Healthcare / Biotechnology (rare-disease, commercial-launch stage) | **Price:** $111.59 | **Mkt Cap:** $24.4B | **Employees:** 1,664

> **Critical framing note:** INSM is a **pre-profit, pipeline-driven biotech** (ARIKAYCE marketed; Brensocatib in bronchiectasis launch/development). Value and quality factor models are built for cash-generative businesses and are **structurally inapplicable** here — negative P/E, EV/EBITDA, and FCF are not "cheap," they are "loss-making." Quant factors carry low predictive power for binary-catalyst biotech; this report should be read alongside clinical/commercial risk that no factor captures.

## 1. Factor Scores

| Factor | Score | Sector Rank (biotech cohort, n=3) | Signal |
|--------|-------|-----------------------------------|--------|
| **Value** | **n/a** (P/E −17.4, EV/EBITDA −19.8, P/FCF −24.6) | Not meaningful | **Neutral / N/A** — all multiples negative; no valuation anchor |
| **Momentum (12-1)** | **45 / 100** (+1.83% excl. last 21d) | **#2 of 3** (VRTX +7.2% > INSM +1.8% > ALNY −13.4%) | **Neutral** — mildly positive, lagging leader |
| **Quality** | **30 / 100** (ROE −172.8%, GP/Assets 0.21, accruals −0.15) | #3 of 3 | **Negative** — deeply loss-making; only accruals are a bright spot |
| **Low Vol** | **20 / 100** (66.4% ann. vol, β 0.70) | **#3 of 3** (VRTX 29% < ALNY 58% < INSM 66%) | **Negative** — highest volatility in cohort |
| **Earnings Revision** | **65 / 100** (2030E EPS $10.32 vs $6.73 = **+53.3%**) | n/a | **Bullish but LOW CONFIDENCE** — long-dated, only 7 analysts; PTs simultaneously being cut |

**Supporting:** Piotroski F-Score **5/9 (Moderate)** — profitability & dilution components (F1, F2, F7) all score 0; leverage, accruals, margin, turnover positive.

## 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|--------|--------------|--------------|
| Annualised return | **−21.64%** | **+53.09%** |
| Annualised volatility | 67.3% | 62.0% |
| **Sharpe** | **−0.321** | **+0.856** |
| **Sortino** | **−0.49** | **+1.32** |
| Max drawdown | 44.3% | — |
| **Alpha vs SPY** | **−34.3%** (annualised) | — |
| Beta vs SPY | 0.707 (R² **0.019**) | — |
| **Alpha vs XBI** | **−49.1%** (annualised) | — |
| Beta vs XBI | 0.846 (R² 0.150) | — |

**⚠️ The single most important statistic in this report:** the **1yr Sharpe of −0.32 vs 2yr Sharpe of +0.86**. INSM was a strong two-year performer that has **rolled over hard in the last twelve months**. Returns are excellent on a trailing-2yr basis but currently in a drawdown/reversal phase. Anyone quoting "Sharpe 0.86" is using stale data; the live 1yr risk-adjusted return is negative.

**⚠️ Statistical validity:** **R² of 0.019 vs SPY and 0.150 vs XBI** means market/sector factors explain almost none of INSM's variance. The alpha estimates (−34% vs SPY, −49% vs XBI) are therefore **statistically unreliable** — INSM trades on idiosyncratic drug/launch news, not macro. Beta ~0.70 is the only defensible regression output.

## 3. Composite Quant Signal

### **NEUTRAL (weak-neutral)** — Composite score ≈ **40 / 100**

| Component | Weight | Score |
|-----------|--------|-------|
| Momentum | 30% | 45 |
| Quality | 30% | 30 |
| Low Vol | 20% | 20 |
| Earnings Revision | 20% | 65 |

**Rationale:** Factors are uninspiring across the board — no value anchor, weak quality (pre-profit), worst-in-cohort volatility, and momentum that has faded. The lone positive (revision) is low-quality: a +53% jump in a **2030** estimate from only 7 analysts, while **sell-side price targets are being cut** (Stifel $195↓, Mizuho $154↓ from $195, Morgan Stanley $213↓, Raymond James $173↓, Barclays $207↓ from $237). Rising long-dated EPS with falling targets = a classic "show-me" divergence, not a clean upgrade cycle.

**The quant model is deliberately not bullish, but it is also blind to the actual thesis.** INSM's investment case is a Brensocatib bronchiectasis launch ($6.2B 2030E revenue consensus, ~$3.0B EBITDA by 2030 per estimates) — a commercial execution/binary bet that a factor model cannot price. Treat the Neutral signal as "no statistical edge," not "sell."

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — CONFIRMED IN PROGRESS.** 2yr return +53% vs 1yr −22%; max drawdown 44%. The stock is de-rating from a prior run-up. Factor momentum is fragile.
2. **Factor-model inapplicability / small-sample caveat.** Value and Quality scores are mechanically distorted by a pre-profit P&L. Sector cohort ranking uses only **n=3** true biotech comps — not statistically significant; directional only.
3. **Regression insignificance.** R² of 1.9% (SPY) means alpha/beta estimates explain essentially nothing; do not use computed alpha as a signal.
4. **Revision signal is low-quality.** 2030 estimate from 7 analysts; price targets falling concurrently. High noise, wide dispersion (2028E EPS low $0.24 / high $6.55).
5. **Extreme volatility & event risk.** 66% annualised vol and high idiosyncratic share = binary clinical/regulatory/launch outcomes dominate. Position sizing must reflect full-loss potential on catalyst.
6. **Concentration / liquidity.** At $24.4B cap liquidity is adequate, but vol + single-pipeline dependence = crowding and gap-risk exposure.

**Bottom line:** No quantitative edge. Neutral signal driven by weak quality/vol factors offset by a noisy positive revision. The trade is fundamentally a **catalyst bet on Brensocatib commercialization**, not a factor trade — and recent price action shows the market is currently skeptical.
