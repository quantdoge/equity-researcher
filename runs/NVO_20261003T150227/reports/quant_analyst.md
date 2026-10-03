# Quant Analyst

- Symbol: NVO
- Elapsed: 207.3s

---
All data gathered. The `rank_universe_by_factor` tool failed twice with contradictory schema errors (list vs string) — I'll note the sector-rank gap. Writing up now.

---

# NVO — Novo Nordisk A/S (ADR) — Quantitative Factor Analysis
*Healthcare / Drug Manufacturers – General | Market cap $165.7B | Price $37.32 | Data as of latest close*

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 1.62*, EV/EBITDA 1.72*, P/FCF 5.73* | **Unreliable — data contamination** | Neutral (low confidence) |
| **Momentum** | 12–1 mo return = **+1.5%** (trailing 1-yr total return **−39.1%**) | ~Bottom half of peer group (LLY +3.9%) | Neutral / weak |
| **Quality** | ROE **52.8%**, ROIC **39.3%**, GrossProfit/Assets **0.46**, Accruals **−0.031** | Top-tier; exceptional absolute level | **Positive (strong)** |
| **Low Vol** | Ann. vol **47.7%** vs SPY beta **0.97**, max DD **−44.9%** | Worst-in-class; highest vol in peer set | **Negative** |
| **Earnings Revision** | FY2030 EPS est. **+4.7%** (DKK 28.60 vs 27.30 prior) | Positive, but below LLY's +9.7% | Positive (modest) |

*\*Raw value metrics are contaminated: P/E 1.62 and a 9.44% dividend yield are implausible for NVO — consistent with a DKK-vs-USD / per-share basis mismatch in the data feed (LLY's same feed returns sane P/E 49.8, EV/EBITDA 33.5, P/FCF 114). Sector rank via `rank_universe_by_factor` could not be computed — the tool rejected both string and list universe formats on retry.*

**Cross-sectional context (peer set: LLY, JNJ, ABBV, MRK, UNH, NVS, AZN, TMO, AMGN, GILD):**
- **Value:** On a sanity-checked basis (trailing EPS ≈ $3.8–4.1 ⇒ P/E ≈ 9–10), NVO is cheap vs the LLY comparator and the sector — but this cannot be confirmed from the factor tool; treat as a weak/fragile value signal.
- **Quality:** ROE 52.8% is elite (peer LLY 77.8%; JNJ/ABBV/MRK 30–45% range). However, the trend is sharply down: ROE 78.5%→70.4%→52.8% and ROIC 76.8%→52.1%→39.3% over 2023–25. Gross margin, turnover, and ROA-improvement sub-scores all flipped negative (Piotroski 6/9, down from a stronger profile).
- **Correlation:** NVO has unusually low 1-yr correlation with the sector: LLY 0.17, JNJ 0.06, MRK 0.07, NVS 0.26, AZN 0.24, ABBV 0.22 — a highly idiosyncratic, story-driven tape rather than a beta story.

## 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **−47.0%** (R² = 0.07 — **noisy; mostly idiosyncratic, not a beta signal**) |
| Beta (vs SPY) | **0.98** (long-term profile beta 0.35 is from a different window/method — do not mix) |
| Sharpe ratio | **−0.82** |
| Sortino ratio | **−0.96** |
| Annualised return / vol | −39.1% / 47.7% |
| Max drawdown | **−44.9%** |

The 12–1 momentum reading (+1.5%) is **stale**: nearly the entire −39% loss landed inside the most recent 21 trading days (the window 12–1 momentum deliberately excludes) — consistent with the post-oral-semaglutide (REDEFINE) de-rating in late Nov 2025. The momentum print will roll sharply negative next month.

## 3. Composite Quant Signal: **NEUTRAL** (Sell-lean on price dynamics)

| Component | Weight direction | Reading |
|-----------|------------------|---------|
| Quality | + | Strong, but deteriorating |
| Earnings revisions | + | +4.7% upgrade (n = 4 analysts — small sample) |
| Value | +/? | Headline data unusable; sanity P/E ~9–10 attractive |
| Momentum | − | Stale positive, contradicted by tape |
| Low vol / price dynamics | − | −0.82 Sharpe, −47% alpha, 44.9% DD |

Three pillars (quality, revisions, sanity-checked valuation) are supportive; two (price dynamics, low vol) are decisively negative, and momentum is about to roll over. That is a textbook Neutral with a bearish path-dependency: no statistical case yet to fade the fundamental strength, but no edge in owning the negative-carry, high-vol profile until price stabilises.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (HIGH):** 12–1 momentum excludes the recent crash; next month's print will read strongly negative. Do not anchor on the +1.5%.
2. **Factor-crowding unwind:** NVO is the crowded obesity/GLP-1 trade; its crash moved alongside LLY even though daily return correlation is only 0.17 — crowding shows up in drawdown co-movement, not pairwise correlation. Crowded-short-adjacent positioning risk.
3. **Quality trend deterioration:** ROE −25pts and ROIC −37pts in two years; accruals are clean (−0.031) but margin/turnover improvement sub-scores are negative — the "quality" factor is drifting toward mean, not improving.
4. **Alpha/beta noise:** R² = 0.07 means systematic estimates are statistically weak (β ≈ 0.97 ± wide error band). The −47% alpha is dominated by idiosyncratic clinical/commercial news, not systematic mispricing.
5. **Data integrity flags:** Value factor inputs (P/E 1.62, div yield 9.44%) are internally inconsistent and must not be used for ranking until corrected; earnings-revision delta based on only 4 analysts (FY2030 period) — small sample, treat direction only.

**Bottom line:** Quantitively, NVO is a high-quality, cheap-ish-but-unverifiable, badly-broken-price story. The numbers favour Neutral with a bearish bias until (a) price stabilises above the recent crash base and (b) the value inputs are re-validated.
