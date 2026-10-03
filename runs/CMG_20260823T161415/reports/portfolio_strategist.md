# portfolio_strategist

_2026-08-23T09:25:58+00:00_

# PORTFOLIO CONSTRUCTION NOTE — CMG (Chipotle Mexican Grill)
**Portfolio Strategist synthesis | Sector: Consumer Discretionary / Fast-Casual QSR | Price $36.90, Mkt Cap ~$47.3B**

All derived risk figures below are the quant_engineer's computed outputs as attributed in the digest (beta, vol, Sharpe, VaR, M-Score, Sloan, DCF intrinsic). I have **not recomputed** anything — where I believe a further computation is warranted, I flag it explicitly.

---

## 1. Conviction Summary

I have mapped the digest's specialist views into the conviction framework (the raw per-agent breakdown wasn't provided, so this is the synthesis layer's aggregation of what the digest supports):

| Dimension | View | Conviction | Key finding |
|---|---|---|---|
| **Value** | Bearish on price | **High (7/10)** | FMP DCF intrinsic **$24–27/sh** sits *below* the $36.90 market price; P/E ~32x, FCF yield ~3.3%. Clean as growth, expensive as entry. |
| **Quality / forensic** | Positive but qualified | **Med (5/10)** | M-Score **-2.65** (clean), Sloan accruals **-6.4%** (cash-rich), zero interest-bearing debt, ~$1.0B net cash. **BUT ~96% of FY25 EPS growth was buyback-driven (net income +0.1%)** — "quality" is partly financial-engineered. |
| **Growth** | Cautiously recovering | **Med (10/10)** | Revenue +5.4% FY25, comps **-1.7%** (first decline since 2016) → Q2'26 comps **+2.2%**, txns +1.0%. Unit pipeline 350–370/yr, Chipotlane ~80%. Historical CAGR 13.5%. Rule of 40 ~17.5 (was 28) — decel. |
| **Momentum/market** | Bearish | **Med-High (6/10)** | 12-1m momentum **-59...**— actually **-25.7%**; 1y Sharpe **-0.25**, Sortino **-0.34**; price -58.9% off peak. Negative realized momentum, though RSI 62.4 shows near-term stabilization. |
| **Low-vol/# of size** | Not a contributor | **High (7/10)** | **41.6%** annualized vol is *high*, not defensive. CMG does **not** belong in the low-volatility bucket. |
| **Risk / event** | Bear (tail) | **High (8/10)** | Fresh multistate **salmonella/jalapeño Aug-2026** (-10% day, -12% wk); 2015-18 history + $25M DPA; CA wage escalation; Mexico avocado tariff (25%); CEO+CFO turnover. Left tail is real, not theoretical. |

**Aggregate conviction score: 4 / 10.**
**Stance: HOLD, biased to TRIM/REDUCE.** No new initiation at current price/expense. This is a well-managed, clean-balance-sheet operator with a genuine recovery narrative — but it is **priced for premium growth it is not yet delivering** (price above FMP intrinsic; comp-vol and margin compression; weak momentum; live food-safety tail). The valuation, momentum, and risk dimensions collectively outweigh the quality/growth positives.

---

## 2. Position Sizing

- **Case weight (current):** Cap at **1.0–2.0%** of a diversified equity book. CMG does **not** earn a high-conviction 3–5% weight.
- **Kelly/edge-odds logic:** Probability-weighted edge is thin. Bull thesis exists (recovery, unit growth, quality), but it must be discounted by (a) price > value intrinsic, (b) negative momentum, (c) fat left tail from food-safety/CA wage/tariff, (d) buyback-inflated EPS masking +0.1% operating income growth. That is a roughly **coin-flip-to-negative** edge against a **large** specific-risk footprint → size **≤2%**, and prefer partial entry.
- **Entry / scale-in discipline given fat left tail:** Do **not** initiate fresh at $36.90 (price above value band). If adding, enter **half now, half only after** one of the following resolves (asymmetry favors waiting — the fat tail is symmetric-ish but the payoff is a step-down on bad news):
  - Price trends toward **$30–$32** or squarely into the intrinsic band (below ~$27 is a genuine value entry, not a trap);
  - **Two consecutive quarters** of comps ≥ +2% **and** FY guidance holding ≥ +8% revenue;
  - Margin evidence that the food-safety/tariff shock is contained (Q3 margins not below ~14%, comps stable).
- On existing holders: **do not add**; let the posit pro determine %, but trim any overweight in Consumer Discretionary/RI. If new capital, treat as a **reconsideration pile at 0.5–1%, scaled in on thesis confirmation**, capped at 2%.left-tail.

---

## 3. Portfolio-Level Factor Exposure

Factor buckets CMG contributes:

| Factor | Bucket | Direction |
|---|---|---|
| **Growth** | Medium-Low (decelerating) | Revenue +5.4%, comps recovering. Adds moderate growth tilt. |
| **Quality** | Clean | Zero IPC debt, $1.0B net cash — but buys-adjusted EPS growth → quality is partially engineered. Neutral-to-positive tilt. |
| **Momentum** | Strongly **negative** | -24.mo momentum, -0.25 Sharpe → a *negative* momentum beta to the book. |
| **Value** | Negative (expensive) | Price > intrinsic DCF. |
| **Low-volatility** | **Adder, not contrib.** | 41.6% vol, large → single-name risk. |

**Does it diversify or concentrate?** It *concentrates* three of the things an equity book least needs right now: (1) Consumer-Discretionary/restaurant spending (correlated with discretionary income and K-shaped consumer weakness — no hedging diversification), (2) **single-name event risk** (food-safety ~ 2018-18 precedent mattered a 25%+ drawdown), (3) tax/tariff sensitivity (CA min-wage, avocado tariff), and (4) a **negative momentum** tilt. It adds **growth** beta but at full market price and high specific vol. **It is a net risk-concentrator, not a diversifier, at current price.**

---

## 4. Correlation / Fit Note

- **Beta:** computed **0.75 (1y) / 0.99 (full)**. That is *market-like-to-slightly-defensive at the market level* but matters less than the **41.6% annualized idiosyncratic vol**, which is the dominant driver of 1-day VaR ($-3.75%/99%-5.56%). In other words: CMG is **not** a market-beta diversifier — its 1-day tail risk is almost entirely idiosyncratic (food-safety event/produto).
- **Fit:** In a diversified book it is a **single-name risk add**, not a low-corr diversifier. Pairing it with a low-idiosyncratic defensive name would hedge beta but cannot hedge the product-irreducible *outbreak risk* that hits CMG alone.
- **Peer position:** FY25 revenue growth 6th-of-8; comps **-1.7% worst in set** (vs CAVA +4.0, TXRH +4.9); margins 4th-of-8. It is at risk for ranking as a *laggard* in the QSR pack on the thing holding the rally.
- **Actionable correlation check (needs quant, not estimated here):** I do NOT have a computed peer/benchmark correlation matrix. **Recommend the quant_engineer compute a 30-factor-style correlation/Covariance matrix of CMG vs CAVA, TXRH, SHAK, DRI, and S&P 500 / Russell 2000 over the trailing 1-2 yrs**, plus the CMG-idiosyncratic share of total variance. That would confirm whether the book already holds enough QSR single-name exposure to make CMG redundant vs incremental. Not computed here by design.

---

## 5. Monitoring Triggers, Stop, Exit

**Thesis invalidation — EXIT:**
1. **Food-safety escalation** → replicated 2018-18 scale outbreak (repeat $25M-class government action, class/justice exposé) → **exit** (the -10% day is a warning; a repeat cuts brand rights deep).
2. **Com상여 relapse:** comps back negative for 2 consecutive quarters or weekly traffic data breaks -3% → revalue down.
3. **Margin collapse:** operating margin below ~14% trailing, or labor >26% of sales sustained + food/packaging >30% → structural break (the model stops compounding).
4. **Buyback-signal breach:** if buy-in exceeds EPS and operating net income declines in a quarter, flag "EPS-quality fails further" — a reason to trim beyond price.

**Stop-loss / price:**
- **Price stop (hard adjust):** exit if shares trade below **~$24/$17–25 intrinsic floor / or through ~$28 trough support (Jun-2026 low $28.18)** on fundamental, not just fatigue, drawdown. If it reaches **~$26** on a food-safety repricing, treat as thesis-break, not bargain.
- **Trim trigger (over-value discipline):** if price crosses **~$39 (≈41% above FMP intrinsic high)** it is already valued-for-growth; **trim if price > ~$40** (it's then ~150% of intrinsic high end) — but *current price $36.90 is already > DCF band*, so the book should already be underweight by valuation rule.
- **Stop-loss (mandatory):** a **-15% intraday/till-week move on any confirmed broad food-safety event repetition** triggers **immediate mute/halve**; a 2nd tier at **-25%** is an **earned exit** for the smaller positions.

**Upgrade signals (for potential re-add):** comps ≥ +2% for two quarters, revenue guide ≥ +8% with operating margin stable, and food-safety clean for ≥ 2 quarters → may move from Trim back to Hold, and if price then sits **below $34**, reconsider scale-in to a 2% cap.

---

## 6. Final Portfolio Action

**TRIM / HOLD AT REDUCED WEIGHT — DO NOT INITIATE at current price.** 
- Cap weight at **≤1.5–2%** (ideally underweight given price > value intrinsic).
- Enter-at-value (target band ~$30–$32/earning-fatter as the recovery confirms); scale-in only on the spelled-out thesis confirmations, never all-at-once into a fat-tailed food-safety/tariff book.
- Treat as a **single-name risk concentrator** — limit CMG's size both on value *and* on id-volience footprint, and avoid stacking with other QSR/discretionary names until the peer correlation matrix is computed.
- Monitor triggers above quarterly: comps/traffic, margins (labor/food/packaging), buyback-to-EPS ratio, and any food-safety event.

**Attribution note:** valuation/quality/forensic figures (P/E ~32x, EV/EBITDA, FCF ~3.3%, DCF $24–27, M-Score -2.65, Sloan -6.4%, net income +0.1%, buyback-driven EPS, zero debt, $1.0B cash, unit pipeline, comps) — all as attributed in the digest to FMP endpoints and the quant_engineer. Momentum/vol/beta/VaR/Sharpe/Sortino — computed quant_engineer stats from the digest. Peer-comp growth ranks and bar use digest peer data (CAVA +4, TXRH +4.9, SHAK +2.1; cmg -1.7%). The **peer correlation matrix is a flagged-to-compute item** and is **not stated-forecast** here.
