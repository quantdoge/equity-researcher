# Short Analyst

- Symbol: INSM
- Elapsed: 112.8s

---
I have enough to complete the forensics. One note: no pure-play comparables were available (the sector tool returned mega-caps like LLY/JNJ/AZN), so peer-multiple work is done off INSM's own history rather than a comp set.

---

# INSM — Forensic Short-Seller Analysis

**Price $111.59 · Market cap $24.4B · EV ~$24.8B · FY25 revenue $606M · Down 47% from $211 high (Dec 2025)**

---

## 1. Earnings Quality Assessment: **MEDIUM** (no manipulation signature — but low absolute quality)

Important framing: INSM is a commercial-stage launch story, not a fraud candidate. The classic quality metrics are largely inapplicable to a company that is deliberately loss-making during a launch. What matters is whether the *accounting* is clean, and it substantially is.

The one genuine quality complaint is **stock-based compensation and adjusted metrics**: SBC ran $41.2M in Q3 2026 (~$165M/yr, ~8% of annualised revenue). The company's adjusted EPS excludes it, which flatters the "path to profitability" narrative. Q2 2026 GAAP loss was only $13.2M (−$0.06) versus an adjusted loss of $0.52 — GAAP came in *better* than adjusted, implying a ~$100M non-operating gain in that quarter. That divergence direction is unusual and worth an analyst's attention.

Also note the headline operating-line volatility is distorted by milestone/IPR&D charges. I estimate R&D was ~$107M in Q2 2026 and ~$274M in Q3 2026 — a $167M one-quarter jump that explains why operating loss widened from −$1.5M to −$89.4M despite $99M more revenue. That timing most likely reflects launch milestones (Japan approval Aug 2026) and is non-run-rate. **This cuts both ways: it means the bulls' "breakeven is imminent" claim is closer to right than GAAP suggests, and it means bears who read the headline operating loss as deterioration are wrong.**

## 2. Key Red Flags Found

| # | Flag | Data | Verdict |
|---|---|---|---|
| 1 | **Receivables outgrowing revenue** | FY25 AR +170.8% vs revenue +66.7%; flagged in all three years | **FALSE POSITIVE** — see §3 |
| 2 | **Dilution** | 140.4M shares (2023) → 164.0M (2024) → 213.6M (2025) → 218.8M (Q3'26). +56% in three years, +12% in nine months | **REAL** — severe per-share value leakage |
| 3 | **CFO departure** | Sara Bonstein stepped down effective Oct 30, 2026 — one day after reporting Q3 | **REAL, MODERATE** |
| 4 | **Inventory** | $163.9M, ~191 days (down from 386 in FY25, 463 in FY23) | **BENIGN** — but note inventory build now *lagging* sales = stock-out risk |
| 5 | **Extreme estimate dispersion** | 2028E EPS range $0.24–$6.55 (27x spread across 17 analysts); only 7 analysts model 2030 | **REAL** — long-dated consensus is low-conviction |
| 6 | **No insider open-market purchases** | 25 Form 4s in five months, clustered at May 15 / Jun 5 / Oct 20; zero buys during a 47% drawdown | **REAL but weak** — direction not confirmed by source; vesting clusters likely |
| 7 | **Altman Z −3.955 "distress"** | — | **NOT MEANINGFUL** — book-equity artifact of a $5.9B accumulated deficit; $1.15B cash vs $741M debt |

## 3. Beneish M-Score and Accruals Analysis

**M-Score −1.96** — sits in the "moderate risk" band (−1.78 to −2.22). I am rejecting the manipulation reading. Decomposing the score:

- **SGI 1.667** and **DSRI 1.624** are the sole drivers. Both are mechanical artifacts of a launch where quarterly revenue rose 6x in five quarters. High sales-growth index inflates M-Score by construction in hyper-growth companies.
- **TATA −0.1509** — *negative* total accruals, which is the conservative direction. The accounting loss is *larger* than cash burn.
- **GMI 0.962** — gross margin **improving** (79.4% FY25 → 85.1% Q3 2026).
- **LVGI 0.784** — leverage falling (debt $1.31B → $741M).
- **AQI 1.028, SGAI 0.912, DEPI 0.823** — no asset-quality, SG&A-capitalisation, or depreciation-extension games.

**Receivables test (my own, not the screw):** DSO = AR ÷ quarterly revenue × 91:
Q4'24 45.3 → Q3'25 41.7 → Q4'25 48.6 → Q1'26 53.1 → Q2'26 46.0 → **Q3'26 45.0**

DSO is flat at ~45–53 days. There is **no channel-stuffing signal.** The 170% AR growth is arithmetic: a quarter with 2.5x the prior year's revenue carries 2.5x the receivable. Same for the pipeline: CSL Behring/Specialty pharmacy distribution for an $88,000 drug carries structurally longer terms than ARIKAYCE. **I cannot support a channel-stuffing or revenue-recognition short thesis on this data.**

**Accruals ratio −0.151 (FY25), −0.160 (2023):** negative, i.e. cash burn *below* accounting loss. Cash conversion 0.73x and FCF conversion 0.76x — poor only because the denominator (net income) is a loss inflated by non-cash IPR&D. The composite quality score of 25/100 is a loss-maker artifact, not evidence of manipulation.

## 4. Competitive Threat Assessment

This is where the bear case has genuine merit, and it is **narrower than bears claim but deeper than bulls admit.**

**The pricing problem is the central risk.** Brinsupri's annual pricing is reported at ~$88,000 per patient in a **chronic, non-fatal** disease with a large eligible population. Launch-year gross-to-net is flattered by copay support and free-drug/temporary-distribution programs. As the payer mix rotates from commercial to Medicare Part D / Medicaid and copay support rolls off,
net price per script erodes. Consensus models assume price *durability* for a decade. That is the single largest modelling assumption I would attack.

**The structural price cliff is under-appreciated.** Brinsupri is an **oral small molecule**. Under the IRA it faces Medicare negotiation seven years post-approval (selected ~2032, effective ~2034) — versus eleven years for a biologic. A drug generating the majority of revenue from Medicare-age bronchiectasis patients will meet the IRA's clock while consensus 2030 estimates are still being marked up.

**Pipeline-in-a-product got a hole punched in it.** The December 2025 discontinuation of the CRSsNP (chronic rhinosinusitis) program took the stock down 16% and removed the "brensocatib is a platform" optionality that underpins the 2030 numbers. DPP1 inhibition in one airway indication does not de-risk the next.

**TPIP vs. sotatercept.** TPIP's PAH opportunity is being crowded out by Merck's Winrevair, which has reset the PAH treatment paradigm. Bulls blend TPIP into the sum-of-parts; it is a late entrant in a market with a dominant new mechanism.

**Field competition.** Verona's Ohtuvayre (ensifentrine) is in a Phase 2 NCFB study and competes for the identical pulmonology call point with a growing COPD franchise. Fifteen-plus competitors are in the NCFB pipeline.

**Offsets I must concede:** first-and-only FDA approval, positive Phase 3b ENCORE data, Japan approval and October 2026 launch (new geography, new price), and 85% gross margins that are *expanding* — the opposite of moat erosion.

## 5. Management Red Flags

The CFO transition is the one I would put in front of an IC. Bonstein departs the day after the Q3 print, at the precise inflection point from cash-burn to profitability, with no disclosed successor. That is not proof of a dispute — it may simply be a life-sciences CFO moving on after six years — but a CFO exit exactly as the financial narrative turns is a pattern worth monitoring, particularly alongside a 12% nine-month share count increase and heavy use of adjusted metrics.

No insider open-market buying during a 47% drawdown is a mild negative signal; no auditor change, no restatement, no related-party concerns, and Section 302 certifications are clean.

**The central operating math:** Q3 2026 revenue $524.4M and R&D + SG&A of $527.2M — opex is still ~100% of revenue. The 2028 consensus net income of $785M on revenue of $3.82B requires opex to grow only ~14% over two years while revenue grows 58%. Achievable in a launch, but it is an *assumption*, not a trend.

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a valuation/expectations short, not an accounting short.**

Bear case: $24.8B EV on ~$1.9B of 2026E revenue (13x) and $2.91B of 2027E (8.5x) already capitalises a near-flawless run to $6.2B of 2030 revenue at ~36% net margins. A single-molecule, single-indication franchise priced at $88k/yr in a non-fatal disease, facing IRA negotiation on a small-molecule clock, G2N erosion, a failed adjacent indication, and a CFO transition, does not deserve the benefit of the doubt across four years of unproven estimates with a 27x spread on 2028 EPS.

Rough scenario work: bear (2028 revenue $3.2B at 22% net margin, 22x) ≈ **$70–75/share**; base ≈ **$105–120**; bull (consensus achieved, 28x 2028) ≈ **$150–180**.

**But the short window has largely closed.** The stock has already been cut 47% from $211. The launch is objectively working (Q3 revenue +23% QoQ, guidance raised to $1.25–1.4B for Brinsupri), the company is nearly self-funding (Q3 FCF only −$42M on $1.15B of cash against $741M of debt — no liquidity event risk), gross margins are expanding, and Payer/DSO data show no recognition games. The Altman distress score and the Beneish flag are both artifacts, and I will not invent a fraud case that the data does not support.

Risk/reward on a fresh short at $111 is roughly symmetric and the borrow carries binary pipeline risk (TPIP readouts, EU/Japan labels, IRA-adjacent policy headlines). **I would not initiate here.**

## 7. Contrarian Rating: **NO EDGE** — Reject Short Thesis (at current price)

**Re-rating triggers that would flip this to a tactical Short:** a return above ~$150–160 without a corresponding estimate increase; two consecutive quarters of decelerating sequential Brinsupri growth; disclosed gross-to-net deterioration or materially rising payer gross-to-net; a TPIP Phase 3 setback; or a successor CFO departing within 18 months.

**What would make me wrong (bull case, stated fairly):** if Brinsupri's $1.25–1.4B 2026 guide is beat and Q4 exits above a $2.5B run-rate with gross-to-net holding, the 2027–2028 estimates are too low, not too high, and this is a $180+ stock. The launch statistics are among the best in respiratory biotech history; the honest bear case rests entirely on price durability and multiple, not on the business failing.
