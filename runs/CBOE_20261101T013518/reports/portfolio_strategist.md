# Portfolio Strategist

- Symbol: CBOE
- Elapsed: 86.7s

---
# CBOE Global Markets — Portfolio Construction Recommendation

**Price $335.53 (verified close 30-Oct-2026) · Mkt cap ~$35.1B · Dilution 105.1M sh · Net cash ~$1.1–1.2B · FY26E EPS $14.22 / FY27E $15.31**

**Data reconciliation before anything else.** I pulled raw OHLCV to adjudicate the price conflict in the handoff. The clean series confirms **$335.53** on 30-Oct-2026 (range 320.01–342.86, volume 2.46M). The Quant's $286.58 was a series terminating 20-Feb-2026 and must be discarded — every multiple, momentum and vol stat derived from it is void. I also **confirm the drawdown the Quant tried to reconstruct away**: $364.92 (13-May) → $230.87 (29-Jun) = **−36.7%**. My sample shows daily moves of ±8–9% clustered in June; realized vol is **~30%**, not 40% and not 19%. The negative beta (−0.19 vs SPY, R²≈0.04) is a statistical artifact — **CBOE is a diversifier by correlation but absolutely not a hedge.**

---

## 1. Agent Conviction Summary Table

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Sector Researcher** | **N/A — report truncated in handoff** | **Zero weight** | Only one line received. Flagged as a gap; no sector view incorporated. |
| **Geo / Legal** | Constructive, watch-list | **Medium** | **LOW–MEDIUM** risk. ~88–90% US revenue, all Tier-1 jurisdictions; Australia divested, Canada pending. Offsets: S&P licence to **2051**, no material enforcement/antitrust actions, $2.66B cash. Watch: **$14.0M CATLLC credit reserve**, ORF sunset, event-contract turf war. |
| **Macro** | **Neutral** | **High** | Earnings positive / multiple negative, they cancel. WTI >$100, CPI 3.72%, Fed hiked Sept, **10Y 4.98% / 30Y 5.32%**. Index-option ADV +22%; **VIX futures ADV −8%**; own beta 0.41. |
| **Value** | **HOLD** | **High** | Wide moat, 74.5% GAAP op margin, ROIC 22.2%, FCF/NI 105%. Base intrinsic **~$360** (range 330–390). **Buy ≤$280, trim >$410.** "Fair price is not a buy." |
| **Growth** | **BUY** (not Strong Buy) | **Medium-High** | Guidance raised 3× (mid-single → **high-teens**); Q3 net rev +18%, adj EPS +43%; Rule of 40 ≈66. But **PEG ~2.8**, consensus 2027 EPS +7.7% vs 2026's +33%. "Own it, don't chase at $335." |
| **Financial Risk** | **LOW risk** | **High** | Net cash, **29x interest cover**, 3.50x covenant vs 0.83x actual, no refinancing cliff (Jan-27 notes covered 3x+). Explicitly rejects the "low-beta hedge" narrative — 40% vol, −37% DD. |
| **Non-Fin Risk** | **MODERATE** | **Medium** | Governance *Adequate* (declassified board, independent chair), clean enforcement record. Flags: **KPI-binary MNPI/surveillance risk**, prediction-market policy binary, CEO tenure 1.4yrs. |
| **Quant** | **BUY** composite | **Medium** | Momentum #1, Quality #1, Low-vol #1 of 5 peers — **but Value bottom quintile** (P/E +14%, P/FCF +26% vs peers). Multiple-driven momentum, no factor cushion. |
| **Short Analyst** | **NO EDGE — reject short** | **High** | Beneish **−2.54**, accruals negative 4 straight years, AR **−11.4%** while revenue +15.1%, cash conversion 111%. Moat *strengthened*. Only bear case is cyclical/valuation. |
| **ESG** | **Neutral** | **Medium** | E-LOW / S-MEDIUM / G-7of10. Only material ESG factor is **product/regulatory risk**: 0DTE >60% of SPX volume. "ESG-tolerable compounder, never a leader." |
| **Alt Data** | **BULLISH, decelerating** | **Medium** | OCC Sept volume +37.9%; 0DTE record 24.2M ADV. **But** stock +32% in one month, Google Trends "options trading" off June peak, **Q1-27 consensus models −1.2% rev / −5.4% EPS**. "Would not chase." |

**Evidence weighting applied:** *stock-selection* weight to Value, Growth, Short and Quant (domain-matched, primary-sourced); *sizing* weight to Fin Risk, Geo/Legal, Non-Fin and Macro (downside definition); *timing* weight to Quant and Alt Data. Sector Researcher assigned **zero weight** — no content delivered.

---

## 2. Consensus Assessment

| Dimension | Agreement | Read |
|---|---|---|
| **Business quality / moat** | **HIGH — unanimous** | All 11 scoring agents: wide moat, ROIC >22%, >100% FCF conversion, licence locked to 2051. The Short Analyst, mandated to destroy it, ended at "no edge." |
| **Balance sheet / solvency** | **HIGH — unanimous** | Net cash, 29x coverage, IG. Even a **−40% revenue** stress leaves leverage at 2.4x and net cash. Not a credit story at any horizon. |
| **Earnings quality** | **HIGH — unanimous** | Three independent forensic passes (Beneish, accruals, receivables) converge. No accounting case. |
| **Valuation / entry price** | **SPLIT — but converging** | Value says HOLD at fair value; Growth says BUY but "don't chase"; Quant says bottom-quintile value; Short says 21.9x for zero growth; Alt Data says already priced. **The apparent conflict is illusory** — nobody is bullish on the *price*. Value and Growth both effectively define ≤$300 as the buy zone. |
| **Forward consensus adequacy** | **CONTESTED** | Growth: 2027 EPS +7.7% is 15–25% too low. Short: consensus flat 2027 EPS is *correct* and the multiple is the problem. Unresolvable before the 5-Feb-27 print. |
| **Risk character** | **AGREES ON DIRECTION, SPLITS ON MAGNITUDE** | Geo/Legal says law-firm-clean; Non-Fin says moderate; Fin Risk says "credit-safe but 30%+ vol with a −37% precedent." **The risk is equity-duration and product-cycle, not solvency or fraud.** |

**Conflict resolution (applied rule: the more specific, evidence-backed risk wins):**

1. **Quant's "low-vol / beta −0.60 / 19% vol" vs Fin Risk's 40%** → I resolve **in favour of Fin Risk, and my raw data confirms it**. The −36.7% drawdown is real; the negative beta is an R²=0.04 artifact. **Consequence: this is sized as a 30%-vol equity, not as a utility.** This single resolution cuts the recommended position roughly in half.
2. **Value (HOLD) vs Growth (BUY)** → Not a real dispute. Both agree intrinsic value ~$360 and both demur at $335. Resolved as: **business = conviction; price = no urgency.**
3. **Growth's claim that price sits "above the majority of published targets"** → **Partly false, and I verified it.** The 15 most recent targets: 300, 301, 309, 315, 332, 334, 343, 354, 356, 358, 380, 450. **Median ≈ $339.** The stock is at consensus fair value, not above it. Upside rests entirely on Morgan Stanley's $450 Top Pick (a $92 raise from $358 two weeks earlier).
4. **Any bull-vs-fraud framing is moot** — Short Analyst's clean bill of health removes the tail risk that would normally dominate position sizing.

**Net consensus verdict: exceptional business, mediocre entry, real but bounded downside. Consensus agreement level: HIGH on quality, SPLIT on price — and the split resolves toward caution.**

---

## 3. Position Sizing Recommendation

### **Initiate at 1.5% of portfolio. Pre-committed ladder to a 3.0% core. Hard cap 4.0%.**

**Scenario-weighted 12-month expected return (my build, off $335.53):**

| Scenario | Prob | Price | Return | Basis |
|---|---|---|---|---|
| Bull — vol regime holds, 2027 guided to low-double-digit organic, 26x on 2028E $16.83 | 30% | **$437** | **+30%** | MS Top Pick path |
| Base — re-rates to Value's base intrinsic, ~23.5x on 2027E $15.31 | 40% | **$360** | **+7%** | Value DCF |
| Bear — volume rollover, EPS cut to $14.50, 19x (CME-like) | 30% | **$275** | **−18%** | Short + Value bear |
| **Probability-weighted** | | | **≈ +6.4%** | |
| *Tail — stagflation trap, 10Y >5.50%, 18x* | *—* | *$243* | *−28%* | Macro bear |

**Sizing logic.** A +6.4% expected return against 30% volatility is a **thin edge** — annualized excess return ÷ variance = ~0.7 full-Kelly, but with a −28% fat tail, full Kelly is reckless and half-Kelly (~35%) is uninvestable in a single name. **The binding constraint is therefore drawdown contribution and entry quality, not the Kelly number.** A 3% position at my hard stop implies a **−59bp portfolio hit**; at the tail, −84bp. That is the correct risk budget for a name with this quality but this price.

**Why only 1.5% at initiation (not 3%):**
- Price sits at **consensus fair value** (median target $339) after **+45% off the 29-Jun low and +32% in one month**; 30-Oct intraday high of **$342.86** is an all-time high.
- **5-Feb-2027 is a genuine binary**: consensus Q4 EPS $3.50 on +7.2% revenue, and Q1-27 consensus models an outright **−1.2% revenue / −5.4% EPS decline** against the March-2026 vol-spike comp. Buying the full position into that print is uncompensated event risk.
- Value's own buy discipline is **≤$280**; I will not ignore the one agent who did the DCF work just because the others are louder.

**Why not pass:**
- The 2051 S&P licence extension **removed the terminal-value cliff** — the single largest historical bear case is gone for a generation.
- Forensic review found **nothing to short**; ROIC 22%, 111% cash conversion, net cash, zero refinancing risk. The cost of being early here is multiple compression, not permanent capital loss.
- **Consensus 2027 EPS may be too low** relative to a company exiting 2026 at high-teens organic growth — an asymmetry that resolves on 5-Feb, and I want to be on the register before it does.

---

## 4. Portfolio Fit Analysis

**Sector / cluster — the most binding constraint.** I measured it: **CBOE–CME 0.60**, CBOE–ICE 0.32, CBOE–NDAQ 0.30. CBOE and CME are the same trade (volatility/derivatives toll roads) at 36% shared variance.
- **Rule: total exchange-operator sleeve capped at 8% of portfolio; CBOE at ≤3–4% within it.**
- If the portfolio already holds **CME ≥3%**, cut the CBOE target to **2.0% core** — the marginal diversification is poor.
- Do **not** treat CBOE as diversifying a broker/retail-flow book (HOOD, IBKR). It shares the 0DTE complex — the same flow that drives their revenue drives CBOE's index-option RPC.

**Factor exposure — CBOE is a rates-duration position wearing a quality label.** At **23.9x TTM / 21.9x 2027E**, with the **10Y at 4.98%** and the Fed having hiked in September with a December hike priced, the multiple — not the volume — is the dominant risk factor. The Macro agent's framing is right: record volumes and a de-rating stock can coexist. Adding CBOE **increases portfolio duration sensitivity** at precisely the point where the term premium is bear-steepening. Net factor additions: **Quality ↑, Momentum ↑ (but multiple-driven → low quality of momentum), Low-beta ↑ (negligible: 3% × (1−0.41) ≈ 1.8bp of portfolio beta), Value ↓.**

**Correlation — helps, but don't over-read it.** CBOE–SPY **−0.19 at R²≈0.04** is statistically indistinguishable from zero. It adds 96% idiosyncratic variance. **It is not a hedge and must not be counted in any downside-protection budget.** It is, however, genuinely non-additive to broad equity beta, which is worth something.

**Concentration in the *thesis*, not the ticker.** CBOE is a single-index, single-licensor, single-product-cycle business: SPX/VIX/0DTE now drives the growth and the multiple. If the portfolio holds any other index-IP or volatility-linked exposure, treat the combined position as one concentrated bet.

---

## 5. Entry Strategy

### **Scale in 50/50. Do not take the full position at the all-time high.**

| Tranche | Size | Trigger | Rationale |
|---|---|---|---|
| **Tranche 1 — now** | **1.5%** | At market, ≤$338 | Own the moat before the 5-Feb catalyst; licence extension de-risks terminal value. Avoid paying >$342.86 (ATH) — use limit orders. |
| **Tranche 2a — value trigger** | **+1.5%** | **≤$300** (−10.6%) | Aligns with Value's framework and with the Oct-1/2 breakout base. Voluntary de-rating, not thesis break. |
| **Tranche 2b — confirmation trigger** | **+1.5%** | After 5-Feb-27 print, **if** 2027 organic guide ≥ low-double-digit **and** stock <$360 | Pays up for information instead of for hope. |
| **(2a and 2b are alternatives — take the first that triggers, not both.)** | | | |
| **Do not add** | — | $361–$405 | Between consensus fair value and Value's trim level there is no compensation for adding. |
| **No-chase rule** | — | If price >$360 pre-print with no upward 2027 revision | Hold at 1.5%, do not chase. |

Whichever tranche does not trigger within 12 months is **cancelled, not carried** — this is a valuation-disciplined build, not a standing order to average into a re-rating.

---

## 6. Risk Management Rules

**Stop-loss (price): weekly close below $270 → exit fully.**
This is not an arbitrary percentage. $270 is the top of the **15–28 Sept base ($253–270)** that preceded the 29-Sept licence-extension gap and the **2-Oct swing low ($269.54)**. A break means the licence re-rating *and* the Q3 beat have fully round-tripped — thesis broken, not noise. At the 1.5% starter this costs **−29bp**; at the 3% core, **−59bp**. Do **not** tighten beyond this: with 30% realized vol, anything inside $300 is noise.

**Soft review (not a stop): close below $300 → halve to 1.0% and re-underwrite before the print.** Never add into a pre-earnings drawdown.

**Thesis invalidation — any one of these triggers a full exit regardless of price:**
1. **5-Feb-27 print: Q4 organic net revenue growth <10%,** or initial 2027 guidance implying **<8% organic** → the mean-reversion case (Value #1, Short #1) is confirmed, not merely feared.
2. **Index-option ADV negative YoY for two consecutive quarters,** or SPX RPC compression >5% YoY → the exclusive franchise is being priced down.
3. **Royalty step-up above "de minimis"** disclosed in the 2027 10-K, or any erosion/shortening of exclusivity → invalidates the single largest component of intrinsic value.
4. **A debt- or cash-funded acquisition >$1.5B** drawing on the $2.66B hoard (Short Analyst's #1 flag; FY2022 precedent: a ~$300–400M write-down drove ROIC to 9.2%).
5. **Adverse appellate / state-AG ruling materially curtailing event contracts *combined with* CFTC retreat on exclusive jurisdiction** — small revenue today (~1–2%), but it is the entire growth narrative and the reason the multiple expanded.
6. **Further CATLLC credit reserves materially above $14.0M** → implies broader impairment of regulatory receivables (Geo/Legal's clearest red flag).

**Trim triggers:**
- **$405–410 → trim one-third.** ~12–14% above base intrinsic value ($360); ~26.5x 2027E. (Value's stated trim level; sector-median P/E multiple reversion is exhausted.)
- **$450 → trim another third** (Morgan Stanley's Top Pick target; ~29x 2027E). Leave a ~1% runner for the 2051-licence compound.
- **Gap >$380 on the 5-Feb print *without* a matching upward 2027 EPS revision → trim one-third immediately.** Price without estimate movement is pure multiple, and multiple is what the 10Y takes back.

**Volatility overlay (portfolio-level, not price-level):** if **VIX sustains <14 for three months**, pre-emptively reduce by one-third. Macro and Alt Data agree this is the tell — VIX futures ADV is already **−8% YoY**, and the worst configuration for CBOE is *sticky inflation without volatility*: multiple compresses while the highest-margin complex goes quiet.

**Monitoring calendar:** monthly OCC/index-option ADV and SPX RPC prints; VIX term structure; 5Y breakevens (escalate if >2.75% while VIX <16); CFTC event-contract final rule and the Kalshi docket; Cboe Canada close conditions; ORF successor fee regime.

---

## 7. Final Portfolio Action

# **INITIATE — 1.5% starter position.**

Not **Add** (no existing position). Not **Pass** (the moat, the forensic clean bill of health, the net-cash balance sheet and the possibly-too-low 2027 consensus are collectively too good to own zero of). Not **Hold** (we are being asked to construct, and the June opportunity at $230.87 has closed).

**The synthesis in one paragraph:** eleven of twelve specialists agree this is one of the highest-quality franchises in financial infrastructure — a legally protected monopoly on the world's benchmark derivative, extended to **2051**, earning 22% on capital with 111% cash conversion, no net debt, and a balance sheet that survives a 40% revenue collapse without breaching a covenant. They also agree, almost unanimously, that **$335.53 is fair value, not a discount** — the stock is +45% off its June low, at an all-time high, at the median of published price targets, priced at 21.9x earnings for consensus-flat 2027 growth, with a 10Y at 4.98% compressing exactly this kind of duration. A −36.7% drawdown nine weeks ago proves how fast the multiple, not the earnings, moves. **Own the business; do not pay up for it.** Start at 1.5%, add only at ≤$300 or on 5-Feb-27 confirmation of a low-double-digit 2027 organic guide, stop at a weekly close below $270, trim into $405 and $450 — and cap the total exchange-operator sleeve at 8% so this does not become a fourth version of the same trade.

**Gaps I could not close (explicit):** Sector Researcher's brief was truncated in the handoff — **no sector view is incorporated**. Peer-median P/E returned 52.1x on n=1 (index-fund artifact) and is unusable; I used the analyst-supplied peer set (CME 27.2x, ICE 29.3x, NDAQ 34.4x). 2029–2030 consensus EPS is n=1 and the revenue line actually *declines* 2029→2030
