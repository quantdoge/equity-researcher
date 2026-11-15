# Geo Legal Researcher

- Symbol: AMD
- Elapsed: 91.5s

---
# AMD — Geopolitical & Legal Risk Assessment
*As of 14 Nov 2026 | Sources: AMD FY2025 Form 10-K (filed 4 Feb 2026), Q3 FY2026 earnings (3 Nov 2026), SEC filings, Reuters, WSJ, BIS/White House actions, congressional correspondence*

---

## 1. Geographic Risk Map

**Anchor fact:** International sales were **67% of net revenue in FY2025** (66% in FY2024) — AMD FY2025 10-K, Item 1. FY2025 revenue $34.6B; Q3 FY2026 revenue a record **$13.38B** (+45% y/y), with Data Center $8.55B (+97% y/y) now ~64% of revenue (AMD newsroom, 3 Nov 2026).

| Country / region | Approx. % of net revenue | Risk level | Driver |
|---|---|---|---|
| **United States** | ~33% | Low | Home market; Section 232 tariffs are inbound-cost, not market-access, risk |
| **China (incl. HK)** | **~22%** | **High** | Export controls (MI308 licences), 15% revenue-share to USG, China anti-sanctions/retaliation, domestic substitution |
| **Taiwan** | ~15% | Medium-High | *ODM/OEM ship-to*, not end-demand; but TSMC is AMD's leading-edge foundry — cross-Strait is an existential supply risk |
| **Singapore** | ~12% | Low-Medium | Distributor/regional hub; diversion risk if used as transshipment |
| **Other (Japan, Europe, Korea, India, Middle East)** | ~18% | Medium | Middle East sovereign AI (HUMAIN/G42) carries licence-condition risk; India is largest engineering footprint |

*Note on data quality: the FY2025 10-K geographic note discloses US / China / Taiwan / Singapore / Other countries only. Percentages above are from secondary aggregation of that note (bullfincher, cross-checked vs. the 67% international disclosure) — treat as ±2pp. The 10-Q text was not machine-retrievable (only the SOX certification exhibit was returned), so I could not verify Q3 FY2026 country mix directly.*

**Nuance that matters for the model:** Taiwan's 15% is *billing location*, not exposure — AMD sells to Taiwanese ODMs who ship globally. The real Taiwan risk is **single-source foundry dependence on TSMC**, which is not visible in the revenue table at all.

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — US–China export-control regime instability (Probability: High / Impact: Medium-High)
AMD holds licences for the **MI308** accelerator in China and has said it is **prepared to pay a 15% cut of China MI308 revenues to the US government** (Reuters, 4 Dec 2025; AP/FT). This is a *novel, non-statutory arrangement* — Commerce has described an "expectation" of the payment, not a codified rule.

Escalation vectors now live:
- The **Neal/Wyden congressional investigation** into the administration's "scheme to take a cut of Nvidia AI chip sales" opened **12 Nov 2026** — explicitly covers the arrangement AMD is party to.
- After the **Nvidia/Megaspeed diversion allegations**, lawmakers (Warren, Coons, Schumer, Foster) are pressing for **tighter China chip rules** (Reuters, 10 Nov 2026; Senate Banking letter, 11 Nov 2026). Nvidia's crisis is AMD's policy risk: tighter rules lift AMD's TAM in China but also its compliance perimeter.
- BIS rulemaking and Commerce Secretary Lutnick personally under scrutiny (Bloomberg, 12 Nov 2026) → **policy volatility, not directionality**, is the risk.

**Quantification:** AMD previously warned that losing China access for the export-compliant chip could cost **~$800M in revenue**. Actual China AI shipments have been small and lumpy: **$390M of MI308 revenue in Q4 FY2025**, guided to **$100M in Q1 FY2026 with no forecast beyond that** (Nikkei; Benzinga, Feb 2026), and **China Instinct revenue was excluded entirely from Q3 FY2026 results and Q4 guidance** (MarketWatch). Net: the China AI option is currently *priced at zero* — a re-licensing is upside, a further crackdown is largely already discounted. The durable exposure is the **~22% China base business** (client CPUs, embedded, gaming).

### Risk 2 — Taiwan Strait + Section 232 tariff/reshoring regime (Probability: Medium / Impact: High)
- A **Section 232 proclamation imposed a 25% tariff on a narrow set of advanced logic semiconductors effective 15 Jan 2026**, plus a **US–Taiwan trade deal** giving capacity-committed importers relief up to 2.5× planned US capacity (White House presidential action, Jan 2026; Global Policy Watch, Feb 2026). AMD, as fabless, must absorb or pass through duty on TSMC-sourced parts entering the US — a gross-margin and pricing issue, and a structural incentive to shift packaging/assembly onshore.
- Cross-Strait: China intensified diplomatic/maritime pressure on Taiwan through 2026 (Global Conflict Tracker; Asia Times, Nov 2026 — "Trump's midterm loss may harden China policy on Taiwan chips"). A blockade scenario is low-probability but **not survivable within a 12-month model horizon** for AMD's leading-edge roadmap (Venice, MI450/Helios all TSMC-dependent).

### Risk 3 — Sovereign-AI / Middle East licensing and customer concentration (Probability: Medium / Impact: Medium)
AMD's growth is now concentrated in a handful of AI customers — **Anthropic, Meta, Microsoft, OpenAI, Oracle** on first Helios racks, plus Google Cloud selecting EPYC for host infrastructure (AMD Q3 FY2026 highlights; Motley Fool, 14 Nov 2026). Middle East build-outs (**HUMAIN** Saudi Arabia, **G42/Core42** UAE — cleared for advanced US chip exports, and UAE moved to Country Group A:5 on 10 July 2026) are licence-contingent revenue. Risk: a single BIS licence suspension or a shift in the US–Gulf AI framework can remove a multi-billion pipeline overnight. Customer concentration also raises **credit/counterparty** risk on the OpenAI-type commitments.

---

## 3. Legal & Regulatory Highlights

**Litigation (manageable)**
- **Adeia Semiconductor Bonding Technologies v. AMD** (E.D. Tex.): two suits filed Nov 2025 alleging infringement of 10 patents, seven covering **hybrid bonding** used in 3D V-Cache (Ryzen X3D, EPYC). **Settled 9 Mar 2026** — AMD took a **multi-year licence** (Reuters, 9 Mar 2026). Cost is opex, not existential; but it establishes a precedent that AMD's stacked-cache roadmap carries a royalty layer.
- **UPC exposure:** AMD named in European Unified Patent Court actions (IAM Media; AMD/Bull, July 2026) — a newer, EU-wide injunction forum for chip IP. Watch item, not yet material.
- **Securities class actions:** a long-running AMD shareholder case settled historically (**$29.5M**, 2014 class period — Levi & Korsinsky/ZLK); Motley Rice maintains an AMD settlement recovery page. AMD's 10-K states management believes current litigation **will not be material**. No new AMD-specific AI-disclosure class action identified — note that the 2026 "AI spending" securities suits I found target Rackspace, not AMD.
- **Item 3 (Legal Proceedings)** in the FY2025 10-K runs only to p.44 and reaffirms immateriality — consistent with a company that litigates as a defendant in patent matters rather than as an antitrust target.

**Regulatory posture**
- Regulators that matter: **BIS/Commerce** (export licences — dominant), **US Treasury/OFAC** (sanctions screening of Gulf/China customers), **SAMR** (China merger control — relevant only if AMD pursues large M&A; SAMR has become more interventionist, with five conditional clearances in 2025 including Synopsys/Ansys), **EU/EC** (merger and DMA-adjacent), and **CFIUS** for any US inbound.
- **Section 232** semiconductor tariffs (25% on advanced logic, Jan 2026) and the Taiwan agreement are the live trade-law items affecting COGS.
- No active FTC/DOJ/EU antitrust case against AMD was identified. AMD is a *complainant-by-implication* beneficiary of scrutiny on Nvidia, not a target.

**Compliance red flags**
1. **The 15% China revenue-share arrangement** — a *quasi-licence fee to a foreign government's executive branch* with no clear statutory basis. This is the single most unusual compliance fact pattern at AMD. Congressional investigation is open; the arrangement may be challenged legally, and it creates disclosure/controls obligations (is it a tax? a fee? a contingent liability?).
2. **Diversion/transshipment risk** — AMD sells ~12% of revenue into Singapore and ~15% into Taiwan ODM channels. Post-Megaspeed, DOJ is actively pursuing AI-chip diversion to China. AMD's distributor/ODM chain is a plausible enforcement surface; any BIS inquiry would be a headline risk even without findings.
3. **China retaliation exposure** — China's Anti-Foreign Sanctions Law, MOFCOM export controls on 16 US entities (suspended/extended repeatedly through Nov 2026), and new draft trade-secret rules targeting foreign firms (MOFCOM, 26 Oct 2026). AMD's Suzhou/Penang assembly-and-test JV (disclosed as "ATMP JV" in the FY2025 10-K) and its China R&D footprint are within reach of Chinese countermeasures.
4. **Defense/aerospace revenue in Embedded** — Embedded grew 29% y/y "led by growth in aerospace and defense." That brings ITAR/EAR obligations, DDTC touchpoints, and reputational/ESG screen exposure not present in AMD's historical profile.
5. **FCPA/AML** — no disclosed FCPA matter. But Gulf sovereign counterparties (HUMAIN, G42) plus government-adjacent revenue are exactly the profile where third-party diligence becomes examinable.

---

## 4. Overall Rating

### **Geopolitical/Legal Risk: HIGH** (leaning High, not Very High)

**Reasoning:**
- **High** because ~22% of revenue sits in the single most contested bilateral relationship in tech, a 25% Section 232 tariff now taxes AMD's TSMC-sourced flow into the US, and leading-edge supply is concentrated in a jurisdiction with credible blockade tail risk.
- **Not Very High** because the acute China AI exposure is *already de-risked* — AMD excludes China Instinct revenue from guidance, has publicly framed the downside at ~$800M, and holds licences rather than prohibitions. Legal risk is genuinely contained: the only live IP matter (Adeia) settled to a licence, no antitrust target status, no FCPA/DOJ investigation disclosed, and management explicitly deems litigation immaterial.
- **Direction of travel is negative, not stable.** Three of the four live policy threads (Megaspeed fallout, the Neal/Wyden probe of the 15% deal, Taiwan tariff architecture) resolved *against* AMD's interest within the last 30 days.

**What would move this to Very High:** (a) formal BIS tightening that captures AMD's China client/embedded business (not just Instinct); (b) the 15% revenue-share being unwound as unlawful, forcing licence renegotiation; (c) any AMD distributor named in a diversion enforcement action; (d) PRC countermeasures reaching AMD's ATMP JV.

**Watch items next 90 days:** Commerce/BIS rulemaking following the Nvidia scandal; Neal/Wyden document requests reaching AMD; Q4 FY2026 China commentary on the 3 Feb 2027 call; any Helios/Middle East licence conditions.

---
**Data gaps (disclosed):** (i) Q3 FY2026 10-Q Item 3 and geographic note not retrievable — SEC EDGAR returned 403 and the filing tool returned only the SOX certification; (ii) FY2025 country percentages are secondary-sourced, not read directly from the filing table; (iii) no AMD-specific China antitrust (SAMR) or EU merger matter identified because none appears to be live — absence of evidence, not verified absence.
