# Geo Legal Researcher

- Symbol: AMD
- Elapsed: 88.5s

---
# AMD — Geopolitical & Legal Risk Assessment
**Advanced Micro Devices, Inc. (NASDAQ: AMD)** | Semiconductors | HQ: Santa Clara, CA | Market cap ~$733B | Latest quote $446.84 (~31% below the $649.42 record close of Oct 6, 2026)

**Bottom line:** AMD's risk profile has shifted from *theoretical* China exposure to an *active* regulatory and legal event. A short-seller report published Nov 19, 2026 alleges firmware/software support to a U.S.-blacklisted Chinese server maker, and it landed the same day new BIS licensing rules took effect. Approximately 35% of AMD's billings go to China and Singapore, and ~15% to Taiwan. This is now the single most important non-fundamental risk in the name.

---

## 1. Geographic Risk Map

FY2025 revenue: **$34.64B**; international sales **67%** of net revenue (per AMD FY2025 Form 10-K, filed Feb 4, 2026). Figures are **billed-to location, not end destination** — a critical caveat, since AMD sells through ODMs and distributors who re-export.

| Country / Region | FY2025 Revenue | % of Revenue | Risk Level | Driver |
|---|---|---|---|---|
| United States | $11.36B | 32.8% | **Low** | Home market; tariff *exemptions* for U.S. data center/consumer use |
| China + Hong Kong | $7.75B | 22.4% | **Very High** | Export controls, Entity List allegations, license dependency, SAMR leverage |
| Taiwan | $5.19B | 15.0% | **High** | TSMC leading-edge dependence; cross-Strait tail risk; worst TW equity week since 1991 |
| Singapore | $4.28B | 12.4% | **High** | New license requirement (BIS IFR, Nov 19, 2026); AI-chip transshipment hub |
| Other (Europe, Japan, Malaysia, Indonesia, Thailand, Brazil, etc.) | $6.06B | 17.5% | **Medium** | Malaysia/Indonesia/Thailand/Brazil now also license-gated |

*Sources: AMD FY2025 Form 10-K via Bullfincher/BusinessQuant; TradingKey, Nov 20, 2026.*

**Concentration insight:** China + Singapore ≈ **35%** of billings; adding Taiwan ≈ **50%** in geopolitically exposed jurisdictions. AMD also depends on a Chinese JV for most back-end manufacturing: two ventures **85% owned by Tongfu Microelectronics** provide the *majority* of AMD's chip assembly, test and packaging; AMD owns 15% and has a **$100M loan outstanding** to one of them (Hunterbrook, Nov 19, 2026).

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — U.S. export-control enforcement tied to IEIT Systems / Inspur network
**Probability: 40–50% of a formal inquiry/subpoena; ~15–20% of a civil penalty. Impact: High.**
Hunterbrook Media alleged (Nov 19, 2026) that IEIT Systems — placed on the Entity List in March 2025, where Commerce's stated policy is to *deny* licenses — incorporated **at least six newer versions of AMD firmware** into its products after blacklisting, the latest posted **Oct 19, 2026**. Three affiliated sellers use near-identical firmware: **Maginfra (China), Kaytus (Singapore), Aivres (California)**. Corporate filings link all three to IEIT (Kaytus's audited accounts name IEIT as ultimate parent; IEIT's 2022 annual report listed Aivres as a subsidiary). AMD's own website lists **Aivres as a maker of Instinct-based servers**.
- AMD's response: claims "misrepresent AMD's business practices and relationships" and that it "complies with applicable US export control laws and regulations." Notably, AMD **did not answer** Hunterbrook's specific question on whether it holds licenses to supply these entities, and did not respond to 24/7 Wall St. on the license records.
- The report itself concedes its findings do **not** "establish on their own a violation of export laws," and the firmware's path is unclear. That materially lowers legal but not reputational risk.
- **Escalation vector:** BIS enforcement has been escalating through 2026; deemed exports of firmware/software support to a listed entity are independently actionable under the EAR.

### Risk 2 — Geographic expansion of licensing + return of the 50%-ownership rule
**Probability: ~70% (rule returns Jan 10, 2027). Impact: Medium-High.**
- BIS published an **interim final rule on Nov 19, 2026** requiring licenses for advanced chips shipped to **Singapore, Malaysia, Indonesia, Thailand and Brazil** — Singapore alone is 12.4% of AMD billings. Orders requiring licenses may not ship on schedule even where already booked.
- A **suspended rule extending restrictions to foreign companies ≥50% owned by blacklisted entities expires Jan 10, 2027**; if it takes effect, it would sweep in **Kaytus** and other IEIT-majority-owned offshore entities — precisely the channel AMD is alleged to rely on.
- **Precedent for cost:** 2025 MI308 export limits produced roughly **$800M of inventory and related charges**. AMD booked only ~$390M of MI308 China sales in Q4 2025 versus $8.55B of Q3 2026 Data Center revenue — i.e., China AI revenue is now small, so the damage is more to *sentiment and multiple* than to near-term EPS.

### Risk 3 — Taiwan concentration and cross-Strait tail risk
**Probability: Low near-term (<10% for a blockade/disruption in 12 months); Impact: Severe (existential to the roadmap).**
AMD is fabless and reliant on TSMC for leading-edge nodes; Taiwan is also a 15% billing destination. Taiwan posted its **worst equity week since 1991** in mid-November 2026, and TSMC fell 4.2% in the same selloff that hit AMD. Mitigants: the **Jan 15, 2026 U.S.–Taiwan trade deal** (reshoring incentives, $250B+ investment pledges) and the 18-month delay of Section 301 tariffs on Chinese legacy chips. The residual risk is unhedgeable and underpins a permanent valuation discount.

**Adjacent risk — policy whiplash:** The Trump–Xi truce is fragile. Eurasia Group's Ian Bremmer expects the truce to be extended but warns tighter chip restrictions could trigger "measured Chinese retaliation." A planned Trump–Xi meeting in April 2027 is the next inflection point. Separately, the unusual **15% revenue-share arrangement** with the U.S. government for China AI-chip licenses (MI308/H20) creates political and legal exposure in its own right.

---

## 3. Legal & Regulatory Highlights

**Export controls / tariffs (live):**
- **Section 232 Proclamation 11002** (Jan 14, 2026): **25% tariff** on a narrow set of advanced logic chips, effective Jan 15, 2026 — technical parameters explicitly include **AMD's MI325X**. Use-based exemptions exist for U.S. data centers, U.S. R&D, startups, and non-data-center consumer/industrial applications, but CBP guidance on documentation is still absent.
- **BIS interim final rule** (Nov 19, 2026) on remote access to advanced semiconductors; license requirements for five Southeast Asian/Brazilian destinations.

**Congressional scrutiny (live):** House Foreign Affairs Committee Chairman **Brian Mast** released Commerce license records on Nov 19, 2026 under Export Control Reform Act authority: **879,000 of 3.4M** requested AI chips approved (Dec 2025–May 2026), covering NVIDIA H200 and **AMD Instinct MI-series**. Roughly **31%** went to buyers on the Pentagon's Chinese military companies list (Tencent 150k, Alibaba 75k, Baidu 43k, BYD). Former official Chris McGuire questioned whether Commerce conducted a serious national security review. NVIDIA executives testify Dec 1–2; **AMD is a plausible follow-on witness** and has not been called to date.

**Securities litigation (new, high probability):** **Rosen Law Firm** announced an AMD securities investigation on **Nov 19, 2026** — the same day as the short report — stating AMD "may have issued materially misleading business information." SBS Law issued a similar solicitation. The two-day decline (~15%) and ~$67B of erased market value create a textbook class-action setup. The core theory would be disclosure adequacy around **billings-location revenue versus end-destination/end-use risk**. No complaint has been confirmed filed as of Nov 20, 2026.

**Patent/IP:** Adeia's two patent suits over 3D V-Cache/Ryzen X3D were **settled in March 2026** via a license deal. **Nextech Semiconductor v. AMD** (W.D. Tex. 7:26-cv-00080) continues — AMD's NDA-based claims survived a sealed dismissal motion (Aug 2026); immaterial in size.

**Antitrust:** China's **SAMR** conditioned the AMD/Xilinx deal (2022) on **no-tying and FRAND supply commitments** — continuing obligations that give Beijing leverage. SAMR has since opened a probe into NVIDIA (Sept 2025), and press reports suggest Beijing is prepared to investigate more U.S. tech deals. AMD's **ZT Systems** acquisition ($4.9B) closed in 2025 with unconditional EU clearance; $300M contingent consideration settled Oct 30, 2025.

**Other alleged blacklisted ties:** AMD reported **$67M of licensing income in 2025** that Hunterbrook traced to two Chinese chip ventures blacklisted in 2019; its February 2026 catalog lists a server from **Cancon**, an alias of blacklisted **Suma**.

---

## 4. Compliance Red Flags

1. **Indirect-channel/transshipment exposure.** Aivres, Kaytus and Maginfra sit in AMD's own partner ecosystem while being structurally tied to an Entity-Listed firm. Aivres alone exported **$5.6B** of advanced technology to Southeast Asia (Apr 2024–Feb 2026). Billings-based revenue recognition means AMD may not know end use — a disclosure and enforcement vulnerability.
2. **Firmware/software support as a deemed export.** Post-blacklisting firmware updates reaching IEIT is the sharpest single allegation; if substantiated, it is an EAR violation independent of any chip shipment.
3. **Related-party concentration in China.** Tongfu-owned JVs handle the majority of AMD's assembly/test/packaging, with a $100M loan outstanding. This is both a supply-chain single point of failure and a technology-transfer question.
4. **Unanswered questions.** AMD declined to state whether it holds licenses covering the named entities — a disclosure gap that feeds both BIS and securities-litigation risk.
5. **Revenue-share arrangement.** Paying 15% of China AI-chip revenue to the U.S. government is unprecedented; expect accounting, disclosure and potential legal challenge.

---

## 5. Overall Geopolitical / Legal Risk Rating: **HIGH** (upper end — one notch below Very High)

**Why High, not Very High:** no confirmed export-law violation, no confirmed BIS enforcement action, no confirmed securities complaint, and AMD's largest single market is the U.S. (32.8%) with tariff exemptions that protect domestic data-center demand. Q3 2026 fundamentals remain intact ($13.4B revenue, +45%; Data Center $8.5B, +97%).

**Why not Medium:** ~50% of billings sit in exposed jurisdictions; a live short-seller allegation of Entity List violations is under public and congressional scrutiny; new licensing rules directly touch the 12.4% Singapore line; ~$800M of MI308 charges in 2025 establish precedent for real P&L damage; and a securities class action is now more likely than not.

**What would change the rating:**
- **To Very High:** a BIS subpoena/enforcement letter, a formal congressional inquiry naming AMD, or a filed securities class action tied to China disclosures.
- **To Medium:** the 50%-ownership rule being suspended again past Jan 10, 2027, plus a clean resolution of the IEIT firmware question and an extension of the U.S.–China truce past April 2027.

**Gaps in this assessment:** AMD's FY2025 10-K risk-factor text could not be retrieved directly (the filing tool returned no 10-K; the 10-Q excerpt returned only the SOX certification). Litigation detail is therefore drawn from dockets, law-firm notices and press coverage rather than the "Legal Proceedings" note. AMD's own China end-destination disclosure was not available — the billings-location figures materially understate true end-use exposure.
