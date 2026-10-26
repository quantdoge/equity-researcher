# Esg Analyst

- Symbol: NET
- Elapsed: 194.5s

---
# ESG ANALYSIS — CLOUDFLARE, INC. (NYSE: NET)

**Sector:** Technology / Software – Infrastructure | **HQ:** San Francisco, US | **Employees:** ~5,156 | **Market cap:** ~$117.6B | **Last close:** $330.22 (26-Oct-2026) | **Beta:** 1.65

**Data quality note (read first):** No 10-K or 10-Q was retrievable for NET through the filing tool (both returned "not found"), so risk-factor language is drawn from the 2026 DEF 14A summary, the Delaware Chancery record, and secondary sources. Peer/emissions data is third-party modelled (DitchCarbon), not audited CDP disclosure. I have flagged every figure that is estimated rather than reported. Cloudflare does not publish a CDP climate score, EcoVadis rating, or audited SASB index that I could locate — that absence is itself a finding.

---

## 1. ESG Materiality Map

Ranked by financial materiality to cash flow, cost of capital, and licence to operate. For an infrastructure/edge-computing company, the ESG factors that actually move valuation are **not** the ones in a typical ESG scorecard — carbon is nearly irrelevant to cash flow; governance control and regulatory/legal exposure are not.

| Rank | Factor | Pillar | Why it is material | Financial transmission channel |
|---|---|---|---|---|
| 1 | **Founder control & capital structure** | G | Dual-class 10:1 votes; recapitalisation enjoined for probable bad faith (Oct 2026); control retainable at ~20% of prior economic interest | Cost of capital, event risk, dilution, M&A optionality |
| 2 | **Shareholder rights / related-party process** | G | <18% non-founder support; auto-deleting Signal messages; special-committee credibility findings | Litigation cost, proxy risk, index/governance-driven exclusion |
| 3 | **Intermediary liability & content blocking** | S | LaLiga IP-blocking dispute in Spain; Cloudflare dismissed in Barcelona court (Mar-2025); documented collateral damage | EU market friction, legal cost, precedent risk, licence to operate |
| 4 | **Service reliability / operational resilience** | S | Global outage 18-Nov-2025 (Bot Management config bug); availability *is* the product | Churn, service credits, renewal risk |
| 5 | **Energy intensity of AI-driven network buildout** | E | Scope 3 ~43.1M kg CO₂e and flat; AI inference/crawler load rising fast; 2030 SBTi target "at risk" | Power procurement cost, customer Scope 3 procurement screens, disclosure burden |
| 6 | **EU digital-regulation compliance stack** | G/E | NIS2, DORA, CRA, CSRD, AI Act all touch an edge provider | Run-rate compliance cost, contractual terms, customer audits |
| 7 | **Cybersecurity / data privacy** | S/G | Operates as a security vendor; SEC Item 1.05 8-K exposure | Litigation, fines, reputational |
| 8 | **Human capital / D&I disclosure** | S | 5,156 FTE; tight AI talent market; no quantified diversity disclosure located | Compensation cost, attrition |
| 9 | **Board independence & comp alignment** | G | 3-member independent special committee; KPMG since 2014; evergreen cap removed (5% of outstanding) | Dilution, pay-for-performance credibility |
| 10 | **Direct carbon cost** | E | 43,300 tCO₂e total; ~$2–7M at $50–150/t internal price | **Immaterial** (~0.1–0.3% of revenue) |

**Key judgement:** this is a **governance-driven ESG story, not a climate story**. The environmental footprint is de minimis in absolute terms; the governance file contains a live, judicially-found probable breach of fiduciary good faith. That is unusual for a large-cap and deserves more weight than the carbon data.

---

## 2. Environmental Risk Assessment — **MEDIUM**

**Reported emissions (FY2025, third-party compiled):**

| Scope | FY2025 | Share | Note |
|---|---|---|---|
| Scope 1 | 198 tCO₂e | 0.5% | Trivial |
| Scope 2 (market-based) | 0 tCO₂e | 0% | 100% renewable electricity via RECs |
| Scope 3 | ~43,100 tCO₂e | 99.5% | Purchased goods/services, network hardware |
| **Total** | **~43,300 tCO₂e** | 100% | |

**Trajectory (total, million kg CO₂e):** 15.6 (2021) → 21.1 (2022) → 57.3 (2023) → 43.3 (2024) → 43.3 (2025). The 2022→2023 jump is almost certainly a Scope 3 methodology/coverage expansion rather than a real tripling; the honest read is **emissions have been flat for two years and remain ~2.8× the 2021 base**, against a 2030 target requiring a 62% cut versus 2019. That is the wrong direction of travel.

**Targets and commitments:** SBTi-validated 62% total-GHG reduction by 2030 vs 2019 — tracked at ~48% progress, flagged "at risk." Near-zero Scope 1&2 by 2025 — ~94% on track. 2040 Scope 3 intensity −50% — behind at ~22%. Of eight tracked climate commitments, **only SBTi is active**; Cloudflare is not a RE100 member, not a Climate Pledge signatory, has no EcoVadis rating, and is not on Climate Action 100.

**Peer positioning — the most useful datapoint.** DitchCarbon score 45 vs industry average 38, i.e. better than 58% of its industry but **materially behind the large-cap infrastructure peers it competes with for enterprise contracts:**

| Company | DitchCarbon score |
|---|---|
| Cisco | 100 |
| Microsoft | 94 |
| Akamai | 76 |
| Okta | 62 |
| NetApp | 61 |
| **Cloudflare** | **45** |
| Industry average | 38 |

**Intensity:** ~20 tCO₂e per $M revenue (estimated on ~$2.1B implied revenue — flag as estimate; revenue not confirmed from filings).

**Assessment.** *Direct carbon cost is immaterial* — even at an aggressive $150/t internal price, total exposure is ~$6.5M against a ~$2B+ revenue base. Physical climate risk is low (software/network, no owned manufacturing; some data-centre and water exposure in leased facilities). The **real** environmental risk is threefold: (a) **greenwashing/credibility risk** from marketing "zero emissions" while Scope 2 is zeroed by procurement of RECs and 99.5% of footprint sits in an unaddressed, flat Scope 3 line — plus the 2021 pledge to "remove all historical carbon since 2010 by 2025," which I could not verify as delivered; (b) **procurement risk** as enterprise customers with their own validated Scope 3 targets push supplier disclosure requirements into RFPs and renewals; (c) **rising energy demand** from AI crawler/inference traffic, which structurally pushes Scope 3 up while the 2030 target already looks unachievable. Rated Medium, with a High trajectory on transition/disclosure risk.

---

## 3. Social Risk Assessment — **MEDIUM**

**Positives:** The company's core product is DDoS mitigation and security for vulnerable organisations; its Project Galileo programme protects civil-society and human-rights sites at no cost, and its 2026 report on cyberattacks against civil society is genuine public-interest output. The business consistently plays a defensive role in major vulnerability events (e.g. rapid mitigation deployment during the 2026 PHP vulnerability alerts) — a real social benefit and a reputational asset. Workforce is small (5,156) and knowledge-intensive, without the supply-chain labour or product-safety exposure of a manufacturer. No labour disputes, strikes, or safety incidents located.

**Risks:**
- **Content intermediation / intermediary liability.** The LaLiga dispute is the clearest live social-licence issue. LaLiga obtained Barcelona court orders (Dec 2024) letting it compel Spanish ISPs to block IP ranges; Cloudflare's appeal was **dismissed 26-Mar-2025** (Commercial Court No. 6), and independent measurement (OONI, 2026) documents substantial collateral damage — legitimate sites caught in IP-based blocking. Bloomberg featured the story in June 2026. The reputational frame — "US company ignores illegal content" — is uncomfortable for a firm whose brand rests on being a neutral, protective layer. Precedent risk across EU member states is the material concern, not the Spanish revenue.
- **Operational reliability.** The 18-Nov-2025 global outage, triggered by a Bot Management configuration-generation bug, is the most financially relevant social/product-safety event: for an availability vendor, a global outage is a direct hit to the trust that justifies the contract. Cost is unquantified but transmitted through credits, churn, and slower enterprise sales cycles. Note this recurs — Cloudflare has had prior global incidents.
- **Human capital / D&I disclosure gap.** I could not locate quantified gender or racial representation data, attrition, or pay-gap figures in accessible sources; commentary is qualitative ("meaningful progress"). Given 10-K human-capital disclosure norms, this is a moderate transparency gap rather than evidence of a poor record — but I cannot rate what I cannot measure. Talent retention in an AI-compensation arms race is the financial channel.
- **Governance-adjacent social issue.** The JLens Network (values-based investor) publicly urged shareholders to **withhold votes on directors Michelle Zatlyn and Scott Sandell** at the 30-Jun-2026 AGM — evidence that the founder-control structure is now attracting organised opposition on values/governance grounds, not just proxy-advisor grounds.

Rated **Medium**: no severe harm events, genuine public-interest positives, but unresolved intermediary-liability litigation and a demonstrated reliability failure in the core product.

---

## 4. Governance Quality Score — **4 / 10**

**This is the weakest pillar by a wide margin and the core of the ESG view.**

**Structural issues:**
- **Dual-class control.** Class B shares carry 10 votes. Founders Matthew Prince (CEO) and Michelle Zatlyn held combined voting power of **60% in 2021, down to 50.3% in June 2026**, and were projected to lose majority control by December 2026 without action. Prince serves as **CEO and Chair** — combined roles with no separation. Zatlyn is co-founder/co-chair; Scott Sandell is Lead Independent Director (a partial mitigant).
- **The recapitalisation, and the injunction.** A three-member special governance committee (formed Oct 2025, all independent and disinterested, with own counsel and adviser) ran a six-month, 18-meeting process and approved a structure converting each Class B share into one Class A plus preferred stock carrying **nine votes**, plus a non-voting Class C distribution allowing founders to sell without losing votes. The preferred redemption trigger — founders' Class A falling below 40% of post-exchange holdings — **excludes Class C**, so founders could cut economic interest to ~20% of its prior level while retaining control. Plaintiffs estimated this permitted **~$2.1B in additional founder sales** before losing control. The deal passed on founder votes with **less than 18% support from other stockholders' voting power.**
- **On 16-Oct-2026, Vice Chancellor Laster of the Delaware Court of Chancery preliminarily enjoined the recapitalisation**, finding a reasonable probability the special committee did **not act in good faith** under amended DGCL §144 — despite being disinterested and unlikely to have been gross negligent. The court cited adviser notes about developing "a narrative" and creating "a good fact pattern," an expert retained whose partner signalled sympathy before learning the company's identity, Prince's resignation threat after which two non-committee directors joined a committee meeting, and — most damaging — **auto-deleting Signal messages** producing adverse inferences from record gaps. Defendants won the statutory-interpretation points and may still establish the safe harbour at an expedited trial. The ruling is preliminary, not a finding of bad faith.
- **Compensation/dilution.** The restated 2019 Equity Incentive Plan **removes the fixed cap on annual evergreen increases**, moving to the lesser of 5% of outstanding shares or a committee-set number from FY2027. At a $117.6B market cap, 5% represents roughly **$5.9B of annual dilution authority** — a material and underappreciated transfer from shareholders. Say-on-Pay is on the ballot; prior-year support was described as high (specific percentage not disclosed in accessible sources).

**Mitigants (why not lower than 4):** board graded **B+**; genuine independent committee with independent advisers; the new charter would *require* a majority of independent directors and independent-director approval for Class C issuances above $100M; capital-at-risk and continuing-service conditions on founder control; KPMG as auditor since 2014 with audit-committee pre-approval; 1-year TSR +52.6% gives management credibility with holders; a third-party acquisition proposal was explicitly not jeopardised by the injunction.

**Why 4/10:** A judicially-found *reasonable probability* of bad faith in a related-party control transaction, combined with destroyed contemporaneous records and sub-18% minority support, is a severe governance signal. The company's defence — "we ran a long, well-advised process" — is precisely what the court rejected. Mitigants are real but prospective. Score would rise to 6–7 on a clean expedited-trial win with the governance concessions intact, or on abandoning the structure.

---

## 5. ESG Controversies (with financial impact estimates)

| Controversy | Status | Estimated financial impact |
|---|---|---|
| **In re Cloudflare Stockholder Litigation** (Del. Ch., C.A. No. 2026-0772-JTL) — recapitalisation enjoined 16-Oct-2026 | Live; expedited trial offered on safe-harbour/good-faith | Direct legal cost low ($5–15M); **market impact observed**: shares fell from $347.70 (13-Oct) to $296.30 (16-Oct), ~−15% over three sessions. Structure uncertainty = cost-of-capital overhang |
| **LaLiga / Spanish IP-blocking dispute** — Cloudflare complaint dismissed 26-Mar-2025; collateral damage documented (OONI 2026) | Ongoing; adverse precedent risk | Legal costs ~$2–10M; Spanish revenue small; **precedent risk** across EU is the real exposure |
| **Global outage 18-Nov-2025** (Bot Management config bug) | Resolved | Unquantified; service credits + churn/renewal friction. Highest *cash-flow* risk of the four |
| **Dual-class/entrenchment proxy opposition** — JLens withhold campaign on Zatlyn & Sandell, AGM 30-Jun-2026 | Active | Governance-driven exclusion from some ESG indices/funds; modest passive outflow risk |
| *Positive:* Project Galileo civil-society protection; 2026 cyberattack-against-civil-society report; PHP vulnerability mitigation | Ongoing | Reputational asset; supports enterprise trust narrative |

I found **no** evidence of bribery/FCPA issues, environmental spills or fines, product-safety recalls, or discrimination settlements. Absence of evidence, not evidence of absence — the filing tool failed, so I could not read legal-proceedings footnotes.

---

## 6. Regulatory ESG Exposure

| Jurisdiction / Rule | Applies? | Note |
|---|---|---|
| **EU CSRD / ESRS** | **Likely** | Non-EU parent with substantial EU turnover; Omnibus "stop-the-clock" pushed wave 2/3 timelines to FY2027 reporting. Double-materiality assessment required |
| **EU NIS2** | **Yes** | Cloudflare is an ICT/digital infrastructure provider — likely "important entity"; incident reporting and supply-chain obligations |
| **EU DORA** | **Yes** | Acts as ICT third-party provider to EU financial entities; contractual, audit-rights and exit-plan obligations; possible critical-ICT designation |
| **EU Cyber Resilience Act** | **Yes** | Product-security obligations for software/firmware; 2027 main application |
| **EU AI Act** | Adjacent | Relevant to AI-crawler/firewall products and to customers' compliance |
| **SEC Reg S-K Item 106 / Item 1.05 8-K** | **Yes** | Annual cyber risk-management disclosure; material-incident reporting |
| **SEC climate rule (S-K Item 1500)** | Stayed | Litigation; not currently binding |
| **California SB 253 / SB 261** | **Likely** | Large US company doing business in CA; Scope 1–3 and climate-risk disclosure; first reports 2026 — this is the rule most likely to force formal Scope 3 reporting |
| **Spain/EU content-blocking orders; UK Online Safety Act; US Section 230** | **Yes** | Intermediary-liability exposure; the LaLiga precedent is the live case |
| **EU CBAM** | **No** | Not a covered good |
| **ESG-linked debt covenants** | None located | Convertible notes carry no sustainability-linked terms |

**Direction of travel:** rising. The material ones are SB 253 (forces audited Scope 1–3 disclosure — Cloudflare's flat 43,100t Scope 3 becomes publicly benchmarked) and the EU stack (NIS2 + DORA) which raises contractual/compliance cost but also, perversely, **creates demand** for Cloudflare's compliance products. Net run-rate compliance cost: est. **$5–15M/yr**, immaterial to cash flow.

---

## 7. Overall ESG Rating: **AVERAGE** (Governance sub-rating: **Laggard-tier**)

- **E: Average** — low absolute footprint, 100% renewable electricity, credible SBTi-validated 2030 target; but flat Scope 3, target "at risk," score of 45 vs 94–100 for Cisco/Microsoft, and only 1 of 8 tracked commitments active. Greenwashing optics on "zero emissions" while 99.5% of footprint sits in Scope 3.
- **S: Average** — genuine public-interest product and strong defensive posture on civil society; offset by intermediary-liability litigation and a demonstrated global-outage reliability failure.
- **G: Laggard** — 10:1 dual class, combined CEO/Chair, recapitalisation enjoined on probable bad faith, destroyed records, sub-18% minority support, evergreen dilution cap removed. This is the swing factor.

**What would change the rating:** *Upgrade to Leader* — clean expedited-trial outcome plus abandonment/modification of the ~20%-economic-control structure, formal CDP/SB 253 Scope 1–3 disclosure, reinstated evergreen cap. *Downgrade to ESG Risk* — adverse final ruling under entire-fairness, further evidence of record destruction, or a repeat global outage.

---

## 8. ESG Investment Implication: **NEUTRAL** (leaning negative on governance overhang only)

**ESG is not the driver of the NET thesis — AI-era connectivity, bot verification and the "operating layer for the automated internet" are.** On ESG-specific grounds the factors are largely non-cash-flow: carbon cost of ~$2–7M is noise against a $117.6B market cap and a business compounding >25%; environmental risk should not move a DCF.

**But the governance file is genuinely material, and it is mispriced if treated as boilerplate:**
1. **Event risk is binary and near-dated.** The court offered an expedited trial on the good-faith safe harbour. A loss pushes to an entire-fairness trial — months of uncertainty over the capital structure of a $117B company. The ~15% drawdown across 13–16 Oct suggests the market is beginning to price this.
2. **Dilution is under-modelled.** Removing the evergreen cap grants authority over ~5% of outstanding shares annually (~$5.9B at current cap). This is a real, quantifiable shareholder cost that sits inside the equity-comp line rather than the governance discussion.
3. **The entrenchment structure caps upside optionality.** Founders able to hold control at ~20% of prior economic interest, with ~$2.1B of permitted sales, reduces the credibility of a third-party takeout — the court noted the injunction didn't jeopardise an acquisition proposal, but the structure itself makes one harder to execute.
4. **EU regulatory friction is a modest, rising cost of doing business** — and partly self-offsetting, since NIS2/DORA/CRA compliance demand pulls customers toward Cloudflare's product set. Watch the LaLiga precedent, not the Spanish revenue.

**Positioning conclusion:** ESG should **not** gate the investment. It should size it. Recommend no ESG-driven exclusion or reduction on environmental grounds; flag governance as a discrete risk factor requiring an explicit event-risk discount (litigation outcome, dilution from uncapped evergreen, founder-sale overhang), and require monitoring triggers: (a) expedited-trial ruling and any settlement terms; (b) the FY2026 proxy for actual Say-on-Pay support and any further withhold campaign; (c) first SB 253 Scope 1–3 filing; (d) any recurrence of a global outage.

**Rating summary:** Environmental **Medium** | Social **Medium** | Governance **4/10** | Overall **Average** | Implication **Neutral**
