# Quant Analyst

- Symbol: SNDK
- Elapsed: 186.0s

---
# SNDK — Quantitative Factor Report

**Sandisk Corporation** · Technology / Computer Hardware (NAND flash / memory) · Mkt cap ~$198B · Last price $1,371.12

> ⚠️ **Data-quality flags up front:** The feed shows a $1,371 share price and $198B cap that are inconsistent with SNDK's true post-spin-off trading range, and beta is reported three different ways (profile 5.22, vol-tool 3.38, alpha-regression 3.40). The earnings-revision window is dated **FY2030**, not a 3-month-forward window. Treat absolute levels with caution; **relative cross-sectional rankings** (vs. memory peers MU/INTC/AMD) are the reliable signal here.

## 1. Factor Scores Table (cross-sectional rank vs. MU, INTC, AMD — n=4)

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 18.6 · EV/EBITDA 15.7 · P/FCF 18.5 | **2 / 4** | Attractive (cheapest ex-MU) |
| **Momentum** | 12-1 return **−7.79%** | **4 / 4 (last)** | **Negative** |
| **Quality** | ROE 72.7% · GP/Assets 0.643 · Accruals −0.011 | **1 / 4** | **Very strong** |
| **Low Vol** | Vol 108.6% · Beta ~3.4 · MaxDD 56.5% | **4 / 4 (worst)** | **Poor** |
| **Earnings Revision** | +69.9% (FY2030 est.) | n/a | Positive but long-dated |

- **Value:** Second-cheapest in group on every multiple (MU 12.2/9.1/17.5 is cheaper; AMD & INTC far more expensive/broken). Cheap for a quality name.
- **Quality:** Best-in-class on all three legs — highest ROE (72.7%), highest gross-profit/assets (0.64), negative accruals (clean earnings). Piotroski **F-Score = 7** (moderate/strong).
- **Momentum:** The lone weak factor — only name in the group with *negative* 12-1 momentum while peers sit +7% to +11%.
- **Low Vol:** Worst of the four on volatility, beta, and drawdown — a high-octane cyclical.

## 2. Price Statistics (252-day, vs. SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **+172.96%** ⚠️ (but R² only 0.169) |
| Beta | **3.40** (regression) / 3.38 (vol-tool) |
| R² | 0.169 — only 17% of variance is market-driven |
| Annualised return | 194.26% |
| Annualised volatility | 108.6–109.1% |
| **Sharpe** | **1.78** |
| **Sortino** | **3.18** (strong upside/downside asymmetry) |
| Max Drawdown | −56.49% |

The high alpha/beta and 194% return reflect a violent run, but **R² = 0.17 means the alpha estimate is statistically noisy** — idiosyncratic risk dominates, so the beta/alpha t-stats should be treated as low-confidence.

## 3. Composite Quant Signal: **NEUTRAL (tilt: Buy)**

**Rationale:** Two of five factors are top-of-group (Quality #1, Earnings Revision strongly positive) and value is top-half — a trio that historically screens well. But this is offset by the **only negative momentum in the peer set** and the **worst volatility/drawdown profile (beta ~3.4)**. It's a "great business, wrong tape" setup — quality/value supports accumulation, but momentum and risk argue against chasing. Net: **Neutral with a quality-driven Buy bias**, contingent on momentum turning.

## 4. Key Quant Risk Flags

- **Momentum reversal / negative trend:** −7.8% 12-1 return, the sole laggard — factor is working *against* the position.
- **Extreme volatility & drawdown:** 109% annualised vol, −56% max DD, beta ~3.4 — position sizing must be small; a 3.4 beta amplifies any market drawdown ~3x.
- **Low R² (0.17) / idiosyncratic risk:** returns are stock-specific, not market-driven — diversification benefit is low, single-name risk is high.
- **Data-integrity caveat:** inconsistent beta fields and a FY2030-dated EPS revision mean the revision and alpha figures should be down-weighted until confirmed.
- **Factor crowding:** memory/NAND is a highly cyclical, crowded semis trade — the strong quality print may be a cycle-peak artifact (ROE 72.7% is abnormally high).

**Bottom line:** Quality + value + revisions are genuinely strong, but negative momentum, outsized volatility and a 0.17 R² keep this at **Neutral** on pure quant — a high-quality but high-risk cyclical that hasn't yet earned a momentum confirmation.
