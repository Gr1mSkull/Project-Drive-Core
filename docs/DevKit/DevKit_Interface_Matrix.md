# DevKit Interface Matrix — Gen1

**Document ID:** DOC-DK-IF-001  
**Version:** 1.0.2  
**Status:** Proposed  
**Work Package:** WP-007 / WP-007-R2  
**Date:** 2026-07-19

> Interface inventory for verification planning.  
> **Does not create new pinouts.** References existing authoritative pinouts where available (`docs/002`, EDL-011).  
> Production fidelity for Logic/Radio physical identity remains ADR-DK-001/002.  
> `TBD-DK-*` identifiers referenced below are defined only in [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md) §4 (authoritative Threshold Resolution Register).

## Interfaces

| Interface ID | Endpoints | Purpose | Type | Direction | Existing source | Production fidelity | Safety critical | Required phase | Observability | Fault injection | Failure behaviour | Version identity | Status |
|--------------|-----------|---------|------|-----------|-----------------|---------------------|-----------------|----------------|---------------|-----------------|-------------------|------------------|--------|
| IF-DK-PWR-IN | Bench PSU → DevKit power entry | Laboratory energization | Power | Input | docs/008 §2–3 (candidate); REQ-DCC-V-DK-019 | Representative | Yes | A | Voltage/current at entry | Interrupt supply / open protection | De-energize / protection trip — limits TBD-DK-001/002 | N/A | Proposed |
| IF-DK-GND | Bench ground ↔ DevKit ground reference | Safety bonding and measurement reference | Power | Bidirectional | docs/008 bench intent; REQ-DCC-V-DK-025 | Representative | Yes | A | Continuity / bond check | Open ground (unsafe — inspection only) | Measurement invalid; do not energize if open | N/A | Proposed |
| IF-DK-KILL | Kill control → Logic/Power kill path | Independent emergency de-energize | Digital | Input | EDL-011 `nKILL_HW`; docs/002; REQ-DCC-V-DK-031 | Same intent | Yes | A | Logic/diag + output current | Assert kill | Outputs de-energized; timing TBD-DK-004 | N/A | Approved source (EDL-011) / Proposed DevKit testability |
| IF-DK-GENABLE | Global enable path | Global output enable interlock | Digital | Bidirectional / sense | EDL-011 `nENABLE_GLOBAL`; REQ-DCC-V-DK-032 | Same intent | Yes | A | Diagnostic/measurement path | Force disable | Outputs inhibited | N/A | Approved source / Proposed observability |
| IF-DK-JLP | Logic ↔ Power (J_LP) | Commands, PWM, sense, BOARD_ID, kill/enable | SPI + digital + analog | Bidirectional | EDL-011; docs/002 §5 | Same interface intent; physical reuse TBD ADR-DK-001 | Yes | A/C | SPI traffic, sense lines, BOARD_ID | SPI timeout / disconnect | Safe de-energize per EDL-011 timeout intent (TBD-DK-007) | Interface rev per docs/002 | Approved source |
| IF-DK-DCPI | Logic ↔ Radio | Binary state/config/diag exchange | SPI (DCPI) | Bidirectional | EDL-010; docs/004 | Same protocol intent; physical Radio board TBD ADR-DK-002 | No (fail-operational) | A/B | DCPI frames / CRC | Corrupt CRC; disconnect Radio | RT continues fail-op functions; Service degraded | `DCPI_PROTO_VER` legacy encoded; mapping TBD | Approved source |
| IF-DK-CAN | DCC ↔ ECU sim / Button Box sim / sniffer | DCP Gen1 bus | CAN FD | Bidirectional | EDL-008; docs/004 | Same bus intent | TBD (depends on function) | B/D | Sniffer | Stop node; disconnect | Stale/LOST handling TBD-DK-006 | DCP legacy encoded + doc v0.1 | Approved source |
| IF-DK-USB | Host ↔ Logic/Radio programming path | Firmware load / serial as provided | USB | Bidirectional | docs/002 / docs/008 USB-C candidate | Representative (connector family candidate — not mandated here) | No | A | Host enumeration | Unplug during idle | Programming fails safely | N/A | Proposed / Candidate connector |
| IF-DK-SWD | Debugger ↔ Real-Time MCU | Program/debug | Debug | Bidirectional | docs/002 SWD intent; REQ-DCC-V-DK-056 | Representative | No | A | Debugger session | Break/halt under no-load | Outputs remain safe OFF if not commanded | Firmware identity per STD-REV-001 | Proposed |
| IF-DK-OUT-HS | Power channel → load bank | Switched high-side load drive | Power | Output | docs/008 channel table (candidate); WP-004 classes | Representative capability | Yes | C | Voltage/current/diag | Overcurrent/short fixtures (safe) | Protect/OFF + fault | Channel config ID | Proposed |
| IF-DK-OUT-PWM | Power PWM channel → load | PWM drive | Power | Output | WP-004 PWM optional; docs/008 | Representative | Yes | C | Scope/current | PWM out-of-range (when limits exist) | TBD-DK-008 | Channel config ID | Proposed / TBD limits |
| IF-DK-OUT-BD | Bidirectional driver → motor/load | Forward/reverse | Power | Bidirectional | docs/008 HB candidate; BD class Proposed | Representative | Yes | C | Current/voltage/diag | Stall fixture; conflicting commands | Protect; conflict prevention | Channel config ID | Proposed |
| IF-DK-ISENSE | Power sense → Logic | Current observation | Analog | Input to Logic | EDL-011 ISENSE MUX intent; docs/002 | Same intent | Yes | C | ADC/diag vs meter | Open sense (analysis) | Degraded diagnostics — behaviour TBD | N/A | Approved source intent |
| IF-DK-VBATT-SENSE | Supply sense → Logic | Battery/rail observation | Analog | Input | EDL-011 VBATT_SENSE; docs/002 | Same intent | Yes | A/C | Meter vs diag | Undervoltage fixture TBD-DK-012 | Defined UV behaviour | N/A | Approved source intent |
| IF-DK-TEMP | Thermal sensor → Logic | Thermal observation | Analog | Input | EDL-011 NTC intent | Same intent | TBD | C | Temperature reading | Heat soak (controlled) | Thermal protect TBD-DK-018/019 | N/A | Approved source intent |
| IF-DK-FAULT-IND | Power/Logic → operator/UI | Fault indication | Digital / diagnostic | Output | docs/004 events; DC-DCC-PWR diagnostics | Representative | Yes | B/C/D | UI/CAN/DCPI event | Inject fault | Indicated fault state | Event/schema versions | Proposed |
| IF-DK-LOADBANK | Channel outputs ↔ replaceable loads | Laboratory loading | Power / mechanical | Bidirectional connection | docs/008 loads (candidate wattages — not normative) | Not applicable (lab only) | Yes | C | Current/voltage | Overload within approved limits | Operator abort | Fixture rev per STD-REV-001 | Proposed |
| IF-DK-CFG | Host/Service → RT config path | Configuration delivery | Digital / DCPI / network | Input to RT | docs/005; REQ-DCC-V-DK-068 | Same config model intent | Yes | B/D | Apply ack/reject | Invalid config; CRC error | Reject; no unsafe partial enable | schema/DCFG versions; hash when available | Proposed |
| IF-DK-DIAG-OUT | RT/Service → tester | Diagnostics/telemetry | Network / CAN / log | Output | docs/004; docs/006 | Representative | No | B/D | REST/WS/CAN/logs | Service stop | RT fail-op continues | API/telemetry schema versions | Proposed |

## Notes

1. Exact WAGO / DTM / USB-C / Hammond selections in `docs/008` / `docs/007` are **candidate design**, not interface mandates in this matrix.
2. BOARD_ID encoding map remains **TBD-DK-020**.
3. DCFG CRC coverage and encoded-version mappings are **not** resolved here (ADR-015 conditions).

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial Proposed interface matrix |
| 1.0.1 | 2026-07-19 | WP-007-R1 — metadata only; no new pinouts |
| 1.0.2 | 2026-07-19 | WP-007-R2 — TBD authority pointer to System Requirements §4 |
