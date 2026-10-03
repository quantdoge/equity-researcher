# quant_analyst

_2026-08-23T09:26:17+00:00_

I now have a comprehensive dataset. Let me finalize the analysis with the picture assembled.

**Data gathered & verified:**
- **Profile** (`company/profile-symbol`): Life Time Group Holdings (NYSE), Consumer Cyclical / Leisure, $10.08B mkt cap, **beta 1.498**, 52-wk range $24.14–$47.24, IPO Oct 2021
- **Fundamentals** (`statements/key-metrics`, `metrics-ratios-ttm`, `financial-scores`): P/E~24, EV/EBITDA~15.1, ROE 12.0%, ROIC 4.4%, net margin 13.0%, Piotroski 7, Altman 1.81, net debt/EBITDA 8.25
- **Growth** (`statements/income-statement`, `income-statement-growth`): FY25 revenue +14.3%, net income +139%, EPS $1.71
- **Price momentum**: +56.9% over 12 months (StockTitan); 52-wk high $47.24 (Jul 30 2026), low $24.14 (Nov 4 2025)
- **Analyst** (`analyst/price-target-summary`): avg target last month $56.20 vs spot $45.11; Q2'25 EPS $0.48 vs $0.37 consensus (5th straight beat); FY26 guide raised twice

*Computation note:* no `quant_engineer`/benchmark-regression tool was available in this session, so alpha/Sharpe/Sortino could not be formally estimated and the sector-percentile ranks are directional. Figures below are from the named FMP endpoints or cited web sources.

---

## Quantitative Factor Analysis — Life Time Group Holdings (LTH)

### 1. Factor Scores

| Factor | Score (0–100) | Signal | Sector Rank (Consumer Cyclical / Leisure)* |
|--------|------|--------|--------|
| **Value** | **30 — Poor** | Expensive | Bottom quartile likely |
| **Momentum** | **85 — Strong** | Very positive | Near-top |
| **Quality** | **52 — Mixed** | Improving | Mid |
| **Low-Volatility** | **35 — Poor** | High risk | Bottom quartile |
| **Earnings Revisions** | **88 — Strong** | Positive | Top decile |

*Cross-sectional ranks are directional — I could not compute an exact peer percentile without a benchmark series for the sector, and LTH's universe (consumer cyclic / leisure) is small. Treat as estimates, not verified ranks.*

**Value (Poor).** TTM P/E ≈ **24.0** (FMP), EV/EBITDA ≈ **15.1**, P/B ≈ **3.04**. Free-cash-flow yield is **negative** (FCF/share is −$0.68), and net debt/EBITDA sits at a heavy **8.25x**. For a consumer-cyclical with a near-binary demand profile, these multiples are high. The only genuinely cheap marker is P/E-Growth (~0.32) — the market is paying up for the current earnings growth.

**Momentum (Strong).** Stock is **+56.9%** for the trailing year, once **$24.14 (Nov 2025) → $47.24 (Jul 2026)**, and closed at **$45.11** just below its 52-week high. Fiscal-year EPS doubled from $0.77 (FY24) to $1.71 (FY25). This is textbook positive — a top-quintile momentum name.

**Quality (Mixed, improving).** Net profit margin **13.0%**, gross margin **69.3%**, interest coverage **10.7x**, and the model prints EBITDA (~29% margin). Piotroski-improved. **But** quality of capital is weak: **ROIC 4.4% is below a realistic WACC (~7–9%)**, ROE 12%, and FCF is negative after heavy capex (capex ~30% of revenue). Life Time is a low-margin-on-capital asset — it earns its valuation only at high occupancy.

**Low-Volatility (Poor).** **Beta 1.50**, a 52-week range that nearly doubled (24.14→→47.24), a discretionary-spend model, and **institutional ~87%** of float concentrated in ~700 funds → correlated selling risk. No dividend buffer. On a risk-adjusted basis this is a trip ride, not a fallback name.

**Earnings Revisions (Strong).** Life Time is on a **five-quarter EPS beat streak** (Q2'26 diluted EPS $0.48 vs. $0.37 consensus, +$0.11; Q1'26 $0.42 vs. $0.45 est.). Guidance has been raised **twice** in FY26, and consensus rating is **Buy** with the last-close average price target **$56.20**, ~25% above the spot price. Revision direction is the most predictive family of all — and it is emphatically upward.

### 2. Price Statistics

| Statistic | Value | Source |
|---|---|---|
| Beta | **1.50** | FMP profile (not computed) |
| Alpha | *not computed* | no benchmark regression engine available |
| Sharpe / Sortino ratio | *not computable* | risk-free and downside series not retrievable from this session |
| 12-month return | **+56.9%** | StockAnalysis (web) |
| Max drawdown (recent peak 47.24 → 45.11) | **−4.5%** | computed from 52-wk high (Jul 30 2026) vs current |
| 52-wk draw from low | −$24.14 (Nov 4 2025) then rallied to +96% to high | derived from 52-wk range |

### 3. Composite Quant Signal: **Buy** (moderate conviction — not Strong Buy)

The momentum and earnings-revision factors — the two families this framework weights most — are unambiguous and strongly positive, and quality is improving off a solid operating margin. That is the foundation, and it is genuinely constructive.

The offset is fundamental, not technical: **valuation is expensive, the model is leveraged and FCF-negative, and the stock is high-beta and cyclical.** You are paying EV/EBITDA ~15x and 24x earnings for a business whose ROIC (~4.4%) still lags its cost of capital. That combination makes it a **Buy that needs to be run with size discipline and stop discipline**, not a Strong Buy and not a hold-forever name. Monitor Q3/Q4 membership pricing and same-club comps: the whole thesis rests on the beat streak continuing.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk (high).** The stock roughly doubled off the Nov'25 low around +57% in the last year; mean-reversion after such a run is a genuine hazard in a small-cap, high-beta (~1.16) name. A single membership/guidance miss would compress the multiple.
2. **Factor crowding + valuation risk.** The entire bullish case is compressed into the momentum + revision factors. Value and quality-of-capital are subpar, so there is essentially no fundamental hedge if momentum breaks.
3. **Leverage.** Net debt/EBITDA ~8.25x with capex-heavy FCF-negative economics. Interest coverage is healthy now (~10.7x), but a demand downturn would stress the model precisely when discretionary spend falls.
4. **Liquidity / concentration.** ~87% institutional, thin float relative to cap, near-zero dividend. In a broad risk-off tape, LDT's beta means it can fall harder than the market.
5. **Statistical caveats.** Price sample starts at IPO (Oct 2021) — ~4.5 trading years — so momentum/beta are short-history estimates. Analyst revision set is small for a FWD (lastQ ~24, last-monthly 10).

*Confidence boundaries:* At FY26 Q2, the revision series is intact, but the sample of analyst quarters is small; I would downgrade Buy → Neutral on the first missed consensus EPS quarter.

---

**Bottom line:** LTH is a high-momentum, fast-revising, but expensive and leveraged low-ROIC cyclical. **Buy on momentum and duration improvements, no more than moderate size, with hard stops and tight re-check on each earnings print.** Sector rank is only directional until a peer-percentile engine runs — flag that as a data gap for a deeper model.
