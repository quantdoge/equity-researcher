# geo_legal_researcher

_2026-08-22T07:44:02+00:00_

# Comprehensive Geopolitical & Legal Risk Analysis: Advanced Micro Devices, Inc. (AMD)

**Analyst:** Geopolitical and Legal Researcher  
**Date:** August 2026  
**Ticker:** AMD (NASDAQ)  
**Fiscal Year Reference:** FY2024 (ended Dec 28, 2024) and FY2025 (ended Dec 27, 2025) where available.

---

## 1. Geographic Risk Map

Revenue figures below are sourced from FMP `statements` / `revenue-geographic-segments`. AMD reports sales by **customer billing location**, not end-market consumption; this is an important nuance because Singapore/Taiwan billing hubs may mask ultimate China demand.

| Country / Region | FY2024 Revenue ($M) | FY2024 % of Total | FY2025 Revenue ($M) | FY2025 % of Total | Risk Level |
|---|---|---|---|---|---|
| **United States** | 8,693 | 33.7% | 11,363 | 32.8% | Low-Medium |
| **China (incl. Hong Kong)** | 6,231 | 24.2% | 7,751 | 22.4% | **Very High** |
| **Singapore** | 3,614 | 14.0% | 4,284 | 12.4% | Medium |
| **Taiwan** | 3,301 | 12.8% | 5,186 | 15.0% | **Very High** |
| **Japan** | 1,767 | 6.9% | *consolidated* | *n/a* | Low |
| **Europe** | 1,625 | 6.3% | *consolidated* | *n/a* | Low-Medium |
| **Other Countries** | 554 | 2.1% | 6,055 | 17.5% | Medium |
| **Total** | **25,785** | **100%** | **34,639** | **100%** | — |

**Notes & Data Gaps:**  
- FY2025 data from FMP consolidates Japan and Europe into "Other Countries," so year-over-year comparability is impaired. AMD has not disclosed whether it changed geographic segment definitions in FY2025; this should be verified in the FY2025 10-K when published.  
- **Physical asset exposure** (from FMP `statements` / `financial-reports-form-10-k-json`, year 2024): AMD holds only **$38M** of net property and equipment in China versus **$1,312M** in the U.S., indicating low direct expropriation risk but high *operational* exposure through joint ventures and suppliers.

---

## 2. Top 3 Geopolitical Risks

### Risk 1: US Export Controls on AI/Advanced Chips to China  
- **Probability:** High  
- **Impact:** High (already materialized)  
- **Evidence:** In April 2025, AMD disclosed it could incur charges of **up to $800 million** related to new U.S. license requirements for exporting its **MI308** AI accelerators to China and other countries. The company stated it expected to apply for licenses but that "there is no assurance that licenses will be granted" (CNBC, `fetch_page`; Reuters, `web_search`). China was AMD's second-largest market in FY2024, generating ~$6.23B (24% of sales).  
- **Assessment:** Further tightening of the Foreign Direct Product Rule (FDPR) or additional entity-list designations could force AMD to write down more China-specific inventory or abandon segments of its Data Center growth trajectory.

### Risk 2: Taiwan Strait / TSMC Supply Chain Disruption  
- **Probability:** Medium  
- **Impact:** Very High  
- **Evidence:** AMD is a fabless semiconductor designer. The 10-K confirms it relies on third-party foundries for wafer manufacturing, but **does not disclose the specific share of wafers sourced from TSMC**. Industry context (via `web_search`) notes that Taiwan produces **60% of global foundry output and >90% of advanced-node chips**, with TSMC accounting for the dominant share. AMD's own case study on TSMC's website confirms a deep operational relationship (`fetch_page`).  
- **Assessment:** A blockade, conflict, or severe natural event in Taiwan would disrupt the supply of virtually all AMD leading-edge CPUs and GPUs. Because this is a supply-side (not revenue-billing) risk, it is **not captured** in the geographic revenue table above. AMD has no near-term alternative foundry at equivalent scale for advanced nodes.

### Risk 3: China Retaliatory Measures & Accelerated Domestic Substitution  
- **Probability:** Medium  
- **Impact:** High  
- **Evidence:** Chinese chip firms are recording record revenue on AI processors as U.S. export controls push domestic substitution (YouTube/tech media via `web_search`). Separately, AMD's China revenue surged from $3.4B in FY2023 to $6.2B in FY2024 and $7.8B in FY2025, even as U.S. restrictions tightened—suggesting strong demand but also raising the stakes if China retaliates with cybersecurity reviews, rare-earth export restrictions, or procurement bans on U.S. chips.  
- **Assessment:** Should China shift from passive adaptation to active retaliation, AMD's second-largest revenue pool could face non-tariff barriers overnight. The **ATMP Joint Venture** and **THATIC Joint Venture** (see Red Flags below) also create potential pressure points.

---

## 3. Legal & Regulatory Highlights

| Matter | Status | Details & Source |
|---|---|---|
| **US BIS Export Controls / MI308 License Requirement** | Active | April 2025: AMD warned of up to **$800M charge** for inventory and purchase commitments tied to new licensing requirements for MI308 shipments to China (CNBC `fetch_page`; Reuters `web_search`). |
| **Adeia Patent Infringement Litigation** | **Settled March 2026** | Nov 2025: Adeia sued AMD in W.D. Texas alleging infringement of **10 patents** (7 hybrid bonding, 3 advanced process node) covering AMD's 3D V-Cache technology in Ryzen X3D and EPYC chips; also sought a USITC exclusion order (TechPowerUp `fetch_page`; ip fray `fetch_page`). **March 9, 2026:** Parties executed a **multi-year IP license agreement**; terms undisclosed (Adeia press release via `web_search`; Reuters `web_search`). |
| **Material Legal Proceedings (FY2024 10-K)** | None disclosed | As of December 28, 2024, the 10-K stated: **"there were no material legal proceedings"** (SEC filing snippet via `web_search`). |
| **ZT Systems Acquisition** | Regulatory risk (likely closed) | Aug 2024: AMD agreed to acquire ZT Systems for ~**$4.9B** cash/stock. Subject to regulatory approvals; **$300M termination fee** if not closed by August 2025 (extended to February 2026) (FMP `statements` / `financial-reports-form-10-k-json`). |

**Regulatory Posture:**  
- **CHIPS Act:** AMD does not directly receive CHIPS Act manufacturing subsidies because it is fabless. However, its foundry partners (notably TSMC and Samsung) are bound by CHIPS Act "national security guardrails" that restrict expansion and technology transfer in "foreign countries of concern" such as China (`web_search`: Congress.gov, cmtradelaw.com). This indirectly constrains foundry capacity allocation and geographic diversification timelines.  
- **Antitrust / FTC / DOJ:** No active antitrust investigations or regulatory actions against AMD were identified in FMP data or web searches. Historically, AMD has been a plaintiff in semiconductor antitrust matters (e.g., vs. Intel), not a defendant.

---

## 4. Compliance Red Flags

### A. China-Based Joint Ventures & Operational Dependence
1. **ATMP JV (Tongfu Microelectronics)**  
   - AMD holds a **15% equity interest** in two Chinese joint ventures providing assembly, test, mark, and packaging (ATMP) services.  
   - FY2024 purchases from ATMP JV: **$1.7 billion**; payables outstanding: **$476 million** (FMP `statements` / `financial-reports-form-10-k-json`).  
   - In October 2024, AMD extended a **$100 million term loan** to one of the ATMP JVs.  
   - **Flag:** A significant share of AMD's backend manufacturing is tied to a Chinese partner. If Tongfu or its affiliates are sanctioned, added to the Entity List, or caught in a cross-border technology clampdown, AMD's ability to ship finished goods could be impaired.

2. **THATIC JV (Higon Information Technology)**  
   - AMD holds an equity interest in two JVs with Higon/THATIC. Carrying value: **$0**.  
   - AMD licensed certain IP in 2016 and receives royalties; FY2024 licensing/royalty income: **$48 million** (FMP `statements` / `financial-reports-form-10-k-json`).  
   - **Flag:** Licensing core semiconductor IP to a Chinese entity is under heightened US government scrutiny. Any retroactive restriction on such arrangements could eliminate future royalty income and invite regulatory review.

### B. Customer Concentration with Geopolitical Tail Risk
- **Customer A (Gaming segment)** accounted for **18% of consolidated net revenue** in FY2024 (FMP `statements` / `financial-reports-form-10-k-json`). This is almost certainly a major game-console OEM.  
- **Flag:** A customer of this scale facing its own China market restrictions or inventory corrections would immediately flow through to AMD's top line.

### C. Export Control Compliance Burden
- The $800M MI308 charge illustrates that AMD must now navigate **product-specific BIS licensing** for Data Center accelerators.  
- **Flag:** Each new generation of AI accelerator (MI350, MI400 series) may require separate classification and licensing reviews, creating recurring revenue uncertainty and inventory obsolescence risk for China-bound product.

---

## 5. Overall Geopolitical / Legal Risk Rating: **HIGH**

### Rationale
AMD earns **~22–24% of its revenue from China**, a jurisdiction now subject to active, escalating U.S. export controls that have already forced an **$800 million charge**. Simultaneously, AMD is **fabless and critically dependent on TSMC/Taiwan** for leading-edge wafer manufacturing—a supply-chain concentration that is not visible in the revenue-by-geography table but represents an **existential vulnerability** should Taiwan Strait tensions escalate. The company also carries **material operational exposure** inside China via the $1.7B/year ATMP joint venture and the THATIC IP-licensing arrangement, both of which sit in a regulatory crossfire. While the recent Adeia patent dispute was settled (eliminating one near-term litigation overhang), the combination of **revenue concentration in a sanctioned market + supply-chain concentration in a geopolitical flashpoint + active technology-transfer restrictions** justifies a **High** overall geopolitical and legal risk rating.

### Data Gaps Flagged
- AMD does **not publicly disclose** the exact percentage of wafers sourced from TSMC by node; the Taiwan supply-chain risk magnitude is inferred from industry data rather than company filings.  
- The **FY2025 geographic revenue breakdown** from FMP consolidated Europe and Japan into "Other Countries," making year-over-year comparability difficult without the full FY2025 10-K.  
- The **financial terms of the Adeia settlement** are undisclosed.  
- AMD has **not quantified** a specific revenue-at-risk scenario for a Taiwan supply disruption in its SEC disclosures.  
- No active DOJ, FTC, or SEC enforcement actions were identified, but absence in public filings does not guarantee absence of informal inquiries.
