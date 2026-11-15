# Quant Analyst

- Symbol: CBRS
- Elapsed: 59.0s

---
## CBRS — Cerebras Systems Inc. | Quantitative Factor Report
Price $108.72 · Mkt cap $24.63B · EV $22.55B · Technology / Semiconductors · IPO 2026-05-14

### ⚠️ Data-integrity note before the scores
CBRS has only **127 trading sessions** of history (IPO 2026-05-14 → 2026-11-13). Every "252-day" metric returned by the factor engine is computed on this 126-return sample. Two artifacts were identified and corrected:

1. **Annualized return / alpha are corrupted.** Reported `annualised_return = -144.39%` and `alpha = -154.73%` are 2× simple annualization of **386.34 → 108.72**, i.e. the engine is using the **IPO-day intraday high**, not the IPO-day close (311.07). True close-to-close return is **-65.05%**. Corrected geometric annualized return ≈ **-87.8%**, corrected alpha ≈ **-90%**.
2. **The +609% earnings revision is a period mismatch, not a revision.** The engine compared FY2028 EPS ($8.79) against FY2027 EPS ($1.24). Genuine same-period revision data is unavailable.

---

### 1. Factor Scores Table
Ranks are within a 5-name comp set (CBRS, NVDA, AMD, AVGO, MU), equal-weight. Sector rank 1 = best.

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| Value | 5 / 100 | 5 of 5 | **Strong Sell** |
| Momentum | 5 / 100 | 5 of 5 | **Strong Sell** |
| Quality | 5 / 100 | 5 of 5 | **Strong Sell** |
| Low Vol | 5 / 100 | 5 of 5 | **Strong Sell** |
| Earnings Revision | n/a | n/a | **Unscoreable** (artifact; see below) |

**Value — bottom of set.** P/E 265.2× (worst), EV/EBITDA 80.7× (2nd worst, and built on a fabricated EBITDA), P/FCF **-59.6×** (negative). P/B is **undefined** — book value per share is **-$2.69** (negative equity). EV/Sales **44.2×**, P/S **48.3×**. Peer P/E: MU 10.5, NVDA 33.2, AVGO 72.8, AMD 201.5.

**Quality — bottom of set on every sub-metric.** ROE **-41.1%**, gross-profit/assets **8.56%** (NVDA 74.2%, MU 54.9%), accruals **+10.66%** (the only positive accruals in the set ⇒ lowest earnings quality). Piotroski F-Score **5/9**, failing F2 (positive operating CF), F4 (accruals), F8 (gross-margin improvement — 42.3%→39.0%), F9 (asset turnover). The reported ROIC of **45.85% is not credible** and should be disregarded: it is derived from a $244.9M "EBIT" figure while *operating income is -$145.3M*.

**Momentum — bottom of set.** -39.8% on the engine's 12-1 window; -28.4% (63d); **-65.05% since IPO close**; -71.9% from the day-1 high. Peers: AMD +8.1%, MU -0.3%, NVDA -2.1%, AVGO -21.7%.

**Low Vol — worst in set.** Annualized vol **113.8%** (vs NVDA 39.9%, AVGO 48.0%, AMD 76.2%, MU 87.5%). Beta 2.81–2.84.

**Earnings Revision — treat as blank, not bullish.** Consensus curve is *unstable, not rising*: FY2026 **-$0.52** (loss, 2 analysts) → FY2027 +$1.24 (5) → FY2028 +$8.79 (3 analysts, range **$5.56–$14.81**, a 2.7× spread). Direction of target price changes is **down**: Mizuho cut to $240, Needham cut to $200, Wedbush cut to $190 (then raised to $205 on 11/13), Morgan Stanley $279 in Aug. Five of six recent actions were reductions.

---

### 2. Price Statistics (126 trading days)

| Metric | Value |
|---|---|
| Beta vs SPY | **2.84** |
| R² vs SPY | **0.125** (corr 0.425–0.43) |
| Alpha (annualized) | -154.7% reported / **≈ -90% corrected** |
| Sharpe | -1.269 reported / **≈ -0.77 corrected** |
| Sortino | -2.492 reported / **≈ -1.5 corrected** |
| Sharpe (63d) | -2.190 |
| Sortino (63d) | -3.831 |
| Annualized vol | **113.8%** (63d: 88.0%) |
| Max drawdown | **-73.73%** (close-to-close: 311.07 → 81.71) |
| Return since IPO close | -65.05% |
| Return off 11/05 low | **+39.7%** (5-day: +21.2%) |

**Beta is technically significant but economically unusable:** SE(β) ≈ 0.67 (t ≈ 4.2), yet R² = 0.125 means only ~12.5% of variance is market-driven. Hedging market risk removes almost none of the exposure. Correlation to peers is the **lowest in the comp set** (NVDA 0.44, AMD 0.47, MU 0.48, AVGO 0.38, vs AMD–MU 0.76 within the peer group): CBRS is a standalone idiosyncratic bet, not a semis proxy.

**Downside skew is severe:** Sortino/Sharpe = 1.96, i.e. downside volatility is roughly double total risk-adjusted dispersion.

---

### 3. Composite Quant Signal: **SELL**

The four scoreable factors each rank **5 of 5** and average **5/100**, which mechanically maps to *Strong Sell*. I am exercising one notch of restraint to **Sell**, for four reasons:

- **One factor is genuinely unscoreable**, not negative (earnings revision). A Strong Sell requires all five in the bottom quintile.
- **Sample size (126 days)** is far below the 12-month minimum for momentum and low-vol factor validity — this is a 6-month post-IPO window dominated by offering dynamics, not a factor signature.
- **Cross-sectional rank is a cohort mismatch.** The available "sector peers" are $0.4–4.9T mega-caps; ranking a $24.6B six-month-old IPO against them tests size, not quality of business.
- **Short-term reversal is inflecting**: +39.7% off the 11/05 low, +21.2% in five days on 36.9M shares (≈4.7× average). The one signal that could turn first (short-term reversal) already has.

**Directional conviction: high on the negative fundamental/valuation read, low on the tradable-timing read.**

---

### 4. Key Quant Risk Flags

1. **Negative equity.** BVPS -$2.69. No book-value floor; P/B undefined; any debt or raise reprices equity from a negative base.
2. **Earnings quality is poor.** FY2025 net income **+$237.8M** against operating cash flow **-$10.1M** — a **~$248M gap**, with operating income at **-$145.3M**. The only profitable year on record is an artifact of ~$383M of non-operating items. Accruals ratio +10.66% (warning). The P/E of 265× and EV/EBITDA of 80.7× carry **no information**.
3. **IPO lockup / supply overhang.** IPO 2026-05-14 → the standard 180-day lockup expires ≈ **2026-11-10**, coinciding with the -15% slide into the 11/05 low (77.84). Residual supply risk is unresolved.
4. **Valuation embeds a flawless ramp.** 44× EV/Sales on $510M revenue requires delivery of consensus $2.93B (FY2027) and $7.64B (FY2028) — a ~4.4× revenue increase in two years. Estimate dispersion (FY2028 EPS $5.56–$14.81) means the market has no agreed earnings anchor.
5. **Momentum-reversal and factor-crowding risk in both directions.** AI-infrastructure semis are the most crowded long in the market; CBRS layers single-name execution risk on top of that factor exposure while offering *low* correlation to the factor itself (0.38–0.48) — it will not be carried by a sector rally.
6. **Event gap risk.** Volume spikes to 17–37M shares on news days vs ~7.5M average; expect double-digit single-session gaps. Liquidity itself is adequate (~$800M/day notional).
7. **Extreme volatility regime.** 113.8% annualized vol prices options at levels where small position sizing is mandatory; a 2.84 beta computed off 126 observations should not be used for hedge sizing.
8. **Statistical caveat, stated plainly:** no metric here clears a 12-month minimum for factor inference. The momentum, low-vol, beta and alpha figures are **directional indicators from a six-month window, not validated factor loadings**. The value and quality reads, by contrast, rest on audited FY2022–FY2025 statements and are robust to sample size.

**Bottom line:** CBRS screens in the bottom quintile on all four scoreable factors, destroys 65% of value in six months with 114% volatility and a -74% drawdown, earns no risk-adjusted return on any window, and offers no valuation support (negative book, negative FCF, 44× sales). The sole offsetting data point is revenue growth of +75.7% YoY off a 175% three-year CAGR — a real operating story, but one that is fully priced and unfinanced by internal cash flow.
