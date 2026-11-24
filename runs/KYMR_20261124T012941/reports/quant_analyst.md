# Quant Analyst

- Symbol: KYMR
- Elapsed: 48.3s

---
I now have a complete picture. The decisive fact: KYMR gapped **+30.4% in a single day on 2026-11-23** (7.76M shares vs. ~700k typical) to $150.37 — a catalyst event that flatters every trailing risk-adjusted metric. Writing the report.

---

# KYMR — Kymera Therapeutics | Quantitative Factor Report

**Sector:** Healthcare / Biotechnology (clinical-stage, pre-revenue protein-degradation platform)
**Price:** $150.37 · **Mkt Cap:** ~$12.8B · **EV:** ~$11.9B (~$0.9B net cash) · **Employees:** 273
**Data note:** The only "Healthcare" sector peers returned were mega-cap pharma (LLY, JNJ, ABBV…). There are **no comparable clinical-stage biotech comps in the peer set**, so true cross-sectional ranks are unavailable — ranks below are illustrative quintiles vs. the early-stage biotech cohort, flagged accordingly.

---

## 1. Factor Scores Table

| Factor | Raw Value | Score (0–100) | Sector Rank (quintile) | Signal |
|--------|-----------|---------------|------------------------|--------|
| **Value** | P/E −40.8, EV/EBITDA −39.3, P/FCF −54.2, P/B 8.0x | **5** | 5th (most expensive) | **Bearish** — but metrics N/A: pre-revenue, no earnings/FCF to value; 8x book is rich |
| **Momentum (12-1)** | **−2.17%** (excl. last 21d) | **30** | 4th | **Negative/Neutral** — flat-to-down trailing year; *but +35.8% in last month is a regime break* |
| **Quality** | ROE −19.7%, ROIC −21.0%, GP/Assets 2.3%, accruals −4.5%, F-Score 4/9 | **15** | 5th | **Bearish** — loss-making, dilutive; low-quality *on standard screens* (ill-suited to biotech) |
| **Low Vol** | Vol 59.5%, Beta 1.62–2.03 | **5** | 5th (highest vol) | **Bearish** — among the riskiest names; no low-vol cushion |
| **Earnings Revision** | Forward EPS revised **+17.7%** (2030: −6.21→−5.11) | **55** | 3rd | **Mild positive, LOW confidence** — see caveat |

**Revision caveat (important):** The +17.7% "upgrade" is measured on the **2030** consensus EPS estimate — a 4+ year-dated number with analyst spread of −$8.31 to −$2.05. Near-term estimates show **widening losses** (2026 −$3.97 → 2027 −$5.22 → 2028 −$5.77 → 2029 −$6.21), reflecting a steep R&D ramp. The revision signal is therefore *directionally encouraging but statistically weak* — driven by the long end of the curve, not near-term beats.

---

## 2. Price Statistics (252-day window vs. SPY)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Alpha (annualized)** | **+75.3%** | Massive outperformance — but see R² |
| **Beta** | **1.63** (regression) / 1.62 (vol tool) / 2.03 (vendor) | High market sensitivity; ~1.6–2.0 |
| **R² vs. SPY** | **0.193** | **Only 19% market-explained → 81% idiosyncratic.** Alpha is not a repeatable "edge," it's event risk |
| **Annualized Return** | +84.8% | Flattered by the single catalyst day |
| **Annualized Volatility** | **59.5%** | ~3x the market |
| **Sharpe Ratio** | **1.41** | Good headline — but fragile (see below) |
| **Sortino Ratio** | **2.90** | 2x Sharpe → returns driven by a few large **positive** jumps (positive skew) |
| **Max Drawdown (252d)** | **−25.0%** | *Understates true risk:* Sept-2024 $53 → Apr-2025 $19.45 was **−63%** (outside this window) |

**Critical interpretive flag:** The Sharpe (1.41) / Sortino (2.90) / Alpha (+75%) are all **dominated by one data point** — the +30.4% gap on 2026-11-23 (from $115.31 → $150.37 on 7.76M shares, ~10x normal volume). Strip out that day and the risk-adjusted profile collapses toward the underlying 60%-vol, loss-making base. **Do not treat these ratios as evidence of durable risk-adjusted skill** — they are a snapshot of a binary clinical-catalyst outcome. The Sharpe–Sortino gap itself confirms the return stream is jump-driven, not smooth.

---

## 3. Composite Quant Signal: **NEUTRAL** (speculative, event-dependent)

On a pure cross-sectional factor basis, KYMR scores poorly across the three "workhorse" factors — **Value (5), Quality (15), Low-Vol (5)** are all bottom-quintile, and **12-1 Momentum is negative (−2.2%)**. That is a classic *unattractive* factor fingerprint and would normally be a **Sell**.

What rescues it to **Neutral** is **not factor strength but a binary event**: the +30% catalyst gap, unanimous Buy/Outperform ratings, and a price-target cluster of **$139–$200 (median ~$165, ~+10–15% upside)**. This is a **catalyst-driven momentum trade, not a factor-supported investment**. The formal quant composite does not support a Buy; the tape and analyst revisions do. Net: **Neutral with a speculative long bias**, sized for binary risk.

> Note: Because value/quality/low-vol are structurally inapplicable to a pre-revenue biotech (no earnings, no meaningful book economics, inherently high vol), the "Sell" those factors imply should be **discounted, not ignored** — they tell you *what kind* of asset this is (high-risk, dilution-dependent), not that it is mispriced.

---

## 4. Key Quant Risk Flags

1. **⚠️ Momentum-reversal / post-catalyst gap risk (HIGHEST).** A +30% single-day gap on 10x volume after a flat trailing year is the textbook setup for **mean-reversion and "sell-the-news" fade**. 12-1 momentum is still negative — the trend was *not* established before the pop. Any disappointing follow-through (e.g., BroADen2 durability data) risks giving back the entire gap.

2. **⚠️ Fragile risk-adjusted stats.** Sharpe 1.41 / Sortino 2.90 / Alpha +75% all hinge on one observation. With R² of just **0.19**, ~81% of variance is idiosyncratic — this is **not diversifying**, it is concentrated binary risk wearing a beta of 1.6.

3. **⚠️ Dilution / runway risk.** Piotroski **F-Score 4/9** — fails on positive ROA, positive operating cash flow, and **no-dilution (F7)**. Burning ~$307–410M/yr (2026–27 EBITDA est.) against ~$0.9B net cash → **~2–2.5 yr runway**, near-certain equity raise ahead. 84.4M diluted shares already, trending up.

4. **⚠️ Estimate quality.** "Upgrade" is on a 2030 estimate with a −$8.3 to −$2.1 spread; near-term losses widen through 2029. **Low signal-to-noise** — do not over-weight the revision score.

5. **⚠️ Liquidity/thin float dynamics.** Normal ADV ~500k–1M shares; the catalyst day traded 7.8M. Expect **wide slippage on exits** and gap risk in both directions; position sizing must account for air pockets (as seen in the −63% 2024–25 drawdown).

6. **Data gaps:** No comparable clinical-stage biotech peers available (only mega-pharma returned); cross-sectional factor ranks are illustrative, not true peer-relative. F-Score and value metrics are mechanically distorted for pre-revenue biotech and should be read qualitatively.

**Bottom line:** A high-beta (1.6), high-vol (60%), loss-making, dilution-prone platform biotech that just re-rated ~+30% on a binary catalyst. The factor stack is weak (Value/Quality/Low-Vol bottom-quintile, momentum formally negative); the bull case rests entirely on event follow-through and analyst conviction (~$165 target). **Neutral / speculative Buy only for risk-tolerant, catalyst-aware capital — with hard stops below the $115 pre-gap level.**
