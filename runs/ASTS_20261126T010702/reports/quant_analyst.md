# Quant Analyst

- Symbol: ASTS
- Elapsed: 37.3s

---
# AST SpaceMobile (ASTS) — Quantitative Factor Report

**Sector:** Communication Services / Telecommunications Services | **Price (profile feed):** $26.02 | **Mkt cap:** ~$6.7–10.7B (feeds disagree) | **Shares:** 255.98M

---

## ⚠️ DATA INTEGRITY FLAG — READ FIRST

Two internal price series conflict materially, and I am not going to paper over it:

| Source | Reading |
|---|---|
| Daily OHLCV feed | $21.64 (2025-01-02) → **$80.20 (2026-02-20)**, i.e. **≈ +270%**; max DD in that series ≈ −39% |
| Profile / valuation feed | price **$26.02**, market cap $6.66–10.66B |
| Analytics tools (momentum, vol, Sharpe, alpha) | 12-1 momentum **−36.9%**, annualised return **−91.7%**, max DD **82.5%** |

These cannot all be true. The analytics endpoints are mutually consistent (Sharpe −0.855 × vol 107.25% ≈ −91.7% return) but are **irreconcilable with the daily OHLCV path**, which contains no 82% drawdown and shows a large 12-month gain. My best read: the profile/valuation and the momentum-vol-Sharpe-alpha family are running on a **stale or alternate series (~$26)**, while the OHLCV pull is a later-dated series. **Every momentum, volatility, alpha/beta and Sharpe figure below should be treated as provisional until this is reconciled.** Validation against an independent tape is the single highest-value follow-up.

---

## 1. Factor Scores

| Factor | Score / Raw Value | Sector Rank (Comm. Services) | Signal |
|---|---|---|---|
| **Value** | P/E −19.4 (loss); EV/EBITDA −17.8; P/FCF −5.9; P/B 2.78; BVPS $9.35 | **Bottom quintile (5/5 worst)** | **Strong negative** — no valuation anchor; all multiples negative or asset-based only |
| **Momentum (12-1)** | −36.93% (tool) — *but OHLCV implies strongly positive* | Not measurable (conflict) | **Negative, low confidence** |
| **Quality** | ROE −14.29%; GP/Assets 0.0076; accruals −0.0539; Piotroski F **5/9** | **Bottom quintile** | **Negative** — only accruals quality is a positive |
| **Low Vol** | Vol 106.1%; β 3.31; max DD 82.5% | **Worst in peer set** (VZ 25.5%, T 30.1%, TMUS 37.1%) | **Strong negative** |
| **Earnings Revision** | +97.75% (2030 EPS $3.65 vs $1.85 prior) | Off-scale positive | **Positive but statistically void — 1 analyst** |

**Peer cross-section (telecom incumbents):**

| | P/E | EV/EBITDA | ROE | GP/Assets | Vol | β |
|---|---|---|---|---|---|---|
| **ASTS** | −19.4 | −17.8 | −14.3% | 0.008 | **106.1%** | **3.31** |
| TMUS | 17.1 | 9.7 | 18.6% | 0.192 | 37.1% | −0.27 |
| VZ | 11.7 | 7.6 | 16.2% | 0.156 | 25.5% | −0.29 |
| T | 7.6 | 5.9 | 17.1% | 0.178 | 30.1% | −0.31 |

ASTS is **last on value, quality and low-vol simultaneously** — 0/3 on the classic factor triad. Caveat: the peer set is profitable incumbents, so this is a *stage-of-life* comparison, not a like-for-like one.

## 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **−121.10%** |
| Beta | **3.327** |
| R² | **0.2503** → 75% of variance is idiosyncratic |
| Annualised vol | 107.25% (106.11% in vol tool) |
| Annualised return | −91.68% *(conflicted — see flag)* |
| **Sharpe** | **−0.855** |
| **Sortino** | **−1.522** |
| Max drawdown | 82.52% |

Sortino materially worse than Sharpe (−1.52 vs −0.86) → the return distribution is **downside-skewed**; volatility is disproportionately to the left. Beta 3.33 with R² of only 0.25 means ASTS is not a market beta play but a levered idiosyncratic bet with a directional market overlay.

## 3. Composite Quant Signal: **SELL**

The factor stack is uniformly adverse: bottom-quintile value, bottom-quintile quality, worst-in-sector volatility, negative tool-derived momentum, alpha of −121%. The two offsets are real but not yet quantifiable: (a) **revenue inflection** — $0 (2023) → $4.4M (2024) → **$70.9M (2025, +1,505% YoY)**, gross margin turning to 53.4%; (b) **revision direction positive**, accruals improving (−18.2% → −5.4%). I cannot upgrade to Buy on a commercial inflection that is not yet in the EPS line: consensus remains **−$1.36 in 2027** and near-zero in 2028, with profitability only arriving 2029–2030 on **1 analyst**. The entire valuation rests on 2030 numbers — 97.75% "revision momentum" is a single-estimator artifact, not a signal.

## 4. Key Quant Risk Flags

1. **Data integrity failure (severity: high).** Price/cap/momentum feeds conflict by an order of magnitude in return terms. Do not trade the momentum or Sharpe numbers before reconciliation.
2. **Momentum reversal / crowded long risk.** 3.31 beta, 106% vol, 82.5% max DD — if the −36.9% print is the true series, this is a broken momentum name in the most crowded retail-satellite theme; if OHLCV is true, it is a +270% crowded long facing violent give-back (already −38% off the Jan-2026 $129.89 peak in that series).
3. **Dilution risk, confirmed in the data.** Shares 154.5M → 256.0M (+66% in one year). Piotroski F7 = 0. Book equity growth is being financed by issuance, not earnings.
4. **No liquidity screen passed.** Dollar volume is adequate (~$0.5–3B/day in the OHLCV series) *but* this is a pre-profit capital-intensive build-out; F-score F2 (positive operating CF) = 0, OCF −$71.5M, net income −$341.9M.
5. **Factor crowding.** Zero overlap with value/quality/low-vol mandates — ASTS is un-ownable for ~80% of institutional factor-screened capital, which cuts both ways (thin marginal buyer, high short-interest sensitivity).

---
**Bottom line:** On the numbers as delivered, ASTS scores **bottom quintile on all three classical factors**, carries **β 3.33 with an R² of just 0.25**, and a **Sharpe of −0.86 / Sortino of −1.52**. The single "positive" factor (earnings revision) rests on **one analyst's 2030 estimate** and is not statistically meaningful. Signal: **SELL** — with the explicit proviso that the price-series conflict must be resolved before any position sizing.
