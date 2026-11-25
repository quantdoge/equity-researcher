# Quant Analyst

- Symbol: INSM
- Elapsed: 80.7s

---
## INSM (Insmed Inc.) — Quantitative Factor Report
**Price basis:** $163.52 (last close 2026-03-31). *Note: valuation-ratio endpoint uses $170.15 (+4.1%) — as-of mismatch flagged.* Market cap ≈$36.4B; Healthcare / Biotechnology.

### 1. Factor Scores Table
Scores are percentiles against a hand-built commercial-stage biotech comp set (VRTX, BMRN, ALNY + INSM, n=4). **Sample size n=4 — ranks are illustrative, not statistical.**

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| Value | 2 / 100 | 4 of 4 | **Very Bearish** |
| Momentum (12-1) | 92 / 100 | 1 of 4 | **Strong Bullish** (see data conflict) |
| Quality | 8 / 100 | 4 of 4 | **Bearish** |
| Low Vol | 15 / 100 | 4 of 4 | **Bearish** |
| Earnings Revision | 50 / 100 | n/a | **Neutral / indeterminate** |

**Value:** Every multiple is negative or extreme — P/E −26.5, EV/EBITDA −30.5, P/FCF −37.6 (FCF yield −2.66%), P/B **49.2**. On P/B it is the most expensive in the comp set (BMRN 2.2, VRTX 7.8, ALNY 28.1); on EV/EBITDA and P/FCF peers trade 21–33x and 18–48x while INSM is loss-making → unrankable at the bottom. The only coherent valuation lens is forward: 51x 2028E EPS ($3.20), 25x 2029E, 16x 2030E ($10.00).

**Quality:** ROE −172.8%, ROIC −78.1%, ROA −56.4%. Gross profit/assets 21.3%. Piotroski F-score **5/9**, but all 5 points come from leverage/working-capital terms — it scores **zero on all four profitability tests** (negative ROA, negative operating CF). Accruals ratio is a genuine positive: **−0.151** (conservative, cash burn exceeds accounting loss). Operating quality is real where it counts: gross margin **79.4%** (vs 76.4% in 2024), revenue **+66.7% to $606.4M**. The disqualifier is dilution: shares 164.0M → 213.6M (**+30.2% in one year**, +52% since 2023), plus SBC of $152.7M = 25% of revenue.

**Momentum — data conflict, treat as unresolved:** the momentum tool returns **−26.0%**. Recomputing 12-1 from the raw price series (2025-03-28 close $77.99 → 2026-03-02 close $146.32) gives **+87.6%**. I cannot reconcile the two and cannot verify which window the tool uses; the price series is the auditable source, so I lean strongly positive but haircut conviction. Total return since 2024-01-02 is **+446%**. Price is **−22.7%** from the 52-week closing high ($211.41, 2025-12-01) and **+152%** off the trailing low (~$64.8).

**Earnings Revision — the tool output is invalid.** It reports "+54.4% upgrade," but that compares the **FY2030** EPS estimate ($10.00) against the **FY2029** estimate ($6.48). That is a different fiscal year, not a revision. **Discard this signal.** The only genuine revision evidence available: FY2025 consensus was −$5.85 EPS vs −$6.41 actual (**miss**) and $582.4M revenue vs $606.4M actual (**+4.1% beat**) — revenue revisions likely up, margin/EPS revisions down. Consensus path: −$1.62 (2026E) → +$0.68 (2027E) → +$3.20 (2028E) → +$10.00 (2030E). Dispersion on 2028E is $0.62–$6.05 (**±85%**), i.e. near-zero informational content.

### 2. Price Statistics
| Metric | 252d | 504d |
|---|---|---|
| Annualised volatility | 72.93% | 65.03% (60.84% alt) |
| Beta vs SPY | 0.439 | 0.358 |
| Alpha (ann., vs SPY) | — | **+75.06%** |
| R² vs SPY | — | **0.0059** |
| Sharpe | 0.564 | **0.874** (1.234 alt) |
| Sortino | — | **1.326** |
| Max drawdown | −44.28% | **−56.54%** |
| Ann. return | — | 53.2% |

**Interpretation:** Beta 0.36–0.44 (0.808 on the profile's 5-yr basis — dispersion is itself a flag) with **R² = 0.006** means SPY explains essentially **none** of INSM's returns. The +75% alpha is therefore *not* a skill/market-relative statistic — with residual vol ~60% over 2 years, standard error on alpha is ~42%, giving **t ≈ 1.8: not significant at 5%**. Sortino/Sharpe of 1.33/0.87 are respectable on a raw basis but rest on a handful of binary catalyst days (e.g. +118% on 2024-05-28, +28.6% on 2025-06-10, −16.1% on 2025-12-18), so the ratios are **not robust** — remove three days and the profile inverts. Also note internal inconsistency: Sharpe prints 0.874 vs 1.234 over the same 504-day window.

### 3. Composite Quant Signal: **NEUTRAL**
One factor (momentum) is doing all the work; value, quality and low-vol are all bottom-of-cohort. A pure cross-sectional multi-factor model would not buy this — it would screen it out on quality and valuation. It's a catalyst-driven binary biotech, not a factor stock.

### 4. Key Quant Risk Flags
1. **Momentum reversal risk — high.** −22.7% off the 52w high with realised vol 65–73%; failure of the recent bounce toward $163 would confirm a lower-highs sequence. The momentum tool's negative print, even if rejected, is a warning.
2. **Cash runway / financing risk.** Cash & ST investments $1.430B vs FCF of **−$967.6M** in 2025 (worsening from −$705.8M and −$549.5M). Roughly **1.5 years of runway at current burn** before another raise; net debt $257.7M, total debt $768.2M, interest expense $83.8M. Any equity raise hits a $36B cap with 213.6M shares already out.
3. **Dilution as a permanent headwind.** +30% share count in 2025 alone. Reported EPS growth understates per-share value creation.
4. **Factor crowding: LOW — the one genuine positive.** Correlation with XBI **0.386**, BMRN 0.347, VRTX 0.274, ALNY **0.039**. This is not a crowded factor long. Corollary: it is ~pure idiosyncratic risk and provides almost no diversification inside a biotech sleeve.
5. **Liquidity: NOT a constraint.** ~2.0–2.7M shares/day (~$350M), 15M+ share days on catalysts. Adequate for institutional size.
6. **Estimate dispersion ±85% on 2028E** — any DCF or target multiple built on that path is speculative, not analytical.

### Statistical Caveats
- Peer set is n=4 and hand-selected; the "sector peers" tool returned mega-cap pharma (LLY, JNJ, ABBV) that are not valid comparables for a pre-profit rare-disease biotech.
- Two of the five factor inputs (earnings revision, momentum) returned values I could not validate or had to override. Factor scores for those rows carry low confidence.
- 504 trading days = 2 years of history. For a stock with 65% vol and a binary catalyst distribution, two years is **not enough for statistically meaningful Sharpe/alpha estimates**.
