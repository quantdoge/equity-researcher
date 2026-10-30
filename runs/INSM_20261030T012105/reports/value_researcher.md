# Value Researcher

- Symbol: INSM
- Elapsed: 53.4s

---
## Insmed Incorporated (INSM) — Value Investment Analysis

**Data caveats up front:** The quote feed is inconsistent — the provider's latest price is **$111.59** (market cap ≈$24.5B on 219.3M shares), while the daily price series in my dataset ends 2026-02-25 at $148.61. Cross-checking analyst notes dated October 2026, the stock traded roughly **$95–$115** through that window, so I treat **~$100–112 as the current range** and use $111.59 for ratios. FY2026 figures are guidance + quarterly reporting, not audited annuals. Insider ownership and exact patent-expiry schedules were not retrievable — noted as gaps.

---

# 1. Business Quality Assessment

**Moat Rating: NARROW** (strong within one indication, not a widening franchise)

Insmed is a commercial-stage biopharma with two marketed products and a pipeline. In five years it has gone from a ~$188M-revenue single-product company to a **>$2.4B run-rate** dual-franchise company.

**BRINSUPRI (brensocatib)** — first-in-class, oral, reversible DPP1 inhibitor. Approved in the US (Aug 2025) as **the first and only treatment ever approved for non-cystic fibrosis bronchiectasis (NCFB)**, in the EU (Nov 2025) and Japan (Oct 2026). This is a textbook intangible-asset moat: a first-mover in a large, previously untreated orphan-like population, protected by 12-year US NCE exclusivity (to ~2037) and 10-year EU exclusivity, with pulmonologist prescribing relationships and chronic-therapy persistence creating moderate switching costs.
- Commercial proof: $172.7M in partial-year 2025 → **$400.1M in Q3'26 alone (+29% QoQ)** → FY2026 guidance $1.35–1.4B. That is one of the fastest rare-disease launches on record.

**ARIKAYCE (amikacin liposome inhalation)** — FY2025 $433.8M (+19%), FY2026 guide $460–470M. The **ENCORE Phase 3b readout (March 2026) was positive** (87.8% vs 57.0% culture conversion), with an sNDA under FDA priority review and a **PDUFA date of January 28, 2027** to expand the label from refractory-only to *all* MAC lung disease patients — a genuine 3–4x patient-population step-up.

**Why only Narrow, not Wide:**
- **The platform thesis narrowed in the last 12 months.** A Phase 2b sinus study failed (Dec 2025) and the **CEDAR Phase 2b study in hidradenitis suppurativa failed outright (April 2026), and the program was terminated.** DPP1 inhibition does not generalize. Essentially all economic value is now concentrated in NCFB.
- **Duplicable market.** NCFB is large, validated and now de-risked — an open invitation to competitors. First-mover advantage is real but not permanent.
- **No demonstrated excess returns on capital.** ROIC has been **-78%** (2025), **-55%** (2024), **-81%** (2023). A moat that has never yet produced a positive return on capital is a *claim* on future returns, not a proven one.
- Hard exclusivity cliff in 2035–2037 bounds the terminal value by construction.

---

# 2. Financial Quality Score: **3.5 / 10**

*(Would be 7–8 if management delivers on its 2027 cash-flow-positive target — the score reflects the present, not the hope.)*

| Metric | FY2023 | FY2024 | FY2025 | Q3 2026 |
|---|---|---|---|---|
| Revenue | $305.2M | $363.7M | $606.4M | $524.4M (qtr) |
| Growth | +24.4% | +19.2% | **+66.7%** | +268% YoY |
| Gross margin | 78.5% | 76.4% | **79.4%** | ~80%+ |
| Operating margin | -232% | -241% | **-194%** | improving |
| Net income | -$749.6M | -$913.8M | -$1,277M | -$100.3M (qtr) |
| Free cash flow | -$549.5M | -$705.8M | **-$967.6M** | — |
| SBC | $74.8M | $96.8M | $152.7M | — |
| Diluted shares | 140.4M | 164.0M | **213.6M** | 219.3M |

**What is genuinely good:** 29.8% five-year revenue CAGR accelerating to triple digits; ~80% gross margins (proper proprietary-drug economics); a clean-ish balance sheet — $1.1B cash at 9/30/26 against $545M long-term debt plus $156M royalty financing, i.e. roughly **net cash**; debt cut from $1.31B to $545M in two years; and a dramatic narrowing of the loss (operating loss $89.4M in Q3'26 vs $366.0M a year prior). Management states cash-flow positivity is achievable in **2027 without new capital**.

**What is genuinely bad:**
- **FCF conversion is meaningless here — there is no FCF.** Buffett's 80% FCF/NI test is unanswerable; the company has burned $3.6B cumulatively and carries **-$5.6B retained earnings**.
- **Dilution is severe and per-share value-destructive:** shares outstanding up **~95% since 2021** (112.1M → 219.3M), including **+30% in 2025 alone**. Gross franchise value has grown fast enough to outrun it, but shareholders own roughly half the company they did five years ago.
- P/B of 32x, negative P/E, negative P/FCF — every conventional quality signal is absent.

**Verdict on financial quality:** an outstanding *growth* profile attached to a still-unproven *profitability* profile. Not yet an investment-grade business by my standards.

---

# 3. Valuation Analysis

At $111.59: market cap ≈$24.5B, enterprise value ≈$24B. Against **FY2026E revenue of ~$1.84B** (BRINSUPRI $1.35–1.4B + ARIKAYCE $460–470M), that is **~13x forward revenue**; against a ~$2.7B FY2027E, ~9x. Negative earnings multiples make screen-based comparison useless, and `compare_peer_valuations` returned only mega-cap pharma (LLY, JNJ, ABBV) — no informative comps.

**Scenario framework** (probability-weighted, 10-year horizon, 10% discount rate, exit multiple on post-2035 earnings, 240–250M diluted shares):

| Scenario | Weight | Assumptions | Intrinsic value |
|---|---|---|---|
| **Bear** | 30% | NCFB penetration disappoints (payer step-edits, IRA negotiation from ~2030, competitive entrants); BRINSUPRI peak ~$2.5B; ARIKAYCE ~$600M; TPIP fails; pipeline written to zero | **~$50–60** |
| **Base** | 45% | BRINSUPRI peak ~$5B global; ARIKAYCE ~$800M post-ENCORE; TPIP reaches ~$1B in PAH/PH-ILD; 30% peak net margin; 15–16x exit | **~$105–115** |
| **Bull** | 25% | BRINSUPRI peak $7.5B+, TPIP $2B, one pipeline asset succeeds; 33% net margin; 18x exit | **~$170–185** |

**Probability-weighted intrinsic value ≈ $108–112 per share.**

**Current price (~$111) sits essentially at intrinsic value — zero margin of safety.** Even the bull case offers only ~55–60% upside against a bear case of ~50% downside: risk/reward is roughly symmetric, which is not what I am paid to take.

**Where I differ from the sell side:** analyst targets cluster at **$154–$218 (median ~$195, implying +70%)**. Those targets capitalize peak sales at premium multiples without probability-weight
