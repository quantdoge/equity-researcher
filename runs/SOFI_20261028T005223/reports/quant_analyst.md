# Quant Analyst

- Symbol: SOFI
- Elapsed: 37.1s

---
# SOFI — Quantitative Factor Report
**As of last close 2026-10-27: $16.40 | Mkt cap ~$20.5–21.2B | Sector: Financial Services / Credit Services**

---

## 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 42.1x, P/B 1.96x, EV/EBITDA 19.9x, P/FCF **−5.15x** | **3 of 5** (mid) | **Neutral** |
| **Momentum (12-1)** | **−6.47%** (252d ex-last-21d) | **3 of 5** | **Negative** |
| **Quality** | ROE 4.59%, GP/Assets 7.07%, Accruals **+8.34%**, F-score **4/9** | **5 of 5** (bottom) | **Strong Negative** |
| **Low Vol** | σ 54.2% (252d) / 54.9% (504d), β 2.42–2.65, MaxDD −45.5% / −55.9% | **2 of 5** (rel.); worst quintile absolute | **Negative** |
| **Earnings Revision** | Tool: +53.4% → **artifact, see note**; consensus FY25 EPS $0.366 vs $0.39 actual | **n/a** | **Neutral / mixed** |

\*Sector rank is against a hand-built comp set (AFRM, UPST, HOOD, SYF). **The `get_sector_peers` feed returned only index funds/ETFs (VSMPX, VTSAX, VTI, VOO, BRK-A) for "Financial Services" — it is unusable for credit-services cross-sectional ranking.** Ranks below are from a 5-name sample, so they are directional only, not statistically robust.

**Peer detail (the basis for the ranks):**

| Metric | SOFI | AFRM | UPST | HOOD | SYF |
|---|---|---|---|---|---|
| P/E | 42.1 | 13.1 | 52.7 | 46.1 | **8.1** |
| P/B | 1.96 | 4.62 | 3.19 | 9.49 | **1.60** |
| EV/EBITDA | 19.9 | 26.1 | 47.3 | 40.4 | **4.8** |
| ROE % | **4.6** | **35.2** | 6.7 | 20.6 | 21.2 |
| Accruals | **+8.3%** | +4.4% | +6.8% | +0.6% | **−5.3%** |
| 12-1 Mom % | −6.5 | −8.0 | −19.7 | **+17.1** | −1.9 |
| Vol % / β | 54.2 / 2.42 | 58.2 / 2.47 | 62.9 / 2.81 | 72.3 / 3.03 | **31.1 / 1.15** |

SOFI is **cheap on book (2nd cheapest of 5) but expensive on earnings**, and **dead last on every quality sub-metric**. That combination — low P/B, high P/E, weak ROE — is the classic signature of an asset-light-turned-balance-sheet lender whose book is growing faster than its returns.

**⚠️ Earnings Revision data artifact:** the tool compared FY2029 EPS ($1.577, 7 analysts) against the FY2028 estimate ($1.028, 14 analysts) and reported +53.4% "upgrade." These are different maturity buckets and different analyst counts — this is **not** a 3-month revision and should be discarded. The genuine evidence: FY25 consensus $0.3657 vs $0.39 reported (modest beat); FY26E $0.592 (+62% y/y), FY27E $0.815 (+38%); **but** the note-level drift is *downward* — Truist $19→$16 (Oct 23), Goldman $18→$15 (Oct 13), Wells $18→$17, against fresh initiations at Monness Buy $20, Scotiabank Outperform $25, Piper Overweight $22. Median PT **$18.75** (+14.3% vs spot). Net: positive multi-year estimate slope, negative near-term PT drift.

---

## 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Annualised return | n/m (negative) | **+30.54%** |
| Annualised vol | 54.22% | 54.93% |
| Beta vs SPY | **2.416** | **2.648** (R² 0.341) |
| Alpha vs SPY (ann.) | — | **−29.82%** |
| Sharpe (0% rf) | **−0.784** | **+0.554** (0.47 alt calc) |
| Sortino | — | **+0.845** |
| Max drawdown | −45.5% | **−55.85%** |

**Alpha is not statistically significant.** With R²=0.34 over 504 days, residual σ ≈ 44.7%, giving SE(α) ≈ 1.99%/day × √252 ≈ **31.6% annualised**. That puts t(α) ≈ **−0.94**. The −29.8% alpha is an estimate, not a finding; the honest statement is "no measurable alpha, directionally negative."

**The Sharpe split is the single most important number here.** +0.554 over two years vs −0.784 over the last one year means essentially all of the trailing two-year return was earned in the *first* half of the window. Actual realized path: close $30.00 on 2025-10-27 → **$16.40 now = −45.3% trailing 12-month total return**, vs a 52-week high close of $32.21 (2025-11-12) — currently **−49.1% off the high**, **−56.8% peak-to-trough** (intraday $32.73 → $13.92 on 2026-10-14). It sits **+17.8% off the low** after a **+13.4% single-session move on 160.4M shares (~4× the 30-day average)**.

---

## 3. Composite Quant Signal: **NEUTRAL (negative-leaning)**

Nothing here clears a long-only quant screen, but nothing forces a short either. The scores are genuinely split: **value is mid-pack, momentum is only mildly negative, and the 12-1 figure understates the damage** because the last 21 days are excluded by construction — precisely the window containing the drawdown to $13.92 and the +13% snapback.

Weighting quality and momentum most heavily (the two factors with the most reliable cross-sectional premia in a 5-name sample): **F-score 4/9, ROE 4.6%, accruals 8.3%, 39% diluted-share growth since 2022, and a −45% 12-month return** point to **Sell**. Weighting book valuation and the +62%/+38% forward EPS slope points to **Neutral**. I resolve to **Neutral with a Sell lean** — the stock is a high-beta rate/credit-sentiment instrument, not a factor-compounder. Any Buy case must rest on forward estimates the trailing quality data does not yet corroborate.

**Fundamental cross-check:** revenue $4.77B FY25 (+28.8%, decelerating from +64% in '23 and +27.8% in '24) — yet **net income fell to $481M from $499M** as SG&A rose 28.9% and interest expense hit $1.16B. Operating cash flow **−$3.74B**. Net margin 10.1%. On FY26E EPS of $0.592 the forward P/E is **27.7x**; FY27E $0.815 → **20.1x**. That is a defensible multiple *if* the estimate slope holds — and that is the entire bet.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / event gap risk (elevated).** +13.4% on 4× volume on the final session is unattested by any fundamental flow-through in the quality data. SOFI's realized vol means ±5% daily moves are routine; a single-day reversal of this magnitude on clustered positioning is the highest-probability near-term loss mode.
2. **Factor crowding — this is a single bet, not a diversifier.** SOFI correlates **0.72 with UPST, 0.69 with HOOD, 0.66 with AFRM**, but only **0.58 with SPY** and **0.46 with SYF**. Owning SOFI alongside other high-beta fintech is ~0.7 duplicate exposure. It is *not* a substitute for consumer-credit beta (SYF, 0.46) despite both being "consumer lending."
3. **Earnings quality (most serious).** Accruals ratio **+8.34%, flagged "warning"** and deteriorating from +4.46% in 2024; OCF −$3.74B; F-score components F2 (op CF), F3 (ROA trend), F4 (accruals), F7 (dilution) all fail. For a lender, some negative OCF is origination-driven and mechanistic — but the *trend* is the wrong direction.
4. **Structural dilution.** Diluted shares 1,251.8M vs 1,101.4M (+13.7% y/y) and 900.9M in 2022 (**+39%**). Per-share value creation is materially below headline net income growth.
5. **Tail risk worst-in-class on drawdown.** −55.9% max DD and β 2.65 put SOFI in the highest-vol cohort; only HOOD and UPST are riskier. Position sizing must reflect that a 50%+ drawdown is a demonstrated, not hypothetical, outcome.
6. **Model/data gaps (honest limitations).** (a) Sector-peer endpoint unusable (returned ETFs), so ranks rest on **n=4 comps** — treat as ordinal color, not quintiles. (b) Earnings-revision score is a **maturity-mismatched artifact** and was excluded. (c) Alpha t-stat ≈ −0.94, **not significant**. (d) P/FCF (−5.15x) and EV/EBITDA are distorted by loan-origination flows and are not decision-grade for a balance-sheet lender — P/B and P/E are the only usable multiples here.

**Bottom line:** Value neutral, Momentum negative, Quality bottom-decile, Low-Vol failing, Revisions mixed. **Neutral / Sell-lean.** Re-underwrite only on evidence that (i) accruals normalize below 5%, (ii) ROE crosses ~10%, and (iii) the 12-1 momentum spread turns positive — none of which is present in the current data.
