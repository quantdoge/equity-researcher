# Quant Analyst

- Symbol: MPWR
- Elapsed: 60.4s

---
# MPWR — Quantitative Factor & Risk Analysis
**Monolithic Power Systems | Semiconductors | Price $1,388.05 | Mkt Cap ~$67.1B**

---

## 1. Factor Scores Table

Sector ranks are percentile within a hand-built semiconductor comp set (MPWR + NVDA, AVGO, AMD, MU, ASML, TSM) — the API's "sector" call returned the entire Technology sector (AAPL/MSFT/ORCL), which is not a valid comp group. **TSM excluded from value ranks: its feed is corrupt (P/E 1.17, EV/EBITDA −0.02).**

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 108.9 · EV/EBITDA 80.4 · P/FCF 100.7 · P/B 19.0 | **~17th pct (5th of 6)** | **Strong Sell** — 1.7–1.8× peer median on all three metrics |
| **Momentum (12-1)** | Tool: −7.35% | ~17th pct (6th of 7) | **Negative — but see conflict flag** |
| **Quality** | ROE 17.4% · GPA 0.367 · Accruals −0.053 · ROIC 20.5% · F-score 6/9 | ~43rd pct (4th of 7) | **Neutral / mild positive** |
| **Low Vol** | β 2.47 (504d) / 2.64 (252d) · σ 53.9% / 62.5% | Bottom quintile (beta-based) | **Strong Sell** |
| **Earnings Revision** | +7.23% (FY2030, n=2) | n/a | **Non-informative — see methodology flag** |

**Value detail vs semis:** peer median P/E 64.1, EV/EBITDA 46.4, P/FCF 55.4 — MPWR sits above each. *Offsetting nuance:* on FY2026E consensus EPS of $29.12 (non-GAAP), forward P/E is **47.7x** — below the peer median *trailing* multiple, on implied +55% revenue / +64% EPS growth. Value is a fail on trailing/latest actuals, defensible only if the 2026 ramp lands.

**Quality detail:** Gross profit/assets 0.367 ranks 3rd of 7 (behind NVDA 0.742, MU 0.549); accruals −0.053 rank 3rd of 7 (clean, cash-backed earnings). But ROE 17.4% ranks 6th of 7. **ROIC trend is deteriorating:** 31.5% (2022) → 23.4% (2023) → 17.1% (2024) → 20.5% (2025). Piotroski 6/9: positive ROA, positive CFO, no dilution, better asset turnover — but *no* ROA improvement, *no* gross-margin improvement (55.2% vs 55.3% FY24, 56.1% FY23), and rising leverage.

**Earnings revision — flag:** the reported +7.23% compares the FY2030 estimate ($75.13) against the **FY2029** estimate ($70.06). That is adjacent-year growth, not a revision of the same forward period — the signal is a **methodology artifact**, made worse by only 2 analysts on that horizon. The genuine revision evidence conflicts: sell-side price targets were **cut** through H2 2026 (Wells Fargo $1,800→$1,700→$1,550; Oppenheimer $1,700→$1,500), while Rosenblatt *upgraded to Buy* with $1,700 on 2026-10-30. Net: **Neutral, low confidence.**

---

## 2. Price Statistics

| Metric | 504-day (2yr) | 252-day (1yr) |
|--------|---------------|---------------|
| Alpha (ann., vs SPY) | **+17.79%** | — |
| Beta (vs SPY) | **2.475** | 2.639 |
| R² | 0.342 | — |
| Annualised return | +63.84% | — |
| Annualised volatility | 53.92% | 62.54% |
| **Sharpe** | **1.177** | 0.669 |
| **Sortino** | **1.830** | — |
| Max drawdown | **−32.85%** | −32.85% |

**Statistical significance — the critical caveat.** Only 34.2% of MPWR's variance is market-explained, so idiosyncratic vol is 54.25% × √(1−0.342) = **44.1%**. Annualised alpha standard error ≈ 44.1/√2 = 31.2%, giving **t ≈ 0.57** — alpha is **not** distinguishable from zero. Sharpe standard error ≈ 0.92 → **t ≈ 1.28**, also insignificant. A 2-year window is simply too short for a stock with this much idiosyncratic risk; the 17.8% alpha and 1.18 Sharpe are *directionally* attractive but **not statistically established**.

Sortino (1.83) > Sharpe (1.18) indicates upside volatility exceeds downside volatility — favourably skewed returns, consistent with the stock's gap-up behaviour. Beta disagreement worth noting: the company profile reports β 1.725 (monthly basis) vs 2.47 daily — a ~40% spread in the single most important risk input.

**Price action (raw data):** 52-wk closing high $1,684.84 (2026-06-03); current $1,388.05 = **−17.6% from high**. Recent tape is violent: −10.3% on 2026-11-05 (2.63M shares, ~3× normal) then **+16.6% on 2026-11-09**. Average daily dollar volume ≈ $0.8B — **no liquidity concern**.

---

## 3. Composite Quant Signal

### **NEUTRAL**

| Factor | Contribution |
|---|---|
| Value | Strongly negative (bottom quintile) |
| Momentum | Negative as measured — **conflicted** (see flag) |
| Quality | Mild positive |
| Low Vol | Strongly negative (β 2.47) |
| Revision | Neutral / unreliable |

The factor stack is genuinely split: the two most reliably measured factors (**value** and **low-vol**) both score bottom-quintile and point to Sell, while quality and realised risk-adjusted returns point to Buy. These do not offset into a directional call — they cancel. This is a high-quality, high-beta, expensive compounder: a **momentum/quality holding, not a value or defensive one**. It is not a Strong Sell only because earnings quality is clean (accruals −0.053), the balance sheet is unlevered, and forward growth estimates imply rapid multiple compression on a 2026–27 view.

---

## 4. Key Quant Risk Flags

1. **⚠️ MOMENTUM DATA CONFLICT — highest-priority flag.** The momentum tool reports **−7.35%** for a 252-day 12-1 window. I cannot reproduce that from the raw price history: 2025-11-10 close $969.81 → 2026-10-09 close $1,386.29 = **+42.9%**. No 252-day variant reconciles to −7.35%. The raw-data figure would rank MPWR **1st of 7** in the comp set (peer median ~+11.5%), not 6th. Treat the tool output as unreliable and **do not act on the momentum factor alone**; the verifiable evidence says momentum is strongly *positive*.

2. **Factor crowding risk is low; valuation risk is acute.** 80.4× EV/EBITDA and 100.7× P/FCF leave no cushion. A single multiple de-rating of 25% plus flat earnings is a −25% outcome with no fundamental break required.

3. **Beta/vol tail risk.** Daily β 2.47 means a 10% SPY drawdown implies ~−25% for MPWR. Observed MDD is already −32.85%, and the stock is −17.6% from its high. Position sizing must treat this as a 2.5× leveraged market exposure.

4. **FY2024 base-year distortion.** FY2024 net income of $1,786.7M on $2,207.1M revenue (81% net margin vs $539M operating income) implies a **~$1.25B one-time, non-operating gain**. This inflates FY2024 ROE to 56.8% and corrupts any 3-year growth/CAGR, P/E history, or quality percentile using 2024 as a base. All 2024-anchored metrics should be discarded.

5. **ROIC decay.** 31.5% → 20.5% over three years; the FY2025 uptick is a partial recovery, not a reversal. Deteriorating capital returns plus a rising multiple is the classic negative-compounding setup for a quality factor.

6. **Gap risk / event concentration.** Consecutive ±10–17% single-day moves in November 2026 on elevated volume indicate news/fundamental-flow sensitivity, not tradeable trend. Any momentum or mean-reversion strategy on this name faces severe slippage and gap risk.

7. **Sample-size and data-quality limits.** Alpha and Sharpe are statistically insignificant (t ≈ 0.57 and 1.28) on 504 days. Peer betas were not retrieved, so the low-vol rank is inferred from MPWR's absolute beta rather than measured cross-sectionally. TSM value data is corrupt and excluded (comp set n=6 for value, n=7 otherwise) — ranks of "5th of 6" carry wide error bars.

**Bottom line: Neutral.** The numbers do not support a directional bet. Fair value on the quant stack requires the FY2026–27 estimate ramp to be delivered; if it is, forward multiples normalise to ~48× and ~30× and the current price is defensible. If growth slips, the 100× P/FCF has no support. The statistically rigorous read is that the impressive track record (17.8% alpha, 1.18 Sharpe) is **not yet proven** — it rests on a 2-year sample in a single high-beta semiconductor cycle.
