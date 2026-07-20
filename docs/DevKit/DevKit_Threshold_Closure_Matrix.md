# DevKit Threshold Closure Matrix — WP-009

**Document ID:** DOC-DK-TBD-MAT-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-009  
**Date:** 2026-07-20

> Authoritative closure disposition for analyzed thresholds. **Status in register remains Open** until System Architect acceptance.

## 1. Disposition legend

| Disposition | Meaning |
|-------------|---------|
| READY_FOR_ACCEPTANCE | Evidence/model sufficient for Architect to accept value or procedure |
| READY_FOR_CONDITIONAL_ACCEPTANCE | Partial bound or method acceptable; numeric/full closure pending |
| BOUND_ESTABLISHED_VALUE_OPEN | Calculation model and bounds defined; numeric Open |
| BLOCKED_BY_ELECTRICAL_ARCHITECTURE | Needs electrical design inputs |
| BLOCKED_BY_COMPONENT_SELECTION | Needs qualified components |
| BLOCKED_BY_MEASUREMENT | Needs physical bench evidence |
| BLOCKED_BY_HAZARD_DECISION | Needs hazard/risk decision beyond WP-009 |

## 2. Primary thresholds (WP-009 scope)

| TBD | Proposed disposition | Candidate value/range | Bound | Evidence available | Missing evidence | Architecture dependency | Component dependency | Fixture dependency | Measurement dependency | Gate blocked | Next artifact |
|-----|---------------------|----------------------|-------|-------------------|------------------|------------------------|---------------------|-------------------|------------------------|--------------|---------------|
| TBD-DK-002 | BOUND_ESTABLISHED_VALUE_OPEN | Study band 8–15 A continuous (C2); tuple 002A/B/C recommended | `I_certified_cont ≤ min(stack)` | ADR-021 Accepted; calculation model | PCB/connector/conductor; protection study; measurement | ADR-019/021 | Fuse, connector, switch | P3 loads | Input + channel current traces | DK-A sizing claims | Architect threshold decision; electrical architecture WP |
| TBD-DK-003 | BOUND_ESTABLISHED_VALUE_OPEN | Profile P4 sum ≤ `I_certified_cont`; no numeric A | Inequality + duty-factor policy | ADR-021 simultaneous policy | Multi-channel thermal; P4 measurement | ADR-019/021 | Per-channel limits | Multi-load fixture | Simultaneous capture | DK-C multi-load | Architect acceptance; P4 measurement |
| TBD-DK-004 | BLOCKED_BY_MEASUREMENT | Study 1–50 ms total | Kill fastest class | ADR-022 path model | HW path; load model; scope traces | ADR-016/022 kill path | Kill switch, smart switch | Kill inject | Oscilloscope timing | DK-A A-012 | PCB + measurement VE (future) |
| TBD-DK-005 | BLOCKED_BY_COMPONENT_SELECTION | Study 50–500 ms (expiry-dominated) | Watchdog > kill (target) | ADR-022 class model | WD period; FW handler budget | ADR-022 | MCU WD config | Fault inject | Timing measurement | DK-A A-011 | FW + component freeze |
| TBD-DK-007 | READY_FOR_CONDITIONAL_ACCEPTANCE | Lower **>100 ms**; upper Open | EDL-011 minimum | EDL-011 Accepted; budget §3.3 | DCPI period; missed frames; HW fail-safe measure | EDL-011; ADR-022 | SPI/timeout HW | Comm loss stim | SPI timeout capture | DK-A A-008; DK-C C-012 | EDL clarification CR; measurement |
| TBD-DK-014 | BOUND_ESTABLISHED_VALUE_OPEN | Study 1–100 ms channel | ≤ control loss (target) | Command path model | FW schedule; switch disable | ADR-022 | Switch driver | Channel load | OFF timing | DK-A A-014; DK-C | FW + measurement |
| TBD-DK-021 | READY_FOR_ACCEPTANCE | State machine (§7 Safety Timing doc) | Procedural | ADR-022 recovery rules | FW implementation | ADR-022 | Kill/enable chain | Kill release test | Sequence log | DK-A A-014 | Architect procedure acceptance |

## 3. Related thresholds (inspected)

| TBD | Proposed disposition | Candidate value/range | Bound | Evidence available | Missing evidence | Architecture dependency | Component dependency | Fixture dependency | Measurement dependency | Gate blocked | Next artifact |
|-----|---------------------|----------------------|-------|-------------------|------------------|------------------------|---------------------|-------------------|------------------------|--------------|---------------|
| TBD-DK-001 | BLOCKED_BY_ELECTRICAL_ARCHITECTURE | 13.8 V nominal **CANDIDATE** | Automotive bench range | docs/008 candidate | UV coordination with 012 | ADR-021 entry | PSU class | N/A | DMM at entry | DK-A A-003 | Architect range decision |
| TBD-DK-012 | BLOCKED_BY_HAZARD_DECISION | 10.5 V **CANDIDATE** (docs/008) | Reaction table required | REQ UV behaviour | Full reaction table | ADR-019/021 | Sense path | UV stim | UV step test | DK-C UV cases | Hazard + table WP |
| TBD-DK-017 | BLOCKED_BY_ELECTRICAL_ARCHITECTURE | ±5 % **CANDIDATE** | Per-rail table | REQ rails measurable | Regulator spec | Logic/Power arch | LDO/DC-DC | N/A | Rail capture | DK-A | Electrical architecture |
| TBD-DK-018 | BLOCKED_BY_MEASUREMENT | Not defined | Thermal case duration | REQ thermal cases | Channel class + load | ADR-019 thermal | NTC/switch | Thermal load | Duration log | DK-C C-009 | Thermal analysis |
| TBD-DK-019 | BLOCKED_BY_HAZARD_DECISION | Surface max **CANDIDATE** | Operator safety | REQ thermal | Touch hazard policy | ADR-DK-011 seq | Thermal paths | Enclosure | IR/TC | DK-C | Hazard decision |
| TBD-DK-022 | BLOCKED_BY_COMPONENT_SELECTION | Stall A/ms **CANDIDATE** | P5 fault class | REQ-042/054/055 | H-bridge + fixture | ADR-019 bidirectional | H-bridge MPN | Stall fixture | Stall capture | DK-C C-010–013 | Component + fixture WP |

## 4. Closure stage separation

For each primary TBD:

| Stage | TBD-DK-002 | TBD-DK-003 | TBD-DK-004 | TBD-DK-005 | TBD-DK-007 | TBD-DK-014 | TBD-DK-021 |
|-------|------------|------------|------------|------------|------------|------------|------------|
| Architecture direction established | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Calculation model established | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (procedure) |
| Candidate value proposed | Band only | Policy only | Band only | Band only | Lower bound | Band only | Procedure |
| Numeric value acceptable now | ❌ | ❌ | ❌ | ❌ | Partial lower | ❌ | Procedure only |
| Numeric value requires hardware | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FW impl |
| Procedure acceptable now | ❌ | ✅ (profile) | ❌ | ❌ | ❌ | ❌ | ✅ (proposed) |
| Evidence remains NOT VERIFIED | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## 5. Thresholds ready for Architect review

### Ready for acceptance (procedure)

- **TBD-DK-021** — post-kill re-enable state machine

### Ready for conditional acceptance

- **TBD-DK-007** — lower bound >100 ms + closure method only

### Bounds established; numeric Open

- **TBD-DK-002**, **TBD-DK-003**, **TBD-DK-014**

### Blocked pending measurement / components

- **TBD-DK-004**, **TBD-DK-005**

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial closure matrix |
