# Geo Legal Researcher

- Symbol: GMAB
- Elapsed: 89.8s

---
## GMAB (Genmab A/S) — Geopolitical & Legal Risk Assessment
*As of late October 2026. Company: Copenhagen-domiciled biotech, ~3,100 FTEs, ~$27.6bn market cap, Nasdaq ADR (GMAB) / Nasdaq Copenhagen primary listing. Foreign private issuer — files Form 20-F, not 10-K.*

**Data note:** SEC EDGAR, Genmab IR static files and GlobeNewswire all returned HTTP 403 to direct fetches, and `fetch_company_facts` returned no submission index. Financial geography below is therefore reconstructed from filing excerpts surfaced via search (Q1–Q2 2026 interim reports, FY2025 annual report release, FY2026 guidance) rather than the full 20-F risk-factor text. Gaps are flagged explicitly.

---

## 1. Geographic Risk Map

Genmab does not publish a clean geographic revenue table in accessible disclosures; the map below is a derivation from (a) DARZALEX US vs. international net trade sales, (b) disclosed "net product sales in the U.S. and Japan by Genmab," and (c) known partner commercial territories.

| Geography | Revenue exposure (est. % of total) | Basis / driver | Risk level |
|---|---|---|---|
| **United States** | **~55–60%** | ~60% of DARZALEX net trade sales are US ($2,528M US vs. $1,711M intl. per quarter); Kesimpta royalties US-weighted; US product sales ($379M in 2025, US+Japan); 50% of Tivdak US gross profit (Pfizer); AbbVie books US epcoritamab | **Medium-High** (pricing policy, tariffs, IRA, litigation forum) |
| **Europe (EU, incl. Denmark HQ)** | **~13–18%** | Ex-US DARZALEX royalties; Genmab records its own sales for Europe; EU HTA/pricing pressure | **Low** |
| **Japan** | **~5–8%** | DARZALEX/Kesimpta royalties; EPKINLY approved by MHLW; Genmab books Japan sales directly | **Low** |
| **Rest of world (RoW)** | **~8–12%** | Ex-US DARZALEX royalties across RoW; no disclosed concentration | **Low-Medium** |
| **China** | **~0% revenue**; material **R&D/cost** exposure | ProfoundBio acquisition (May 2024, ~$1.8bn): HQ Seattle, "R&D center of innovation in Suzhou, China" — source of the Rina-S ADC | **Medium** (BIOSECURE/IP/data, supply chain) |
| **Russia / Belarus** | ~0% | No disclosed revenue; Danish/EU sanctions alignment | **Low** |

**Concentration flag:** 2026 guidance is anchored on **DARZALEX royalties of ~$2.83bn at the midpoint** (raised from ~$2.7bn at Q1) against royalty revenue of $3,102M in FY2025 (+23% YoY) and Q1 2026 revenue of $896M (+25%, royalty revenue $742M, of which DARZALEX $562M). That implies **~65–70% of total revenue from a single royalty stream** controlled commercially by Johnson & Johnson — a legal/counterparty exposure that is also geopolitically levered (see Risk 1).

---

## 2. Top 3 Geopolitical Risks

**Risk 1 — US pharmaceutical pricing and tariff regime (Section 232 + MFN). Probability: High (policy in force). Impact: Medium-High.**
On **April 2, 2026** the White House invoked Section 232 to impose a **100% headline tariff** on patented pharmaceuticals/biologics and their APIs from **July 31, 2026**. Key mechanics for GMAB:
- **EU member-state products (incl. Denmark) are capped at 15%**, not 100% (Crowell & Moring).
- **Antibody-drug conjugates are expressly exempt** — materially favourable for Rina-S.
- Companies with an **HHS MFN pricing agreement** escape additional tariff through Jan 20, 2029; **13 companies in Annex II** already qualified, and by end-2025 **16 manufacturers** had executed MFN agreements (Crowell). **Genmab is a royalty collector, not the US importer of DARZALEX** — so direct duty incidence is limited, but the second-order hit is real: J&J and Novartis face tariff/MFN price pressure on the underlying molecules, which compresses the royalty base. Genmab's own US-bound product (and any ex-US-manufactured ADC/antibody product it imports) is exposed at 15%.
- Separately, **Medicare Part B drugs enter IRA negotiation for 2028** (JMCP) — DARZALEX is physician-administered, making this a live watch item even though I could not confirm DARZALEX's selection in any CMS list from the tools available.

**Risk 2 — US–China technology and supply-chain decoupling. Probability: Medium. Impact: Low-Medium.**
The Suzhou R&D centre acquired with ProfoundBio places part of Genmab's ADC discovery capability inside China. Exposure vectors: BIOSECURE-style restrictions on Chinese biotech collaboration, outbound investment/data-transfer rules, and the risk that Chinese-origin IP becomes evidentiary fuel in the AbbVie suit. No China revenue, so the P&L hit is cost/optionality, not top line.

**Risk 3 — Transatlantic / Danish-domicile friction (Greenland) and EU pricing. Probability: Low-Medium. Impact: Low.**
US–Denmark relations are strained over Greenland: Denmark has publicly pushed back as the administration touted Greenland oil and mineral deals (Al Jazeera, Oct 14 2026), with a security deal announced that excludes mining/drilling rights. I found **no evidence of company-specific targeting** of Danish pharma; treat this as a tail risk to domicile reputation and to the 15% EU tariff carve-out. On the EU side, the EU HTA regulation and pharma-package pricing pressure are a structural, slow-burn margin risk rather than a geopolitical shock.

---

## 3. Legal & Regulatory Highlights

| Matter | Forum / date | Substance | Materiality |
|---|---|---|---|
| **AbbVie Inc. v. Genmab A/S et al** (2:25-cv-00510) | W.D. Wash. (Judge Tana Lin), filed **Mar 21, 2025** | **DTSA trade-secret misappropriation** re ADC technology; AbbVie alleges Genmab was "intentionally and willfully blind" to theft by former AbbVie employees; names **ProfoundBio**. Genmab "categorically refutes"; Genmab/ProfoundBio moved to dismiss (Law360); docket order Jan 16, 2026 | **HIGH** — directly implicates **Rina-S**, which just delivered positive Phase 3 RAINFOL-02 (stat. sig. PFS *and* OS in platinum-resistant ovarian cancer, Oct 23 2026). An injunction or damages finding would hit the most valuable near-term catalyst |
| **Janssen/J&J arbitration (second)** | AAA/arbitral tribunal; appeal denied | Genmab sought **$405M in accrued DARZALEX FASPRO milestones plus an extended royalty term**; tribunal ruled for Janssen (2-1), appeal rejected — claims dismissed as brought in the wrong forum. Tribunal also permitted **J&J to keep reducing royalties to offset its Halozyme obligations** | **MEDIUM** — concluded adversely; sets a permanent royalty leakage on the core asset |
| **MorphoSys v. Genmab/Janssen** (CD38 patent) | D. Del. | Settled — MorphoSys dismissed infringement claims with prejudice; Genmab/Janssen dropped inequitable-conduct counterclaims | Closed |
| **Genentech/Biogen dispute** | Fed. Cir. | Final judgment for Genmab upheld; exhausted on appeal | Closed |
| **J&J opts out of HexaBody-CD38** | 2026 | J&J declined its worldwide license option after Ph1/2 data; Genmab discontinued the program. No guidance impact | Pipeline write-off; underscores single-partner dependence |
| **Regulatory posture** | FDA, EMA/CHMP, Japan MHLW | Multiple approvals/expansions (EPKINLY in EU and Japan; Tivdak accelerated approval — confirmatory-trial obligations). Rina-S data to be "discussed with regulatory authorities worldwide" | Standard; Tivdak's accelerated status is a conversion risk |

**Notable commercial/legal positives reducing risk:** new Incyte clinical collaboration in KRAS G12D mCRC (Oct 24, 2026) and the Rina-S Phase 3 win diversify the story away from pure DARZALEX royalty dependence over time.

---

## 4. Compliance Red Flags

- **No sanctions, AML, or FCPA/UK Bribery Act issues identified.** Genmab's footprint is US/EU/Japan-weighted with ~zero revenue in sanctioned or high-corruption-risk jurisdictions — a structurally clean compliance profile for a company of this size.
- **Export controls:** Denmark has issued **Executive Order 365/2026** aligning Danish dual-use export controls with EU/US regimes (globalsanctions.com). Low relevance to antibody therapeutics, but relevant to any Suzhou-based technology transfer.
- **Trade-secret/IP hygiene** is the genuine compliance theme here, not bribery: the AbbVie complaint centres on the conduct of former AbbVie employees now at ProfoundBio. This is a **diligence-governance** red flag on the $1.8bn ProfoundBio deal.
- **Data privacy:** GDPR plus EU AI Act exposure from R&D/clinical data use — not currently a flagged issue.
- **Unverified item / gap:** A J&J 10-K legal-proceedings exhibit references an "unfair competition action against Genmab and Johnson & Johnson" involving a Eurasian ("EA") patent and an oral hearing. I could not retrieve the SEC text (403) to confirm jurisdiction or materiality. Treat as **de minimis / unresolved**.

---

## 5. Overall Geopolitical/Legal Risk Rating: **MEDIUM**

**Rationale.** Jurisdictionally this is a low-risk profile: Danish domicile, OECD-only revenue, no sanctions or emerging-market currency/repatriation exposure, and no bribery/AML flags. That anchors the rating below "High." What lifts it to Medium is an unusual combination of **concentration and policy sensitivity**: ~65–70% of revenue is a royalty on one molecule (DARZALEX) whose US pricing and import economics are now directly in scope of the Section 232 tariff regime and MFN pricing agreements, and a single licensor (J&J) has already prevailed against Genmab twice in arbitration and declined its HexaBody-CD38 option. Layered on top is the **AbbVie trade-secret suit**, which is the single largest binary legal risk because it targets Rina-S — the asset on which the post-DARZALEX growth narrative most depends — out of the US District Court in Seattle.

**What would move the rating:** *to High* — an adverse injunction or damages finding in AbbVie v. Genmab, or revocation/renegotiation of the 15% EU tariff carve-out or a punitive MFN designation for J&J/Novartis flowing through to royalty rates. *to Low* — early dismissal of the AbbVie claims plus confirmation that DARZALEX is outside IRA Part B negotiation and that Genmab's own import footprint is ADC-exempt.

**Key sources:** Crowell & Moring client alert on the April 2, 2026 Section 232 proclamation; White House proclamation (Apr 2026); Genmab FY2025 annual report release and Q1/Q2 2026 interim reports (via search excerpts); Genmab press releases on Janssen arbitration and appeal denial, HexaBody-CD38, and RAINFOL-02 (Oct 23, 2026); Justia/PacerMonitor dockets for *AbbVie v. Genmab* (2:25-cv-00510); Al Jazeera (Oct 14, 2026) on US–Denmark–Greenland; globalsanctions.com on Danish Executive Order 365/2026; CMS/KFF/JMCP on IRA negotiation, including 2028 Part B inclusion.
