# Nonfin Risk Analyst

- Symbol: ZM
- Elapsed: 84.8s

---
# Non-Financial Risk Assessment — Zoom Communications, Inc. (ZM)

**Price context:** $83.48 (close 11/20/26); 52-wk range $70.70–$114.74; −27% from the 6/1/26 high of $114.74. The 11/19 drop (−9.6% to $83.82 on 5.9M shares, 2x normal volume) coincided with a broad AI/tech selloff ("Nasdaq falls 2% as Anthropic IPO fails to resuscitate AI trade") ahead of 11/23 Q3 earnings — **I found no company-specific adverse event explaining it.** Market cap ~$24.3B.

---

## 1. Governance Quality Rating: ADEQUATE (structurally constrained)

**Evidence:**
- **Combined Chairman/CEO + founder control.** Eric Yuan is founder, President, CEO *and* Chairman (since 2011), so the board chair is not independent. Dual-class structure: Class B carries 10 votes; Yuan holds ~7% of shares but roughly **32–38% of voting power** (sources conflict: ~32% per one analysis, 37.7% of total vote / 72.6% of Class B per 2026 proxy summaries). Minority holders cannot meaningfully contest control.
- **Board independence is otherwise reasonable.** Class I nominees elected 6/11/26: Yuan and Lt. Gen. H.R. McMaster. Named directors include Jonathan Chadwick (ex-VMware CFO), Dan Scheinman (ex-Cisco), Santiago Subotovsky (Emergence Capital), Jeff Epstein, plus Yuan/McMaster — a credible mix of SaaS, finance and national-security expertise. Yuan also sits on Intuit's board (outside commitment disclosed in proxy).
- **Vote outcomes are mostly strong but contain one sharp outlier.** Yuan 93% for (26.4M withheld); auditor ratification 99.7%; say-on-pay **93% for** (up from 81% in 2025). But **McMaster received only 77% — 22.7% withheld**, which by standard thresholds is *significant* dissent against a named director.
- **Compensation is unusually low-leverage for a founder-CEO.** FY26 CEO total pay $1.28M (−63% YoY from $3.43M), pay ratio **7.8:1** (median employee $165k), equity only 36% of pay ($464k in awards). Alignment comes almost entirely from Yuan's ~41.3M-share (~$3.4B) holding, not from ongoing incentive design. Company is shifting from 4-year to annual refresh grants in FY27 — mildly positive for retention/alignment.
- **No proxy access, dual-class sunset, or shareholder proposals on the 2026 ballot** (4–5 items only) — an insular ballot.

**Assessment:** Clean of scandal and free of related-party red flags, but concentrated control and non-independent chair cap the rating. Watch for a contested say-on-pay or a dual-class sunset proposal as the natural activist vector.

## 2. Regulatory Risk Summary — MODERATE (structural, not acute)

- **SEC enforcement: none found.** EDGAR full-text search for enforcement actions mentioning ZM returned zero results.
- **Live FTC consent order (Nov 2020) is the dominant structural exposure.** No monetary penalty, but it runs **20 years (to 2040)** and requires biennial independent privacy/security assessments and bars misrepresentation of privacy/security practices. This remains an open compliance perimeter, not a closed historical matter.
- **AI data use is the most probable next enforcement vector.** The 2023 terms-of-service/AI-training controversy (GDPR/ePrivacy questions raised by EU counsel; service-generated-data definitions) forced a terms rewrite. In 2023 the **CAIDP filed an FTC complaint alleging Zoom's ML services violated the existing consent order** — a repeat-violation theory that remains live as Zoom expands agentic AI, AI Companion, and a "federated AI architecture" with third-party models. EU AI Act GPAI obligations and data-sovereignty/localization regimes add cost.
- **Securities litigation: resolved.** *In re Zoom Securities Litigation* — **$150M settlement, final approval 11/10/25**; no active securities class actions found. This reduces overhang but is a reminder of disclosure risk tied to growth and security representations.
- **Telecom perimeter widening.** Zoom Phone (in 29% of Meetings enterprise accounts) carries e911/nomadic-emergency-calling and carrier-licensing obligations across jurisdictions — a new regulated business line layered onto a software company.
- **China-origin legacy.** Citizen Lab/DHS findings and the admitted "mistaken" routing of calls through Chinese data centers (2020) remain a latent geopolitical/ procurement disqualifier for government and defense accounts.
- *Gap:* `fetch_filing_text` returned no 10-K/10-Q and SEC/IR URLs returned 403, so I could not read current risk-factor language directly; the above draws on secondary sources and precedent filings.

## 3. Insider Activity Analysis — HEAVY NET SELLING, ZERO BUYING (12 months)

Form 4 detail shows a **uniformly one-sided tape: no open-market purchases by any officer or director, and continuous sales**, mostly under pre-arranged 10b5-1 plans:

| Insider | Activity (2026) |
|---|---|
| **Eric Yuan (CEO/Chair)** | ~24,200 sh sold nearly monthly at $91–$109: Jun 2 $109.05 ($2.64M); Jul 13 57,824 sh @ $91.47 (**$5.29M**); Aug 5 $100.18 ($2.42M); Sep 1 $95.58 ($2.31M); Oct 5 $93.91 ($2.27M); Nov 3 $92.20 ($2.23M). Plus Class B→A conversions. Still holds **~41.3M shares (~$3.4B)** |
| **Michelle Chang (CFO)** | Jul 10 8,489 @ $90.80 ($771k); Oct 12 8,489 @ $99.46 ($844k); Oct 21 10,156 @ $101.93 (**$1.04M**) |
| **Velchamy Sankarlingam (Pres. Eng/Product)** | Jul 15 7,644 @ $91.98 ($703k); Sep 10 2,590 @ $95.81 ($248k); Oct 12 7,645 @ $99.26 ($759k) |
| **Santiago Subotovsky (Director)** | Sold **every 1–2 weeks** in 2,637-share lots (~$237k–$255k each), plus 7,911 @ $101.33 (Aug 4) and 4,549 @ $99.94 (Oct 15) — cumulative **>$2.5M** |
| **H.R. McMaster (Director)** | 3,000 @ $94.71 (Oct 8); 1,500 @ $101.25 (Oct 21) — leaves only **6,979 shares**, effectively exiting the position |

**Interpretation:** The pattern is consistent with scheduled diversification by a founder whose wealth is overwhelmingly one stock, and Yuan's remaining ~$3.4B stake is genuine alignment — this is *not* a distress signal. However, three flags: (i) **zero insider buys** even with the stock at $83 and 27% off its high; (ii) an **Oct cluster of sales at $94–$102** immediately preceding the Nov 19 drawdown and Nov 23 print; (iii) **directors selling down to de minimis** (McMaster) removes independent-shareholder skin in the game.

## 4. Top Operational Risks

- **Securitization of product-embedded cyber risk.** Repeated 2026 critical client-side flaws: **CVE-2026-22844** (Jan 2026) and **CVE-2026-53412/53413/53415** — zero-click RCEs in Zoom Workplace for Windows / VDI / Meeting SDK, CVSS up to **9.0**. For a company whose brand was rebuilt on the promise "we fixed security," recurring memory-corruption RCEs imply security-engineering debt and patch-latency exposure across a large installed base.
- **Key-person dependence on a founder-CEO with a thin bench.** 7,438 FTEs; strategy (AI pivot, FY30 6–8% growth / 40% margin targets) is personally identified with Yuan, who is also chair. NEO bench is four deep (CFO Chang, COO Bawa, President Sankarlingam) and has seen CFO turnover. Prior restructurings (1,300 cuts = 15% in 2023; ~150 in 2024) mean the AI pivot is being executed on flat headcount — execution risk.
- **Structural competitive compression and third-party AI dependency.** Microsoft Teams bundled in M365 remains the core margin threat (revenue growth only 4.9%, enterprise 7.8%). Simultaneously, Zoom's "federated AI" architecture outsources model capability to third parties (Anthropic among them) — creating supplier dependency, terms-of-service risk, and commoditization of the meeting layer. Cloud/infrastructure concentration adds continuity risk.

## 5. Reputational Risk Assessment — MODERATE

- **A long tail of trust events:** Zoombombing/encryption misrepresentation (2020), China call-routing, $85M privacy class settlement, $150M securities settlement (final 2025), and the 2023 AI-training ToS backlash. The pattern — *privacy promises getting ahead of actual practice* — is the reputational through-line and now recurs around AI.
- **Narrative risk has shifted from scandal to irrelevance-plus-proxy.** Recent coverage frames ZM as an "Anthropic IPO sympathy play" rather than a communications company. Its **~$3.13B Anthropic stake** (up from $1.27B on the books at 4/30/26, with a **$1.61B unrealized Q2 gain**) is now material to reported earnings and sentiment. If the Anthropic IPO prices or trades poorly, ZM can de-rate for reasons unrelated to its operations — and conversely, part of the current "value" case rests on a mark-to-market asset the company does not control. This also raises an **accounting-quality/disclosure question** (GAAP vs non-GAAP divergence, fair-value hierarchy for a private stake), not a fraud finding.
- **Mitigants:** Zoomtopia 2026 AI-governance tooling (centralized AI management, guardrails, deepfake-risk controls), a responsible-AI whitepaper, buybacks, and constructive insider-selling headlines ("Zoom drops 6% as investors digest insider selling") that have so far been absorbed without structural brand damage. Consumer-trust damage is real but enterprise trust — where the revenue is — appears intact.

## 6. Overall Non-Financial Risk Rating: **MODERATE**

Not Low, because of concentrated founder control, a live 20-year FTC order sitting directly in the path of the company's AI strategy, a persistent zero-buy insider tape, and recurring critical client vulnerabilities. Not High, because there is no active SEC/DOJ action, no active securities class action, no fraud indicators, no whistleblower or auditor issues, audit ratification at 99.7%, and a founder still ~$3.4B long the stock. **No fraud indicators identified.**

## 7. Red Flags Requiring Escalation

1. **McMaster's 22.7% withheld vote (77% support)** — significant director-level dissent; identify the cause (compensation committee? independence? attendance?) before the 2027 meeting.
2. **Twelve months of insider sales with zero purchases**, including an October cluster at $94–$102 just before a 10% drawdown, and directors (McMaster, Subotovsky) reducing toward de minimis. Confirm 10b5-1 adoption dates and any plan modifications — off-cycle adoption or acceleration would upgrade this to a genuine concern.
3. **Anthropic stake now a primary earnings and valuation driver** ($3.13B vs. $24.3B market cap; $1.61B unrealized gain) — request the valuation methodology, Level 3 assumptions, and lockup/registration-rights terms. Customary-index exclusion and earnings-quality optics are underappreciated.
4. **FTC consent order (to 2040) + CAIDP's AI-training complaint** — a repeat-violation theory already on file. Any overstated AI/privacy claim is a decree violation, not just a marketing problem.
5. **Zero-click RCE cluster in 2026 (CVE-2026-53412/413/415, CVSS ≤9.0)** — verify patch SLAs, incident-disclosure posture, and whether any exploitation occurred; a material breach would re-open the 2020 reputational playbook.
6. **Dual-class control (~32–38% voting power on ~7% economics) with combined Chair/CEO** — no mechanism for shareholders to force change; weight governance risk accordingly in any position-sizing decision.

---
**Data gaps (honest):** 10-K risk-factor text, 10-Q, and DEF 14A could not be retrieved (tool returned no filings for ZM; SEC/IR URLs returned HTTP 403), and the regulatory-news feed returned only analyst/13F noise. Governance and compensation facts are sourced from proxy summaries and an 8-K vote tally and should be re-verified against the primary DEF 14A before publication. The precise Yuan voting-power figure (32% vs. 37.7%) is unresolved across sources.
