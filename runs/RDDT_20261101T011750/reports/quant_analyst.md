# Quant Analyst

- Symbol: RDDT
- Elapsed: 60.1s

---
# RDDT — Quantitative Factor & Risk Report
*Price used: **$91.67** (last close $91.73, 2026‑10‑30). Mkt cap $17.6B basic / $18.5B diluted (202.1M). Net cash ≈ $2.45B (13% of cap).*

## 1. Factor Scores

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **25** | **4 of 4** | Expensive on trailing/reported basis |
| **Momentum** | **15** | **4 of 4** | Negative |
| **Quality** | **78** | **2 of 4** | Positive / sharply improving |
| **Low Vol** | **8** | **4 of 4** | High risk — worst in group |
| **Earnings Revision** | **55** | **2 of 4** (low conf.) | Mixed — tool says upgrade, tape says cuts |

Peer set = {GOOG, META, NFLX, RDDT} (Internet Content & Information + NFLX). VZ/T/TMUS/DIS excluded as structurally non-comparable. **n=4 is too small for a true quintile rank — treat ranks as ordinal only.**

**Value detail.** P/E 35.0x, EV/EBITDA 29.5x, P/FCF 27.1x, P/B 6.3x vs peers P/E 24.5–26.2x, EV/EBITDA 9.0–18.5x. RDDT pays ~1.8x the peer median EV/EBITDA (16.8x). **Caveat that materially changes this rank:** the ratio engine uses FY2025 annuals (EPS $2.62). On trailing-twelve-months through Q3'26 (diluted EPS $4.90, EBITDA $1,023M), P/E ≈ **18.7x** and EV/EBITDA ≈ **15.7x** — i.e. roughly in line with META (15.2x). The bottom-quintile value rank is an artifact of stale denominators; forward consensus (FY26E EPS $5.43) implies **16.9x**. Only the P/FCF rank (2 of 4) is robust.

**Quality detail.** ROE 18.1%, ROIC 15.0% (from −26.0% in FY24), gross profit/assets **0.62** — best in group (META 0.45, GOOG 0.40) — accruals ratio **−0.0498** (negative accruals = conservative earnings). Piotroski F-score **7/9**; the two failures are *lower leverage* (no debt to pay down) and *no dilution*. Operating margin 20.1% FY25 → **32.6% TTM**. Revenue +69.4% FY25, +61.1% Q2'26, **+53.0% Q3'26**. This is the one genuinely top-quintile factor.

**Momentum detail.** 12‑1 momentum −12.4% vs META +20.2%, GOOG +7.0%, NFLX −2.7%. 12‑month total return −52.8% (−55.6% annualised). Peak-to-trough −66.1% ($270.71 on 2025‑09‑18 → $91.73).

**Revision detail — treat with suspicion.** The engine returns +22.5% (FY2030 EPS $11.90 vs $9.72 prior), but that is a **five-year-out** period with only **9 analysts**. The near-term evidence is opposite: on 2026‑10‑30 (Q3 print) Bernstein cut to $120, Cantor to $120, Guggenheim to $170, Needham to $150. Consensus also implies FY27 revenue growth decelerating to +29% from +53%. I score this 55, not 80.

## 2. Price Statistics (252 trading days)

| Metric | Value |
|---|---|
| Annualised alpha vs SPY | **−111.8%** |
| Beta vs SPY | **2.25** (R² = 0.1415) |
| Annualised return | −55.6% |
| Annualised volatility | **78.5%** |
| Sharpe | **−0.705** |
| Sortino | **−0.925** |
| Max drawdown (252d) | **−58.1%** (peak-to-current −66.1%) |
| Correlation vs SPY / META / GOOG / NFLX | 0.37 / 0.34 / 0.25 / 0.22 |

Volatility is 1.76x META (44.6%), 2.09x NFLX (37.6%), 2.27x GOOG (34.5%). Beta 2.25 is significantly above 1.0 (**t ≈ 6.4**, SE ≈ 0.35), but not distinguishable from 2.0. Sortino < Sharpe means downside semideviation exceeds total SD — a fat left tail, not symmetric risk. **86% of return variance is idiosyncratic (R²=0.14)**; low sector correlation (0.22–0.34) means no crowding in the peer group.

## 3. Composite Quant Signal

**NEUTRAL — composite 36/100** (equal-weighted: 25/15/78/8/55).
Horizon split: **Sell-lean 1–3 months** (negative earnings-gap drift; four successive PT cuts) / **Buy-lean 12 months** (quality 78, TTM 18.7x P/E, +53% revenue growth). The composite is not bottom-decile because quality carries the score; it is not investment-grade because two of five factors sit in the bottom decile.

## 4. Key Quant Risk Flags

1. **Single-event dominance / estimation fragility.** On 2026‑10‑30 the stock gapped **−29.2%** ($129.60→$91.73) on 33.4M shares (~4x ADV) despite an EPS/revenue *beat* ($1.40 vs. trend, revenue $895M +53% YoY). That one session drives >25pp of the annualised alpha and the entire momentum reading. The −111.8% alpha is a real point estimate but a poor forecast — it is one draw, not a distribution.
2. **Small sample / no significance.** RDDT IPO'd 2024‑03‑21; ~19 months of history, one 252d window, zero full cycle. SE on an annualised Sharpe with T=1yr is ≈1.1, so **Sharpe −0.705 is not statistically distinguishable from zero (t≈0.63)**. Volatility SE ≈ ±3.5pp. Do not over-read annualised stats here.
3. **Momentum reversal / PEAD.** A −29% earnings gap into a broad October tech selloff (META and GOOG Sharpe also negative despite positive 12‑1 momentum) leaves beta-2.25 exposure into a de-risking tape.
4. **Valuation-rank distortion.** Any cross-sectional screen using FY2025 annuals will systematically over-rank RDDT as expensive; TTM EV/EBITDA is 15.7x, not 29.5x. Screens built on this data will mis-sell the name.
5. **SBC / dilution.** FY25 SBC $343M = 15.6% of revenue (FY24: $802M = 61.7%). Diluted-minus-basic spread 8.4%; F-score dilution test fails. GAAP net income overstates distributable economics.
6. **Liquidity: NOT a constraint.** ~$500–700M ADV, $17.6B cap, Oct‑30 turnover $3.1B. Exclude from risk list.
7. **Unmodelled: traffic concentration** (search-referral dependence) is the most plausible cause of the gap and is invisible to these factors.

*Gaps: no short-interest, borrow, or options-implied data; peer set limited to 4 names; sector-level quintile ranking therefore proxy-only.*
