# Geo Legal Researcher

- Symbol: CRWV
- Elapsed: 55.4s

---
# CoreWeave, Inc. (CRWV) — Geopolitical & Legal Risk Assessment

**Prepared for:** Investment Committee | **Data as of:** Nov 12, 2026 (latest filings: 10-Q filed 11/12/26; FY2025 10-K filed 3/2/26; Q3'26 results 11/11/26)

**Framing note:** CoreWeave is a *domestic-regulatory* risk story, not a classic emerging-market/sanctions story. ~88% of long-lived assets and ~90% of headcount sit in the US, and essentially all disclosed material customers (Microsoft, OpenAI, Meta, NVIDIA, Jane Street) are US-domiciled. Country/sovereign risk is low; **sub-sovereign (state, county, utility) risk is high and rising.** That distinction drives the rating at the bottom.

---

## 1. Geographic Risk Map

No country-level revenue table was retrievable (company reports **one operating segment**; filings disaggregate by geography but the figures sit inside documents where my SEC direct fetch was blocked — 403). I use **long-lived-asset share** (filed) and **capacity/power commitments** as exposure proxies and flag this as an explicit data gap.

| Geography | Exposure (proxy) | Source | Risk |
|---|---|---|---|
| **United States** | **88% of long-lived assets** (6/30/26 & 12/31/25; 90% at 12/31/24); 1,967 of 2,189 employees at 12/31/25; essentially all revenue billed to US counterparties | FY2025 10-K; Q2'26 10-Q | **Medium-High (rising)** — state permitting pause, AG probe, local moratoria |
| **United Kingdom** | <10% of long-lived assets; European HQ in London; part of 6-country estate | 10-K; Q2'26 10-Q ("US, Canada, Europe and United Kingdom") | Low-Medium — UK AI/data policy, energy grid queue |
| **Continental Europe (EU)** | <10%; Denmark capacity added 2026; EUR 2.0bn 8.50% notes due 2032 issued June 2026 | 10-K; 8-K 6/18/26; coreweave.com | Low-Medium — GDPR/EU AI Act, data-sovereignty, EUR funding |
| **Canada** | <10%; added to footprint disclosure in Q2'26 (not in 10-K) | Q2'26 10-Q | Low |
| **Indonesia (APAC)** | **0% of current revenue**; 360 MW contracted across 3 owned/operated sites (announced Aug 2026, ~18 months to energize) | Reuters 8/4/26; CoreWeave press release | **Medium-High** — EM permitting, grid, land, FX, rule-of-law on a greenfield first-of-kind build |
| **China / Russia / sanctioned states** | **Nil direct revenue or operations identified.** Indirect: NVIDIA GPU and memory/storage supply chain | 10-K supplier concentration | Low direct / Medium indirect (see Risk 3) |

**Concentration context:** >1 GW of power contracted outside the US, and management expects international to become "a major driver of growth." This means the exposure mix **shifts toward higher-risk jurisdictions over 2027–2030** even as revenue stays US-billed.

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — US state/local permitting and anti-data-center politics (PROBABILITY: High / occurring; IMPACT: High)
This is the single most material geopolitical factor and it is already biting.

- **Texas:** Gov. Abbott directed TCEQ on **Sept 21, 2026** to halt *all* data center permits until ERCOT completes its grid/water audit — no stated endpoint. ERCOT's report is due **on or before Dec 10, 2026**; TCEQ compliance report due Oct 19, 2026 (Beveridge & Diamond, 9/29/26).
- **Texas AG opened an investigation** into data center developments (Sept 24, 2026) over water-use reporting compliance; TWDB enforcement directed Sept 14.
- **Political regime change:** Texas has a **governor-elect (Gina Hinojosa)**; CoreWeave's CEO has already written to her asking that already-permitted projects be allowed to finish and offering to help draft rules (Quartz/biggo, Nov 2026). A company lobbying a governor-elect pre-inauguration is a tell on severity.
- **New York:** Executive Order No. 62 (Hochul, **July 14, 2026**) — first statewide moratorium, one-year pause on discretionary permits for facilities consuming ≥50 MW (governor.ny.gov; Reuters 7/14/26). Disclosed as a new item in the Q2'26 10-Q risk factor.
- **Local:** 100+ Texas local ordinances since July 2025; Denton moratorium proceedings (relevant given CoreWeave's Denton campus).
- **Quantified impact:** sell-side estimate — a one-year delay on **400 MW in Texas ≈ $1.4bn** of revenue at ~$11M revenue/MW/yr; Denton judged "largely insulated" because permits are held (Seeking Alpha, 11/12/26). Post-midterm, CNN (11/5/26) reports hundreds of projects awaiting permits, utility service or tax incentives are "particularly exposed."

**Investment read:** this is a **schedule risk to contracted backlog**, not a demand risk — and schedule risk on 98%-committed revenue converts directly into the securities-litigation theory below.

### Risk 2 — Counterparty concentration fused with partner-side regulatory risk (PROBABILITY: Medium / IMPACT: Very High)
- **Microsoft = ~67% of FY2025 revenue** (named in Item 1A). Largest customer 36% in Q2'26, second 26%, third 10% — concentration is easing but remains extreme.
- **NVIDIA sits on four sides of the trade:** sole GPU supplier, 10%+ shareholder ($2bn, 22.9M shares at $87.20, Jan 2026), customer ($6.3bn order form to April 2032), **and obligated buyer of CoreWeave's residual unsold capacity through 4/13/2032**. That structure is a magnet for antitrust/related-party/accounting scrutiny.
- **Sector-wide antitrust attention:** DOJ and FTC have active probes touching NVIDIA, OpenAI and Microsoft. No CoreWeave-specific investigation was found — but CoreWeave's revenue is a derivative of those counterparties' regulatory standing.
- NVIDIA-linked contagion is already a demonstrated transmission channel (Barron's, 11/12/26: "NVIDIA AI Contagion"; CRWV fell ~9–10% on peer/partner news).

### Risk 3 — Export controls & hardware supply chokepoints (PROBABILITY: Medium / IMPACT: High)
- **100% of GPUs are NVIDIA**; supplier concentration was 23%/20%/17% of purchases in FY2025. The Q2'26 10-Q *added* risk language on storage and memory component supply and on the cost of moving off NVIDIA.
- **Policy direction is unstable:** BIS now reviews H200/AMD MI325X-class licenses to China **case-by-case**; the live frontier is **remote-access/IaaS rules** — measures that would impose know-your-customer and end-use obligations on cloud providers serving foreign users. CoreWeave, as an IaaS provider expanding into Indonesia and Europe, is squarely in the scope of any such rule. Direct China revenue: none identified.
- **Tariffs** on imported compute hardware are a cost/variance risk not separately quantified in filings.

---

## 3. Legal & Regulatory Highlights

**Securities class action (the main legal contingency).** Filed **Jan 12, 2026, District of New Jersey** against CoreWeave and certain executives; class period **Mar 28, 2025 – Dec 15, 2025**; §§10(b)/20(a) and Rule 10b-5. Allegations: overstated ability to meet demand, understated reliance on a **single third-party data center developer**, after the Nov 10, 2025 guidance cut (WSJ Dec 15, 2025 exposé). **Lead plaintiff deadline Mar 13, 2026** (Rosen, Berger Montague, Hagens Berman, Pomerantz, KTMC et al.). Q4'25 loss cited at **$452M** with soft guidance. Notably, the 10-K **changed the litigation risk factor from "we may become involved" to "we are involved,"** naming the actions (D&O Diary, 1/14/26; AlphaSpread 3/6/26).

**SOX / internal control.** **Material weaknesses continued to exist at June 30, 2026**, with six remediation actions listed — a live disclosure-controls compliance gap that compounds litigation exposure.

**Debt covenants (contractual-legal risk).** $35.6bn total indebtedness at 6/30/26; liabilities 93.5% of assets; **debt service of ~$6.2bn in H1'26 vs $3.7bn operating cash flow**. DDTL facilities carry 1.15x–1.40x debt-service-coverage tests; DDTL 3.0 was **amended Dec 31, 2025** to postpone the first DSC test to Oct 31, 2027, cut minimum liquidity to $100M, and permit **unlimited equity cures before Oct 28, 2026**. Facilities contain **cross-default triggers tied to material customer contracts** — legal linkage between customer and creditor risk.

**M&A.** Core Scientific merger **terminated Oct 30, 2025** after stockholders failed to approve; **$270M termination fee payable by Core Scientific** in specified circumstances. No litigation arising was identified.

**Regulatory/administrative.** Texas AG investigation (water-use reporting, opened 9/24/26); NY EO 62; ERCOT/PUCT information requests (State & Community Impact RFI due 10/12/26; failure to respond is reported to PUCT and the Governor's office).

**No FCPA, OFAC/sanctions, AML, or bribery matters were identified** in filings, news, or enforcement searches. Disclosure-control and permitting risk, not corruption risk, is the exposure.

---

## 4. Compliance Red Flags

1. **Material weaknesses persisting through Q2'26** — with a securities class action alleging disclosure failures, this is the most legally dangerous combination on the sheet.
2. **Export-control/KYC build-out lag.** Contracting 1+ GW abroad (Indonesia first) ahead of any remote-access/end-use customer-screening regime creates a rules-readiness gap.
3. **Related-party optics with NVIDIA** (supplier + shareholder + customer + residual-capacity guarantor) — audit-committee and, in a stressed scenario, congressional/antitrust attention.
4. **Public-disclosure exposure on water/power.** State AG and ERCOT RFIs demand notarized attestations on water, power, ownership and incentives; inconsistent statements to regulators are actionable.
5. **Data privacy/EU AI Act + GDPR** across UK/EU expansion; the 10-K specifically broadened this risk factor to add **AI** to regulated data subjects.
6. **Covenant-linked equity cures** create incentive to raise equity at unfavorable prices — a governance flag for minority holders.

---

## 5. Overall Geopolitical/Legal Risk Rating: **HIGH**

**Rationale.** Sovereign/sanctions/FCPA risk is genuinely **low** — this is a US-domiciled company with no China, Russia or sanctioned-market revenue. But the rating rests on four converging factors: (i) an **active, adversarial US state-level regulatory environment** that changed regimes in the last quarter and is directly delaying contracted revenue; (ii) an **unresolved securities class action** targeting precisely the disclosure that the permitting situation puts under stress; (iii) **67% single-customer concentration** to a counterparty that is itself under antitrust scrutiny; and (iv) **contractual-covenant fragility** (93.5% liabilities/assets) that converts operational slippage into legal default risk.

**What would change the rating:**
- **Upgrade to Medium:** ERCOT report (by Dec 10, 2026) leads to resumed TCEQ permitting; Texas governor-elect ratifies already-permitted projects; class action dismissed or settled within insurance limits; Microsoft concentration sustained below ~35%.
- **Downgrade to Very High:** adverse ruling/survival of the 10b-5 claim past motion to dismiss; a formal DOJ/FTC inquiry into the NVIDIA–CoreWeave capacity-backstop arrangement; a second state adopting a ≥50 MW moratorium covering an existing CoreWeave campus; or a covenant test failure requiring an equity cure.

**Key gaps:** country-level revenue split not obtained (SEC direct fetch blocked, 403); no CoreWeave-specific government investigation confirmed beyond the Texas AG's sector-wide data center probe; Indonesian project economics/permitting status unverified beyond the announcement.
