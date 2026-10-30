# Quant Analyst

- Symbol: NOW
- Elapsed: 47.7s

---
# NOW (ServiceNow, Inc.) — Quantitative Factor Report

**Sector:** Technology / Software – Application | **Price:** $109.67 | **Mkt Cap:** ~$113–115B | **Report date:** 2026

> ⚠️ **Data integrity caveat up front.** The dataset's share count (1.047B diluted) is roughly 5× the actual ServiceNow share count (~207M), which forces an artificially low per-share price. All *ratio* outputs (P/E, EV/EBITDA, vol, beta, alpha) are internally consistent and usable; absolute price/market-cap figures should not be taken at face value. Several tools also disagree (Sharpe 0.12 vs 0.226; beta 0.99 profile vs 0.656 regression) — noted individually below.

---

## 1. Factor Scores Table

Peer set: 6 US software comparables (MSFT, CRM, ADBE, INTU, WDAY, SNOW) + NOW = 7 names. Cross-sectional ranks are ordinal within this hand-built software cohort — **not** the full 12-name "Technology" sector list, which is dominated by semis and is the wrong comparison group for a workflow-software vendor.

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 65.7x, EV/EBITDA 37.0x, P/FCF 25.1x, P/B 8.86x | **7 of 7 (bottom)** | 🔴 **Strongly negative** |
| **Momentum (12-1)** | **+44.3%** | **2 of 7 (~83rd pct)** | 🟢 **Positive — but see reversal flag** |
| **Quality** | ROE 13.5%, GP/A 0.395, accruals −14.2% | **4 of 7 (median)** | 🟡 **Neutral** |
| **Low Vol** | Vol 70.2%, β 0.656, MaxDD 39.1% | **6 of 7 (bottom quintile)** | 🔴 **Negative** |
| **Earnings Revision** | **+22.2%** (fwd EPS 6.94 → 8.49) | n/a (no peer data) | 🟢 **Upgrade — low confidence** |

**Value detail.** NOW is the most expensive profitable name in the cohort on both P/E and EV/EBITDA, beating only loss-making SNOW (negative multiples). Cheapest comps: ADBE (14.9x P/E, 10.8x EV/EBITDA), INTU (20.1x, 13.1x), CRM (29.6x, 17.4x). NOW's P/FCF of 25.1x is actually mid-pack — FCF conversion is the one place the multiple is defensible.

**Momentum detail.** +44.3% ranks 2nd behind CRM (+45.5%), ahead of WDAY (+41.0%), MSFT (+31.6%), SNOW (+27.7%), ADBE (+10.5%), INTU (−0.6%). Strong on paper.

**Quality detail.** Cleanest accruals in the peer set (−0.142; every name has negative accruals, i.e., cash earnings exceed reported earnings — a genuine positive). But ROE of 13.5% is mid-pack and has *declined* from 22.7% (2023) → 14.8% (2024) → 13.5% (2025). Piotroski F-Score **5/9 (Moderate)**: strong on profitability and leverage, weak on gross-margin improvement, asset-turnover improvement, and share-count discipline.

**Revision detail — discount this materially.** The +22.2% revision is measured on the **FY2030** consensus estimate, not a rolling 12-month forward period. A five-year-out estimate carries almost no information content for near-term revision momentum. Recent sell-side targets are in fact *mixed*: of 8 notes dated the same session, 4 raised (incl. Baird +$60 to $185, Jefferies +$5, UBS to $140) and 3 lowered (RBC $176→$165, Barclays $160→$152, Mizuho $165). **Treat revision signal as Neutral-positive, not Upgrade.**

---

## 2. Price Statistics (252 trading days)

| Metric | Value | Assessment |
|---|---|---|
| Annualised return | **+15.89%** | Below what 70% vol demands |
| Annualised volatility | **70.2–70.3%** | Extreme for a $113B software co. |
| Beta vs SPY | **0.656** | Regression; profile says 0.99 — conflict |
| **Alpha (annualised)** | **−2.65%** | Negative, and see R² below |
| **R² vs SPY** | **0.0147** | ⚠️ **Only 1.5% of variance explained — alpha is statistically meaningless** |
| Sharpe ratio | **0.226** | Poor (0.12 via low-vol tool — methodology diff) |
| Sortino ratio | **0.279** | Poor; downside vol nearly equals total vol |
| **Max drawdown** | **−39.12%** | Severe |
| Correlation vs SPY | **0.121** | Near-uncorrelated with the market |
| Corr vs WDAY / CRM / SNOW / MSFT | 0.71 / 0.76 / 0.53 / 0.48 | Trades as an idiosyncratic software name |

**The alpha is not real.** With R² = 0.015 and beta of 0.656, the −2.65% alpha has a standard error far larger than the point estimate. The correct read is: **NOW has essentially zero market beta and its returns are driven by stock-specific events, not the index.** The honest conclusion is "no measurable market alpha," not "negative alpha." Sample of 252 daily observations is adequate in length but the model simply does not fit — this is a low-correlation asset, not a mispriced one.

**Sharpe/Sortino below 0.3 is disqualifying on a risk-adjusted basis.** A 16% return against 70% vol and a 39% drawdown is a poor risk budget. Sortino (0.279) barely exceeds Sharpe (0.226), meaning there is virtually no asymmetry — downside deviation ≈ 0.71 × total vol, i.e., losses are almost as frequent/large as gains.

---

## 3. Composite Quant Signal

### ➡️ **NEUTRAL**

Weighted composite: Value 25% (bottom decile, heavily negative) + Momentum 25% (top quintile, positive) + Quality 20% (median) + Low Vol 10% (bottom quintile) + Revisions 20% (nominal positive, discounted to neutral).

Factor scores largely cancel: **the cheapest thing about NOW is nothing; the strongest thing about NOW is a momentum print that the price path says is already reversing.** This is a classic "expensive quality-ish momentum name" — a profile that historically underperforms once the momentum leg breaks. It is not a short (revenue still compounding ~22% CAGR: $7.25B → $13.28B, 2022–2025), but it does not clear a quant bar for new capital.

---

## 4. Key Quant Risk Flags

1. 🔴 **MOMENTUM REVERSAL — highest-priority flag.** The 12-1 print of +44% badly misrepresents what actually happened recently. Trailing 60-day path: **$103 → $89.81 (Apr 9) → $84.78 → recovery to $139.20 (Jun 1) → collapse back to $89.52 (Jun 25) → $99.28 (Jun 30) → $109.67 now.** A ~55% round-trip in eight weeks ending in a lower high is textbook blow-off-top and distribution. The 12-1 window deliberately excludes only the last 21 days; it is still contaminated by this episode. **Momentum factor exposure here is a liability, not a signal.**

2. 🔴 **Volatility anomaly / possible data error.** 70% annualised vol for a mega-cap application-software company is roughly 2× what its peer group (35–59%) exhibits, and its 0.656 regression beta contradicts its 0.99 profile beta. Either NOW is undergoing an idiosyncratic de-rating (event-driven: the April gap and the late-May spike both look like news shocks), or the vol feed is distorted. **I cannot fully separate the two with this dataset.** Position sizing off a 70% vol assumption is conservative-safe; sizing off the 0.66 beta is not.

3. 🟠 **Factor crowding in software momentum.** NOW correlates 0.76 with CRM, 0.71 with WDAY, 0.69 CRM↔WDAY. This is one crowded trade — enterprise SaaS on an AI-workflow narrative. A factor unwind hits all three simultaneously; NOW's low market beta offers no diversification because the risk is sector-factor, not market-factor.

4. 🟠 **Valuation leaves no margin for error.** 37x EV/EBITDA and 66x P/E against a company whose ROE is *falling* (22.7% → 13.5% over two years) and whose Piotroski deteriorated on margin and turnover. Multiple compression of even 20% is a 20%+ drawdown with zero fundamental change.

5. 🟡 **Earnings-quality flag is favourable, contrary to peer pattern.** Accruals of −14.2% means operating cash flow ($5.44B) exceeds net income ($1.75B) by 3.1×. Combined with 36/37 F-score points on profitability and cash flow, the earnings are real. **This is the single best quantitative support for the name** — it argues against accounting deterioration, not against valuation.

6. 🟡 **Weak revision signal quality.** Only the FY2030 estimate is available; near-term revision momentum could not be computed (analyst-estimates endpoint unavailable on the current data plan). Splits of 4 raised / 3 lowered in one session suggest flat-to-slightly-negative near-term revisions. **Confidence: low.**

7. 🟡 **Share-count/liquidity checks pass.** Average volume 15–85M shares daily; no liquidity constraint. Dilution is modest (1.017B → 1.047B weighted shares, +1.6% over three years) though the F-score penalises it.

---

## Bottom Line

Statistically, NOW presents as a **high-volatility, near-zero-beta, expensive, sector-crowded growth stock** whose only genuine factor positives are (a) a nominal momentum score contaminated by a violent round-trip and (b) unusually clean cash-based earnings quality. Sharpe 0.226 / Sortino 0.279 are bottom-tier risk-adjusted returns. **Composite: NEUTRAL, with a skew to Sell on any further momentum deterioration.** The alpha estimate (−2.65%) is not statistically distinguishable from zero at R² = 0.015, and should be reported as "no measurable alpha," not as underperformance.

*Sample notes: 252 daily observations; peer cross-section n=6 (ranks are ordinal and unstable at this size); revision score based on a single 2030-dated estimate pair — treat with low confidence. Absolute price/market-cap figures unusable due to a ~5× share-count discrepancy in the feed.*
