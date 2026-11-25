# Quant Analyst

- Symbol: PCVX
- Elapsed: 79.8s

---
## PCVX — Vaxcyte, Inc. | Quantitative Factor Report
**Clinical-stage biotechnology (pneumococcal conjugate vaccines) | Market cap ≈ $8.6–10.0B | Price $60.81 (close 2026‑09‑01; ratio engine uses $63.18 — 3.8% stale)**

> ⚠️ **Read this first.** PCVX is pre‑revenue (FY2025 revenue $0, net income −$766.6M). Valuation, quality and revision factors are structurally degenerate for this name — several tools return *numbers* that are not *information*. I mark those "n.m." rather than launder them into a score.

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E −11.22 · EV/EBITDA −9.65 · P/FCF −12.85 · **P/B 3.20** | n.m. | **n.m. / N/A** — negative earnings, EBITDA and FCF make every multiple except P/B meaningless. EV $7.15B vs $1.49B cash; you are paying ~$5.7B EV for a pipeline with no approved product. |
| **Momentum** | **+0.75%** (12‑1, 252d) | n.m. | **Neutral (flat)** per tool of record. *But see conflict below* — short-window momentum is strongly positive: 1m +13.6%, 3m +24.3%, 6m −1.9%. |
| **Quality** | ROE **−28.55%**, GP/Assets **0.00**, accruals **−3.7%**, **Piotroski F = 1/9** (Weak) | n.m. | **Strong Sell** — F‑score 1 with only 1 of 9 checks passed (accruals quality). Components: no positive ROA, no positive operating CF, no ROA improvement, leverage/equity/dilution/gross-margin/turnover all fail. |
| **Low Vol** | Ann. vol **59.5%** (252d) / **56.6%** (365d), beta **1.15–1.16**, max DD **−27.95%** | n.m. | **Strong Sell** — vol ~4x SPY, beta modestly >1. No low‑vol premium, pure idiosyncratic risk. |
| **Earnings Revision** | "**+170% upgrade**" (EPS $2.19 vs −$3.13) | n.m. | **INVALID — do not use.** This is *not* a revision. The tool compares **FY2030** EPS (+$2.19) against **FY2029** EPS (−$3.13) — two different forecast periods, i.e. the path to profitability, not analysts changing their minds. FY2030 carries **2 analysts** (revenue: 6). Statistically unusable. |

**Sector rank unavailable.** `get_sector_peers` returned mega-cap pharma/drug manufacturers (LLY $1.32T, JNJ, ABBV, MRK, UNH…) — **not** valid comparables for a $9B clinical-stage vaccine company. Cross-sectional ranking against that list (or against the default 25-name mega-cap universe returned by the ranking tool) would be a category error. Treat all ranks as missing data, not zero.

### 2. Price Statistics (365-day window, benchmark SPY)

| Metric | Value |
|---|---|
| **Alpha (annualised)** | **+40.1%** |
| **Beta** | **1.154** (profile 5y beta 1.289) |
| **R² vs SPY** | **0.093** — only 9.3% of variance is market-explained |
| Annualised return | +58.2% |
| Annualised volatility | 56.6–56.8% |
| **Sharpe** | **1.02** (365d) / 0.65 (252d, 59.5% vol) |
| **Sortino** | **2.05** (upside/downside dispersion ratio 2:1) |
| Max drawdown | **−27.95%** |

**Statistical caveat:** with R² = 0.09, the +40.1% alpha is estimated off a regression explaining almost nothing. Standard error on annualised alpha in this specification is roughly 40–55pp, implying **t ≈ 0.7–1.0 — not significant**. The alpha is real arithmetic, not a proven edge. Bear the true driver in mind: binary clinical catalysts, not a repeatable factor premium. Sortino 2.05 vs Sharpe 1.02 confirms returns are driven by a few large positive jumps with clustered downside.

### 3. Composite Quant Signal: **NEUTRAL**
(no short-sale recommendation: 59% vol, binary catalysts, and heavy short interest make an outright Sell a poor risk-adjusted expression)

Reasoning: three of five factors are uninformative or structurally negative for a pre-revenue biotech; momentum is genuinely ambiguous; quality and low-vol are decisively bad. Nothing here is a high-quality quant long — and nothing here is a clean short either. **This is an event-driven holding, not a factor holding.** Position sizing should be set by catalyst probability and cash runway, not by factor scores.

### 4. Key Quant Risk Flags

1. **DATA CONFLICT on momentum — resolve before acting.** Tool momentum = +0.75% (flat). The price history I retrieved begins **2025‑09‑02 at $31.56** and ends **$60.81** → **+92.7%**. A 252-trading-day lookback from 2026‑09‑01 anchors near late‑Aug 2025, implying PCVX traded ~$60 *before* the visible series starts and fell ~47% into early September 2025. Either (a) a genuine ~47% single-event repricing occurred, or (b) the feed is truncated/gapped. **Consequence: 12‑1 momentum is flat only because it straddles that break.** Re-based from Sep‑2025, the trend is unambiguously up (+93%; new highs — close $63.30 on 2026‑08‑19, only −3.9% off). *Momentum reversal risk is moderate-to-high* precisely because the trailing 6-month return is already flat (−1.9%) after a +93% run — classic late-stage momentum deceleration.
2. **Binary/factor-crowding risk.** 91% idiosyncratic variance = no diversification benefit; correlation to SPY (0.30 by R²) offers no hedge value. Reverse-merger/liquidity and index-flow effects are the real risk drivers.
3. **Liquidity: acceptable but thin at the tails.** Median volume ~1.0–1.2M shares (~$65M/day) — fine for institutional positions up to a few hundred $M, but drawdown events came on volume spikes (5.3M sh 2026‑05‑07 as price fell $57.10→$51.48).
4. **Runway/quality flag.** Piotroski 1/9, FY2025 operating cash burn **−$655.6M**, R&D-and-capex heavy (PP&E $371M→$663M in one quarter). Latest reported cash + ST investments **$1.29–1.49B** vs ~$270M/quarter implied burn → **~5 quarters of runway before financing risk**, i.e. dilution probability is material inside a 2-year horizon. Note: the balance sheet contains a period dated 2026‑09‑30 with a 2026‑11‑04 filing date — **future-dated data, treated as unreliable**; I used the 2026‑06‑30 quarter.
5. **Estimate dispersion.** FY2027–28 EPS estimates span wide ranges (e.g. FY2028 −$8.10 to −$3.48 on 6 analysts); FY2030's +$2.19 single-point value with 2 contributors is a placeholder, not a consensus. **Do not build a DCF or PEG off it.**

**Sample-size disclosure:** effective fundamental sample = 0 revenue periods, 0 profitable years, 4 loss-making cash-flow years, 2 covering analysts on the first projected profitable year. Fundamental factor statistics on PCVX are not statistically meaningful; the only statistically usable series is price (≈250 observations).
