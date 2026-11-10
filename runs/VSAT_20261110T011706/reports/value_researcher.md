# Value Researcher

- Symbol: VSAT
- Elapsed: 73.6s

---
The DCF tool returned corrupted output (it multiplied WACC by 100 — `wacc_pct: 850`), and the peer-median comparison returns a mega-cap tech set (AAPL/NVDA/MSFT) that is not a valid comparable for VSAT; I'll note both gaps and build the valuation by hand.

---

# Viasat, Inc. (NASDAQ: VSAT) — Value Investment Analysis

**Price:** ~$73–74 (Nov 2026; range of recent prints $63.95 on 11/6 → $73.23 on 11/9) · **Shares:** ~137M diluted · **Market cap:** ~$10.2B · **Net debt:** $5.11B · **EV:** ~$15.3B

---

## 1. Business Quality Assessment — Moat Rating: **Narrow (and narrowing)**

Viasat is three things bolted together: (a) a legacy GEO satellite broadband/consumer ISP, (b) an Inmarsat-derived mobility franchise (aviation IFC, maritime, government L-band), and (c) a defense/space-systems contract business (DAT segment) now under strategic review.

**Genuine moat sources:**
- **Intangible assets** — ITU-coordinated L-band and S-band spectrum rights, orbital slots, and FCC/regulatory authorizations. This is the single most valuable thing Viasat owns and is genuinely scarce.
- **Switching costs** — multi-year airline IFC contracts, installed antenna/baseband infrastructure, and government/defense security accreditations (real barriers; note the Sept 2026 $307M-ceiling Marine Corps award and NASA NEXUS win).
- **Efficient scale** — orbital slot scarcity.

**But the moat is not producing economic returns.** The decisive test is capital returns, and Viasat fails it for four consecutive years:

| FY (Mar) | ROIC | ROE | Gross margin | Op margin |
|---|---|---|---|---|
| 2026 | **0.9%** | -0.7% | 27.4% | 2.3% |
| 2025 | -0.8% | -12.4% | 33.0% | -2.2% |
| 2024 | -7.0% | -21.1% | 32.3% | -20.8% |
| 2023 | -2.4% | -15.0% | 28.2% | -6.1% |

**ROIC of ~1% against a WACC of roughly 8–9% is a 700–800bp annual destruction of capital.** A wide moat shows ROIC > WACC *consistently*; Viasat has not cleared its cost of capital once. Revenue is also no longer growing organically: +2.7% in FY2026, and the most recent quarter (Sep-2026) declined **-1.2% YoY**. Fixed broadband subscribers and maritime installations are contracting, offset only partly by aviation and DAT.

The structural threat is obvious and is the reason the moat has narrowed: **SpaceX Starlink** (and now Amazon Kuiper) attacks every Viasat end market (consumer, maritime, aviation) from a position of zero-cost launch, no legacy GEO fleet to amortize, and vastly lower cost per bit. Viasat's answer — the ViaSat-3 constellation and the proposed **Equatys** L/S-band D2D network — requires capital Viasat does not have.

**Verdict: asset-rich, returns-poor. A "narrow moat" that has been eroding for five years, not widening.**

---

## 2. Financial Quality Score: **2 / 10**

| Metric | FY2026 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|
| Revenue | $4.64B | $4.52B | $4.28B | $2.56B |
| Adj. EBITDA (approx.) | ~$1.8B | ~$1.24B | ~$0.36B | ~$0.40B |
| Net income | **-$34M** | **-$575M** | **-$1,069M** | **-$577M** |
| Reported FCF | $597M | -$122M | -$851M | -$796M |
| Capex | $993M | $1,030M | $1,539M | $1,164M |
| Owner earnings | $328M | -$244M | -$1,451M | -$1,241M |

**The reported FY2026 FCF of $597M is not what it appears.** Q3 FY2026 operating cash flow was $727M — versus $260–322M in the other three quarters — because it captured the **$568M Ligado settlement receipt**. Ex-Ligado, FY2026 underlying FCF was roughly **$30M**. The FY2027 run-rate is better but modest: $42M (Jun-26) and $78M (Sep-26) per quarter, i.e. **~$240M annualized** — versus guided capex of **$850–900M**.

**Four straight years of net losses; cumulative retained earnings have gone from +$1.32B (FY2022) to −$540M — roughly $1.9B of accumulated value destruction since the Inmarsat deal.**

**Balance sheet: the weakest element.**
- Total debt **$6.87B**, cash $1.76B, **net debt $5.11B**; net leverage ~**3.2x** Adj. EBITDA
- Interest expense **~$370M/yr** (Q2 FY2027 alone: $102M) — EBITDA/interest coverage only ~4.2x, and near-zero GAAP profit means almost no interest is tax-shielded
- Goodwill & intangibles **$3.49B = 76% of equity**. **Tangible equity is negative ~$4B.** The $4.6B book value is largely accounting residue of the Inmarsat purchase, not recoverable capital.
- FY2027 capex guidance offers the one real positive: the capex cliff is finally arriving ($1.54B in FY2024 → ~$875M mid-point), which mechanically lifts FCF.

**FCF conversion (FCF/net income) is meaningless here and negative in 3 of 4 years — a clear fail on the >80% test.**

---

## 3. Valuation Analysis

*(Note: the automated DCF tool returned corrupted output — WACC was applied as 850% — and the peer-median comparison drew mega-cap tech comparables (AAPL, NVDA, MSFT) rather than satellite peers. Both were discarded; the valuation below is built manually from reported figures.)*

**Current multiples:** EV/EBITDA ~**9.8x** on FY2027E Adj. EBITDA of ~$1.55B · P/B **2.12x** (on book that is 76% goodwill) · FCF yield 5.9% *only if you count the one-time Ligado inflow* (underlying ~2.4%) · **forward adjusted P/E ~250x** (consensus FY2027 adj. EPS ~$0.30). Trailing GAAP earnings are negative.

**A. Operating business value (no spectrum credit).** Take normalized FCF of ~$280M and apply 10–12x for a zero-growth, declining, 3.2x-levered business: **$2.8–3.4B equity → $20–25/share.** Cross-check on EV/EBITDA: 5.5x on $1.55B = $8.5B EV − $5.1B net debt = **$3.4B → $25/share.** Both methods converge on **$20–25/share**.

**B. My own DCF (8.5% WACC, FCF ramping $300M → $520M by year 5 as capex normalizes, 2.5% terminal):** EV ~$7.5B, less net debt $5.1B = **$2.4B equity → ~$18/share.** Operating value is modest and highly sensitive to WACC because debt is 2x the equity value.

**C. The spectrum option.** The entire gap between $20 and $74 is a call option on Viasat's ~68 MHz of L/S-band spectrum, benchmarked to **EchoStar's $17B sale of 50–65 MHz of AWS-4/H-block to SpaceX** (Sept 2026), which some commentary values at "up to $15B" for Viasat. I would discount this heavily:
- EchoStar's band is **US terrestrial, directly deployable for D2D**. Viasat's core L-band is **MSS/global, encumbered** by federal incumbents, Ligado coordination obligations, and ITU constraints — it is not a like-for-like comp.
- Realizing it requires a buyer, FCC approval, and multi-year clearing. Management, asked directly in Nov 2026, **explicitly declined to commit to a separation or a spectrum sale**, calling the DAT review "ongoing."
- Any proceeds are shared with bondholders at 3.2x leverage.
- Equatys (the value-maximizing use) needs billions in funding Viasat doesn't have.

Probability-weighting (say 30–35% × $12B, discounted four years at 10%, net of tax/NOLs) yields roughly **$2.4B → ~$17/share.**

**Sum-of-parts intrinsic value: ~$40/share base case.**
- **Bear (~$10–15):** spectrum proves unmonetizable; Starlink takes aviation share; EBITDA erodes.
- **Base (~$40):** operating stub $22 + probability-weighted spectrum $17.
- **Bull (~$90–110):** full-spectrum sale at EchoStar-like pricing plus a DAT separation.

**At $73–74 you are paying approximately the bull case in full, with a 45% premium to base-case intrinsic value. There is no margin of safety — there is a margin of speculation.**

---

## 4. Management Quality Assessment — **Mixed (5/10)**

**Positives:** Mark Dankberg is a genuine founder-operator (CEO since co-founding in 1986), technically exceptional, with meaningful personal ownership and no empire-building via dividends or buybacks that the balance sheet can't support (zero dividend, trivial repurchases). Recent behavior is disciplined and shareholder-aware: capex cut from $1.54B to ~$875M, cost actions, a public strategic review of the DAT segment, and candid disclosure (management openly acknowledged the fixed-broadband and maritime shortfalls in the Q2 FY2027 call rather than hiding them).

**Negatives — and they are serious:** the **Inmarsat acquisition (May 2023)** is a textbook case of capital misallocation at the cycle top. It took revenue from $2.56B to $4.28B but:
- share count from **73M → 135M (+85% dilution)**,
- debt from **$2.78B → $7.64B**,
- net income from -$577M to **-$1,069M**, with billions of goodwill subsequently impaired,
- and it was announced into the teeth of the Starlink build-out.

That single decision is why ROIC went from marginally negative to structurally below WACC. The Equatys concept, if pursued at scale, would risk repeating the pattern. **Insider alignment is real; capital allocation judgment is not yet demonstrated.**

---

## 5. Investment Verdict: **SELL** (or avoid outright)

Reasoning in Buffett terms:
1. **Outside the circle of competence in the way that matters.** I can underwrite Viasat's cash flows; I cannot underwrite the FCC's and a hypothetical buyer's valuation of encumbered MSS spectrum. When more than half the market price rests on a regulatory/strategic binary, that is a trade, not an investment.
2. **The moat does not earn its keep.** ROIC ~1% vs WACC ~8.5%, for four straight years. A widening moat does not look like this.
3. **The balance sheet removes the margin of safety.** $5.1B net debt against negative tangible equity means bondholders, not shareholders, own the first claim on any spectrum windfall.
4. **The price is at the top of a 10x, momentum-driven move** ($7 in Nov-2024 → $90 in mid-2026) that coincided with exactly the kind of external re-rating (SpaceX/EchoStar spectrum comps) that is most likely to mean-revert. Analyst targets ($49 Barclays → $140 Oppenheimer) span 3x, which is an admission that no one is anchoring to earnings.
5. **The business is shrinking.** Revenue -1.2% YoY in the latest quarter, in an industry with a 22% CAGR in D2D. Viasat is on the wrong side of that growth curve.

An existing holder treating VSAT as a small, sized-to-zero, event-driven call option on spectrum is defensible. As a *value investment* at $74, it fails every one of my tests. **Sell into strength; revisit below ~$35–40, which is where the operating business alone would offer a genuine margin of safety.**

---

## 6. Key Risks to the Value Thesis (i.e., how I could be wrong)

1. **Spectrum monetization at EchoStar-like value** — a $10–15B transaction would make equity worth $70–110/share almost regardless of operating performance. This is the single largest upside risk and is genuinely non-zero.
2. **DAT separation/spin** — a clean split could re-rate the defense/space-systems business at government-contractor multiples (15x+ EBITDA), which is not reflected in today's consolidated multiple.
3. **ViaSat-3 F2 (in service Sept 2026) and F3 capacity ramp** — incremental bandwidth per platform could restore aviation/mobility EBITDA growth and flip the revenue trajectory.
4. **Capex cliff → FCF inflection** — if capex falls toward $600M by FY2029, FCF could reach $600–700M, supporting a materially higher stub value than my $25/share.
5. **Refinancing risk cuts both ways** — a successful debt paydown from asset sales de-risks the equity sharply.
6. **Short positioning and momentum** — high short interest in a name with a binary catalyst produces violent squeezes unrelated to fundamentals.

**Principal downside risks:** Starlink/Kuiper aviation and maritime share loss; an equity raise or convert to fund Equatys; refinancing at 7–8%; further goodwill impairment; and the strategic review concluding with no transaction.

---

**Data gaps to disclose:** insider ownership percentage, senior note maturity schedule, segment-level EBITDA, and satellite-industry peer multiples (IRDM/ASTS/EchoStar) were not retrievable within budget; the built-in DCF and peer-comparison tools returned invalid output and were replaced with manual calculations. All conclusions above rely on reported financials through the quarter ended **September 30, 2026** and public commentary through **November 9, 2026**.
