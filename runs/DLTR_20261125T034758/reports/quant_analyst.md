# Quant Analyst

- Symbol: DLTR
- Elapsed: 26.2s

---
## DLTR — Dollar Tree, Inc. | Quantitative Factor Report

**Price $154.65 · Market cap $29.0B · Consumer Defensive / Discount Stores · Beta (reported) 0.685**

Peer cohort used for cross-sectional ranking: **DG, TGT, WMT, COST** (5-name discount-retail set). *Note: ranks are within this narrow cohort, not the full 60+ name Consumer Defensive sector — treat as indicative, not a true quintile.*

### 1. Factor Scores

| Factor | Score | Peer Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 26.0 · EV/EBITDA 16.2 · P/FCF 22.8 | **3rd** | Neutral |
| **Momentum (12-1)** | **−4.55%** | **3rd of 3** | Negative |
| **Quality** | ROE 34.2% · GP/Assets 0.525 · Accruals −0.093 | **1st** | Strong Positive |
| **Low Vol** | Vol 46.4% · Beta 0.60 · MaxDD 35.5% | **5th (worst)** | Strong Negative |
| **Earnings Revision** | Forward EPS 10.07 vs 9.40 (+7.1%) | **2nd of 3** | Positive (upgrade) |

**Supporting quality detail**
- **Piotroski F-Score: 8/9 — Strong.** Sole miss is F6 (positive equity change), a mechanical consequence of the Family Dollar impairment/buyback history, not operating deterioration.
- **ROIC trend (4y): 11.12% → 12.09% → 12.38% → 14.78%** — four consecutive years of improvement. This is the cleanest quality signal in the dataset.
- **Accruals ratio: 0.00 → −0.167 → −0.316 → −0.093.** Persistently negative (cash earnings exceed reported net income) = high earnings quality. FY2026's −0.093 is less negative than FY2025 but well below the 0.05 deterioration threshold.
- **Caveat on ROE (34.2%):** this is arithmetically inflated by a heavily impaired equity base (ROE was **−76.2%** in FY2025 and −13.7% in FY2024). Use ROIC 14.8%, not ROE, as the economic quality measure. On ROIC DLTR sits mid-pack, not top.

**Value context:** DLTR is not cheap. DG is the cheapest name in the cohort on all three multiples (20.2 / 13.9 / 12.8), TGT second on EV/EBITDA (11.4). DLTR's 26.0× P/E and 16.2× EV/EBITDA sit above both, though far below WMT (48.5×) and COST (52.6×).

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **+37.09%** |
| Annualised volatility | **46.86%** |
| **Alpha (annualised)** | **+29.0%** |
| **Beta** | **0.603** |
| **R² vs SPY** | **0.043** |
| Sharpe ratio | **0.792** |
| Sortino ratio | **1.589** |
| Max drawdown | **−35.47%** |

**Critical statistical caveat on alpha:** R² of **0.043** means the market explains only 4.3% of DLTR's variance — 95.7% is idiosyncratic. With residual vol ≈ 45.8% (= 46.86% × √(1−0.043)), the standard error on a one-year annualised alpha is roughly 45.8%, giving **t ≈ 0.63**. The +29% alpha is **statistically indistinguishable from zero**. Do not underwrite the alpha; the correct read is "very high tracking error, one-year sample, no significant excess return."

**Sharpe/Sortino spread:** Sortino (1.589) is almost exactly 2× Sharpe (0.792), implying downside deviation ≈ 23.4% versus total vol 46.9%. Returns are right-skewed with contained downside for the calendar year — but this sits awkwardly beside a 35.5% max drawdown, so the favourable Sortino reflects path dependence of the specific window rather than a structural downside buffer.

### 3. Composite Quant Signal: **BUY (low conviction)**

Strengths (quality rank 1, F-score 8, ROIC improving four straight years, negative accruals, revisions +7.1%) offset by momentum −4.55% and the **worst low-vol profile in the peer cohort**. Value is neutral; there is no valuation cushion at 26× earnings. The signal is a quality-and-revisions buy, not a factor-alignment buy — DLTR does not score top-quintile on value, momentum, AND quality simultaneously.

### 4. Key Quant Risk Flags

1. **Momentum reversal / negative trend:** −4.55% 12-1 return, and last in a 3-name momentum sample. Buying quality against negative momentum is a known factor-timing hazard.
2. **Volatility & factor crowding excluded:** 46.4% annualised vol is 2.3× COST (20.2%) and highest in cohort. Beta 0.60 understates total risk dramatically — the low beta is *not* a low-risk signal here.
3. **Alpha not significant (R² 0.043):** the high alpha / high vol combination is the signature of a stock driven by company-specific catalysts (Family Dollar disposition, tariff and pricing news), not by factor exposure. Position sizing should reflect idiosyncratic, not market, risk.
4. **ROE distortion:** headline 34.2% ROE is an artifact of a depleted equity base. Any screen ranking DLTR top-decile on ROE is a false positive.
5. **Sample size:** momentum and revision ranks rest on 3 comparables; value/quality/low-vol on 5. None of these ranks carry statistical significance and should be treated as ordinal context only.
6. **Liquidity:** $29.0B market cap — no liquidity constraint; not a flag.

**Data gaps:** Full Consumer Defensive sector distribution unavailable (peer list returned mostly beverage/tobacco/household names, not discount retailers), so quintile placement is approximated from a hand-selected 5-name cohort. Peer ROIC not retrieved, so DLTR's mid-pack ROIC positioning is inferred from absolute level only.
