# Quant Analyst

- Symbol: CHTR
- Elapsed: 74.4s

---
## CHTR — Quantitative Factor & Risk Report
**Price $138.39 (13-Nov-2026) · Mkt cap $19.1B · EV $115.7B · Net debt ≈ $96.6B**

---

### 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank (telecom peers: VZ, T, TMUS) | Signal |
|---|---|---|---|
| **Value** | **95** | **1 of 4** | **Strong positive** |
| **Momentum** | **5** | **4 of 4** | **Strong negative** |
| **Quality** | **60** | **2 of 4** | Neutral / leverage-distorted |
| **Low Vol** | **3** | **4 of 4** | **Strong negative** |
| **Earnings Revision** | **15** | **4 of 4** | **Negative (tool output overridden)** |

**Value — genuinely the cheapest name in telecom.** CHTR is cheapest on all three legs: P/E 3.82 (VZ 11.4, T 7.3, TMUS 17.5), EV/EBITDA 5.46 (VZ 7.5, T 5.8, TMUS 9.9), P/FCF 4.31 (VZ 10.0, T 8.2, TMUS 12.5). P/B 0.93 — below book for the first time. Equity FCF yield ≈23%. On the numbers this is a top-quintile value score. **Caveat: this is a distress multiple, not a mispricing multiple** — see leverage math below.

**Momentum — worst in sector, but a violent reversal is underway.** 12-1 momentum −30.06% vs VZ −3.2%, T −0.0%, TMUS −11.1%. However the last 21 trading days (the window the 12-1 signal *excludes*) returned **+25.8%** ($109.99 → $138.39), and the stock is **+36.9% off the 26-Oct low of $101.11**. Classic momentum-crash/reversal configuration — the factor signal is negative but decelerating.

**Quality — the ROE is an artifact of leverage.** ROE 24.3% ranks 1/4, but ROA is only 3.23% and ROIC 11.34% (flat for 4 years: 11.08→11.47→11.08→11.34). ROE is high because equity ($20.5B) is thin against $96.6B net debt, not because the business earns exceptional returns. Gross profit/assets 0.1645 ranks 3/4. Accruals −7.19% ranks 2/4 (excellent — cash conversion is far above reported earnings: OCF $16.1B vs NI $5.0B). Piotroski **F-Score 7** (moderate-strong), with points for gross-margin improvement (39.0%→46.3% since 2023) and aggressive buybacks (diluted shares 164.4M→137.7M, −16%). ROE trend is deteriorating: 40.3→31.0→25.8→24.3.

**Low Vol — the worst possible score.** Realised vol **59.0%** vs VZ 25.8%, T 30.3%, TMUS 37.8%. Max drawdown 58.8% in the 252-day window; −76.3% peak-to-trough since May 2025. Beta of −0.12 is **statistically meaningless** (R² = 0.0009; t-stat on the slope ≈ 0.48, p ≈ 0.63). This is not a low-beta stock — it is a high-vol stock with zero market correlation.

**Earnings Revision — tool output is invalid; the real signal is negative.** The tool reports **+27.55% "upgrade"** by comparing the FY**2030** EPS estimate ($77.09) against the FY**2029** estimate ($60.44). Those are two different fiscal years, not two vintages of the same year — the "revision" is a term-structure artifact, and FY2030 carries **2 analysts**. Discard it.
The actual revision evidence is unambiguously negative: **seven consecutive price-target cuts** (UBS $235→$140, Deutsche Bank $215→$150, Wells Fargo $160→$101, Barclays $130→$115, Bernstein $150→$120, RBC $160→$150) plus a **downgrade to Underperform** (Wolfe). Median target ≈ **$120–125 vs spot $138.39 (−10%)**. Forward consensus is also internally incoherent: FY2026E EPS $15.12 (−58% YoY) on revenue *up* 5.5% to $57.8B — implying an unmodelled one-off charge — then $44.57 (2027), $53.44 (2028) with a 2027 range of **$19.30–$66.34**. Coverage is 2–7 analysts. **These estimates are not usable for a revision signal.**

---

### 2. Price Statistics (252-day window, vs SPY, rf = 0%)

| Metric | Value |
|---|---|
| Annualised return | **−53.52%** |
| Annualised volatility | **59.5%** (59.04% on vol-tool basis) |
| Beta vs SPY | **−0.121** (R² 0.0009 — not significant) |
| Alpha (annualised) | **−46.73%** |
| Sharpe ratio | **−0.899** |
| Sortino ratio | **−1.108** (implied downside deviation ≈ 48.3%) |
| Max drawdown (252d) | **−58.83%** |
| Peak-to-trough (May-25 → Oct-26) | **−76.3%** ($427.25 → $101.11) |
| Current drawdown from peak | **−67.6%** |

**Statistical caveat (important):** with one year of daily data, the standard error of the annualised mean return is approximately the annualised volatility itself (~59.5%). So the −53.5% annualised return carries a t-stat of only ≈ **−0.9** — the *mean return* is not statistically distinguishable from zero. The same applies to alpha (t ≈ −0.8). What *is* certain is the arithmetic: the price fell 62% over the period and sits 67.6% below its peak. Treat the point estimates of Sharpe/Sortino/alpha as descriptive of one realised path, not as precise parameters.

**Correlation structure — CHTR is idiosyncratic, not a sector trade:**
CHTR–VZ **0.357** · CHTR–T **0.341** · CHTR–TMUS **0.263** · CHTR–SPY **−0.029**
(For contrast, VZ–T = 0.824, VZ–TMUS = 0.669.) The collapse is company-specific (broadband subscriber loss), not a sector de-rating — though all four telecoms show negative SPY beta in this window, implying a sector-wide relative de-rating against a rising index.

---

### 3. Composite Quant Signal

Weighting: Value 30% · Quality 20% · Momentum 20% · Low Vol 15% · Revisions 15%

**Composite = 44 / 100 → NEUTRAL (with a negative tactical tilt)**

The score is held up entirely by the value factor. Strip value out and CHTR scores in the bottom decile of every other dimension. I do not treat a 44 as "balanced" here: the value signal and the risk signal are describing the same fact — the market is pricing a levered EBITDA stream it no longer trusts.

**The leverage multiplier is the whole story:** EBITDA $21.2B against an equity market cap of $19.1B. At 5.46× EV/EBITDA, a **1% change in EBITDA moves equity value ~6.1%**. That single statistic explains the 59% vol, the −76% drawdown, and the 3.82× P/E simultaneously. Interest expense of $5.04B consumes **38% of EBIT** ($12.5B); EBITDA/interest coverage is 4.2× — thin for a capital-intensive cable operator with declining EBITDA ($21.40B → $21.21B).

---

### 4. Key Quant Risk Flags

1. **Value-trap / distress-multiple risk (HIGH).** P/E 3.82 and P/B 0.93 are not cheapness — they are the market's discount rate on a 6.1× levered equity stub with flat-to-declining EBITDA and revenue stuck at ~$55B for four years.
2. **Momentum reversal risk — now bidirectional (HIGH).** The −30% 12-1 signal argues for continued weakness, but +36.9% off the October low on rising volume means a short-squeeze/reversal is live. Shorting into this is as dangerous as buying it. The factor signal has lost information value at this inflection.
3. **Factor crowding (LOW).** Correlation to peers is 0.26–0.36 and to SPY is −0.03. There is no crowded factor exposure here; the position is almost pure idiosyncratic risk. That cuts both ways — no factor support in a drawdown.
4. **Liquidity (MODERATE).** Normal ADV ~2–3M shares (~$300–400M notional) is adequate. But the tape gaps violently on news: **−25.5% on 24-Apr-2026** (13.3M shares, $233→$180), −18.6% on 25-Jul-2025 (9.6M shares), and 17.9M-share and 12.7M-share event days in Jun-2026. Slippage and gap risk on earnings/catalyst dates is severe and cannot be hedged with a market beta (R² = 0.0009).
5. **Data-quality flag on estimates (HIGH).** The revision factor is uncomputable from this dataset — the FY2026 EPS estimate is inconsistent with its own revenue line, FY2027 dispersion spans $19.30–$66.34, and FY2030 has 2 analysts. Any revision-based thesis on CHTR should be rebuilt from the price-target revision series, which is uniformly negative.
6. **Sample-size flag.** All single-year statistics (Sharpe, Sortino, alpha, beta) rest on ~252 observations = effectively one independent annual observation. Beta and alpha are not statistically significant. Only the drawdown and the price change are facts rather than estimates.

**Bottom line:** Top-quintile value, bottom-quintile on everything else. The quantitative case for CHTR is a levered-recovery bet on EBITDA stabilisation, not a factor-driven buy. **Neutral / avoid until either EBITDA inflects or the equity de-levers** — the cheap multiple is compensation for 6× operating leverage, not an anomaly to be arbitraged.
