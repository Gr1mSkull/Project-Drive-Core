# DevKit Load and Fault Profile Catalog — WP-014

**Document ID:** DOC-DK-LFPC-001  
**Version:** 1.2  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Abstract load/fault classes only — no physical loads, ratings, or injection circuits Approved.
P0–P6 meaning unchanged from Accepted WP-009/WP-012.
```

## 1. Representative load classes

| Load class | Behaviour (symbolic) | Energy direction | Capability alias | Observables | Protection | Thermal | Fault | Fixture authority | Missing inputs | Readiness |
|------------|----------------------|------------------|------------------|-------------|------------------|---------|-------|-------------------|----------------|-----------|
| LOAD-RESISTIVE | R load | Draw from DUT out | CH-HS-BASE | V_LOAD, I_LOAD | OC path | P_LOSS | Overload | AUTH_LOAD_BANK or base load | ED-IN-026 | PARTIAL |
| LOAD-INCANDESCENT_OR_INRUSH | High inrush then settle | Draw | CH-HS-BASE/PWM | I peak/avg | Inrush vs OC | Transient heat | Inrush | AUTH_LOAD_BANK | ED-IN-027 | PARTIAL |
| LOAD-INDUCTIVE | L with stored energy | Draw; clamp on interrupt | CH-HS-* | V spike, I | Clamp/energy | Pulse | Open under current | AUTH_LOAD_BANK | Clamp energy Open | PARTIAL |
| LOAD-MOTOR_UNIDIRECTIONAL | Motor-like | Draw | CH-HS-* | I, speed proxy Open | Stall/OC | Continuous | Stall | AUTH_LOAD_BANK | ED-IN-020 | BLOCKED_BY_FIXTURE_DESIGN (detail) |
| LOAD-MOTOR_BIDIRECTIONAL | Reversible | Both | CH-BI-REP | I dir, V | Shoot-through/stall | Both | Conflict/stall | AUTH_LOAD_BANK + BI setup | OI-BI-001 | BLOCKED_BY_ARCHITECTURE |
| LOAD-PWM | PWM switched | Draw (avg/rms) | CH-HS-PWM | I_RMS, D, f | Same | Switching loss | — | AUTH_LOAD_BANK | ED-IN-010 | PARTIAL |
| LOAD-CAPACITIVE | C charge | Draw pulse | CH-HS-* | I pulse | Inrush | Pulse | Short-like | AUTH_LOAD_BANK | — | PARTIAL |
| LOAD-ELECTRONIC | Programmable sink | Draw (not source) | Multiple | I cmd | Electronic limit | Device | Fail-to-remove | AUTH_LOAD_BANK | Ratings Open | PARTIAL |
| LOAD-OPEN | Open circuit | None | OL conditional | V open | OL diag claim | — | Open inject | AUTH_FAULT | PWR-A-010 | PARTIAL |
| LOAD-SHORT | Hard short | Fault energy | CH-HS-PROTECTED | I_FAULT | SC path | Pulse | Hard short | AUTH_FAULT | OI-SC-001; ED-IN-021 | BLOCKED_BY_FIXTURE_DESIGN |
| LOAD-STALL | Stall torque/current | Draw / heat | CH-BI-REP | I_STALL | Stall protect | Accum | Stall | AUTH_FAULT/LOAD | OI-FIX-002; TBD-DK-022 | BLOCKED_BY_FIXTURE_DESIGN |
| LOAD-REGENERATIVE_OR_RETURNING | Return toward source | Return (I&lt;0) | CH-BI-REP | I_CH_IN signed | Clamp/absorb | Bridge loss | Regen | AUTH_* + absorb path | Absorption topology Open | BLOCKED_BY_ARCHITECTURE |

## 2. Operating profiles P0–P6 (mapping only)

| Profile | Purpose | Energized domains | Source AUTH | Load class (typical) | Direction | Capability role | Measurement boundary | Fault inject | Thermal | Protection | Preconditions | Safe exit | Missing inputs | Cases (examples) |
|---------|---------|-------------------|-------------|----------------------|-----------|-----------------|----------------------|--------------|---------|------------|---------------|-----------|----------------|------------------|
| **P0** | Quiescent / idle | BASE minimal | AUTH_BASE | none/open | — | — | I_ENTRY, rails | No | Low | Baseline | READY→BASE | SAFE_OFF | Envelope Open | A/C baseline |
| **P1** | Single channel continuous | BASE + 1 ch | AUTH_BASE | RESISTIVE/PWM | Draw | CH-HS-BASE/PWM | I_ENTRY, I_LOAD, I_CH_IN | No default | Cont. | Channel | TEST_ACTIVE | De-energize | ED-IN-002/026 | C-002 |
| **P2** | Multi-channel concurrent | BASE + N ch | AUTH_BASE | RESISTIVE | Draw | Concurrent aliases | Entry + channels | No default | Cont. | Domain/ch | Overlap policy | De-energize | TBD-DK-003 | C-003 |
| **P3** | PWM representative | BASE + PWM ch | AUTH_BASE | PWM | Draw | CH-HS-PWM | I_RMS, f | No default | Switching | Channel | f_PWM Open | De-energize | ED-IN-010 | C-004 area |
| **P4** | Fault / protection | BASE + fault AUTH | AUTH_BASE+FAULT | SHORT/OPEN/OVER | Fault | PROTECTED | Fault MPs | Yes (armed) | Pulse | P2–P5 | FAULT_* states | ENERGY_REMOVAL→LOCKOUT | Bounds Open | C-005/006 |
| **P5** | Control-loss / KILL / enable | BASE as needed | AUTH_BASE | as profile | — | Safety | KILL/ENABLE MPs | Stimulus | — | P5 | Dedicated | ENERGY_REMOVAL | TBD-DK-007 | A-012/014; C-012 |
| **P6** | External envelope | EXT domains only (not simultaneous with BASE while OI-GND-001 Open) | AUTH_EXT_* | EXT load/module | Ext | CH-HC-EXTERNAL / ext | Ext MPs only | Bounded | Ext | Ext + back-feed | EXTERNAL_ENERGY_ARMED (auth only; physical EXT energization blocked for combined BASE/EXT while OI-GND-001 Open) | Independent EXT removal | OI-FIX-001; OI-GND-001 | ADR-020 HC |

P6 remains **outside** base `I_certified_cont` certification (PWR-A-001/002). Combined BASE/EXT execution of P6 while OI-GND-001 Open: **BLOCKED_BY_ARCHITECTURE**. `EXTERNAL_ENERGY_ARMED` does not energize EXT paths by itself.

## 3. Fault-injection capability catalog

| Capability | Default | Auth | Blockers | Notes |
|------------|---------|------|----------|-------|
| Open circuit | Inhibited | AUTH_FAULT | — | Conditional OL (PWR-A-010) |
| Controlled overload | Inhibited | AUTH_FAULT | Energy bound Open | |
| Hard short circuit | Inhibited | AUTH_FAULT | OI-SC-001; ED-IN-021 | Lab-supervised (ADR-023) |
| Input interruption | Inhibited | AUTH_FAULT / source | — | |
| Undervoltage | Inhibited | AUTH_FAULT / source | TBD-DK UV | |
| Reverse-polarity boundary | Inhibited | AUTH_FAULT | OI-PROT-001 | BLOCKED_BY_ARCHITECTURE (method) |
| Control-link loss | Inhibited | AUTH_FAULT | — | J_LP disconnect |
| Watchdog stimulus | Inhibited | AUTH_FAULT | Fixture design | A-011 |
| KILL assertion | Inhibited | AUTH_FAULT | — | Independent of SW |
| nENABLE_GLOBAL removal | Inhibited | AUTH_FAULT | — | Distinct from KILL |
| BI conflict attempt | Inhibited | AUTH_FAULT | OI-BI-001 | |
| BI stall | Inhibited | AUTH_FAULT | OI-FIX-002; TBD-DK-022 | |
| Measurement-path fault | Inhibited | AUTH_FAULT | Method Open | |
| External back-feed challenge | Inhibited | AUTH_FAULT | OI-GND-001; OI-FIX-001 | BLOCKED_BY_ARCHITECTURE (GND) |

## 4. Fault-energy governance

Required fields per energy-producing fault: energy source · source impedance · prospective fault current · fault duration · first/backup protection · energy-removal authority · affected paths · measurement boundary · operator risk · residual energy.

```text
E_FAULT = ∫ V(t) × I(t) dt
E_FAULT_BOUND = V_BOUND × I_BOUND × T_BOUND   # only if V_BOUND, I_BOUND, T_BOUND are proven bounds
```

Else **BLOCKED_BY_INPUT**. The bound form is a **candidate analytical form**, **non-normative**, and **not conservative unless every input is a proven bound**. `V_nom`, `I_nom`, typical current, and expected clearing time are not conservative bounds without separate proof.

## 5. Bidirectional energy separation

```text
E_SOURCE_STALL · E_BRIDGE_LOSS · E_LOAD_ABSORBED · E_RETURNED · E_CLAMPED
```

Do not equate source stall energy with bridge thermal loss.

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial load and fault profile catalog — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — P6 EXTERNAL_ENERGY_ARMED name; OI-GND combined block |
| 1.2 | 2026-07-20 | WP-014-R2 — fault-energy candidate/non-normative label; no nominal bound |
