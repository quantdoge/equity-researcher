# Quant Analyst

- Symbol: ADSK
- Elapsed: 82.7s

---
# ADSK — Quantitative Factor Report

**Price basis:** last close in feed **$231.22** (2026-02-13); valuation tool's reference price **$239.90** (FY end 2026-01-31). Market cap **$51.6B**, EV **$51.7B**, diluted shares 215M, net cash ~$1.4B. No dividend.

---

## 1. Factor Scores

| Factor | Score (0–10) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | 3.5 | 3 of 4 | **Unattractive on headline, mixed on cash** |
| **Momentum** | 2.0 | 4 of 4 | **Bearish — laggard** |
| **Quality** | 9.0 | 1 of 4 | **Strongly positive** |
| **Low Vol** | 5.0 | 2 of 4 | **Neutral (low beta, high realized vol)** |
| **Earnings Revision** | 5.0 | n/a | **Indeterminate — tool output invalid (see §5)** |

\*Rank within an explicit 4-name software-application cohort (ADSK, MSFT, CRM, NOW), built because ADSK's raw sector peer list returns mega-cap semis (NVDA, TSM, AVGO, MU) that are not valid comparables. n = 4 is **too small for statistically meaningful quintiles** — treat ranks as directional only.

**Value — raw inputs**

| Metric | ADSK | MSFT | CRM | NOW |
|---|---|---|---|---|
| P/E (GAAP) | 45.9 | 29.5 | 30.9 | 85.0 |
| EV/EBITDA | 27.1 | 19.3 | 18.1 | 48.3 |
| P/FCF | 21.4 | 58.9 | 16.0 | 32.5 |

ADSK is mid-pack: 3rd cheapest of 4 on P/E and EV/EBITDA, but 2nd best (21.4x) on P/FCF. The GAAP P/E of 45.9x sits against ~$10.24 of FY2026 non-GAAP EPS, implying ~22.6x adjusted trailing and **~18.4x FY2027E ($12.59) / 16.3x FY2028E ($14.17)** — i.e. the headline multiple is a GAAP-vs-adjusted artifact, not evidence of extreme expensiveness.

**Quality — raw inputs (this is the standout)**

- Piotroski **F-Score = 8/9** ("Strong"): all 4 profitability and all 3 leverage/liquidity tests pass; asset-turnover and gross-margin improvement both positive.
- **ROE 36.9%**, ROA 9.0%, **ROIC 27.3%** — ROIC stable/rising across four years: 25.9% (FY23) → 25.2% → 26.4% → **27.3% (FY26)**.
- **Gross profit/assets 0.534** — highest of the four (NOW 0.395, MSFT 0.297, CRM 0.287).
- **Accruals ratio −0.107** — strongly negative, i.e. cash earnings far exceed accounting earnings. Best-in-class earnings quality (only NOW's −0.142 is better).
- Only non-passing F-test: FY26 ROA did not improve (9.02% vs 10.26%).

Caveat: ROE is flattered by a thin equity base (BVPS $14.16 → **P/B 16.9x**); ROIC is the more honest profitability read, and 27% is genuinely high.

---

## 2. Price Statistics

| Metric | Value | Interpretation |
|---|---|---|
| **Alpha (ann., 504d, vs SPY)** | **−16.91%** | Large, economically material underperformance |
| **Beta (504d vs SPY)** | **0.562** | R² = **0.038** |
| Beta (252d vs SPY) | 0.426 | Window-unstable |
| **Sharpe (504d)** | **−0.214** | Negative risk-adjusted return |
| **Sortino (504d)** | **−0.302** | Worse than Sharpe → downside vol dominates |
| Annualized return (504d) | **−7.66%** | 2-yr cumulative ≈ −12% vs a rising market |
| Annualized vol (504d) | 35.76% | High for a large-cap software name |
| Annualized vol (252d) | 42.79% | Current regime is materially hotter |
| **Max drawdown (252d)** | **−32.45%** | Close-to-close tape peak $326.79 (2025-09-08) → $223.49 (2026-02-12) = **−31.6%** ✓ corroborated |
| SPY-relative | Momentum rank 4/4 | Peers 12-1: CRM +46.7%, MSFT +28.7%, NOW +24.5%, **ADSK +4.0%** |

**Statistical notes.** (a) With R² = 0.038, only ~4% of ADSK's variance is market-explained; β's standard error ≈ 0.13 (t ≈ 4.5, so β is significant, but the *model* has almost no explanatory power). The alpha t-stat is very large (|t| ≈ 10) — the negative alpha is not noise. (b) **Beta is unstable and window-sensitive: 0.43 (1y) vs 0.56 (2y) vs 1.327 (company-profile 5y monthly).** For cost-of-capital work use ~1.1–1.3; the short-window betas understate market sensitivity and are distorted by idiosyncratic, event-driven moves. Do not treat ADSK as a defensive low-beta name on the basis of the 0.43 print.

---

## 3. Composite Quant Signal

**NEUTRAL (market-weight), score 4.9/10**

The book is a genuine two-sided trade: **top-decile quality and cash conversion** (F=8, ROIC 27%, accruals −0.11, GP/A 0.53) against **bottom-of-cohort momentum, negative 16.9% annualized alpha, negative Sharpe (−0.21) and Sortino (−0.30), and a −32% drawdown**. This is the classic "good company, bad stock" configuration — quality without a catalyst or a positive revision trend.

Constructive case: 18.4x FY27E / 16.3x FY28E adjusted EPS and 21x P/FCF is not a stretched multiple for a ~20% grower with 27% ROIC; analyst targets (median ≈ $305, **+32%** vs $231) imply the sell side still sees value.

Defensive caution: price sits ~29% below its 52-week high with no momentum mean-reversion yet observable (last 3 months: 300.8 → 231.2, −23%).

**What would move this to Buy:** a positive 12-1 momentum inflection (reclaim of the ~$270 area / 50-day trend) *combined with* upward FY27 EPS revisions. **What would move it to Sell:** deceleration in FY27 EPS estimates (currently $12.59, +23% YoY) or a break below the $216 February low.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / continued de-rating risk — HIGH.** Rank 4 of 4 on 12-1 momentum, −16.9% alpha, and a fresh 52-week low ($216.01 intraday, 2026-02-12) on 5.4M shares (≈3x normal volume). Falling price on rising volume is distribution, not accumulation.
2. **Factor crowding / event-driven distortion.** ADSK carries activist and takeover speculation (Starboard, plus a wide, contradictory PT set: **$215 Cantor to $338 Piper** for the same stock). Beta instability (0.43 vs 1.33) and the near-zero R² are symptoms of return variance being driven by deal/story flow rather than the market or software fundamentals. Judgment-based overlay risk is elevated.
3. **Data-integrity flags in the factor feeds — do not act on these blindly:**
   - *Earnings Revision = −100%, "downgrade"* is a **backend artifact**: the tool compared the **FY2031** placeholder (EPS $0.00, 5 analysts) against FY2030 ($18.08) — comparing meaningless placeholders, not a real revision. **Discard this reading.**
   - *Momentum +4.01%* is **not reproducible** from the daily tape, which gives roughly **−5% to −11%** for the 12-1 window depending on anchor date. The *rank* conclusion (worst of four peers) is robust either way; the *level* is not.
   - *252-day vol of 42.79%* likely reflects the recent high-vol regime; full-window realized vol from the tape is closer to ~30%. Both exceed software-peer median.
4. **Valuation risk is real but mis-specified.** GAAP P/E 45.9x and EV/EBITDA 27.1x screen expensive; the ratio spread between GAAP and adjusted EPS (~2x) means headline multiples can flip with one non-cash item. Anchor on P/FCF 21.4x and ROIC 27.3%.
5. **Liquidity: NOT a risk.** $51.6B cap, ~1.5–2.5M shares/day typical; no capacity constraint for institutional positions.
6. **Estimate concentration:** FY2027–FY2028 consensus rests on 21 estimates (robust), but FY2029 (10) and FY2030 (4) are thin — the long-dated growth tail implied by the $305 median target is statistically fragile.

**Bottom line:** quality is real and top-ranked; price behavior is the weakest in its cohort and statistically significant (alpha t ≈ 10) — positive alpha cannot be inferred here. **Neutral until momentum and revisions confirm.**
