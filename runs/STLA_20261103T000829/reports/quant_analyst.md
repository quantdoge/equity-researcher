# Quant Analyst

- Symbol: STLA
- Elapsed: 68.0s

---
# STLA (Stellantis N.V.) — Quantitative Factor & Risk Report
Auto – Manufacturers | Price **$4.72** | Mkt cap **$13.6bn** | EV **$28.2bn** | FY end 2025-12-31 | Reporting ccy **EUR**

## 1. Factor Scores

Sector ranks are against n=5 Auto–Manufacturers with available data (STLA, TM, GM, F, TSLA). **Sample of 5 — treat ranks as ordinal only, not statistically robust.**

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E **−0.61**, EV/EBITDA **−1.85**, P/FCF **−0.84**, P/B **0.25**, FCF yield negative | **2 / 5** | Caution — **value trap**, not value |
| **Momentum** | 12-1 return **−21.1%** (tool); raw 12-mo price **−53.8%** | **5 / 5 (worst)** | Strong negative |
| **Quality** | ROE **−41.4%**, GP/assets **−0.022** (only negative in group), accruals −8.7% | **5 / 5 (worst)** | Very weak |
| **Low Vol** | Ann. vol **53.2%**, beta **1.07** (R²=0.07), max DD **−60.3%** | **5 / 5 (worst)** | Strong negative |
| **Earnings Revision** | +15.4% "upgrade" | **n.m.** | **Not meaningful — see note** |

**Peer cross-section (raw):**

| | P/E | EV/EBITDA | P/FCF | ROE | Vol | 12-1 Mom |
|---|---|---|---|---|---|---|
| **STLA** | −0.61 | −1.85 | −0.84 | **−41.4%** | **53.2%** | **−21.1%** |
| TM | 0.06* | 3.99 | 1.42 | 9.67% | 26.3% | +5.6% |
| GM | 27.5 | 10.31 | 7.90 | 4.27% | 35.3% | −2.7% |
| F | −6.12 | −39.1 | 4.02 | −22.7% | 39.0% | −14.6% |
| TSLA | 373.9 | 118.1 | 229.1 | 4.58% | 45.4% | +21.0% |

*TM P/E is a currency-mismatch artifact (JPY EPS vs USD price); ignore.

**Earnings-revision caveat (important):** the +15.4% figure compares **FY2030E €2.136 to FY2029E €1.851** — different forecast periods, covered by **one analyst**. That is a tool artifact, not revision momentum. The genuine signal is the consensus path: FY2025A **−€7.75** → FY2026E **€0.45** (4 analysts) → FY2027E **€0.90** → FY2028E **€1.35** → FY2030E **€2.14** (1 analyst). Recovery is entirely back-loaded and statistically weightless beyond 2027.

## 2. Price Statistics (252d, vs SPY)

| Metric | Value | Read |
|---|---|---|
| Alpha (ann.) | **−91.9%** | **t ≈ −1.8, NOT significant** |
| Beta | **1.075** | R² = **0.070** → beta explains 7% of variance |
| Sharpe | **−1.648** | t ≈ **−17** (highly significant) |
| Sortino | **−2.108** | downside dev > total-led |
| Ann. volatility | **53.2–54.0%** | ~2× the sector (TM 26%) |
| Max drawdown | **−60.3%** | worst in peer set |
| Ann. return (tool) | −88.9% | **inconsistent with price series — see caveat** |

**Data-integrity flags (must be read before using these numbers):**
- The −88.9% annualized return is **irreconcilable** with the observed series: 2025-11-03 $10.22 → 2026-11-02 $4.72 = **−53.8%**. Treat return/alpha point estimates as directionally valid only.
- Momentum (−21%) also conflicts with the raw 12-month price change (−54%); the tool's window appears to end mid-2026. **Actual momentum is worse than reported**, so the momentum signal is, if anything, understated.
- **Alpha is statistically insignificant.** With R²=0.070, residual vol is ~52% and the OLS intercept SE is enormous. But the Sharpe ratio is significant at t≈−17. Correct interpretation: **the destruction is idiosyncratic, not market-relative** — you cannot beta-hedge this position.

## 3. Fundamental Reality Check (why the factors look like this)

FY2025 (filed 2026-02-26) was an annus horribilis: revenue **€153.5bn** but cost of revenue **€157.7bn** → **gross profit −€4.2bn**; operating income **−€22.2bn**; net income **−€22.4bn**; EPS **−€7.75**; EBITDA **−€15.3bn**. Prior trajectory: NI €16.8bn (2022) → €18.6bn (2023) → €5.5bn (2024) → **−€22.4bn (2025)**. Piotroski **F-score 3/9 (Weak)**; interest coverage, ROA and leverage all fail.

The −24% single-day gap on **2026-02-06** (93M shares, ~6× ADV) is the repricing of that print. Market cap now ≈ **0.08× forward sales** and **0.25× book** — the market is explicitly pricing ~75% further impairment of an already-impaired book.

## 4. Composite Quant Signal: **STRONG SELL**

Bottom of the peer group on **momentum (5/5), quality (5/5), and low-vol (5/5)**. Its only "cheap" attribute is accounting book value, and the P/E, EV/EBITDA and P/FCF inputs are all negative — meaning the value factor is **degenerate here and cannot be scored as attractive**. There is no factor combination in the model under which STLA screens well.

## 5. Key Quant Risk Flags

1. **Value-trap / non-earning multiple.** Negative P/E, EV/EBITDA and P/FCF. A 0.25× P/B on a business with *negative gross profit* is not a discount — it is a probability-weighted further-writedown estimate.
2. **Momentum-reversal & squeeze risk (primary risk to a short).** 53% vol, 60% drawdown, R²=0.070. Factor models explain almost nothing here. Any restructuring, stake-sale or consolidation headline produces violent two-way gaps. Position sizing, not conviction, is the binding constraint.
3. **Dividend is not covered.** Headline **16.35% yield** against negative EPS and negative FCF (P/FCF −0.84). Do **not** treat this as income; the yield is a stale/pre-cut artifact and the cut is the base case.
4. **Beta-hedging is ineffective.** R²=0.070 means a 1.07 beta is noise; a market-neutral factor pair will not isolate the alpha. Residual risk is ~52% annualized.
5. **Estimate quality / coverage gap.** FY2029–30 estimates rest on **1 analyst**; FY2028 on 2. The apparent recovery is unfalsifiable and cannot support a revision-based signal.
6. **Balance sheet.** EV $28.2bn vs mkt cap $13.6bn → **~$14.6bn net debt** with negative EBITDA (leverage undefined). An equity raise at 0.25× book would be maximally dilutive, so dilution risk is real but management has strong incentive to avoid it — favouring asset sales/dividend suspension.
7. **Liquidity: not a flag.** ADV 15–25M shares (>$100M); the gap day traded 93M. Execution is fine.
8. **Sample-size caveat.** All five sector ranks rest on n=5 comparables, and the risk statistics contain the internal inconsistencies noted in §2. **Do not over-fit to the magnitudes; rely on sign and cross-sectional rank.**

**Bottom line:** the numbers do not support the "cheap auto turnaround" story. Every factor except an illusory book-value discount ranks STLA last in its peer group, quality and momentum are unambiguously broken, and the one positive datapoint (revision momentum) fails significance. **Strong Sell on the factor composite**, sized for a fat left tail rather than a smooth one.
