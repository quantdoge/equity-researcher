# Esg Analyst

- Symbol: FROG
- Elapsed: 97.7s

---
# ESG ANALYSIS — JFrog Ltd. (NASDAQ: FROG)

**Sector:** Technology / Software–Application (DevOps & software supply-chain security) · **Domicile:** Israel (US-listed, HQ Sunnyvale CA) · **Market cap:** ~$13.1–13.9B · **Employees:** ~1,800 · **Revenue run-rate:** ~$717M (Q3-2026 rev $179.2M, +31% y/y) · **Analysis date:** Nov 2026

**Bottom line up front:** JFrog is structurally a **low-environmental-impact, high-human-capital-leverage business** whose most financially material ESG factor is *not* carbon — it is **product security and software supply-chain integrity**, an issue that sits at the intersection of Social (customer harm) and Governance (board cyber oversight). That risk crystallised in **August–September 2026** with an actively exploited, CVSS 9.8 authentication bypass in Artifactory (CVE-2026-82329, CISA KEV remediation deadline 5-Sep-2026), and it has **not yet appeared in the numbers** — Q3-2026 was a record quarter (stock +30% post-print, 52-week high). Governance is the relative weak spot: combined Chairman/CEO, founder dual-class control, and a staggered board. Net: ESG is **not a valuation driver here**, but it is a **tail-risk monitor**.

---

## 1. ESG Materiality Map

Materiality ranked for a subscription/consumption SaaS vendor selling into regulated enterprises. Weightings are my judgement of ultimate cash-flow / cost-of-capital linkage, not vendor ESG scores.

| # | Factor | Pillar | Materiality | Financial transmission channel |
|---|---|---|---|---|
| 1 | **Product & supply-chain security** (own code vulnerabilities, malicious-package detection) | S / G | **Critical** | Customer harm → churn, federal/regulated procurement exclusion, CRA/NIS2 liability, litigation |
| 2 | **Governance: founder control & board structure** (dual-class, CEO=Chair, classified board) | G | **High** | Cost of equity, index/ESG-fund exclusion, M&A veto asymmetry |
| 3 | **Human capital & Israel concentration** (~55% of staff in Israel; reserve duty) | S | **High** | Business continuity, R&D velocity, key-person risk |
| 4 | **Cyber governance & disclosure controls** (board cyber oversight, incident disclosure) | G | **High** | SEC disclosure exposure, reputational beta |
| 5 | **Executive compensation alignment** (founder-CEO/CTO pay packages) | G | Medium | Capital allocation, dilution |
| 6 | **Data privacy / GDPR** (customer metadata, telemetry) | S | Medium | Fines, DPA friction in EU |
| 7 | **Scope 3 / cloud & AI compute footprint** | E | Low–Medium | Energy cost pass-through, CSRD/SB 253 reporting cost |
| 8 | **Scope 1 & 2 emissions, water, waste, physical climate** | E | **Low** | Immaterial: no manufacturing, leased offices, no water/land exposure |
| 9 | **Supply-chain labour standards** (hardware/contractors) | S | Low | Minimal direct goods sourcing |
| 10 | **CBAM / stranded assets / carbon taxes** | E | **Not material** | No carbon-intensive assets or traded goods |

**Key insight:** an ESG screen built on emissions would rate FROG a "Leader" and tell you nothing. The material risk is that **JFrog's own security posture is its product** — a supply-chain-security vendor that suffers an exploited auth bypass faces a credibility tax that a generic SaaS peer would not.

---

## 2. Environmental Risk Assessment: **LOW**

- **Footprint:** Asset-light. Leased offices, cloud-hosted SaaS delivery (AWS/GCP/Azure-class infrastructure), no manufacturing, no owned data centres of scale, no water/land/biodiversity exposure. Scope 1 and 2 are de minimis in absolute terms.
- **Disclosure:** Publishes an annual GHG inventory across **Scope 1, 2 and 3** ("Sustainability Report 2025", fiscal 2025) and states cloud optimisation reduces "upstream impact and corporate costs." However, **absolute emissions figures, intensity metrics, and a base year were not retrievable** in machine-readable form from the report (PDF extraction failed; see Data Gaps). Company materials are qualitative on *ambition*.
- **Credible gap — no public net-zero / SBTi-validated target.** This is the single clearest E weakness for a company of this size and market cap. Peers of scale (MSFT, GOOGL-class) have validated targets; mid-cap SaaS increasingly does. FROG is behind on target-setting, though not on inventory.
- **Product-level positive:** JFrog's caching/dedup/compute-efficiency and "zero-touch remediation" features have a genuine **customer-side abatement** story (avoided network traffic and storage duplication), which is the more defensible climate narrative for a software vendor than its own footprint.
- **Estimates (mine, low confidence):** Scope 1+2 likely **<2,000 tCO₂e**; Scope 3 dominated by purchased cloud. Implied intensity on the order of **~15–40 tCO₂e per $M revenue** — among the lowest of any sector. Even a 4x carbon price shock would be immaterial to EBITDA.

**Verdict:** Environmental is a **reporting-cost and reputational item, not a cash-flow item.** Adds modest administrative cost as CSRD/California thresholds are crossed; no licensing or stranded-asset risk.

---

## 3. Social Risk Assessment: **MEDIUM**

**Positives**
- High-wage knowledge work; occupational injury risk structurally negligible; no unionised manufacturing footprint, no reported labour disputes or strikes.
- **Security-training discipline:** 99% completion rate on employee security-awareness training (self-reported).
- **Open-source citizenship is core to identity, not marketing:** Artifactory began as an open-source project; the company maintains large free-tier/community usage, and its Security Research team **first reported the Shai-Hulud npm worm (16-Sep-2025)** — a genuine public-good contribution that also functions as demand generation. Company claims **420,000 unique malicious open-source packages flagged**.
- Community programme: >2,700 employee volunteer hours; employee-led CSR committees by region.

**Risks**
1. **Geographic human-capital concentration (the key S risk).** Roughly **1,000 of ~1,800 employees are in Israel (~55%)**. During the October 2023 war, management stated **~15% of Israel-based staff were called up as reservists**. Mitigants: a large captive India R&D/base ("India kept JFrog running when war hit Israel") and Sunnyvale HQ. But a single-jurisdiction R&D concentration is a real continuity and velocity risk in a conflict-active region, and it is not diversifiable quickly.
2. **Product safety / customer harm — the dominant S factor.** CVE-2026-82329 (CVSS 9.8, authentication bypass in JFrog Access, unauthenticated admin takeover). Because Artifactory sits in the privileged position of the build-and-release pipeline, compromise enables **software-supply-chain manipulation at customers**, not merely data theft. Exploitation began within ~4 days of the 28-Aug-2026 patch; attackers minted admin tokens, enumerated users/credentials/federated trusts, and in some cases **created backdoor users**. Self-hosted (typically large enterprise/on-prem) customers are the exposed cohort; JFrog Cloud was vendor-remediated.
3. **Talent disclosure is thin:** no published turnover, engagement, or gender/ethnicity pay-gap data at the level institutional investors now request. Diversity metrics not disclosed in any form I could verify.
4. **Privacy:** Customer metadata in Artifactory/Xray is sensitive-by-association; GDPR exposure exists but no enforcement action found.

**Verdict:** Medium. No systemic labour or community-relations problem; the exposure is **concentrated, binary and reputation-linked** — a second exploited critical CVE inside 18 months would materially damage the security-vendor franchise.

---

## 4. Governance Quality Score: **6 / 10** (below peer-median for a US-listed software company)

| Sub-factor | Assessment | Direction |
|---|---|---|
| Board independence | ~7–8 member board with a **majority of independent directors** (Steele, Visoso, Zarmi, Zwarenstein, Sela) and an explicit **Lead Independent Director** role | ✓ |
| CEO / Chairman duality | **Shlomi Ben Haim is co-founder, Chairman AND CEO** — combined. Under Israeli Companies Law his service as both requires **shareholder re-approval every three years** (a structural check absent in the US) | ✗✗ |
| Shareholder rights | **Dual-class**: Class A = 1 vote, Class B = (reported) **10 votes**; co-founders Ben Haim and Landman hold Class B → insiders retain **effective voting control** on low-double-digit economics. Sunset provisions not confirmed | ✗✗ |
| Board accountability | **Staggered/classified board** (Class I/II/III, 3-year terms; four Class III nominees elected May-2026 to terms expiring 2029) — entrenchment mechanism, no annual declassification | ✗ |
| Compensation | Say-on-pay is **advisory and voluntary** (not legally required for an Israeli issuer) — a genuine pro-shareholder choice. But 2026 AGM included **separate votes to change CEO Ben Haim's and CTO Landman's compensation** — founder pay being re-cut annually is a watch item. Non-employee director equity raised from $200k→$250k for committee chairs | ~ |
| Audit & controls | **EY member firm (Kost, Forer, Gabbay & Kasierer)** ratified; dedicated **Audit Committee Financial Expert**; no restatements or material weaknesses found; clean going-concern-free reporting | ✓ |
| Ethics / anti-corruption | Global Code of Business Conduct, mandatory training, **quarterly internal-audit ethics reviews**, anonymous hotline tested quarterly, Audit Committee reports to Board quarterly | ✓ |
| Cyber governance | Notably, the 2026 director-comp proposal explicitly cites **"increased responsibilities such as cybersecurity oversight and AI-era governance"** as justification — evidence the board has formally taken on cyber oversight, though the CVE-2026-82329 timeline tests how effective that is | ~ |
| Third-party governance grade | Boardroom Alpha: **B–** | ~ |

**Rationale for 6/10:** Real institutional scaffolding (independent majority, lead independent director, empowered audit committee, voluntary say-on-pay, quarterly ethics auditing, shareholder votes on founder comp) is offset by three structural entrenchment features that standard governance screens penalise: **combined Chair/CEO, 10:1 founder dual class, and a classified board.** These reduce the probability of value-enhancing activism, M&A, or management accountability — directly relevant given the stock trades at ~19–20x sales and the thesis rests on execution, not optionality. Not a governance "laggard" (no self-dealing, no related-party abuse, no accounting concerns), but a clear step below best-practice US peers.

---

## 5. ESG Controversies (with financial impact estimates)

| Incident | Date | Severity | Financial impact estimate |
|---|---|---|---|
| **CVE-2026-82329 — Artifactory auth bypass (CVSS 9.8), actively exploited in the wild** | Patched 28-Aug-2026; exploitation from ~1-Sep-2026; **CISA KEV, federal remediation due 5-Sep-2026**; Cal OES cyber advisory issued | **High** | Direct remediation cost immaterial (<$5M). **Real risk is revenue-side:** ① possible exclusion/slowdown in US federal and regulated self-hosted procurement — I estimate **1–2% of revenue (~$8–15M) at risk** over 12 months; ② elongated enterprise deal cycles in the security-sensitive cohort; ③ potential customer class action and contractual liability claims, **$5–20M** plausible range, largely insured. **No evidence yet in results**: Q3-2026 rev +31% to $179.2M, $76M multiyear cloud deal signed, stock at 52-week high — the market is treating this as immaterial. Watch Q4 guidance language and net-retention on self-hosted. |
| **Shai-Hulud npm supply-chain worm** | Sep-2025 (and follow-on waves) | Positive | **First reported by JFrog Security Research.** Reputational credit and pipeline generation; no liability to FROG |
| **Israel–Hamas war / mass reserve call-up** | Oct-2023 onward | Medium | ~15% of ~1,000 Israel employees mobilised; continuity preserved via India. Cost not separately disclosed; embedded in opex. Ongoing geopolitical tail |
| **Securities class-action history (post-2021 IPO growth deceleration)** | 2021–2023 | Low/Unverified | **Could not verify docket or settlement via available tools** — flagged as an open item, not asserted. Marketing-related shareholder suits against Israeli issuers are common; assume de minimis |
| **Workforce restructuring** | 2023–2026 | Low | No JFrog-specific material layoff event identified in tech-layoff trackers; headcount ~1,800 and growing |
| **Environmental / pollution / bribery incidents** | — | **None identified** | $0 |

---

## 6. Regulatory ESG Exposure

| Jurisdiction / Regime | Applies? | Exposure & timing |
|---|---|---|
| **EU Cyber Resilience Act (CRA)** | **Yes — highest-priority item** | Products with digital elements sold in the EU fall under mandatory vulnerability-handling and **24-hour actively-exploited-vulnerability reporting** (Art. 14). Full application **11-Dec-2027**. This converts events like CVE-2026-82329 from a reputational problem into a **compliance obligation with penalty exposure**. JFrog must industrialise incident disclosure, not just patching |
| **EU NIS2** | **Yes (indirect)** | As a supplier to EU essential/important entities, JFrog will be pulled into customers' supply-chain security assurance (Art. 21) — an audit and procurement-cost item, and a competitive advantage for Xray/Advanced Security if executed |
| **EU CSRD (non-EU parent wave)** | **Probable, FY2028** | Triggers for non-EU groups with EU net turnover >€150M plus an EU subsidiary/branch. FROG's EU revenue is plausibly in that range; requires limited assurance on ESRS-aligned E/S/G data — **materially more rigorous than the current sustainability report** |
| **US SEC climate disclosure rule** | **No** | 2024 rule stayed and de facto abandoned under current SEC posture. Exposure is now reputational/investor-driven, not legal |
| **California SB 253 / SB 261** | **Approaching** | SB 253 applies at >$1B revenue doing business in CA. FROG (~$700M FY26) crosses this within ~1–2 years → **Scope 1/2/3 reporting with third-party assurance**. This is the single most concrete near-term E obligation |
| **US federal (CISA BOD 22-01 / KEV)** | **Yes** | Federal customers bind JFrog remediation SLAs to KEV deadlines — CVE-2026-82329 already triggered a 5-Sep-2026 federal deadline |
| **Israel: Companies Law 5759 / Securities Law** | **Yes** | Permits dual-class and classified boards (structural governance discount); mandates **triennial shareholder approval of CEO-as-Chairman** and shareholder votes on director/founder comp (checks absent in US practice); special tender-offer rules |
| **GDPR / CCPA** | Yes, routine | No open enforcement actions identified |
| **CBAM / carbon taxes / ESG-linked debt covenants** | **No** | No traded goods; no evidence of sustainability-linked borrowing. Convertible notes carry no ESG ratchets identified |

---

## 7. Overall ESG Rating: **AVERAGE**

**Rationale:** Best-in-class on Environmental (structurally low impact, full Scope 1/2/3 inventory) offset by **absent target-setting and thin quantitative E/S disclosure**; solid on Social with a **concentrated Israel human-capital exposure and an elevated product-security event**; and **below-peer Governance** (combined Chair/CEO, 10:1 founder control, classified board). This is not an ESG-risk name — there is no stranded-asset, pollution, labour-abuse, or fraud profile — but it is not an ESG leader either, and it would likely fail a strict "best-in-class governance" screen on structural grounds alone.

---

## 8. ESG Investment Implication: **NEUTRAL**

**ESG is not a driver of the FROG thesis; it is a tail-risk overlay. Do not pay for ESG, do not underwrite against it.**

**Why neutral, not negative:**
- Environmental factors are financially immaterial — no carbon cost pass-through, no compliance capex, no licence-to-operate risk. Rising CSRD/SB 253 reporting costs are rounding errors against a $13B market cap.
- Governance entrenchment is a **known and priced** feature of founder-led Israeli software issuers; it caps activism/M&A optionality but it is also the reason the franchise has been run for growth (31% growth at ~$700M scale). The 10:1 structure is a discount-rate annoyance, not an earnings risk.
- Social positives (open-source roots, first-responder security research, CRA/NIS2-driven demand for Advanced Security) are **commercially additive** — the regulatory trajectory on software supply-chain security is a **demand tailwind for Xray/Advanced Security**, which is the fastest-growing part of the story.

**Why not positive:**
- The one issue that could genuinely move the P&L is **product security**, and FROG just had a CVSS 9.8 exploited auth bypass in its flagship product (KEV-listed, federal deadline). At ~19–20x sales with a beta of 1.31, there is no valuation cushion for a credibility shock to the security franchise. A second exploited critical CVE, or disclosure of a customer breach originating in Artifactory, would compress the multiple far more than any carbon disclosure ever could.

**Monitoring triggers that would move me to NEGATIVE:**
1. Q4-2026/FY27 net-retention or self-hosted (Enterprise/on-prem) weakness, or federal deal slippage → confirms CVE converted to revenue damage.
2. Any customer breach traced to CVE-2026-82329 exploitation; class action filing naming JFrog.
3. Evidence the board's cyber-oversight committee is passive (e.g., no disclosure of incident-review process in the next proxy).
4. Sun-setting of Class B, or separation of Chair/CEO — would move Governance to 7–8/10 and the rating to **Leader**.

**Triggers that would move me to POSITIVE:** published net-zero/SBTi-validated target with quantified Scope 1/2/3 and intensity trend; declassified board + independent chair; quantified human-capital and diversity disclosure; formal CRA/NIS2-aligned vulnerability-disclosure programme (a genuine moat against GitLab/Wiz-style competition).

---

### Data Gaps & Confidence
- **SEC filings unavailable via tools** (10-K, 20-F, DEF 14A all returned "not found"; proxy PDFs returned unparseable binary). Board composition, independence percentages, exact Class B vote ratio (sourced as 10:1 from secondary references — *medium confidence*), founder voting-power percentage, and the FY2025 emissions **numbers** are therefore **not primary-sourced**. Figures above are corroborated from the company sustainability site, investor-relations governance pages, AGM/proxy summaries, and independent security reporting.
- **No peer-multiple or ESG-score benchmarking** was retrievable (sector peer list returned only mega-cap semis, not comparable mid-cap DevOps names such as GTLB, ESTC, DT, PD).
- Emissions intensity figures are **analyst estimates** and clearly labelled as such — not company disclosure.
- No environmental fines, bribery, or labour controversies were found in any search; absence of evidence here is reasonably strong given the company's size and coverage.
