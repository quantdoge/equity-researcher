# Quant Analyst

- Symbol: HALO
- Elapsed: 32.3s

---
## HALO — Halozyme Therapeutics | Quantitative Factor Report
**Price $103.63 · Mkt cap $11.76B · Healthcare / Biotechnology · Beta (vendor) 0.897**

Data caveats up front: the price history feed terminates 2025-12-31 ($67.30 close) while the live quote is $103.63 — the stock is up roughly **+54% since year-end 2025**. All return statistics below come from computed windows through the current date, so they are current; only the raw OHLC series is stale. Peer set = 5 largest sector comps (LLY, JNJ, ABBV, MRK, AMGN).

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 5.5/10 – mixed | 3 of 5 on P/E; **1 of 5 on P/FCF** | Neutral |
| **Momentum (12-1)** | 9.0/10 | **1 of 6** | **Strong positive** |
| **Quality** | 8.5/10 | 1–2 of 5 | **Strong positive** |
| **Low Vol** | 3.5/10 | 6 of 6 on total vol | **Negative** |
| **Earnings Revision** | 4.0/10 (low confidence) | n/a – n=1 analyst | Negative (unreliable) |

**Value detail:** P/E 40.5x, EV/EBITDA 25.9x, P/FCF **19.9x**, ROE 649% (artifact of a ~$49M book — ignore). P/FCF of 19.9x is the *cheapest* in the peer group (MRK 29.8, ABBV 29.0, AMGN 30.8, LLY 135.5). The headline P/E is inflated by a GAAP net-income decline (FY25 $316.9M vs FY24 $444.1M) *despite* revenue +37.5% ($1.397B vs $1.015B) and operating income +45.5% ($802.6M vs $551.5M) — i.e. the earnings hit sits below the operating line. On cash economics HALO screens cheap; on reported EPS it screens expensive. Genuine "cheap" reading requires the FCF lens.

**Momentum detail:** +32.56% (12-1, ex last 21 days) vs peers LLY +2.25%, JNJ +2.70%, ABBV +7.40%, AMGN +7.65%, MRK +12.84%. HALO is **2.5x the best peer**. Rank 1 of 6.

**Quality detail:** gross profit/assets 0.4625 (rank 2, behind LLY 0.4812); accruals ratio **-0.1325** — the most negative (highest-quality earnings) in the group (ABBV -0.1105, AMGN -0.0248, MRK +0.013, LLY +0.034). ROIC has compounded upward four straight years: **15.96% → 21.32% → 29.50% → 36.62%**. Piotroski F-Score **5/9 (moderate)** — the weakness is balance-sheet/equity items (F5 leverage, F6 equity change down), not profitability.

**Earnings revision detail:** Tool reports **-7.46%** — but this is the FY**2030** consensus (10.01 vs 10.81 prior), carried by **1 analyst**. That is not an investable signal; treat it as noise. Near-term estimate shape from the same feed looks constructive (FY27 $10.42, FY29 $10.81, FY30 $10.01) but consensus coverage is only 3–6 analysts, so revision breadth is unmeasurable. **This is the weakest data point in the model and I am discounting it heavily.**

### 2. Price Statistics

| Metric | Value | Window |
|---|---|---|
| Annualised return | 53.21% | 504d |
| Alpha (annualised) | **+41.57%** | 504d |
| Beta vs SPY | **0.563** | 504d |
| R² vs SPY | **0.0376** | 504d |
| Sharpe (0% rf) | **1.452** | 504d |
| Sortino | **2.064** | 504d |
| Annualised vol | 36.65% | 504d |
| Annualised vol | 43.44% | 252d |
| Beta vs SPY | 0.591 | 252d |
| Max drawdown | **-24.13%** | 252d |

**Read the R² before the alpha.** R² = 0.038 means the market explains under 4% of HALO's variance — this is an idiosyncratic single-asset bet, not a beta play. Residual vol ≈ 35.9%; with a 2-year window the standard error on that alpha is roughly 25%, giving **t ≈ 1.6 — NOT statistically significant at 5%**. The 41.6% alpha is directionally real but statistically undemonstrated; I would not defend it as skill at conventional confidence.

Sharpe of 1.45 is computed at 0% rf; at a ~4% risk-free rate it drops to ~1.34. Sortino/Sharpe of 1.41 confirms downside vol is not disproportionately large over the window, but see the gap risk flag below.

### 3. Composite Quant Signal: **BUY** (not Strong Buy)

Momentum rank 1 of 6, quality top-2 with rising ROIC and negative accruals, cheapest FCF yield in the peer set, beta 0.56, and short interest-independent purity of cash generation. What keeps it off Strong Buy: total volatility is the *highest* in the peer group (43.4% vs mega-pharma ~20%), meaning the low-vol factor is a material drag, and the value signal only works on one of three metrics. A top-quintile momentum + quality + FCF-yield combination is genuinely rare — but the -7.5% revision print and 25.9x EV/EBITDA cap the score.

*Corroborating (non-model) check:* sell-side targets have been revised **up** repeatedly — Morgan Stanley 78→94→96→93→105, H.C. Wainwright 90→95→115→130, Wells Fargo 65→75→95, Leerink upgraded to Outperform (Aug-2026). Median target ~$130 vs $103.63 spot (~+25%). This directly contradicts the tool's negative revision signal and supports my discount of it.

### 4. Key Quant Risk Flags

1. **Gap risk / fat left tail (HIGH).** 2025-05-13: $66.58 → $50.23 in one session (**-24.5%**), on ~14M shares. 2024-11-15: -15% over two days. Daily-vol models materially understate tail risk for this name; Sharpe/Sortino overstate the risk-adjusted case for a real-money position.
2. **Momentum reversal / extension risk (MEDIUM-HIGH).** +54% since 2025-12-31 on top of a 32.6% 12-1 print, with the stock now within 25% of the median price target. Mean-reversion risk is elevated at these levels; the 12-1 signal is strong but late-stage.
3. **Factor crowding: LOW.** Beta 0.56 and R² 0.04 mean HALO is not a crowded beta or momentum-index holding — a genuine diversifier.
4. **Liquidity: ADEQUATE.** ~2M shares/day ≈ $200M notional; 11.7M- and 21.4M-share spikes are index/event days, not structural illiquidity.
5. **Coverage thinness (MEDIUM).** 1–6 analysts across forecast years. Every consensus-based metric (revision momentum, target dispersion) is low-confidence here; the revision factor should be weighted at roughly half the nominal weight until breadth improves.
6. **Structural: royalty/partner concentration.** Revenue is licensing-and-royalty driven on ENHANZE; it produces superb FCF conversion but is inherently event-concentrated — consistent with both the negative accruals and the gap risk above.
