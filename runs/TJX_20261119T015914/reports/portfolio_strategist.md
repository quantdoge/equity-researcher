# Portfolio Strategist

- Symbol: TJX
- Elapsed: 102.4s

---
## PORTFOLIO CONSTRUCTION RECOMMENDATION — THE TJX COMPANIES (TJX)

**Price: $140.30 (close 18-Nov-2026) | Mkt cap $157.8B | EV $165.1B**

### 0. Data Integrity Resolutions (must read before the table)

Three agents disagreed about the price. I resolved it from raw OHLCV: **the latest bar is 11/18/2026 at $140.30**, confirmed by the valuation engine (market cap $157.8B, 1.125B shares).

| Conflict | Resolution |
|---|---|
| Quant used $152.93 "close 2026-02-13" and re-based all multiples +9.0% | **Stale by nine months.** All Quant valuations must be discarded. At $140.30 the true multiples are *lower*, not higher. |
| Quant: +26.8% 12-1 momentum; Value: $156.66 last close | Both stales. My own regression: **alpha −9.19%, Sharpe −0.248, beta 0.305, R² 0.029.** The +5.84% alpha claim is inverted. |
| Quant dismissed the 26.83% max drawdown as "a stale/fixed value" | **Quant is wrong; the number is correct.** $167.29 (6/12/26) → $122.41 (9/16/26) = **−26.8%**, reproduced exactly from the daily series. |

**Net: the momentum tailwind the Quant underweighted does not exist.** TJX is −16.1% from its June high, −6.0% over six months, and has posted *negative* risk-adjusted return for a year while the business compounded EPS ~14%. That is a de-rating, not a momentum trade.

---

### 1. Agent Conviction Summary

| Agent | View | Conviction | Key Finding | My Weight |
|---|---|---|---|---|
| **Sector** | BULLISH — sector ATRX, TJX preferred vehicle | Medium-High | +459bps OM premium to peer median; off-price share +950bps vs dept stores since 2022. Own data shows TJX is *slowest-growing* of Big Three. | **High** |
| **Value** | HOLD / DO NOT INITIATE; intrinsic ~$100–105 | High | 28.7x TTM, 19.3x EV/EBITDA, 3.1% FCF yield; reverse DCF requires 14.5% FCF CAGR vs 6.4% rev CAGR history. | **High** (DCF inputs aggressive — see §2) |
| **Short Analyst** | No fraud; **margin-cycle short only** | Medium-High | Beneish −2.66, accruals −3.9% (4 yrs negative) — clean. **But Q3 GM −11bp YoY (first decline); Q4 guide cut on fuel/freight; inventory days 57.4→63.9; ~$32M insider sales at $157–169, zero buys.** | **High** — most differentiated evidence |
| **Macro** | NEUTRAL — favourable business, hostile discount rate | Medium-High | 10Y **5.13%**, 30Y 5.47%, 5Y real ~2.7%, Fed hiking. Multiple-led upside capped. | **High** (verified: 2s10s +39bp, no inversion) |
| **Fin Risk** | **LOW** | High | Net **cash** ex-leases ($2.87B debt vs $6.23B cash); 98.6x interest cover; Altman 6.4 on mkt cap; F-Score 8/9. | **High** (corroborated by my ROIC data) |
| **Geo Legal** | MEDIUM (leaning low) | Medium | All 10 countries high-rule-of-law; no material Item 3 litigation. Tariff-refund consumer action = credible new front. | Medium |
| **Nonfin Risk** | MODERATE | Medium | Govemance ADEQUATE (non-indep. Exec Chair); **insider tape one-way**; $331M refund/$112M bonus controversy with Senate criticism. | Medium |
| **Growth** | BULLISH — 6–7% rev runway, 7,500-store target | Medium | FY27E rev $64.1B (+6.1%), EPS $5.22 (+7.0%). *Report truncated mid-table; no valuation discipline.* | Medium |
| **Alt Data** | BULLISH (moderate) | Medium | News tone +1.00, 0 negatives. **But TJ Maxx search flat over 12 weeks — Marmaxx not visibly fixed.** Series ends 11/8, pre-Black Friday. | Medium |
| **Quant** | BUY, composite 66/100 | **Low** | Quality 92, Low-Vol 85 — corroborated. **Value 30/100 — corroborated.** Momentum +26.8% and alpha +5.84% — **invalidated (stale data).** | **Low** (quality/vol legs only) |
| **ESG** | AVERAGE / NEUTRAL | Medium | ~$5–15M/yr run-rate penalties = <0.1% of revenue. Explicitly not thesis-relevant. | Low |

---

### 2. Consenssus Assessment: **SPLIT — but a clean, diagnosable split**

This is not noise; it is a textbook **"great business, wrong price"** split, and the two halves are internally unanimous:

**Consensus #1 (HIGH agreement): the business is elite.** Sector, Value, Growth, Fin Risk, Quant, Short — every agent independently reaches the same conclusion. 30.3% ROIC rising four consecutive years, net cash, 125% cash conversion, Beneish −2.66, wide moat from a 21,000-vendor buying network. **The Short Analyst could not build a forensic short and said so explicitly.** No agent disputes quality.

**Consensus #2 (HIGH agreement): the price already capitalises it.** Value (fails margin of safety), Quant (Value 30/100, worst of peer set), Macro (5.13% 10Y hostile to 28x), Short (margin inflection). *Four independent methodologies, same conclusion.*

**Contested — and where I must adjudicate:**

- **Is margin expansion structural or cyclical?** Sector/Value/Fin Risk say structural (+335bps GM). Short says the inflection is here. **Short wins on the near-term evidence, and the specific numbers are checkable:** Q2 FY27 GM of 33.4% contained 2.0pts of tarif refunnds (≈$0.21/sh, ~15% of that quarter's EPS); Q3 GM *fell* 11bp YoY; Q4 guided **below** prior outlook on fuel/freight. FY26's margin was explicitly credited to "lower freght and lower shrink" — both cyclical. **Adjudication: the +335bps is real but ~150–200bps of it is cyclically peak. FY28 margin is flat-to-down, not expanding. EPS growth reverts to ~6–8%.**

- **Is the refunnd a tailwind or a headwind?** No agent framed this correctly. It is **both**: a one-time $331M benefit *inside* the FY27 base that must roll out of the FY28 comp. That mechanically depresses FY28 growth regardless of operations. This is the single most under-appreciated item in the entire book.

- **Value's $100–105 intrinsic is too low.** A 8.5% WACC / 2.5% terminal DCF on a 30%-ROIC business with net cash understates value; my honest range is **$110–140**, centred ~$125. I weight Value's *direction* (premium exists) heavily and its *magnitude* only partially. Note the de-rate math is milder than Value implied: at peer-median 23.7x, downside is **$116 on TTM EPS (−17%)** but only **$136 on FY28E EPS (−3%)**.

---

### 3. Position Sizing RecoMmendation: **0% now; pre-authored ladder to a 3.0% cap**

**Kelly test: negative edge → size zero.** At $140.30 you pay ~112% of my $125 mid-cycle intrinsic. Expected 1-year return decomposes as:

| Component | Contribution |
|---|---|
| EPS growth (reverted, ex-refund) | +6% to +8% |
| Dividend | +1.3% |
| Multiple: hold at 26.5x FY27E | 0% |
| Multiple: de-rate to 23.7x peer median | −10% to −15% |
| **Expected return (probability-weighted)** | **−6% to +9%, centred ~+2%** |

A ~2% expected return against 26% annualised volatility and a −26.8% realised drawdown is **not investable at size**. Risk/reward is roughly symmetric ($167 prior high = +19%; $105–112 macro bear case = −20% to −25%), with the left tail better-anchored than the right.

**If the portfolio mandates consumer-defensive ballast:** cap at **0.5% tracker position** only, with the hard rules in §6.

**Ladder (pre-authorised, no discretion):**

| Tranche | Trigger | Size | Implied multiple | Rationale |
|---|---|---|---|---|
| 1 | **$118–120** | 1.0% | 22.6x FY27E | Peer-median de-rate complete; momentum fully flushed |
| 2 | **$105–108** | +1.0% | 20.0x FY27E, 4.6% FCF yield | Value's buy zone **and** Macro's bear case (−20/25%) converge here |
| 3 | **$88–92** | +1.0% | 17.3x FY27E, 5.5% FCF yield | "Back up the truck" — cyclically depressed multiple on structural moat |
| **Max** | — | **3.0%** | — | See §4 |

**Why 3.0% and not 3–5%:** top-decile quality argues for the high end; three offsets cap it — (i) 21% P/E premium to peer median, (ii) margin inflection + refund rolloff, (iii) factor crowding (quality+low-vol is the market's most crowded pair) and 0.58–0.64 correlation to off-price peers limits incremental diversification.

---

### 4. Portfolio Fit Analysis

*Holdings were not supplied; framed conditionally.*

**Correlation matrix (252d, computed):**

| | TJX | SPY | ROST | BURL | HD | XLP | WMT | COST |
|---|---|---|---|---|---|---|---|---|---|---|
| **TJX** | 1.00 | **0.17** | **0.64** | **0.58** | 0.43 | 0.41 | 0.36 | 0.30 |

- **Beta 0.305, corr to SPY 0.17, R² 0.029** → TJX contributes almost no market exposure. It is a genuine **portfolio-beta reducer** and, on this axis alone, an attractive addition to a high-beta book. ~21% of its variance is systematic; ~79% is idiosyncratic.
- **Factor tilt:** adding TJX raises loading on **Quality + Low-Vol** — the most crowded factor pair in the market. You are *lowering* beta while *raising* crowding risk. Those are different risks and both must be sized.
- **Duplication flag:** if the book already holds ROST or BURL, correlation of 0.64/0.58 means TJX is substantially the **same off-price factor**. Cap the combined off-price sleeve at **3–4%**, and prefer TJX as the vehicle (highest margin, only one with above-median growth *and* margin expansion).
- **Sector:** Consumer Discretionary / Apparel Retail. If the book is already overweight consumer, this is a pass on sector grounds alone.
- **The uncomfortable datum:** alpha **−9.19%** over the trailing year. Despite beta 0.30, TJX has been a **performance drag, not a hedge**. Do not buy it for downside protection — the low beta did not deliver it.

---

### 5. Entry Strategy: **Do not buy at market. Ladder only.**

The stock gapped +8% on 11/18 (from $129.85) on an **in-line** EPS print — a relief rally, not a re-rating. Alt Data confirms the demand backdrop supports it but also that **TJ Maxx search interest is flat over 12 weeks** while Marshalls re-accelerates. Management calls Marmaxx "self-inflicted," implying a fixable execution issue; the alt data says it is **not yet fixing**. A one-week pre-Black Friday signal is not confirmation.

Combined with the fed at 3.75–4.00% and the 10Y at 5.13%, buying a 26.5x-forward compander **three days into a relief rally, at a 21% peer premium, in a bear-steepening curve** is the worst-executed version of a good long-term idea.

**Rule: no market orders. Limit orders only, per the §3 ladder. Re-run alt-data search series after Black Friday before tranche 1 is even considered.**

---

### 6. Risk Management Rules

**Stop-loss (any tracker/held position):** hard stop on a **weekly close below $119.00** (−15.2%), which is beneath the 9/16 52-week low of $122.41. A break of that low confirms the de-rating trend and invalidates the "quality defends the multiple" premise.

**Thesis invalidation — any TWO of these, exit regardless of price:**
1. **Marmaxx comps fail to exceed +2% by Q1 FY28** (consensus needs ~3%).
2. **Consolidated gross margin below 30.5% for two consecutive quarters** — i.e. the refund rolloff plus freght/shrink reversal is not offset by merchandise margin.
3. **Inventory days above 68** (currently 63.9; was 57.4 two years ago). Packaway into decelerating comps is how markdown risk is manufactured.
4. **FY28 EPS guidance below $5.40** (<5% growth).
5. **A state AG or filed consumer class action on tarif-refund retention** → upgrade to Govemance/Nonfin escalation (currently pre-suit investigation only).
6. **10Y UST above 5.75%** → the 20x scenario becomes base case; multiple compression dominates EPS growth.

**Trim triggers:**
- Trim one-third at **$167** (prior high) if reached on **multiple expansion rather than an EPS upgrade** — i.e. P/E above 30x FY28E without a matching estimate revision. That is re-rating, and it does not repeat.
- Trim one-third if **P/E exceeds 32x** on unchanged forward estimates.
- Trim if the off-price sleeve (TJX + ROST + BURL) exceeds 4% of the portfolio.

**Review cadence:** Q4 FY27 on **24-Feb-2027** (consensus EPS $1.47). This is the decisive print — it is the first quarter where the tarif-refund comp base and the fuel/freight reversal both bite, and management has already guided Q4 *below* prior outlook.

---

### 7. Final Portfolio Action: **PASS**

**Do not initiate at $140.30.** Pre-authorise the three-tranche ladder in §3 (max 3.0%). Existing holders: **HOLD, do not add** — selling a 30%-ROIC, net-cash, wide-moat compounder incurs tax friction and forfeits compounding, but there is no case for adding at a 21% peer premium into a margin inflection.

**The one-paragraph rational:**

TJX is the highest-quality operator in an attractive channel — 30.3% ROIC rising four years straight, net cash, 125% cash conversion, a forensic-clean P&L, and a beta of 0.30 that would genuinely diversify a high-beta book. None of that is in dispute; eleven
