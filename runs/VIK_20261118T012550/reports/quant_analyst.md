# Quant Analyst

- Symbol: VIK
- Elapsed: 49.1s

---
## VIK — Viking Holdings Ltd | Quantitative Factor Report
**Sector:** Consumer Cyclical / Travel Services (cruise & river) · **Price:** $94.28 · **Mkt cap:** $42.1B · **IPO:** May 2024
**Peer set:** RCL, CCL, NCLH (cruise comparables — the sector tool returns mega-cap retail/auto, which is not a valid cross-section for this name)

### ⚠️ Data integrity flag (read first)
The OHLC feed I pulled ends **2026-02-20 at $78.80**, while the valuation snapshot is **$94.28**; external quotes show ~$88 in Nov 2026. The risk/return module clearly uses a window running to ~Nov 2026 (implied 12-mo drawdown −27.8% cannot be produced from the series I have). Because of this gap, **the momentum module output (−15.95%) is internally inconsistent with the Sharpe module (+35.99% annualised return) and with verifiable OHLC**. I report both and weight momentum lightly.

### 1. Factor Scores Table

| Factor | Score | Sector Rank (of 4 cruise peers) | Signal |
|---|---|---|---|
| **Value** | **1.0 / 5** | **4th** — PE 36.7x (4/4), EV/EBITDA 24.3x (4/4), P/FCF 27.5x (2/4) | **Expensive / Negative** |
| **Momentum** | 2.0 / 5 ⚠️ | 4th per tool (−15.95%) — **conflicts with OHLC** | **Unreliable** |
| **Quality** | **4.5 / 5** | **1st** — GP/assets 0.207 (1/4), accruals −0.116 (1/4), ROIC 21.9% | **Positive** |
| **Low Vol** | 2.0 / 5 | **1st of 4** (vol 42.1% vs 44.3/49.7/55.0) but 1.60 beta absolute | **Neutral (relative only)** |
| **Earnings Revision** | 3.5 / 5 | **2nd** (+14.4% vs RCL +18.6, CCL +2.8, NCLH −16.6) | **Mildly positive** |

**Raw factor detail**

| Metric | VIK | RCL | CCL | NCLH |
|---|---|---|---|---|
| P/E | 36.7 | 19.7 | 13.9 | 19.6 |
| EV/EBITDA | 24.3 | 15.1 | 9.5 | 5.9 |
| P/FCF | 27.5 | 67.9 | 15.1 | −6.9 |
| ROE | 102.3%* | 41.7% | 22.5% | 19.2% |
| GP/Assets | 0.207 | 0.202 | 0.153 | 0.139 |
| Accruals | −0.116 | −0.053 | −0.067 | −0.074 |
| 12-mo vol | 42.1% | 44.3% | 49.7% | 55.0% |
| Beta | 1.60 | 1.54 | 2.01 | 1.75 |

*VIK ROE is a mechanical artifact of near-zero book equity (BVPS $2.51, P/B 37.6x). **Use ROIC 21.9%** (up from 20.1% in 2024) — that is the honest quality measure.
Note: the tool tags quality "low" for all four cruise names because capex-heavy fleets structurally fail the GP/assets threshold. The label carries **zero cross-sectional information** here; I ranked on raw metrics instead.

**Fundamental quality corroboration:** Piotroski **F-Score 8/9** (only miss: F7 no dilution — diluted shares 431.6M → 446.4M, +3.4%). Gross margin 36.7% → 39.0%; operating margin 20.2% → 23.1%; net income $152M → $1,148M. Accruals −0.116 means cash earnings comfortably exceed accounting earnings. Revenue $5.33B → $6.50B (+21.9%).

### 2. Price Statistics (252-day)
| Metric | Value |
|---|---|
| Annualised return | **+35.99%** |
| Annualised volatility | 42.36% (vs SPY ~14%) |
| **Alpha (annualised, vs SPY)** | **+20.36%** |
| **Beta** | **1.611** (R² = 0.304) |
| **Sharpe** | **0.85** |
| **Sortino** | **1.34** (downside dev ≈ 63% of total vol → mildly positive skew) |
| **Max drawdown** | **−27.77%** (best of peer group: RCL −32.7, CCL −33.6, NCLH −43.6) |

**Statistical significance — the critical point:** with R² of only 0.304, residual (idiosyncratic) vol is ~35.3% annualised. Standard error on a 1-year alpha estimate is therefore ≈35 pts, giving **alpha t ≈ 0.6 — NOT statistically significant**. The +20% alpha is indistinguishable from noise; the market explains just 30% of VIK's variance. Beta SE ≈ 0.16, so beta 1.61 *is* significant (t ≈ 10).

**Crash-tested momentum (from OHLC I can verify):** 2025-02-19 → 2026-01-20 (12-1) **+33.0%**; trailing 12m +49.9% ($51.40 → $77.04); final 21 sessions **+15.3%**. This contradicts the −15.95% tool reading and argues the momentum signal is a stale-window artifact.

**Correlation structure:** VIK–SPY 0.55; VIK–CCL 0.67, VIK–RCL 0.63, VIK–NCLH 0.62 — versus peer-to-peer correlations of 0.74–0.82. VIK is meaningfully *less* coupled to cruise peers (river-cruise/upscale niche), which modestly reduces sector crowding but does not remove the 1.6 market beta.

### 3. Composite Quant Signal: **NEUTRAL** (composite 2.8 / 5)
Weighted (Value 25%, Momentum 25%, Quality 25%, Low-Vol 10%, Revision 15%). Quality and revisions are genuinely strong; **valuation is the binding constraint** — 24.3x EV/EBITDA is a 60–160% premium to CCL (9.5x) and RCL (15.1x). If momentum were scored on the verifiable OHLC instead of the suspect tool output, the composite rises to ~3.3 (**Neutral/Buy**). The call hinges on resolving that data conflict — a rigorous analyst does not upgrade on an unverified print.

Partial offset: the premium is growth-backed — consensus revenue CAGR 2025→28 ≈16%, EPS $2.57 (2025) → $3.20 (2026E) → $4.30 (2027E) → $5.28 (2028E), i.e. forward P/E 29.5x (2026) and 21.9x (2027), PEG ≈1.2 falling to 0.6. Bookings support: 96% of 2026 capacity sold, 53% of 2027 sold against +15% capacity growth.

### 4. Key Quant Risk Flags
1. **Valuation/factor crowding (high):** top-quartile multiple in a low-multiple industry. P/B 37.6x on $2.51 BVPS means **no book-value floor** — multiple compression, not fundamentals, is the dominant downside vector.
2. **Alpha insignificance (high):** R² 0.304, alpha t ≈0.6. Do not attribute the +36% return to skill/quality; it is largely high-beta + idiosyncratic.
3. **Beta/vol (high):** beta 1.61, 42% vol ≈3x market. A −28% drawdown already occurred inside 12 months. This is a high-conviction-sizing problem, not a core holding.
4. **Momentum reversal (medium):** +15.3% in the final 21 sessions of my sample is exactly the short-term reversal setup the 12-1 convention is designed to strip out.
5. **Revision-signal low power (medium):** the +14.4% revision is measured on the **2030** period with only **4 analysts** — the thinnest, noisiest cell. Nearer years (2026/27) carry 11 analysts but no revision history is available. Treat as weak evidence.
6. **CapEx/FCF (medium):** OCF $2.56B but FCF ~$1.53B — fleet growth absorbs ~40% of operating cash. FCF yield 3.6%, P/FCF 27.5x; free cash is not the reason to own it.
7. **ROE distortion (medium):** 102% ROE and 37.6x P/B both stem from a decimated equity base. Any quality screen keyed on ROE will rank VIK first for the wrong reason.
8. **Sample size (high):** IPO May 2024 → ~1.9 years of history. All 252-day statistics are a **single regime, one observation of a 12-month return**; Sharpe/Sortino/alpha are descriptive, not inferential. No dividend (yield null).
9. **Estimates are extrapolative:** 2030 EPS of $7.78 implies ~3x current earnings and is a 4-analyst projection — the revision score partly measures distant-model drift rather than near-term analyst conviction.

**Bottom line:** Quality (F-score 8, ROIC 21.9%, best-in-class accruals) and best drawdown control in the peer group are real. But value scores dead last in its own industry, beta is 1.6, the alpha is statistically invisible, and the momentum input cannot be trusted. **Neutral — prefer trimming into strength; re-evaluate on a confirmed near-term (2026/27) upward revision series or a multiple reset toward 18–20x EV/EBITDA.**
