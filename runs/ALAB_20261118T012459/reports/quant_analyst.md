# Quant Analyst

- Symbol: ALAB
- Elapsed: 43.7s

---
## ALAB — Astera Labs, Inc. | Quantitative Factor & Risk Report
**Price $216.18 (11/10/26 close; profile quote $211.60) · Mkt cap $37.0B · Semiconductors · IPO 3/20/24**

---

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank (of 5 semis) | Signal |
|---|---|---|---|
| **Value** | P/E 173.4 · EV/EBITDA 163.7 · P/FCF 134.8 | **4–5 / 5 (bottom quintile)** | **Negative** |
| **Momentum (12-1M)** | −10.2% | **4 / 5** (only AVGO −20.7% worse) | **Negative** |
| **Quality** | ROE 16.1% · GP/Assets 0.421 · Accruals −0.065 | **2 / 5 (top 40%)** | **Positive** |
| **Low Vol** | σ 103.8% · β 4.13 · MDD −62.8% | **5 / 5 (worst)** | **Strong Negative** |
| **Earnings Revision** | +24.5% (FY2030 EPS $17.33 vs $13.92) | n/a — 5 analysts only | **Weak Positive / low confidence** |

Peer set: NVDA, AVGO, AMD, MU (largest semis in sector). **n = 5 — quintile ranks are not statistically meaningful; treat as ordinal only.**

**Value detail** — cheapest-to-richest P/E: MU 9.6 → NVDA 31.7 → AVGO 71.6 → **ALAB 173.4** → AMD 190.0. EV/EBITDA: MU 7.1 → NVDA 26.0 → AVGO 49.2 → AMD 112.4 → **ALAB 163.7 (5/5)**. Mitigant: on **forward** consensus, FY26 EPS $4.34 = 49.8×, FY27 $7.16 = 30.2×, FY28 $9.13 = 23.7× — the multiple compresses fast if estimates hold.

**Quality detail** — best accruals in the peer group (−0.0654 vs NVDA +0.0839, the only peer with positive accruals), GP/Assets 0.421 is 3/5 (NVDA 0.742, MU 0.549 ahead). Piotroski F-Score **6/9 (Moderate)**; failures = F5 leverage (+), F7 dilution (share count up — post-IPO SBC), F8 gross margin improvement. ROIC 12.4% FY25 vs −12.0% FY24 and −18.4% FY23 — genuine inflection.

**Momentum detail** — the 12-1 figure masks a violent reversal: +12.8% over the 6-month window (ex-last-month) but **−36 to −37% in the last ~21 trading days** ($342 → $216). Peak-to-trough −54% on closing basis ($389.80 on 10/6 → $179.47 on 11/5); intraday low $177.61.

**Revision detail** — ⚠️ The +24.5% upgrade is measured on **FY2030**, a 5-analyst estimate four years out. **Contradicting signal:** the sell-side target path is deteriorating — Aug-5 cluster $425–500 (RBC $500, Roth/Jefferies $450, UBS $425, Needham $425) → Nov-4 cluster **$290–315** (Northland $315 upgrade, Needham "lowered" $300, UBS "lowered" $290). Latest median PT ~$300 (+39% vs spot), but the *direction* is down sharply. Consensus revenue path also decelerates: FY26 $2.03B → FY27 $3.46B (+70%) → FY28 $4.48B (+29%) → FY29 $6.61B (+47%) → FY30 $7.44B (**+12.6%**).

---

### 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Annualised vol | 103.8% | 105.0% |
| Beta vs SPY | 4.13–4.16 | 5.01 |
| Alpha (ann., OLS) | **+32.0%** | **−62.6%** |
| R² vs SPY | 0.33 | 0.46 |
| Sharpe (rf=0) | 1.12 | −0.98 |
| Sortino (rf=0) | 1.78 | −1.49 |
| Max drawdown | **−62.8%** | −62.8% |

**Correlation matrix (252d):** AMD 0.68 · AVGO 0.59 · SPY 0.57 · MU 0.56 · NVDA 0.44. Highest beta in the peer set with only 0.33 R² — ~67% of variance is idiosyncratic.

⚠️ **Data integrity flag:** the tool's "annualised return" (+113.6% at 252d, −102.4% at 126d) is a linear scaling of mean daily returns and is internally inconsistent with the price path. Reconciling against actual closes: **trailing-12M return ≈ −43%** (momentum-implied 11/25 price ≈ $381 → $216), which implies a true trailing Sharpe of roughly **−0.4**, not +1.12. The +1.12/+1.78 pair appears to be computed over the **full since-IPO history** (Mar-2024, +113% ann.), not the stated window. **Use −0.4 to −0.5 as the honest 12-month Sharpe; the +32% 252-day alpha is an artefact of fitting a period containing the 2025 melt-up.** Six-month figures (−0.98 Sharpe, −1.49 Sortino, −62.6% alpha) are directionally reliable and are the ones I weight.

---

### 3. Composite Quant Signal: **NEUTRAL** (high-risk hold; tilt Sell on risk-adjusted basis)

Scoring: Value −1, Momentum −1, Quality +1, Low Vol −2, Revisions 0 (offsetting) → **net ≈ −3 on 6 points of weight ≈ Neutral**, dragged to the lower half by the vol/beta penalty. Raw risk-adjusted expectancy is negative (6M Sharpe −0.98, Sortino −1.49); the offset is a quality-inflected franchise trading at 24× FY28 if the estimate stack survives. Nothing here justifies adding at current volatility.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — ACTIVE, not prospective.** The stock has already broken: −54% from the 10/6 peak in ~5 weeks on expanding volume (11.9M shares on 11/5 vs ~3M average). 12-1 momentum is now negative and short-term momentum is deeply negative. Classic post-parabolic de-rating signature.
2. **Beta 4.1–5.0 / vol ~104%.** A 10% SPY drawdown mechanically implies a ~40–50% drawdown here. Position sizing, not conviction, is the binding constraint. Beta *rose* from 4.13 (252d) to 5.01 (126d) — risk is increasing, not decaying.
3. **Estimate-revision divergence.** +24.5% on FY2030 EPS vs targets cut 25–30% in three months. When long-dated estimates rise while price targets fall, the market is discounting the *terminal* multiple, not the earnings. Treat the revision score as low-quality (5 analysts, 4-year horizon).
4. **Factor crowding / rate sensitivity.** R² vs SPY only 0.33 with 0.68 correlation to AMD — this is a high-multiple AI-connectivity derivative, not a diversifier. It will not hedge a semis or duration drawdown.
5. **Liquidity: adequate, not a constraint** (~$1.4B daily dollar volume), but volume spikes are *downside* spikes — a distribution pattern.
6. **Small-sample caveats:** peer ranks n=5; **no statistical significance** on the earnings-revision score (num_analysts = 5); 252-day alpha contaminated by a regime break. Piotroski 6/9 with F7 (dilution) failed — expect continued SBC-driven share growth to cap per-share compounding.
