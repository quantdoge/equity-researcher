# Quant Analyst

- Symbol: SKHY
- Elapsed: 61.2s

---
## SKHY (SK hynix Inc. — US ADR) — Quantitative Factor Report

**Price $164.70 · Mkt cap ~$1.17T · Technology / Semiconductors · 78 trading days of history (first trade 2026-07-10)**

> **DATA INTEGRITY WARNING — read before using any number below.** Two vendor defects materially change interpretation:
> 1. **Sample size:** the ADR has traded only **78 sessions** (2026-07-10 → 2026-10-28). Every "252-day" metric returned is annualized from ~77 returns (<1/3 of a year). Beta, alpha and Sharpe carry very wide error bands.
> 2. **Currency mismatch:** valuation fields divide a **USD** price by **KRW** financials. P/E "0.03" = 164.70 ÷ 5,668 (FY25E EPS in *won*). The raw value-factor and valuation-ratio outputs are **unusable** — plugged into a screen, SKHY would spuriously rank the cheapest stock in the universe.

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **n/a — vendor field corrupted.** Manual: FY26E EPS 34,949 KRW (~$25.3 @1,380) → **P/E ~6.5x**; FY27E ~4.8x. P/B unresolvable (BVPS field 10x off) | Unrankable | **Unverifiable — do not act** |
| **Momentum** | **+7.1%** (12-1 proxy, tool); manual inception-to-t ≈ −2.0% | **2 of 2** (MU +9.7%) | Mild positive, **decaying** |
| **Quality** | ROE **35.6%**, GP/Assets **0.333**, accruals **−0.059** (excellent), **F-Score 8/9** | **2 of 2** (MU ROE 61.4%, GP/A 0.549) | **Positive** |
| **Low Vol** | Vol **101.8%**, beta **3.51** | **2 of 2** (MU 84.2% / 3.33) | **Strong negative** |
| **Earnings Revision** | **VOID** — reported +57.15% is an artifact | **n/a** | **No signal** |

**Why the revision score is void (important):** the tool's "3-months-prior estimate" for FY2030 (69,053.78) is *identical* to the current FY2029 estimate (69,053.78). The +57% is simply the FY30÷FY29 estimate ladder, not a revision. The out-year estimates rest on **2–3 analysts** and imply revenue of 358T KRW in FY26 → 1,193T by FY30 (3.8x in one year, ~18%/yr after) — not credible. **No usable revision read.**

**Value caveat — cyclical trap:** ROIC went 7.7% (2022) → **−9.0% (2023)** → 23.6% (2024) → **32.5% (2025)**. A 6.5x multiple on peak-cycle earnings is the classic memory value trap; normalize-cycle EPS is far below consensus.

### 2. Price Statistics (78 obs — all low confidence)

| Metric | SKHY | MU (comp) |
|---|---|---|
| Alpha (ann., vs SPY) | **+11.59% — statistically zero** (SE ≈ ±169%, t ≈ 0.07) | — |
| Beta vs SPY | **3.51** (SE ±0.99, t ≈ 3.5) | 3.33 |
| R² vs SPY | **0.141** — SPY explains only 14% of variance | — |
| Sharpe | **0.418** | 1.79 |
| Sortino | **0.827** (downside vol ~51%) | 3.10 |
| Ann. volatility | **101.8%** | 84.2% |
| Max drawdown | **−34.61%** | −39.1% |
| Realized cumulative return | **−1.95%** since listing | — |
| Arithmetic ann. return (tool) | +42.6% | +152% |

Sharpe/Sortino are **not comparable to MU**: SKHY's are 78-day estimates, MU's are 252-day. Sortino > Sharpe 2x tells you the return distribution is violently right-skewed (+27.3% on 7/14, −11.7% on 7/28) — long-gamma payoff, not steady compounding. The +42.6% "annualized return" vs −1.95% *realized* gap is pure **volatility drag (~44 pts)**.

### 3. Composite Quant Signal: **NEUTRAL** (speculative, low conviction)

Strong business quality (F-Score 8, negative accruals, 32% ROIC) is real, but it is **fully offset**: unverifiable valuation, >100% vol with beta ~3.5, a 34.6% drawdown, momentum rolling over, and no valid revision signal. Not investable on quant evidence alone — the sample cannot support a Buy.

### 4. Key Quant Risk Flags

1. **Sample-size risk (highest):** 78 obs. Alpha is noise (t≈0.07); beta SE ±1.0. Any annualized stat here is indicative only.
2. **Momentum reversal:** 12-1 is +7.1%, but the **last 21 sessions are −11.8%** (186.68 → 164.70) and the stock is −17.1% off its 198.63 close high. Trend has already broken.
3. **Factor crowding / redundancy:** **0.81 correlation with MU** — SKHY delivers almost nothing new alongside memory exposure. NVDA 0.46, SPY 0.37 (low market beta-relevance).
4. **Model/data risk:** corrupted valuation fields will misfire any automated value screen by ~4 orders of magnitude. **Exclude SKHY from cross-sectional value ranking until fixed.**
5. **Cyclical earnings risk:** peak ROIC + commodity DRAM/NAND pricing; FY25E P/E ~40x vs FY26E ~6.5x requires a 6x EPS step-up that hinges on only 6 analysts.
6. **Liquidity: NOT a flag** (10–108M shares/day, $1.6–18B notional). The real structural risk is post-IPO ADR float/lockup and index-inclusion flows.

**Gaps:** no clean P/B or EV/EBITDA; no valid estimate-revision series; sector ranking vs a single pure-memory comp (MU) only — NVDA/TSM/AVGO/AMD/ASML/INTC were not scored.
