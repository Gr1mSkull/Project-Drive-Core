# DevKit Electrical Architecture Open Issues — WP-010

**Document ID:** DOC-DK-OI-001  
**Version:** 1.6  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-010 / WP-010-R1 (Accepted)  
**Date:** 2026-07-20

## 1. Open issue register

| ID | Issue | Why unresolved | Blocking source | Decision type | Owner | Required evidence | Blocks next stage |
|----|-------|----------------|-----------------|---------------|-------|-------------------|-------------------|
| **OI-VIN-001** | Exact input voltage range | TBD-DK-001 Open | WP-009; register | THRESHOLD_OPEN | System Architect | PSU characterization; UV tests | Electrical sizing WP |
| **OI-UV-002** | UV hysteresis / brief-dip resume policy | No Accepted UV reaction table | TBD-DK-012 | THRESHOLD_OPEN | System Architect | Accepted UV reaction table | DK-C UV cases |
| **OI-CUR-001** | Exact base continuous current envelope | TBD-DK-002 Open | ADR-021; WP-009 | SIZING_OPEN | System Architect | Limit stack calculation + measurement | Sizing WP |
| **OI-CUR-002** | Simultaneous-load profiles and values | TBD-DK-003 Open | WP-009 profile model | THRESHOLD_OPEN | System Architect | Overlap profile approval + P4 test | Multi-load DK-C |
| **OI-CUR-003** | Conductor/connector/fuse sizing | No qualification | ADR-021 | SIZING_OPEN | Implementation Engineer | Component qual + thermal | Schematic WP |
| **OI-CHAN-001** | Physical channel population vs capability aliases | Aliases do not fix count | WP-010-R1 | ARCHITECTURE_OPEN | System Architect | Sizing + schematic WP mapping | Schematic WP |
| **OI-PCB-001** | PCB current and thermal capacity | No layout | WP-009 L6/L13 | SIZING_OPEN | Implementation Engineer | Copper/thermal model | Schematic WP |
| **OI-COMP-001** | High-side component class | No qualification | ADR-019; CR-001 | COMPONENT_OPEN | Component Engineer | Qualification report | Schematic WP |
| **OI-COMP-002** | Bidirectional component class | No qualification | ADR-019 | COMPONENT_OPEN | Component Engineer | Qualification report | Schematic WP |
| **OI-PROT-001** | Input reverse-polarity method | Architecture not decided | docs/002 preview only | ARCHITECTURE_OPEN | System Architect | Architecture decision | Component WP |
| **OI-PROT-002** | Transient-protection method | Not selected | — | COMPONENT_OPEN | Component Engineer | Qualification | Schematic WP |
| **OI-RAIL-001** | Rail voltages and current budgets | All rails symbolic | TBD-DK-017 | SIZING_OPEN | Implementation Engineer | Load analysis | Sizing WP |
| **OI-GND-001** | Ground/reference between base and external envelope | Safety-critical unknown; WP-014 retains Open (no isolation claim) | ADR-020/021; WP-014 FESB | ARCHITECTURE_OPEN | System Architect | Architect decision + fixture design | EXT interconnection |
| **OI-KILL-001** | KILL input conditioning detail | No hardware design | ADR-022 | IMPLEMENTATION_OPEN | Implementation Engineer | Timing measurement | Schematic WP |
| **OI-WD-001** | Watchdog implementation period | TBD-DK-005 Open | ADR-022 | THRESHOLD_OPEN | FW Architect | FW design + measurement | FW BSP WP |
| **OI-EDL-011** | EDL-011 clarification for control-loss | Semantic ambiguity | EDL-011 | EDL_CLARIFICATION | System Architect | EDL CR acceptance | TBD-DK-007 numeric |
| **OI-UV-001** | Undervoltage thresholds | TBD-DK-001/012 Open | Register | THRESHOLD_OPEN | System Architect | UV testing | Sizing WP |
| **OI-THM-001** | Temperature limits and observation | ADR-DK-011 Open | ADR-DK-011 request | ARCHITECTURE_OPEN | System Architect | ADR-DK-011 decision | Thermal WP |
| **OI-DECAY-001** | Load-decay models | Unknown loads | WP-009 | SIZING_OPEN | Test Engineer | Load characterization | Timing verification |
| **OI-CONN-001** | Connector/enclosure decision | ADR-DK-012 Open | ADR-DK-012 request | ARCHITECTURE_OPEN | System Architect | ADR-DK-012 acceptance | Schematic WP |
| **OI-ENV-001** | Thermal/environment split | ADR-DK-011 Open | ADR-DK-011 | ARCHITECTURE_OPEN | System Architect | ADR-DK-011 | Qualification scope |
| **OI-FIX-001** | External fixture interface (EXT-SOURCE / EXT-LOAD-BANK / EXT-POWER-MODULE) | Requirements Proposed (WP-014); design not started | ADR-020; WP-014 | FIXTURE_OPEN | Test Engineer | Fixture prelim design after WP-014 Accepted | HC discovery |
| **OI-FIX-002** | Stall-test fixture boundary | TBD-DK-022 Open; WP-014 maps requirement | ADR-023; WP-014 | FIXTURE_OPEN | Test Engineer | Fixture prelim design | VER-DCC-DK-C-011 |
| **OI-SC-001** | Short-circuit injection method | TBD-DK-011 Open; WP-014 fault catalog maps capability | ADR-023; WP-014 | FIXTURE_OPEN | Test Engineer | Safe injection design | DK-C SC cases |
| **OI-EPOCH-001** | Command epoch normative definition | Procedural only | TBD-DK-021 | IMPLEMENTATION_OPEN | FW Architect | FW specification | Post-kill verification |
| **OI-CONFIG-001** | Configuration-retention policy (if any) | No Accepted policy | REQ-DCC-V-DK config rules | ARCHITECTURE_OPEN | System Architect | Config governance CR | Config invalid cases |
| **OI-BI-001** | BI shoot-through prevention topology | Functional only | ADR-019 | COMPONENT_OPEN | Component Engineer | Switch topology selection | Schematic WP |
| **OI-SENSE-001** | Current sense accuracy and observation topology | TBD-DK-009 Open | REQ-DCC-V-DK-043 | THRESHOLD_OPEN | Component Engineer | Calibration evidence; topology selection | DK-C-004 |

### OI-GND-001 — permitted future options (not selected in WP-010)

```text
galvanically isolated
controlled common reference
single-point reference connection
fixture-defined differential interface
```

Base and external envelopes are functionally separated and protected against back-feed. Ground/reference relationship remains **Open**.

## 2. Classification legend

| Class | Meaning |
|-------|---------|
| ARCHITECTURE_OPEN | Requires architecture decision |
| SIZING_OPEN | Requires calculation and sizing WP |
| COMPONENT_OPEN | Requires qualification and selection |
| THRESHOLD_OPEN | Numeric threshold still Open |
| FIXTURE_OPEN | Requires fixture WP |
| EDL_CLARIFICATION | Blocked on EDL change/clarification |
| IMPLEMENTATION_OPEN | Requires schematic/FW implementation |

## 3. Downstream WP mapping

| Next WP | Open issues consumed |
|---------|---------------------|
| Architecture acceptance (WP-010) | All — disposition by Architect |
| EDL-011 clarification CR | OI-EDL-011 |
| Preliminary component-class qualification | OI-COMP-001, OI-COMP-002, OI-BI-001, OI-SENSE-001 — WP-012 evaluation readiness |
| Electrical sizing framework (WP-012) | OI-CUR-001…003, OI-PCB-001, OI-RAIL-001, OI-UV-001 |
| Component-class comparison (WP-013) | OI-COMP-001, OI-COMP-002, OI-BI-001, OI-SENSE-001, OI-PROT-001/002 — recommendations **Proposed** |
| Fixture/load-bank requirements (WP-014 Proposed) | OI-GND-001, OI-FIX-001, OI-FIX-002, OI-SC-001 — statuses remain Open |
| Fixture preliminary design (WP-015 Proposed) | OI-GND-001 (GND-OPTION-A…D compared, not selected); OI-PROT-001/002; OI-SC-001; OI-FIX-002; OI-BI-001; OI-SENSE-001 — all statuses remain Open; WP-015 maps options only |
| OI-GND-001 / OI-PROT / E-stop decision packages (after WP-015) | OI-GND-001, OI-PROT-001/002, REQ-DCC-V-FX-071 E-stop topology |
| Schematic WP | OI-PROT-001/002, OI-KILL-001, OI-CONN-001, OI-CHAN-001 |
| PCB constraints/layout WP | OI-PCB-001 |
| FW BSP planning | OI-WD-001, OI-EPOCH-001, OI-CONFIG-001 |

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial open issue register — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — OI-UV-002, OI-CHAN-001, OI-CONFIG-001; GND-001 options; external energy roles |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #14 merged (`c98ce56`) |
| 1.3 | 2026-07-20 | WP-012 — downstream mapping for sizing framework |
| 1.4 | 2026-07-20 | WP-013 — downstream mapping for class comparison (OI statuses unchanged) |
| 1.5 | 2026-07-20 | WP-014 — fixture OI consumers updated; all listed OI remain Open |
| 1.6 | 2026-07-20 | WP-015 — preliminary-design downstream mapping (options compared, not selected); OI statuses unchanged |
