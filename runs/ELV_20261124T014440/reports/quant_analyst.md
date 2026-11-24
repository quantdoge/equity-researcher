# Quant Analyst

- Symbol: ELV
- Elapsed: 25.6s

---
## ELV — Elevance Health: Quantitative Factor Scorecard

**Price:** $379.55 | **Market cap:** $82.0B | **Sector:** Healthcare / Managed Care | Data through FY2025 (12/31/25) annuals; price history through 12/31/25

---

### 1. Factor Scores Table

*Peer set = managed-care cohort (UNH, CI, CVS, HUM, CNC). ⚠️ Note: `get_sector_peers` returned broad-sector Healthcare (mostly pharma: LLY, JNJ, ABBV, MRK). Those are not valid comparables for a health insurer, so I built the ranking on the managed-care cohort instead. Rank is 1=best of 6.*

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 15.1, EV/EBITDA 11.2, P/B 1.91, P/FCF 26.5 | **2 / 6** | **Positive** |
| **Momentum** (12-1) | +8.21% | **2 / 6** | **Positive (low magnitude)** |
| **Quality** | ROE 12.86%, GP/A 0.419, accruals +0.0113, F-score 6/9 | **2 / 6** | **Neutral** |
| **Low Vol** | σ 34.0%, β 0.06–0.15, max DD 19–31% | **4 / 6** | **Negative** |
| **Earnings Revision** | +16.06% (2030 EPS est.) | **2 / 6** | **Positive — but N=1 analyst** |

**Value detail (lower = cheaper):**

| | ELV | CI | UNH | HUM | CVS | CNC |
|---|---|---|---|---|---|---|
| P/E | 15.1 | **12.2** | 25.4 | 39.0 | 57.3 | n.m. (-4.7) |
| EV/EBITDA | 11.2 | **8.2** | 15.4 | 19.0 | 17.3 | n.m. |
| P/FCF | 26.5 | **8.6** | 19.0 | 123.6 | 13.0 | 7.2 |

ELV is a clear #2 — cheap on P/E and EV/EBITDA, but **P/FCF of 26.5 is the weakest of the profitable peers**, because 2025 operating cash flow ($4.29B) fell below net income ($5.66B) for the first time in four years. On cash-based valuation ELV is not cheap.

**Quality detail:** ELV has the **highest gross-profit/assets in the cohort (0.419)** and #2 ROE (12.86%, behind CI's 14.23%), but the **worst accruals ratio (+0.0113)** — every other peer posted negative accruals (UNH −0.025, CVS −0.035, CNC −0.153). F-score 6/9, failing on ROA improvement, accruals quality, and gross-margin improvement. More importantly, the trend is deteriorating, not stable:

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| ROE | 16.22% | 15.19% | 14.44% | **12.86%** |
| ROIC | 13.60% | 13.24% | 11.99% | **10.50%** |

Four straight years of decline on both metrics. GP/A being high is a *static* strength masking a *dynamic* decay.

**Earnings revision detail:** ELV +16.1% (rank 2/6), CNC +19.1, UNH +11.6, CI +9.9, CVS +7.2, HUM −5.1 (only downgrade). **⚠️ Critical caveat: the revision metric is computed on the FY2030 consensus, and ELV's 2030 EPS carries `num_analysts: 1`.** A one-analyst estimate revision is not statistically meaningful — it is a single model update, not consensus breadth. Nearer-dated estimates have proper coverage (FY2027: 13 analysts, $30.31; FY2028: 5 analysts, $34.62). Treat ELV's revision signal as **unverified** rather than bullish.

---

### 2. Price Statistics

| Metric | 504-day (2yr) | 252-day (1yr) |
|---|---|---|
| Annualised return | 9.71% | — |
| Annualised volatility | 37.42% | 34.00% |
| Beta vs SPY | 0.154 | 0.064 |
| Alpha (annualised) | **+5.11%** | — |
| R² vs SPY | **0.0032** | — |
| Sharpe (0% rf) | **0.257** | 0.593 |
| Sortino (0% rf) | **0.296** | — |
| Max drawdown | 30.6% | 19.37% |

**⚠️ Beta is unusable as stated.** Three sources disagree: vendor profile β = 0.711, 504d regression β = 0.154, 252d β = 0.064 — and the 252d correlation with SPY is **0.030**. The regression is internally consistent (0.030 × 34.0%/14.5% ≈ 0.07), so the recent decoupling is real, not a data error; the 0.711 figure likely uses 5-year monthly data. **R² of 0.32% means the market factor explains essentially none of ELV's variance.** ELV is not a market-beta story — it is a pure managed-care policy/medical-cost factor trade. Any risk model relying on β ≈ 0.7 (or 0.06) will mis-size this position badly.

**⚠️ Max drawdown figure looks understated.** The 504d tool reports 30.6%, but the raw price history I retrieved shows a peak-to-trough of **−51.0%** ($544.58 on 9/3/24 → $267.04 on 8/4/25). I'd trust the raw-series figure. Note also that ELV's realized vol (34–37%) is *barely below* its absolute price decline — this is a high-dispersion name, and the 12-1 momentum of +8.2% is only ~0.24× annualised vol: **not a statistically robust momentum signal.**

Sharpe of 0.257 / Sortino 0.296 over two years is poor — below the ~0.5 threshold most allocators require. Returns came almost entirely from a violent post-July-2025 mean reversion (+29% off the August low), not from steady compounding. The 252d Sharpe of 0.593 flatters a single lucky rebound.

---

### 3. Composite Quant Signal: **NEUTRAL** (borderline Buy)

Rough factor composite (each factor scored −2 to +2): Value +1.5, Revision +1.0 (haircut from +1.5 for N=1), Momentum +1.0, Quality +0.5, Low Vol −0.5 → **mean ≈ +0.7 → Neutral.**

The case for a Buy: top-2 ranking on value, momentum, and revisions, with a 15× P/E and 1.9× book on an $82B franchise. The case against: (a) quality is decaying four years running (ROIC 13.6% → 10.5%), (b) the revision signal rests on one analyst, (c) risk-adjusted returns are weak (Sharpe 0.26), (d) the momentum is a reversal bounce inside a −51% drawdown, not trend. Value and revisions say Buy; the deterioration trend and risk metrics say don't pay up for it. **Net: interesting valuation, unproven inflection.**

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** The +8.2% 12-1 return sits atop a −51% drawdown and consists of a single +29% mean-reversion leg off the August 2025 low. The stock has printed four separate >10% single-day gaps in 15 months (10/17/24 −12%, 7/2/25 −11%, 7/17/25 −12%). Momentum continuity is not established.
2. **Quality decay / accruals deterioration.** ROIC down 310bp in three years; 2025 OCF ($4.29B) below net income ($5.66B) for the first time — the only cohort member with positive accruals. P/FCF 26.5 vs CI's 8.6. This is the single most under-priced risk in the name.
3. **Factor crowding via managed-care correlation — MODERATE/HIGH.** ELV correlates 0.58 with UNH, 0.60 with CNC, 0.53 with HUM, 0.54 with CI, but only **0.03 with SPY**. This is a sector bet in disguise: 100% of its risk is a single, highly-correlated policy/medical-cost factor. Any managed-care derating hits it with no market offset. Correlation with CVS is lower (0.29), the one genuine diversifier in the group.
4. **Unreliable beta → mis-sized risk.** R² = 0.32%. Beta estimates spanning 0.06 to 0.71 mean hedging and position sizing must be done on total vol (34%) and factor correlation, not CAPM beta.
5. **Liquidity is fine:** ADV ~1.5M shares (~$500M/day); no liquidity constraint. Not a risk.
6. **Sample-size flags:** revision score N=1 analyst (not significant); 252d beta estimated on a window containing two guidance-shock outliers (not robust); 12-1 momentum is 0.24× annual vol (not significant at conventional thresholds).

**Peer data gaps:** the mandated `get_sector_peers` output (pharma-heavy) was unusable for cross-sectional ranking; I substituted the managed-care cohort from knowledge of the industry. Peer FY2025 annual detail was limited to factor-tool outputs — no peer-level statement data was pulled for CI/CVS/HUM/CNC beyond the standardised factor metrics.
