# Quant Analyst

- Symbol: AMD
- Elapsed: 76.9s

---
## AMD — Quantitative Factor & Risk Report
**Data as of 2026-11-09 | Price $508.58 | Market cap ~$832bn | Sector: Technology / Semiconductors**

> **Data integrity note (read first).** Three module outputs are internally inconsistent with raw price/fundamental data and are flagged rather than used at face value. All figures I could verify against raw closes are reported as "verified." Detail in Flag #6.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 191.9x · EV/EBITDA 113.5x · P/FCF 123.5x · P/B 13.2x · FCF yield **0.81%** | **4 of 4** semis (worst) | **Strong Sell** |
| **Momentum** | +117.8% trailing 12m (verified: $233.54→$508.58); 12-1 ≈ +166% ($235.56→$620.68) | **1 of 5** (best) | **Strong Buy** |
| **Quality** | ROE 6.9% · GP/Assets 0.223 · ROIC 5.5% · Accruals −0.044 · **Piotroski F-Score 8/9** | **4 of 5** | **Sell** (improving) |
| **Low Vol** | Vol 78.1% ann. · Beta 3.60 (12m) / 3.90 (6m) | **5 of 5** (worst) | **Strong Sell** |
| **Earnings Revision** | +28.8% EPS revision — **but on FY2030, 10 analysts only** | n/a — not comparable | Weak Buy (low confidence) |

**Peer set (Semiconductors):** MU, NVDA, AVGO, TSM. TSM excluded from value ranking — ratios corrupt (P/E 1.17x, EV/EBITDA −0.02x).

**Value detail — AMD is the most expensive name in its peer group by a wide margin:**

| | P/E | EV/EBITDA | P/FCF | ROE |
|---|---|---|---|---|
| MU | 9.9x | 7.4x | 14.2x | 61.4% |
| NVDA | 36.5x | 30.0x | 45.3x | 76.3% |
| AVGO | 67.0x | 46.1x | 57.6x | 28.5% |
| **AMD** | **191.9x** | **113.5x** | **123.5x** | **6.9%** |

**Critical nuance on the multiple:** the 191.9x is *backward-looking GAAP* (implied trailing EPS $2.65). On consensus forward estimates the de-rating is violent: FY2026E EPS $7.98 → **63.7x**; FY2027E $17.45 → **29.1x**; FY2028E $25.63 → **19.8x**. Consensus implies revenue compounding from $34.1bn (FY25) to $52.2bn (FY26) to $95.4bn (FY27, +83%) — an embedded AI-accelerator share-gain assumption, not a base case. The value factor is genuinely negative, but it is a *growth-expectation* risk, not a static-multiple risk.

**Quality detail:** bottom-of-group on both ROE (6.9% vs 28–76% peers) and Novy-Marx GP/Assets (0.223 vs 0.253–0.742). Offsetting: accruals are **negative and improving** (−0.012 → −0.020 → −0.044 across FY23–25), Piotroski F-Score **8/9** (only miss: leverage), and ROIC has climbed monotonically 0.68% → 2.19% → 3.18% → **5.47%** (FY22–25). Quality is low in *level* but the trend is unambiguously up. F-Score 8 is genuinely inconsistent with the "low quality" label and I weight the trend over the level.

---

### 2. Price Statistics

| Metric | Trailing 12m (252d) | Trailing 6m (126d) | Δ |
|---|---|---|---|
| Total return | **+117.8%** (verified geometric) | +11.7% (verified: $455.19→$508.58) | Decelerating hard |
| Alpha vs SPY | **+80.1%** ann. | **+13.7%** ann. | **−66.4pp** |
| Beta vs SPY | 3.60 | 3.90 | Rising |
| R² vs SPY | 0.445 | 0.518 | — |
| Annualised vol | 78.2% | 78.1% | Stable (extremely high) |
| Sharpe (rf=0%) | **1.92** | **0.36** | **−81%** |
| Sortino (rf=0%) | **3.22** | **0.54** | **−83%** |
| Max drawdown | **−37.73%** | −37.73% | same event |

**Notes on the above:**
- The 12m Sharpe of 1.92 uses arithmetic annualisation (mean daily × 252 = 145.7%); geometric annualisation gives ~1.51–1.60. Either way, risk-adjusted performance over 12m has been **excellent**, and over 6m merely **average**.
- Sortino/Sharpe ratio of ~1.8x means downside deviation is only modestly larger than total deviation — but with 78% vol the absolute downside is brutal: a single **−37.73% peak-to-trough decline** from the 2026-10-06 close of $649.42 to the 2026-11-05 close of $404.40. Verified against raw closes; the drawdown figure is accurate.
- **Current position: $508.58, which is −21.7% below that October peak.** The stock remains in active recovery from a completed momentum break.
- **Beta instability is the single most important statistical fact here.** Regression beta 3.60 (12m) vs 3.90 (6m) vs company-reported 2.49 — a 57% spread. With R² of only 0.445, **55% of AMD's variance is idiosyncratic**, not market. Beta-based position sizing is therefore unreliable; risk must be managed via position size on vol, not via index beta.

**Correlation structure (252d):**

| | AMD | NVDA | AVGO | MU | SPY |
|---|---|---|---|---|---|
| **AMD** | 1.00 | 0.517 | 0.610 | **0.665** | 0.664 |
| NVDA | 0.517 | 1.00 | 0.533 | 0.471 | 0.637 |

AMD's highest correlation is with **MU (0.665)** and SPY (0.664) — notably *higher* than with NVDA (0.517). AMD is trading as a high-beta memory/cyclical + index proxy, not as a clean AI-compute derivative. This is a meaningful distinction: it means AMD does not diversify an AI-semi book (AVGO 0.610, MU 0.665), and it does not hedge a broad-market book either (0.664).

---

### 3. Composite Quant Signal

## **NEUTRAL (Hold) — momentum-driven, factor profile deteriorating**

The panel is **1 strong positive, 4 negatives**. Rules-based composite: momentum (+2) + value (−2) + quality (−1) + low-vol (−2) + weak revision (+1) = **−2 / plausible range −6 to +6 → Neutral**, explicitly *not* Buy.

Two forces decide this, and they point opposite ways:
- **Bull argument is purely momentum + estimate trajectory.** Top-ranked momentum in the peer group, F-Score 8, negative accruals, ROIC on a four-year climb, and a consensus path implying 19.8x FY28 earnings. The business inflection is real.
- **Bear argument is that the alpha is already spent.** Alpha collapse from +80.1% (12m) to +13.7% (6m), Sharpe collapse from 1.92 to 0.36, and a −37.7% drawdown inside the last 13 months are the classic signature of **momentum maturity, not momentum initiation**. Buying here means paying 123x FCF for a 13.7% residual alpha.

**Position guidance:** Neutral/Hold for existing holders; do **not** initiate new full-size positions at $508.58. The distribution of outcomes is dominated by the FY27 $95.4bn revenue assumption. A quant-justified entry requires either (a) multiple compression toward ~35–40x FY27E EPS (≈$610–700 is *not* it — that's above spot on FY26, i.e. 29x FY27 is already priced near spot via the pullback), or more practically (b) renewed upward estimate revision on a *near-term* horizon, which the current data does not establish.

---

### 4. Key Quant Risk Flags

1. **Valuation is bottom-decile, 4/4 in peers.** 123.5x P/FCF = 0.81% FCF yield. Zero valuation support — the entire thesis rests on consensus estimates 2–5 years out. No margin of safety.
2. **Momentum reversal risk — HIGH.** Alpha 80.1%→13.7%, Sharpe 1.92→0.36, Sortino 3.22→0.54 over the same two windows. A stock with 78% vol that has already drawn down 37.7% is in the late innings of its momentum leg, not the early ones.
3. **Beta instability / sizing hazard.** Beta 2.49 (reported) to 3.90 (6m regression), R² 0.445. Any beta-based hedge ratio is unstable and will mis-size by up to 50%. **Size on 78% vol, not on index beta.**
4. **Factor crowding — HIGH.** Correlations 0.665 (MU), 0.610 (AVGO), 0.664 (SPY). AMD sits inside the most crowded trade in the market as a high-beta proxy; an AI-semi de-risking event hits AMD via two channels (sector beta + its own beta) simultaneously.
5. **Liquidity — NOT a concern.** ~50.7M shares/day, ~$25bn daily dollar volume (2026-11-09: 50.7M sh at $508.58). Institutional-size entry/exit is frictionless; no liquidity discount required.
6. **Data-quality flags — treat as gaps, not signals:**
   - *Momentum module returned +24.8% (252d); raw closes show +117.8%.* An ~93pp discrepancy. I report the **verified +117.8%** and disregard the module output. Direction (positive) is unaffected; magnitude is not.
   - *TSM valuation ratios corrupt* (P/E 1.17x, EV/EBITDA −0.02x, ROE 31.5%) — mathematically impossible, excluded from the value ranking. Peer value rank is based on 4 names, not 5.
   - *MU earnings revision of −100%* (current estimate went to 0.0) — clearly a data error, not a downgrade.
   - *Earnings-revision factor anchors on FY2030 (AMD, 10 analysts; NVDA FY2031).* A revision on a 5-year-forward estimate is not estimate-revision momentum — genuine ERM requires FY2026/2027 vintages. **The +28.8% AMD reading has low statistical validity** and I weight it weak-positive only. The near-term read-across from the consensus table (FY26 EPS $7.98, FY27 $17.45, FY28 $25.63 — each *above* prior vintages) is more informative than the module's own headline.
   - *Sharpe discrepancy* (1.92 from one module, 1.60 from another) is explained by arithmetic vs geometric annualisation, not error. Both reported.

**Bottom line:** statistically strong trailing momentum and a genuinely inflecting operating base, priced at the most extreme multiple in its peer group with the highest volatility and an unstable beta. The factor panel does not support a Buy. Neutral, sized on volatility, with the FY27 revenue assumption as the single variable that matters.
