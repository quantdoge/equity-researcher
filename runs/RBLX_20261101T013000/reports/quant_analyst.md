# Quant Analyst

- Symbol: RBLX
- Elapsed: 24.5s

---
# RBLX — Quantitative Factor & Risk Report

**Price $42.99 | Mkt cap $29.6B | Technology / Electronic Gaming & Multimedia**

---

## 1. Factor Scores

| Factor | Raw Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E −27.9, EV/EBITDA −35.4, P/B 79.6, P/FCF 21.9 | Bottom decile | **Strong negative** |
| **Momentum** | 12-1m **−7.2%**; 6m **+15.7%** | Mid (improving) | **Neutral / mixed** |
| **Quality** | ROIC −56.6%, ROA −11.1%, GP/Assets 0.400, Accruals −0.299 | Lower third | **Low (Piotroski 7/9)** |
| **Low Vol** | Ann. vol 75.6%, β 1.85 | Bottom quintile | **Strong negative** |
| **Earnings Revision** | +196.3% (see caveat) | Not credible | **Unreliable → weak** |

**Value.** Negative P/E and EV/EBITDA make multiples uninterpretable — there is no earnings-based valuation floor. The one non-negative metric, P/FCF of 21.9x, is misleading: FCF is flattered by deferred-revenue working capital ($1.80B OCF vs −$1.07B net income) rather than by profitability. On the only hard accounting anchor, book value of $0.54/sh against a $43 price (P/B **79.6x**), this is among the most expensive assets in large-cap tech.

**Momentum.** Textbook factor conflict: −7.2% on 12-1, but **+15.7%** on the trailing 6 months. The stock has been recovering off a depressed base while still negative over the year. Short-term trend is up; the 12-1 signal that historically carries predictive weight is negative.

**Quality.** Genuinely poor on returns on capital (ROIC −56.6%, negative all four years: −49.6%, −68.8%, −52.8%, −56.6%) but with real operating quality underneath: gross profit/assets of 0.400 is a solid Novy-Marx reading, and the accruals ratio of **−0.299** is deeply negative across all four years, indicating cash earnings far exceed accounting earnings. Piotroski **7/9** (passes ROA improvement, operating CF, accruals, leverage, margin, turnover; **fails positive ROA and fails no-dilution**). The quality factor signal is "low" primarily because ROE (−284%) is an artifact of a near-zero equity base, not because cash generation is bad.

**Low Vol — the clearest negative.** 75.6% annualised volatility and β of 1.85 put RBLX in the worst quantile of any large-cap universe. This is a high-beta, high-dispersion instrument with no defensive characteristics.

**Earnings Revision — flag as invalid.** The tool reports a +196.3% "upgrade," but the comparison is **FY2030 EPS of $0.26 versus the FY2029 estimate of −$0.27** — two *different* fiscal years, not a revision of the same forward period. This is a methodology artifact, not an upgrade signal. The underlying estimate curve does improve monotonically (FY26 −1.42 → FY27 −1.27 → FY28 −1.03 → FY29 −0.27 → FY30 **+0.26**), implying roughly 20-25%/yr loss compression, but **consensus does not model profitability until 2030** — five years out, on only 13 analysts. I assign this factor **no positive weight**.

---

## 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Alpha (ann., vs SPY) | **−66.6%** | **−51.9%** |
| Beta | 1.86 | 1.63 |
| R² | 0.104 | 0.093 |
| Ann. return | −31.0% | — |
| Ann. volatility | 75.0% | 75.6% |
| **Sharpe** | **−0.414** | — |
| **Sortino** | **−0.498** | — |
| Max drawdown | **−53.1%** | — |

**The alpha is the story.** A −66.6% annualised alpha with β of 1.86 means the stock lost roughly 1.9x the market's move *and* an additional ~67pts of idiosyncratic destruction. R² of only 0.10 is critical: **90% of RBLX's variance is unexplained by the market.** Market beta is a weak risk-management tool here — position sizing must be driven by total volatility, not beta-adjusted exposure.

Sharpe (−0.41) and Sortino (−0.50) both negative, with Sortino *worse* than Sharpe, meaning downside deviation exceeds total deviation — the return distribution is negatively skewed. A 53% peak-to-trough drawdown within a single year, on a $29B market cap, is not a liquidity artifact; it is fundamental re-rating risk.

---

## 3. Composite Quant Signal: **SELL**

There is no factor in the top quintile, and three of five are in the bottom quintile. The composite is dragged by the combination that historically performs worst: **negative 12-1 momentum + bottom-decile valuation support + worst-quintile volatility + negative risk-adjusted returns**. The two offsetting positives — 6-month price recovery and genuine cash conversion — are single-factor and unconfirmed by either revisions or profitability.

Analyst price targets corroborate a capped, not a broken, thesis: median target **$50**, mean $49.67 across 12 recent notes (~16% implied upside), but the direction of travel reversed — September notes were raises (Wells Fargo $46→$64, Roth $55→$60, Wedbush $40→$48) while the latest 30-Oct notes were **cuts** (UBS $53→$50, Goldman →$55). Targets are compressing toward the $42-55 cluster as the stock has fallen from ~$52 to $43.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (high).** 12-1 momentum is −7.2% while the last 6 months are +15.7%. This is the classic setup for a failed recovery rally — the longer-horizon signal disagrees with the short-horizon one, and the longer one has the better historical hit rate.
2. **No valuation floor.** With P/B at 79.6x and negative earnings, there is no accounting anchor to stop a de-rating. Drawdowns are unbounded by multiples.
3. **Extreme volatility / poor risk-adjusted return.** 75% vol with Sharpe −0.41 and Sortino −0.50. Negative skew means tail losses exceed what a normal-distribution position-size model would imply.
4. **Dilution.** Piotroski F7 fails: 689.6M diluted shares against negative equity. Share-count growth is a persistent per-share drag on any eventual earnings recovery.
5. **Model risk in consensus.** Breakeven EPS not until FY2030, from 13 analysts. Long-dated estimates on a loss-making platform carry very wide dispersion (FY2028 EPS range −$1.92 to −$0.31 — a 6x spread). Treat all revision and target data as low-confidence.
6. **Not factor-crowded.** The only *positive* risk note: with negative momentum and negative alpha, RBLX is unlikely to be a crowded long — unwind/flush risk is lower than for a consensus darling. Liquidity is ample ($29.6B cap).
7. **Peer correlation is idiosyncratic.** RBLX correlates 0.45 with TTWO, −0.04 with EA, and only 0.32 with SPY. It provides essentially no gaming-sector hedge and little market hedge — it is a standalone idiosyncratic bet, so it cannot be neutralised inside a sector basket.

---

## Data Limitations (stated explicitly)

- **Sector rank is not rigorously computed.** `get_sector_peers` returns only mega-cap semis/software (AAPL, NVDA, MSFT, TSM…) — none are Electronic Gaming & Multimedia comparables. Ranks above are qualitative against a gaming peer proxy (EA, TTWO), not a true cross-sectional z-score. A proper peer screen (EA, TTWO, NTES, RBLX) would materially tighten the quintile assignments.
- **Short sample.** IPO was 2021-03-10; only four annual periods exist (FY22-FY25) and the 504-day window spans ~2 years. Multi-year factor conclusions are not statistically robust — beta standard errors are wide and the −51.9% 2-year alpha is estimated on ~500 observations with R² < 0.10.
- **Earnings revision factor is invalid as computed** (cross-fiscal-year comparison, FY2030 vs FY2029) and was excluded from the composite rather than used.
- Deferred-revenue-driven OCF means P/FCF and accruals both overstate underlying cash quality relative to a subscription-normalised view.
