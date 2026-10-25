# Quant Analyst

- Symbol: TRU
- Elapsed: 68.2s

---
# TRU (TransUnion) — Quantitative Factor & Risk Scorecard

**Sector:** Financial Services / Financial Data & Stock Exchanges · **Price:** $78.23 · **Mkt cap:** $14.99bn · **EV:** ~$19.68bn (net debt ~$4.7bn)

**Peer group (n=6, hand-built — the sector feed returned only index funds):** EFX, VRSK, FICO, MCO, SPGI. Ranks are 1 = best of 6.

---

## 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 33.7 · EV/EBITDA **13.5** · P/FCF 23.3 · P/B **3.38** | **2 of 6** (~70th pct) | **Positive** — cheapest EV/EBITDA and lowest P/B in group; P/E (5th) inflated by low net income |
| **Momentum (12-1)** | **−5.56%** | 2 of 6 (~80th pct) | **Negative in absolute terms** — best-in-a-bad-tape; whole peer group is negative (FICO −28.5%, VRSK −11.0%) |
| **Quality** | ROIC **8.84%** · ROE 10.02% · ROA 4.10% · GP/Assets 0.243 · Accruals **−4.79%** · F-Score **8/9** | **6 of 6** (0th pct on ROIC/ROA) | **Negative** — lowest ROIC and ROA in the group; only accruals/F-Score strong |
| **Low Vol** | Vol **44.48%** · β **0.923** · Max DD 28.76% | **5 of 6** (~20th pct) | **Negative** — 2nd-highest vol and highest beta of the six |
| **Earnings Revision** | FY30 EPS **+5.95%** (+5 analysts) | **5 of 6** (~20th pct) | **Weak positive** — upgraded, but weakest-but-one; peer revisions +7.7% to +19.0% |

**Peer detail:**

| | TRU | EFX | VRSK | FICO | MCO | SPGI |
|---|---|---|---|---|---|---|
| EV/EBITDA | **13.5** | 14.4 | 19.8 | 23.7 | 23.0 | 19.0 |
| P/FCF | 23.3 | 19.3 | 22.3 | 25.5 | 33.2 | 24.5 |
| ROIC (%) | **8.8** | 11.1 | 25.1 | 69.6 | 29.9 | 12.9 |
| 12-1 Mom (%) | −5.6 | −7.2 | −11.0 | −28.5 | −5.1 | −7.9 |
| Vol (%) / β | 44.5 / 0.92 | 44.0 / 0.59 | 37.9 / −0.43 | 68.4 / 0.38 | 29.7 / 0.54 | 34.5 / 0.41 |
| EPS revision (%) | 6.0 | 1.9 | 12.9 | 19.0 | 14.6 | 7.7 |

---

## 2. Price Statistics (252d, daily, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **−1.79%** |
| Annualised vol | **44.7%** |
| **Alpha (annualised)** | **−14.25%** |
| Beta | 0.927 (profile β = 1.575 on a longer window) |
| R² vs SPY | **0.075** |
| **Sharpe** | **−0.04** |
| **Sortino** | **−0.061** |
| Max drawdown | −28.76% |

Correlation: **EFX 0.86** (near-duplicate exposure), MCO 0.64, SPGI 0.61, FICO 0.57, VRSK 0.51, **SPY 0.27**.

---

## 3. Composite Quant Signal

**NEUTRAL (negative bias — 38th percentile composite)**

Equal-weighted percentile across the five factors: Value 70, Momentum 80, Quality 0, Low Vol 20, Revision 20 → **38th**. The entire score rests on one leg — cheap EV/EBITDA and P/B. That cheapness is unattractive-cheap, not mispriced-cheap: it is paired with the group's **lowest returns on capital (8.8% ROIC)**, the highest beta, and a **−14.2% annualised alpha**. Long-dated EPS estimates are drifting up (+6.0% on FY30) while every major broker is **cutting price targets** — Mizuho 77→74, RBC 100→92, MS 106→97, GS 77→68, Barclays 85→70. Median target ~$74 sits **below** the $78.23 spot. Estimates up, targets down is the classic "multiple compression" signature, not an upgrade cycle.

Verdict: **not a Buy.** Value rank alone cannot carry a name with 0th-percentile quality and 20th-percentile low-vol. Signal would upgrade to Buy on a ROIC inflection above ~11% (EFX parity) or two consecutive quarters of upward *target* revisions.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / downtrend intact.** 12-1 momentum −5.6% and price above consensus targets. Relative rank (2/6) is deceptive — it reflects peers falling faster, not TRU strength. Sector-wide de-rating of credit/data bureau multiples.
2. **Beta estimate is statistically unreliable.** R² = 0.075 means the market explains only 7.5% of TRU's variance; the 0.923 beta carries a very wide standard error and the 1-year (0.92) vs profile (1.575) estimates diverge sharply. Do **not** size this off a market-beta model — use EFX as the hedge leg instead.
3. **Factor crowding / idio-risk via EFX.** 0.86 correlation with Equifax makes TRU + EFX a near-duplicate position; true idiosyncratic diversification requires the MCO/SPGI or VRSK legs.
4. **Left-tail heavy.** Sortino (−0.061) is *worse* than Sharpe (−0.04), implying downside deviation exceeds total volatility — asymmetric drawdown risk. Max DD −28.8% with a 44% vol profile.
5. **Earnings-quality gap.** Accruals are healthy (−4.79%; OCF $988m vs NI $455m = 2.17× cash conversion) and F-Score is 8/9 (only gross-margin trend fails) — this conflicts with the bottom-ranked ROIC. The reconciling item is leverage: EV $19.7bn vs $15.4bn equity, which suppresses ROE/ROIC and inflates P/E while flattering EV/EBITDA. Any deleveraging or rate shock hits this directly.
6. **Sample-size limitations.** (a) Earnings-revision score is computed on **FY2030** estimates — 4 years forward, **5 analysts** — statistically thin; peer revisions use the same 2030 convention so ranks are methodologically consistent but low-power. (b) n=6 peers → quintile statistics are not meaningful; treat "sector rank" as ordinal only. (c) All risk metrics are single 252-day windows — no multi-horizon robustness check; the negative Sharpe/Sortino magnitudes (≈−0.04) are inside sampling noise of zero.

**Gaps:** gross-profit-to-assets peer comparison not pulled (only TRU's 0.243); sector peer feed returned ETFs/funds rather than comparables, so peers were specified manually; no SPY momentum benchmark for a market-relative momentum read.
