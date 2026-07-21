# DevKit Fixture Detailed-Design Input Register — WP-016

**Document ID:** DOC-DK-FDDIR-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Controlled detailed-design input baseline. No numeric input is Approved by WP-016.
Value-type separation: architecture (non-numeric) vs numeric vs qualification vs derived.
Entries are dependency references, not approved design inputs, until the named authority accepts them.
```

## 1. Value-type legend

```text
ACCEPTED_ARCH   — Accepted non-numeric architecture input (from Accepted WP)
PROPOSED_ARCH   — Proposed architecture input (WP-016; pending Architect)
OPEN_NUMERIC    — Open numeric input (threshold/rating; not Approved)
COMPONENT_QUAL  — Component-qualification input (future qualification WP)
DD_DERIVED      — Detailed-design-derived input (produced later)
MEAS_DERIVED    — Measurement-derived input (produced by test)
```

## 2. Register

| ID | Input | Source | Authority | Value type | Current status | Consumer | Blocker | Owner | Closure artifact |
|----|-------|--------|-----------|------------|----------------|----------|--------|-------|------------------|
| FX-DD-IN-001 | Selected ground/reference architecture | WP-016 GRDP | System Architect | PROPOSED_ARCH | DEFER/SPLIT recommended | External/measurement design | OI-GND-001 | System Architect | OI-GND-001 disposition |
| FX-DD-IN-002 | Permitted energy directions | WP-015/WP-016 | Accepted + Architect | ACCEPTED_ARCH | Defined (mutually-exclusive basis) | Energy-path design | — | System Architect | Energy-path detailed design |
| FX-DD-IN-003 | Base/external exclusivity | WP-015 FX-PD-003 | Accepted | ACCEPTED_ARCH | Accepted (while OI-GND-001 Open) | Interlock design | — | System Architect | Interlock detailed design |
| FX-DD-IN-004 | Back-feed-prevention allocation | WP-016 GRDP; FX-PD-005 | Architect | PROPOSED_ARCH | External-boundary; realization Open | Protection design | OI-GND-001; OI-PROT-001 | System Architect | Protection package |
| FX-DD-IN-005 | E-stop functional architecture | WP-016 EADP | Architect | PROPOSED_ARCH | OPT-2/OPT-3 class; DEFER final | E-stop design | Proof-test inputs | System Architect | E-stop package |
| FX-DD-IN-006 | E-stop integrity observation | REQ-DCC-V-FX-071; WP-016 | Architect | PROPOSED_ARCH | Required; topology Open | Safety design | Topology + proof | System Architect | E-stop package |
| FX-DD-IN-007 | Energy-removal confirmation | WP-015/WP-016 | Architect | PROPOSED_ARCH | Independent observation required | State machine | Detailed design | System Architect | Energy-removal design |
| FX-DD-IN-008 | Discharge-complete observation | WP-015/WP-016 | Architect | PROPOSED_ARCH | Required before recovery | State machine | Timing Open | System Architect | Discharge design |
| FX-DD-IN-009 | Reverse-polarity protection class | WP-016 PADP; OI-PROT-001 | Architect | PROPOSED_ARCH | Class direction; final Open | Protection design | Numeric; component qual | Component Engineer | OI-PROT-001 disposition |
| FX-DD-IN-010 | Transient-protection class | WP-016 PADP; OI-PROT-002 | Architect | PROPOSED_ARCH | Hybrid layered; energy bound Open | Protection design | Waveform/energy bound | Component Engineer | OI-PROT-002 disposition |
| FX-DD-IN-011 | Source prospective-fault envelope | ED-IN-009; WP-012 | System Architect | OPEN_NUMERIC | Open (BLOCKED_BY_INPUT) | Protection coordination | Numeric | System Architect | Sizing + measurement |
| FX-DD-IN-012 | Measurement input/reference behavior | WP-016 MCSA; FX-PD-018 | Architect | PROPOSED_ARCH | Potential energy/fault path model | Measurement design | OI-GND-001; OI-SENSE-001 | Component Engineer | Measurement package |
| FX-DD-IN-013 | Returned-energy policy | WP-016 RECA; FX-PD-009 | Architect | PROPOSED_ARCH | Gen1 policy D (prohibit regen) | Load-bank design | OI-BI-001 | System Architect | OI-BI-001 disposition |
| FX-DD-IN-014 | Containment requirements | WP-015 FX-PD-017 | Architect | PROPOSED_ARCH | Functional only; realization Open | Enclosure design | ADR-DK-011/012 | System Architect | ADR-DK-011/012 |
| FX-DD-IN-015 | Identity/configuration inputs | WP-014/WP-015 | Architect | PROPOSED_ARCH | Required; retention policy Open | Identity design | OI-CONFIG-001 | System Architect | Config governance |
| FX-DD-IN-016 | Connector/conductor inputs | ADR-DK-012; ED-IN-028 | System Architect | OPEN_NUMERIC / COMPONENT_QUAL | Open | Wiring/harness design | ADR-DK-012; ratings | System Architect | Connector policy WP |
| FX-DD-IN-017 | Environmental inputs (thermal) | ADR-DK-011; ED-IN-016/017 | System Architect | OPEN_NUMERIC | Open | Thermal design | ADR-DK-011 | System Architect | Thermal WP |
| FX-DD-IN-018 | Calibration inputs | WP-016 MCSA; ED-IN-011/012 | Component Engineer | OPEN_NUMERIC / MEAS_DERIVED | Open | Measurement design | Accuracy Open | Component Engineer | Qualification WP |
| FX-DD-IN-019 | Verification-boundary inputs | WP-014 verification capability | System Architect | PROPOSED_ARCH | Defined boundaries; cases BLOCKED | Verification planning | Numeric; fixture build | Test Engineer | Verification WP |
| FX-DD-IN-020 | Source continuous/fault current envelope | ED-IN-002/008/009 | System Architect | OPEN_NUMERIC | Open (BLOCKED_BY_THRESHOLD) | Sizing; protection | TBD-DK-002 | System Architect | Sizing + measurement |

No numeric input becomes Approved through WP-016. ED-IN entries referenced here remain dependency references (WP-011 R6).

## 3. Value-type summary

| Value type | Entries |
|-----------|---------|
| ACCEPTED_ARCH | FX-DD-IN-002, 003 |
| PROPOSED_ARCH | FX-DD-IN-001, 004, 005, 006, 007, 008, 009, 010, 012, 013, 014, 015, 019 |
| OPEN_NUMERIC | FX-DD-IN-011, 016, 017, 018, 020 |
| COMPONENT_QUAL | FX-DD-IN-009/010/016 (qualification portions) |
| DD_DERIVED / MEAS_DERIVED | Produced later (FX-DD-IN-018 meas; detailed-design outputs) |

## 4. Traceability

FX-PD-003/005/006/009/017/018 · OI-GND-001 · OI-PROT-001/002 · OI-BI-001 · OI-SENSE-001 · OI-CONFIG-001 · ADR-DK-011/012 · ED-IN-002/008/009/011/012/016/017/028 · REQ-DCC-V-FX-071.

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial detailed-design input register (FX-DD-IN-001…020) — Proposed |
