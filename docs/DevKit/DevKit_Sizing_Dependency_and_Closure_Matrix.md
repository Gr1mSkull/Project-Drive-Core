# DevKit Sizing Dependency and Closure Matrix — WP-012

**Document ID:** DOC-DK-SDCM-001  
**Version:** 1.3  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20

Closure disposition for sizing parameters. Register Status for TBD-DK-* remains **Open** unless explicitly noted — **not Resolved**.

## 1. Matrix

| Parameter / issue | Source | Current status | Sizing method | Missing input | Architecture dependency | Component dependency | Schematic dependency | PCB dependency | Fixture dependency | Measurement dependency | Blocks | Recommended next WP |
|-------------------|--------|----------------|---------------|---------------|-------------------------|----------------------|----------------------|----------------|--------------------|-----------------------|--------|----------------------|
| **TBD-DK-001** input voltage | Register | Open | Envelope + UV/OV table | V_IN min/max | OI-VIN-001 | RP/TVS class | Entry schematic | — | PSU characterization | DK-C-012 | UV cases; sizing | Sizing + Architect |
| **TBD-DK-002** certified base current | Register | Open | Limit stack min() | All L2–L13 terms | ADR-021 | HS/BI class; connector | Entry + distribution | Copper thermal | Fixture cont | P3 continuous trace | Component qual; schematic | Sizing + measurement |
| **TBD-DK-003** simultaneous envelope | Register | Open | Profile peak/avg/RMS | Overlap profiles | WP-009 overlap model | Per-channel limits | Channel map | Thermal coupling | P4 loads | P4 simultaneous | Multi-load DK-C | Sizing + P4 meas |
| **TBD-DK-004** KILL response | Register | Open | T-Class H budget | KILL path netlist | ADR-022; OI-KILL-001 | Enable chain class | KILL schematic | — | Scope trigger | DK-A kill cases | Timing PASS | FW BSP + meas |
| **TBD-DK-005** watchdog response | Register | Open | T-Class R budget | WDT period/handler | ADR-022 | Logic MCU | FW design | — | — | FW + meas | Timing PASS | FW BSP WP |
| **TBD-DK-007** control-loss | Register | Open; **BLOCKED_BY_EDL_CLARIFICATION** | T-Class C budget | Numeric ms; detection split | WP-011 Option D semantics | Power controller fail-safe | Power-side HW | — | Comm-loss fixture | DK-A-008, C-012 | Numeric timing | Measurement + optional EDL CR |
| **TBD-DK-008** PWM frequency | Register | Open | Loss + EMI model | f_PWM range | — | Switch PWM cap | Gate drive | — | PWM load | DK-C-003 | PWM verification | Component qual |
| **TBD-DK-009** sense accuracy | Register | Open | Error budget | Calibration proc | OI-SENSE-001 | Sense class | Sense topology | Shunt layout | Cal fixture | DK-C-004 | Sense verification | Qualification WP |
| **TBD-DK-010** thermal observation | Register | Open | Sensor error budget | Sensor class | ADR-DK-011 | Temp sensor | Routing | — | — | DK-C thermal | Thermal cases | Qualification WP |
| **TBD-DK-011** fault injection | Register | Open | E_FAULT methodology | Injection fixture | ADR-023 | SC withstand | Protection nets | Copper I²t | SC fixture | DK-C SC | SC verification | Fixture WP |
| **TBD-DK-012** UV reaction | Register | Open | UV state table | Thresholds + hysteresis | OI-UV-001/002 | UV monitor | Input chain | — | PSU ramp | DK-C-012 | UV verification | Architect + sizing |
| **TBD-DK-013** retry/latch | Register | Open | Thermal accumulation check | Policy table | — | Switch latch behaviour | Channel ctrl | — | Fault repeat | DK-C-008 | Retry cases | Architect + FW |
| **TBD-DK-014** commanded OFF | Register | Open | OFF budget | SW/HW path delay | ADR-022 | Switch OFF time | Output stage | — | Load monitor | DK-A/C | OFF timing | FW BSP + meas |
| **TBD-DK-017** rail tolerances | Register | Open | Load/regulation budget | Rail loads | OI-RAIL-001 | Regulators | Power schematic | — | DMM/load | DK-A rails | Rail tests | Sizing WP |
| **TBD-DK-018** thermal duration | Register | Open | Soak time model | t_thermal_test | ADR-DK-011 | — | — | Thermal mass | Chamber | DK-C thermal | Thermal PASS | ADR-DK-011 |
| **TBD-DK-019** max safe temperature | Register | Open | Derating curve | T_max | ADR-DK-011 | Junction limits | — | Copper | IR/chamber | Thermal qual | Thermal freeze | ADR-DK-011 |
| **TBD-DK-022** BI stall | Register | Open | Stall I × duration | Fixture boundary | ADR-019 | BI class | Bridge topology | — | Stall fixture | DK-C-011 | Stall test | Fixture WP |
| **ADR-DK-011** thermal/environment | Request | Open | Test split definition | T_amb classes | Architect decision | Qual scope | — | Enclosure | Chamber policy | All thermal | Qualification scope | Architect ADR |
| **ADR-DK-012** connector/enclosure | Request | Open | Entry/distribution class | Connector family | Architect decision | Connector qual | Symbol placement | Mechanical | — | — | Schematic auth | Architect ADR |
| **OI-GND-001** external GND | OI register | Open | Isolation model | GND option selection | ADR-020/021 | — | Isolation devices | — | Fixture GND | Fixture qual | P6 safety | Fixture + Architect |
| **OI-CHAN-001** channel population | OI register | Open | Alias→instance map | Physical count | WP-010-R1 | Channel count | Schematic | Layout | — | Per-channel DK-C | Schematic | Schematic WP |
| **OI-COMP-001** HS evaluation class | OI register | Open | Class comparison | ED-IN-002/026/030 | ADR-019 | HS class qual | — | — | — | — | Schematic | Component qual WP |
| **OI-COMP-002** BI evaluation class | OI register | Open | Class comparison | ED-IN-031; TBD-DK-022 | ADR-019 | BI class qual | — | — | Stall fixture | DK-C-011 | Schematic | Component qual WP |
| **OI-PROT-001** reverse polarity | OI register | Open | RP architecture study | Method selection | Architect | RP device class | Input schematic | — | RP test | DK-A entry | Input protection | Architect + qual |
| **OI-PROT-002** transient protection | OI register | Open | Clamp energy study | Clamp class | — | TVS/clamp qual | Input schematic | — | Injection | Transient test | Input survival | Component qual |

## 2. Evaluation-class readiness

| Evaluation function | Minimum required inputs | Inputs currently available | Missing inputs | Qualification readiness |
|---------------------|-------------------------|----------------------------|----------------|-------------------------|
| High-side switching | ADR-019 caps; symbolic I_CHANNEL; thermal method; protection philosophy | Capability map; WP-011 classes; budget equations | I_certified_cont; T_max; f_PWM; class direction | **PARTIAL** |
| Bidirectional switching | BI caps; stall fixture boundary; shoot-through method | ADR-019; OI-BI-001; classes | TBD-DK-022; topology; I_CHANNEL | **NOT_READY** |
| Current observation | Accuracy target; topology; calibration | TBD-DK-009 Open; sense classes | Sense class selection; shunt/layout | **NOT_READY** |
| Input reverse-polarity protection | RP architecture decision | OI-PROT-001 Open | Architect method | **BLOCKED** |
| Input transient protection | Clamp architecture; energy | OI-PROT-002 Open | Device class; V_IN envelope | **BLOCKED** |
| Rail conversion | Rail loads; efficiency | OI-RAIL-001; symbolic P_CONV | Regulator selection; I_LOGIC/RADIO peaks | **NOT_READY** |
| Input replaceable protection | I_protection vs I_certified distinction | ADR-021; WP-009 L4 | Numeric ratings; fuse class | **NOT_READY** |
| Controller interface (J_LP) | Fail-safe mechanism; SPI model | WP-010; WP-011 CTRL classes | TBD-DK-007 numeric; Power-side HW | **PARTIAL** |
| KILL / global-enable | Direct KILL branch; default OFF | ADR-022; PWR-A-004/005 | OI-KILL-001 detail; timing | **PARTIAL** |

Readiness legend: **READY_FOR_CLASS_COMPARISON** · **PARTIAL** · **NOT_READY** · **BLOCKED**

## 3. Sizing method reference (WP-012)

| Document | Methods provided |
|----------|------------------|
| [`DevKit_Electrical_Sizing_Framework.md`](DevKit_Electrical_Sizing_Framework.md) | Lifecycle; domains; readiness states |
| [`DevKit_Current_and_Power_Budget_Model.md`](DevKit_Current_and_Power_Budget_Model.md) | I/P quantities; P0–P6; equations |
| [`DevKit_Thermal_Sizing_Framework.md`](DevKit_Thermal_Sizing_Framework.md) | Thermal path; states; R_th rules |
| [`DevKit_Protection_Coordination_Framework.md`](DevKit_Protection_Coordination_Framework.md) | P0–P5; faults; E_FAULT |
| [`DevKit_Power_Path_Assumption_Register.md`](DevKit_Power_Path_Assumption_Register.md) | PWR-A-* constraints |

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial sizing dependency and closure matrix — Proposed |
| 1.1 | 2026-07-20 | WP-012-R1 — cross-ref staged closure model |
| 1.3 | 2026-07-20 | Architecture Review Accepted — PR #16 merged (`9c5c7e7` / `fe700d4`); TBD-DK-007 BLOCKED unchanged |
