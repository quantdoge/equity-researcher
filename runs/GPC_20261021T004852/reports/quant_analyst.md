# Quant Analyst

- Symbol: GPC
- Elapsed: 42.6s

---
## GPC — Quantitative Factor & Price Statistics
*Genuine Parts Company · Consumer Cyclical / Auto Parts · Price $123.52 · Mkt cap $17.2B · EV $25.0B*

### ⚠️ Critical data-integrity note before reading scores
**FY2025 GAAP EPS collapsed to $0.47 from $6.49**, on revenue that *grew* to $24.30B (op. income still +$1.21B). This is a ~$1.0B non-cash charge year, not an operating collapse. Consequences:
- **Trailing P/E of 262.8x and EV/EBITDA of 33.2x are artifacts** and must not be used.
- Data inconsistency: FY2025 "EBITDA" ($754M) is reported *below* EBIT ($1,216M) — internally impossible. I discard the reported EV/EBITDA.
- **Normalized basis (FY2026 consensus EPS $7.735, EBITDA $1.96B): forward P/E 15.97x, EV/EBITDA 12.7x.** These are the usable numbers.

### 1. Factor Scores Table
Scores are my own 0–100 composite based on raw factor inputs (z-score tooling unavailable for these names).

| Factor | Score | Sector Rank (Auto Parts peer set) | Signal |
|---|---|---|---|
| Value | **30** (raw) / **55** (normalized) | 4th of 5 | Neutral — cheap only after normalizing |
| Momentum | **45** | 3rd of 5 | Neutral (12-1 +5.73%, but recent reversal) |
| Quality | **40** | 3rd of 5 | Neutral-Weak — deteriorating |
| Low Vol | **35** | 2nd of 5 (beta) / 5th (vol) | Negative on vol, positive on beta |
| Earnings Revision | **55** | 2nd of 5 | Weak Positive — low confidence (see below) |
| **Composite** | **41** | — | **Neutral** |

**Value (30/55).** P/B 3.87, P/FCF 40.9 → FCF yield only **2.45%** (FCF ≈ $421M). Dividend yield 3.41%. Trailing multiples are junk; on normalized forward earnings the stock is genuinely cheaper than AZO/ORLY (which carry premium multiples) but GPC structurally *deserves* a discount — lower margins, industrial-cycle exposure, falling ROIC.

**Momentum (45).** 12-1 month return **+5.73%** (positive). But 252-day total return is **−3.42%**, implying the stock fell roughly **−8.7% in the last ~21 sessions**. Classic short-term reversal — momentum is fading at the tape.

**Quality (40).** The weakest link. ROIC fell **20.3% → 18.8% → 14.3% → 9.6%** over 2022–2025 — a four-year monotonic deterioration. ROE 1.49%, ROA 0.32% (distorted 2025). Offsetting: gross profit/assets 0.404 (healthy Novy-Marx), accruals ratio **−0.0397** (negative accruals = high earnings quality, cash-backed), Piotroski **5/9** (Moderate; fails on ROA improvement, leverage, gross margin trend, and asset turnover). OCF of $891M vs. net income $66M confirms the charge is non-cash.

**Low Vol (35).** Split signal: **beta 0.482 is genuinely low**, but **annualized vol 36.4% is high** and max drawdown 37.5%. R² vs SPY is only **0.030** — 97% of GPC's variance is idiosyncratic. This is *not* a low-vol defensive name despite the low beta.

**Earnings Revision (55).** **I reject the tool's +19.12% "upgrade."** It compared FY2029 EPS ($10.75) against FY2028 ($9.02) — different fiscal periods, not a same-period revision, and FY2029 has **n=1 analyst**. Not statistically meaningful. Proxy evidence is mixed-positive: price targets show more raises than cuts (DA Davidson 145→150→170; Raymond James 145→165; Truist 126→131), but Goldman *cut* 135→122 and UBS trimmed. Median PT ≈ $131 (+6%).

### 2. Price Statistics (252-day window)
| Metric | Value |
|---|---|
| Alpha (annualized, vs SPY) | **−2.85%** |
| Beta (vs SPY) | **0.482** |
| R² | **0.030** |
| Annualized return | −3.42% |
| Annualized volatility | 36.4% |
| Sharpe | **−0.094** |
| Sortino | **−0.129** |
| Max drawdown | **−37.5%** |

**Statistical significance:** Alpha t ≈ **−1.26** → **NOT significant** at 95%. With R² of 3%, the standard error on alpha is ±2.3%, so a −2.85% alpha is indistinguishable from noise. Beta is significant (t ≈ 2.8). **Do not report alpha as evidence of underperformance.**

⚠️ The vol tool returned a Sharpe of **+0.12** while the dedicated Sharpe/Sortino tool returned **−0.094** with the same 36.4% vol. The inconsistency implies different return windows; I use the explicit Sharpe/Sortino tool output and flag both as window-sensitive.

### 3. Composite Quant Signal: **NEUTRAL**
No factor is in the top quintile; none is in the bottom decile on a normalized basis. Cheap-if-you-normalize value, deteriorating but cash-backed quality, fading momentum, high idiosyncratic risk, and statistically insignificant alpha offset by a 3.4% dividend yield and modest positive revision tone. This is a **hold, not a buy or a short**.

### 4. Key Quant Risk Flags
1. **Momentum reversal risk (HIGH)** — +5.73% 12-1 return masking an ~8.7% one-month drawdown. Goldman's PT cut to $122 (below spot) in late October corroborates negative recent drift.
2. **Idiosyncratic / factor-orphan risk (HIGH)** — R² 0.030 vs SPY; correlation with true auto-parts comps is only 0.38 (AZO), 0.39 (ORLY), 0.44 (AAP). GPC will not hedge a consumer-cyclical book. Highest peer correlation is LKQ at 0.58.
3. **Quality decay (MEDIUM-HIGH)** — ROIC nearly halved in three years. If FY2025's charge signals structural impairment in the Industrial segment rather than a one-off, the "normalized" $7.74 FY2026 EPS is overstated and the 16x forward P/E is a trap.
4. **Earnings-quality benchmark distortion (MEDIUM)** — GAAP-to-adjusted gap of ~$7/share means any screen ranking GPC on trailing metrics will systematically misprice it. Avoid.
5. **Liquidity: not a concern** — $17.2B cap, 139M shares.
6. **Estimate coverage thinness (MEDIUM)** — FY2027+ EPS has only 6 analysts, FY2029 only 1. Long-dated consensus is unreliable.
7. **Sample size caveat** — single 252-day window. Alpha and Sortino are not statistically robust; a 3-year window would be required for a defensible risk-adjusted verdict.
