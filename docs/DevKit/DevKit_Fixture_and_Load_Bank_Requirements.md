# DevKit Fixture and Load-Bank Requirements — WP-014

**Document ID:** DOC-DK-FLBR-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
All REQ-DCC-V-FX-* remain PROPOSED until Architecture Review.
No MPN · no ratings · no construction · no VE · NOT VERIFIED.
```

## 1. Purpose

Normative **Proposed** requirements for a future laboratory fixture and load-bank supporting Gen1 DevKit verification. Prefix **`REQ-DCC-V-FX-`** is newly allocated (unused before WP-014).

## 2. Requirement status

Every FX requirement: **PROPOSED**. Physical verification: not performed. Separations: Proposed ≠ Accepted ≠ constructed ≠ demonstrated ≠ Verified.

## 3. Energization authorities

| Authority | Default | Observable | Revoked by |
|-----------|---------|------------|------------|
| AUTH_BASE_SOURCE | Inactive | Required | E-stop; invalid state; control loss (where applicable) |
| AUTH_EXT_SOURCE | Inactive | Required | Same |
| AUTH_LOAD_BANK | Inactive | Required | Same |
| AUTH_EXT_POWER_MODULE | Inactive | Required | Same |
| AUTH_FAULT_INJECTION | Inactive | Required | Same |
| AUTH_DUT_ENABLE | Inactive | Required | Same; also DUT KILL / nENABLE paths per DUT rules |

Radio/Tablet may **request**; fixture safety layer **decides**.

---

## 4. Requirements

### 4.1 Fixture state and identity

#### REQ-DCC-V-FX-001

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-001` |
| Statement | The fixture shall implement the state set SAFE_OFF, INSPECTION, READY, BASE_ENERGIZED, EXTERNAL_ENERGY_ARMED, TEST_ACTIVE, FAULT_INJECTION_ARMED, FAULT_ACTIVE, ENERGY_REMOVAL, POST_FAULT_LOCKOUT, RECOVERY_VALIDATION per DOC-DK-FFA-001. |
| Status | PROPOSED |
| Safe minimum | Uncommanded startup and power restoration enter SAFE_OFF |

#### REQ-DCC-V-FX-002

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-002` |
| Statement | Power restoration, E-stop, physical KILL, fixture power interruption, source interruption, controller reset, invalid identity, invalid configuration, or loss of fixture-control authority shall invalidate prior fixture commands (stale). A new command epoch shall be required before hazardous-energy AUTH grant. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-003

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-003` |
| Statement | Invalid or unsupported fixture identity shall inhibit hazardous energy, fault injection, and external energy, and shall prevent test configuration execution. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-004

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-004` |
| Statement | Invalid fixture configuration shall inhibit hazardous energy and shall not execute the invalid configuration. |
| Status | PROPOSED |

### 4.2 Safety authorities

#### REQ-DCC-V-FX-010

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-010` |
| Statement | Fixture E-stop shall remove or inhibit fixture-controlled hazardous energy, including external energy, independently of DevKit firmware, Radio, Tablet, and SPI/DCPI; shall default to energy-inhibited; shall require deliberate reset; shall invalidate prior test commands; shall prevent automatic test resumption. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-011

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-011` |
| Statement | Fixture E-stop shall not replace DUT physical KILL. DUT physical KILL shall not replace fixture E-stop. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-012

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-012` |
| Statement | The fixture shall support independent observation and actuation testing of DUT physical KILL (direct hardware-effective path) and Logic observation path without requiring Radio or Tablet. |
| Status | PROPOSED |
| Trace | PWR-A-004; ADR-022 |

#### REQ-DCC-V-FX-013

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-013` |
| Statement | The fixture shall support independent control and observation of `nENABLE_GLOBAL` as distinct from physical KILL and fixture E-stop. |
| Status | PROPOSED |
| Trace | PWR-A-005 |

#### REQ-DCC-V-FX-014

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-014` |
| Statement | AUTH_BASE_SOURCE, AUTH_EXT_SOURCE, AUTH_LOAD_BANK, AUTH_EXT_POWER_MODULE, AUTH_FAULT_INJECTION, and AUTH_DUT_ENABLE shall each default inactive, be independently observable, require valid fixture state, be revoked by fixture E-stop and invalid fixture state, and shall not automatically restore after interruption. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-015

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-015` |
| Statement | Radio and Tablet shall have no direct hazardous-energy authority. Service UIs may request actions only. |
| Status | PROPOSED |

### 4.3 Base source

#### REQ-DCC-V-FX-020

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-020` |
| Statement | The fixture shall provide controlled BASE-SOURCE output authority (AUTH_BASE_SOURCE) with observable source state. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-021

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-021` |
| Statement | Source-current limitation shall be treated as one protection layer (P0) and shall not be the sole protection layer for DevKit verification. |
| Status | PROPOSED |
| Trace | PWR-A-017 (PROPOSED_CONSTRAINT); WP-012 P0–P5 |

#### REQ-DCC-V-FX-022

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-022` |
| Statement | The fixture shall provide controlled input interruption capability for base-envelope tests. |
| Status | PROPOSED |
| Numeric | Open (TBD/ED-IN) |

#### REQ-DCC-V-FX-023

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-023` |
| Statement | The fixture shall provide a reverse-polarity **test boundary** capability for base input. Topology remains Open (OI-PROT-001). Dependent realization: BLOCKED_BY_ARCHITECTURE until OI-PROT-001. |
| Status | PROPOSED / BLOCKED_BY_ARCHITECTURE (realization) |

#### REQ-DCC-V-FX-024

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-024` |
| Statement | The fixture shall provide undervoltage and overvoltage/transient **test boundaries** for base input. Numeric limits Open; OI-PROT-002 Open for transient method. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-025

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-025` |
| Statement | Prospective fault-energy for fixture-controlled faults shall be governed per DOC-DK-FLBR §6 and WP-012 `E_FAULT` rules. Unproven bounds ⇒ BLOCKED_BY_INPUT for that fault profile. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-026

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-026` |
| Statement | The fixture shall provide safe disconnection of BASE-SOURCE under ENERGY_REMOVAL without requiring DUT firmware. |
| Status | PROPOSED |

### 4.4 External source / load bank / power module

#### REQ-DCC-V-FX-030

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-030` |
| Statement | EXT-SOURCE shall have separate energy authority (AUTH_EXT_SOURCE), independent energy removal, back-feed prevention to base, envelope identification, and separate evidence classification. |
| Status | PROPOSED |
| Trace | ADR-020/021; OI-FIX-001; PWR-A-001…003 |

#### REQ-DCC-V-FX-031

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-031` |
| Statement | EXT-SOURCE ground/reference relationship to base remains Open (OI-GND-001). Dependent detailed interconnection requirements: BLOCKED_BY_ARCHITECTURE. |
| Status | PROPOSED / BLOCKED_BY_ARCHITECTURE (GND detail) |

#### REQ-DCC-V-FX-032

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-032` |
| Statement | EXT-LOAD-BANK shall absorb energy under AUTH_LOAD_BANK; shall not be described or used as an energy source; shall provide commanded load removal, thermal protection requirements (limits Open), failure-to-remove-load response (safe minimum: remove AUTH and enter ENERGY_REMOVAL), measurement boundary, and external-load-bank evidence scope. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-033

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-033` |
| Statement | EXT-POWER-MODULE shall remain functionally separate from base DevKit, carry independent external rating, provide interface protection and safe de-energization, and use separate evidence scope. |
| Status | PROPOSED |
| Trace | ADR-020 |

#### REQ-DCC-V-FX-034

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-034` |
| Statement | External ratings shall not increase `I_certified_cont` or certify the base distribution path. |
| Status | PROPOSED |
| Trace | PWR-A-002 |

### 4.5 Fixture auxiliary

#### REQ-DCC-V-FX-040

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-040` |
| Statement | FIXTURE-AUX shall support fixture-control operation independent of DUT state where required for E-stop and inhibit functions; AUX loss shall not cause uncontrolled DUT energization; indication/logging availability requirements apply (details Open). |
| Status | PROPOSED |

### 4.6 Loads, faults, bidirectional

#### REQ-DCC-V-FX-050

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-050` |
| Statement | The fixture shall support abstract load classes LOAD-RESISTIVE, LOAD-INCANDESCENT_OR_INRUSH, LOAD-INDUCTIVE, LOAD-MOTOR_UNIDIRECTIONAL, LOAD-MOTOR_BIDIRECTIONAL, LOAD-PWM, LOAD-CAPACITIVE, LOAD-ELECTRONIC, LOAD-OPEN, LOAD-SHORT, LOAD-STALL, LOAD-REGENERATIVE_OR_RETURNING per DOC-DK-LFPC-001 without selecting physical ratings. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-051

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-051` |
| Statement | Operating profiles P0–P6 shall be mappable to fixture functions without changing Accepted WP-009/WP-012 meaning and without assigning numeric currents. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-052

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-052` |
| Statement | Fault injection shall be deliberate, bounded, state-controlled, disabled by default, inhibited by E-stop, separately authorized (AUTH_FAULT_INJECTION), observable, logged, recoverable only through controlled sequence, non-persistent after reset, and non-auto-resuming after interruption (ADR-023). |
| Status | PROPOSED |

#### REQ-DCC-V-FX-053

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-053` |
| Statement | Abstract injection capabilities shall include: open circuit; controlled overload; hard short circuit; input interruption; undervoltage; reverse-polarity boundary; control-link loss; watchdog stimulus; KILL assertion; nENABLE_GLOBAL removal; bidirectional conflict attempt; bidirectional stall; measurement-path fault; external back-feed challenge. Physical circuits not defined. Blocked items marked in catalog. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-054

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-054` |
| Statement | For energy-producing faults, the fixture requirements package shall require definition of: energy source; source impedance; prospective fault current; fault duration; first and backup protection layers; energy-removal authority; affected conductor/connector/PCB/semiconductor paths; measurement boundary; operator risk; residual energy. Numeric values Open. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-055

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-055` |
| Statement | `E_FAULT = ∫ V(t)×I(t) dt`. Bound `V_BOUND×I_BOUND×T_BOUND` only when bounds proven; else BLOCKED_BY_INPUT. Nominal multiplication without proof is not conservative. |
| Status | PROPOSED |
| Trace | WP-012/WP-013-R1 |

#### REQ-DCC-V-FX-056

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-056` |
| Statement | Bidirectional tests shall distinguish E_SOURCE_STALL, E_BRIDGE_LOSS, E_LOAD_ABSORBED, E_RETURNED, E_CLAMPED; shall not assume source can absorb return; shall not assume load bank acts as source. Final regen topology BLOCKED_BY_ARCHITECTURE / component inputs (OI-BI-001). |
| Status | PROPOSED |

### 4.7 Measurement

#### REQ-DCC-V-FX-060

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-060` |
| Statement | Measurement architecture shall provide distinct roles for I_ENTRY_MEAS, I_DOM_IN_x, I_CH_IN_n, I_LOAD_n, I_STORAGE_NET, related voltages, KILL raw/conditioned/observed, nENABLE_GLOBAL, fixture E-stop, source enables, load-bank state, fault-injection state, and representative output safe-state result per DOC-DK-FIMR-001. |
| Status | PROPOSED |

#### REQ-DCC-V-FX-061

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-061` |
| Statement | Sign convention: positive current = draw from the applicable source; negative = return toward the applicable source. Returned/reactive/storage energy shall not be double-counted across I_CH_IN_n / I_DOM_IN_x and I_STORAGE_NET (WP-012 R1–R5). |
| Status | PROPOSED |

#### REQ-DCC-V-FX-062

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-062` |
| Statement | An instrument connection shall not become an uncontrolled energy path. Unavailable measurement shall block tests that depend on that measurement. |
| Status | PROPOSED |

### 4.8 Interfaces (functional)

#### REQ-DCC-V-FX-070

| Field | Value |
|-------|-------|
| Requirement ID | `REQ-DCC-V-FX-070` |
| Statement | The fixture shall define functional interfaces IF-FX-BASE-SOURCE, IF-FX-EXT-SOURCE, IF-FX-LOAD-BANK, IF-FX-EXT-POWER, IF-FX-DUT-POWER, IF-FX-DUT-LOGIC, IF-FX-DUT-KILL, IF-FX-DUT-ENABLE, IF-FX-DUT-COMM, IF-FX-FAULT-INJECTION, IF-FX-MEASUREMENT, IF-FX-E-STOP, IF-FX-SERVICE with safe defaults and prohibited back-feed. Physical connectors/pinouts remain Open. |
| Status | PROPOSED |

## 5. Interlock principles (normative summary)

1. Hazardous energy defaults inhibited.  
2. Fault injection defaults inhibited.  
3. External energy requires independent authority.  
4. Fixture E-stop overrides all fixture-controlled hazardous-energy commands.  
5. DUT KILL remains independently testable.  
6. Loss of control does not restore previous authority.  
7–8. Invalid identity/configuration inhibit hazardous energy.  
9. Source-to-source connection prohibited unless future Accepted topology.  
10. Back-feed prevention mandatory.  
11. Stored energy: controlled discharge or confirmed safe decay.  
12. E-stop reset does not itself energize.  
13. Test start requires new command epoch.  
14. Fault recovery requires deliberate authorization.  
15. Software-only interlocks do not replace required hardware-effective protection.  
16–20. Instrument not uncontrolled energy path; tablet/radio not safety-critical; unavailable measurement blocks dependent tests; unconfirmed state unsafe; protection failure not hidden by automatic retry.

## 6. Traceability

REQ-DCC-V-DK-* · VER-DCC-DK-* · ADR-019…023 · TBD-DK-* · ED-IN-* · OI-* · PWR-A-* · WP-012/013.

## 7. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture and load-bank requirements — Proposed |
