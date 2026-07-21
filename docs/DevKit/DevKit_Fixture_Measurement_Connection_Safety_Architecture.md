# DevKit Fixture Measurement-Connection Safety Architecture — WP-016

**Document ID:** DOC-DK-FMCSA-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Architecture DECISION PROPOSAL only. No instrument, DAQ, connector, isolation component, or numeric selected.
A physical measurement connection is NOT classified non-energy without proof (FX-PD-018 Accepted).
OI-SENSE-001 remains OPEN until the System Architect accepts an explicit closure.
```

## 1. Issue (exact)

Measurement connections were accepted (WP-015 R1, `FX-PD-018`) as **potential energy/reference/fault paths until qualified**. WP-016 defines the safety architecture and detailed-design input requirements for each measurement class, without selecting instruments or isolation topology. `OI-SENSE-001` (sense accuracy/topology) remains Open.

## 2. Measurement concept separation (per class)

```text
measurement function            — the quantity to observe
physical conductor              — the wire/path (potential energy/fault path)
instrument input                — finite-impedance terminal (possible energy path)
reference connection            — reference/return (possible cross-envelope link)
safety observation              — observation consumed by the safety layer
independent reference instrument — separate qualified instrument for evidence independence
```

## 3. Measurement class safety table

| Class | Potential normal energy | Potential fault energy | Source/reference envelope | Unintended return path | Back-feed path | Input-limiting req | Protection req | Isolation dependency | Calibration dependency | Independence req | Safe failure behavior | Blocker |
|-------|-------------------------|------------------------|---------------------------|------------------------|----------------|--------------------|----------------|----------------------|------------------------|------------------|-----------------------|---------|
| `I_LOAD_n` | Load-level | Fault current if shunt/path fails | Per envelope (base/ext) | Via return/reference | Via instrument ground | Yes | Series/shunt protection | OI-GND-001 | Accuracy Open | For evidence | Open/high-Z on fail; block dependent test | OI-GND-001; OI-SENSE-001 |
| `I_CH_IN_n` | Channel-level (signed) | Fault current | Base | Reference share | Instrument path | Yes | Protection | — | Accuracy Open | For evidence | Fail-safe observe | OI-SENSE-001 |
| `I_DOM_IN_x` | Domain-level | Fault current | Base | Reference share | Instrument path | Yes | Protection | — | Open | — | Fail-safe | thresholds Open |
| `I_ENTRY_MEAS` | Entry-level | Prospective fault current | Per envelope | Reference | Instrument ground | Yes | Protection + limiting | OI-GND-001 | Open | For evidence | Fail-safe | OI-GND-001 |
| `V_DUT_ENTRY` | Entry voltage | OV/transient | Per envelope | Reference | Probe ground | High-Z + limiting | Clamp/limit | OI-GND-001 | Open | — | High-Z on fail | OI-GND-001; OI-PROT-002 |
| `V_DOMAIN_x` | Rail voltage | Rail fault | Base | Reference | Probe ground | High-Z | Limit | — | Open | — | High-Z | thresholds Open |
| `V_CHANNEL_n` | Channel voltage | Channel fault | Base | Reference | Probe | High-Z | Limit | — | — | — | High-Z | — |
| `V_LOAD_n` | Load voltage | Load fault/OV | Per envelope | Reference | Probe ground | High-Z | Limit | OI-GND-001 | Open | — | High-Z | OI-GND-001 |
| KILL observation | Logic | Coupled fault | DUT | Reference | — | Yes | Buffer/limit | — | — | Independent of actuation | Fail-safe read | — |
| nENABLE_GLOBAL observation | Logic | Coupled fault | DUT | Reference | — | Yes | Buffer/limit | — | — | Distinct | Fail-safe | — |
| E-stop integrity observation | Logic/continuity | Coupled | Aux | Reference | — | Yes | Buffer/monitor | — | — | Independent | Inhibit on loss | REQ-DCC-V-FX-071 |
| residual-energy observation | Stored energy | Residual discharge | Per envelope | Reference | Probe | High-Z + limiting | Bleed/limit | OI-GND-001 | Open | For recovery gate | Hold lockout if unconfirmed | timing Open |

No class is classified non-energy without proof. Each physical conductor and instrument input is treated as a potential energy/reference/fault path until qualified.

## 4. Architecture requirements (proposed)

- Each measurement connection shall have a defined input-limiting and protection requirement and a defined reference boundary before it is used for a safety observation.
- Cross-envelope measurement (base↔external) is gated by OI-GND-001; until dispositioned, cross-envelope references are `BLOCKED_BY_ARCHITECTURE`.
- Safety observations (KILL, nENABLE, E-stop integrity, residual energy) shall be independent of the actuation path they observe.
- Evidence-grade measurements shall use an independent reference instrument (FX-PD-011/012 Accepted).
- Unavailable required measurement blocks the dependent test and inhibits dependent AUTH.

## 5. Detailed-design input requirements (measurement)

Each class contributes `FX-DD-IN-*` entries (see detailed-design input register): input impedance, protection/limiting, reference/return, isolation dependency (OI-GND-001), calibration, independence, and safe-failure behavior — all values **Open**; none Approved by WP-016.

## 6. Proposed issue disposition

| Issue | Existing status | WP-016 recommendation | Residual blocker | Proposed Architect action |
|-------|-----------------|-----------------------|------------------|---------------------------|
| OI-SENSE-001 | OPEN | SPLIT: architecture-closed (measurement-connection safety model + independence) + implementation-open (topology/accuracy) | Accuracy/topology + OI-GND-001 | ACCEPT ARCHITECTURE; SPLIT / DEFER |

`OI-SENSE-001` remains Open unless the Architect accepts an explicit closure.

## 7. Traceability

FX-PD-007/011/012/018 · OI-SENSE-001 · OI-GND-001 · OI-PROT-002 · REQ-DCC-V-FX-060/061/062/071 · ED-IN-011/032 · WP-014 FIMR (FX-MP-*).

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial measurement-connection safety architecture — Proposed |
