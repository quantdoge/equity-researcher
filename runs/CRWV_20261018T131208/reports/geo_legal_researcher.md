# Geo Legal Researcher

- Symbol: CRWV
- Elapsed: 241.6s

---
## CoreWeave (CRWV) — Geopolitical, Legal & Regulatory Risk Assessment
*As of ~19 October 2026. Sources: FY2025 10-K (filed 3/2/2026), company press releases, Reuters/WSJ/CNBC/Bloomberg coverage retrieved via search.*

### Company frame
CoreWeave, Inc. — AI "neocloud" GPU infrastructure; incorporated in Delaware, HQ Livingston, NJ; IPO 28-Mar-2025; ~$33.9B market cap; 2,189 FTEs; 51 active data centers (Motley Fool, 10/17/26). FY2025 revenue ~$5.13B (+168% YoY).

---

### 1. Geographic Risk Map

**Disclosure caveat (important gap):** CoreWeave reports "revenue by geography ... based on the address of the customer," and I was unable to retrieve the FY2025 *Geographic Information* note values (SEC.gov returned HTTP 403; the EDGAR XBRL mirror truncated before the geographic note). Revenue is **US-dominant** — historically substantially all revenue has been US-booked — but the exact FY2025 US/international split is **not verified here**. Treat percentages below as qualitative, not disclosed figures.

| Geography | Revenue exposure | Nature of exposure | Risk level |
|---|---|---|---|
| **United States** | Dominant (est. >85%, unverified) | All 51 live data centers; HQ/NJ; Delaware corp; federal regulatory & chip-policy nexus | **Medium-High** |
| **United Kingdom / EU** | Small but strategic (not disclosed) | European data-center footprint, GDPR + EU AI Act, energy permitting | **Medium** |
| **Middle East / APAC** | Not disclosed; new-contract optionality | Third-country diversion & export-control licensing risk on re-export of US GPUs | **Medium-High** |
| **China** | Effectively nil (direct) | Indirect only: NVIDIA supply chain, TSMC/Asia hardware lead times | **Low direct / High indirect** |

Client-address-based geography understates true risk: CoreWeave's **economic** exposure is to a handful of US-hyperscaler/AI-lab balance sheets, not to a diversified country map.

---

### 2. Top 3 Geopolitical Risks

**① US AI-chip export controls / NVIDIA supply-and-shareholder dependency — Probability: High (already binding) | Impact: High**
- NVIDIA is simultaneously **supplier, ~10% shareholder, and ecosystem partner** (Seeking Alpha, 10/16/26). Any BIS tightening changes what CoreWeave can resell and to whom.
- Policy direction is toward **stricter, whitelist-based control**: BIS has been closing third-country channels and NVIDIA has reportedly halved its list of authorized Asian AI-chip buyers; the Huawei ban was expanded to foreign-made chips using US technology. A neocloud that resells US-origin compute to non-US customers sits squarely in that enforcement perimeter — diversion/traceability failures are a strict-liability-style BIS risk.
- Secondary: TSMC/Asia packaging bottlenecks mean CoreWeave can be capacity-rationed by geopolitics it cannot influence ("CoreWeave Fails to Meet Nvidia Chip Demand").

**② Data-center permitting, power and local moratoriums — Probability: High | Impact: High**
- As of Aug 2026, moratorium legislation introduced in **at least 15 states** and **100+ local governments** have enacted outright moratoriums (McGuireWoods, 9/2026); Moody's warns **14 states are weighing statewide moratoriums in 2026**; Denver imposed a one-year moratorium (19-May-2026) and 500+ local governments have permit pauses.
- CoreWeave is unusually exposed because it **owns neither most of the property nor the power supply** for its sites (Motley Fool, 10/18/26) — it is a tenant of third-party landlords and dependent on utility interconnection queues and rate-case outcomes.
- This is the single fastest-moving legal risk to the >$100B revenue backlog: contracts are signed against capacity that may not get permitted.

**③ Customer concentration and "circular financing" political scrutiny — Probability: Medium-High | Impact: Very High**
- **Microsoft = ~67% of FY2025 revenue** (FY25 10-K, Item 1). Adding OpenAI (large backlog counterparty) makes CoreWeave a levered derivative of two balance sheets.
- Circularity (NVIDIA→CoreWeave→OpenAI/NVIDIA ecosystem) is now a **public-policy issue**: the CEO has had to publicly defend "circular deals," and CoreWeave's CEO appeared alongside OpenAI and Microsoft in Senate AI-infrastructure lobbying. Expect hearings, and possibly FTC/DOJ or SEC inquiry into AI-infrastructure deal accounting and related-party disclosure.
- **Core Scientific merger terminated 30-Oct-2025** after shareholders rejected the $9B all-stock deal (Reuters, WSJ). Core Scientific's own FY2025 10-K states **CoreWeave = 100% of its Colocation segment revenue** — a mutual hostage situation now governed by contract rather than ownership, raising renegotiation, dispute and landlord-leverage risk.

*Additional:* CoreWeave's 15% bond yields / record CDS spreads (CNBC 10/14/26; Bloomberg 10/16/26) mean a legal or regulatory shock now transmits directly into refinancing capacity — the credit channel amplifies every risk above.

---

### 3. Legal & Regulatory Highlights

| Matter | Status | Assessment |
|---|---|---|
| **Securities fraud class action (CRWV)** | Filed; class period **28-Mar-2025 → 15-Dec-2025**; lead-plaintiff motions filed 13-Mar-2026; ongoing (Kessler Topaz, Rosen, Bernstein Liebhard, ZLK) | Triggered by a **WSJ report on 15-Dec-2025**; shares fell 3.39% to $69.50 on 16-Dec. Typical post-IPO §10(b) claim; expect multi-year, modest direct damages vs. discovery/disclosure overhang. **Probable — but not individually company-threatening.** |
| **Core Scientific merger** | **Terminated 30-Oct-2025** (stockholder vote failed); no break fee resolution disclosed | Removes HSR/antitrust exposure; substitutes contract-counterparty risk |
| **Export controls (BIS/EAR)** | No company-specific enforcement action found | Structural, not event, risk — monitor customer end-use and re-export |
| **Data center / energy regulation** | State & municipal permitting regimes tightening (see risk ②) | Non-financial but backlog-material |
| **EU/UK**: GDPR, EU AI Act, energy rules | No CoreWeave-specific action found | Standard multinational compliance load |
| **Antitrust** | No open CRWV investigation identified | Low near term |

**Governance/compliance red flags (4):**
1. **Short public-company control history** — FY2025 10-K shows *"ICFR Auditor Attestation Flag: false"* and *Non-accelerated Filer* status; first SOX 404(b) audit still ahead. Disclosure-control failures are the usual precursor to a second securities suit.
2. **Massive insider selling** — 12 insiders sold >$5B in 12 months; three co-founders ~$3.3B since IPO (Finbold 10/18/26; 24/7 Wall St 10/17/26) — optics risk in any fraud litigation (scienter narrative).
3. **Related-party density** — NVIDIA equity stake + supply dependence; **Magnetar** appears as a lender (Magnetar Loan facility in the FY2025 debt note) to a company Magnetar helped incubate. Heightened related-party disclosure scrutiny.
4. **Legacy crypto-mining origin** (Atlantic Crypto Corp., 2017) — residual AML/KYC and reputational sensitivity on customer onboarding, plus散去 energy-market exposure.

---

### 4. Overall Geopolitical / Legal Risk Rating

**HIGH**

Rationale: no direct China/Russia revenue or sanctions exposure and no active government investigation — which keeps this out of "Very High." But the combination of (a) binding, tightening US export-control regime over its core input, (b) a national permitting backlash against exactly the asset class it is building, (c) 67% single-customer concentration, and (d) an active securities class action into a 15%-bond-yield capital structure is a genuinely elevated profile. Risk is **concentrated in US policy and credit contagion**, not in emerging-market country risk.

**What would move the rating:**
- ↓ To Medium: FY2026 US data-center permitting clarity + Microsoft concentration below ~50% + class action dismissed.
- ↑ To Very High: any BIS enforcement action touching CoreWeave customers, an SEC subpoena on backlog/related-party accounting, or a state-level moratorium hitting a named CoreWeave campus.

**Data gaps to close before the memo goes out:** FY2025 revenue-by-geography dollar split and long-lived-assets-by-country (FY25 10-K, *Geographic Information* note); FY2025 Item 3 *Legal Proceedings* full text; Q2/Q3 2026 10-Q updates on new litigation; confirmation of whether any CoreWeave customer is subject to a BIS Entity List designation.
