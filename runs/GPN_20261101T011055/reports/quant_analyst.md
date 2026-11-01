# Quant Analyst

- Symbol: GPN
- Elapsed: 47.3s

---
# GPN — Global Payments Inc. | Quantitative Factor & Risk Report
**Price $96.84 · Mkt Cap ~$23.3B · Financial Services / Credit Services · FY25 10-K filed 2026-02-20**

## ⚠️ Data Integrity Notes (read first)
Three tool outputs were internally inconsistent and I resolved them against raw filings/prices. Numbers below use the **verified** figures; tool artifacts are flagged.

1. **Sharpe/Sortino window conflict.** The risk tools returned `annualized_return 51.32%, Sharpe 1.119, Sortino 2.133`. That return is **not reproducible** from the price series: GPN closed at **$110.60 (Jan-2025) → $81.66 (Feb-2026) → $96.84 (current)**, i.e. **-12.4%** over ~20 months, not +51%. A trailing-252d window starting ~Oct-2025 (~$86–88) implies ~**+10–12%**, Sharpe **~0.25**. Reported max DD of 24.0% *is* consistent (peak $88.43 Oct-2025 → trough $66.13 Feb-2026 = -25.2%), confirming the window start. **I treat 51.32%/1.119 as a feed error and use the reconstructed ~0.25 Sharpe as the conservative case.**
2. **Earnings-revision tool returned an invalid comparison** — it diffed FY2030 EPS ($26.01) against FY2029 ($22.21). Different forecast periods; +17.11% is just the 2029→30 growth rate, **not a revision**. I rebuilt the signal from price-target/rating history instead (see below).
3. **`get_sector_peers` failed** — returned Vanguard index funds, ETFs and JPMorgan rather than payments comparables. **No sector percentile ranks are published below; fabricating them would be worse than omitting them.**

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | **78 / 100** | n/a (peer set unavailable) | **Positive — attractive** |
| **Momentum** | **35 / 100** | n/a | **Neutral — deteriorating** |
| **Quality** | **32 / 100** | n/a | **Negative** |
| **Low Vol** | **40 / 100** | n/a | **Negative (vol), Positive (beta)** |
| **Earnings Revision** | **80 / 100** | n/a | **Positive — upgrade cycle** |
| **Composite** | **54 / 100** | — | **NEUTRAL** |

**Value (78/100).** P/B **0.98** (below book), P/FCF **11.4x**, EV/EBITDA **10.7x**, GAAP P/E 16.6x, div yield 1.03%. Critically, FY26 consensus EPS of **$13.64** (23 analysts, tight $13.52–13.71 range) vs FY25 **GAAP** diluted EPS of $5.83 implies the headline 16.6x P/E is a GAAP artifact — **adjusted forward P/E is ~7.1x**. Deep value on cash flow, but see the quality trap below.

**Momentum (35/100).** Standard 12-1 momentum **+0.95%** — flat. Intermediate 6-1 momentum **-15.25%** — clearly negative. Yet price is **+46% off the Feb-2026 low of $66.13**. Classic late-stage reversal pattern: a collapsed intermediate trend with an explosive but unconfirmed short-term bounce.

**Quality (32/100) — the core problem.** ROE **5.89%**, ROA 2.62%, **ROIC 3.22%**, down from 5.74% (2024) and 5.38% (2023). Gross profit/assets **10.5%** (low). Piotroski **F-score 6/9** (moderate) — losing points on ROA improvement, leverage, and asset turnover. Only genuine bright spot: accruals ratio **-2.36%** (negative accruals = clean earnings) and FCF/NI of **1.40x** (strong cash conversion). **ROIC of 3.22% sits below any reasonable WACC (~8%) — this is a value-destroying capital allocator, and it is getting worse, not better.**

**Low Vol (40/100).** Annualized vol **45.34%** — very high for a payments processor and disqualifying for low-vol screens. Beta **0.839/0.844** (two independent methods agree — reliable) is genuinely low, which partially offsets. High idiosyncratic risk, low market risk.

**Earnings Revision (80/100).** Rebuilt from primary evidence, and it is strong: **eight consecutive upward price-target revisions** — BMO $76→$83, Truist $79→$95, Argus $95→$110, RBC $96→$102, MS $100→$103, RBC $102→$106, Wolfe $110→$125, Baird $114→$120 — plus **two rating upgrades** (KeyBanc to Overweight; Oppenheimer to Outperform, $115) and a Buy initiation (Loop, $137). Median target **~$107.50** vs $96.84 = **+11% implied upside**. Consensus EPS path: FY26 $13.64 → FY27 $16.11 (+18.1%) → FY28 $18.83 (+16.9%). *Caveat: FY28 dispersion is $7.56–$30.68 across only 13 analysts — long-dated estimates are unusable.*

---

## 2. Price Statistics

| Metric | Value | Reliability |
|---|---|---|
| Beta vs SPY | **0.839** | High (two methods agree) |
| Alpha (annualized) | **+32.45%** | **Not significant** |
| R² vs SPY | **0.0595** | — |
| Alpha t-stat (derived) | **≈0.73** | — |
| Annualized volatility | **45.34%** | High |
| Sharpe | **1.119 reported / ~0.25 reconstructed** | **Conflicted — see note 1** |
| Sortino | **2.133 reported / not verified** | **Conflicted** |
| Max drawdown (252d) | **-24.0%** | Verified (Oct-25→Feb-26) |
| Max drawdown (Jan-25→Feb-26) | **-40.1%** ($110.60→$66.20) | Verified |

**The alpha is noise.** With R² of just **5.95%**, only 6% of GPN's variance is explained by the market — 94% is idiosyncratic. Residual vol is ~44.5% annualized, giving a standard error on the annualized alpha of roughly 44.5% over a one-year sample. **t ≈ 0.73.** The +32.45% "alpha" is statistically indistinguishable from zero. I will not cite it as evidence of outperformance. Note also the single-year (252-day) sample — this is a low-power estimate regardless.

---

## 3. Composite Quant Signal: **NEUTRAL (54/100)**

Weighted: Value 30% (78) + Quality 25% (32) + Momentum 20% (35) + Revision 15% (80) + Low-Vol 10% (40).

**The setup:** a deeply discounted multiple (P/B <1, 8.8% FCF yield) with a genuine, broad-based analyst upgrade cycle — but the cheapness is *earned*, not a mispricing. ROIC of 3.22% means the business currently earns less than its cost of capital, so book value at $0.98 is not a bargain signal but a rational discount. The 45% volatility and 3.9x net-debt/EBITDA compound the risk. **This is a value trap until ROIC inflects.** Upgrade to Buy requires ROIC stabilizing above ~6% and 6-1 momentum turning positive. Downgrade to Sell on a break below the $66 February low.

---

## 4. Key Quant Risk Flags

1. **Alpha is statistically meaningless** — R² 5.95%, t ≈ 0.73. Do not build a thesis on it.
2. **Sharpe/Sortino are unreliable** — reported 1.119/2.133 conflicts with the verified price path (~0.25 Sharpe). Any ranking or memo that uses the reported figures is misinformed.
3. **ROIC 3.22% < WACC** and deteriorating three years running (5.37→5.38→5.74→3.22). Hard quality veto.
4. **Momentum reversal risk is elevated** — +46% in weeks against 6-1 momentum of -15.25%. Post-bounce mean reversion is the base case absent a fundamental catalyst.
5. **Leverage** — net debt **$13.53B**, net debt/EBITDA **3.9x**, interest expense $650M (~3.4% avg cost). Refinancing-sensitive.
6. **Goodwill & intangibles $21.31B = 90% of the $23.78B equity base.** Tangible book is only **~$2.47B (~$10.3/sh)** → **P/TBV ≈ 9.4x**, not 0.98x. The P/B "cheapness" is almost entirely accounting goodwill.
7. **Revenue fell -24% YoY** ($10.11B→$7.71B) and EBITDA -21% ($4.37B→$3.45B) — divestiture-driven. **Organic growth is not verifiable from these statements**; the FY26 consensus revenue of $12.36B implies a re-expansion that needs explaining.
8. **GAAP vs adjusted EPS gap** — P/E is 16.6x on GAAP ($5.83) but ~7.1x on FY26 adjusted ($13.64). A 2.3x gap. Use the adjusted figure only if you accept the add-back schedule.
9. **Peer cross-sectional ranking unavailable** — sector feed returned funds/ETFs. No factor percentile claims made.
10. **Small-sample caveat** — 252 daily observations, one fiscal year, 5–13 analysts on long-dated EPS. Treat all estimates as low-power.
11. **Liquidity is not a concern** — ~3–8M shares/day, $23B cap, no crowding or liquidity flag.

**Bottom line:** Value and estimate revisions say yes; quality, ROIC, and intermediate momentum say no. The quantitative evidence does not support a Buy.
