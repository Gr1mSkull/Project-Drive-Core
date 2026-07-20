# DevKit Fixture Interface and Measurement Register — WP-014

**Document ID:** DOC-DK-FIMR-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review (2026-07-20)  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Functional interfaces and measurement roles only — no connectors, pinouts, or instruments selected.
```

## 1. Sign convention

```text
positive current = draw from the applicable source
negative current = return toward the applicable source
```

Applies per declared energy envelope. WP-012 R1–R5 anti double-count retained: no parallel counting of returned/reactive/storage in `I_CH_IN_n`/`I_DOM_IN_x` and `I_STORAGE_NET`.

## 2. Measurement roles

| Measurement ID | Quantity | Functional location | Envelope | Sign | Purpose | BW | Accuracy | Isolation/ref | Instrument class | Calibration | Evidence consumer | Status | Closure |
|----------------|----------|---------------------|----------|------|---------|----|----------|---------------|------------------|-------------|-------------------|--------|---------|
| FX-MP-ENTRY-V | V_ENTRY | Base entry | Base | — | Envelope V | Open | Open (ED-IN) | OI-GND-001 | Voltage sense | Proposed | DK-C entry | PROPOSED | Fixture design |
| FX-MP-ENTRY-I | I_ENTRY_MEAS | Base entry | Base | + draw | Entry current | Open | Open | OI-GND-001 | Current sense | Proposed | DK-C entry | PROPOSED | Fixture design |
| FX-MP-DOM-I-* | I_DOM_IN_x | Domain rails | Base | Signed | Domain budget | Open | Open | — | Current sense | Proposed | Sizing/VE | PROPOSED | ED-IN rails |
| FX-MP-CH-IN-* | I_CH_IN_n | Source-referred ch | Base | Signed | Channel contribution | Open | Open | — | Derived/sense | Proposed | WP-012 | PROPOSED | OI-SENSE-001 |
| FX-MP-LOAD-* | I_LOAD_n | Channel output | Base/Ext | Load | Load current | Open | Open | — | Current sense | Proposed | DK-C | PROPOSED | Same |
| FX-MP-STORAGE | I_STORAGE_NET | Unalloc shared only | Base | Signed | Storage path | Open | Open | — | Current sense | Proposed | Budget | PROPOSED | Declare or 0 |
| FX-MP-KILL-RAW | KILL raw | DUT KILL input | Aux/DUT | Logic | Stimulus | Open | — | — | Digital | Proposed | A-012/014 | PROPOSED | — |
| FX-MP-KILL-HW | HW-effective KILL | Power disable | DUT | Logic | Direct path | Open | — | — | Digital | Proposed | Safety | PROPOSED | — |
| FX-MP-KILL-OBS | Logic-observed KILL | Logic | DUT | Logic | Observation | Open | — | — | Digital | Proposed | Safety | PROPOSED | — |
| FX-MP-NEN | nENABLE_GLOBAL | Enable | DUT | Logic | Distinct enable | Open | — | — | Digital | Proposed | Safety | PROPOSED | — |
| FX-MP-ESTOP | Fixture E-stop | Fixture | Aux | Logic | E-stop state | Open | — | — | Digital | Proposed | Safety | PROPOSED | — |
| FX-MP-AUTH-* | AUTH_* states | Fixture | Aux | Logic | Authority | Open | — | — | Digital | Proposed | Governance | PROPOSED | — |
| FX-MP-LB-STATE | Load-bank state | EXT-LOAD-BANK | External | — | Sink status | Open | Open | OI-GND-001 | Status/I | Proposed | Ext evidence | PROPOSED | OI-FIX-001 |
| FX-MP-FAULT | Fault-inject state | Fault domain | Declared | — | Armed/active | Open | — | — | Digital | Proposed | ADR-023 | PROPOSED | — |
| FX-MP-SAFE-OUT | Output safe-state | DUT outs | Base | — | OFF confirm | Open | — | — | V/I | Proposed | Safe-state | PROPOSED | — |
| FX-MP-EXT-* | Ext V/I | EXT-SOURCE/MODULE | External | Per EXT | Ext envelope | Open | Open | OI-GND-001 | Sense | Proposed | Ext evidence | BLOCKED_BY_ARCHITECTURE | OI-GND-001 |

Carry-forward DevKit MPs (MP-IN-V, MP-IN-I, MP-KILL-*, MP-GLOBAL-ENABLE, MP-CH-*, MP-*-RAIL, MP-LOAD-*-RETURN) remain valid roles; fixture may provide access without renaming Accepted MP registry.

## 3. Functional interfaces

| Interface | Direction | Energy | Authority | Safe default | Back-feed | Domain | Observation | Fault containment | GND dep | Config/ID | Physical |
|-----------|-----------|--------|-----------|--------------|-----------|--------|-------------|-------------------|---------|-----------|----------|
| IF-FX-BASE-SOURCE | Source→DUT | In | AUTH_BASE | Off | N/A | Base | FX-MP-ENTRY-* | P0/P1 | — | Required | Open |
| IF-FX-EXT-SOURCE | Ext→module/DUT path | In | AUTH_EXT | Off | To base prohibited | Ext | FX-MP-EXT-* | Ext removal | OI-GND-001 | Required | Open |
| IF-FX-LOAD-BANK | DUT→sink | Out absorb | AUTH_LOAD_BANK | Inactive | Not a source | Ext/Base load | FX-MP-LB-* | Revoke AUTH_LOAD_BANK; remove/inhibit upstream energy; confirm safe state; lock out restart | OI-GND-001 | Required | Open |
| IF-FX-EXT-POWER | Fixture↔module | Ext | AUTH_EXT_POWER | Off | To base prohibited | Ext | Module MPs | Independent | OI-GND-001 | Required | Open |
| IF-FX-DUT-POWER | Fixture↔DUT power | Base | AUTH_BASE | Off | — | Base | Entry/ch | Disconnect | — | Required | Open |
| IF-FX-DUT-LOGIC | Fixture↔Logic | Signal | — | Safe | — | Aux | Comm | — | — | Required | Open |
| IF-FX-DUT-KILL | Fixture↔KILL | Signal/HW | AUTH_FAULT / test | Inactive assert | — | Safety | FX-MP-KILL-* | Direct path | — | Required | Open |
| IF-FX-DUT-ENABLE | Fixture↔nENABLE | Signal | AUTH_DUT_ENABLE | Inactive | — | Safety | FX-MP-NEN | Distinct | — | Required | Open |
| IF-FX-DUT-COMM | Service/SPI/etc | Signal | None hazardous | — | — | Service | — | No energy AUTH | — | — | Open |
| IF-FX-FAULT-INJECTION | Fixture→DUT path | Conditional | AUTH_FAULT | Inhibited | Contained | Fault | FX-MP-FAULT | Bound+backup | — | Required | Open |
| IF-FX-MEASUREMENT | Sense | No power | — | High-Z/safe | No energy path | Declared | All FX-MP | Measurement-path protection and reference method Open; no isolation topology selected | OI-GND-001 | — | Open |
| IF-FX-E-STOP | Operator→fixture | Safety | Overrides | Asserted safe | — | Emergency | FX-MP-ESTOP | Removal | — | — | Open |
| IF-FX-SERVICE | UI/service | Signal | Request only | No AUTH | — | Service | — | No direct energy | — | — | Open |

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture interface and measurement register — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — load-bank fault containment; measurement isolation wording |
| 1.2 | 2026-07-20 | Architecture Review **Accepted** (WP-014; reviewed head `084f579`, PR #18); Open decisions retained; NOT VERIFIED |
