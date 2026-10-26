# Geo Legal Researcher

- Symbol: NBIS
- Elapsed: 171.2s

---
# NBIS — Nebius Group N.V.: Geopolitical, Regulatory & Legal Risk Assessment
**Prepared by:** Geopolitical & Legal Research | **Data as of:** late October 2026 | **Sources:** SEC filings/company releases, Reuters, CNBC, Barron's, WHYY, BIS/export-control guidance, law-firm commentary

---

## 1. Geographic Risk Map

Nebius is a Dutch-domiciled (Amsterdam HQ), Nasdaq-listed AI infrastructure company — the renamed former Yandex N.V. after the July 2024 $5.4bn divestment of its Russian businesses (Reuters, Morgan Lewis). Its revenue base is overwhelmingly **US-customer-driven**, while its physical footprint is **European-weighted**.

| Country / Region | Role & Exposure | Revenue/Asset Exposure | Risk Level |
|---|---|---|---|
| **United States** | Microsoft (~$17.4bn→$19.4bn through 2031) and Meta (~$3bn 2025 + $12bn from 2027, up to +$15bn) contracts ≈ **80% of ~$40bn firm commitments**; 300MW Vineland, NJ data center; Kansas City deployment; Nasdaq listing/US securities law | Very High (majority of contracted revenue; large capex) | **High** |
| **Finland** | Owned Mäntsälä data center; expansion to 75MW, then a **310MW / ~$10bn AI factory**; EU member bordering Russia | High (largest European asset base) | **Medium-High** |
| **Netherlands** | HQ, corporate domicile, Dutch law, EU regulatory perimeter, R&D | Low revenue; high legal/regulatory salience | **Medium** |
| **France, UK, Iceland** | Colocation capacity; UK is a separate export-control and data-protection jurisdiction | Moderate (capacity, not disclosed revenue) | **Low-Medium** |
| **Israel** | R&D hub; regional conflict and talent-mobility risk | Low revenue; operational | **High (geopolitical)** |
| **Russia (legacy)** | Exited July 2024; residual sanctions/legal/reputational tail | Nil operating; contingent legal | **Medium-High** |
| **Global AI developers** | Customer base beyond hyperscalers (Reflection, Cohere et al.); end-use jurisdiction unknown | Growing | **Medium (compliance)** |

**Disclosure gap:** Nebius does not publish granular country-level revenue percentages in the accessible 20-F excerpts. Segment disclosure shows AI cloud = **98% of Q2 FY2026 group revenue** ($575M AI revenue; ~$587M group), with FY2025 revenue ≈$530M (+479% YoY) and AI ARR ~$1.9B in Q1 FY2026. The closest available proxy for geographic revenue is customer concentration: three unnamed customers were **24%, 21% and 14% of Q2 FY2026 revenue** (Motley Fool/Yahoo Finance), all but certainly US-domiciled. Treat "US = majority of revenue" as an inference from customer mix and contracted backlog, not a filed figure.

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — US export-control and chip-supply dependence (Probability: Medium-High | Impact: High)
Nebius's product is Nvidia GPU capacity (H200/GB300/Blackwell/Vera Rubin). GPUs sit under ECCNs 3A090/3A991 with license requirements; BIS reaffirmed licensing on 31 May 2026 and shifted H200/AMD review policy in January 2026. Nebius operates EU data centers (Finland, France, Iceland, UK) plus Israel and the US, and serves foreign AI developers — meaning **re-export, end-use and "deemed export" exposure** across multiple jurisdictions. Any tightening of country caps, customer end-use vetting, or license conditions directly constrains revenue and capacity utilisation. Law-firm commentary explicitly warns that improperly handled GPUs carry the "taint" of an EAR violation. This is the single largest externally-imposed constraint on the model.

### Risk 2 — Jurisdictional concentration in the US customer base and US policy leverage (Probability: High for friction; Medium for material loss | Impact: High)
Roughly four-fifths of ~$40bn firm commitments come from two US hyperscalers. Contracts are take-or-pay and Microsoft has prepaid ~$7bn, which cushions near-term cancellation — but both customers retain tranche-level cancellation rights for delivery/availability failures. Concentration cuts three ways: (a) US trade/tech policy and antitrust action against Microsoft/Meta transmit directly to Nebius; (b) tariff and EU–US trade tensions (Washington linking steel tariff relief to softer DMA enforcement; EU preparing China tariffs) raise input and compliance costs; (c) state-level US energy/environmental politics — see the New Jersey enforcement below — can halt capacity.

### Risk 3 — Russia legacy and sanctions/legal tail (Probability: Low-Medium | Impact: Medium-High)
The Russian asset sale closed July 2024 ($5.4bn, including a 28% stake sold for $2.8bn cash plus 162.5m shares), and CEO Arkady Volozh was **removed from the EU sanctions list in March 2024** after condemning the Ukraine invasion — a genuine de-risking. Residual exposures: reputational/"ex-Russian" screening by enterprise and government customers; possible claims from Russian minority shareholders or brokers (a Russian private investor sued broker ATON over Yandex N.V. share purchases); EU sanctions escalation (12 Oct 2026 added 826 entities/743 individuals to the asset-freeze list) which raises counterparty-screening obligations; and Dutch–Russian enforcement asymmetry — the 20-F itself notes there is **no mutual recognition treaty between the US and the Netherlands**, complicating judgment enforcement either way.

*Secondary:* Israel operations (conflict escalation, reservist mobilisation) and EU AI Act/GDPR exposure (Risk 2 in Section 3).

---

## 3. Legal & Regulatory Highlights

- **New Jersey environmental enforcement (active, material):** The 300MW Vineland data center being built by DataOne for Nebius (under the ~$17bn Microsoft arrangement) was fined **more than $1 million** by the NJ DEP for running **62 natural-gas generators without a permit** — described by the Commissioner as "by far the largest ever taken against a data center in New Jersey." The site also received **two stop-work notices** for an unpermitted LNG tank and fuel-cell units. A **class-action lawsuit** has been filed by residents over noise. This is the most concrete, quantified legal/regulatory contingency disclosed in public sources and sits on the critical path of the Microsoft contract.
- **Securities litigation exposure:** The 20-F risk factors acknowledge that companies with volatile share prices "have been subject to securities class action litigation" and cite "litigation exposure… or other compliance deficiencies including regulatory investigations." NBIS has fallen sharply (down ~50% from peak per 24/7 Wall Street; Musk's "guppy-level death" comments hit the whole neocloud complex on 26 Oct 2026), which is precisely the fact pattern that attracts securities plaintiffs. **No specific active class action against Nebius was confirmed** in this search — treat as a probable, not confirmed, contingency.
- **EU regulatory perimeter:** EU AI Act high-risk obligations phase in around 2 Aug 2026 (with talk of a delay to Dec 2027); GDPR (Nebius markets itself as an EU data processor); NIS2; EU Data Act; Dutch AI supervisory framework; and the EU's updated dual-use export-control list (Delegated Regulation adopted 14 Sep 2026). Nebius's "EU-based, GDPR-compliant" positioning is a commercial asset but also an enforcement surface.
- **Foreign investment screening:** Dutch FDI screening (Vifo Act) and US CFIUS could apply to future data-center or GPU-asset transactions; not currently flagged as an active review.
- **Antitrust/competition:** No active action identified; the EU's DMA enforcement against US Big Tech is an indirect risk given customer concentration.

---

## 4. Compliance Red Flags

1. **Export controls / end-use screening (highest priority):** GPU re-export and end-use compliance across Finland, France, Iceland, UK, Israel and the US; customer due diligence on foreign AI developers; "deemed export" exposure for US-person engineering support. The BIS "taint" doctrine and 2026 policy shifts make this a live, board-level issue.
2. **Russia sanctions tail:** KYC of legacy counterparties and the buyer consortium; ongoing EU listing risk for executives/entities; secondary-sanctions screening of customers. Volozh's delisting is mitigating, not eliminating.
3. **Environmental and power-generation permitting:** Unpermitted generators and stop-work orders at Vineland indicate weak local permit governance at the landlord/tenant boundary — a repeatable risk across the 300MW NJ site and other "bring-your-own-power" deployments.
4. **Data protection/AI Act:** GDPR processor obligations, cross-border transfers, and AI Act conformity for high-risk use cases; potential DPA complaints.
5. **Disclosure/accounting controls:** FY2025 net income of $82.5M was driven by a $694.2M tax/interest/other line against a $611.7M operating loss — a profile that invites SEC scrutiny and securities claims if guidance slips.

---

## 5. Overall Geopolitical / Legal Risk Rating

**MEDIUM-HIGH**

*Rationale:* Sanctions risk is materially lower than at Yandex N.V. (Russia exited, CEO de-listed from EU sanctions), but the company has swapped a Russia problem for a **US-dependence problem** — US chips, US customers, US listing and US state-level permitting — layered on top of a **Russia legal/reputational tail** and a **European asset base** exposed to EU AI/energy/export rules. The NJ enforcement action, the ~80% customer concentration and the export-control regime are the three items most likely to produce a material adverse event within 12–24 months. Sub-ratings: **Regulatory/compliance: High; Sanctions: Medium; Litigation: Medium-High; Political: Medium-High.**

**Key data gaps to close:** country-level revenue split (request the full 20-F financial statements note on geographic information); confirmation of whether any securities class action has been docketed against NBIS; the identity/jurisdiction of the three unnamed customers representing 24%/21%/14% of Q2 revenue; and the full text of the Vineland enforcement order and noise class action.
