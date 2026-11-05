# Geo Legal Researcher

- Symbol: BE
- Elapsed: 49.4s

---
## Bloom Energy (BE) — Geopolitical & Legal Risk Assessment

**Company snapshot:** Bloom Energy Corp. (CIK 0001664703), San Jose, CA. Solid-oxide fuel cell systems for onsite power; ~1,100 sites across 9 countries; ~2,214 employees; market cap ≈$59B, beta 3.64 (source: `get_company_profile`). FY2026 revenue guidance $4.4–4.6B after three raises; Q3'26 revenue $1,235.8M (+138% YoY) (Q3'26 press release, 22-Oct-2026). Added to the S&P 500 in September 2026.

**Important data caveat:** SEC.gov direct fetches returned HTTP 403 and `fetch_filing_text` could not surface the 10-K (the FY2025 10-K, accession 0001628280-26-006516, sits outside the tool's recent-filings window). Geographic revenue percentages below are therefore **estimated ranges**, not filed figures; qualitative facts are sourced.

---

## 1. Geographic Risk Map

| Country / Region | Revenue Exposure (est.) | Basis for estimate | Risk Level |
|---|---|---|---|
| **United States** | ~80–90% | Dominant market; hyperscaler/data-center and utility demand (Oracle, AEP, Brookfield JVs, California Resources MOU). FY2026 revenue surge is US-led. | **Medium** (permitting, tax-credit policy, litigation — not country risk) |
| **South Korea** | ~5–12% | "South Korea is our second-largest market," with ~600 MW of deployed Energy Server equipment; SK ecoplant owns ~2.5% of Class A stock and holds a Korean JV (Bloom SK Fuel Cell, LLC). (FY2025 10-K; Q1'25 10-Q; TradingView 10-K summary) | **Low–Medium** |
| **Japan** | <3% | Historically a distribution market; also named as an intermediary route in Bloom's scandium supply chain (Hunterbrook, 8-Jul-2026) | **Medium** (supply-chain, not demand) |
| **Taiwan / Europe / India / other** | Low single digits combined | "Beyond the U.S. and South Korea, we are pursuing selective international expansion" (FY2025 10-K). European AI-factory site (Brookfield) still unnamed per Hunterbrook. | **Low** |
| **China** | **0% direct revenue** | No disclosed China sales | **Very High — as a supply-chain chokepoint, not a market** |

**Key inversion:** Bloom's geographic risk is not where it sells; it is where a single input is refined. Roughly all fuel-cell-grade scandium oxide processing sits in China. This is the defining feature of the risk profile.

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — China's scandium export-licensing regime as an "off-switch" (Probability: High / Impact: Severe)
Beijing now requires an export licence for **every shipment of scandium** leaving China; the April-2025 regime covered seven rare earths including scandium, samarium and yttrium, with tightening through 2025–26 and episodic suspensions of the October-2025 tranche (CSIS; Clark Hill; Hunterbrook). Hunterbrook (8-Jul-2026) reports tracing **four separate China-linked routes** into Bloom's supply chain — scandium oxide shipped directly to Bloom's Delaware plant, plus scandium-bearing ceramics and powders routed through intermediaries in **Thailand, Japan and South Korea**. Hunan Oriental Scandium, claiming >50% of the global fuel-cell-grade scandium oxide market, told Hunterbrook: *"We are also BE's largest supplier of scandium,"* and, on how material reaches US customers under Beijing's controls: *"Not exported directly."*

- **Why it matters:** Management has repeatedly asserted "no China supply chain" and no dependence on Chinese scandium — a claim made at least five times since February 2025 (Hunterbrook). If inaccurate, the licence regime gives a foreign adversary a discretionary throttle on a company supplying power to US AI data centers. Western ex-China scandium processing capacity is described as essentially non-existent.
- **Impact channel:** physical supply constraint → volume miss against the 5 GW ambition; plus disclosure and litigation exposure (Risk 3). Mitigants: Bloom publicly states its supply chain supports up to 25 GW/yr and is not China-dependent (Bloom blog, "Demystifying Scandium Oxide").

### Risk 2 — FEOC / prohibited-foreign-entity contamination of customers' 48E tax credits (Probability: Medium-High / Impact: High)
The One Big Beautiful Bill Act superimposed **foreign entity of concern (FEOC/PFE)** rules on §§45Y/48E: even a compliant taxpayer is barred from the credit where a facility has sufficient **"material assistance"** from entities connected to China, Russia, North Korea or Iran (K&L Gates; Bipartisan Policy Center; IRS Notice 2026-15). OBBBA also compressed 48E timelines — begin construction by 4-Jul-2026 or be placed in service by 31-Dec-2027 for the restricted technologies — making credit eligibility a live commercial variable for Bloom's customers.

- **Why it matters:** Bloom's value proposition is partly an economics story in which customers monetise the ITC. If scandium-bearing components sourced from China constitute creditable "material assistance," customers' tax equity could be impaired — a demand-side risk originating in a China supply-chain fact. This is an inference from the two sources, not a company disclosure; it is unquantified and warrants direct diligence.

### Risk 3 — US permitting and environmental litigation on flagship projects (Probability: Medium-High / Impact: Medium-High)
Oracle's "Project Jupiter" in New Mexico is reported to lack an approved air permit for fuel cells and a gas pipeline to feed them; an environmental group is suing to stop it, with first power potentially slipping from 2027 toward 2029 or later (Hunterbrook; SemiAnalysis cited therein). AEP's $2.65B fuel cell order reportedly slipped from end-2028 to "no later than 2030." These are **allegations from a short seller** and should be verified against filings — but they are consistent with the structural reality that distributed generation is exposed to state air-permit and local opposition risk.

*Runners-up (not in top 3): US–Korea trade friction (KORUS insulates Bloom's exports; low); tariffs on imported components (moderate cost risk); nationalisation/expropriation (negligible — US/Korea); currency controls (negligible).*

---

## 3. Legal & Regulatory Highlights

**Active securities class action.** *Nevins v. Bloom Energy Corporation*, No. 3:26-cv-07944 (N.D. Cal.), Judge Rita F. Lin, filed 2026. Class period **27-Feb-2025 to 8-Jul-2026**. Lead-plaintiff deadline 28-Sep-2026. The complaint alleges defendants misrepresented/omitted that Bloom (1) obtained scandium through intermediaries sourcing from China; (2) downplayed the extent of that reliance; (3) consequently made false statements about business and prospects. Stock fell nearly 6% on the Hunterbrook report (Kessler Topaz; Levi & Korsinsky; BusinessWire). Multiple firms are soliciting — Rosen, Kaplan Fox, ZLK.

**Derivative litigation / D&O exposure.** A shareholder derivative action is being investigated on behalf of holders predating 27-Feb-2026, targeting board and officer oversight failures (Berger Montague). Bloom's 8-K of 9-Jul-2026 states the company "categorically rejects the Report's claims regarding the Company's financial results and accounting."

**Short-seller allegations beyond scandium (unproven, but litigation fuel).** Hunterbrook alleges Q4'25 revenue of $778M included $574M (74%) from Bloom part-owned JVs with Brookfield, with footnotes conceding customers "may be a project-finance affiliate rather than the ultimate end user"; that the unaudited "$20B backlog" is ~40x audited RPO of $492.6M (31-Mar-2026), and includes non-obligatory service revenue and ungranted tax credits. Treat as allegations; they nonetheless set the template for amended complaints and SEC inquiry risk.

**Regulators and policy.** Primary exposure is US federal energy tax policy (Treasury/IRS on 48E, FEOC and 45V hydrogen), state air-quality regulators (California, New Mexico, Texas), and utility interconnection regimes. No disclosed DOJ, SEC, FTC or FCPA enforcement action was found in this review.

**Prior history.** Bloom has been a serial securities-litigation defendant since its 2018 IPO, including post-IPO class actions around growth/guidance disclosures and a 2021 Delaware Chancery dispute with a former executive. Expect plaintiff firms to be well versed in the name.

---

## 4. Compliance Red Flags

| Flag | Assessment |
|---|---|
| **Disclosure accuracy on China sourcing** | **Highest-severity flag.** Public CEO statements ("no China supply chain") sit uneasily against alleged indirect sourcing via Thailand/Japan/Korea intermediaries. Intermediated routing to obscure origin is precisely the fact pattern regulators and plaintiff experts probe. |
| **Sanctions/export-control adjacency** | Not a sanctions violation per se — China's controls are *Chinese* export licensing, not US law. But any US person facilitating circumvention of a foreign licensing regime, or mis-declaring origin on imports (customs/FTC "Made in USA" and origin rules), creates secondary exposure. Worth confirming whether Bloom's Chinese suppliers are obtaining licences or routing around them. |
| **FEOC attestation risk** | Customers claiming 48E must document supply chains. Bloom may face contractual attestation demands from tax-equity investors. |
| **Third-party intermediary risk (FCPA)** | Sales and sourcing run through distributors/JVs in Korea, Japan and Thailand. No FCPA matter identified, but distributor commissions and JV governance in these markets are standard FCPA control points. **Low current concern.** |
| **Data privacy** | Negligible — operational telemetry from industrial power systems, no consumer data at scale. |
| **Related-party revenue quality** | Brookfield JV revenue concentration (alleged 74% of Q4'25) raises the possibility of related-party disclosure and revenue-recognition scrutiny. **Watch item.** |

---

## 5. Overall Geopolitical / Legal Risk Rating

# **HIGH**

**Rationale.** Bloom's *demand* geography is benign — the US and South Korea are low-risk, rules-based jurisdictions, and there is no Russia/Iran/emerging-market expropriation exposure. The rating is driven instead by three compounding factors:

1. **Single-point chokepoint in a hostile jurisdiction.** China controls essentially all fuel-cell-grade scandium processing and has erected a per-shipment licensing regime. Bloom has no substitute supplier at scale and no direct China revenue to offset the risk.
2. **The chokepoint is also the litigation.** The company's public denial of China dependence is the exact subject of a live securities class action and a derivative probe, with a class period extending 17 months. Legal risk and geopolitical risk are the same risk here, not diversifiable against each other.
3. **Policy linkage amplifies it.** FEOC/"material assistance" rules under OBBBA mean a supply-chain fact could degrade customers' ITC economics, converting a procurement problem into a demand problem.

**What would move the rating:** *Down to Medium* — a verifiable, contracted ex-China scandium supply chain (Australia/Canada/Philippines processing) with third-party audit, plus dismissal or cheap settlement of the class action. *Up to Very High* — a Chinese licensing denial causing shipment delay, any SEC formal investigation or subpoena, or an 8-K acknowledging indirect China sourcing.

**Diligence priorities:** (1) obtain the FY2025 10-K geographic revenue table and the "supply chain"/"raw materials" risk factor verbatim (SEC EDGAR direct access required — blocked in this session); (2) confirm whether Bloom or its suppliers hold Chinese export licences; (3) quantify scandium as a % of product COGS; (4) request customer FEOC attestations and any tax-equity indemnities.

---

**Sources:** `get_company_profile`; `fetch_company_facts`; Bloom Q3'26 press release (investor.bloomenergy.com, 22-Oct-2026); FY2025 10-K and Q1'25 10-Q references via EDGAR search results; Bloom 8-K dated 9-Jul-2026; Hunterbrook Media, "Bloom's Big Lie," 8-Jul-2026; Kessler Topaz case page (N.D. Cal. 3:26-cv-07944); Levi & Korsinsky / BusinessWire (6-Aug-2026); Berger Montague derivative notice; CSIS, "Consequences of China's New Rare Earths Export Restrictions"; Clark Hill on China's rare-earth control pause; K&L Gates and Bipartisan Policy Center on FEOC/PFE rules; IRS Notice 2026-15.
