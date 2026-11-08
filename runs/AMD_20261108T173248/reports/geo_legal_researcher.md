# Geo Legal Researcher

- Symbol: AMD
- Elapsed: 69.9s

---
# AMD — Geopolitical, Regulatory & Legal Risk Assessment

**Company:** Advanced Micro Devices, Inc. (NASDAQ: AMD) · Semiconductors · US-domiciled (Santa Clara, CA) · Market cap ~$733B · ~31,000 employees
**Assessment date:** November 2026 · Primary source documents: FY2025 Form 10-K (filed Feb 4, 2026), Q3 FY2026 Form 10-Q (filed Nov 4, 2026), BIS/White House rulemakings, court dockets, Reuters/FT/AP

---

## 1. Geographic Risk Map

FY2025 net revenue: **$34.6B** (record). International sales were **67%** of net revenue in FY2025 vs. 66% in FY2024 (FY2025 10-K).

| Geography | FY2025 Rev ($B) | % of Rev | FY2024 % | Trend | Risk Level | Key exposure |
|---|---|---|---|---|---|---|
| **United States** | 11.36 | 32.8% | 33.7% | Flat | **Low** | Tariff/export-control *policy originator*; Section 232 use-based exemptions favor US data-center deployments |
| **China** | 7.75 | 22.4% | 24.2% | Down from 2024 peak; 15.1% in FY2023 | **High** | License-gated AI chips (MI308/MI325X), USG revenue-share, Beijing import vetoes, retaliation risk |
| **Taiwan** | 5.19 | 15.0% | 12.8% | Rising fast (8.1% in FY2023) | **High** | Not demand — this is the *supply* chokepoint: TSMC leading-edge wafers + CoWoS packaging; ODM billing hub |
| **Singapore** | 4.28 | 12.4% | 14.0% | Stable | **Low-Med** | Regional HQ / distributor & ODM billing hub; destination-of-invoice, not end demand |
| **Other countries** | 6.06 | 17.5% | 2.2% | Up sharply | **Low-Med** | Europe, Japan, Korea, India, Israel R&D; Canada; FX/EM volatility |

Sources: FY2025 10-K geographic note (via Bullfincher compilation of 10-K FY2023–FY2025); total revenue per AMD Q4/FY2025 press release.

**Critical analytical caveat:** AMD bills by *shipment destination*, not end-customer domicile. A large share of "China" revenue is components sold to Chinese ODMs/board partners and to non-Chinese OEMs who assemble in China — so true China *end-demand* exposure is lower than 22%, but so is the visibility. Conversely, Taiwan's 15% is largely a pass-through of TSMC/ODM flows and understates real dependence: AMD is **fabless with a single leading-edge foundry**. This is the single largest geographic concentration in the business.

**Customer concentration is a mitigant:** "No customer accounted for at least 10% of the Company's consolidated net revenue in fiscal years 2025 and 2024" (FY2025 10-K) — though one Client & Gaming segment customer is disclosed at segment level, and the AI ramp is increasingly concentrated in a handful of hyperscalers (Q3 FY2026 data center revenue $8.5B, +97% y/y, per stocktitan/AMD Q3 release).

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — US–China AI chip export-control whiplash (Probability: 100% ongoing / Impact: High)
AMD's China business is now administered by license, not by market. The timeline is dense and shows *policy oscillation*, not a stable regime:

- **Apr 2025:** MI308 license requirement → ~**$800M** revenue hit.
- **Aug 2025:** Nvidia/AMD agreed to give the **US government 15% of China MI308 revenues** in exchange for licenses (FT, AP, CBS).
- **Dec 4, 2025:** CEO Lisa Su confirms licenses for some MI308 shipments and readiness to pay the 15% "tax" (Reuters).
- **Dec 8, 2025:** Trump authorizes H200-class sales to approved Chinese customers.
- **Jan 13, 2026:** **BIS final rule** — case-by-case review for Nvidia H200, **AMD MI325X** and similar, conditioned on: no diversion of global capacity from US customers, purchaser export-compliance procedures/customer screening, and **independent third-party US testing** (BIS press release). Reports indicate a **25% USG revenue share** attaches to this tier (Covington/Global Policy Watch).
- **Demand side is not the company's to control:** Chinese customs initially told agents H200 was "not permitted" (Reuters, Jan 14, 2026); Beijing has been "playing a tactical game of refusing to buy" MI308/H20; AMD excluded MI308 from its Q4 FY2025 guide, then booked ~$390M of MI308 China revenue in a later quarter (Morningstar). Nvidia has since guided **zero** China data-center compute revenue (Spheron/gpusmith); AMD's China line is lumpy and unforecastable.

**Assessment:** The risk is not "will controls bite" — they already have — but that **US and Chinese policy are both unilateral and mutually reinforcing**. A single BIS rule change can vaporize ~20% of revenue; a MOFCOM directive can do the same from the other side. Bipartisan scrutiny is live (Aug 2025 Krishnamoorthi letter to the President on the revenue-share arrangement), so the arrangement carries political/legal uncertainty of its own.

### Risk 2 — Taiwan Strait / foundry concentration (Probability: Low-Medium per year / Impact: Existential)
AMD is fabless. Leading-edge EPYC/Instinct wafer supply and advanced packaging come from TSMC in Taiwan. Taiwan is already 15% of billed revenue and rising. A blockade, quarantine, or kinetic event would halt AMD's AI ramp regardless of demand. Partial mitigants: TSMC's Arizona fabs, the **Jan 15, 2026 US–Taiwan trade deal** on reshoring (Global Policy Watch), and AMD's stated intent to diversify. None of these close the gap before 2028. Also note **Taiwan is itself weaponizing export controls** (proposed restrictions on 47 semiconductor products; tightened advanced-chip exports to China) — a new source of regulatory risk sitting in AMD's supply chain.

### Risk 3 — Section 232 tariffs and the "second phase" overhang (Probability: Medium-High / Impact: Medium)
**Proclamation 11002 (Jan 14, 2026)** imposed a **25% tariff** on a narrow band of advanced logic — parameters that explicitly capture **Nvidia H200 and AMD MI325X** — effective Jan 15, 2026. Critically:
- Use-based **exemptions** cover imports for US data centers, US R&D, startups, and non-data-center consumer uses (gaming, PC, workstation) — which shelters most of AMD's US-bound volume *if* documentation holds (CBP guidance on proof of end-use is still thin).
- **No drawback available**; the tariff stacks on MFN and Section 301 duties.
- The Proclamation explicitly reserves **"significant" broader tariffs** on all semiconductors and equipment, with a 90-day negotiation report and a **July 1, 2026** data-center market review. Commerce Secretary Lutnick has publicly floated **tariffs up to 100%** for chipmakers who do not invest in US capacity. Section 301 tariffs on Chinese semiconductors were deferred 18 months, not removed.

**Assessment:** Tariffs are being used as *leverage for onshoring*, so the base case is tariff-threat rather than tariff-shock — but the direction of travel is toward broader coverage, and AMD's supply chain (Taiwan wafers → Malaysian/Vietnamese assembly → US import) sits squarely in scope.

---

## 3. Legal & Regulatory Highlights

**Litigation inventory (no material accrual disclosed):**
- **Adeia Semiconductor Bonding Technologies v. AMD** — W.D. Tex., filed Nov 3, 2025 (7:25-cv-00511); ten patents asserted, including hybrid-bonding/3D V-Cache technology used in gaming chips; parallel D.D.C. miscellaneous action (1:26-mc-00004, Jan 20, 2026). **Settled March 9, 2026** (Reuters) — terms undisclosed. IP risk around advanced packaging is *structurally rising* as AMD leans on chiplets/3D stacking.
- **Consumer class action re alleged defective AMD CPUs (with HP)** — AMD's motion for summary judgment on plaintiffs' consumer-protection and implied-warranty claims was **denied Oct 29, 2025** (Hagens Berman case page). Modest dollar exposure; reputational and precedential nuisance value.
- **Securities litigation history:** AMD has successfully defeated prior securities class actions (Bloomberg Law) and a board-diversity derivative suit (Reuters, 2021). No AMD-specific AI-related securities class action was identified — but note the **2026 environment**: AI/"AI-washing" securities filings hit record levels (D&O Diary, Harvard CorpGov, Skadden). Given AMD's guidance for **>80% revenue growth in 2027** and >$1T-then-$733B market-cap round trip (Nov 5, 2026: -17% single day), the disclosure-risk surface is large. *Flag as watch item, not current contingency.*

**Regulatory:**
- Principal regulators: **BIS (Commerce)** on export licensing; **CBP** on Section 232 end-use exemptions; **USTR** (Section 301); **FTC/DOJ Antitrust** (sector-wide scrutiny of AI silicon); **MOFCOM/SAMR** in China (which has already found Nvidia in preliminary violation of China's anti-monopoly law — a precedent that could be extended to AMD as a competitive counterweight).
- **China's draft Financial Law / Anti-Foreign Sanctions Law** proposes counter-sanction powers (Geopolitechs, Oct 2026) — creating a genuine **conflict-of-laws** risk: complying with the US revenue-share/licensing regime could be characterized as complying with "improper restrictions."
- **Critical minerals:** China's suspension of its gallium/germanium/antimony export ban runs to **Dec 8, 2026** — a near-dated supply-chain trigger.

---

## 4. Compliance Red Flags

| Area | Status |
|---|---|
| **Export controls (EAR)** | **AMBER — the primary flag.** New license conditions require Chinese-purchaser screening, end-use verification, and third-party US performance testing. The 15%/25% revenue-share arrangements are unprecedented, contractually novel, and politically contestable — accounting treatment, enforceability and FCPA-adjacent "government fee" characterization are all unsettled. |
| **Sanctions (OFAC/Russia)** | **GREEN.** No material Russia/ Iran/ DPRK exposure disclosed; AMD exited Russia in 2022. No OFAC designation. |
| **FCPA / AML** | **GREEN.** No disclosed DOJ/SEC investigations. Channel/distributor risk in China is the theoretical vector, not a known issue. |
| **Data privacy** | **GREEN-LOW.** B2B silicon vendor; no consumer data at scale. EU AI Act/Data Act affects customers more than AMD directly. |
| **China entity-list / affiliates rule** | **AMBER.** The 50%-affiliates rule has been repeatedly suspended (extended to Jan 10 per Nikkei) rather than repealed — its reinstatement would sweep in Chinese customers currently deemed compliant. |

---

## 5. Overall Geopolitical/Legal Risk Rating

### **MEDIUM-HIGH** — with divergent sub-ratings:

| Dimension | Rating | Rationale |
|---|---|---|
| China / trade & export controls | **HIGH** | 22% of revenue license-gated; policy oscillating quarterly; revenue-share arrangements politically fragile; Beijing holds a demand-side veto |
| Supply-chain geography (Taiwan) | **HIGH** | Single-source leading-edge foundry + CoWoS packaging; no pre-2028 fix |
| Tariff exposure | **MEDIUM** | 25% Section 232 applies to MI325X, but use-based exemptions shelter most US-bound volume; "significant" phase-2 tariffs a live tail risk |
| Legal / litigation | **LOW-MEDIUM** | Adeia settled; no material accrual; consumer CPU case is small; AI disclosure-litigation environment is the watch item |
| Compliance / sanctions | **LOW** | No FCPA/AML/OFAC matters; export-control *process* burden is the cost, not a violation |

**What would move this to HIGH:** (i) BIS revoking or re-conditioning the MI325X/H200 licensing pathway (post-July 1, 2026 data-center review); (ii) China formally barring MI308/MI325X imports; (iii) reinstatement of the affiliates rule or new Chinese counter-sanctions on firms paying USG revenue shares; (iv) any Taiwan Strait quarantine; (v) an AMD-specific AI-disclosure securities class action following the Nov 2026 drawdown.

**What would move it to MEDIUM:** China revenue mix falling below ~10% via explicit exclusion from guidance (as Nvidia has done), plus Arizona-based wafer/packaging capacity coming online.

---

### Sourcing notes / gaps
Geographic splits are from AMD's FY2025 10-K geographic note as compiled by Bullfincher (10-K dates, FY2023–FY2025); AMD's own 10-K and 10-Q HTML could not be text-extracted through the available tools (inline-XBRL wrapper consumed the fetch), and the `10-K` filing-type lookup returned "no 10-K found" because the recent-filings feed only carries 10-Q/8-K/4. **The 10-K "Legal Proceedings" and risk-factor text was therefore not read directly** — the litigation inventory above is reconstructed from court dockets (Justia), Reuters/FT/AP reporting, and law-firm case pages, and should be confirmed against Item 3 of the FY2025 10-K and Part II Item 1 of the Q3 FY2026 10-Q before publication.
