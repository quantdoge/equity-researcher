# Quant Analyst

- Symbol: MRVL
- Elapsed: 82.6s

---
## MRVL — Quantitative Factor Scorecard
**As of 2026-02-20 · Marvell Technology, Inc. · Technology / Semiconductors · Mkt cap ~$69B (OHLCV-implied)**

---

### ⚠️ DATA INTEGRITY FLAG (read before using any multiple below)

Two internal price sources disagree by **~2.16x**:

| Source | Price | Implied Mkt Cap |
|---|---|---|
| OHLCV series (2026-02-20 close) | **$79.40** | $69.1B |
| Profile / valuation-ratios static field | **$171.41** | $149.1B |

I treat **$79.40 as authoritative**: it is consistent with the momentum score (12-1 of +39.65% back-solves to a ~$57 Feb-2025 price), with P/B (4.8x vs 10.4x — MRVL's normal 3–6x band), and with the full return/risk series, which is computed off OHLCV. The $171.41 field looks like a stale/erroneous snapshot and **inflates every reported multiple by 2.16x**. I show both, but score on the recomputed set.

---

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E **25.9x** (vendor: 55.8x) · EV/EBITDA **15.7x** (33.3x) · P/FCF **49.4x** (106.8x) · P/B 4.83x · Div yld 0.14% | **4/6** (2/6 on raw multiples) | **Neutral** |
| **Momentum** | **+39.65%** (12-1, 252d ex-last-21d) | **1/6** | **Strong Positive** |
| **Quality** | ROE 18.7% · GP/Assets **0.188** · Accruals **+0.0413** · F-Score **6/9** | **6/6 (worst)** | **Strong Negative** |
| **Low Vol** | Vol **89.9%** · β **3.51** · Max DD **−48.4%** | **6/6 (worst)** | **Strong Negative** |
| **Earnings Revision** | **+53.0%** — but on **FY2031** consensus, not 3-mo forward | **1/6** | **Positive (low confidence)** |

**Peer cross-section (semis: MRVL, NVDA, AVGO, AMD, MU, TSM)**

| Metric | MRVL | NVDA | AVGO | AMD | MU | TSM |
|---|---|---|---|---|---|---|
| 12-1 Momentum | **39.65%** | 15.63% | −4.91% | 21.04% | 15.53% | 20.75% |
| ROE | 18.66% | 76.33% | 28.45% | 6.88% | 61.40% | 31.46% |
| GP/Assets | **0.188** | 0.742 | 0.253 | 0.223 | 0.549 | 0.288 |
| Accruals | **+0.041** | +0.084 | −0.026 | −0.044 | −0.024 | −0.073 |
| Volatility | **89.9%** | 38.3% | 45.2% | 73.5% | 84.9% | 41.9% |
| Beta vs SPY | **3.51** | 1.93 | 2.10 | 3.53 | 3.36 | 2.26 |
| EPS Revision | **+53.0%** | +3.9% | +4.6% | +39.4% | +22.7% | +2.3% |

MRVL is **best-in-class on momentum and revisions, worst-in-class on quality and volatility** — a textbook high-beta "story momentum" profile, not a quality-compounder profile. Note TSM's P/E (1.2x) and EV/EBITDA (0.0x) are corrupt; excluded from value ranking.

---

### 2. Price Statistics

| Statistic | 252-day | 504-day |
|---|---|---|
| Annualised return | **154.5%** | **96.7%** |
| Annualised volatility | 91.2% (low-vol tool: 89.9%) | 75.5% |
| **Beta vs SPY** | **3.53** | **3.08** |
| **Alpha (annualised)** | **+91.4%** | **+42.0%** |
| R² vs SPY | **0.265** | **0.249** |
| **Sharpe** | **1.694** (alt: 1.51) | **1.28** |
| **Sortino** | **2.682** | **1.887** |
| Max drawdown (252d) | **−48.4%** | — |

**Statistical significance warning.** R² of 0.25–0.27 means **73–75% of MRVL's variance is idiosyncratic**. Residual vol is 78.1% (252d) / 65.4% (504d), so the standard error on the annualised alpha is ~78% and ~46% respectively. Implied **alpha t-stats are ~1.17 and ~0.91 — neither is significant** at any conventional level. The headline "+91% alpha" is noise, not skill-signal. Treat the beta (3.1–3.5) as the only reliable regression output.

**Correlation structure (252d):** SPY 0.51, TSM 0.59, AMD 0.59, MU 0.56, AVGO 0.55, **NVDA 0.41 (lowest)**. MRVL offers modest diversification vs NVDA but is not a low-beta hedge — 3.5x market sensitivity dominates.

---

### 3. Composite Quant Signal: **NEUTRAL** (negative risk-adjusted tilt)

Equal-weighting five factors gives a mid-pack score (2 top-quintile, 2 bottom-quintile, 1 middle). But reliability-weighting pushes it down:
- **Momentum is already breaking.** MRVL peaked at **$100.03 on 2025-12-03** and is **−20.6% since**; last 21 trading days are **−0.4%**, YTD **−6.4%**. The +39.65% 12-1 figure is entirely a Feb–Nov 2025 artifact. **Momentum-reversal risk is live, not hypothetical.**
- **The +53% revision is not real revision momentum.** It compares FY2031 consensus ($28.26) to the prior FY2031 figure ($18.47) across only 10 analysts — a 5-year-horizon CAGR mark-up, not a 3-month-forward period revision. Low evidentiary weight (sample n=10).
- Quality and low-vol are **measured reliably and are bottom-of-peer-group on both.**

---

### 4. Key Quant Risk Flags

1. **Earnings quality — the single largest red flag.** FY2026 net income of **$2,670M exceeds pre-tax income (~$1,136M)** off operating income of $1,338M and interest of $203M. That implies a **~$1.5B net tax benefit** embedded in earnings. Reported EPS of $3.07 is therefore inflated; **normalised EPS is roughly $1.10–1.25**, putting the true P/E at **~65–70x**, not 25.9x. Corroborated by accruals of **+0.041** (NI exceeds operating CF of $1,751M by $920M) and Piotroski F4 (accruals quality) scoring **0**.
2. **Capital efficiency is below cost of capital.** FY2026 **ROIC of 7.01%** — below a reasonable ~9–10% WACC. ROE 18.66% is flattered by the tax benefit and leverage, not operating returns. F-Score 6/9 with F5 (leverage) and F7 (dilution) both failing; share count rose despite $2.04B of buybacks, with SBC of $591M.
3. **Momentum reversal / crowding.** β 3.5 with 90% vol and a −48% max drawdown. A −20.6% drawdown from the December peak is consistent with factor unwinding in the AI-semi complex (AVGO already at −4.9% 12-1).
4. **Severe idiosyncratic risk.** R² 0.25 → index hedging is ineffective; ~75% of risk is stock-specific (custom silicon / AI program concentration).
5. **Liquidity: adequate.** ADV ~13–20M shares; no liquidity constraint.
6. **Vendor data conflict** (2.16x price error) — every vendor-supplied multiple in this report should be re-derived from OHLCV before entering a model.

**Bottom line:** strong trailing momentum and a favourable long-horizon estimate trajectory, offset by worst-in-sector quality, worst-in-sector volatility, an already-rolling-over price trend, and a 65–70x normalised earnings multiple. **Do not underwrite the reported 25.9x P/E — it is a tax-benefit artifact.**
