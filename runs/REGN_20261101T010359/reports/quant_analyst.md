# Quant Analyst

- Symbol: REGN
- Elapsed: 44.2s

---
# REGN — Regeneron Pharmaceuticals | Quantitative Factor & Price-Statistics Report

**Price:** $927.89 | **Mkt Cap:** ~$100.8B (108.6M dil. sh.) | **Sector:** Healthcare / Biotechnology | **Data as of:** 2026-10-30

---

## 1. Factor Scores

Sector rank is computed cross-sectionally against five large-cap Healthcare comparables (LLY, ABBV, MRK, AMGN, GILD) — n = 6, a deliberately small peer set, so ranks should be read as **coarse** (one notch ≈ 12.5% of the cross-section), not fine-grained.

| Factor | Raw Metrics | Score /10 | Sector Rank | Signal |
|---|---|---|---|---|
| **Value** | P/E 22.37 · EV/EBITDA 16.31 · P/B 3.22 · P/FCF 24.70 · FCF yield 4.05% · Fwd P/E (FY26) 14.4x | **8** | **2 / 6** | **Bullish** |
| **Momentum** | 12-1 return **+12.91%** · 6M (126d) **−8.98%** · 1M (21d) **+26.3%** | **5** | **1 / 6** | **Mixed — internally divergent** |
| **Quality** | ROE 14.41% · GP/Assets 0.302 · Accruals −0.0117 · ROIC 10.53% (▼ from 21.2%) · F-Score 5/9 | **4** | **5 / 6** | **Bearish** |
| **Low Vol** | Ann. vol 34.21% · Beta 0.37 · Max DD 25.01% · Sharpe 0.97 | **4** | **5 / 6** | **Bearish** (beta good, vol poor) |
| **Earnings Revision** | FY30 EPS est. 89.99 vs 82.91 (+8.54%), n=5 analysts | **6** | **3 / 6** | **Mildly bullish** |

### Factor Detail

**Value — the strongest leg.** REGN ranks #2 of 6 on *all three* multiples independently (P/E 2nd, EV/EBITDA 2nd, P/FCF 2nd), which is unusually consistent. Only MRK is cheaper on trailing multiples (P/E 20.5, EV/EBITDA 14.5). On forward numbers the picture improves materially: at $927.89 against FY2026 consensus EPS of $64.64, forward P/E is **14.4x**, falling to **13.7x** (FY27) and **12.3x** (FY28). Peer trailing P/Es: LLY 61.8, ABBV 124.4, AMGN 32.8, GILD 25.2, MRK 20.5. This is a genuine valuation discount, not a value trap on multiples alone.

**Momentum — statistically fragile, and the headline number is stale.** The 12-1 score of +12.91% (rank 1/6, ahead of MRK +11.25% and GILD +11.23%) is *entirely* an artefact of the Oct–Nov 2025 rally. The intermediate trend is the opposite: **6-month momentum is −8.98%**, i.e. the stock fell from ~$1,000-equivalent levels between Feb and Sep 2026 (close-to-close: $840.84 on 2026-08-19 → $752.25 on 2026-09-28). The 12-1 window deliberately excludes the last 21 days, so it also excludes the +26.3% October surge. **The momentum factor is lagging the price action, not leading it.**

**Quality — the weakest leg, and deteriorating on a trend basis.** Regeneron's absolute quality is fine (accruals have been negative for four straight years: −2.32%, −1.94%, −0.02%, −1.17%, i.e. earnings fully cash-backed). But the *direction* is poor and the cross-sectional rank is 5th of 6:

| Period | ROE | ROA | ROIC |
|---|---|---|---|
| 2022 | 19.14% | 14.85% | **21.23%** |
| 2023 | 15.22% | 11.95% | 15.16% |
| 2024 | 15.03% | 11.69% | 12.45% |
| 2025 | **14.41%** | **11.11%** | **10.53%** |

ROIC has **halved in three years** (21.2% → 10.5%). Piotroski F-Score of 5/9 confirms stagnation: no ROA improvement (F3=0), rising leverage (F5=0), no gross-margin improvement (F8=0), no asset-turnover improvement (F9=0). Peers rank better on ROE (AMGN 89%, LLY 78%, GILD 37.6%, MRK 34.7%) and GP/Assets (LLY 0.48, GILD 0.39, MRK 0.34).

**Earnings Revision — positive but weakly sampled.** +8.54% revision ranks 3/6, behind LLY (+10.37%) and GILD (+9.40%). **Critical caveat: this is a single-point comparison against the FY2030 estimate with n=5 analysts.** That is below any reasonable significance threshold. The near-term estimate dispersion is also wide — FY2026 EPS range is $48.01 to $73.35 against a $64.64 midpoint (±19%), which signals high model uncertainty, not conviction.

---

## 2. Price Statistics (252 trading days)

| Metric | Value |
|---|---|
| Annualised return | **+34.03%** |
| Annualised volatility | **34.48%** |
| Beta vs SPY | **0.37** (regression) / 0.368 (low-vol tool) |
| Alpha vs SPY (annualised) | **+28.20%** |
| R² vs SPY | **0.0201** |
| **Sharpe ratio** | **0.987** |
| **Sortino ratio** | **1.530** |
| Max drawdown | **−25.01%** |
| Downside deviation (derived) | ~22.2% |
| Vol / downside-dev ratio | ~1.55 (positive skew) |

**Alpha is not statistically significant — this must be stated plainly.** R² of 0.0201 means SPY explains **2.0%** of REGN's variance; 98% is idiosyncratic. The standard error on an annualised alpha estimate scales roughly as σ·√(1−R²)/√T ≈ 34.5% × 0.99 / 1.0 ≈ **34%** over a one-year window. That puts the alpha t-statistic at roughly **t ≈ 0.83** — well inside the noise band. A +28.2% alpha on a single year of data with R²=0.02 is **not distinguishable from luck**. The 34% annualised return is a raw return, not evidence of skill or mispricing.

**Sharpe 0.99 / Sortino 1.53:** the 1.55× gap between total vol and downside deviation is a genuinely favourable asymmetry — realised gains clustered more than losses. But both ratios assume normality, and REGN violates that assumption severely (see Jump Risk below). Treat the Sortino as a ceiling, not a floor.

**Low-vol factor:** beta of 0.37 looks excellent (peers: ABBV −0.17, MRK 0.07, LLY 0.15, GILD 0.25, AMGN 0.41), but *realised* volatility of 34.21% is second-worst in the peer group (ABBV 25.4%, GILD 27.1%, AMGN 29.6%, MRK 30.7%, LLY 37.0%). **This is a low-beta / high-idiosyncratic-risk profile** — market-neutral, not low-risk. Ranking 5/6 on the low-vol factor is correct.

---

## 3. Composite Quant Signal

### **BUY** (moderate conviction — not Strong Buy)

Weighting: Value 30% · Momentum 20% · Revision 20% · Quality 20% · Low-Vol 10% → composite z ≈ **+0.6σ**.

The case is a cheap asset (14.4x forward, 4.05% FCF yield, #2 of 6 on every multiple) with cash-clean earnings and positive revisions. The case for *not* upgrading to Strong Buy:

1. **Quality is deteriorating, not stable** — ROIC 21% → 10.5% is a structural trend, and the Piotroski 5/9 confirms no operational improvement.
2. **Alpha is statistically indistinguishable from zero** (t ≈ 0.83, R² = 0.02).
3. **Momentum is stale** and the position is technically extended after a one-month +26% move.

Consensus price targets (10 most recent) average ~**$869.80** vs the $927.89 spot — the stock is trading **~6.7% above the mean analyst target**, the first time that has been true all year. Targets were clustered $779–$978 while the stock was $730–$790 in mid-October; the stock has now run past most of them. Revisions to targets, not just estimates, would be required to sustain this level.

---

## 4. Key Quant Risk Flags

**🔴 FLAG 1 — Stale momentum + acute short-term reversal risk.** 12-1 momentum (+12.91%) and 6-month momentum (−8.98%) point opposite directions. The stock closed at **$927.89 on 2026-10-30, a 52-week closing high**, up **+54.7% from its June 1 low of $599.96** and **+26.3% in 21 sessions**. Buying on the 12-1 signal here means buying after the move, not before it. Mean-reversion risk on a 1–3 month horizon is elevated.

**🔴 FLAG 2 — Severe jump/gap risk invalidates normal-distribution risk metrics.** Four double-digit single-session moves in 13 months: **+12.0%** (2025-10-28), **−9.8%** (2026-05-18, with a gap-down open at $614.29 from a $696.39 prior close), **−6.2%** (2026-04-29), and **+13.3%** on 2026-10-30 (open $869.43 → close $927.89, on **2.87M shares vs ~0.6M ADV**, a 5× volume event). Realised vol of 34.21% and the 25.01% max drawdown both **understate** true tail risk. Sharpe and Sortino are unreliable inputs here; size positions to jump risk, not to σ.

**🟠 FLAG 3 — Revision score rests on n=5.** The +8.54% signal compares FY2030 consensus across 5 analysts — statistically meaningless in isolation. FY2026 dispersion (low $48.01 / high $73.35 vs $64.64 mid) implies a ±19% earnings band. Do not treat the revision signal as confirmatory.

**🟠 FLAG 4 — Quality factor crowding in the *wrong* direction.** REGN sits in the bottom-two on Quality *and* bottom-two on Low-Vol within a peer set where the top quintile is crowded (LLY, MRK, GILD all score "high" quality). A portfolio already long large-cap pharma quality is adding a diversifier on value but a *concentrator* on quality-factor exposure.

**🟡 FLAG 5 — Correlation cluster, not a hedge.** vs AMGN **0.49**, GILD **0.48**, LLY 0.39, XBI 0.38, MRK 0.36, ABBV 0.33, but only **0.14** vs SPY. REGN provides no meaningful market hedge and substantial biotech-sector beta. Effective diversification requires pairing against non-pharma exposure.

**🟡 Liquidity: not a constraint.** ~$650M average daily dollar volume; the 2026-10-30 session traded ~$2.6B. Capacity is ample.

**Data gaps:** Peer cross-section is n=6 (no small/mid-cap biotech comps); estimate history is a single snapshot rather than a time series, so the revision signal could not be verified for persistence; no explicit short-interest or borrow data was available.
