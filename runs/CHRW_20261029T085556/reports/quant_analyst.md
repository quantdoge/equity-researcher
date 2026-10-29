# Quant Analyst

- Symbol: CHRW
- Elapsed: 31.4s

---
I have enough to complete the analysis. Before writing, I must flag a **critical data-integrity finding**: several price-derived tool outputs contradict the raw OHLCV series I pulled. The price history shows CHRW rising from ~$102 (Dec-2024) to ~$159 (Dec-2025), a **+56% total return**, yet the momentum/alpha/Sharpe tools returned −29% momentum and −43% annualized return. **The price-statistics tools are returning corrupted values and I will not report them at face value.**

---

# CHRW — Quantitative Factor Report
*C.H. Robinson Worldwide | Industrials / Integrated Freight & Logistics | Price $158.99 (31-Dec-2025 actual close); Mkt cap ~$15.0B*

## ⚠️ Data Integrity Warning (read first)
| Metric | Tool Output | Raw-OHLCV Reality | Verdict |
|---|---|---|---|
| 1-yr return | −43.5% | **+55.6%** (102.15→158.99) | ❌ Corrupted |
| 12-1 momentum | −29.1% | **≈ +58%** | ❌ Sign inverted |
| Annualized vol | 47.9% | ≈ 25–28% (est.) | ❌ Implausible |
| Beta | 0.61 (R²=0.028) | Profile beta **0.95**; R²=0.03 impossible for a liquid large-cap | ❌ Corrupted |
| Max drawdown | −38.8% | ≈ −22% (peak $107 Jan → trough $83.5 Apr) | ❌ Overstated |

The R² of 0.028 and 48% vol for a $15B logistics name are not credible. I have **reconciled these from the raw adjusted-close series** and report the corrected estimates below; tool numbers shown for auditability only.

## 1. Factor Scores Table
*(Ranks estimated vs broad Industrials universe; sector-specific freight peers — FDX/UPS/XPO — not available as peers, so ranks carry wide error bands)*

| Factor | Score (0–100) | Sector Rank (est.) | Signal |
|---|---|---|---|
| **Value** | 30 | Bottom tercile | **Unattractive** — P/E 26.4, EV/EBITDA 19.1, P/B 8.4, P/FCF 17.3. Rich for a cyclical broker even on recovery earnings. |
| **Momentum** | 85 | Top quintile | **Strong positive** — 12-1 ≈ +58%; two earnings gap-ups (Jul-31 +18%, Oct-30 +20%) drove sustained trend. |
| **Quality** | 75 | Top tercile | **Favorable** — ROIC 22.9%, ROE 31.8%, negative accruals (−0.065 = high earnings quality), Piotroski F=7. *(Note: tool's "low" quality flag is a scoring artifact — fundamentals are strong.)* |
| **Low Vol** | 55 | Middle | **Neutral** — 5yr beta 0.95, realized vol ~25–28%. Moderate risk, not defensive. |
| **Earnings Revision** | 45 | Middle | **Neutral/weak** — tool used a single-analyst 2030 estimate (+0.7%); near-term revision not statistically usable. Genuine revision breadth unavailable. |

## 2. Price Statistics (reconciled from raw OHLCV)
| Metric | Reconciled Estimate | Note |
|---|---|---|
| Total return (1yr, Dec-24→Dec-25) | **+55.6%** | vs SPY ~+13% → large positive alpha |
| 12-1 momentum | **≈ +58%** | Strong |
| Beta (5yr monthly, profile) | **0.95** | 1-yr daily tool value unreliable |
| Realized vol (est.) | **~25–28%** | Not 48% |
| Max drawdown (est.) | **≈ −22%** | Jan–Apr 2025 freight-tariff selloff |
| Sharpe (rf=0, est.) | **≈ 1.9–2.2** | Reinvested in recovery; high but cyclically inflated |
| Sortino | **Not reliably computable** | Downside-deviation tool output corrupted with the return series |

*Alpha/beta regression: the −39% alpha / 0.61 beta / R²=0.028 tool output is internally inconsistent; a stock up 56% while SPY up ~13% must show strongly **positive** alpha. Actual beta≈0.95.*

## 3. Composite Quant Signal
**BUY (moderate conviction)** — driven by the rare *momentum + quality* pairing (top-quintile momentum, top-tercile quality/ROIC with clean accruals) offset by a *bottom-tercile value* score. This is a quality-momentum profile that is fundamentally sound but **not cheap**: you are paying 26x earnings after a 56% run.

## 4. Key Quant Risk Flags
- **Momentum-reversal / post-rally valuation risk** ⚠️: +58% 12-1 return into a 26.4x P/E leaves little cushion; cyclical freight names mean-revert hard after earnings-driven gaps.
- **Cyclicality / earnings fragility**: EPS estimates are volatile (2028 est. $8.28 vs 2027 $7.44 — inconsistent series), freight-rate cycle is the dominant driver.
- **Data-feed reliability**: price-statistics pipeline returned unusable momentum/vol/beta/Sharpe — **do not cite the raw tool outputs in the memo**; use the reconciled figures.
- **Estimate-revision confidence**: low — near-term analyst breadth not retrievable; forward estimate rests on thin coverage (1–5 analysts on the far periods).
- **Liquidity**: adequate (large-cap, ~1M+ ADV) — not a constraint.

**Bottom line:** Fundamentals and trend are genuinely strong (high ROIC, clean accruals, top-quintile momentum), but valuation is stretched and the provided risk-statistical tools are corrupted. Net: **Buy on quality/momentum, sized cautiously for cyclical reversal risk.**
