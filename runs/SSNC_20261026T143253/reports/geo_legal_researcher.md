# Geo Legal Researcher

- Symbol: SSNC
- Elapsed: 89.3s

---
## SS&C Technologies (SSNC) — Geopolitical & Legal Risk Assessment

**Data note / gaps:** SEC.gov and investor.ssctech.com returned HTTP 403 on direct fetches, and the filing tool had no 10-K in its index (only the 30 Jul 2026 10-Q, which returned the CEO certification). Geography and segment facts below come from indexed excerpts of the **FY2025 10-K (`ssnc-20251231.htm`, accession 0001193125-26-076745)** and the Q3 2026 call. **I could not retrieve the FY2025 10-K "Legal Proceedings" note text** — litigation detail below is reconstructed from court/news sources, not the filing itself.

---

### 1. Geographic Risk Map

| Geography | Revenue exposure | Risk level | Basis |
|---|---|---|---|
| **United States** | ~67% (33% non-US in FY2025) | Low | 10-K: "we generated 33% of our revenues from clients outside of the United States" (FY2025) |
| **United Kingdom** | Disclosed as a **separate reporting geography** (implies materiality, conventionally >10%); precise % not retrieved | Low–Medium | 10-K geographic note discloses (a) US, (b) UK, (c) Europe ex-UK/MEA, (d) APAC & Japan, (e) Canada, (f) Americas ex-US |
| **Europe ex-UK, Middle East & Africa** | Combined EMEA bucket; not broken out publicly | Medium | Same note; DORA/operational-resilience regime applies |
| **Asia Pacific & Japan** | **$344.0M in FY2025**, +22.9% since 2023 — fastest-growing region | Medium | 10-K: "revenue from the Asia Pacific region has increased 22.9% to $344.0 million" |
| **Canada** | Separate geography; small | Low | 10-K geographic note |
| **India** | Not a revenue geography, but the **delivery backbone**: 10-K risk factor flags "substantial operations and a significant number of employees in India subject to regulatory, economic and political uncertainties" | **Medium–High** | FY2025 10-K risk factors |
| **LATAM (Americas ex-US)** | Small | Medium | 10-K geographic note |

**FX exposure:** ~**24% of revenues are in currencies other than the USD** (Q1 and Q2 2026 10-Qs) — GBP/EUR/CAD/AUD translation risk, partly natural-hedged by INR/GBP cost bases. Headcount 28,800; beta 1.09.

**Notable:** no material Russia/Ukraine revenue or asset disclosure surfaced; company has 22.9% APAC growth, so China/APAC exposure is rising but not disclosed as a separate line.

---

### 2. Top 3 Geopolitical Risks

**(1) India delivery concentration — the single largest structural geopolitical exposure**
- *Probability: Medium (disruption) / Impact: High.* SS&C runs large-scale fund accounting, transfer agency and healthcare claims processing out of India. Risks: state-level political/labour disruption, new data-localisation or cross-border data rules (RBI/MeitY), tax/transfer-pricing disputes, and wage inflation. Company's own 10-K names India as a specific sovereign risk.
- A 1-day outage in a fund-accounting centre is client-visible and contractually penalised; India concentration is also an increasingly common **DORA Art. 28 "concentration risk"** objection from EU clients.

**(2) EU/UK regulatory escalation as a "critical third-party" ICT provider**
- *Probability: High / Impact: Medium.* DORA (in force since Jan 2025) plus UK FCA/PRA operational-resilience rules put SS&C into a supervised vendor category: mandated contractual clauses, audit rights, exit plans, and (under DORA) fines up to 2% of global turnover for critical providers. SS&C's own Intralinks unit publishes DORA content, so the company is tracking it. Rising compliance cost + client-mandated audit/exit rights are a slow margin and contract-terms drag, and a supervisory finding would be reputationally material for a regulated-client franchise.

**(3) Sanctions/AML liability embedded in the Intralinks & GIDS franchise**
- *Probability: Low–Medium / Impact: High (tail).* Deal-room and investor-servicing platforms onboard counterparties from sanctioned or high-risk jurisdictions; SS&C is effectively a gatekeeper. A failure (unscreened sanctioned party in a Virtual Data Room, or an investor in a GIDS-administered fund) creates OFAC/EU sanctions and AML exposure and potential client attrition. Compounding this: new **agentic AI products (AI Gateway, WorkHQ — 900+ workflows, 200 agents in production)** create fresh EU AI Act / model-governance and data-residency questions.

**Secondary:** tariff/trade-policy noise is largely irrelevant to revenue directly (software/services), but SS&C is highly **beta to capital markets and private-markets activity** (its management cites "political tensions" as an M&A drag in its own 2026 dealmaker survey) — geopolitical shocks compress deal and AUM-linked revenue across GIDS/GlobeOp.

---

### 3. Legal & Regulatory Highlights

**Active/ongoing litigation cluster (adverse-party sources, 2026):**

| Matter | Forum / status | Read-through |
|---|---|---|
| **SS&C v. D.E. Shaw & Co.** (1:23-cv-09158, SDNY) | **Feb 2026: court granted D.E. Shaw judgment on the pleadings, dismissing SS&C's amended complaint**; D.E. Shaw's antitrust counterclaims dismissed as time-barred/Noerr-Pennington-protected | **Negative for SS&C** — its affirmative contract/antitrust theory failed on the pleadings. Suggests SS&C's aggressive licensing-enforcement posture is meeting judicial resistance |
| **SS&C Advent v. Advent AI** (trademark, filed Jun 2026) | Seeking injunction + unspecified damages (Reuters, 23 Jun 2026) | Offensive; brand-protection cost, low financial materiality |
| **SEI Global Services v. SS&C Advent / SS&C Technologies** (licensing/competition claims) | Pending | Peer-versus-peer licensing warfare; potential damages + injunction risk against Advent |
| **SS&C v. BNY Mellon** (Canada, 17-year data-licensing dispute) | Ontario CA found the bank breached data contracts; **2026 SCC 29** on spoliation | **Favourable to SS&C** on liability; establishes data-licensing enforceability |
| **Clearwater Analytics trade-secrets** (Cook County) | 2019 jury verdict: **$44M incl. $28M punitive** | Historic but establishes SS&C as a repeat IP litigant on both sides |
| **Eigo v. SS&C** (NY) | Employment discrimination | Routine; immaterial |

**Regulatory posture:** SS&C operates an SEC **clearing-agency exemption** (Release 34-76514), with a **withdrawal letter dated 6 Aug 2025** — indicates active engagement with SEC Trading & Markets on the scope of its registered activities. Its **ALPS Advisors** unit is an SEC-registered adviser and its fund-administration entities are supervised in the UK (FCA), Ireland, Luxembourg, Hong Kong, Singapore and Australia — i.e. multi-regulator surface, not a single-regulator company.

**No SEC/FCA/DOJ enforcement action, fine, or securities class action against SS&C surfaced in 2024–2026 searches.** No material FCPA/bribery matter identified.

---

### 4. Compliance Red Flags

- 🟡 **Sanctions screening in Intralinks/GIDS** — counterparty and investor onboarding is the highest-severity tail risk (OFAC/EU); no evidence of a control failure, but the surface is inherently exposed.
- 🟡 **India/APAC third-party and FCPA exposure** — large offshore headcount plus local sales/BPO intermediaries; standard FCPA/UK Bribery Act agent-diligence risk. No matter disclosed.
- 🟡 **GDPR / data-localisation** — Intralinks and healthcare claims data (HIPAA-adjacent, PHI) across EU, UK, India, Australia; cross-border transfer and breach-notification exposure.
- 🟢 **AI governance (EU AI Act)** — the new agentic-AI portfolio is being sold into "highly regulated workflows"; SS&C is marketing "governance built in from day one," which limits but does not eliminate first-mover documentation risk.
- 🟢 **Litigation-related disclosure risk** — legal costs and adverse rulings (notably D.E. Shaw) are absorbed in ongoing SG&A; none appears individually material to a $19.5B market cap / ~$6.7B revenue base.

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Rationale:** Two-thirds US revenue, no disclosed Russia/Ukraine or China-concentration exposure, and no live government enforcement action keep this out of High territory. What lifts it above Low is (a) a hard-to-replicate **India delivery concentration** that is exactly the profile EU/UK regulators now scrutinise as critical-vendor concentration risk, (b) a **multi-regulator footprint** (SEC, FCA, CBI, CSSF, HKMA-equivalents) across a 33% international revenue base, and (c) an **active IP/contract litigation cluster** in which the most recent substantive ruling (D.E. Shaw, Feb 2026) went against SS&C.

**Monitoring triggers:** any DORA/FCA critical-third-party designation; an OFAC/AML event at Intralinks; new Indian data-localisation rules; an adverse SEI or Advent AI outcome; and any 10-K disclosure of a material legal accrual (the FY2025 legal-proceedings note could not be verified here — **flag for the drafting team to pull directly before publication**).
