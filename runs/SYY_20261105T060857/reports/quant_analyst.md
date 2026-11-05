# Quant Analyst

- Symbol: SYY
- Elapsed: 39.5s

---
All data collected. Two serious data-integrity issues surfaced that change how the risk statistics must be read — flagging both explicitly below.

# SYY (Sysco Corp) — Quantitative Factor & Risk Report

**Price basis:** $81.53 (close 2026-09-01). Note: the valuation feed prices SYY at $76.94 (FY-end 2026-06-27); I report feed multiples *and* restate to the current $81.53 close where it matters. Sector = Consumer Defensive / Food Distribution. Market cap ≈ $39.2B, ADV ≈ 3.1M shares.

## 1. Factor Scores Table

Peer set = 6 largest Consumer Defensive names (WMT, COST, KO, PG, PEP, MDLZ), n=7 including SYY. Ranks are 1=best.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 22.3 (feed 21.0) · EV/EBITDA 12.7 (12.2) · P/FCF 20.2 (19.1) · P/B 14.7 · Div yield 2.67% | **1 / 7** (cheapest on all 3 multiples) | **Strong positive** |
| **Momentum** | 12-1 return **−9.23%** | **6 / 7** | **Negative** |
| **Quality** | ROE 65.9% · GP/Assets 0.551 · Accruals −0.031 · Piotroski F **7/9** | **2 / 7** | **Positive** |
| **Low Vol** | Realised vol **28.96%** · MDD 23.98% · beta 0.17 (unreliable, see §2) | **7 / 7** (highest vol) | **Negative** |
| **Earnings Revision** | EPS revision tool **+6.89%** → "upgrade" — **artifact, do not use** | n/a (no peer data) | **Inconclusive / restated positive** |

**Value detail vs peers:** SYY is the cheapest name in the group on every metric — P/E 22.3 vs peer median 31.5 (−29%), EV/EBITDA 12.7 vs PEP 15.2 (next best) and COST 31.5, P/FCF 20.2 vs peer median 27.0. This is the one factor where SYY is unambiguously top-quintile, and the discount is not explained by leverage (net debt $13.2B, ~0.26x EV).

**Quality detail:** ROE 65.9% is the highest in the peer set but is flattered by a thin equity base (BVPS $5.55, P/B 14.7) — ROIC of 17.6% is the honest measure and is *decelerating*: 23.0% (FY23) → 21.6% (FY24) → 18.9% (FY25) → 17.6% (FY26). Accruals have been negative four years running (−0.031 to −0.048) — genuinely clean cash conversion (OCF $2.64B vs NI $1.76B, 1.50x). F-score 7 loses points on ROA improvement and asset-turnover improvement, i.e. the *trend* is deteriorating even though the *level* is good.

**Earnings revision — the tool output is not usable.** The revision score compared an FY**2031** estimate ($6.83) against $6.39, which is the FY**2030** consensus — two different forecast periods, not the same period three months apart. The +6.89% is therefore just implied FY30→FY31 growth, not a revision. Underlying coverage is also too thin to support a signal: FY2028–FY2031 only (1–7 analysts), and **no FY2026/FY2027 consensus at all**.
*Genuine revision evidence comes from the price-target tape instead:* targets were cut hard post-March (Bernstein $90→$85, Deutsche Bank downgraded to Hold at $84 in April), then revised **up** sequentially — Piper $77→$84 (Aug), Guggenheim $90 Buy (Sept), Morgan Stanley $88→$91 (Oct). Median target **$91** = **+11.6% upside**, mean $91.0, range $84–$100. Direction of travel is up, but from a post-shock trough.

## 2. Price Statistics

| Metric | Value | Read |
|---|---|---|
| Annualised return (252d) | **−8.47%** | Underperforming |
| Annualised volatility | **28.96%** | Highest in peer set (peers 19.9–28.0%) |
| **Sharpe** | **−0.289** | Worst in peer set (KO +1.95, PG +0.96, MDLZ +0.94, WMT +0.63, COST +0.61, PEP +0.04) |
| **Sortino** | **−0.277** | ≈ Sharpe — no positive skew; downside deviation ≈ total vol |
| Max drawdown | **−23.98%** (close-to-close, 2026-02-27 $89.25 → 2026-03-30 $67.85) | 2nd worst after PEP (−25.2%) |
| Alpha (annualised) | **−6.51%** | **Statistically meaningless — see below** |
| Beta vs SPY | **0.166** (R² = **0.0057**) | **Not usable** |
| Beta, 5-yr monthly (profile) | **0.64** | The defensible figure |

**Why the regression statistics are unusable:** R² of 0.0057 means SPY explains 0.57% of SYY's variance. Implied beta standard error ≈ 0.138, so t ≈ 1.2 and the 95% CI on beta is roughly **−0.11 to +0.44** — indistinguishable from zero. The alpha t-stat is ≈ −0.22 (annualised residual vol ≈ 29%). **Neither the −6.51% alpha nor the 0.166 beta is significant; do not build a position on them.**

This is a benchmark-series defect, not a property of Sysco. Every peer shows the same pathology: SPY correlation is negative for COST (−0.157), KO (−0.194), PEP (−0.125), MDLZ (−0.194), WMT (−0.028), and near-zero for PG (+0.007). Real large-cap staples correlate ~0.4–0.6 with SPY. Use the 5-year monthly **beta of 0.64** and treat alpha as unmeasured rather than −6.5%.

**Other price observations:** the −23.98% drawdown was concentrated in a **single session** — 2026-03-30 fell −15.3% (80.08→67.85) on 24.6M shares, ~9x normal volume. That is an event/idiosyncratic repricing, not a drift. SYY has since recovered to $81.53, sitting 63.9% up the 52-week range ($67.85–$89.25) but still 8.6% below the February high.

**Correlation / crowding:** SYY's correlation to every peer is only **0.22–0.29** — the lowest in the group (peers correlate 0.39–0.71 with each other). Low co-movement argues *against* factor-crowding risk and offers genuine diversification within Consumer Defensive.

## 3. Composite Quant Signal: **NEUTRAL** (equal-weight percentile ≈ 51st)

Equal-weighting the four measurable factors (Value 100th pct, Quality 78th, Momentum 17th, Low-Vol 8th) gives ≈ **51st percentile** — a dead-centre score driven by two strongly opposing legs.

The character is clear: **a cheap, cash-generative, low-beta-by-construction name in a confirmed downtrend with elevated realised volatility.** Value + Quality at the top of the peer group is the rare combination worth owning — but the framework requires momentum confirmation, and −9.23% 12-1 return with the peer set *uniformly negative* (PG −0.71% to PEP −12.5%) says this is sector-wide de-rating plus stock-specific underperformance, not a bottoming pattern. The positive price-target revision trend is the single best argument for an early **Buy**, but it is a leading indicator without yet a price trend behind it. Upgrade to Buy on 12-1 momentum turning positive or a sustained break above the $89 high; downgrade to Sell on a close below $67.85.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — active and unfavourable.** −9.23% 12-1 momentum, 6th of 7 peers, in a sector where all 7 are negative. Buying value into negative momentum is the classic "value trap" setup; there is no statistical evidence of mean reversion here.
2. **Volatility/liquidity mismatch.** 28.96% realised vol is ~45% above the peer median (~22%) for a $39B staple — and the March −15.3% gap on 9x volume shows event risk is real and concentrated. Position sizing should use ~29% vol, not the 0.64 beta's implied stability.
3. **Broken risk statistics (highest-priority data flag).** Alpha (−6.51%), beta (0.166), R² (0.006), and the Sharpe/Sortino figures are all computed off a benchmark series that is uncorrelated with the entire staples complex. The *ranking* conclusion (SYY's Sharpe is worst in the peer group) holds because it uses SYY's own return series, but the *absolute* alpha/beta numbers should not be quoted in the memo.
4. **Estimate data too thin for significance.** No FY2026/FY2027 consensus; FY2028–FY2031 covered by 1–7 analysts. FY2028 EPS of $5.39 implies +47% growth over trailing $3.66 in two years for a ~4% revenue grower — implausible without major margin expansion. Any forward P/E (15.1x on FY28) built on this is low-confidence.
5. **Quality trend deteriorating beneath a good level.** ROIC has fallen 540bp over three years (23.0%→17.6%) and F-score gives 0 on both ROA improvement and asset-turnover improvement. The quality factor score is level-based and masks this.
6. **Sector-rank sample is too small and mis-specified.** n=7 mega-cap staples; SYY's true comparables (PFGC, USFD — food distribution) were **not returned by the sector feed and are absent from this analysis**. Ranks are therefore "vs. large-cap Consumer Defensive," not vs. distribution peers — a material gap given SYY's 12.7x EV/EBITDA should be benchmarked against PFGC/USFD, which typically trade at a premium.

**Data gaps, stated plainly:** no food-distribution peer multiples, no near-term consensus, no peer price targets, no usable benchmark regression. Everything reported above is either a direct feed value or a restatement I have shown the arithmetic for.
