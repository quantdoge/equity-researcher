# Quant Analyst

- Symbol: FCNCA
- Elapsed: 63.8s

---
# FCNCA — Quantitative Factor & Risk Report

**First Citizens BancShares (NASDAQ: FCNCA)** · Financial Services / Banks–Regional · Price ≈ $2,387 · Mkt cap ≈ $29.5B · P/B 1.33 · BVPS $1,798.75

> Data note: the `get_sector_peers` feed returned index funds/ETFs (Vanguard, Berkshire), not bank comparables. I substituted a curated regional-bank peer set (HBAN, RF, FITB, ZION, MTB) and ranked FCNCA within **n = 6**. Ranks are 1 = most attractive.

## 1. Factor Scores

| Factor | Score (0–100) | Sector Rank (of 6) | Signal |
|--------|---------------|--------------------|--------|
| **Value** | 20 | 5–6th (5th on P/E, 6th on P/FCF) | **Negative — richest in group.** P/E 14.4 vs peer median 12.9 (+12%); P/FCF 14.25 vs 11.1 (+28%); P/B 1.33. Only name not on a discount. |
| **Momentum (12-1)** | 45 | **1st** (best) | **Neutral — relative winner, absolute loser.** −5.09% vs peers −8.0% to −11.3%. Best in group but still negative; whole cohort de-rating. |
| **Quality** | 40 | 4th (ROE 4th, GP/A 4th, Accruals 2nd) | **Neutral / low absolute.** ROE 9.92%, ROIC 5.1%, ROA 0.96%; Piotroski F = 5/9. Accruals clean (−0.31%), but profitability compressed well below 2023 (ROE 53.9%). |
| **Low Vol** | 55 | 3rd | **Mildly positive.** Beta 0.416 (lowest in group by far — next is MTB 0.588) but vol 29.1% (highest). Low-beta profile, high-total-risk profile. |
| **Earnings Revision** | 70 | n/a (tool signal: **upgrade**) | **Positive, low confidence.** FY2028 consensus EPS $223.72 vs $205.51 3-mo prior = **+8.86%**. Caveat: far-dated period, only **4 analysts** — thin, low-power estimate. |

**Factor internals (peer cross-section):**
- Value (lower=better): P/E — ZION 11.1 < HBAN 11.4 < RF 12.6 < MTB 13.2 < **FCNCA 14.4** < FITB 15.1. P/FCF — FITB 9.4 < ZION 10.0 < HBAN 10.5 < RF 11.8 < MTB 12.3 < **FCNCA 14.25**.
- Quality (higher=better): ROE — ZION 12.5 > FITB 11.6 > RF 11.3 > **FCNCA 9.9** > MTB 9.8 > HBAN 9.1. All six score "low" on GP/A (structural for banks).
- Revisions: no peer revisions computed — no relative revision rank available (gap).

## 2. Price Statistics (504-day / ~2yr window vs SPY)

| Metric | Value | Note |
|--------|-------|------|
| Annualised return | **19.56%** | Solid absolute |
| Annualised volatility | 27.55% (252d: 29.11%) | **Highest in peer group** |
| **Beta vs SPY** | **0.644** (504d); 0.416 (252d); 0.581 (reported) | Consistently low-beta; window-sensitive |
| **Alpha (annualised)** | **+5.22%** | **Low confidence — R² = 0.081** |
| R² | **0.081** | Only 8% of variance explained → alpha not statistically robust |
| **Sharpe** | **0.71** | Decent (0% rf) |
| **Sortino** | **0.988** | Downside well-controlled vs total vol |
| Max drawdown | 19.77% (252d tool) | **Realised 2025 P-to-T ≈ −33.5%** (Nov-24 $2,334 → Apr-25 $1,552) |
| Correlation to peers | 0.54–0.65 | Lower than peer-to-peer (0.82–0.90) → idiosyncratic |

**Sharpe/Sortino read:** Sortino (0.99) > Sharpe (0.71) by a healthy margin = return distribution is skewed by a few large up-days while routine down-days are moderate — favorable asymmetry. But the +5.2% alpha rests on an R² of 0.08, so treat alpha as directional, not statistically significant.

## 3. Composite Quant Signal: **NEUTRAL**

**Rationale:** FCNCA is the **relative momentum leader** (1st of 6) with a **positive revision drift** (+8.9%), **structurally low beta** (0.42–0.64), and **acceptable risk-adjusted returns** (Sharpe 0.71 / Sortino 0.99, alpha +5.2%). Against that: it is the **most expensive name on value** (worst P/E and P/FCF in group), with **mid-pack, absolutely-low quality** (ROE < 10%, F-score 5) and a **negative absolute trend**. Strengths and weaknesses roughly offset → **Neutral / Hold**. Not a value or quality buy; not a momentum short (it leads its cohort).

## 4. Key Quant Risk Flags

1. **Momentum-reversal / trend risk.** 12-1 momentum is **−5.09% and negative**; every peer is also negative (−8% to −11%) — this is a **sector-wide de-rating**, so FCNCA's "rank 1" is relative strength inside a falling group, not an uptrend. Low beta (0.42) means it will **lag hard in a sharp risk-on/beta rally**.
2. **Valuation premium vulnerability.** P/B 1.33, P/E 14.4, P/FCF 14.25 — all at the **top of the peer range**. Any multiple compression removes the one thing driving relative performance.
3. **Alpha not statistically robust.** R² = 0.081 → +5.22% alpha has a wide standard error; **do not over-weight**. Beta estimate itself swings 0.42 → 0.64 by window — factor exposure is unstable.
4. **Liquidity / float.** Only ~12.4M diluted shares and a ~$2,387 price → **thin share volume** (many sessions < 100k shares), wide spreads, single-name concentration risk for larger positions. Dollar ADV ~$300M, but share-count float is tiny vs peers.
5. **Earnings-revision thin coverage.** The "upgrade" signal is built on the **FY2028** estimate with only **4 analysts** — low statistical power; treat as weak evidence.
6. **Factor crowding:** LOW. Peer correlations (0.54–0.65) sit well below the 0.82–0.90 peer-to-peer cluster — FCNCA offers genuine **diversification** vs other regionals, but this also means idiosyncratic (company-specific) risk dominates sector beta.

**Gaps:** No valid bank-peer data from the sector feed (substituted curated set, n=6 — small sample, ranks are indicative); no peer earnings-revision ranks; EV/EBITDA unreliable for banks (RF/MTB EBITDA negative — excluded from value logic).
