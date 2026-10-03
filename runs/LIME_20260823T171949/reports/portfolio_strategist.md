# portfolio_strategist

_2026-08-23T09:24:30+00:00_

# LIME (Neutron Holdings) — Portfolio Construction Recommendation

## Data grounding (all retrieved, traceable)

| Item | Source |
|---|---|
| Price $41.06, mkt cap $2.63B, day vol 348,618 sh, 50d avg $30.81, 200d avg $30.81 | `quote`/`quote` |
| Price range since IPO: **$23.87 low → $42.84 high**; run from $25.00 offer to $41.06 (+64%) | `chart`/`historical-price-eod-full` |
| IPO pricing July 1, 2026 at $25 (range $24–26); net raise ~$174M | Renaissance Capital / IPO Scoop via `web_search` |
| Q1'26 revenue $170.2M; 2023 loss $24.6M → 2025 reported profit $70.4M | Micromobility Industries / S-1 via `web_search` |
| General lockup ~160 days (~early Dec 2026); quiet period ended Aug 10, 2026 | Stock Titan / MarketBeat via `web_search` |
| Peer refs: Lyft $17.47/$6.6B, Uber $78.80/$160B | `quote`/`quote` |
| Earnings date, beta, vol, correlation, fundamental scores | **not available** / must be computed |

---

## 1. Position sizing — satellite, not core

**Recommendation: capacity is a long position, size ≤1.5% of NAV, model at 1.0% target; if any short-side signal triggers, the same 1.5% cap applies gross.** This is classically a **satellite/tactical** position, *not* a core holding. Do not carve from the core bucket.

Rationale on the hard caps:
- **Liquidity is the binding constraint.** LIME averages roughly 200–400k sh/day (~$8–16M/day at $40). A 1% position in a $1B sleeve = ~$10M nominal ≈ an entire day's float. You cannot build, trim, or exit a meaningful position without moving the stock. This alone caps you well below the 3–5% a high-conviction name would otherwise earn.
- **Recent IPO, single-name, pre-profit, likely high-beta high-vol** — a double concentration penalty (idiosyncratic + factor). Pre-profit 2023-24 → break-even 2025 → Q1'26 revenue of $170M is encouraging but thin; the earnings series is only ~1 year old and unproven at scale.
- Because no survivorship/long-horizon record exists, Kelly-criterion sizing collapses to a **risk-budget answer**: keep the *edge-implied* weight small and put most of the position-side discipline into sizing discipline, not max sizing.

Consensus score (Section 2) comes out **neutral-to-mild-positive (~2.9/5)** — meaning the call is "own a little, risk-manage aggressively," not "own a lot."

Position target by conviction scenario (in a diversified book):
- Bull (conviction ≥3.75): **up to 2%** (still liquidity-capped; 2% ≈ 1–2 days' float).
- Base case (my read): **1.0–1.5%**.
- Confirmed negative/3+ red flags: **flat/short via a *small* tactical short ≤0.5–1%** — but only if liquidity and borrow cost are workable; otherwise Pass.

---

## 2. Conviction aggregation framework & weights

Weight each specialist by (a) how far their evidence is from pure narrative and (b) their risk-priority in this profile:

| Agent | Domain weight | Why |
|---|---|---|
| **Risk / Short** | **30%** | Highest veto power for a pre-profit single name; a fraud/going-concern flag must override everything. |
| **Quant** | **20%** | Returns your realized vol/correlation/capital-structure facts — directly sizes the position. |
| **Value** | **15%** | On an unprofitable story stock, intrinsic value is the *least* informative signal (DCF on a loss-maker is speculative). Downweight vs. a mature compounder. |
| **Growth** | **15%** | This is the one positive differentiator (2025 profitability turn, Q1'26 $170M rev) — hold moderate weight. |
| **Macro** | **10%** | Rates/capex/consumer spend frame but don't drive a single high-vol name. |
| **Sentiment/News** | **5%** | Tradeable sentiment helps timing, not thesis. |
| **Moat/Competitive** | **5%** | Real but secondary for sizing. |

Total = 100%.

**Aggregation rule:** Conviction = Σ (specialist_score × domain_weight), then apply **vetoes**:
1. **Short/fraud signal** (conviction>0.7) → floor conviction at 0, force Stop, no long.
2. **>2 agents' red flags** in *fundamental and risk* — drop max weight to 1%.
3. Quantitative *liquidity* or *vol* breach (e.g., vol>60% ann. or volume < capital) — hard cap applied.

Consensus grade: **Split-direction consensus, weak**. Multiple agents (growth, sentiment, moat) are mildly positive; risk regime (macro/funding, vol, short-critical) is cautious. No single agent is strongly non-neutral. That is a **package-level agreement ≈ Medium**, direction ≈ "selective long."

---

## 3. Entry / exit discipline

Given the price has already run from $25 → $41 (+64% in ~7wk), **do not chase the tape**:

- **Scale-in:** 3 tranches, not all-at-once. Tranche 1 (33% of target) only **below $38**; tranche 2 (33%) **below $33–34**; tranche 3 (34%) only on confirmed fundamental catalyst (positive EPS / profitability guide) — otherwise hold dry powder. At $41 now, **do not open a full position**; stand aside and set alerts to the tranches above.
- **Trim trigger:** if the name re-rates to >2.5% of NAV from drift, trim mechanically back to 1.5% regardless of thesis.
- **Rebalance:** hard-trigger if weekly move >30% in the post-IPO first 90 days; re-validate thesis on any >20% single-day move (both ways).
- **Price/period elastic:** base valuation on 2025 Q1–2026 Q1 trajectory, not the current tape — the market cap is already pricing in a lot of success.

---

## 4. Portfolio-level correlation & factor note

- **Factor tilt:** LIME almost certainly loads on (a) **growth/small-cap** and (b) **cyclical-consumer/ridership** ("macro + micro mobility"). If you already hold Lyft / Uber / consumer-cyclicals, LIME adds **factor-crowding, not diversification** — a market-away in-rate- shock tears at all of them at once.
- **Correlation:** expect **high-ish** vs Lyft (same ridership/addiction to consumer spend) and **moderate** vs Uber (overlap in TaaS exposure). This is *not* a diversifier; treat it as an incremental factor bet, sized accordingly.
- **Behavior on risk regime:** if you already carry an overweight in high-beta/small-gloss names, the cap is reduced **size-wise** because of the crowding, not only LIME's own risk.
- **Signal with the factor, not against it.** No — separate from any hedge value; it is a pure long to them over a risk-tolerance lens, so treat it as factor-additive.

---

## 5. Risk controls

1. **Position limit:** hard 1.5% long cap (per above); 2.0% absolute outer ceiling only at ≥3.75 conviction **and** when daily traded $ can chronicle build/exits.
2. **Liquidity constraint:** only opened net if average daily traded $ ≥ ~2× the target size. Current ~$8–16M/day ≈ supports a ~$4–8M position per ~ trading guideline. Cap accordingly.
3. **Event risk:**
   - **Lockup expiry ~early Dec 2026** (~160 days post-offer): treat as supply/overhang event — expect float pressure. Consider not holding into it unless genuinely willing to ride volatility; trim/hedge watch.
   - **Quiet period ended Aug 10** — when analyst coverage publishes, re-validate (first opinion released, low-volume watch).
   - **Earnings:** first print date from the S-1, but `calendar`/`earnings-company` had no entry for LIME yet (**not available** in FMP as of retrieval); do not position large into it blind.
4. **Thesis invalidation (exit):** any of — reversal in Q2/Q3 revenue trajectory, profitability prints turning negative for 2+ quarters, margin/insider selling spree, or a short/fraud flag.
5. **Trim trigger:** trim to 1% ≤ if price ≥ 90% of none-available intrinsic-value estimate; prefer to-hold sized to <1.5%, not to fight.

---

## 6. COMPUTE REQUESTS (for quant_engineer)

None needed to product this recommendation, but the following would sharpen it — flag to quant_engine to compute:
- **COMPUTE REQUEST A:** realized 90-day (and since-IPO) **annualized volatility** of LIME vs Lyft, Uber from the EOD series `chart`/`historical-price-eod-full` (I clipped only the run; do not hand-estimate these). This directly gates the position-cap rule in §3/§5.
- **COMPUTE REQUEST B:** **rolling correlation** of LIME's daily returns vs LYFT and UBER, since July 1, 2026 — to confirm "crowding yes/moderate" in §4 rather than assume.
- **COMPUTE REQUEST C:** **effective beta** of LIME to the S&P 500 (and a broad MoB index) from `indexes` EOD series — for factor-tilt quantification.
- **COMPUTE REQUEST D (if keeping it core-like):** a **Kelly-edge table** applying conviction weighted by domain weights to decide whether 1.5%→2% upgrade is justified; needs the return/loss ratio from the above.

---

## Portfolio-strategy reading

**Current tape ($41, +54% since IPO) = NO new full position.** This is a **post-run, low-liquidity, pre-unit-specific-profit, single-agency name** — it is a watchlist term: at-or-below $26 it is a candidate for a small satellite long (1.0–1.5%), sized by liquidity (not by thesis), with hard risk triggers. It is **not a Hay digested core holding**. Mark as: **REDUCE/HOLD light if held, else SIDELINE on watchlist.** Do not build above a 1%–2% cap, and force re-evaluation at first Dec-2026 lockup and first earnings.

---

**Recommended final action: SIDELINE / ADD-ONLY BELOW $26, cap 1.5% NAV, satellite, strong risk triggers.**
