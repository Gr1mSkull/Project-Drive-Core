# DevKit Functional Electrical Architecture — WP-010

**Document ID:** DOC-DK-FEA-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer

```text
Functional architecture — not a schematic.
No numeric current or timing limits are Approved by this document.
No component MPNs, connector pins, fuse ratings, or PCB sizing are defined.
```

## 1. Purpose and scope

This document converts Accepted WP-007 requirements, Accepted ADR-016…023, and Accepted WP-009 analytical methods into a reviewable **functional electrical architecture** for the DriveCore Gen1 DevKit.

**In scope:** functional domains; board and fixture boundaries; energy, control, service, safety, and measurement views; representative channel allocation; symbolic parameters; downstream sizing inputs; fault-containment analysis.

**Out of scope:** schematics; PCB; BOM; wiring pinouts; firmware; fixtures; numeric threshold approval; component selection; EDL-011 resolution.

**Authoritative inputs:** Engineering Constitution; EDL-001, 007, 011, 014; ADR-016…023; WP-007/008/009 Accepted artifacts; `docs/002`, `docs/DCC/*`; `config/vehicles/devkit.yaml` (logical map only — candidate values non-normative).

## 2. Architecture principles

| # | Rule | Source |
|---|------|--------|
| 1 | Logic owns Real-Time and safety-relevant output execution | ADR-016; constitution |
| 2 | Radio cannot directly energize power outputs | ADR-017; REQ-DCC-V-DK-037 |
| 3 | Hardware KILL independent of Radio and Tablet | ADR-022; REQ-DCC-V-DK-033 |
| 4 | `nENABLE_GLOBAL` defaults inactive during Logic reset/unpowered | ADR-022; REQ-DCC-V-DK-034 |
| 5 | Control-loss → Power-side fail-safe OFF | EDL-011; ADR-022; REQ-DCC-V-DK-035 |
| 6 | External high-energy path separated from base envelope | ADR-020/021; WP-009 P6 |
| 7 | Base DevKit does not inherit external-bank ratings | ADR-021 |
| 8 | All represented capabilities independently testable | ADR-019 |
| 9 | Open-load conditional on future implementation claim | ADR-019 |
| 10 | Pre-kill commands cannot replay after kill release | ADR-022; TBD-DK-021 |
| 11 | Numeric thresholds remain Open unless Accepted elsewhere | WP-009 |
| 12 | Phase E production hardware separately verified | EDL-014; ADR-020 |

## 3. Board decomposition (staged fidelity)

Per ADR-016…019 Option D staged model; **DK-A…DK-D gate evidence requires Option B minimum** on each board class.

### 3.1 Logic board (Real-Time domain)

| Attribute | Functional definition |
|-----------|----------------------|
| **Processor class** | STM32G474-class per EDL-001 |
| **Responsibilities** | VSM; rule execution; CAN; J_LP master; DCPI RT endpoint; hardware kill observation/propagation; `nENABLE_GLOBAL` control; watchdog; BOARD_ID read; channel command scheduling |
| **Interfaces** | J_LP (IF-DK-JLP); DCPI (IF-DK-DCPI); CAN (IF-DK-CAN); debug (IF-DK-DEBUG-LOGIC); kill input (IF-DK-KILL) |
| **Safe state** | Outputs disabled via withdrawn `nENABLE_GLOBAL`; kill path asserted when applicable |
| **Not authorized** | Exact package; dev-board MPN; pin-level schematic |

### 3.2 Radio board (Service domain)

| Attribute | Functional definition |
|-----------|----------------------|
| **Processor class** | ESP32-class Service implementation |
| **Responsibilities** | DCPI Service endpoint; Wi-Fi/REST/WebSocket; configuration transfer; telemetry; heartbeat — **no power output authority** |
| **Interfaces** | DCPI (IF-DK-DCPI); debug (IF-DK-DEBUG-RADIO); expansion header (production J_EXP intent) |
| **Safe state** | Service loss does not de-energize RT outputs (fail-operational) |
| **Not authorized** | Radio module MPN; antenna/EMC design |

### 3.3 Power board (representative power domain)

| Attribute | Functional definition |
|-----------|----------------------|
| **Responsibilities** | Input distribution; channel switching (HS, PWM, BI); local protection; current sense aggregation; fault reporting; J_LP slave; BOARD_ID; control-loss fail-safe |
| **Interfaces** | J_LP; base load (IF-DK-BASE-LOAD); bidirectional load (IF-DK-BIDIRECTIONAL-LOAD); measurement (IF-DK-MEASUREMENT) |
| **Replaceability** | Power board replaceable without redesigning Logic/Radio external contracts (REQ-DCC-V-DK-113) |
| **Not authorized** | Final channel population; switch MPN; copper sizing |

### 3.4 Fixture boundary (external)

| Attribute | Functional definition |
|-----------|----------------------|
| **Responsibilities** | External high-energy source/load-bank interface; fixture protection; E-stop; energy supervision; measurement boundary |
| **Separation** | Electrical, control, and evidence scope separate from base DevKit envelope (ADR-020) |
| **Not authorized** | Fixture schematic or build |

## 4. Functional electrical domains

Companion detail: [`DevKit_Power_Domain_Matrix.md`](DevKit_Power_Domain_Matrix.md), [`DevKit_Safe_State_Path_Matrix.md`](DevKit_Safe_State_Path_Matrix.md), [`DevKit_Functional_Block_Diagram.md`](DevKit_Functional_Block_Diagram.md).

| Domain ID | Purpose | Authority | Safe state | Main interfaces |
|-----------|---------|-----------|------------|-----------------|
| **DOM-LAB-SUPPLY** | Controlled bench energy source | Operator / lab PSU | OFF when disconnected | IF-DK-POWER-IN |
| **DOM-INPUT-PROTECT** | Replaceable input OCP; entry protection boundary | Hardware + operator replacement | Open circuit on trip | IF-DK-POWER-IN |
| **DOM-INPUT-DIST** | Distribution from entry to board domains | Power board | De-energized when upstream removed | Internal to Power |
| **DOM-LOGIC-PWR** | Logic rail generation | Logic board local regulation | OFF when `V_IN` absent or UV | MP-LOGIC-RAIL |
| **DOM-PWR-CTRL** | Power controller and driver logic | Power board + J_LP commands | All channels OFF | IF-DK-JLP |
| **DOM-RADIO** | Service processor domain | Radio board | Service unavailable; RT continues | IF-DK-DCPI |
| **DOM-HS-REP** | Representative high-side channels | Logic command → Power execution | Channel OFF | IF-DK-BASE-LOAD |
| **DOM-BI-REP** | Representative bidirectional channel | Logic command → Power execution | Both directions OFF | IF-DK-BIDIRECTIONAL-LOAD |
| **DOM-SENSE-DIAG** | Current, voltage, temperature, fault aggregation | Power sense + Logic diagnostics | Observability only | IF-DK-MEASUREMENT |
| **DOM-HW-KILL** | Hardware emergency disable path | External kill + conditioning | Outputs disabled | IF-DK-KILL |
| **DOM-GLOBAL-EN** | Logic-controlled global output enable | Logic RT | Inactive (safe) default | IF-DK-JLP |
| **DOM-EXT-BANK** | External high-energy path | Fixture operator + supervision | De-energized; no back-feed | IF-DK-EXTERNAL-BANK |
| **DOM-BENCH-LOAD** | On-board representative loads | Test operator | OFF when channel OFF | IF-DK-BASE-LOAD |
| **DOM-PROG-DEBUG** | SWD / programming | Developer | No effect on output safe state | IF-DK-DEBUG-* |
| **DOM-CAN** | Vehicle-bus representative interface | Logic RT | Bus loss ≠ power kill | IF-DK-CAN |
| **DOM-DCPI** | Logic↔Radio binary service link | Logic RT + Radio Service | Service loss isolated | IF-DK-DCPI |
| **DOM-MEASURE** | Test and trigger observation | Verification operator | N/A | IF-DK-MEASUREMENT |
| **DOM-FIXTURE-CTL** | External fixture control boundary | Fixture controller | E-stop → energy removal | IF-DK-EXTERNAL-BANK |

For each domain: enable condition, shutdown condition, upstream/downstream dependencies, fault containment, diagnostic observability, and measurement points are defined in the companion matrices and §§5–10 below.

## 5. View A — Energy flow

### 5.1 Base DevKit path

```text
Lab PSU (I_PSU_limit)
  → source-side current limiting (operator set)
  → replaceable input protection (I_protection_rating ≠ I_certified_cont)
  → DevKit input entry (IF-DK-POWER-IN)
  → input distribution (DOM-INPUT-DIST)
  → Logic rail (V_LOGIC) + Radio rail (V_RADIO) + Power control (V_POWER_CTRL)
  → representative HS channel (CH-HS-*)
  → bench load terminal (IF-DK-BASE-LOAD)
  → bench load / test load (I_CHANNEL_CONT within I_certified_cont)
```

**Symbolic constraints (Open numerics):**

```text
I_certified_cont = min(L1…L13 per WP-009 limit stack)
I_BASE_CONT ≤ I_certified_cont
I_PROFILE_PEAK ≤ I_fault_peak (protection layer)
```

Architecture valid only if future calculated `I_certified_cont` satisfies Scenario C2 pattern (WP-009) without exceeding any non-collapsed limit layer.

### 5.2 External high-energy path

```text
External high-energy source / load-bank
  → separate fixture protection (I_loadbank_limit)
  → external representative module or controlled load interface
  → measurement boundary (DOM-MEASURE)
  → abort / fixture E-stop
```

**Rules:**

- External path shall **not** silently back-feed base DevKit input distribution (ADR-020/021).
- `I_loadbank_limit` does **not** increase `I_certified_cont`.
- Energization requires explicit fixture enable authority and procedural supervision (ADR-023).
- Ground/isolation relationship: **Open decision** — see §10 and [`DevKit_Electrical_Architecture_Open_Issues.md`](DevKit_Electrical_Architecture_Open_Issues.md) OI-GND-001.

## 6. View B — Control flow

```text
Logic (RT)
  → J_LP SPI command + PWM + nENABLE_GLOBAL + nKILL_HW observation
  → Power control domain (DOM-PWR-CTRL)
  → channel switching function (CH-HS-* / CH-BI-REP)
  → output function
```

| Control element | Function | Safe default |
|-----------------|----------|--------------|
| SPI command transport | Channel ON/OFF, PWM duty, configuration | Invalid/stale → rejected or ignored |
| Command-valid / epoch | Pre-kill command invalidation | Post-kill: stale commands blocked (TBD-DK-021) |
| PWM paths | Timer-driven switching | OFF when enable withdrawn |
| `nENABLE_GLOBAL` | Global AND in enable chain | **Inactive (LOW)** = outputs disabled |
| `nKILL_HW` | Hardware emergency AND | Asserted = outputs disabled regardless of SW |
| Fault feedback | `FAULT_N`, sense data via J_LP | Observable by Logic; triggers protection |
| BOARD_ID | Power revision identity | Invalid ID → safe degraded behaviour |

**Control-loss:** Last valid J_LP frame → Power-side timeout → fail-safe OFF. Numeric `T_CTRL_LOSS_MAX` = TBD-DK-007 — **BLOCKED_BY_EDL_CLARIFICATION**. EDL-011 file unchanged; no interpretation selected.

## 7. View C — Service flow

```text
Radio (Service) ↔ DCPI ↔ Logic (RT)
Tablet / REST / WebSocket ↔ Radio only
```

| Event | RT power execution | Service availability |
|-------|-------------------|---------------------|
| Radio unpowered | Continues per fail-operational rules | Unavailable |
| Radio reset loop | Continues | Degraded telemetry |
| Tablet disconnect | Continues | UI unavailable |
| DCPI CRC/loss | RT continues; diagnostics degraded | Reconnect required |

Service shall not be the sole path for kill, global enable, or channel energization (REQ-DCC-V-DK-037).

## 8. View D — Safety flow (independent paths)

Each path is **distinct** — not collapsed into one shutdown block.

| Path ID | Trigger | Mechanism class | Expected result | Timing symbol |
|---------|---------|-----------------|-----------------|---------------|
| **SS-KILL** | Physical KILL asserted | Hardware-effective | All outputs OFF | `T_KILL_MAX` (TBD-DK-004) |
| **SS-GEN-DIS** | `nENABLE_GLOBAL` removed | Hardware-effective | All outputs OFF | Part of kill/global chain |
| **SS-WD** | Logic watchdog expires | RT → global disable | All outputs OFF | `T_WD_MAX` (TBD-DK-005) |
| **SS-CTRL-LOSS** | J_LP communication lost | Power fail-safe | All outputs OFF | `T_CTRL_LOSS_MAX` (TBD-DK-007) |
| **SS-LOCAL-OC** | Channel overcurrent | Local protection | Affected channel OFF | Component-dependent |
| **SS-LOCAL-SC** | Short circuit | Local protection + fuse layer | Channel/system OFF | `T_SC_*` Open |
| **SS-INPUT-UV** | Input undervoltage | Input monitor | Controlled shutdown | TBD-DK-001/012 |
| **SS-INPUT-INT** | Input protection open / supply removed | Energy removal | All outputs OFF | Immediate |
| **SS-FIX-ESTOP** | Fixture E-stop | Fixture energy removal | External path OFF | Immediate |
| **SS-CMD-OFF** | Valid OFF command | Firmware-requested | Channel OFF | `T_CMD_OFF_MAX` (TBD-DK-014) |

**Distinction:**

```text
hardware-effective OFF     → KILL, nENABLE_GLOBAL removal, control-loss fail-safe, input energy removal
firmware-requested OFF     → commanded OFF, diagnostic disable
local channel protection   → OC/SC/thermal per channel
observability-only fault   → logged; may not de-energize if fail-operational applies
```

Post-kill re-enable FSM per WP-009 / TBD-DK-021 — no auto-restore; operator ack required.

## 9. View E — Measurement flow

Measurement supports WP-009 [`DevKit_Threshold_Measurement_Plan.md`](DevKit_Threshold_Measurement_Plan.md). Full register: [`DevKit_Measurement_Point_Register.md`](DevKit_Measurement_Point_Register.md).

| Flow | Points | Purpose |
|------|--------|---------|
| Input energy | MP-IN-V, MP-IN-I | Envelope certification; UV behaviour |
| Kill chain | MP-KILL-RAW, MP-KILL-COND, MP-GLOBAL-ENABLE | TBD-DK-004 timing |
| J_LP | MP-JLP-CMD, MP-JLP-FAULT | Control-loss; fault visibility |
| Channel | MP-CH-HS-VOUT, MP-CH-HS-IOUT, MP-CH-BI-* | TBD-DK-009; OC/SC |
| Rails | MP-LOGIC-RAIL, MP-RADIO-RAIL, MP-POWER-CTRL-RAIL | TBD-DK-017 |
| Returns | MP-LOAD-BASE-RETURN, MP-LOAD-EXT-RETURN | Ground loop analysis |

Timestamp source: bench instrument + Logic diagnostic timestamp correlation (future FW WP). Isolation boundary at fixture interface — **Open** for differential requirements.

## 10. Grounding and reference architecture

Functional reference domains (no copper geometry):

| Reference | Relation to others | Classification |
|-----------|---------------------|----------------|
| **LOGIC_GND** | Common with RADIO_GND at single controlled point | single-point connected (intended) |
| **RADIO_GND** | See LOGIC_GND | single-point connected |
| **POWER_CTRL_GND** | High-current return path to input | directly common with BASE_LOAD_RETURN at Power board |
| **BASE_LOAD_RETURN** | On-board load current return | directly common with POWER_CTRL_GND |
| **EXTERNAL_LOAD_RETURN** | External bank return | **Open decision** vs BASE — see OI-GND-001 |
| **MEASUREMENT_REFERENCE** | Instrument reference | fixture-defined for external path |
| **SHIELD / CHASSIS_REFERENCE** | Enclosure bonding | **Open decision** — ADR-DK-012 |

Addressed risks: measurement ground loops (MP placement); high-current return separation; Logic/Radio noise coupling; external bank back-feed; CAN reference; differential sense needs.

## 11. Input protection functional chain

| Layer | Protected failure | Authority | Expected reaction | Downstream WP |
|-------|-------------------|-----------|-------------------|---------------|
| L1 Source-side limit | PSU overload | Operator | Current foldback / trip | Lab procedure |
| L2 Replaceable protection | Overcurrent, some SC | Fuse/device (TBD) | Open circuit; replace to reset | Sizing WP |
| L3 Reverse-polarity | Wrong connection | Hardware (method Open) | Block or protect | Component WP |
| L4 Transient protection | Surge | Hardware (method Open) | Clamp / absorb | Component WP |
| L5 Input disconnect | Emergency | Operator / fixture | Energy removal | Fixture WP |
| L6 Distribution | Internal fault | Power board design | Localize; report | Schematic WP |
| L7 Rail generation | Regulator fault | Local regulation | UV/OV behaviour | Schematic WP |
| L8 Local channel protection | OC/SC | Channel switch + sense | Channel OFF / latch | Qualification WP |
| L9 Fixture protection | External HC fault | Fixture | E-stop; fuse | Fixture WP |

No fuse type, TVS, RP device, relay, conductor, connector, or rating selected.

## 12. J_LP functional contract

Per EDL-011 and `docs/002` §9 (functional — no pin numbers in this architecture):

| Signal class | Direction | Function |
|--------------|-----------|----------|
| SPI (SCK/MOSI/MISO/CS) | Logic → Power | Command transport; configuration |
| `nKILL_HW` | Logic ↔ Power | Hardware kill net (active safe) |
| `nENABLE_GLOBAL` | Logic → Power | Global output enable |
| `FAULT_N` | Power → Logic | Aggregate fault indication |
| PWM0–3 | Logic → Power | PWM control to channels |
| ISENSE + MUX | Power → Logic | Multiplexed current sense |
| VBATT_SENSE, TEMP | Power → Logic | Input and thermal observation |
| BOARD_ID | Power → Logic | Revision identity |
| `nRESET_PWR` | Logic → Power | Power controller reset |

**Disconnect behaviour:** J_LP removal → control-loss fail-safe → outputs OFF (REQ-DCC-V-DK-035). Numeric timeout **BLOCKED_BY_EDL_CLARIFICATION** (TBD-DK-007).

**Cable/board boundary:** Production-intent connector family — **Open** (ADR-DK-012).

## 13. DCPI and Service boundary

| Aspect | Owner | Notes |
|--------|-------|-------|
| Real-Time execution | Logic | Safety-relevant paths |
| Service/UI | Radio | Fail-operational isolation |
| Message direction | Bidirectional binary DCPI | No new frames defined |
| Configuration transfer | Radio → Logic → execution | Schema unchanged |
| Diagnostics / heartbeat | Both | Presence ≠ full health |
| Reset independence | Logic and Radio separable | Service reset ≠ power kill |
| Debug separation | IF-DK-DEBUG-LOGIC vs IF-DK-DEBUG-RADIO | Distinct programming paths |

## 14. High-side functional topology

```text
input distribution
  → channel protection boundary
  → controllable high-side switching function
  → load terminal
  → current/diagnostic observation
  → Power-domain fault reporting
  → Logic-domain diagnostic reporting
```

Supported where claimed (ADR-019): ON/OFF; PWM; current observation; OC reaction; SC reaction; retry/latch; control-loss safe OFF; open-load **only if selected implementation claims it**.

## 15. Bidirectional functional topology

```text
power source
  → bidirectional switching function
  → reversible load interface
  → current/fault observation
  → conflict prevention
  → safe OFF
```

| Concern | Responsibility |
|---------|----------------|
| Mutually exclusive direction | Logic command policy + Power hardware interlock |
| Shoot-through prevention | Power switching function (topology TBD) |
| Default state | Both directions OFF |
| Disable path | KILL, global enable, control-loss, local fault |
| Stall-test boundary | External fixture (TBD-DK-022) |
| External energy limitation | Fixture + `I_loadbank_limit` |

Full-bridge component topology **not decided** — functional requirement only.

## 16. External load-bank boundary

| Boundary | Base DevKit | External bank |
|----------|-------------|---------------|
| Electrical | `I_certified_cont`; on-board channels | `I_loadbank_limit`; fixture-defined |
| Control | Logic + J_LP | Fixture controller + operator |
| Ground | BASE_LOAD_RETURN | EXTERNAL_LOAD_RETURN — relation **Open** |
| Enable authority | Logic RT + hardware enables | Fixture explicit enable |
| Abort authority | KILL + input removal | Fixture E-stop + KILL |
| Back-feed prevention | Required — architecture constraint | Must not energize base input |
| Evidence scope | DK-A…DK-D bounded | HC continuous → Phase E (ADR-020) |
| Energization condition | Standard lab procedure | Documented fixture procedure + supervision |

## 17. Representative channel allocation

See [`DevKit_Representative_Channel_Allocation.md`](DevKit_Representative_Channel_Allocation.md).

Functional aliases: CH-HS-BASE, CH-HS-PWM, CH-HS-SENSE, CH-HS-PROTECTED, CH-BI-REP, CH-HC-EXTERNAL.

## 18. Fault-containment analysis (functional)

Label: **functional fault-containment analysis** — not full FMEA.

| Fault origin | Propagation | Local containment | Global mechanism | Single-point risk |
|--------------|-------------|-------------------|------------------|-------------------|
| Logic unpowered | No RT commands | `nENABLE_GLOBAL` safe default | Outputs OFF | KILL path must remain hardware-effective |
| Logic reset | Command epoch reset | Global enable inactive | Outputs OFF until re-enable | Stale command replay if epoch missing |
| Logic pin stuck | Erroneous command | Watchdog; command validation | KILL override | KILL must not depend on Logic pin state alone |
| Power unpowered | No switching | Loads de-energized | Input removal | N/A |
| Power comm frozen | Stale control | Control-loss fail-safe | `T_CTRL_LOSS_MAX` | Timeout value Open |
| Radio unpowered | No Service | None on RT path | Fail-operational | None if RT independent |
| Input protection open | No energy | Immediate OFF | All outputs OFF | Operator must replace protection |
| HS stuck ON | Overcurrent | Local protection; KILL | KILL + fuse layer | Requires independent kill test |
| Sense invalid | Wrong diagnostics | Plausibility checks | Channel derate/OFF | TBD — FW WP |
| BI conflicting control | Shoot-through risk | Direction interlock | Command reject + OFF | Power hardware must default OFF |
| External bank miswired | Back-feed | Fixture design | Input blocking | **Open** — fixture WP |
| Measurement GF | Person/equipment hazard | Lab procedure | E-stop | Procedure-dependent |

## 19. Downstream design-input table

| Parameter | Symbol | Source | Status | Needed by | Closure WP |
|-----------|--------|--------|--------|-----------|------------|
| Input voltage range | `V_IN` | TBD-DK-001 | Open | Sizing | Electrical sizing WP |
| Logic peak current | `I_LOGIC_PEAK` | Architecture | Open | Sizing | Sizing WP |
| Radio peak current | `I_RADIO_PEAK` | Architecture | Open | Sizing | Sizing WP |
| Auxiliary rail current | `I_AUX` | Architecture | Open | Sizing | Sizing WP |
| Rep. channel continuous | `I_CHANNEL_CONT` | TBD-DK-002 | Open | Qualification | Sizing + qual WP |
| PWM frequency | `f_PWM` | TBD-DK-008 | Open | Component | Component WP |
| Channel inrush | `I_INRUSH` | TBD-DK-002 | Open | Protection | Sizing WP |
| SC prospective current | `I_FAULT_PEAK` | WP-009 L14/15 | Open | Protection | Sizing WP |
| Simultaneous profile | `I_simultaneous` | TBD-DK-003 | Open | Multi-load | Sizing + measurement |
| External bank current | `I_loadbank_limit` | ADR-020/021 | Open | Fixture | Fixture WP |
| Kill response | `T_KILL_MAX` | TBD-DK-004 | Open | Verification | Measurement |
| Watchdog response | `T_WD_MAX` | TBD-DK-005 | Open | FW + measurement | FW BSP WP |
| Control-loss timeout | `T_CTRL_LOSS_MAX` | TBD-DK-007 | BLOCKED | Protection | EDL-011 CR |
| Commanded OFF | `T_CMD_OFF_MAX` | TBD-DK-014 | Open | FW | FW BSP WP |
| Ambient temperature | `T_AMB` | ADR-DK-011 | Open | Thermal | Thermal WP |
| Temp rise allowance | `ΔT_allow` | TBD-DK-018/019 | Open | Thermal | Thermal WP |
| Connector mating cycles | `N_mate` | ADR-DK-012 | Open | Connector | ADR-DK-012 |
| Fault-test energy | `E_fault` | ADR-023 | Open | Fixture | Fixture WP |

## 20. Requirement traceability summary

| Architecture block | Requirements | Verification | ADR |
|--------------------|--------------|--------------|-----|
| Board decomposition | REQ-DCC-V-DK-005, 009–012 | VER-DCC-DK-A-001, 007, 009 | ADR-016–018 |
| Power entry | REQ-DCC-V-DK-019–027 | VER-DCC-DK-A-002, 003 | ADR-021 |
| Kill / global enable | REQ-DCC-V-DK-031–038 | VER-DCC-DK-A-012–014 | ADR-022 |
| Channels | REQ-DCC-V-DK-039–055 | VER-DCC-DK-C-* | ADR-019, 020 |
| Measurement | REQ-DCC-V-DK-093–097 | VER-DCC-DK-A-013, C-004 | WP-009 plan |
| Fault injection | REQ-DCC-V-DK-100 | VER-DCC-DK-A/C/D per ADR-023 | ADR-023 |
| Governance | DK-GOV-024, 025 | Inspection | WP-009 |

Full matrix update: [`docs/traceability/TRACEABILITY_MATRIX.md`](../traceability/TRACEABILITY_MATRIX.md).

## 21. Open issues

See [`DevKit_Electrical_Architecture_Open_Issues.md`](DevKit_Electrical_Architecture_Open_Issues.md).

## 22. Related documents

| Document | Role |
|----------|------|
| [`DevKit_Functional_Block_Diagram.md`](DevKit_Functional_Block_Diagram.md) | Diagrams |
| [`DevKit_Power_Domain_Matrix.md`](DevKit_Power_Domain_Matrix.md) | Domain matrix |
| [`DevKit_Safe_State_Path_Matrix.md`](DevKit_Safe_State_Path_Matrix.md) | Safe-state paths |
| [`DevKit_Representative_Channel_Allocation.md`](DevKit_Representative_Channel_Allocation.md) | Channels |
| [`DevKit_Measurement_Point_Register.md`](DevKit_Measurement_Point_Register.md) | Measurement |
| [`DevKit_Electrical_Interface_Register.md`](DevKit_Electrical_Interface_Register.md) | Interfaces |

## 23. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial functional electrical architecture — Proposed |
