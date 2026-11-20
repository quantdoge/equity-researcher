# Nonfin Risk Analyst

- Symbol: TEM
- Elapsed: 62.2s

---
I have sufficient evidence. Note the tooling gaps: `fetch_filing_text` returned "no 10-K/DEF 14A" for TEM and the EDGAR enforcement search was unavailable, so governance detail below rests on filing metadata, the S-1/424B4 disclosure trail, Form 4 records and press/litigation reporting rather than full risk-factor text.

---

# Tempus AI, Inc. (NASDAQ: TEM) — Non-Financial Risk Assessment

**Company snapshot:** Healthcare / medical information services; precision oncology diagnostics + data licensing. IPO June 2024, market cap ≈$9.8B, ~3,800 FTE, beta 3.61. Founder-controlled, loss-making on a GAAP basis.

## 1. Governance Quality Rating: **WEAK**

Evidence:

- **Dual-class control with 30:1 voting.** Per the 424B4 and the Personalis S-4/A, Class B common carries **30 votes per share** vs. 1 for Class A. Eric Lefkofsky (Founder, CEO, Chairman, 10%+ owner) controls the company via Class B and Gray Media/GRAT vehicles. Minority holders have effectively no ability to influence board composition, compensation, or M&A — including the $1.5B Personalis deal.
- **CEO/Chairman duality** — power concentrated in a single founder-executive, the textbook independence failure mode.
- **Board is independent on paper only.** Directors include Jennifer Doudna, David Epstein and Nadja West, and the Governance Guidelines promise a majority-independent board — but with 30:1 voting, "independence" is not enforceable by shareholders. (Proxy text could not be retrieved; committee composition unverified.)
- **Related-party concern in the Personalis transaction.** BFA is investigating "whether Tempus' prior relationship with Personalis caused related-party"-style conflicts, and KSF is investigating price/process adequacy. Personalis was a pre-existing Tempus collaborator — a supplier being acquired by its customer/controller is a classic conflict vector.
- **Insider alignment is poor in practice** (see §3): management sells heavily into strength, with no open-market buying.

## 2. Regulatory & Legal Risk Summary — **ELEVATED**

| Matter | Status | Risk |
|---|---|---|
| **Illinois GIPA class actions** (N.D. Ill., incl. 1:26-cv-04246, filed 4/15/26; earlier suits Feb 2026) | Active; consolidated-type claims | **Highest severity.** Alleges Ambry Genetics patient genetic data was transferred/integrated into Tempus models without proper consent post-$600M acquisition. GIPA carries **per-violation statutory liquidated damages**, so exposure scales with database size — potentially existential, not merely a fine. |
| **"AI-washing" securities class action** (N.D. Ill., filed 6/12/25) | Pending; multiple firms soliciting | Alleged misrepresentation of AI-derived revenue. Directly attacks the equity's core narrative. Also a 2025 stock-drop claim with an Aug-2024-onward class period. |
| **Personalis acquisition** ($1.5B, all-stock, $16.25/sh) | Pending PSNL shareholder vote + HSR/regulatory clearance; targeted late-2026/early-2027 | Delay/re-vote risk; Delaware appraisal and disclosure suits likely. S-4/A discloses a below-$46 walk-away dynamic. |
| **Reimbursement / FDA** | Structural | Revenue depends on Medicare ASP/PAMA and CPT coding; the ~$80M 2027 oncology ASP uplift is a policy-dependent assumption. xT CDx FDA approval and EU IVDR Class C certification for xR (Oct 2026) are positives but raise ongoing QMS/compliance obligations. |
| **Data privacy (GDPR/CCPA/HIPAA + state genetic laws)** | Structural | The GIPA suits are the template; other states with genetic-privacy statutes are natural follow-on venues. |

No active SEC/DOJ enforcement action was identified (EDGAR full-text enforcement search was unavailable — **gap, not clearance**).

## 3. Insider Activity Analysis — **HEAVILY NET SELLING, ZERO BUYING**

Across ~40 Form 4s reviewed (June–November 2026), there is **not a single open-market purchase**. Third-party aggregators put net insider sales at **~$90.5M over 90 days and ~$125.5M over six months**.

- **Lefkofsky (CEO/Chairman):** ~**$98M sold in 2026** across at least nine transactions — 250,000 sh @ $70.36 (10/27, $17.6M); 250,000 @ $77.47 (9/22, $19.4M); 200,000 @ $80.57 (9/17, $16.1M); 238,152 @ $68.39 (8/25, $16.3M); 132,591 @ $49.61 (8/18, $6.6M); 166,250 @ $57.48 (6/29, $9.6M); plus a $1.08M tax-withholding sale 11/17. Still holds ~36.1M shares (plus a 10M-share GRAT), so this is diversification, not exit — but it is relentless.
- **Broad-based, not idiosyncratic:** CFO Rogers (~$3.1M), CLO Polovin (~$2.2M), CAO Bartolucci (~$0.9M), CEO-Data Fukushima (~$11M+ across 10+ filings), CEO-Diagnostics Schoenherr (~$2.0M).
- **Directors selling:** Doudna, Epstein, West (small, ~$16K–$207K — consistent with RSU vesting/tax).
- **11/17/26:** five executives sold the same day at a uniform $63.02 — consistent with a coordinated 10b5-1/tax event, which softens the read on that single filing but not on the pattern.

**Interpretation:** much is likely pre-scheduled 10b5-1 and tax-related, which is normal. The signal is the *aggregate asymmetry*: $100M+ of supply, zero bids, into a stock that ran from ~$42 to ~$85. Insiders are de-risking at the same time the AI/data narrative is being litigated.

## 4. Top Operational Risks

- **Platform dependence on de-identified multi-modal data — consent provenance is the whole asset.** If the Ambry data cannot be used (injunction, remediation, re-consent), the Data & Applications segment's raw material is impaired. This is simultaneously a legal, operational and reputational risk.
- **Pharma customer concentration.** Data & Applications growth (33% YoY) rests on a small set of large partners — AstraZeneca, GSK, Merck, BMS, Moderna, Recursion, Pathos. Contract non-renewal or a partnership dispute would hit the highest-margin, highest-multiple segment hard, and the recently signed $193M/5-yr data agreements are lumpy and milestone-based.
- **Integration + compute execution.** Absorbing Ambry ($600M) and Personalis ($1.5B) while building AI infrastructure (management cites compute cost pressure) with a still-unprofitable GAAP P&L. Key-person concentration in Lefkofsky and in Ryan Fukushima (CEO, Data) — the latter is the most prolific seller outside the CEO.
- **Cybersecurity:** no disclosed material breach found, but the company holds one of the largest identified genomic/clinical repositories in the U.S. — a high-value target; breach would be an extinction-level reputational event given the privacy litigation already outstanding.

## 5. Reputational Risk Assessment — **ELEVATED**

- **"AI-washing" is the central reputational vector.** Having sold the market an AI story while generating most revenue from lab diagnostics, Tempus is exposed to the same credibility trap that hit other AI-branded issuers; the securities suit institutionalises that critique.
- **DNA privacy is a board-level reputational issue,** amplified by specialist oncology press (The Cancer Letter: "making a lot of people nervous" at cancer centers). The "de-identified means de-identifiable" argument is losing in public discourse — this could chill health-system partnerships, the exact distribution channel the diagnostics business needs.
- **Insider-selling optics** (CEO selling ~$19M weeks before/after a strong Q3 pop) will draw scrutiny if the stock retraces.
- **Offsetting positives:** genuine scientific credibility (Doudna on the board), top-tier pharma validation (Moderna/Merck neoantigen deal, BMS, ARPA-H award), IVDR certification, and legitimate clinical momentum (MRD volumes +300% YoY). Brand damage is currently a *legal/trust* problem, not a *customer-abandonment* problem.

## 6. Overall Non-Financial Risk Rating: **HIGH**

Governance is the binding constraint (30:1 founder control + CEO/Chairman duality + $100M of insider supply and no buys), layered on a **materially underappreciated GIPA liability** whose damages scale with the size of the asset that generates the company's data revenue, plus two live securities class actions. The business is operationally real and improving — this is not a fraud thesis — but the non-financial risk profile is well above what a 3.6-beta, ~$10B, GAAP-loss-making issuer with a super-voting founder deserves credit for.

## 7. Red Flags Requiring Escalation

1. **GIPA statutory-damages exposure (Ambry data).** Sizing is unquantifiable from public disclosure and the damages mechanic is per-violation. Request: outside-counsel reserve estimate and whether any restitution/injunction scenario impairs the Insights dataset. Not priced into consensus.
2. **Dual-class 30:1 control + CEO/Chairman duality.** Shareholders cannot constrain capital allocation, M&A, or compensation. Any ESG/governance-screened mandate should treat TEM as non-investable on governance grounds alone.
3. **$100M+ insider net selling with zero purchases**, including ~$98M by the controlling shareholder/CEO, into a 2x rally.
4. **Related-party/conflict taint on Personalis.** Pre-existing commercial relationship between acquirer and target, with plaintiff firms already probing process adequacy — treat as a disclosure-control and litigation-reserve issue.
5. **AI-washing securities suit** (N.D. Ill.) — tests the AI-revenue disclosure narrative and compounds with the privacy suits into a single "trust deficit" cluster.
6. **Reimbursement policy dependence** — the $80M 2027 ASP uplift and MRD economics hinge on CMS decisions outside management's control.

**Data gaps to close before IC:** full 10-K risk factors and DEF 14A committee/compensation detail (filing-text tool returned no documents), loss-reserve disclosure in the Q3 2026 10-Q MD&A, and confirmation of no open SEC/DOJ inquiry (EDGAR enforcement search was unavailable).
