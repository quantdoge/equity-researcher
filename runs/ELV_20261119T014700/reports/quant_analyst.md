# Quant Analyst

- Symbol: ELV
- Elapsed: 46.2s

---
## ELV — Elevance Health Inc. | Quantitative Factor Report

**Data vintage note (important):** the live price is **$400.84**; the analyst price-target feed runs through **Oct–Nov 2026**, so the "current" date is ~1 year past the FY2025 (`2025-12-31`) statements that feed the trailing multiples. Every trailing multiple below is therefore ~1 year stale — I report forward-adjusted figures where I can. Peer ranks are computed against a **hand-built health-plan comp set** (UNH, CI, CVS, HUM), because the sector screener returns a Healthcare universe that is ~90% pharma and is not a meaningful comparable.

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **7 / 10** | **2 / 5** | Attractive. P/E 15.96, P/B 2.02, EV/EBITDA 11.66, div yld 1.72%. Cheaper than UNH (26.5x / 16.0x) and HUM (39.2x / 19.0x); behind CI (12.9x / 8.5x). Fwd P/E **13.2x** on FY27E $30.25. **Blemish: P/FCF 28.0** → FCF yield only 3.6% |
| **Quality** | **5 / 10** | **1 / 5** (GP/assets) / **2 / 5** composite | Mixed and **decaying**. ROE 12.86%, ROIC 10.5% — but ROE 16.22%→12.86% and ROIC 13.6%→10.5% over 4 yrs. GP/assets **0.419 = best in group**. Accruals +0.011 (only positive in group). Piotroski **F=6**, with 0/1 on ROA improvement, accruals quality, gross-margin trend |
| **Momentum** | **6 / 10** | **3 / 5** | Positive but decelerating. 12-1m **+11.69%** (6m +5.23%). Behind HUM +14.1%, CI +11.8%; ahead of UNH +4.3%, CVS −0.0% |
| **Low Vol** | **3 / 10** | **4 / 5** | Poor. Ann. vol **33.7% (252d) / 37.5% (504d)** — high absolute risk. Low beta is not a real hedging property here (see flag #1) |
| **Earnings Revision** | **6 / 10** (low confidence) | **1 / 5** | Tool output **invalid — see flag #2.** Genuine evidence: 10/10 recent targets *raised*, median **$492.50** (+22.9% vs $400.84), Argus upgrade to Buy ($510). Offsetting: FY2026E EPS $29.05 < FY2025E $29.99 = **−3.1% near-term** |

### 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Annualised return | 28.66% | 11.87% |
| Annualised vol | 34.01% | 37.53% |
| **Sharpe** | **0.843** (0.021 alt-calc) | **0.316** |
| **Sortino** | **1.176** | **0.363** |
| Max drawdown | −19.37% | — |
| Beta vs SPY | 0.165 | 0.251 |
| Alpha (ann.) | +32.96% | +8.97% |
| R² | **0.0049** | **0.0076** |

**Do not use the alpha/beta/R² block.** See flags. Economically defensible beta = **0.711** (vendor 5-yr monthly).

### 3. Composite Quant Signal: **NEUTRAL (5.6 / 10)**

Weights 25/25/20/15/15 → Value 1.75 + Quality 1.25 + Momentum 1.20 + LowVol 0.45 + Revision 0.90. Cheap and re-rating with sell-side support, but the quality factor is deteriorating and price risk is high. Not a factor-model long; a valuation-only long.

### 4. Key Quant Risk Flags

1. **Beta/alpha regression is unusable.** R² of 0.005–0.008 means SPY explains <1% of ELV variance — impossible for a healthcare payer. Beta 0.165 is a data/alignment artifact; the +33% "alpha" is that artifact's mirror image (it is just ELV's own return). **Discard both.** Use β≈0.71.
2. **The earnings-revision score is not a revision.** The tool compared **FY2030E ($46.39, n=1 analyst)** against **FY2029E ($39.97, n=1)** — adjacent-year growth, not same-period revision, on a single analyst. Zero statistical significance. Real near-term revisions skew **negative** (−3.1% for FY26E).
3. **Fundamental/ROIC decay.** Four straight years of ROE and ROIC compression (16.2%→12.9%; 13.6%→10.5%) with F-score sub-scores failing on ROA improvement and gross-margin trend. Quality is the factor working *against* the value thesis.
4. **Cash-conversion deterioration.** OCF $8.40B (2022) → $8.06B → $5.81B → **$4.29B (2025)** while net income held ~$5.7–6.0B. Accruals ratio flipped from −0.024 to **+0.011**. P/FCF 28 vs P/E 16 is the tell.
5. **Momentum is event-driven, not trend.** Peak $539.81 (Sep-2024) → trough $267.84 (Aug-2025) = **−50%**; single-day **−25%** on 2025-07-17 at 7.4M shares (~4x normal volume). 33–38% vol is idiosyncratic policy/medical-cost risk, so momentum-reversal risk is elevated and the 19.4% 252-day drawdown materially understates true tail.
6. **Window instability.** Sharpe 0.84 (1y) vs 0.32 (2y); Sortino 1.18 vs 0.36. The 1-year figures are flattered by the recovery off the July-2025 crash low — quote the 2-year number in any risk-adjusted comparison.
7. **Stale trailing multiples.** FY2025 statements against a ~late-2026 price; rely on forward P/E ~13.2x (FY27E) rather than 15.96x.

**Gaps:** no same-period revision history available (could not compute true revision momentum); no 5-year price series pulled, so full-cycle drawdown/beta unverified; sector rank n=5 (small cross-section, ranks are indicative only).
