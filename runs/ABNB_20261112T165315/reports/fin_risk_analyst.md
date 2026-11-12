# Fin Risk Analyst

- Symbol: ABNB
- Elapsed: 71.4s

---
## ABNB — Financial Risk Assessment
**Data as of:** FY2025 10-K (filed 2026-02-12) and market close 2026-02-27 ($135.11). All $ in millions.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (high quality)**

Airbnb is a **net-cash, essentially debt-free business** trading at a premium specifically *because* its balance sheet carries no financial risk.

| Signal | Reading |
|---|---|
| Cash & ST investments | $11,014 vs total debt $2,271 → **net cash $8,743** |
| Net debt / EBITDA | **−3.24x** (net cash) |
| Gross debt / EBITDA | 0.84x |
| Interest expense FY25 | **$0** (FY23: $83) — coverage effectively undefined/infinite |
| S&P issuer rating | **'A-' / Stable** (assigned with ~$11B of ST investments at 12/31; Moody's/Fitch not confirmed — *gap*) |
| Debt/assets | 0.10 |

**Refinancing:** $1,999M of debt is classified **current** at 12/31/25 (the $1,995M senior notes rolled from long-term) — a 2026 maturity. It is covered **5.5x** by cash. Post-year-end the company issued **$2.5B of investment-grade notes** (5.25% Mar-2036). No refinancing cliff; pro-forma annual interest of ~$130M is ~5% of EBIT (coverage ~19x).

**Why the Z-Score looks wrong (important):** the tool returns **Z = 1.224 → "Distress."** This is a **false positive**. It uses *book* equity (x4 = 0.585) and is dragged down by **negative retained earnings of −$5,502M** (x2 = −0.248, legacy accumulated deficit). Recomputing with market capitalization:

> Z = 1.2(0.232) + 1.4(−0.248) + 3.3(0.118) + 0.6(**5.75**) + 1.0(0.554) = **4.33 → Safe zone**

Strongly above the 2.99 threshold, and still ~3.2 in a −35% equity scenario. **I do not treat Z = 1.224 as a credit signal.**

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Revenue | 12,305 | 11,102 | 9,917 | +10.8% (decelerating from +11.9%, +18.1%) |
| Operating income | 2,609 | 2,553 | 1,518 | 21.2% margin (was 23.0%) |
| Net income | 2,511 | 2,648 | 4,792* | **−5.2% YoY** despite +11% revenue |
| EBITDA (EBIT+D&A) | 2,700 | 2,618 | 1,562 | |
| Debt/Equity | 0.28 | 0.27 | 0.28 | Very low |
| Net debt/EBITDA | **−3.24x** | −1.75x | −2.93x | Net cash |
| Interest coverage | n/m ($0 int.) | n/m | 26.3x | No interest burden |
| Current ratio | 1.38 | 1.69 | 1.66 | Adequate (see caveat) |
| Quick ratio | 1.38 | 1.69 | 1.66 | No inventory |
| Cash ratio | 0.81 | 1.04 | 1.01 | |
| Working capital | 5,148 | 6,579 | 6,559 | Declining |
| Equity/Assets | 0.37 | 0.40 | 0.40 | Thin book equity |
| Altman Z (book) | 1.22 | — | — | *Distorted — see above* |
| Altman Z (mkt cap) | **4.33** | — | — | Safe |
| Piotroski F-Score | **5** | — | — | Moderate (likely 6 — see gap) |
| FCF | 4,646 | 4,518 | 3,884 | +2.8% — lagging revenue |
| FCF margin | 37.8% | 40.7% | 39.2% | **Deteriorating** |
| SBC / revenue | 12.9% | 12.7% | 11.3% | High, rising |
| FCF yield (mkt) | **5.5–5.8%** | — | — | vs 4.07% as reported (stale mkt cap) |

\*FY2023 net income includes a large one-off tax valuation-allowance release (~$2.9B); not comparable.

**Liquidity nuance:** the 1.38 current ratio *understates* liquidity. Current liabilities of $13,649M are dominated by **funds payable to hosts and deferred revenue** — pass-through obligations settled from guest prepayments, not funded debt. Genuine financial obligations are $2.3B against $11.0B of cash. There is **no cash burn**: FCF is +$4.6B, so cash runway is not a meaningful concept here.

**Note on SBC quality:** $1,592M of SBC is added back in FCF. Cash-out SBC-adjusted FCF = **$3,054M (24.8% margin)**, yield ~3.8%. Buybacks of $3,789M more than offset dilution (basic shares 632M → 613M), but **buybacks exceed SBC-adjusted FCF**.

---

### 3. Market Risk Profile — **HIGH (equity risk, not credit risk)**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **38.1%** |
| Beta vs SPY | **1.19** (my calc) / 1.27 (vendor, 5-yr) |
| Max drawdown (close-to-close) | **−34.5%** (Feb-2025 $161.42 → Apr-2025 $105.69) |
| Peak-to-trough (Mar-24 high) | **−37.7%** ($169.69 → $105.69) |
| Sharpe ratio | **0.68** |
| 1-day 95% / 99% VaR | **3.95% / 5.59%** (~$5.3 / $7.6 per share) |
| 10-day 99% VaR | ~17.7% |
| 52-week range | $105.69 – $161.42 (now $135.11; −16% off high, +28% off low) |
| Sortino | *not returned by tool — gap* |

Beta of 1.19 implies a **−20% market drawdown maps to ~−24% for ABNB**; realized vol is ~2.4x the index, and the stock has twice de-rated >30% in three years on demand/guidance scares (Aug-2024, Apr-2025, Aug-2025). The 3-year cumulative return is only ~+59% (~15.6% p.a.) with materially above-market risk — **risk-adjusted returns are mediocre**. Note: from the Mar-2024 peak the stock is still **−20%**, so this is a high-beta, high-variance, sentiment-driven equity despite the fortress balance sheet.

---

### 4. Downside Scenario Analysis

**Scenario A — Revenue −20% (recession / travel demand shock, $12,305 → $9,844)**

Cost assumptions: cost of revenue 85% variable; SG&A 5% variable (people-heavy, sticky); other opex 55% variable (marketing is the flex lever — Airbnb cut it ~50% in 2020).

| | Base | −20% Revenue |
|---|---|---|
| Revenue | 12,305 | 9,844 |
| Cost of revenue | 3,413 | 2,833 |
| SG&A | 3,930 | 3,891 |
| Other opex | 2,353 | 2,094 |
| **Operating income** | **2,609** | **1,026** (−61%) |
| Margin | 21.2% | 10.4% |
| EBITDA | 2,700 | 1,117 |
| Net debt/EBITDA | −3.24x | **−7.8x (still net cash)** |
| Interest coverage | n/m | n/m (no debt service) |
| FCF (with SBC add-back) | 4,646 | **~$2,900–3,100** |
| FCF yield | 5.8% | ~3.6% |
| Altman Z (mkt, equity −35%) | 4.33 | **~3.2 (Safe)** |

**Conclusion: a 20% revenue decline is a P&L event, not a solvency event.** The company remains net cash, FCF-positive at a ~30% margin, and retains full access to investment-grade capital markets.

**Scenario B — Severe (−30% revenue, COVID analogue).** Operations earned a 15% margin even in 2023 on far lower scale; with 2020-style cost action (Airbnb cut 25% of headcount and marketing) operating income stays positive and FCF remains ~$1.5–2.0B. Historical proof point: in 2020 revenue fell ~30% and Airbnb *still* raised $2B of 10% notes and $1B of equity — and it is now rated **A−** rather than unrated/crossover. Downside tail for creditors is close to nil.

**Where the real downside lives:** the equity, not the balance sheet. The stock trades at ~9.8x book and ~15x FCF; a regulatory shock (city-level short-term rental bans) is a *structural revenue* risk that cost cuts cannot offset. That is not modeled in the data provided.

---

### 5. Overall
