# Quant Analyst

- Symbol: HUBS
- Elapsed: 71.8s

---
## HUBS (HubSpot, Inc.) — Quantitative Factor Report

Price ~$244–251 (last close 2026-03-31: $244.10) | Mkt cap ~$13.0B | EV ~$11.9B | Technology / Application Software

**Comparable set used:** CRM, NOW, WDAY, TEAM, DOCU, ZM. The `get_sector_peers` feed returned only mega-cap semis/hardware (NVDA, AAPL, TSM…) — not valid comparables for mid-market application software — so ranks below are computed against the hand-built software comp set (n=6–7). Small-sample caveat applies throughout.

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| Value | GAAP-cheap **no**: P/E 291.6x, EV/EBITDA 57.6x, P/B 6.46x; cash-cheap **yes**: P/FCF 18.85x | ~4th of 7 (~25th pct composite) | **Weak / Neutral** |
| Momentum | **−52.7%** 12-1m (raw price: 582.11 → 275.37); +0.13% from tool (see data flag) | 7th of 7 (bottom decile) | **Strong Sell** |
| Quality | ROE 2.22%, ROA 1.19%, ROIC 0.49%, GP/Assets **0.681**, Accruals **−0.186**; F-Score **7** | ~4th of 7 (~50th pct) | **Neutral** |
| Low Vol | Vol 79.9% (252d) / 65.9% (504d), max DD **74.7%**, beta 0.35–0.80 | 6th of 6 (worst) | **Strong Sell** |
| Earnings Revision | +15.2% (FY2030 EPS 23.45 → 27.02) | 3rd of 6 (~50th pct) | **Neutral / mild Buy** |

**Composite percentile ≈ 29 → Sell.**

**Value — the split is the story.** On GAAP earnings HUBS is the most expensive name in the comp set (P/E 291.6x vs ZM 15.8x, CRM 31.1x). On cash flow it is not: P/FCF 18.85x sits mid-pack (DOCU 15.5, ZM 15.6, CRM 16.1 ahead of it). On consensus (adjusted) EPS the picture inverts again: 2026E $13.30 → **forward P/E ~18.4x**; 2027E $16.90 → ~14.4x. The 291x trailing multiple is a GAAP-earnings artifact (net income $45.9M vs operating cash flow $760.7M), not a cash-flow statement. Value is genuinely cheap on cash and forward adjusted earnings, expensive on the printed multiple.

**Quality.** Genuinely high gross economics — gross profit/assets 0.681 is 2nd of 7 (only TEAM higher) — and accruals of −0.186 mean earnings are heavily cash-backed (OCF $760.7M vs NI $45.9M). But ROE of 2.22% is 6th of 7 and ROIC 0.49% is barely positive. ROIC trajectory is the one clear positive: −9.47% (2023) → −2.55% (2024) → +0.49% (2025). F-Score 7 is "moderate," failing only F7 (share count rose) and F8 (gross margin did not improve).

**Revisions.** +15.2% looks constructive but is **not usable as a conviction signal**: the revision window is the FY2030 period, which carries **num_analysts = 1** for EPS. Confidence interval on a one-analyst FY2030 number is effectively unbounded. Revenue coverage is broader (9–25 analysts) and implies ~18% growth in 2026, decelerating to ~14% by 2028 — respectable but not accelerating.

### 2. Price Statistics

| Metric | 504-day (2y) | 252-day (1y) |
|---|---|---|
| Annualised return | **−46.47%** | — |
| Alpha vs SPY (ann.) | **−60.82%** | — |
| Beta vs SPY | 0.798 | 0.349 |
| R² | **0.0223** | — |
| Volatility (ann.) | 65.94% | **79.93%** |
| Sharpe (0% rf) | **−0.708** (alt calc −0.64) | −0.256 |
| Sortino | **−0.959** | — |
| Max drawdown | **−74.67%** | −54.71% |

Referencing: peak close $819.71 (2025-02-13; ATH intraday $881.13) → −70% from high; Feb-2026 low $209.33 (2/11) → now +16.6% off the low; last 3 months −39.2%; last month −7.7%. Profile beta 1.235 (long-run) vs 0.35–0.80 computed — the spread is itself the finding.

**Statistical significance flags (important):**
- **Alpha is not significant.** Residual vol ≈65%; over 2 years SE(annualised alpha) ≈ 46%, so t ≈ **−1.3**. The −60.8% alpha is economically large but statistically indistinguishable from zero — it is one idiosyncratic repricing, not a reliably estimated edge.
- **Beta is not estimable.** SE(beta) ≈ 3.1; the estimates 0.35 / 0.80 / 1.235 are mutually within noise. **Do not size hedges or factor-risk budgets off HUBS beta.**
- **R² = 0.0223**: 97.8% of HUBS variance is stock-specific. Market/factor exposure explains almost nothing; this is a single-name event-risk position, and diversification benefit is minimal.

### 3. Composite Quant Signal

**SELL** (composite ≈ 29th percentile). Momentum in the bottom decile, volatility worst-in-class, Sharpe and Sortino both negative over two years, and four separate >9% single-day gaps in the last five months. The offsets are real but not yet scoreable: P/FCF 18.85x, ~18x forward adjusted EPS, improving ROIC, cash-backed accruals, and mildly positive long-dated revisions.

This is a **falling-knife with improving fundamentals** — a setup that becomes a Buy only on evidence of momentum stabilisation (e.g., 3-month relative performance turning positive and volatility rolling over), not on valuation alone. Valuation breadth is not a catalyst in a 0.02-R² stock.

### 4. Key Quant Risk Flags

- **Momentum reversal / continuation risk (high).** −52.7% 12-1m, deeply negative; no sign of trend repair yet (1m still −7.7%).
- **Event/gap risk (high).** −15% (2025-11-06), −11% (2026-01-29), −12.5% (2026-02-03), −9.5% (2026-02-11) on 2.3–4.0M shares (4–7× normal). Earnings-day binary risk dominates the return distribution.
- **Volatility/factor risk (high).** 80% annualised vol and 74.7% drawdown — worst of the 6-name comp set on both. Any risk-parity sizing collapses the position to a rounding error.
- **Factor crowding (low).** Departed from the growth/momentum factor long ago; HUBS is not a crowded momentum name. Its risk is the opposite — being abandoned.
- **Liquidity (not a flag).** ~1–2M shares/day, ~$300M+ turnover. Adequate for institutional position sizes.
- **Data-integrity flags.** (a) `calculate_momentum_score` returned **+0.13%** where raw adj-close prices imply **≈−52.7%** over the same 12-1m window — treat the momentum tool output as unreliable for HUBS and use the price-derived figure. (b) Low-vol beta (0.349, 252d) conflicts with the profile beta (1.235) — see significance note. (c) The quality factor labels both HUBS and CRM "low" and only DOCU/ZM "high," a coarse ROE-driven binary that masks HUBS's top-decile gross-profitability and accruals profile. (d) Peer sample n=6–7; factor percentile ranks are directional only and no rank should be read as statistically robust.
