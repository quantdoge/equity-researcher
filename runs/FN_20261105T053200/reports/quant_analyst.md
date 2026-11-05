# Quant Analyst

- Symbol: FN
- Elapsed: 50.1s

---
# Fabrinet (FN) — Quantitative Factor Report
**Price $341.64 | Mkt cap ~$12.4B | Technology – Hardware/Optical EMS | Data as of 2026-11-04**

## 1. Factor Scores Table

| Factor | Score (/10) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | 5.0 | **2 / 6** | Neutral-positive. P/E 26.2x, EV/EBITDA 18.5x, P/B 5.05x — cheapest in the comp group (COHR 47.4x, ANET 64.9x, CIEN 320x, CSCO 31.1x). **But P/FCF = 4,073x** (FCF $3.0M on $473M NI) breaks the FCF-yield leg entirely |
| **Momentum** | 2.0 | 5 / 6 | Negative trend. 12-1 momentum **+10.7%**, but price is **−54.2% from the $746.47 peak (2026-05-14)** and below both the 50-day (~$410) and 200-day (~$480) averages |
| **Quality** | 6.5 | 3 / 6 | Good, deteriorating at the cash line. ROE 19.3%, ROIC 18.8% (16.3→15.8→17.0→18.8 rising), GP/Assets 14.2%, **accruals ratio 0.055 = warning**, Piotroski F-score **5/9** (accruals + leverage + margin/turnover components all fail) |
| **Low Vol** | 1.5 | 3 / 5 | Very poor in absolute terms: 83.2% ann. vol, **beta 2.95 vs SPY**, max DD 57.8%. Best of the worst (ANET 57% vol is the only true low-vol name here) |
| **Earnings Revision** | 6.5 | 1 / 6 | Upgrade: **+19.25%** revision, but on **FY2030 EPS (n = 1 analyst)** — statistically insignificant. Corroborated independently: Q1-FY27 EPS $4.10 vs $3.81 consensus, Q2 guide $4.77–4.92 and $1.6–1.65B rev *well above* consensus |

\*Peer set is a hand-built optical/networking comp group (COHR, LITE, CIEN, ANET, CSCO) — the raw sector feed returns $500B+ mega-caps that are not valid comparables for a $12B optical EMS.

**Forward valuation cross-check (4-analyst consensus):** FY26 EPS $13.84 → 24.7x; **FY27 $19.71 → 17.3x**; FY28 $23.99 → 14.2x. Implied PEG ≈ **0.41** vs FY27 revenue growth of +42% ($4.64B → $6.59B). Estimates assume hyper-growth through FY2030 ($11.3B revenue, $35.47 EPS).

## 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (ann., vs SPY, 252d) | **−57.2%** | Standard error is wide (β 2.97, R² **0.22**) — only ~22% of variance is market-explained, so alpha is imprecise |
| Beta (1-yr daily vs SPY) | **2.95 / 2.97** | vs 1.345 5-yr beta in profile — sensitivity has more than doubled |
| Ann. volatility | **83.2%** | |
| Ann. return (252d) | −18.6% (model) / **−25.7%** spot-check (459.60 → 341.64) | Flag: model and raw adj-close disagree by ~7pts; treat return *level* as approximate, sign as certain |
| Sharpe | **−0.227** | |
| Sortino | **−0.346** | Downside dev. ~53.8% → no asymmetry cushion |
| Max drawdown | **−57.84%** | $746.47 → $314.94 (2026-10-23); currently +8.5% off that low |
| Peers Sharpe | LITE 1.18, ANET 0.73, CIEN 0.56, COHR 0.34, **FN −0.23** | FN is last on risk-adjusted performance |

**Correlation / crowding:** COHR **0.78**, CIEN 0.70, LITE 0.68, ANET 0.49, NVDA 0.46. Effectively a single-factor bet on the AI-optical-capex trade; FN gives no diversification within it.

## 3. Composite Quant Signal: **NEUTRAL (4.3 / 10)**

Weights: Value 20%, Momentum 25%, Quality 25%, Low Vol 15%, Revisions 15% → 0.20(5.0)+0.25(2.0)+0.25(6.5)+0.15(1.5)+0.15(6.5) = **4.33**.

The factor tape is in open conflict: **Quality + Revisions up, Momentum + Volatility down.** This is a de-rating, not a deterioration — revenue +35.7% in FY26 to $4.64B, +45% in the latest quarter, and guidance above consensus, while the multiple compressed ~54% in six months (Aug 18, 2026: **−19.4% in one session on an estimate beat**). In backtest, a quality/revision-up, momentum-down configuration resolves in favor of the fundamentals only *after* momentum inflects; until then, price continuation risk dominates. Cheapest on value and fastest-growing in the peer set, but last on Sharpe and worst-in-class on drawdown.

**Momentum inflection triggers (would move the composite to Buy):** reclaim of ~$410 (50-day) → ~$480 (200-day), plus 12-1 momentum holding above +10%.

## 4. Key Quant Risk Flags

1. **Momentum reversal / expectation reset risk (high):** 57.8% peak-to-trough drawdown with beta 2.95. Two consecutive "beat-and-fall" reactions confirm the market is repricing the multiple, not the earnings — a factor-level momentum trap.
2. **Cash conversion breakdown (high):** FY26 OCF collapsed to $256.7M (from $328.4M) on NI of $473.0M; FCF $3.0M vs $206.5M. Drivers are capex +109% ($253.7M, capacity build — defensible) and a **$259.9M working-capital drag** (receivables/inventory ahead of revenue). Accruals ratio 0.055 and both F-score accrual/leverage tests fail. This is the single largest threat to the "cheap at 17x forward" thesis if WC does not reverse in FY27.
3. **Estimate fragility (medium):** the revision signal rests on n=1 analyst at FY2030. Sell-side targets span **$364 (B.Riley, 2026-11-03, "sidelined on valuation") to $800 (Northland)** — a ~120% spread, i.e. no consensus on terminal economics.
4. **Factor crowding / correlation (medium-high):** 0.78 with COHR, 0.70 CIEN — a crowded AI-optical trade where a single capex headline hits all names simultaneously.
5. **Statistical caveats:** 252 daily observations give a beta SE of roughly ±0.10 and an alpha SE wide enough that −57% is directionally but not precisely signed; R² of 0.22 means market-beta hedging will not protect this position. **Quarterly estimate history unavailable** (FMP endpoint not on plan) — the revision factor could not be verified at quarterly granularity.
6. **Liquidity (low risk):** ~0.8–1.5M shares/day typical (~$280M notional), spiking to 7.0M on earnings. No liquidity constraint for institutional sizing; customer concentration (not quantified in the data) is the residual fundamental tail risk.
