# DevKit Power-Path Assumption Register — WP-012

**Document ID:** DOC-DK-PPAR-001  
**Version:** 1.9  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20

Assumptions and constraints for power-path sizing. **Not** approved design inputs (ED-IN R6 alignment).

## 1. Status legend

| Status | Meaning |
|--------|---------|
| **ACCEPTED_CONSTRAINT** | Architecturally Accepted boundary — not a numeric value; exact Accepted source cited |
| **PROPOSED_CONSTRAINT** | First introduced by a WP — **Proposed** until Architecture Review acceptance; Implementation Engineer shall not self-approve |
| **OPEN_ASSUMPTION** | Documented assumption; closure required |
| **BLOCKED** | Cannot proceed without listed artifact |
| **REJECTED** | Shall not be used as normative basis |
| **HISTORICAL_ONLY** | Context only — non-normative |

## 2. Assumption register

| ID | Assumption or constraint | Source | Authority | Status | Rationale | Risk if false | Owner | Closure artifact |
|----|--------------------------|--------|-----------|--------|-----------|---------------|-------|------------------|
| **PWR-A-001** | Base and external energy envelopes are distinct | ADR-020/021; WP-010 | Accepted ADR | ACCEPTED_CONSTRAINT | Prevents HC scope creep into base cert | Base rating inflated by fixture | System Architect | WP-010 FEA; P6 profile |
| **PWR-A-002** | External ratings do not increase `I_certified_cont` | ADR-020; WP-009 L12 | Accepted ADR | ACCEPTED_CONSTRAINT | Load-bank limit separate from P3 | Silent base envelope expansion | System Architect | Closure matrix |
| **PWR-A-003** | Back-feed into base distribution is prohibited | WP-010; OI-GND-001 | Accepted architecture | ACCEPTED_CONSTRAINT | Safety / damage prevention | Uncontrolled energization | System Architect | Accepted fixture interconnection decision + back-feed-prevention evidence + ground/reference disposition under OI-GND-001 |
| **PWR-A-004** | Physical KILL has direct hardware-effective disable path | ADR-022; WP-010-R1 | Accepted ADR | ACCEPTED_CONSTRAINT | Kill not Logic-only | Kill latency / failure | Implementation Engineer | Schematic + timing meas |
| **PWR-A-005** | `nENABLE_GLOBAL` defaults inactive (outputs OFF) | EDL-011 semantics; WP-011 Option D | Accepted interpretation | ACCEPTED_CONSTRAINT | Fail-safe default | Outputs ON at power-up | Implementation Engineer | Power-controller qual |
| **PWR-A-006** | Radio has no direct output-enable authority | WP-010 §3.2; safety standard | Accepted architecture | ACCEPTED_CONSTRAINT | ESP32/Radio non-safety | Unauthorized enable | System Architect | Interface matrix |
| **PWR-A-007** | Numeric base current envelope is Open | TBD-DK-002; register | Accepted WP-009 | OPEN_ASSUMPTION | No ampere ceiling Approved | Premature component selection | System Architect | Sizing + measurement WP |
| **PWR-A-008** | Physical channel population is Open | OI-CHAN-001; WP-010-R1 | Accepted architecture | OPEN_ASSUMPTION | Aliases ≠ channel count | Verification gap | System Architect | Schematic mapping WP |
| **PWR-A-009** | Ground/reference relation to external envelope is Open | OI-GND-001 | Architecture Open | OPEN_ASSUMPTION | Fixture safety depends on GND | Hazardous measurement | System Architect | ADR/fixture decision |
| **PWR-A-010** | Open-load capability is conditional on implementation claim | ADR-023; WP-008-R1 | Accepted ADR | ACCEPTED_CONSTRAINT | Not all channels require OL detect | False verification scope | Component Engineer | Qualification report |
| **PWR-A-011** | Control-loss timing numeric value is Open | TBD-DK-007; WP-011 | Register BLOCKED | BLOCKED | Semantics Accepted; numeric not | Wrong timeout in FW/HW | System Architect | Measurement + optional EDL CR |
| **PWR-A-012** | Thermal/environment split remains Open | ADR-DK-011 request | Architecture Open | OPEN_ASSUMPTION | Qualification scope undefined | Wrong thermal test conditions | System Architect | ADR-DK-011 |
| **PWR-A-013** | Connector/enclosure decision remains Open | ADR-DK-012 request | Architecture Open | OPEN_ASSUMPTION | Entry/distribution unknown | Wrong conductor/thermal path | System Architect | ADR-DK-012 |
| **PWR-A-014** | Historical 30 A references are non-normative | docs/008; devkit.yaml | WP-009 disposition | HISTORICAL_ONLY | Candidate only | Silent numeric freeze | Implementation Engineer | Threshold acceptance |
| **PWR-A-015** | Unknown channel overlap treated as concurrent | WP-009-R1; budget model | Accepted method | ACCEPTED_CONSTRAINT | Conservative sizing | Undersized input path | Test Engineer | P4 overlap profiles |
| **PWR-A-016** | Fuse nominal ≠ continuous certification | ADR-021; WP-009 L4 | Accepted ADR | ACCEPTED_CONSTRAINT | Protection vs continuous distinct | Using fuse as continuous rating | Implementation Engineer | Protection study |
| **PWR-A-017** | PSU current limiting is not the sole protection layer | WP-012 protection framework §3 princ. 1 | WP-012 protection framework + explicit WP-014 Architecture Review disposition | **ACCEPTED_CONSTRAINT** | Layer coordination | Single-point reliance | System Architect | WP-014 Architecture Review (non-numeric; no topology/fuse/current/time approved) |
| **PWR-A-018** | Software-commanded OFF is not hardware fault containment | WP-012 protection framework §3 princ. 7 | WP-012 protection framework + explicit WP-014 Architecture Review disposition | **ACCEPTED_CONSTRAINT** | Software OFF ≠ hardware protection | SC sustained by SW only | System Architect | WP-014 Architecture Review (non-numeric; no topology/component approved) |
| **PWR-A-019** | ED-IN entries are dependency references only | WP-011 R6 | Accepted WP-011 | ACCEPTED_CONSTRAINT | No silent input freeze | Treating register as Approved BOM input | System Architect | ED-IN register |
| **PWR-A-020** | Evaluation classes are not procurement shortlist | WP-011 | Accepted WP-011 | ACCEPTED_CONSTRAINT | Qualification discipline | Premature MPN order | Component Engineer | Qualification WP |
| **PWR-A-021** | Fixture E-stop is independent of DUT physical KILL and `nENABLE_GLOBAL` | WP-014 FESB | WP-014 + Architecture Review disposition | **ACCEPTED_CONSTRAINT** | Distinct safety authorities | Merged authorities hide failures | System Architect | WP-014 Architecture Review (2026-07-20) |
| **PWR-A-022** | Hazardous fixture AUTH_* default inactive; stale after interruption/reset | WP-014 FFA | WP-014 + Architecture Review disposition | **ACCEPTED_CONSTRAINT** | No auto-resume | Unexpected energization | System Architect | WP-014 Architecture Review (2026-07-20) |
| **PWR-A-023** | EXT-LOAD-BANK is an energy sink, not a source | WP-014 FESB; ADR-020 | WP-014 + Architecture Review disposition | **ACCEPTED_CONSTRAINT** | Prevent source/sink confusion | Back-feed / wrong evidence | System Architect | WP-014 Architecture Review (2026-07-20) |
| **PWR-A-024** | Radio/Tablet have no direct hazardous-energy authority on fixture | WP-014; safety standard | WP-014 + Architecture Review disposition | **ACCEPTED_CONSTRAINT** | Align ESP32 non-safety | UI-owned energy | System Architect | WP-014 Architecture Review (2026-07-20) |

## 3. Prohibited conversions

Assumptions in this register shall **not** be converted to requirements or numeric thresholds without Controlled Architect acceptance and traceability update.

**WP-012-R1 rule:** Constraints first introduced by a WP remain **PROPOSED_CONSTRAINT** until explicit Architecture Review acceptance. Implementation Engineer cannot self-approve.

**WP-013 note:** Class recommendations do not alter PWR-A statuses. PWR-A-020 (evaluation classes ≠ procurement shortlist) remains **ACCEPTED_CONSTRAINT**.

**WP-014 / WP-014-R1 note:** PWR-A-017 and PWR-A-018 are **ACCEPTED_CONSTRAINT** by explicit Architecture Review disposition (non-numeric; no component, topology, fuse, current, or clearing time approved; no verification claim). PWR-A-003 closure artifact no longer requires an unconditional isolation proof — isolation proof is a possible future artifact only if Architect selects galvanic isolation under OI-GND-001.

**WP-016 note (2026-07-21):** WP-016 decision proposals consume PWR-A-003/017/018 as `ACCEPTED_INPUT` and introduce no new PWR-A status. Back-feed prohibition (PWR-A-003), PSU-limit-not-sole-protection (PWR-A-017), and software-OFF-not-containment (PWR-A-018) are reaffirmed in the protection architecture proposal. No status change.

**WP-015 note (2026-07-20):** WP-015 preliminary design consumes PWR-A constraints as `ACCEPTED_INPUT`; it introduces no new PWR-A status and does not alter PWR-A-017/018/021…024 (all ACCEPTED_CONSTRAINT). New WP-015 constraints live in the WP-015 decision register as `PROPOSED_*`.

**WP-014 acceptance note (2026-07-20):** PWR-A-021…024 are now **ACCEPTED_CONSTRAINT** through WP-014 Architecture Acceptance (non-numeric safety-authority/sink/UI boundaries; no component, topology, or numeric value approved; no verification claim). OI-GND-001 and all listed OI-* remain Open; TBD-DK-007 remains BLOCKED_BY_EDL_CLARIFICATION.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial power-path assumption register — Proposed |
| 1.1 | 2026-07-20 | WP-012-R1 — PROPOSED_CONSTRAINT status; PWR-A-017/018 disposition |
| 1.3 | 2026-07-20 | Architecture Review Accepted — PR #16 merged (`9c5c7e7` / `fe700d4`) |
| 1.4 | 2026-07-20 | WP-013 — note that class recommendations do not change PWR-A statuses |
| 1.5 | 2026-07-20 | WP-014 — PWR-A-021…024 PROPOSED_CONSTRAINT (fixture authorities / sink / UI) |
| 1.6 | 2026-07-20 | WP-014-R1 — PWR-A-017/018 ACCEPTED_CONSTRAINT; PWR-A-003 closure artifact (no isolation proof mandate) |
| 1.7 | 2026-07-20 | WP-014 Architecture Acceptance — PWR-A-021…024 ACCEPTED_CONSTRAINT; Open decisions retained |
| 1.8 | 2026-07-20 | WP-015 — note: preliminary design consumes PWR-A as ACCEPTED_INPUT; no status change |
| 1.9 | 2026-07-21 | WP-016 — note: decision proposals consume PWR-A-003/017/018 as ACCEPTED_INPUT; no status change |
