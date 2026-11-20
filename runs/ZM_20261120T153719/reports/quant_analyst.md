# Quant Analyst

- Symbol: ZM
- Elapsed: 48.8s

---
## ZM (Zoom Communications) — Quantitative Factor Report
**Price $83.48 | Mkt cap $25.66B | EV $17.90B | FY-end Jan-2026 | Data as of 2026-11-20**

### 1. Factor Scores

| Factor | Score (−2…+2) | Sector Rank (SaaS comp set)* | Signal |
|---|---|---|---|
| Value | **+1.5** | 1st of 5 (top quintile) | Attractive, *only after normalization* |
| Momentum | **−2.0** | 5th of 5 (bottom quintile) | Strongly negative |
| Quality | **+1.0** | 2nd of 5 (top quintile) | Positive, SBC-diluted |
| Low Vol | **−1.5** | 5th of 5 (bottom quintile) | Unfavourable |
| Earnings Revision | **0.0** | n/a — insufficient coverage | Uninformative |

\*The `get_sector_peers` feed returns Technology by market cap (AAPL/MSFT/NVDA/TSM), which is not a valid comp set for an application-software name. I substituted CRM, NOW, TEAM, WDAY, pulled directly.

**Value detail (and the report's central finding).** Headline multiples say ZM is absurdly cheap: P/E 13.5, EV/EBITDA **7.0x**, P/FCF 13.3. These are distorted. FY2026 operating income was $1,123.6M but reported "EBIT" was $2,422.3M and net income $1,900.1M — i.e. **~$1,299M (27% of revenue) of pre-tax income was non-operating**, largely a non-cash gain (OCF of $1,989M vs. NI+D&A+SBC of $2,525M confirms ~$536M+ of gain backed out of cash flow). Normalized:

| Metric | Headline | Core-adjusted |
|---|---|---|
| EV/EBITDA | 7.0x | **~14.2x** (EBITDA $1,256M) |
| P/E | 13.5x | **~29x** (EPS ~$2.88 core) |
| P/FCF | 13.3x | **~22.1x** (SBC-adj: FCF $1,163M) |
| ROE | 19.4% | ~11–12% |

Core EV/EBITDA of 14.2x vs. SaaS peers (CRM 14.3x, NOW 30.9x, WDAY 40.7x, TEAM 172x; median ex-ZM 35.8x) still supports a genuine value signal — but it is "cheapest in software," not "half of book."

**Quality detail.** Piotroski **F-Score 8/9 (Strong)** — 8 of 9 flags green, failing only asset-turnover improvement. ROIC has compounded: 3.89% (FY23) → 6.49% → 9.04% → **11.39% (FY26)**. Gross profit/assets 0.313. Accruals −0.0074 (negative = conservative). Two drags: **SBC is $760.8M, 15.6% of revenue** (trimming from $1,057M in FY24 but still heavy), and accruals quality has *deteriorated* five-fold (−0.146 → −0.097 → −0.085 → −0.0074) — the cushion is nearly gone.

**Growth context (why the multiple is low).** Revenue +4.4% (FY26 $4,869M vs $4,665M), +3.1% prior year — ex-growth. Consensus FY27 $5,093M (+4.6%), FY28 $5,320M (+4.5%).

**Earnings revision — flagged as unreliable.** The revision tool compared FY**2031** EPS of $6.62 vs. $7.346 three months prior (−9.88%) on **4 analysts**. That is not a revision signal; it is noise. Better read: 16-analyst FY27 consensus of $6.15 sits above FY26's $5.967 consensus and reported diluted EPS of $6.18 (a modest beat). Price targets (n=12, Aug–Nov 2026) median **$115.50**, mean $117.9 → +38% implied upside, but every target was posted between $89.70 and $111.62 and direction is mixed (StoneX $125→$130, Bernstein/MS up; UBS $115→$112, Jefferies $118→$116 down). Stale and non-directional → Neutral.

### 2. Price Statistics

| Statistic | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Alpha vs. SPY (ann.) | **−7.45%** | **−4.59%** |
| Beta vs. SPY | 1.12 | 1.13 |
| R² | **0.119** | 0.121 |
| Ann. volatility | 47.5% | 42.6% |
| Sharpe (0% rf) | **0.153** | 0.325 |
| Sortino | **0.232** | 0.513 |
| Annualized return | 7.29% | 13.84% |
| Max drawdown | **−25.9%** | — |

**The alpha is statistically meaningless.** With R² of 0.119, only 12% of ZM's variance is market-driven; residual vol ≈ 44.6%. The standard error on annualized alpha is roughly that same 44.6%, giving **t ≈ −0.17**. Do not present "−7.45% alpha" as a finding — it is indistinguishable from zero. Beta (1.12) is likewise a poor risk descriptor for this name.

Methodology conflict to disclose: the low-vol module reports Sharpe **−0.03** while the dedicated Sharpe/Sortino module reports **+0.153** on near-identical vol (47.54% vs 47.73%), implying an ~8.7pp gap in mean return. The dedicated module is internally consistent (7.29%/47.73%); I use **0.153** as primary. Either way, the honest statement is: **risk-adjusted return is statistically zero.**

Momentum is deteriorating faster than the 12-1 figure captures: 12-1m **−12.81%**, 6m **+7.89%**, 24m −14.4%, and the stock fell **−9.5% on 2026-11-19** (92.68→83.82) on 5.86M shares — an earnings-type gap — leaving it **−24.7% below its Aug-2026 close high of $109.84**.

**Correlation structure** — ZM is a sector bet, not a market bet: CRM 0.52, NOW 0.46, TEAM 0.46, WDAY 0.45, MSFT 0.36, **SPY 0.34**.

### 3. Composite Quant Signal: **NEUTRAL** (composite ≈ +0.2σ)
Top-quintile value *and* top-quintile quality is a rare and normally attractive pairing (F-Score 8, ROIC inflecting 3.9%→11.4%, EV/EBITDA 14.2x core vs. 35.8x peer median). It is offset by bottom-quintile momentum, bottom-quintile volatility, and a fresh post-earnings gap-down. Levels argue Buy; trajectory argues wait. **Neutral, with a Buy bias on a 12-month horizon once the current downdraft stabilizes.** Not a Strong Buy — the value is real but roughly half of it is an accounting artifact, and there is no revision tailwind to trigger re-rating.

### 4. Key Quant Risk Flags
1. **Earnings-quality inflation (highest priority).** $1.30B of FY26 pre-tax income was non-operating. Every headline multiple, the 19.4% ROE and the 7.0x EV/EBITDA must be normalized. Screen-based value models will systematically over-rank this name.
2. **Momentum reversal / falling-knife risk.** −9.5% gap on 3x normal volume, 24.7% off highs, no 12-1 momentum support. Do not treat "cheap" as a catalyst.
3. **Factor crowding in SaaS correlation.** 0.45–0.52 correlation to application-software peers means ZM offers little diversification within a software book; the beta of 1.12 materially understates true sector-factor exposure.
4. **SBC dilution & capital return.** SBC 15.6% of revenue; $1.62B buyback in FY26 partially offsets. FCF is ~40% SBC-dependent on an adjusted basis.
5. **Coverage/liquidity.** FY31 revisions rest on 4 analysts; last bar shows 790k shares (partial session). Small-sample — treat all revision and short-window statistics as low-confidence.
6. **Accruals cushion exhausted** (−0.146 → −0.007), leaving less room for further non-cash earnings support.

**Sample-size caveat:** all price statistics are single- or two-year windows (n=252/504) on a stock with 0.12 R². Alpha, beta and Sharpe should all be read as low-significance estimates, not measurements.
