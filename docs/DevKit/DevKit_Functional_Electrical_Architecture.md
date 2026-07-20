# DevKit Functional Electrical Architecture — WP-010

**Document ID:** DOC-DK-FEA-001  
**Version:** 1.1  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-010 / WP-010-R1 (Accepted)  
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
| 3 | Hardware KILL independent of Radio, Tablet, and Logic CPU execution | ADR-022; REQ-DCC-V-DK-033 |
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
| **Responsibilities** | VSM; rule execution; CAN; J_LP command master; DCPI RT endpoint; KILL **observation** (parallel branch only); `nENABLE_GLOBAL` control; watchdog; BOARD_ID read; channel command scheduling |
| **Interfaces** | J_LP command/diagnostic (IF-DK-JLP); DCPI (IF-DK-DCPI); CAN (IF-DK-CAN); debug (IF-DK-DEBUG-LOGIC); kill observation (IF-DK-KILL observation branch) |
| **Safe state** | Outputs disabled via withdrawn `nENABLE_GLOBAL`; KILL direct branch effective without Logic execution |
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
| **Responsibilities** | Input distribution; channel switching (HS, PWM, BI); local protection; sense aggregation function; fault reporting; J_LP slave; BOARD_ID; control-loss fail-safe |
| **Interfaces** | J_LP; base load (IF-DK-BASE-LOAD); bidirectional load (IF-DK-BIDIRECTIONAL-LOAD); measurement (IF-DK-MEASUREMENT) |
| **Replaceability** | Power board replaceable without redesigning Logic/Radio external contracts (REQ-DCC-V-DK-113) |
| **Not authorized** | Final channel population; switch MPN; copper sizing |

### 3.4 Fixture boundary (external)

| Attribute | Functional definition |
|-----------|----------------------|
| **Responsibilities** | EXT-SOURCE / EXT-LOAD-BANK / EXT-POWER-MODULE interfaces; fixture protection; E-stop; energy supervision; measurement boundary |
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

External energy roles (distinct):

| Role | Description |
|------|-------------|
| **EXT-SOURCE** | External source of electrical energy (e.g. bench supply for HC discovery) |
| **EXT-LOAD-BANK** | Controlled external load that absorbs energy |
| **EXT-POWER-MODULE** | External representative switching/protection module, if later required |

```text
EXT-SOURCE (when present)
  → separate fixture protection (I_loadbank_limit)
  → EXT-POWER-MODULE (if used)
  → EXT-LOAD-BANK or controlled load interface
  → measurement boundary (DOM-MEASURE)
  → fixture E-stop / abort
```

**Accepted boundary constraints:**

- base and external envelopes remain distinct;
- external ratings do **not** expand `I_certified_cont`;
- back-feed into base distribution is **prohibited**;
- external energization requires explicit fixture authority;
- external E-stop removes external energy;
- measurement and evidence scopes are distinct.

**Ground/reference:** electrically separated in function and protected against back-feed; ground/reference relationship remains **Open** under OI-GND-001. Permitted future options include galvanically isolated, controlled common reference, single-point reference connection, or fixture-defined differential interface. WP-010 does **not** select one.

Do **not** describe a load bank as an energy source.

## 6. View B — Control flow

```text
Logic (RT)
  → J_LP command transport (SPI, PWM)
  → J_LP hardwired safety signals (nENABLE_GLOBAL)
  → Power control domain (DOM-PWR-CTRL)
  → channel switching function (CH-HS-* / CH-BI-REP)
  → output function

Physical KILL (parallel, not Logic-generated):
  → direct hardware-effective branch → Power output-disable authority
  → observation branch → Logic input (logging, epoch, recovery FSM)
```

| Control element | Function | Safe default |
|-----------------|----------|--------------|
| SPI command transport | Channel ON/OFF, PWM duty, configuration | Invalid/stale → rejected or ignored |
| Command-valid / epoch | Pre-kill command invalidation | Post-kill: stale commands blocked (TBD-DK-021) |
| PWM paths | Timer-driven switching | OFF when enable withdrawn |
| `nENABLE_GLOBAL` | Logic-controlled global enable (distinct from KILL) | **Inactive (LOW)** = outputs inhibited |
| `nKILL_HW` | Hardwired safety signal — **not** Logic-generated command | Direct branch: outputs inhibited regardless of SW/Logic CPU |
| Fault feedback | Aggregate fault + diagnostic observation path | Observable by Logic; triggers protection |
| BOARD_ID | Power revision identity | Unsupported/invalid ID → **outputs inhibited** |

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
| **SS-LOCAL-SC** | Short circuit | Local protection + fuse layer | Affected channel de-energized or upstream energy removed; no continued uncontrolled energization | `T_SC_*` Open |
| **SS-INPUT-UV** | Input undervoltage | Input monitor | Outputs inhibited; prior ON commands not auto-restored | TBD-DK-001/012 |
| **SS-INPUT-INT** | Input protection open / supply removed | Energy removal | All outputs inhibited; stale commands on restoration | Energy-removal / load-decay dependent; numeric Open |
| **SS-FIX-ESTOP** | Fixture E-stop | Fixture energy removal | External path energy removed | Energy-removal dependent; numeric Open |
| **SS-CMD-OFF** | Valid OFF command | Firmware-requested | Channel OFF | `T_CMD_OFF_MAX` (TBD-DK-014) |

**Distinction:**

```text
hardware-effective OFF     → KILL, nENABLE_GLOBAL removal, control-loss fail-safe, input energy removal
firmware-requested OFF     → commanded OFF, diagnostic disable
local channel protection   → OC/SC/thermal per channel
observability-only fault   → logged; may not de-energize if fail-operational applies
```

Post-kill re-enable FSM per WP-009 / TBD-DK-021 — no auto-restore; operator ack required.

### 8.1 Safe-state recovery policies

See [`DevKit_Safe_State_Path_Matrix.md`](DevKit_Safe_State_Path_Matrix.md) §2 for full policy text.

| Event | Unconditional minimum | Auto-restore of prior ON commands |
|-------|----------------------|----------------------------------|
| Undervoltage | Outputs inhibited; safe state entered | **No** — explicit enable/new commands required |
| Power restoration | Normal safe startup; all outputs default OFF | **No** — pre-interruption commands stale |
| Invalid BOARD_ID | Outputs inhibited | N/A |
| Invalid configuration | Outputs inhibited; config not executed | N/A |

## 9. View E — Measurement flow

Measurement supports WP-009 [`DevKit_Threshold_Measurement_Plan.md`](DevKit_Threshold_Measurement_Plan.md). Full register: [`DevKit_Measurement_Point_Register.md`](DevKit_Measurement_Point_Register.md).

| Flow | Points | Purpose |
|------|--------|---------|
| Input energy | MP-IN-V, MP-IN-I | Envelope certification; UV behaviour |
| Kill chain | MP-KILL-RAW, MP-KILL-COND, MP-KILL-OBS, MP-GLOBAL-ENABLE, MP-CH-HS-VOUT | TBD-DK-004 timing |
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

Per EDL-011 and `docs/002` §9 (functional — no pin numbers in this architecture).

### 12.1 Signal classes (separated)

| Class | Examples | Nature |
|-------|----------|--------|
| **J_LP command transport** | SPI (SCK/MOSI/MISO/CS); PWM0–3 | Logic-generated commands |
| **J_LP hardwired safety signals** | `nKILL_HW` (if carried on J_LP); `nENABLE_GLOBAL`; `nRESET_PWR` | Hardwired safety — not Logic-generated commands |
| **J_LP diagnostic/sense signals** | Aggregate fault; current-observation path; VBATT_SENSE; TEMP; BOARD_ID | Diagnostic observation |

`nKILL_HW` carried on J_LP is classified as **hardwired safety signal carried by the interface** — not a Logic-generated J_LP control command.

| Signal | Class | Direction | Function |
|--------|-------|-----------|----------|
| SPI | Command transport | Logic → Power | Command transport; configuration |
| PWM0–3 | Command transport | Logic → Power | PWM control to channels |
| `nKILL_HW` | Hardwired safety | External → Power (direct branch); tap → Logic (observation) | Hardware kill net — direct branch independent of Logic CPU |
| `nENABLE_GLOBAL` | Hardwired safety | Logic → Power | Logic-controlled global enable — distinct from KILL |
| `FAULT_N` | Diagnostic/sense | Power → Logic | Aggregate fault indication |
| Current-observation path | Diagnostic/sense | Power → Logic | Sense aggregation function — topology Component/Schematic scope |
| VBATT_SENSE, TEMP | Diagnostic/sense | Power → Logic | Input and thermal observation |
| BOARD_ID | Diagnostic/sense | Power → Logic | Revision identity |
| `nRESET_PWR` | Hardwired safety | Logic → Power | Power controller reset |

**Disconnect behaviour:** J_LP removal → control-loss fail-safe → outputs inhibited (REQ-DCC-V-DK-035). Numeric timeout **BLOCKED_BY_EDL_CLARIFICATION** (TBD-DK-007).

**Cable/board boundary:** Production-intent connector family — **Open** (ADR-DK-012).

## 12.2 Hardware KILL independence topology

```text
Physical KILL input
    ├── direct hardware-effective branch
    │       → Power output-disable authority
    │       → independent of Logic firmware,
    │         Radio, Tablet and DCPI
    │
    └── observation branch
            → Logic input
            → event logging
            → command-epoch invalidation
            → post-kill recovery FSM
```

Logic observation may fail without preventing the hardware-effective disable action.

The direct branch may traverse a future board connector or J_LP hardwired safety net, but shall **not** depend on:

- Logic CPU execution;
- Logic GPIO re-transmission of kill state;
- SPI/DCPI traffic;
- firmware scheduling;
- Radio or Tablet state.

`nENABLE_GLOBAL` remains a **separate** Logic-controlled global enable with inactive safe default. KILL and `nENABLE_GLOBAL` shall not be merged into one signal or one authority.

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

## 16. External energy boundary

| Boundary | Base DevKit | External (EXT-SOURCE / EXT-LOAD-BANK / EXT-POWER-MODULE) |
|----------|-------------|--------------------------------------------------------------|
| Electrical | `I_certified_cont`; on-board channels | `I_loadbank_limit`; fixture-defined |
| Control | Logic RT + hardware enables | Fixture controller + operator |
| Ground/reference | BASE_LOAD_RETURN | EXTERNAL_LOAD_RETURN — **Open** (OI-GND-001); functionally separated; back-feed prohibited |
| Enable authority | Logic RT + hardware enables | Fixture explicit enable |
| Abort authority | KILL direct branch + input removal | Fixture E-stop + KILL |
| Back-feed prevention | Mandatory — base distribution protected | Must not energize base input |
| Evidence scope | DK-A…DK-D bounded | HC continuous → Phase E (ADR-020) |
| Energization condition | Standard lab procedure | Documented fixture procedure + supervision |

## 17. Representative channel allocation

See [`DevKit_Representative_Channel_Allocation.md`](DevKit_Representative_Channel_Allocation.md).

**Capability aliases** (not physical channel counts): CH-HS-BASE, CH-HS-PWM, CH-HS-SENSE, CH-HS-PROTECTED, CH-BI-REP, CH-HC-EXTERNAL.

One physical channel may satisfy multiple HS aliases when §1 conditions in the channel allocation document are met. Physical channel count is **not frozen** in WP-010.

## 18. Fault-containment analysis (functional)

Label: **functional fault-containment analysis** — not full FMEA.

| Fault origin | Propagation | Local containment | Global mechanism | Single-point risk |
|--------------|-------------|-------------------|------------------|-------------------|
| Logic unpowered | No RT commands | `nENABLE_GLOBAL` safe default; KILL direct branch | Outputs inhibited | KILL direct branch must remain hardware-effective without Logic CPU |
| Logic reset | Command epoch reset | Global enable inactive | Outputs inhibited until re-enable | Stale command replay if epoch missing |
| Logic pin stuck | Erroneous command | Watchdog; command validation | KILL direct branch override | KILL direct branch must not depend on Logic pin state |
| Power unpowered | No switching | Loads de-energized | Input removal | N/A |
| Power comm frozen | Stale control | Control-loss fail-safe | `T_CTRL_LOSS_MAX` | Timeout value Open |
| Radio unpowered | No Service | None on RT path | Fail-operational | None if RT independent |
| Input protection open | No energy | Outputs inhibited | All outputs inhibited | Operator must replace protection |
| HS stuck ON | Overcurrent | Local protection; KILL direct branch | KILL + fuse layer | Requires independent kill test |
| Sense invalid | Wrong diagnostics | Plausibility checks | Affected channel inhibited | TBD — FW WP |
| BI conflicting control | Shoot-through risk | Direction interlock | Both directions inhibited | Power hardware must default OFF |
| External bank miswired | Back-feed risk | Fixture design + base protection | Base outputs inhibited | OI-GND-001; fixture WP |
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
| 1.1 | 2026-07-20 | WP-010-R1 — capability aliases; recovery policies; external energy roles; KILL direct branch |
| 1.2 | 2026-07-20 | Architecture Review — WP-010 / WP-010-R1 Accepted; PR #14 merged (`c98ce56`) |

## 24. Architecture Review acceptance (2026-07-20)

| Field | Value |
|-------|-------|
| **Status** | Accepted — Architecture Review |
| **Review date** | 2026-07-20 |
| **Approver role** | System Architect |
| **PR** | #14 merged (`c98ce56`) |

**Accepted:** functional domain decomposition; energy/control/service/safety/measurement views; capability aliases and conditional sharing; safe-state recovery policies; KILL direct branch topology; external energy boundary; measurement and interface registers; open-issue model.

**Not Accepted / remains Open:** numeric current and timing thresholds; component MPNs; connector pins; sizing; schematics; PCB; firmware; fixtures; EDL-011 resolution (TBD-DK-007 BLOCKED).

**Next authorized WP:** WP-011 — EDL-011 clarification + preliminary component-class qualification preparation.
