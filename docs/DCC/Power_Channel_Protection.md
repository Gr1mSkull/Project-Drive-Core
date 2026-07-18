# DCC Power Channel Protection

**Document ID:** DCC-PWR-PROT-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-004

Protection philosophy and requirements for DCC power channels. **No implementation methods** (no specific TVS, fuse, or PROFET features).

Normative requirements: [Power_Channel_Requirements.md](Power_Channel_Requirements.md) § protection (DC-DCC-PWR-061–080).

---

## 1. Purpose

Document required protection capabilities that every channel class shall satisfy or inherit from the DCC Power Board, independent of component selection.

## 2. Protection principles

1. **Fail-safe OFF** — Protection events shall not leave outputs in an uncontrolled ON state.
2. **Energy limiting** — Short circuits and overcurrent shall limit delivered energy within bounds **TBD** per class.
3. **Layered defence** — Vehicle wiring protection (external fuse **TBD**), channel protection, and board input protection are separate layers.
4. **No silent failure** — Detected faults shall produce diagnostic records.
5. **TBD until measured** — Thresholds derive from WP-003 load measurements and future component datasheets.

## 3. Required protection features

| Feature | Requirement summary | Threshold / method |
|---------|---------------------|-------------------|
| **Reverse polarity tolerance** | DCC input shall tolerate reverse battery connection without damage to Logic; power outputs shall not energize | Magnitude/duration **TBD** |
| **Load dump tolerance** | Shall survive vehicle load dump events on supply | Level/duration **TBD** |
| **Short circuit handling** | Detect and de-energize; optional retry per config | Trip current **TBD**; time **TBD** |
| **Overcurrent detection** | Continuous and peak overcurrent detection per channel | Limits **TBD** per class and load |
| **Thermal shutdown** | Channel or board thermal limit shall force de-energization or derating | Temperature **TBD** |
| **Overvoltage** | Supply overvoltage shall inhibit enable or force safe state | Threshold **TBD** |
| **Undervoltage** | Supply undervoltage shall inhibit enable or derate high-draw channels | Threshold **TBD** (config uses 11.0 V warning for EHPS derate log only today) |
| **Open load detection** | Configurable per channel where load type permits | Detection threshold **TBD** |
| **Supply monitoring** | Battery voltage at DCC input shall be measured for rules and logging | Accuracy **TBD** |
| **Reverse current consideration** | Bidirectional and motor loads may feed energy back; shall not damage channel | BD-A and motor classes — clamp policy **TBD** |
| **Global enable interlock** | Hardware path shall disable all channels independent of firmware | See docs/001 §9 |
| **Kill switch** | Independent of MCU; shall open enable chain | Architecture fixed |
| **Watchdog / comms loss** | Loss of valid control shall de-energize within time **TBD** | SPI timeout **TBD** |

## 4. Protection by channel class

| Class | Additional emphasis |
|-------|---------------------|
| HC-A | Inrush tolerance; sustained overcurrent; thermal priority in GRP-COOLING-HIGH |
| HC-B | Same as HC-A when assigned equivalent load |
| MC-A | Inrush; blocked-rotor / stall policy **ADR**; PWM overcurrent |
| LC-A | ECU hold-up during crank undervoltage **ADR**; lighting open load |
| LC-B | Standard; non-critical shedding candidate |
| BD-A | Shoot-through prevention; reverse current; stall timeout |

## 5. External protection coordination

Per WP-003 load inventory, each load may require external fuse protection — status **TBD**. DCC channel protection shall **not** assume external fuse is present unless configured.

| Layer | Responsibility |
|-------|----------------|
| Vehicle harness fuse | Architect / harness WP — **TBD** |
| DCC channel electronic protection | Channel class requirements |
| DCC input protection | Power Board input — implementation TBD |

## 6. Fault severity classes (abstract)

| Class | Examples | Retry | Latch |
|-------|----------|-------|-------|
| Transient | Brief inrush exceed | Yes | No |
| Persistent overcurrent | Short circuit | Configurable | Yes |
| Open load | Lamp failure | **TBD** | **TBD** |
| Thermal warning | Board hot | Derate **TBD** | **TBD** |
| Thermal critical | Junction limit | No | Yes |
| Supply | UV/OV | Inhibit enable | Until cleared |

Exact classification **TBD** — ARCHITECTURAL DECISION REQUIRED for ECU channel latch.

## 7. Interaction with state machine

| Protection event | Typical state transition |
|------------------|-------------------------|
| Transient OC | Enabled → Fault Detected → Retry Delay |
| Persistent SC | Enabled → Fault Detected → Latched Fault |
| Thermal critical | Enabled → Latched Fault (all affected channels **TBD**) |
| UV inhibit | Ready (cannot → Enabled) |
| Kill active | Any → Disabled |

## 8. E30 simultaneous-load considerations

GRP-COOLING-HIGH and GRP-ENGINE-CRITICAL may overlap in ENGINE_RUN/RACE. Aggregate supply current **TBD**. Protection shall not assume single-channel isolation accounts for battery sag — supply monitoring required.

## 9. Verification (future)

Each protection requirement shall map to a test case when thresholds are defined. Until then, requirements remain specification-only.

## 10. Related documents

- [Power_Channel_State_Model.md](Power_Channel_State_Model.md)
- [Power_Channel_Diagnostics.md](Power_Channel_Diagnostics.md)
- [E30_Gen1_Load_Inventory.md](../Vehicle_Integration/E30_Gen1_Load_Inventory.md)

## 11. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-004 protection philosophy |
