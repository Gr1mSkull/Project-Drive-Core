# DevKit Fixture Interface and Wiring Architecture — WP-015

**Document ID:** DOC-DK-FIWA-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review (2026-07-21)  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Symbolic interfaces, evaluation wiring classes, and operator control/indication only.
No connector family, pinout, conductor size, insulation, color, or rating selected.
```

## 1. Fixture interface groups (§25)

| Interface ID | Functional signals (symbolic) | Energy class | Direction | Safety relevance | Default state | Separation requirement | Measurement point (ref) | Open issue | Detailed-design owner |
|--------------|-------------------------------|--------------|-----------|------------------|---------------|------------------------|-------------------------|------------|-----------------------|
| `IF-FX-SOURCE` | source enable, source sense | Hazardous | Fixture→source ctrl | High | Inactive | From signal/measurement | I_ENTRY_MEAS, V_DUT_ENTRY | thresholds Open | Source subsystem WP |
| `IF-FX-DUT-POWER` | base power to DUT | Hazardous (base) | Fixture→DUT | High | Off | From logic/comm | I_ENTRY_MEAS | — | DUT interface WP |
| `IF-FX-DUT-LOGIC` | logic I/O | Signal | Bidirectional | Medium | Safe | From power | — | — | DUT interface WP |
| `IF-FX-CAN` | CAN FD | Signal | Bidirectional | Medium | Safe | From power | — | — | Comm WP |
| `IF-FX-KILL` | KILL raw / HW-effective / logic-observed | Signal/HW (safety) | Fixture↔DUT | High (safety) | Inactive assert | Dedicated safety separation | KILL MPs | — | Safety WP |
| `IF-FX-GLOBAL-ENABLE` | nENABLE_GLOBAL | Signal (safety) | Fixture↔DUT | High (safety) | Inactive | Dedicated safety separation | nENABLE MP | — | Safety WP |
| `IF-FX-LOAD-BANK` | sink control, sink sense | Hazardous (load) | DUT→sink | High | Inactive | From source | I_LOAD_n, V_LOAD_n | OI-BI-001 | Load-bank WP |
| `IF-FX-FAULT-INJECTION` | fault stimulus, abort | Conditional | Fixture→DUT | High | Inhibited | Contained | fault MPs | OI-SC-001 | Fault WP |
| `IF-FX-MEASUREMENT` | sense taps | Potential energy/reference/fault path (until qualified) | DUT/fixture→sense | Medium–High (potential energy/fault path) | High-Z/safe (impedance/protection Open) | From energy paths; reference-path Open | all MPs | OI-GND-001 | Measurement WP |
| `IF-FX-DAQ` | acquisition/log | None | Sense→DAQ | Medium | Passive | From energy | — | accuracy Open | DAQ WP |
| `IF-FX-ESTOP` | emergency inhibit | Safety-effective | Operator→fixture | Highest | Asserted-safe | Dedicated | E-stop state | REQ-DCC-V-FX-071 | Safety WP |
| `IF-FX-SERVICE` | service/UI/log | None (never hazardous) | Bidirectional | Low (non-safety) | No AUTH | From safety | — | — | Service WP |
| `IF-FX-EXTERNAL-ENERGY` | ext source/module control+sense | Hazardous (external) | Fixture↔ext | High | Off | From base (distinct) | ext MPs | OI-GND-001 | External WP |

No connector families or pinouts are selected.

## 2. Wiring evaluation classes (§26)

| Class | Functional purpose | Energy class | Separation needs | Routing constraints | Observation requirements | Fault consequences | Required inputs (I/V/thermal) | Connector evaluation inputs | Detailed-design blockers |
|-------|--------------------|--------------|------------------|---------------------|--------------------------|--------------------|-------------------------------|-----------------------------|--------------------------|
| `W-FX-POWER-BASE` | Base hazardous energy | Hazardous (base) | From signal/safety | Short, defined return | Entry/channel MPs | overheat/arc | I/V/thermal Open | derating inputs Open | thresholds; OI-PROT |
| `W-FX-POWER-EXTERNAL` | External hazardous energy | Hazardous (external) | From base; distinct | Separate from base | Ext MPs | back-feed/arc | I/V/thermal Open | derating inputs Open | OI-GND-001 |
| `W-FX-RETURN` | Energy return paths | Hazardous (return) | Defined per envelope | Low-impedance defined | current MPs | ground shift | I/thermal Open | — | OI-GND-001 |
| `W-FX-SAFETY` | E-stop/KILL/enable | Signal (safety) | Dedicated, independent | Integrity-monitored | safety-state MPs | loss of inhibit | integrity inputs Open | — | REQ-DCC-V-FX-071 |
| `W-FX-CONTROL` | Command/control | Signal | From power/safety | Noise-controlled | — | wrong command | — | — | — |
| `W-FX-COMMUNICATION` | CAN/service comms | Signal | From power | Impedance-controlled | — | comm loss | — | — | — |
| `W-FX-MEASUREMENT` | Sense/observation | Potential energy/reference/fault path (until qualified) | From power; high-Z; reference-path controlled | Shielded/twisted (class); protection/impedance Open | all MPs | wrong reading; fault-energy carry; unintended reference/back-feed | accuracy/fault-energy/impedance/protection inputs Open | — | OI-SENSE-001; OI-GND-001 |
| `W-FX-SHIELD` | Shielding/reference | Reference | Per GND decision | Per GND decision | — | noise/ground loop | — | — | OI-GND-001 |
| `W-FX-FAULT-INJECTION` | Fault stimulus routing | Conditional | Contained, dedicated | Contained | fault MPs | uncontrolled fault | bounds Open | — | OI-SC-001 |

No conductor size, insulation type, color, or connector is selected.

**Measurement wiring/interface note (WP-015-R1):** `W-FX-MEASUREMENT` and `IF-FX-MEASUREMENT` are **not** classified as unconditionally non-energy. A measurement conductor/instrument input is treated as a potential energy/reference/fault path until its impedance, protection, reference, isolation, and fault behavior are qualified (see `DevKit_Fixture_Measurement_and_DAQ_Architecture.md` §1). No isolation topology is selected (OI-GND-001 Open).

## 3. Operator control and indication (§27)

Preliminary operator controls (request/command only; never sole safety authority):

```text
MASTER FIXTURE ENABLE · BASE AUTH REQUEST · EXTERNAL AUTH REQUEST · ENERGY REMOVE ·
E-STOP · FAULT RESET · RECOVERY CONFIRM · TEST START · TEST ABORT
```

Preliminary indications (presentation; never substitute for physical energy observation):

```text
FIXTURE SAFE · BASE AUTHORIZED · BASE ENERGY OBSERVED · EXTERNAL AUTHORIZED ·
EXTERNAL ENERGY OBSERVED · LOAD BANK ACTIVE · ENERGY REMOVAL ACTIVE ·
DISCHARGE INCOMPLETE · INTERLOCK OPEN · FAULT · LOCKOUT · MEASUREMENT NOT READY
```

Rules:

- `E-STOP` is a safety-effective control, not merely a UI request.
- UI indication shall not substitute for physical energy observation (`ENERGY_PATH_OBSERVED_*`).
- Tablet, web UI, or service PC shall **not** have sole safety authority (PWR-A-024).

## 4. Traceability

REQ-DCC-V-FX-005/010…015/030…034/040/060…062/070/071 · PWR-A-024 · OI-GND-001 · OI-PROT-001/002 · OI-SC-001 · OI-SENSE-001.

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial interface and wiring architecture (+ operator control/indication) — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — measurement interface/wiring reclassified as potential energy/reference/fault path (not unconditional non-energy) |
| 1.2 | 2026-07-21 | Architecture Review **Accepted** (WP-015 / R1 / R2 / R3; reviewed head `227ea78`, PR #19); Open decisions retained; NOT VERIFIED |
