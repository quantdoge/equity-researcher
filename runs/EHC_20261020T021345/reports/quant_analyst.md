# Quant Analyst

- Symbol: EHC
- Elapsed: 72.0s

---
## EHC — Encompass Health Corp. | Quantitative Factor Report
**Sector:** Healthcare / Medical – Care Facilities (post-acute inpatient rehab + home health & hospice) · **Price:** $121.71 · **Mkt Cap:** $12.0B · **EV:** ~$15.0B · **Net debt/EBITDA ≈ 1.7x**

> **Peer-set note:** The FMP "sector" peer list returns mega-cap pharma (LLY, JNJ, ABBV, MRK…), which is economically useless for a post-acute operator. All ranks below use a hand-built industry comp set: **UHS, THC, ACHC, ENSG, SEM, CHE**. That set has **n = 5–6** — far too small for quintile inference. Treat ranks as ordinal colour, not statistical rank.

---

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 21.97 · EV/EBITDA 10.69 · P/FCF 28.32 · P/B 3.80 · Div yld 0.64% | **4 / 5** (beat only ENSG) | **Negative** — trades at 10.7x EV/EBITDA vs UHS 6.2x, THC 7.7x; P/FCF 28.3 vs THC 9.6, UHS 13.8. ~40–70% premium to facility peers. |
| **Momentum (12-1)** | +8.06% | **3 / 7** | **Mild positive** — behind THC +31.0%, UHS +13.9%; ahead of SEM +1.7%, ENSG +0.9%, CHE −0.3%, ACHC −15.6%. |
| **Quality** | ROE 17.28% · ROIC 17.58% · GP/Assets 0.362 · Accruals −0.086 | **2 / 6** | **Strong positive** — only UHS (ROIC tier, GP/A 0.98) clearly better. Negative accruals = cash earnings exceed reported NI every year 2022–25. |
| **Low Vol** | σ 31.2% (1y) / 27.4% (2y) · β 0.005 (1y), 0.137 (2y) · MaxDD −15.5% (1y) | **3 / 6** | **Neutral** — mid-pack σ vs SEM 18.3%, ENSG 30.0%, UHS 33.6%, THC 44.8%, ACHC 66.5%. |
| **Earnings Revision** | +9.72% (est. $8.44 → $9.26) | **2 / 4** | **Positive but low confidence** — THC +24.3%, ENSG +9.6%, UHS −0.3%. **See flag #2: measured on FY2030 EPS with n = 1 analyst.** |

**Supporting quality build (absolute, not ordinal):**
- **Piotroski F-Score: 9 / 9** — perfect (profitability 4/4, leverage/liquidity 3/3, efficiency 2/2). Rare; genuinely confirms the quality factor here rather than contradicting it.
- **ROIC trend: 12.98% → 13.99% → 15.54% → 17.58%** (2022→2025). Monotonic expansion of ~150bp/yr. Assuming ~8.5–9% WACC, the spread is +850bp and **widening** — this is the single best number in the file.
- **Accruals ratio −0.086 / −0.084 / −0.082 / −0.077** — consistently negative and stable. No earnings-quality deterioration. Note the negative sign is partly structural (heavy D&A on the hospital estate), so read it as "no red flag," not "aggressive conservatism."

---

### 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Annualised return | **+32.76%** | +5.86% |
| Annualised volatility | 31.20% | 27.40% |
| **Sharpe** | **1.05** | **0.214** |
| **Sortino** | **2.091** | **0.311** |
| **Alpha (vs SPY, ann.)** | — | **+4.32%** |
| **Beta (vs SPY)** | **0.005** | **0.137** |
| **R² vs SPY** | — | **0.0039** |
| Max drawdown | −15.49% | −26.09% |

**Read:** The 1-year risk-adjusted profile (Sharpe 1.05, Sortino 2.09, Sortino/Sharpe ratio 1.99 indicating fat right-tail / thin left-tail) is genuinely good. The 2-year numbers are mediocre (Sharpe 0.21) because they include a −26% drawdown. **The stock's entire 2-year performance is recent.**

**Correlation structure (252d):** ENSG 0.45, UHS 0.34, THC 0.33, ACHC 0.20, CHE 0.16. Correlations are low but note **THC–UHS pairs at 0.59** while both sit at only ~0.33 to EHC — EHC is *not* trading as a facilities-sector proxy.

---

### 3. Composite Quant Signal

# NEUTRAL (Buy lean, quality-driven)

Factor-percentile average across the five factors lands at roughly the **49th percentile** of the peer set — dead neutral. The composition is the story: **Quality is top-tercile, Value is bottom-tercile.** Quality is the most persistent of the factors, and a 9/9 F-Score with monotonically rising ROIC is not a marginal-quality signal — but paying 10.7x EV/EBITDA for a Medicare-exposed, rate-sensitive business to get it caps the upside.

**Valuation cross-check:** forward P/E on FY2026E EPS of $6.11 is **19.9x**; FY2028E $7.29 → 16.7x. EPS CAGR 2025E→2028E = **11.1%** → **PEG ≈ 1.8**. Growth does not fund the multiple. Consensus PTs ($140–155, 8 notes, mean ≈ $148.6) imply **~22% upside** — supportive, but that is sell-side, not a factor.

**Upgrade trigger:** Value factor moving to 3/5 (EV/EBITDA < ~9x, or EPS revisions confirmed on FY2026/FY2027 with n ≥ 8) would push this to Buy.
**Downgrade trigger:** A close below the −15.5% 1y drawdown level on volume, or FY2026 EPS revisions turning negative.

---

### 4. Key Quant Risk Flags

1. **Beta is unestimable — this matters for portfolio construction.** Beta prints **0.005 (1y), 0.137 (2y), 0.608 (company profile, ~5yr monthly)**. With **R² = 0.0039**, SPY explains **0.4%** of EHC's daily variance. The dispersion across windows is 120x. Practical consequence: **a SPY short does not hedge this name** — it is effectively a single-name idiosyncratic bet, and any beta-based risk budget applied here is fiction. Flagging as a probable data-quality artifact (stale daily prints) rather than a true zero-beta; the 5-year 0.608 is the more credible figure.

2. **The revision signal is statistically empty.** The +9.72% revision is computed on **FY2030** consensus EPS, where the estimate table shows **num_analysts = 1** (FY2029 also n = 1). The nearest period with real coverage (FY2026, n = 8) shows $6.11 and I have **no prior-period comparison** for it. A 5-year-forward, one-analyst estimate is not a revision signal. **This factor should be scored as unavailable, not positive** — and it moves the composite toward Neutral, not away.

3. **Severe short-term reversal risk — this is the standout quantitative finding.** 252-day total return is **+32.76%**, but 12-1 momentum (excluding the last 21 trading days) is only **+8.06%**. Backing out the residual: **(1.3276 / 1.0806) − 1 ≈ +22.9% in the most recent month.** Essentially the entire year's return arrived in ~4 weeks. Momentum factor scores that include recent days will look much stronger than the reversal-controlled +8.06%. Buying after a +23% one-month move in a low-beta, idiosyncratic name is a poor entry — the standard short-term reversal effect predicts give-back.

4. **Small-sample rank distortion.** With n = 5–6 peers, every "rank" above is one observation away from flipping. A quintile assignment requires ≥ 20 names. **No rank in this report is statistically significant**; the raw factor values are trustworthy, the ordinal ranks are directional only.

5. **Factor crowding / low diversification.** Peer correlations 0.16–0.45 mean a facilities-sector long/short book gets almost no natural offset from EHC. Combined with the near-zero market beta, EHC adds **variance with no hedge benefit**.

6. **Balance sheet & policy fat tails.** EV $15.0B vs mkt cap $12.0B → ~$2.6B net debt, ~1.7x EBITDA — moderate but material in a higher-for-longer rate regime, and the stock is duration-sensitive. Separately, revenue is overwhelmingly Medicare/IRF-PPS dependent: a single annual reimbursement rule can move earnings far more than any factor in this screen. This is a policy risk, not a factor risk, and no factor model in this file prices it.

7. **Liquidity:** $12B cap, ample. **Not a flag.**

---
**Data caveats:** Peer value metrics unavailable for SEM (nulls) and negative/meaningless for ACHC (distressed, negative equity → P/E −2.48, ROE −51.5%); ACHC excluded from value ranking, retained in quality ranking as a floor reference. All ranks computed on the 6-name industry set, not the FMP sector list.
