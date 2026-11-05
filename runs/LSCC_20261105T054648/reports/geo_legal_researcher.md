# Geo Legal Researcher

- Symbol: LSCC
- Elapsed: 122.7s

---
# Lattice Semiconductor (LSCC) — Geopolitical & Legal Risk Assessment
*Research date: November 2026 | Latest filing: 10-Q filed 11/03/2026 (FQ3'26 ended Oct 3, 2026)*

---

## 1. Geographic Risk Map

**Revenue mix (ship-to geography):**

| Region | FY2025 | FQ1'26 | FQ2'26 | FQ3'26 | FQ3'25 | Risk Level |
|---|---|---|---|---|---|---|
| **Greater China** (mainland + HK) | **52%** ($273.2M) | **64%** | n/d | n/d | n/d | **Very High** |
| Asia ex-China (Taiwan, Japan, Malaysia, Korea, Other Asia) | ~24% | ~14% | n/d | n/d | n/d | High |
| **Asia total** | ~76% | **78%** | **79%** | **76%** | 65% | **High** |
| Americas | ~14% | 11% | 12% | **16%** | 19% | Low |
| Europe (incl. Africa) | ~10% | 11% | 9% | **8%** | 16% | Low–Medium |

*Foreign sales = 83% of FY2025 revenue (82% in FY2024 and FY2023).* Sources: FY2025 10-K (filed 02/13/2026); FQ3'26 earnings release supplemental table (11/02/2026); FQ1'26 release.

**Operational footprint & other exposures:**

| Country | Exposure | Risk Level |
|---|---|---|
| **China (mainland)** | ~50%+ of revenue; Shenzhen technical summit (700+ customers/partners); distributor-led channel | **Very High** |
| **Taiwan** | Primary foundry (TSMC-class) for all FPGA wafer supply; significant long-lived assets; Taipei summit; AMI Rack Manager launch | **High** |
| **Hong Kong** | Bundled into "Greater China"; 10-K explicitly warns HK-shipped product "may subsequently be resold" into mainland | **High** |
| **Malaysia, Philippines** | Assembly/test, long-lived assets | Medium |
| **India** | Long-lived assets; AMI's large India engineering base (inherited via acquisition) | Medium |
| **US** | HQ (Hillsboro, OR); 16% Americas revenue only | Low |
| **Israel/Europe** | Minimal revenue (8%), no manufacturing concentration identified | Low |

**Two structural facts that dominate the risk profile:**
1. **~Half of revenue is China-destination, and it is rising** — Greater China went from 52% (FY2025) to 64% (FQ1'26) on the AI/industrial recovery. This is among the highest China exposure in the US semiconductor universe.
2. **81–89% of revenue flows through distributors** (81% Q3'26, 95% Q2'26, 89% 9M'26). This is the single most important compliance fact: Lattice frequently does not know the ultimate end-user of chips shipped to Chinese/Hong Kong distributors.

---

## 2. Top 3 Geopolitical Risks

### Risk 1 — US–China export controls and Chinese retaliation against a >50%-China revenue base
**Probability: High (already materializing) | Impact: High**

The FY2025 10-K and FQ3'26 10-Q risk factors explicitly flag that "China has responded by implementing additional export controls on products exported from China" and that tariffs/trade actions could harm "revenues, gross margin." Chinese countermeasures have escalated materially through 2026 (MOFCOM dual-use/advanced-technology controls; CFR documents controls on gallium, rare earths and at least seven other materials between 2023–2026). Notably, the US–China truce on chip and critical-mineral controls is described as a *paused*, not resolved, arrangement — i.e., re-escalation is a live binary.

The acute channel of harm is not Lattice's own chips being "advanced" (small/mid-range FPGAs are generally below the advanced-node thresholds), but **derivative-product tariffs**: the 25% Section 232 duty effective 15 January 2026 applies to specified chips *and products containing them*, which reaches Lattice content embedded in China-assembled servers and industrial equipment. With 81–89% of sales via distribution, the company has limited line-of-sight to where its parts land, raising both tariff cost and diversion-liability risk.

*Why this is elevated for LSCC specifically:* In 2017, a China-backed acquirer (Canyon Bridge) agreed to buy Lattice for ~$1.3B, and the transaction was **blocked by presidential order on CFIUS/national-security grounds** — one of only a handful of such blocks in decades. Lattice is a formally designated sensitive-technology asset. Its 2026 pivot into AI data-center control planes and firmware (via AMI) increases, not decreases, that sensitivity.

### Risk 2 — Taiwan Strait / foundry single-point-of-failure
**Probability: Low–Medium | Impact: Severe**

Lattice is fabless and dependent on Taiwan-based foundry for wafer supply, with Taiwan also carrying significant long-lived assets and meaningful revenue. Taiwan is actively *tightening* advanced-chip export controls toward mainland China (reported November 2026), which compresses Lattice's supply-and-sell-through corridor between its foundry and its largest market. A blockade, quarantine, or escalated cross-strait action would simultaneously cut supply and destroy demand. No mitigation is disclosed beyond generic "dependence on third-party foundry, assembly and test providers."

### Risk 3 — AMI integration expands the regulated perimeter (firmware, critical infrastructure, India/China delivery)
**Probability: Medium | Impact: Medium–High**

The $1.59B AMI acquisition (closed 27 July 2026; $1.0B cash, ~$650M stock) moves Lattice into **BIOS/UEFI and BMC firmware** for servers — firmware is a far more regulated and security-scrutinized product category than FPGAs. This creates new exposure to: (a) government/agency scrutiny of firmware in critical infrastructure; (b) mandatory vulnerability-disclosure and product-security regimes (e.g., EU Cyber Resilience Act, US federal software supply-chain attestation); (c) open-source/SBOM diligence obligations, since AMI builds on open-source firmware; and (d) foreign-delivery exposure, given AMI's substantial India engineering footprint now inside a US defense-adjacent supplier. The release itself concedes "risks relating to the security of our products and firmware, including vulnerabilities arising from third-party or open-source components." AMI posted a **$14.4M net loss** on $39.1M of revenue post-close — the acquired business is unprofitable while carrying the regulated risk.

**Secondary risk — cross-border cash/liquidity:** Of $128.3M total cash, **$82.4M (64%) is held by foreign subsidiaries**, against $875M of term-loan principal. Debt service is USD-denominated while cash generation sits in Asia. This creates a repatriation/currency-control friction if China tightens capital flows.

---

## 3. Legal & Regulatory Highlights

- **No material pending litigation disclosed.** The most recent 10-Q (11/03/2026) and FY2025 10-K carry the standard "litigation and unfavorable results of legal proceedings" risk language but no identified active case with material quantified exposure. *(Caveat: the 10-Q "Legal Proceedings" note could not be retrieved in full — SEC Archives and ir.latticesemi.com static files returned 403; this is a verified gap, not a confirmed clean bill.)*
- **Historical export-control penalty.** Lattice was previously assessed approximately **$560,000** for deemed-export violations arising from sharing controlled chip design technology with foreign nationals — a documented compliance failure directly relevant to its current India/China engineering footprint and post-AMI integration of foreign engineering teams.
- **Regulatory posture:** Principal regimes are BIS/EAR (export licensing), OFAC (sanctions screening of distributors/end-users), Section 232 (semiconductor tariffs, 25% on a narrow advanced-chip category from 15 Jan 2026), and — newly via AMI — firmware/product-security regulation.
- **Antitrust/CFIUS:** The AMI deal was completed without a disclosed CFIUS mitigation agreement, but Lattice's status as a 2017 presidential-block target means any future strategic transaction (inbound or outbound involving Chinese parties) faces elevated CFIUS risk.
- **IP:** Lattice monetizes a patent portfolio and has historically asserted IP; it is both plaintiff and potential defendant in FPGA IP disputes. Elevated risk given Chinese FPGA competitors (domestic substitution policy actively funds local FPGA rivals).

---

## 4. Compliance Red Flags

| Flag | Severity | Detail |
|---|---|---|
| **Distributor-led China sales with no end-user visibility** | 🔴 High | 81–89% of revenue via distributors; 10-K concedes HK-shipped product may be resold into mainland. Structural diversion risk under EAR/Entity List. |
| **Prior deemed-export violation (~$560K)** | 🟠 Medium-High | Demonstrated enforcement history; recurring risk as foreign engineering headcount (India, Malaysia, Philippines) grows post-AMI. |
| **Firmware in critical infrastructure / AI data centers** | 🟠 Medium-High | New product-security liability, disclosure obligations, and national-security optics as AMI firmware runs in hyperscale AI racks. |
| **Offshore cash vs. USD debt** | 🟡 Medium | $82.4M of $128.3M cash held offshore against $875M term loan — repatriation/currency-control sensitivity. |
| **China revenue concentration** | 🔴 High | ~50–64% of revenue from a jurisdiction explicitly named in the company's own risk factors as a source of retaliatory controls. |

---

## 5. Overall Geopolitical/Legal Risk Rating: **HIGH**

**Rationale:** Lattice combines (i) the highest-tier China revenue concentration in the US semi cohort (~52% FY2025, 64% FQ1'26), (ii) a Taiwan-fab dependency, (iii) an opaque distributor channel that historically produced an export-control penalty, and (iv) a formally designated national-security-sensitive corporate identity (2017 presidential CFIUS block). Litigation risk itself is **Low**, and Europe/Americas exposure is immaterial. The rating is driven almost entirely by *export-control, tariff, and cross-strait* exposure rather than by courtroom or regulator-investigation risk.

**What would change the rating:**
- Up to **Very High** if: China-destination revenue exceeds ~65% again, a BIS enforcement action or Entity-List designation touches a Lattice distributor, or cross-strait military/blockade escalation.
- Down to **Medium** if: Americas/Europe revenue mix rises structurally above ~30% (the AMI deal helps here — Americas went 12%→16% in one quarter), and a formal export-compliance program disclosure (diversion screening, end-user certification) appears in the 10-K.

**Key monitoring triggers:** Section 232 derivative-product scope expansion; Chinese rare-earth/gallium licensing decisions; Taiwan export-control tightening implementation; AMI firmware CVE disclosures; any CFIUS filing involving Chinese counterparties.
