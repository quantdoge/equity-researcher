# Quant Analyst

- Symbol: BTSG
- Elapsed: 23.4s

---
# BTSG — Quantitative Factor & Risk Analysis
**BrightSpring Health Services, Inc.** | Healthcare — Home/Community Pharmacy & Provider Services | Price $66.89 | Mkt Cap ~$14.7B | IPO 2024-01-26

> **Data caveat up front:** BTSG is a 2024 IPO, so all trailing windows (~252 trading days) span a short, post-listing sample. Several statistics below are statistically fragile as a result. Two tool outputs also contain artifacts I flag explicitly rather than pass through.

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 76.9 · EV/EBITDA 37.7 · P/FCF 37.3 · P/B 7.8 | n/a¹ | **Strongly negative (rich)** |
| **Momentum (12-1)** | **−13.73%** | n/a¹ | **Negative** |
| **Quality** | ROE 10.1% · ROIC 6.4% · GP/Assets 0.24 · Accruals −4.7% · **Piotroski 7/9** | n/a¹ | **Mixed (weak level, improving trend)** |
| **Low Vol** | Ann. vol **47.5%** · beta(SPY) 1.03 · max DD −23.6% | n/a¹ | **Negative (high vol)** |
| **Earnings Revision** | see §1a — genuine upgrade, tool number is artifact | n/a¹ | **Positive** |

¹ **Sector rank unavailable.** The peer endpoint returned mega-cap pharma (LLY, JNJ, ABBV, MRK, UNH…) which are *not* operating comps to a home-infusion/pharmacy-services company. Ranking BTSG against drug majors would be spurious, so I withhold it rather than mislead.

### 1a. Earnings revision — the one caveat worth reading
The tool reported **+33.4% revision, "upgrade."** That number is **invalid**: it compared the **FY2030** consensus EPS ($5.45) against the **FY2029** estimate ($4.085). Those are *different fiscal years*, not the same forward period 3 months apart — so the +33% is just the passage of time between two different years' estimates, not an analyst upgrade. Coverage is also thin (2 analysts on FY2030).

**However, real revision momentum is clearly positive** from the price-target tape:
- Deutsche Bank: $60 → **$70** (Aug 2026)
- Morgan Stanley: $71 → **$80**
- KeyBanc: $60 → **$80**
- Wells Fargo: $61 → **$78**
- Guggenheim: initiate **Buy, $81**

Five up-revisions / initiations in ~1 month, targets $70–81 vs price $66.89 → **+5% to +21% implied upside**, consensus centered ~$78 (~+17%). Direction of travel is unambiguously bullish. **Signal: Positive.**

---

## 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| Alpha (ann., vs SPY) | **+65.2%** | **Not statistically reliable** — R² = 0.081 |
| Beta (vs SPY) | 1.03 | R² 0.081 → beta ≈ noise; profile beta 1.85 differs |
| Annualised vol | 47.5% | Very high |
| Annualised return (252d) | +79.0% | Single-run driven |
| **Sharpe** | **1.65** | Strong *if* stable |
| **Sortino** | **2.01** | Strong, upside-skewed |
| Max drawdown | −23.6% | |

**Critical interpretation:** With **R² = 0.081**, only ~8% of BTSG's variance is explained by the market. That means the +65% "alpha" and the 1.03 beta are effectively **unidentified** — the standard errors on both are enormous. Do not treat this as a market-neutral 65% alpha; it is mostly idiosyncratic move on a thin sample. The Sharpe/Sortino look impressive but rest on ~1 year of post-IPO data dominated by a single leg up.

**Momentum vs return conflict:** 12-1 momentum is **−13.7%** while trailing 1yr return is **+79%**. Reconciles only if the gain front-loaded and the last ~quarter reversed hard. The target tape confirms violent recent swings (price ~$71 mid-July → ~$61 early Aug → $66.89 now). **The momentum signal is highly window-sensitive — treat as "recent reversal," not a clean 12-1 read.**

---

## 3. Composite Quant Signal

### **NEUTRAL**

**Bullish offsets:**
- Genuine, broad analyst up-revisions / new Buy initiations (targets $70–81)
- Improving fundamentals: **Piotroski 7/9** — positive ROA, positive operating CF, ROA improvement, deleveraging, negative accruals (earnings quality OK)
- ROIC grinding up 3.4% (2023) → 4.5% → 6.4% (2025); ROE flipped from −25% to +10%
- Strong trailing Sharpe (1.65) / Sortino (2.01)

**Bearish drags:**
- **Valuation is stretched** across every multiple: 77× earnings, 38× EBITDA, 37× FCF. No valuation support if growth disappoints.
- **Momentum negative** (−13.7% 12-1) and recent price action choppy.
- **High volatility** (47.5%) prices it as a high-beta-crowded name despite low measured correlation.
- Absolute profitability still modest (ROIC 6.4% < likely cost of capital; ROA 2.97%).

The improving-fundamentals + upgrade story is real, but it is **already substantially in the price** at 38× EBITDA, and the risk-adjusted stats are too sample-dependent to lean on. Net: **Neutral** — a momentum/valuation tug-of-war, not a factor-aligned Strong Buy.

---

## 4. Key Quant Risk Flags

1. **Small-sample / short-history risk (HIGH):** 2024 IPO → all vol, Sharpe, alpha, beta figures rest on ≤1yr of data. The +65% alpha and 1.03 beta are **statistically insignificant (R² 0.08)**. Do not size a position on these.
2. **Momentum reversal / window sensitivity (HIGH):** 12-1 = −13.7% but 1yr = +79% signals a sharp recent pullback-then-bounce; the signal flips depending on window. Choppy tape = poor entry timing.
3. **Factor crowding / valuation risk (MEDIUM-HIGH):** 37.7× EV/EBITDA and 77× P/E leave no cushion; a high-multiple, high-vol name is exposed to multiple compression and rate/risk-appetite shifts. Beta discrepancy (1.03 measured vs 1.85 profile) hints the true market sensitivity is understated by the short window.
4. **Estimate-data artifact (flag):** The tool's +33% revision score compares FY2030 vs FY2029 — *do not use the number*. Verified upgrade signal instead comes from the target tape.
5. **Thin analyst coverage on long-dated estimates:** FY2030 EPS from only 2 analysts; consensus fragility beyond FY2027.
6. **Liquidity/size:** ~$14.7B cap is adequate, but post-IPO lockup/float dynamics can amplify moves — consistent with the 47.5% vol.

**Bottom line:** Positive fundamental inflection and a real analyst upgrade wave, against a rich multiple and unreliable risk statistics. **Neutral** — attractive on the revision/quality-improvement axis, unattractive on value and momentum. Await a better entry or confirmation that estimates keep rising at the *near-term* (FY2026–27) periods before upgrading.
