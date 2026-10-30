# Quant Analyst

- Symbol: GKOS
- Elapsed: 60.4s

---
# GKOS — Glaukos Corporation | Quantitative Factor Report
**Price $242.48 (29-Oct-2026) · Mkt cap $14.30B · EV $13.73B · Healthcare / Medical Devices**

---

## ⚠️ Data Integrity Note (read first)
Three tool outputs are internally inconsistent with the raw OHLCV tape, and I use **recomputed-from-raw values** where I can arithmetically verify them:

| Metric | Tool output | Recomputed from OHLCV | Resolution |
|---|---|---|---|
| 12-1 momentum | +6.74% | **+101.3%** (81.55 → 164.19, skip-21d) | Tool window mis-specified; use recomputed |
| 1-yr total return | implied 79.02% | **+214.5%** (77.09 → 242.48) | Return annualised over wrong period |
| Sharpe/Sortino | 1.413 / 2.771 | see §2 | Tool values reported but flagged |

Max drawdown **−28.39%** *does* reconcile exactly (peak 143.82 20-May-26 → trough 103.12 01-Jun-26), confirming the risk window is current.

---

## 1. Factor Scores

| Factor | Score / Raw Value | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E −73.9 · EV/EBITDA −94.0 · P/FCF −256.8 · **P/B 21.1** · P/S ≈ 21x TTM | **5th quintile (bottom)** | **Negative** — no earnings, no FCF, 21x book; valuation is purely option-value on future iDose/cataract ramp |
| **Momentum** | 12-1 **+101.3%** · 12-mo +214.5% · YTD +114.7% | **1st quintile (top)** | **Strongly positive** |
| **Quality** | ROE −28.6% · ROIC −10.9% · ROA −21.0% · GP/Assets **0.440** (good) · Accruals **−0.158** (conservative) · **Piotroski F 3/9** | **4th quintile** | **Negative, improving** — negative ROIC 4 yrs running; F-score components F1–F3, F5–F7 all fail |
| **Low Vol** | σ 64.57% (~4.3x S&P) · β 0.738 · R² vs SPY **0.026** | **5th quintile** | **Negative** — beta is statistically meaningless at R²=0.03; true risk is ~65% idiosyncratic |
| **Earnings Revision** | +64.24% (2030E: $4.64 vs $2.83) | n/a (long-dated) | **Positive but low-confidence** — see caveat |

\* *Peer tool returned mega-cap pharma (LLY, JNJ, ABBV…), not device comps. Ranks are my judgment vs. the true Medical-Devices cohort (ISRG/BSX/MDT/SYK), not a computed cross-sectional z-score. **Treat as directional, not scored.***

**Revision-score caveat (important):** the +64.2% is measured on the **FY2030** estimate carried by **5 analysts**. That is a 4-year-out number with high dispersion (low $4.30 / high $5.02) and is not the 12-month revision signal the factor is meant to capture. The *credible* revision evidence is consensus EPS trajectory — **FY26 −$0.30 → FY27 +$0.52 → FY28 +$1.65 → FY29 +$2.83** — plus six brokers raising targets on 29-Oct-26 (Mizuho $190→$225, Stifel $190→$225, Piper $195→$240, Needham →$251, Truist →$255, H.C. Wainwright $195→$248). Direction is unambiguously up.

**Fundamental inflection behind the revision (Q3-26, reported 28-Oct-26):**
- Revenue $211.0M, **+58% YoY** (vs $133.5M); sequential $150.6M → $185.6M → $211.0M
- **First GAAP profit: NI +$2.0M, EPS +$0.03** (vs −$0.34 in Q1-26)
- Gross margin **85.2%**; TTM revenue $690M, gross profit/assets 0.440 confirms pricing power
- FY25 OCF still **−$46.3M**; accruals ratio −0.158 reflects large non-cash charges (Q4-25 net loss −$133.7M vs op. loss −$27.0M)

---

## 2. Price Statistics

| Metric | Value | Assessment |
|---|---|---|
| Beta vs SPY (504d) | **0.739** | Low — but see R² |
| **R² vs SPY** | **0.0258** | **Only 2.6% of variance is market-explained** — beta is not usable for risk budgeting |
| Alpha (annualised, 504d) | **+66.3%** | **Not statistically significant: t ≈ 1.7** (α ÷ σ/√2yrs = 66.3/39.5). Fails a 5% test |
| Annualised vol (252d) | **64.57%** | Extreme; ~4.3x market |
| Max drawdown (252d) | **−28.39%** | Verified; three separate >19% drawdowns in 12 months |
| Sharpe (504d / 252d) | **1.413 / 1.637** | Flattered by a mis-annualised mean return; on verified +214.5% 12-mo return Sharpe ≈ 3.3 — an exceptional-year artifact, not a stable expectation |
| **Sortino (504d)** | **2.771** | Implies annualised downside deviation ≈ 28.5% (≈51% of total vol) — downside is nearly as large as total risk |
| Correlation: SPY / ISRG / ALC | **0.148 / 0.163 / 0.281** | Very low — diversifying, but because returns are event-driven, not because of defensive characteristics |
| Realised 1-yr / YTD return | +214.5% / +114.7% | All-time high set 29-Oct-26 (+33.6% **single session**, 5.4M shares vs ~1.1M ADV) |

**Event-risk concentration:** the entire recent move is two gap days — 29-Oct-26 (+33.6%) and 30-Apr-26 (+22.9%), plus the 21-Feb-25 (−20.0%) and 20-Oct-25 (−8.8%) air-pockets. This is a headline-driven tape; the historical Sharpe/Sortino **will not** persist through the next binary catalyst.

---

## 3. Composite Quant Signal

### **NEUTRAL** (trend-positive, factor-unsupported)

- **Supports:** #1-quintile momentum, unambiguously positive estimate revisions, genuine fundamental inflection (first profit, 58% growth, 85% gross margin), very low market correlation.
- **Against:** bottom-quintile **Value** and **Low Vol**; 4th-quintile **Quality** (F-score 3/9, ROIC −10.9% for four consecutive years); alpha statistically insignificant (t≈1.7); ~65% idiosyncratic vol.
- **Why not Buy:** a "top-quintile on value *and* momentum *and* quality" name this is not. Two of five factors are bottom-quintile, one is fourth-quintile. The positive signals are (a) a momentum print with a bad measurement window and (b) a revision metric computed on a 2030 estimate with 5 analysts.
- **Why not Sell:** the revision *direction* is real and broad-based, operating leverage is inflecting, and there is no factor-crowding evidence (correlation to ISRG 0.16 shows it is not being traded as a medtech proxy).

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / gap-retracement risk (HIGH).** +33.6% on 29-Oct-26 on 5x normal volume. Post-earnings-announcement drift is positive but a single-session re-rating of this size historically mean-reverts: three prior >19% drawdowns in 12 months (−28.4%, −22.9%, −19.1%).
2. **Statistical insignificance (HIGH).** Alpha t≈1.7, R²=0.026, and revision score n=5. **No factor conclusion here clears a 5% significance bar.** Sample size is the binding constraint — this is a single-name, single-catalyst story, not a repeatable signal.
3. **Volatility / drawdown asymmetry (HIGH).** σ 64.6%, Sortino/Sharpe ratio 1.96 (normal is ~1.3–1.5) — dispersion of outcomes is wide. Position size should scale to 4x-market vol, not to beta 0.74.
4. **Factor crowding (LOW).** Correlation with ISRG 0.16, ALC 0.28, SPY 0.15 — no crowding signature.
5. **Liquidity (LOW).** ~1.1M shares ADV ≈ $200M+/day at current price; $14.3B cap. Institutionally tradeable; note volume is event-spiky (2.2x–5.4x ADV on news days).
6. **Valuation floor risk (MEDIUM).** 21x book, 21x TTM sales, negative EV/EBITDA and P/FCF. There is no valuation support in a derating scenario — downside is a multiple, not earnings, event.
7. **Accounting quality (MEDIUM, improving).** F-score 3/9; FY25 OCF −$46M; but accruals −0.158 and Q3-26 GAAP profitability indicate the trajectory has turned.

---
**Bottom line:** statistically the strongest things you can say about GKOS are (i) momentum is real and extreme, (ii) estimate revisions are broadly upward, (iii) the fundamental inflection in Q3-26 is measurable and not narrative. Everything else — value, quality, low-vol, alpha significance — is weak or fails a significance test. **Neutral composite, tactical-monitor, unsuitable as a core quality holding.**
