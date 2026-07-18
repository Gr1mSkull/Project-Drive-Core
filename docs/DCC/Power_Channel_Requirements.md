# DCC Power Channel Requirements

**Document ID:** DCC-PWR-REQ-001  
**Version:** 1.0  
**Status:** Proposed · **Normative**  
**Work Package:** WP-004

Implementation-independent requirements for DCC power-output channels. Requirement IDs use prefix **DC-DCC-PWR-**.

Supporting documents: [Power_Channel_Architecture.md](Power_Channel_Architecture.md), [Power_Channel_Classes.md](Power_Channel_Classes.md), [Power_Channel_State_Model.md](Power_Channel_State_Model.md), [Power_Channel_Protection.md](Power_Channel_Protection.md), [Power_Channel_Diagnostics.md](Power_Channel_Diagnostics.md).

---

## 1. Architecture requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-001** | The DCC SHALL model each power output as an engineering channel class (HC-A, HC-B, MC-A, LC-A, LC-B, or BD-A) independent of semiconductor part numbers. |
| **DC-DCC-PWR-002** | Each physical channel index SHALL be assigned exactly one engineering class for a given Power Board hardware revision. |
| **DC-DCC-PWR-003** | The DCC SHALL de-energize all power channels when the global enable interlock is inactive or the kill input is asserted. |
| **DC-DCC-PWR-004** | The DCC SHALL bind logical vehicle outputs to physical channel indices only through validated configuration (YAML/DCFG), not hardcoded firmware assignment. |
| **DC-DCC-PWR-005** | Channel class capabilities SHALL be documented before any smart switch or driver component is selected for qualification. |
| **DC-DCC-PWR-006** | Electrical current and voltage limits for channel classes SHALL remain TBD until supported by measured load data or qualified component evidence. |
| **DC-DCC-PWR-007** | The DCC SHALL support at least twenty-two unidirectional high-side logical channels and two bidirectional bridge logical channels in Gen1 hardware capacity mapping. |
| **DC-DCC-PWR-008** | Channel requirements SHALL be traceable to E30 load records (E30LD-XXX) where a load is assigned. |
| **DC-DCC-PWR-009** | The DCC SHALL NOT enter production BOM without qualification records per [COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md). |
| **DC-DCC-PWR-010** | Power channel behaviour SHALL be configurable per output without firmware rebuild. |

## 2. Channel class requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-011** | Class HC-A SHALL support assignment of the highest-tier vehicle loads identified as critical high-draw in the load inventory. |
| **DC-DCC-PWR-012** | Class HC-B SHALL provide equivalent capability tier to HC-A for reserve or alternate high-draw assignment. |
| **DC-DCC-PWR-013** | Class MC-A SHALL support PWM-controlled motor loads and intermittent motor loads per configuration. |
| **DC-DCC-PWR-014** | Class LC-A SHALL support ECU supply, lighting, and standard cabin motor loads. |
| **DC-DCC-PWR-015** | Class LC-B SHALL support auxiliary lighting, wiper, and low-duty accessory loads. |
| **DC-DCC-PWR-016** | Class BD-A SHALL support bidirectional motor control with distinct forward, reverse, and off commands. |
| **DC-DCC-PWR-017** | Each channel class SHALL define a safe state of de-energized output unless ARCHITECTURAL DECISION REQUIRED is explicitly documented. |
| **DC-DCC-PWR-018** | PWM-capable classes SHALL accept duty commands from configuration or rules engine without channel-specific firmware branches. |
| **DC-DCC-PWR-019** | HC-A and HC-B channels SHALL provide current observation suitable for overcurrent detection before latch. |
| **DC-DCC-PWR-020** | BD-A channels SHALL prevent overlapping forward and reverse enable commands. |

## 3. Switching and operation requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-021** | A channel SHALL energize only when VCM mode, configuration, interlocks, and channel state collectively permit enable. |
| **DC-DCC-PWR-022** | A channel SHALL de-energize when commanded off, when VCM transitions require off per `outputs.*.modes`, or when a protection event occurs. |
| **DC-DCC-PWR-023** | Continuous operation limits SHALL be defined per assigned load after measurement; until then values SHALL be TBD. |
| **DC-DCC-PWR-024** | Intermittent and inrush operation limits SHALL be defined per assigned load after measurement; until then values SHALL be TBD. |
| **DC-DCC-PWR-025** | Simultaneous energization of channels in the same WP-003 simultaneous-operation group SHALL be evaluated for aggregate supply impact before production approval. |
| **DC-DCC-PWR-026** | Retry count per channel SHALL be configurable via vehicle configuration. |
| **DC-DCC-PWR-027** | After configured retries are exhausted, the channel SHALL enter Latched Fault state. |
| **DC-DCC-PWR-028** | Degraded DCC behaviour for non-critical channels SHALL follow architect-approved policy; until approved, behaviour SHALL be ARCHITECTURAL DECISION REQUIRED. |
| **DC-DCC-PWR-029** | Fuel prime and other timed behaviours SHALL use configuration-defined modes (e.g. `prime`) without hardcoded dwell times in channel drivers until architect defines timing. |
| **DC-DCC-PWR-030** | AUTO mode channels SHALL reflect rules engine and ECU telemetry without requiring manual enable per event. |

## 4. State machine requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-041** | Each channel SHALL implement the states defined in [Power_Channel_State_Model.md](Power_Channel_State_Model.md). |
| **DC-DCC-PWR-042** | A channel in Unknown state SHALL NOT energize until transitioned to Ready. |
| **DC-DCC-PWR-043** | Transition from Disabled to Enabled SHALL pass through Ready. |
| **DC-DCC-PWR-044** | Transition from Latched Fault to Enabled SHALL NOT occur without passing through Ready or authorized Service Mode. |
| **DC-DCC-PWR-045** | Fault Detected state SHALL de-energize the channel output. |
| **DC-DCC-PWR-046** | Retry Delay duration SHALL be configurable or documented as TBD until timing studies complete. |
| **DC-DCC-PWR-047** | Service Mode entry and exit conditions SHALL be ARCHITECTURAL DECISION REQUIRED until defined. |
| **DC-DCC-PWR-048** | Global kill event SHALL force all channels out of Enabled within time TBD. |
| **DC-DCC-PWR-049** | Loss of valid control communication SHALL force fail-safe de-energization within time TBD. |
| **DC-DCC-PWR-050** | State transitions SHALL be deterministic for a given fault and configuration input sequence. |

## 5. Logging requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-051** | Each transition to Fault Detected, Latched Fault, or Latched Fault cleared SHALL generate an event log entry. |
| **DC-DCC-PWR-052** | Event log entries SHALL include channel index and configured load key when present. |
| **DC-DCC-PWR-053** | Retry attempts SHALL be logged with attempt number and fault cause category TBD. |
| **DC-DCC-PWR-054** | PWM duty changes MAY be logged at configurable verbosity; fault events SHALL always be logged. |
| **DC-DCC-PWR-055** | State transition timestamps SHALL use a monotonic or UTC time base with resolution TBD. |

## 6. Protection requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-061** | The DCC power path SHALL tolerate vehicle reverse polarity events without catastrophic damage; magnitude TBD. |
| **DC-DCC-PWR-062** | The DCC power path SHALL tolerate load dump events; level TBD. |
| **DC-DCC-PWR-063** | Each channel SHALL detect overcurrent above configured limit TBD and de-energize. |
| **DC-DCC-PWR-064** | Each channel SHALL detect short circuit conditions per class policy and de-energize. |
| **DC-DCC-PWR-065** | Thermal limits SHALL cause de-energization or derating per architect policy TBD. |
| **DC-DCC-PWR-066** | Supply overvoltage SHALL inhibit new enable commands until voltage returns to acceptable range TBD. |
| **DC-DCC-PWR-067** | Supply undervoltage SHALL inhibit or derate enable per channel class policy TBD. |
| **DC-DCC-PWR-068** | Open load detection SHALL be configurable per channel where load type supports detection; default TBD. |
| **DC-DCC-PWR-069** | Battery supply voltage at DCC input SHALL be monitored for rules and diagnostics. |
| **DC-DCC-PWR-070** | BD-A channels SHALL account for reverse current from motor regeneration without damage; clamp TBD. |
| **DC-DCC-PWR-071** | Protection events SHALL NOT leave outputs in an uncontrolled ON state. |
| **DC-DCC-PWR-072** | External fuse presence SHALL be configurable per load; DCC SHALL NOT assume harness fuse without configuration. |

## 7. Diagnostic requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-081** | Each channel SHALL expose its current state from the defined state machine. |
| **DC-DCC-PWR-082** | Each channel SHALL expose a fault flag set covering at minimum overcurrent, short circuit, open load, thermal, supply, and latched conditions. |
| **DC-DCC-PWR-083** | Fault events SHALL record a timestamp of first occurrence for latched faults. |
| **DC-DCC-PWR-084** | Diagnostic data SHALL be readable without energizing the channel in normal operation. |
| **DC-DCC-PWR-085** | Per-channel diagnostic counters (enable, fault, retry, latch) SHALL be maintained. |
| **DC-DCC-PWR-086** | HC-A, HC-B, MC-A, and BD-A channels SHALL provide load current measurement for diagnostics; accuracy TBD. |
| **DC-DCC-PWR-087** | Health reporting SHALL integrate with the DCC event log defined in configuration model documentation. |
| **DC-DCC-PWR-088** | Diagnostic records SHALL remain available when Service layer is offline. |
| **DC-DCC-PWR-089** | Simulated fault injection for test SHALL be supported in Service Mode when architect approves procedure TBD. |
| **DC-DCC-PWR-090** | Open load diagnostic SHALL be suppressible during known bulb-out tolerant operation only if architect approves TBD. |

## 8. Configuration requirements

| ID | Requirement |
|----|-------------|
| **DC-DCC-PWR-101** | Each output configuration SHALL declare channel index, output type (`high_side`, `pwm`, `hbridge`), and mode table. |
| **DC-DCC-PWR-102** | Each output configuration SHALL declare retry count as a non-negative integer. |
| **DC-DCC-PWR-103** | Current limit fields in configuration SHALL be nullable or TBD until load measurement populates values. |
| **DC-DCC-PWR-104** | Configuration validation SHALL reject binding a load to a channel index outside hardware capacity. |
| **DC-DCC-PWR-105** | Configuration validation SHALL reject PWM type on channels without PWM capability TBD mapping. |
| **DC-DCC-PWR-106** | Channel class metadata SHALL be available to the validator separately from vehicle YAML until schema version TBD merges load inventory. |
| **DC-DCC-PWR-107** | Changing configuration SHALL NOT reset latched faults without explicit clear action TBD. |
| **DC-DCC-PWR-108** | DevKit and vehicle profiles MAY declare different channel counts while using the same state and protection model. |

## 9. Verification traceability

| Requirement ID | Verification method (when thresholds defined) |
|----------------|-----------------------------------------------|
| DC-DCC-PWR-003 | Kill switch bench test |
| DC-DCC-PWR-027 | Fault injection with retry exhaustion |
| DC-DCC-PWR-042 | Power-on state observation |
| DC-DCC-PWR-063–064 | Overcurrent / short bench test per load |
| DC-DCC-PWR-081–087 | DCPI diag read / event log inspection |

Until thresholds are TBD-resolved, requirements are verified by inspection of design documentation and peer review.

## 10. Requirement index

Total normative requirements: **75** (DC-DCC-PWR-001–010, 011–020, 021–030, 041–055, 061–072, 081–090, 101–108).

## 11. Related documents

- [docs/SRS/Volume_2_DCC.md](../SRS/Volume_2_DCC.md) — future REQ migration target
- [config/vehicles/e30_gen1_loads.yaml](../../config/vehicles/e30_gen1_loads.yaml)
- [config/vehicles/e30_gen1.yaml](../../config/vehicles/e30_gen1.yaml) — unchanged by WP-004

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-004 initial requirement set |
