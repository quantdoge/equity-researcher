# Quant Analyst

- Symbol: TSN
- Elapsed: 38.3s

---
# TYSON FOODS (TSN) — Quantitative Factor Report

**Data as of:** last OHLCV observation 2026-10-30 | 5-yr daily series | Benchmark SPY
**Price:** $57.04 (last close) | Market cap ~$22.5B | Sector: Consumer Defensive / Agricultural Farm Products

> **⚠️ Data integrity flag up front:** the dataset contains two different price levels — the OHLCV feed closes at **$57.04** on 2026-10-30, while the valuation/profile module reports **$63.95** (and BVPS $100.11 → P/B 0.64 implies $63.95). That's a ~12% gap. Multiples below are quoted as delivered; price-derived return stats are computed by me from the OHLCV series. Treat the level-dependent figures as provisional.

---

## 1. Factor Scores Table

Peer set = TSN, HRL, CAG, KHC, PPC (true protein/packaged-food comparables). **Note:** `get_sector_peers` returns only Consumer Defensive mega-caps (WMT, COST, KO, PG, PM, PEP, BUD, UL) — not valid comparables for a commodity meat processor. I built the peer set manually. **n=5 is far below the ~30 names needed for a stable quintile break; all ranks are ordinal, not statistically robust.**

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | 55 / 100 | **2 of 5** | Neutral–Positive |
| **Momentum** | 40 / 100 | **2 of 5** | Negative (absolute) |
| **Quality** | 25 / 100 | **4 of 5** | Negative |
| **Low Vol** | 70 / 100 | **1 of 5** | Positive |
| **Earnings Revision** | 45 / 100 | n/a (n=2) | Neutral — unreliable |

**Value — 55/100, rank 2/5.** P/B **0.64** and EV/EBITDA **11.95x** are the only genuine cheapness. But P/E **49.96x** is the *highest* in the peer set — a textbook trough-earnings artifact (ROE 1.28%). For a commodity processor, 11.95x EV/EBITDA is not cheap in absolute terms: **PPC trades at 4.55x**. FCF yield 7.3% (P/FCF 13.61) is respectable; dividend yield 3.19%. Score is floor-supported by book value, not earnings.

**Momentum — 40/100, rank 2/5.** 12-1 month return **−6.09%** (negative, below zero). Positive only by being less bad than HRL (−17.4%), CAG (−7.2%), KHC (−7.0%). **PPC (+3.9%) is the only positive name.** Recent tape diverges: **+12.9% in the last month** off the 2026-10-01 low — short-term reversal fighting a negative intermediate trend.

**Quality — 25/100, rank 4/5. This is the hole in the thesis.**
- ROE **1.28%**; ROIC **2.55%** — declining for three straight years (FY24 4.98% → FY25 4.06% → FY26 2.55%). **ROIC is roughly a third of any reasonable WACC estimate; TSN is destroying economic value.**
- Gross profit/assets **0.092** — *worst in the peer set* (PPC 0.228, HRL 0.141, CAG 0.156, KHC 0.102).
- One bright spot: accruals ratio **−5.64%** — cash earnings exceed GAAP net income, so earnings are conservatively stated, not inflated. Piotroski **F-Score 6/9** (Moderate): positive ROA/OCF, falling leverage, positive equity change; fails on ROA improvement, dilution, gross margin, and (partially) asset turnover.

**Low Vol — 70/100, rank 1/5.** Annualised vol **28.74%** (252d) / **25.7%** (504d) — the lowest of the five (KHC 29.2, HRL 31.0, CAG 34.2, PPC 40.4). Max drawdown **25.27%**, better than HRL/PPC/CAG.

**Earnings Revision — 45/100, Neutral, low confidence.** The tool reports **+8.64%** (FY2029 EPS $5.32 vs $4.897 prior) — but **only 2 analysts** cover FY2029 and the "prior" figure is identical to the current FY2028 estimate. That is almost certainly a **roll-forward artifact, not a real upgrade.** Meanwhile genuine sell-side sentiment is deteriorating:

| Date | Firm | Target |
|---|---|---|
| 2026-10-07 | Piper Sandler | $66 → **$56** |
| 2026-09-10 | Piper Sandler | $78 → $66 |
| 2026-09-04 | Barclays | $78 → $75 |
| 2026-09-04 | BMO | **$65** |
| 2026-08-04 | Bernstein | $63 → $66 |
| 2026-07-14 | JPMorgan | $71 → $65 |
| 2026-07-02 | Bernstein | $65 → $63 |

**5 of the last 7 actions were cuts.** Median target ~$66 vs $57.04 spot (~+16%, but computed against a drifting-down anchor).

---

## 2. Price Statistics

| Metric | 504-day | 252-day |
|---|---|---|
| Annualised return | 16.48% *(see caveat)* | — |
| Annualised volatility | 25.69–25.91% | 28.74% |
| **Sharpe** | **0.636** | **0.157** |
| **Sortino** | **1.048** | — |
| **Alpha (annualised)** | **+16.18%** | — |
| **Beta vs SPY** | **−0.057** | −0.247 |
| **R²** | **0.0008** | — |
| Max drawdown | 25.27% | 25.27% |

**Returns I computed directly from the OHLCV feed** (these disagree with the module, consistent with the price-level discrepancy):
- 1 month: **+12.90%** ($50.53 → $57.04)
- 3 months: **−5.07%** ($60.09 → $57.04)
- 12 months: **+14.86%** ($49.66 → $57.04)
- 24 months: **+3.84% cumulative ≈ 1.9% CAGR** — *not* 16.48%/yr
- YTD 2026: **−0.16%**
- 52-week range **$49.66 – $67.54**; spot at the **41st percentile**, **−15.5% from the 52-week high**

### Statistical validity warnings — read before using alpha/beta
- **The alpha is not real.** R² = **0.0008** means the CAPM regression explains **0.08% of TSN's variance**. Beta of −0.057 carries a t-stat ≈ **0.6** and the 16.18% alpha a t-stat ≈ **0.9**. Both are indistinguishable from noise. A zero-beta, 16%-alpha food company does not exist; this is an uninformative regression, not an inefficiency.
- The **negative betas across all five peers** (−0.03 to −0.39) confirm a **systematic benchmark/date-alignment bug**, not a genuine property of the meat complex. The company profile's own beta of **0.375** is more credible. **Use β ≈ 0.35–0.40** for cost-of-capital work.
- **Sharpe/Sortino are internally inconsistent with the price series.** A 0.636 Sharpe on 25.9% vol implies ~16.5% annualised return; the OHLCV series shows ~1.9% CAGR over the same 24 months. The Sortino/Sharpe ratio of 1.65x implies reasonably symmetric tails, but **the level should not be trusted** — and Sharpe fell from 0.636 (504d) to **0.157 (252d)**, i.e. risk-adjusted performance has decayed sharply in the most recent year.

---

## 3. Composite Quant Signal

**NEUTRAL** (composite 45 / 100)

Weighting: Value 25%, Quality 25%, Momentum 20%, Low Vol 15%, Revision 15%.

```
0.25(55) + 0.25(25) + 0.20(40) + 0.15(70) + 0.15(45) = 45.3
```

The factors pull in opposite directions and net out. Valuation support rests entirely on **book value (P/B 0.64)** and asset-backed downside protection — not on earnings power. Quality is **bottom-quartile and deteriorating** (ROIC 2.55% and falling, gross profitability worst in class), which is precisely the profile that makes P/B screens into value traps. Low-vol is the strongest genuine signal. Momentum is negative on the 12-1 horizon but improving sharply in the last month. There is **no factor combination here that justifies conviction in either direction.**

---

## 4. Key Quant Risk Flags

1. **Quality/value-trap confluence (highest severity).** Cheap on book, expensive on earnings, with ROIC of 2.55% trending down for three years and gross profit/assets dead last among peers. P/B 0.64 with ROE 1.28% is the classic signature of a **melting book value**, not a discount. P/E 49.96x and forward P/E ~17x (FY26E $3.29) / ~14.5x (FY27E $3.94) mean the stock already prices a margin recovery.

2. **Momentum reversal risk — in both directions.** 12-1 of −6.09% but **+12.9% in the past month** produces a violent short-term/long-term conflict. Historically this pattern resolves toward the longer horizon, so the recent rally is **fragile** and vulnerable to gap risk.

3. **Earnings-event gap risk.** Single-day moves of **+8.0% (2026-05-04)**, **−7.3% (2026-09-03)**, **−4.4% (2026-06-03)**, **−4.6% (2025-11-24)**. Earnings-catalyst concentration is high for a "low-vol" name — vol is low *on average*, but the daily distribution is fat-tailed.

4. **Leverage / dividend coverage.** Net debt ≈ **$6.9B** (EV $29.56B − mkt cap $22.64B) on EBITDA of ~$2.47B = **~2.8x net debt/EBITDA**. Dividend of ~$2.04/share (~$722M) is **1.6x GAAP EPS** of $1.28 — covered only by FCF (~$1.66B, ~43% of FCF). Any FCF compression puts the 3.19% yield at risk, and the yield is a meaningful part of the total-return case.

5. **Sell-side revision momentum is negative while the quant revision tool says positive.** Trust the price targets (real, dated, firm-attributed) over the tool's +8.64% (n=2, artifact-contaminated). **Do not treat this name as an upward-revision story.**

6. **Sample-size limits.** Cross-sectional ranks are computed on **5 names**; a stable quintile needs ~30. The alpha/beta/Sharpe block is **statistically void** (R² ≈ 0.001, |t| < 1) and should be excluded from any cost-of-capital or risk-budgeting calculation. All conclusions here rest on the fundamental ratios and my direct computation from the price series, not on the regression output.

7. **Liquidity is adequate** — average volume ~2.7M shares/day, no liquidity constraint on position sizing up to institutional scale.

---

**Bottom line: Neutral, not actionable as a factor long.** The only defensible quantitative case is "cheap on assets, low vol, 3.2% yield, cash-backed earnings (accruals −5.6%)" — an income/defensive holding at best. Against that: the worst quality in its peer set, ROIC below cost of capital and falling, negative 12-1 momentum, deteriorating price targets, and 2.8x leverage with a dividend exceeding GAAP earnings. A quality screen would rank it near the bottom; that should dominate the P/B screen until ROIC inflects. **Re-rate to Buy only on two consecutive quarters of ROIC expansion above ~5%, or on a 12-1 momentum turn positive.**
