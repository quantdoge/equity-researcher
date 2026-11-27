# Quant Analyst

- Symbol: HPQ
- Elapsed: 37.5s

---
# HPQ — Quantitative Factor Analysis

**HP Inc. | Technology – Computer Hardware | Price $31.15 | Mkt Cap ~$28.1B | 55k employees**

---

## 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| **Value** | P/E 37.1 · P/B 54.7 · EV/EBITDA 19.4 · **P/FCF 9.0** · Div yield 3.88% | 2nd quintile (mixed) | **Neutral** |
| **Momentum** | 12-1 return **+9.37%** | 3rd quintile | **Neutral / Mild positive** |
| **Quality** | ROE 145.9%* · ROIC 8.6% · GP/Assets 5.9% · Accruals −6.7% · Piotroski 6/9 | 3rd quintile | **Weak / Neutral** |
| **Low Vol** | Ann. vol **51.4%** · Beta 0.49 · Max DD 24.3% | 4th quintile (high vol) | **Neutral (low-beta, high-vol)** |
| **Earnings Revision** | Forward EPS revised **+3.48%** | 2nd quintile | **Positive / Upgrade** |

*ROE is distorted by near-zero book equity (BVPS $0.57); P/B 54.7 is not a meaningful valuation read.

**Read-across:** HPQ screens cheap on **cash-flow and dividend** metrics (P/FCF 9.0 vs AAPL 38.5 / MSFT 54.5; yield 3.88% vs 0.3% / 0.8%) but expensive on **earnings and book** (P/E 37.1 ≈ AAPL 39.6, above MSFT 27.3; EV/EBITDA 19.4 between MSFT 17.9 and AAPL 30.5). The cheapness is real on FCF/yield but the quality side is fragile — low gross-profit-to-assets and ROIC of 8.6% are the weak link. This is a classic "value trap" risk profile: optically cheap, structurally low-margin.

---

## 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| **Alpha (annualized)** | **+82.3%** | ⚠️ R² = 0.0237 — **statistically unreliable** |
| **Beta (vs SPY)** | **0.495** | vs 1.211 in company profile — see flags |
| **R²** | 0.0237 | Regression explains <3% of returns |
| **Sharpe ratio** | **1.672** | Good headline, but see return caveat |
| **Sortino ratio** | **3.221** | Strong — favorable upside/downside capture |
| Annualized vol | 51.4% | High for a mature hardware name |
| Max drawdown | 24.3% | Moderate |
| Annualized return (tool) | 87.3% | ⚠️ Inconsistent with 9.4% 12-1 momentum |

The **Sortino (3.22) >> Sharpe (1.67)** spread implies returns are positively skewed with limited downside — attractive if the return series is trusted. But the **82% alpha is essentially noise**: with R² of 2.4%, the beta is near-zero and the alpha estimate carries an enormous standard error. Do not present this alpha as a genuine signal.

---

## 3. Composite Quant Signal: **NEUTRAL**

Reasoning: positive-but-modest momentum (+9.4%) and a genuine earnings upgrade (+3.5%) are offset by **low quality** (ROIC 8.6%, GP/assets 5.9%, Piotroski 6) and **very high volatility** (51%). Valuation is bifurcated — cheap on FCF/yield, expensive on P/E. The alpha/Sharpe figures look stellar but rest on an unstable regression (R² 0.02) and an inconsistent return series. Net: **Neutral** — no factor cluster strong enough to justify Buy; quality weakness argues against upgrading despite the cheap FCF yield.

---

## 4. Key Quant Risk Flags

1. **⚠️ Alpha not statistically meaningful** — R² = 0.0237. The +82% alpha is driven by idiosyncratic moves unrelated to the market; treat as noise, not skill.
2. **⚠️ Beta source discrepancy** — computed 1-year daily beta 0.49 vs profile 1.211. Exposure estimates are unstable; size position sizing conservatively.
3. **⚠️ Quality metrics distorted** — near-zero/negative book equity inflates ROE (145.9%) and P/B (54.7). ROIC 8.6% is the cleaner quality read and it is only modest.
4. **⚠️ Earnings revision confidence** — the +3.48% upgrade rests on **n=1 analyst** for the far-forward period (FY2029); near-term periods have 7–10 analysts. Low sample size limits the signal's reliability.
5. **⚠️ Momentum reversal risk** — 51% annualized vol leaves little cushion; a 24% max drawdown is on record. High-vol names with modest momentum are prone to sharp reversals.
6. **⚠️ Return-series inconsistency** — 87.3% annualized return clashes with 9.4% 12-1 momentum and 24% max DD. Likely a data artifact (split/adjustment); verify before relying on Sharpe/Sortino.
7. **Peer set not apples-to-apples** — "Technology" peers returned are mega-cap semis/software (AAPL, MSFT, NVDA, AVGO…), not Computer Hardware. Cross-sectional ranks are indicative only; a true comp set (Dell, Lenovo) would sharpen the value read.

---

**Bottom line:** HPQ is a cheap-on-cash-flow, dividend-supported hardware name with a mild positive momentum/revision tilt, but **quality is structurally weak and volatility is high**. The headline risk-adjusted ratios (Sharpe 1.67, Sortino 3.22, alpha 82%) are **not reliable** given R² ≈ 0.02 and metric inconsistencies. **Composite: Neutral** — attractive only as a yield/FCF value play, not a momentum or quality holding.
