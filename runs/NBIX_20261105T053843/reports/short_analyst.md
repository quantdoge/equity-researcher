# Short Analyst

- Symbol: NBIX
- Elapsed: 75.0s

---
I have enough to write. Additional data gaps: no peer multiples available from the feed (biotech rather than diversified pharma comparables), and Form 4 detail is limited to filing dates/insiders, not transaction direction.

---

# NBIX — Forensic Short-Seller Analysis
**Neurocrine Biosciences, Inc.** | Price $166.05 (4-Nov-26) | Mkt cap $16.81B | Net cash ~$0.35B | TTM rev $3.70B

---

## 1. Earnings Quality Assessment: **HIGH**

Let me state the conclusion up front, because it is unusual for this desk: **there is no accounting fraud here.** Every forensic tripwire I ran came back clean, and several came back unusually clean.

| Metric | Value | Read |
|---|---|---|
| Beneish M-Score (FY25) | **−2.473** | Below both the −1.78 and −2.22 thresholds → low manipulation risk |
| Accruals ratio (BS) | **−0.0657** (FY25) | Negative accruals, 4 straight years (FY22 −0.078, FY23 −0.043, FY24 −0.068) |
| Cash conversion (OCF/NI) | **1.635x** (FY25); 1.23x YTD-26 | Far above the 1.0x quality bar |
| FCF conversion | **1.564x** | Confirms cash is real, not just working-capital timing |
| Piotroski F-Score | **7/9** | Strength: all profitability, leverage, dilution tests pass |
| Altman Z-Score | **3.084** (safe zone) | Indicative only — uses book equity; on market equity it is far stronger |
| TATA component | **−0.0657** | The single most predictive Beneish input, and it is *negative* |

Beneish sub-indices show no strain: GMI 1.004 (gross margin *flat to slightly better* — no pricing-power collapse in the numbers), SGAI 0.945 (SG&A falling as a % of sales — a *positive* efficiency signal), LVGI 0.98 (leverage down), AQI 0.895. The only index above 1.1 is DSRI at 1.18, addressed below.

**Anomaly to flag:** the composite earnings-quality tool returned 43/100, which is internally inconsistent with its own inputs (1.6x cash conversion, negative accruals, 1.56x FCF conversion). I am disregarding the composite and relying on the raw ratios. Similarly, the reported FY24 interest expense of $126.6M against only $455M of debt (and $0 in FY25) is not economically coherent — I treat it as a data-feed artifact, not a red flag, but it means the FY24 income statement should not be used verbatim.

**The one honest caveat on "quality":** stock-based compensation was $217.9M in FY25 — **46% of net income** — and is running ~$235M annualised in FY26. Cash flow "beats" net income partly because SBC is a non-cash add-back that is nonetheless a genuine economic cost. SBC-adjusted FY26 FCF is ~$805M, not $1,040M, which moves EV/FCF from ~15.8x to **~20.5x**. That is a valuation adjustment, not an accounting problem.

---

## 2. Key Red Flags Found

**Flag 1 — Receivables growing at 2x revenue (the only genuine forensic flag).**
FY25: AR +43.4% vs revenue +21.5%. The AR-growth test fires `red_flag: true` for the first time in three years (FY24 was 9.1% vs 24.8%; FY23 25.5% vs 26.8%).

DSO (AR ÷ TTM revenue × 365):

| Period | DSO |
|---|---|
| FY23 | 84.9 |
| FY24 | **74.2** |
| FY25 | 87.6 |
| Q1-26 | 90.4 |
| Q2-26 | 96.0 |
| Q3-26 | **94.4** |

**~20 days of DSO expansion on a $3.7B revenue base ≈ $205M of revenue recognised but not yet collected (~5.5% of TTM revenue).** Mitigating factors that keep this yellow rather than red: (a) it is a *cash drag*, not a cash fiction — rising AR already penalised OCF, which still converted at 1.2–1.6x; (b) the Q2-26 opening of $2.7B of Soleno/VYKAT XR receivables plus two new launch products (CRENESSITY, VYKAT XR) genuinely change distributor and specialty-pharmacy terms; (c) Q3-26 change in working capital turned *positive* (+$19.9M) and Q3-26 OCF of $395M was ~1.9x net income. Conclusion: watch it, don't short on it.

**Flag 2 — Reported growth acceleration is substantially inorganic and base-effect driven.**
The revenue-deceleration screen says "accelerating" (+41% YoY in Q3-26). That headline is misleading. Q1-26's +42% was struck against a depressed Q1-25 (+11%) that absorbed the Medicare Part D gross-to-net reset — the two-year stack is ~26%/yr, not 42%. From Q2-26 onward the acceleration is M&A: goodwill and intangibles went from **$0 (Q1-26) → $2.73B (Q2-26)**, cash fell from $1.32B to $390M, and D&A jumped from $7.5M to $44M/qtr as acquisition amortisation began. Q3-26 total revenue $1,122.7M included VYKAT XR and CRENESSITY; **core INGREZZA was $801M, +17%** — decelerating from the 29% Q4-25 print. Growth is now being bought, not just earned.

**Flag 3 — New $2.69B intangible pile = future impairment and a widening GAAP/non-GAAP gap.**
Goodwill + intangibles are now **69% of shareholders' equity** ($2.69B vs $3.88B) at a company that carried essentially none a year ago. Amortisation will widen the gap between GAAP EPS and the non-GAAP figure management will now emphasise. This is the classic post-deal set-up: adjusted numbers compound, GAAP sags, and the write-down arrives 2–4 years later.

**Flag 4 — Capital allocation: $626M of buybacks, zero net share reduction.**
Buybacks: $300M (FY24) + $167.7M (FY25) + $158.1M (YT-26) ≈ $626M. Diluted shares nonetheless went from 101.0M (FY23) to **105.2M (Q3-26)**. Buybacks are entirely offsetting SBC and were executed at $140–160 — near cycle highs. This is value transfer to employees, not to shareholders.

**Flag 5 — Inventory days are structurally useless as a signal here.**
Inventory days of 483 (FY25) vs 616 (FY24) vs 352 (FY23) look alarming but are meaningless: COGS is only 1.8% of revenue ($52.1M), so the ratio is dominated by a tiny denominator. No signal either way. I am discarding it rather than spinning it — a disciplined bear must not manufacture evidence.

---

## 3. Beneish & Accruals — Detail

Full M-Score decomposition (FY25 vs FY24): DSRI 1.18, GMI 1.004, AQI 0.895, SGI 1.214, DEPI 0.837, SGAI 0.945, LVGI 0.98, TATA −0.0657 → **M = −2.473**.

Importantly, the two indices that carry the most manipulation information for a pharma are both innocent: **TATA is negative** (earnings are cash-backed) and **GMI ≈ 1.00** (2.4% COGS on $1.12B quarterly revenue, 97.6% gross margin, unchanged). Channel stuffing to hit a number would normally show up as DSRI spiking *without* a corresponding cash collection — but OCF/NI of 1.6x rules out that specific mechanism.

**Caveat on the model:** this M-Score is computed on the pre-acquisition pair (FY25/FY24). The FY26 balance sheet has been transformed by Soleno; a FY26-vs-FY25 M-Score would be distorted by the deal and should not be used as evidence either way. That is a limitation of my analysis, stated plainly.

---

## 4. Competitive Threat Assessment

This is where the bull case is genuinely fragile.

- **Single-product concentration:** INGREZZA ~$2.9B of ~$4.0B FY26E revenue (**~73%**). One molecule, one indication family (tardive dyskinesia / chorea in Huntington's), one price.
- **Live, dated pricing catalyst — the best bear catalyst I can find.** Teva's AUSTEDO/AUSTEDO XR is the direct VMAT2 competitor and has been selected for Medicare Drug Price Negotiation; its maximum fair price environment begins 2027. Neurocrine's own 10-K explicitly warns that *"lower negotiated prices for AUSTEDO and AUSTEDO XR may increase competitive pressures on INGREZZA, including heightened pricing pressure."* A VMAT2 price war starting January 2027 is not speculative — it is disclosed.
- **INGREZZA loses its own shield.** It qualified for the small-biotech exception to the Medicare negotiation programme, but 2026 formulary literature identifies valbenazine as a drug becoming eligible *because that exception expires*. Negotiated pricing therefore lands on the core asset in the 2029–2031 window.
- **Patent position is murky, and the market is already pricing it.** Core composition patent 8,039,627 runs to April 2031; settlement-driven generic entry estimates range from 2036 to 2038, with listed patents to 2040. That ambiguity is exactly why consensus revenue growth collapses from +10.5% (2028, $5.02B) to **+2.8% (2029, $5.16B)**. The cliff is priced.
- **Pipeline productivity is poor relative to spend.** R&D is ~$1.0B in FY25 (36% of revenue) and ~$1.4B annualised in FY26 — rising sharply into a pipeline with a weak hit rate (the stock has taken two ~19% single-day hits in 18 months: Aug-2024 and Feb-2025). High, rising R&D against repeated disappointments is a bear argument, not a moat.
- **Not a moat erosion story in the numbers (yet):** gross margin 97.6% and stable; no share loss visible. I will not overstate this.

---

## 5. Management & Governance Red Flags

- **Net insider selling, with the tell being the absence of buying.** Form 4 flow is heavily one-directional through 2026 (large September-15 and May-29 batches consistent with vest-and-sell and annual grants; individual sales by officers incl. CRO, Chief Corp. Affairs Officer, and director L. Norwalk). Critically, **there were no open-market insider purchases during the April-2025 collapse to $87.54** — a 43% drawdown that eight-plus directors and officers declined to buy. That is a meaningful negative signal about insider views of intrinsic value. *(Data limitation: my Form 4 feed returns filing metadata, not transaction direction or size; direction is inferred from pattern and third-party aggregators.)*
- **Promotional framing of M&A-flattered growth.** Guiding headline revenue growth while the acquired portion is the accelerant, and pivoting to non-GAAP just as acquired-intangible amortisation begins, is standard but deserves scrutiny.
- **No auditor changes, no related-party red flags, no restatements** surfaced. Governance is clean on the hard tests.
- **Capital allocation at the top of the cycle:** $2.9B cash for Soleno (VYKAT XR, Prader-Willi hyperphagia) — a high-multiple, single-asset deal closed precisely as organic INGREZZA growth decelerated from 29% to 17%. Buying growth is what managements do when they can no longer generate it.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**The bear case exists, but it is a business-model and terminal-value case, not a fraud case. And at this price it is not a good short.**

What the bear *can* say with data:
1. Growth is decelerating on the core asset (29% → 17%) and the "acceleration" is M&A.
2. A VMAT2 price war with a government-set AUSTEDO price begins January 2027 — disclosed by the company itself.
3. 73% revenue concentration in one molecule facing that price war plus IRA eligibility around 2029–2031.
4. $2.7B of fresh intangibles, 69% of equity, with impairment risk and a widening GAAP/non-GAAP gap.
5. ~$235M/yr of SBC masquerading as cash flow, and $626M of buybacks that shrank nothing.
6. ~$205M of uncollected receivables inflating reported growth.

What the bear *cannot* say: that earnings are fabricated. **Cash conversion 1.6x, negative accruals four years running, M-score −2.47, Z-score 3.08, net cash, no write-downs, no auditor issues.** The "quality of earnings" short simply does not exist.

And the valuation does not cooperate: **23.9x TTM earnings, 17.0x 2027E EPS ($9.78), 15.8x TTM FCF (20.5x SBC-adjusted), 4.4x EV/revenue, with net cash.** Consensus already models the cliff (+2.8% revenue growth in 2029). To profit shorting a 97.6%-gross-margin, net-cash, 17x-forward franchise, you need a specific negative catalyst and a compressed multiple — you have the first and not the second.

**Honest note on my own evidence:** the "cheap on 2028" argument ($12.08 EPS → 13.7x) is built on data I do not trust. The 2027 EPS range is $6.99–$13.41 (a 92% spread), and the 2028/2029/2030 estimates are internally inconsistent (2028 net income $1.63B implies ~135M shares at $12.08 EPS vs 105M actual; 2029 EPS rises while 2029 net income falls). Consensus dispersion this wide cuts both ways, but it means neither bull nor bear should lean on out-year EPS. I also could not obtain clean peer multiples — the feed returned diversified mega-pharma (LLY, JNJ, ABBV) rather than specialty-CNS biotech comparables, so my relative-valuation statement is directional only.

---

## 7. Contrarian Rating: **NO EDGE** (short thesis **rejected** on quality and valuation; tactical short only on a specific catalyst)

**Position recommendation: no short.** If forced to express the view, the only defensible structure is a *catalyst-driven, small-size, event-specific* short around (a) the January-2027 AUSTEDO maximum-fair-price implementation and the INGREZZA gross-to-net commentary that follows it, (b) any CRENESSITY or VYKAT XR launch deceleration, or (c) a pipeline readout — with a hard stop, because the base rates on 97.6%-margin franchises beating soft expectations are against you.

**What would change my mind and make this a real short:** DSO moving above ~110 days with cash conversion falling below 1.0x; a goodwill impairment on the Soleno intangibles; INGREZZA quarterly net sales declining sequentially for two consecutive quarters while management raises guidance (the classic promotional divergence); gross margin slipping below ~95%; or a credible at-risk generic launch filing.

**The other side, stated fairly:** the bull case is stronger than the bear case today. INGREZZA still grows high-teens on volume, CRENESSITY is a genuine new$1B-class franchise in congenital adrenal hyperplasia, the balance sheet is net cash, and the stock is at 17x 2027E earnings with the patent cliff already modelled by consensus. My value in this note is telling you not to run the fraud playbook against a company whose cash flow is real — reflexively bearish would have cost you 88% from the April-2025 low.
