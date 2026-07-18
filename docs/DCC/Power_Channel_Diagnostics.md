# DCC Power Channel Diagnostics

**Document ID:** DCC-PWR-DIAG-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-004

Diagnostic requirements for DCC power channels. **No hardware specification** (no ADC part numbers, sense resistor values, or PROFET DIAG pin wiring).

Normative requirements: [Power_Channel_Requirements.md](Power_Channel_Requirements.md) § diagnostics (DC-DCC-PWR-081–100).

---

## 1. Purpose

Define what the DCC platform shall observe, record, and report for each power channel so faults are detectable, traceable, and reviewable without prescribing implementation.

## 2. Diagnostic scope

| Layer | Observables |
|-------|-------------|
| Per channel | State, command vs feedback, faults, current **TBD**, optional output voltage **TBD** |
| Per board | Supply voltage, board temperature, global fault aggregate |
| Per vehicle | Load key mapping, VCM mode, simultaneous-group context |

## 3. Required diagnostic capabilities

### 3.1 Current measurement

| Requirement | Detail |
|-------------|--------|
| Availability | SHALL be provided for HC-A, HC-B, MC-A; SHALL be provided for BD-A; SHOULD be provided for LC-A; MAY be provided for LC-B — **TBD** per assignment |
| Resolution | **TBD** |
| Accuracy | **TBD** |
| Sample rate | Sufficient for overcurrent detection time **TBD** |
| Range | Per channel class maximum **TBD** |

### 3.2 Output voltage

| Requirement | Detail |
|-------------|--------|
| Purpose | Open-load detection, wiring fault inference |
| Availability | **TBD** per channel class |
| Accuracy | **TBD** |

### 3.3 Fault flags

Each channel shall expose a structured fault bitmask including at minimum:

| Flag (abstract) | Description |
|-----------------|-------------|
| `OVERCURRENT` | Current exceeds configured limit **TBD** |
| `SHORT_CIRCUIT` | Severe overcurrent classification **TBD** |
| `OPEN_LOAD` | Open circuit detected when enabled |
| `THERMAL` | Channel or zone thermal limit |
| `SUPPLY_UV` | Undervoltage prevented enable |
| `SUPPLY_OV` | Overvoltage event |
| `COMM_LOSS` | Control path invalid |
| `LATCHED` | Channel in latched fault |
| `RETRY_EXHAUSTED` | Retries consumed |

Exact bit assignment **TBD** in firmware spec.

### 3.4 Fault timestamps

- Each fault transition shall record UTC or monotonic timestamp with millisecond resolution **TBD**.
- Latched faults shall retain first-occurrence timestamp until cleared.

### 3.5 Persistent fault log

- SHALL integrate with DCC event log per [docs/005](../005_Configuration_Model.md) §7.
- Format: `<timestamp> <severity> <channel> <load_key> <fault> <message>`
- Examples: `Fan1 Overcurrent`, `Ch07 Latched`, `EHPS Retry 2/3`

### 3.6 Diagnostic counters

Per channel, SHALL maintain:

| Counter | Purpose |
|---------|---------|
| `enable_count` | Total enable cycles |
| `fault_count` | Total fault events |
| `retry_count_total` | Cumulative retries |
| `latch_count` | Times entered Latched Fault |
| `runtime_s` | Total energized time **TBD** precision |

Counters shall survive power cycle if FRAM policy permits — **TBD**.

### 3.7 Health reporting

SHALL expose channel health via:

| Interface | Content |
|-----------|---------|
| DCPI / SPI diag read | Fault bitmap, state, current **TBD** |
| CAN telemetry **TBD** | Aggregated DCC health |
| REST / WebSocket | Per [docs/006](../006_Communication_Protocol.md) when Service layer active |

Health report period **TBD**. Loss of health reporting shall not block fail-safe OFF.

## 4. Diagnostics by channel class

| Class | Minimum diagnostic set |
|-------|--------------------------|
| HC-A | Current, OC/SC flags, latch, timestamps, counters |
| HC-B | Same as HC-A |
| MC-A | Current, PWM feedback **TBD**, OC/inrush flags |
| LC-A | Current recommended; open load for lighting **TBD** |
| LC-B | Fault flags; current optional |
| BD-A | Current, direction state, stall flag **TBD** |

## 5. Service and maintenance diagnostics

In Service Mode (**ADR**), channels shall support:

- Read raw diagnostic snapshot without energizing
- Supervised single-channel test energization with timeout **TBD**
- Manual fault clear audit log entry

## 6. E30 load traceability

Diagnostic records shall include `load_key` and E30LD ID when configured (e.g. `fuel_pump` / E30LD-005) for WP-003 traceability.

## 7. Verification (future)

| Test | Pass criterion |
|------|----------------|
| Simulated open load | Flag set within time **TBD** |
| Simulated overcurrent | De-energize and log within time **TBD** |
| Latch persistence | Survives power cycle **TBD** if required |
| Counter monotonicity | Increments on each event |

## 8. Related documents

- [Power_Channel_State_Model.md](Power_Channel_State_Model.md)
- [Power_Channel_Protection.md](Power_Channel_Protection.md)
- [E30_Gen1_Load_Measurement_Plan.md](../Vehicle_Integration/E30_Gen1_Load_Measurement_Plan.md)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-004 diagnostic requirements |
