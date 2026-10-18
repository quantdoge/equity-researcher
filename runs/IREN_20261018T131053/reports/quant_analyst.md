# Quant Analyst

- Symbol: IREN
- Elapsed: 38.3s

---
## IREN Limited (IREN) — Quantitative Factor & Risk Report

**Price $26.99 | Mkt cap $8.53bn | EV $10.48bn | P/B 2.04 | BVPS $13.24 | Sector: Technology (data centers / Bitcoin mining) | FY end June**

⚠️ **Data-infrastructure note:** the vendor sector-peer list returned NVDA/AAPL/MSFT — mega-cap semis/software, not valid comparables for a vertically integrated miner/HPC datacenter. I therefore built a **crypto-miner peer set (MARA, RIOT, CLSK, HUT, n=5)** for cross-sectional ranking. Ranks below are against that set, not the vendor "sector."

### 1. Factor Scores

| Factor | Score / Raw | Rank (miner set) | Signal |
|---|---|---|---|
| **Value** | P/E −12.16 · P/B 2.04 · EV/EBITDA **301.7x** · P/FCF −3.82 | 2 / 5 | **Negative** (no earnings, no FCF; 2.0x book is not cheap for a −17% ROE) |
| **Momentum** | 12−1 = **+11.9%** · 6−1 = +4.3% | 2 / 5 | **Positive but stale** (see reversal flag) |
| **Quality** | ROE −16.8% · GP/Assets 3.1% · Accruals −17.8% | 2 / 5 | **Low** |
| **Low Vol** | Vol **106.5%** · Beta **3.97** · MaxDD 60.2% | **5 / 5 (worst)** | **Strongly negative** |
| **Earnings Revision** | FY30 EPS $1.33 vs $3.41 → **−60.9%** | n/a | **Downgrade** (⚠ n=1 analyst) |
| *F-Score (Piotroski)* | **4 / 9 — Weak** | — | Negative |

**F-Score detail:** F1 ROA<0 ✗ · F2 OCF>0 ✓ · F3 ROA worse ✗ · F4 accruals ✓ · F5 leverage up ✗ · F6 equity up ✓ (issuance) · F7 **dilution ✗** · F8 gross margin up ✓ · F9 asset turnover down ✗. The two "positives" are accruals and equity issuance — one is a cash-vs-income artefact, the other is shareholder dilution.

**Peer factor comparison**

| | IREN | MARA | RIOT | CLSK | HUT |
|---|---|---|---|---|---|
| 12−1 Mom. | 11.9% | 0.2% | 10.4% | 12.3% | −7.0% |
| Vol | **106.5%** | 88.3% | 91.0% | 88.4% | 104.4% |
| Beta | 3.97 | 3.33 | 3.85 | 3.46 | 4.22 |
| MaxDD | **60.2%** | 49.3% | 52.2% | 55.3% | 49.1% |
| ROE | −16.8% | −37.7% | −23.2% | +16.8% | n/a |
| EV/EBITDA | 301.7 | −10.6 | −99.7 | 3.3 | n/a |

IREN is the **highest-volatility, deepest-drawdown name in the group**, mid-pack on momentum/quality, and second-best on book-value-based value only because peers have negative EBITDA. CLSK dominates on every fundamental factor (P/E 7.5, EV/EBITDA 3.3, ROE +16.8%) though its accruals ratio of +25.9% is a genuine red flag.

### 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **−38.8%** |
| Annualised volatility | 106.4% |
| **Sharpe** | **−0.364** |
| **Sortino** | **−0.682** |
| **Beta** | **3.99** (R² 0.242) |
| **Annualised alpha** | **−71.3%** |
| Max drawdown | 60.2% |
| Correlation vs SPY | 0.489 |
| Correlation vs CLSK / HUT / RIOT / MARA | 0.741 / 0.737 / 0.727 / 0.634 |

Negative Sharpe *and* a Sortino more negative than the Sharpe ⇒ returns are asymmetrically downside-driven. R² of only 0.24 means ~76% of variance is idiosyncratic: the −71% alpha carries a residual vol of ~93%, giving an **alpha t-stat ≈ 0.8 — NOT statistically significant**. Treat alpha as directionally negative but statistically unproven; beta ≈ 4.0 is the far more reliable estimate.

### 3. Composite Quant Signal: **SELL**

Four of five factors are negative or bottom-ranked. The single supportive factor (12−1 momentum, +11.9%) is **stale by construction** — the 12−1 convention deliberately excludes the last 21 trading days, which is precisely the window containing the crash.

### 4. Key Quant Risk Flags

1. **Momentum reversal already in motion.** Close fell $47.23 (9/21) → $30.39 (10/15) → **$26.99 now**, roughly **−43% from the September high** and −65% from the $76.41 November-2025 peak. The positive momentum score is a lagging artefact; the live trend is sharply negative.
2. **Factor crowding / crypto-beta concentration.** 0.63–0.74 correlation with every miner and beta 3.97 means IREN offers almost no idiosyncratic diversification — it is levered crypto beta inside a "Technology" GICS bucket.
3. **Valuation has no earnings anchor.** Negative P/E and P/FCF, EV/EBITDA 301.7x, so any DCF/multiple work rests entirely on FY28–FY30 estimates.
4. **Thin estimate coverage.** FY30 EPS revision (−60.9%) rests on **1 analyst**; FY28 on 4. Statistically fragile — the strongest-looking negative factor is the least reliable one.
5. **Earnings-quality/OCF wedge.** FY26 net income −$702.6m vs OCF **+$2,100m**, accruals −17.8%. OCF is inflated by non-cash items (impairments/fair-value), so cash generation overstates true economics; F-Score's F7 flags continued dilution.
6. **Liquidity is fine** (10-day ADV >10m shares at peak) — not a liquidity risk, but volume spikes coincide with gap-downs, i.e. distribution.

**Caveat on sample size:** all price statistics use a 252-day window (~250 obs) — adequate for vol/beta, but the alpha estimate is too noisy to be decisive, and the revision signal is single-analyst.
