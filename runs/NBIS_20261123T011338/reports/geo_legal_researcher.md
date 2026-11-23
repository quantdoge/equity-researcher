# Geo Legal Researcher

- Symbol: NBIS
- Elapsed: 55.4s

---
## NBIS — Geopolitical & Legal Risk Assessment
**Nebius Group N.V.** | CIK 0001513845 | ISIN NL0009805522 | Amsterdam, NL | Mkt cap ~$19.5B | Price $81.31

---

### 1. Geographic Risk Map

**Important basis-of-estimate note:** Nebius does not publish a clean revenue-by-geography table in its 6-Ks, and the FY2025 20-F was not machine-readable via my tools (SEC returned HTTP 403 on direct fetch). I have therefore triangulated from (a) long-lived assets by jurisdiction disclosed in the Q1 2026 6-K exhibit, (b) disclosed data-center locations, and (c) the location of the counterparties behind its largest contracts. Percentages below are **analyst estimates**, not reported figures — treat as directional.

| Jurisdiction | Asset/Revenue Exposure (est.) | Basis | Risk Level |
|---|---|---|---|
| **United States** | ~35–45% of revenue; ~35% of long-lived assets ($4,558.8M at 3/31/26) | Microsoft $17.4B/5yr dedicated-capacity deal served from Vineland, NJ; Birmingham, AL site; largest asset base | **Medium-High** |
| **Finland** | ~20–30% of delivery capacity; 310 MW owned campus (Mäntsälä / Lappeenranta, ~$10B) | Only wholly-owned data center; largest European asset | **Low-Medium** |
| **Israel** | ~15–25% of delivery capacity; Beit Shemesh + Mega Or lease (+134 MW, 7yr + 5yr option, completion Q2 2028); R&D (Avride, Toloka) | Active conflict zone; lease-dependent, not owned | **High** |
| **Netherlands** | ~$2,910.8M long-lived assets; HQ, tax residency, incorporation | Domicile, not a major delivery market | **Low** (but see tax/policy) |
| **France** | 240 MW Lille AI factory (development) | Announced build-out | **Low** |
| **UAE / Middle East (ex-Israel)** | Small, growing; "Middle East" named in footprint | 6-K footprint disclosure | **Medium** |
| **Russia** | **Nil — divested** | Russian businesses sold July 2024, ~$5.4B; discontinued ops | **Low residual / residual stigma** |

**Footprint, verbatim:** *"The Group's data center footprint spans Europe, the United States and the Middle East, and comprises its owned data center in Finland, leased…"* (Q3 2026 Form 6-K, filed 11/12/2026).

---

### 2. Top 3 Geopolitical Risks

#### Risk #1 — US remote-access export controls (BIS Interim Final Rule, Nov 16–19, 2026)
**Probability of material impact: High (70–80%) | Impact: High**

This is the single most important geopolitical fact about NBIS and it is *days old*. On November 16, 2026, BIS filed an interim final rule, effective on Federal Register publication November 19, 2026, creating **15 C.F.R. § 744.24** — an end-use control requiring a license to export, reexport or in-country transfer advanced computing items **worldwide** where the supplier has *knowledge* that the items will be used in a data center providing "significant compute" above a **12,000,000 aggregate TPP threshold** to companies headquartered in, or whose ultimate parent is headquartered in, **Country Group D:5 or Macau** (MoFo client alert, 11/19/2026).

Three features make this existential-adjacent for a neocloud:
- **The 90-day cliff.** § 744.24(b)(3) states that data centers *already* providing significant compute to D:5/Macau-headquartered companies before publication must obtain a license **within 90 days** of the effective date — i.e., roughly **mid-February 2027** — or "face future export restrictions." Nebius must now prove to BIS that no Chinese-headquartered tenant sits above threshold on its Finland, France, Israel, or US estates. Its customers rent *anonymous cloud capacity*; that is precisely the diligence problem the rule targets.
- **Aggregation across "linked data centers."** Multi-site operators must assess whether networked facilities count as a single data center for the 12M TPP threshold. Nebius operates a *single logical cloud* across Finland, France, Israel and the US — the worst-case reading of this provision captures it.
- **Loss of the AI Diffusion Rule** (formally rescinded, including license exceptions and ECCN 4E091 for model weights) removes prior clarity while the IFR makes "significant but contestable assertions about the legal status of prior AI data center deployments that involved remote access by D:5/Macau-headquartered companies" (MoFo). Retroactive-looking language is the tail risk.

Secondary: the same IFR imposes new license requirements for advanced computing items to **Indonesia, Malaysia, Singapore, Brazil and Thailand** (with an exclusion for qualifying US-headquartered end users), constraining any future Nebius expansion into Southeast Asia — a natural growth region for AI capacity.

*Mitigant:* BIS is accepting public comment for 60 days (to **January 19, 2027**), and the rule is an *IFR*, not final — trade-association engagement can still move thresholds. Nebius's customer base is overwhelmingly US/Western (Microsoft, Meta), which is favorable. But the compliance cost is real and non-optional.

#### Risk #2 — US policy turn against offshore AI build-out / "data center inversion"
**Probability: Medium (40–50%) | Impact: High**

On Friday, November 20, 2026, President Trump said US companies would be **banned from building data centers abroad or face a "tremendous tax"** if they do, explicitly naming Meta and framing it as keeping AI leadership in America against China (CNBC, Axios, Politico, Newsweek, all 11/20/2026). This landed the same week as NBIS's ~16% single-day decline.

Nebius is structurally on the wrong side of this policy vector in three ways, even though it is a *Dutch* company and not nominally a "US company":
1. Its growth plan is disproportionately **European** — a 310 MW Finnish campus (~$10B) and a 240 MW French campus — meaning its barrels sit exactly where US policy now wants to *discourage* deployment.
2. Its **counterparties are US hyperscalers**. If Washington taxes or restricts Microsoft/Meta building abroad, those customers redirect capex to US soil, and NBIS's European capacity loses its anchor tenants.
3. The company's willingness to domicile in the Netherlands while selling to US customers invites the "inversion" framing regardless of legal form.

Nebius guides to **$27B of 2026 capex** and **$40–45B of 2027 capex** (Zacks, 11/19/2026) — a bet on 3 GW of global capacity announced largely *outside* the US. That plan's geographic premise is now a live policy variable rather than a settled assumption.

#### Risk #3 — Israel operational and conflict exposure
**Probability: Medium-High (60%) | Impact: Medium**

Israel is one of three named delivery regions and hosts material R&D (Avride autonomous driving, Toloka data operations, plus the historic Yandex Israel R&D base). Nebius is expanding aggressively there: a **134 MW lease expansion with Mega Or**, seven-year term plus a five-year option, with Beit Shemesh under construction and completions targeted by **Q2 2028** (DatacenterDynamics, Nov 2026).

The risk is *leased, not owned* capacity in an active conflict zone: physical security of facilities, call-up of technical staff, insurance repricing, and the possibility of tenant relocation demands. Because the capacity is leased, Nebius cannot easily redeploy the capital. Note the timeline mismatch: capacity contracted for 2028 under a 7-year lease while the underlying security environment is re-priced annually. Middle East escalation also drags in the UAE/Gulf portion of the footprint.

---

### 3. Legal & Regulatory Highlights

**Pending litigation**
- **Regions Bank shareholder suit (Sept 2026).** A Regions Bank shareholder is suing over a **$66 million loss** after land tied to Nebius's **Birmingham, Alabama** data center site was flipped three times (WRBC, 9/9/2026). Nebius is not obviously the defendant, but its site selection is the proximate cause of the dispute and its name is in the caption-adjacent facts. Watch for discovery spillover into how Nebius sources land — a reputational and diligence issue as it scales to dozens of sites.
- **Securities class action exposure — elevated.** Nebius's own 20-F carries the standard warning that "companies that have experienced volatility in the market price of their shares have been subject to securities class action litigation." That boilerplate is now materially live: the stock is **~72% below its June 2026 record** (from ~$290 to $81.31), it missed the timing of its own **$7B ARR target by two months**, and Q3 included **$325.1M of "strategic partnership" revenue that management itself flags as potentially non-recurring**. A >70% drawdown on a guidance slip plus non-recurring revenue concentration is the classic fact pattern for a 10b-5 filing. Probability of a suit within 12 months: **moderate-to-high**.

**Regulatory posture**
- **BIS/export controls** — the dominant regulator now (see Risk #1). Nebius must stand up a customer-diligence function capable of attesting, to BIS's heightened evidentiary standard, the *headquarters and ultimate parent* of every tenant consuming >12M TPP. The IFR explicitly raises diligence standards and requires exporters to obtain information from foreign data centers about the data center's own customer diligence.
- **Dutch/EU layer** — Dutch incorporation subjects NBIS to EU AI Act obligations, GDPR, the EU Foreign Subsidies Regulation (relevant given state-linked customer prepayments), and Dutch FDI/security screening for its data-center assets. EU sanctions on Russia remain a live compliance perimeter given the Yandex lineage.
- **SEC disclosure** — foreign private issuer on Form 20-F/6-K. Note the absence of a 10-K/10-Q cadence means less frequent disclosure than US peers, a governance discount some investors apply.

**Capital structure as a legal contingency**
Contractual cash requirements were **$1,285.5M within 12 months and $32,891.9M beyond**, with lease amounts including facilities not yet commenced and convertible notes assumed unconverted (Q3 2026 6-K). Nine-month customer advances inflated deferred revenue by **$7,829.0M**, and quarterly interest expense jumped to **$112.5M** from $14.7M. Net debt/adjusted EBITDA has been reported at ~8x. The company raised **$3,908.5M from treasury-share sales** and **$2,000.0M from pre-funded warrants** in nine months, plus exchanged notes for 15,770,124 ordinary shares — meaningful dilution and a financing structure whose enforceability across Dutch/US/Israeli law adds cross-border litigation surface if counterparties dispute prepayment terms in a downturn.

---

### 4. Compliance Red Flags

1. **🚩 Customer-of-customer opacity under § 744.24.** Nebius sells anonymous compute. The new rule demands knowing the ultimate parent HQ of tenants at a 12M TPP threshold, aggregated across "linked data centers," with a mid-February 2027 compliance deadline. This is the highest-probability enforcement exposure in the file.
2. **🚩 Residual Russia nexus.** The $5.4B divestment closed July 2024 and founder-CEO Arkady Volozh's EU sanctions were lifted in early 2024 — but the company's engineering base, shareholder register and brand history remain partly Russian-linked, and it trades under a "is Nebius a Russian company?" cloud. Secondary-sanctions and reputational screening by US government customers is a live sales-cycle friction. No OFAC/SEC enforcement action against NBIS was identified.
3. **🚩 Related-party / "strategic partnership" revenue.** $325.1M of Q3 revenue (33%) came from "strategic partnerships" that management concedes may be non-recurring. Combined with **$17.4B Microsoft** (up to $19.4B) concentration, disclosure-quality and customer-concentration risk are both elevated.
4. **🚩 Offshore-buildout tax policy.** No enacted statute yet, but a presidential threat to tax US companies' foreign data centers, aimed at companies Nebius counts as customers, is a disclosure-worthy contingency.
5. **Data privacy/AI:** EU AI Act + GDPR obligations across Dutch, Finnish, French and Israeli processing locations; Israeli data-transfer adequacy adds complexity to the Israel cluster.

---

### 5. Overall Geopolitical / Legal Risk Rating: **HIGH**

**Rationale.** Nebius is not a high-risk *jurisdiction* story — its assets sit in the Netherlands, Finland, France, the US and Israel, all investment-grade rule-of-law environments. It is a high-risk **policy-perimeter** story. The company's entire product is advanced US-origin compute rented across borders, which places it precisely at the intersection of the two most active US policy levers of November 2026: the BIS remote-access rule of November 16 and the President's November 20 threat against offshore data centers. It carries a **90-day regulatory compliance cliff**, a **>70% drawdown** that invites securities litigation, **33% of quarterly revenue flagged as potentially non-recurring**, **~$33B of forward contractual obligations**, and a **7-year lease in a conflict zone**. Diversification across five jurisdictions is genuine and offsets country-specific risk; the concentration is thematic, not geographic — and thematic concentration does not diversify.

**Upgrade triggers:** favorable amendment to § 744.24 during the comment window closing January 19, 2027; a definitive, uncontested new US hyperscaler contract sourced from US soil; no securities suit filed by mid-2027.
**Downgrade triggers:** any BIS inquiry or licence denial; a formal 10b-5 complaint; enacted offshore-data-center tax legislation; Israel escalation affecting Beit Shemesh construction timelines.

---

### Sourcing & Gaps

**Sources:** Nebius Q3 2026 Form 6-K (filed 11/12/2026, via StockTitan); MoFo client alert on the BIS IFR (11/19/2026); BIS press release and WilmerHale/Wiley/Akin Gump/Gibson Dunn/Steptoe analyses of the 11/16/2026 IFR; CNBC, Axios, Politico, Newsweek (11/20/2026) on the Trump data-center tax threat; Reuters (3/31/2026) on the $10B Finland campus; DatacenterDynamics (Nov 2026) on the Israel Mega Or expansion; WRBC (9/9/2026) on the Regions Bank suit; Nebius newsroom on Microsoft and Finland/France projects; Zacks (11/19/2026) on the $27B 2026 capex guide; Cision/Reuters (7/15/2024) on the $5.4B Russia divestment.

**Gaps acknowledged:** (1) No audited revenue-by-geography table — the FY2025 20-F could not be retrieved (SEC 403); my exposure percentages are triangulated from long-lived assets and customer locations, not reported revenue. (2) No SEC/DOJ/FTC investigation into NBIS was located in searches — absence of evidence, not evidence of absence. (3) The Q3 2026 cash-flow statement and full risk-factor text were only available in summarized form. Recommend the analyst pull the 20-F directly from EDGAR and request the customer-jurisdiction diligence policy ahead of the February 2027 licence deadline.
