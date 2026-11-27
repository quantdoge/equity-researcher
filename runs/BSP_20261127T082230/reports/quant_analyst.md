# Quant Analyst

- Symbol: BSP
- Elapsed: 47.9s

---
## Bending Spoons S.p.A. (BSP) — Quantitative Factor Report
**Price $46.29 | Mkt cap $29.4B | EV $29.77B | Sector: Technology / Software–Application (Italy) | IPO 2026-07-01**

⚠️ **Critical sample-size caveat up front:** BSP listed on 2026-07-01. All price-based statistics below rest on **~103 trading days (≈0.41 years)** of data, and the data feed's "252-day" windows silently truncated to what exists. Every annualised price number here is a 5-month extrapolation. Fundamental factors use FY2023–FY2025 annuals (3 observations).

### 1. Factor Scores

| Factor | Score | Sector Rank (est.) | Signal |
|--------|-------|--------------------|--------|
| **Value** | 12 / 100 | Bottom decile | **Strong Sell** — trailing EV/EBITDA 72.5x, P/FCF 95.6x, P/B 27.9x, P/E n/a (FY25 EPS ≈ $0.00). Only the forward curve rescues it: 18.2x EV/EBITDA on FY26E, 12.5x on FY27E |
| **Momentum** | 62 / 100 | Top tercile | **Buy** — 12-1 momentum **+21.3%** (truncated window, ~82 td); +14.3% since IPO close, +49.3% off the $31.00 first print; 3-month return +9.0% |
| **Quality** | 34 / 100 | Third quintile | **Weak** — internal "low" signal. ROE −0.01%, ROIC 7.58% and **falling** (11.60% → 8.47% → 7.58%); Piotroski **4/9** (weak). Offsets: GP/assets 0.180 (decent), accruals −6.11% (excellent, cash-backed) |
| **Low Vol** | 8 / 100 | Bottom percentile | **Strong Sell** — 110.2% annualised vol, max DD −40.1%. Beta 0.92 is *not* a mitigant (see §2) |
| **Earnings Revision** | 84 / 100 | Top quintile | **Buy** — FY27 consensus EPS **$2.28 vs $1.49 (+53.0%)** over 3 months; FY26 $1.49 on $2.95B rev. PTs: 5 raised / 2 cut in 8 notes |

**Composite draw:** cheap-on-nothing valuation, elite revision momentum, deteriorating returns on capital, near-maximum volatility. Factor signals conflict — that is a **Neutral**, not a Buy.

### 2. Price Statistics (103 td, benchmark SPY)

| Metric | Value | Reliability |
|---|---|---|
| Annualised return | **87.78%** (arithmetic) | ⚠️ Geometric-consistent = **+38.7%**; actual cumulative = **+14.3%** |
| Annualised vol | **110.24%** (daily ≈ 6.9%) | Usable, but regime-dominated |
| Beta vs SPY | **0.933** (α/β tool) / 0.924 (low-vol tool) | ❌ **Not significant.** R² 0.0205; SE(β) ≈ 0.72, t ≈ 1.3, 95% CI ≈ [−0.5, +2.3] |
| Alpha (annualised) | **+94.97%** | ❌ 98% of variance is idiosyncratic; this is the IPO/listing pop, not skill. Geometric-consistent alpha ≈ +27% |
| Sharpe | **0.796** (0% rf) | SE ≈ 0.11 → 95% CI ≈ [0.57, 1.02]; geometric-consistent ≈ **0.35** |
| Sortino | **1.603** | Fragile — downside deviation from very few down days; one −27% episode |
| Max drawdown | **−40.1%** (tool series) | Close-to-close check: **−27.4%** (Oct 15 close 55.77 → Nov 11 close 40.50). Intraday Aug 11 58.94 → Sep 22 35.60 = −39.6% |

**Return decomposition — the honest picture:** two sessions generate most of the performance: **Oct 14 +41.2%** (gap-open +32.9%, 19.7M shares) and **Aug 10 +15.7%**. Ex-those two days the series is roughly flat-to-down since mid-August. A Sharpe built on 2 of 103 observations is not an estimate of anything stable — treat 0.80 as an upper bound and 0.35 as the fair geometric read.

### 3. Composite Quant Signal: **NEUTRAL**
Revision momentum (+53% FY27 EPS, PT median $47.50 vs $46.29 spot = +2.6%; mean $50.16 = +8.4%) offsets a bottom-decile value score and bottom-percentile volatility. The stock is priced for flawless execution of an acquisition-led margin ramp (EBITDA margin 31% FY25 → **55% FY27E** consensus, net income $892M FY26E from ~$0 FY25) while carrying leveraged-rollup risk. **Verdict: Neutral / hold-sized, not a factor-portfolio long.** Any position is a volatility bet, not a quality or value bet.

### 4. Key Quant Risk Flags
1. **Statistical insignificance (highest severity).** 103 days → beta, alpha, and R² are uninformative; Sharpe CI spans 0.57–1.02; the 12-1 momentum window is 82 days, not 12 months. Do not let these numbers into a factor model with normal weights.
2. **Event concentration / momentum-reversal risk.** +41% single-day gap leaves a large unfilled gap zone (37.9→50.3); momentum this dependent on gap days mean-reverts violently. Compression from $59.50 intraday high already −22%.
3. **Lock-up overhang.** 180-day post-IPO lockup expires ~late-Dec 2026/Jan 2027 — a dated supply shock immediately ahead.
4. **Leverage vs. interest coverage.** FY25 interest expense $142.6M vs EBIT $253.8M = **1.78x coverage** (2023: 4.4x). Debt-funded M&A model is rate- and EBITDA-sensitive; Piotroski F5 (lower leverage) fails.
5. **Dilution.** Diluted shares 518.6M → 596.8M → 598.9M (+15.5% over 2 yrs); F7 (no new shares) fails. Acquisition currency risk.
6. **Earnings-quality optics.** Negative accruals (−6.11%) are genuinely good (OCF $290.6M vs NI ≈ −$0.14M), but GAAP net income is zero — the OCF/NI gap is D&A ($157M) plus non-cash comp. The quality score is carrying one strong leg and two weak ones.
7. **Thin coverage & dispersion.** Only 5–6 EPS analysts, 7 revenue analysts; PT range **$36–$72 (2.0x)** — revision momentum of +53% off a 5-analyst base is a low-confidence signal.
8. **Data gaps (disclosed, not hidden):** no P/E (negative/nil earnings); no dividend; **no valid application-software peer set** — `get_sector_peers` returns only mega-cap Technology (AAPL, MSFT, NVDA, TSM, AVGO), so no true cross-sectional sector rank exists and my quintile ranks above are judgement, not computed percentiles. No quarterly data available to test revision trajectory within years. Ratings field is null in all price targets.

**Falsification triggers:** any FY26 revenue guide below $2.82B (low end), EBITDA margin guidance under ~45%, or a financing event that pushes coverage below 1.5x → revision score flips and the Neutral becomes Sell. Conversely, two more consecutive upward FY27 revisions with the lockup absorbed cleanly would justify Buy despite the valuation.
