# DCC Power Channel Architecture

**Document ID:** DCC-PWR-ARCH-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-004

## 1. Purpose

Define the abstract architecture for DriveCore DCC power-output channels before component selection. Establishes engineering channel classes, their relationship to vehicle loads, and the documentation structure for requirements, protection, diagnostics, and state behaviour.

This document does **not** select semiconductors, assign ampere ratings to ICs, define PCB layout, or modify system architecture.

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Abstract high-side and bidirectional channel classes | MPN selection, BOM, schematics |
| Requirement identifiers and traceability | Connector family selection |
| Generic state, protection, diagnostic models | Firmware implementation algorithms |
| Mapping guidance to E30 load inventory | Final channel current ratings |

## 3. References

| Document | Role |
|----------|------|
| [docs/001_System_Architecture.md](../001_System_Architecture.md) | DCC role, VCM, fail-safe |
| [docs/002_DCC_Hardware.md](../002_DCC_Hardware.md) | Gen1 hardware capacity (informational only) |
| [docs/005_Configuration_Model.md](../005_Configuration_Model.md) | `outputs` binding model |
| [E30_Gen1_Load_Inventory.md](../Vehicle_Integration/E30_Gen1_Load_Inventory.md) | Load requirements (WP-003) |
| [E30_Gen1_Operating_Modes.md](../Vehicle_Integration/E30_Gen1_Operating_Modes.md) | Mode versus load matrix |
| [Power_Channel_Classes.md](Power_Channel_Classes.md) | Class definitions |
| [Power_Channel_Requirements.md](Power_Channel_Requirements.md) | Normative requirements |
| [Power_Channel_State_Model.md](Power_Channel_State_Model.md) | Channel state machine |
| [Power_Channel_Protection.md](Power_Channel_Protection.md) | Protection philosophy |
| [Power_Channel_Diagnostics.md](Power_Channel_Diagnostics.md) | Diagnostic requirements |

## 4. Architectural principles

1. **Hardware fixed, behaviour configurable** — Logical load names bind to physical channel indices in vehicle YAML; channel class is a hardware capacity attribute.
2. **Class before component** — Channel classes (HC-A, HC-B, MC-A, LC-A, LC-B, BD-A) describe capability tiers without naming switches or current ampacity.
3. **Load-driven sizing** — E30 load measurements (WP-003) shall inform future class-to-load assignment; until measured, electrical limits remain **TBD**.
4. **Fail-safe OFF** — Any undefined, faulted, or latched state shall default to safe de-energization per [Power_Channel_Protection.md](Power_Channel_Protection.md).
5. **Independence** — Requirements use `DC-DCC-PWR-NNN` identifiers and SHALL statements; implementation is verified separately.

## 5. Channel taxonomy

### 5.1 High-side classes (unidirectional)

| Class ID | Tier | Purpose summary |
|----------|------|-----------------|
| **HC-A** | Highest | Primary high-draw vehicle loads (e.g. steering pump class per E30LD-001) |
| **HC-B** | High reserve | Second high-tier channel or future high-draw reserve |
| **MC-A** | Medium | Motor and pump class loads (cooling, fuel delivery) |
| **LC-A** | Standard | ECU feed, lighting, cabin PWM motors |
| **LC-B** | Auxiliary | Position lamps, wipers, small cabin loads |

### 5.2 Bidirectional class

| Class ID | Purpose summary |
|----------|-----------------|
| **BD-A** | Reversible DC motor loads (e.g. power windows E30LD-023/024) |

Classes are **not** components. They do not imply a specific ampere rating in this work package.

### 5.3 Gen1 hardware capacity (informational)

Gen1 Power Board provides a fixed count of outputs documented in [docs/002](../002_DCC_Hardware.md) and [docs/001](../001_System_Architecture.md) §5.3. WP-004 does not convert these counts into class ampacity.

| Gen1 label (docs) | Abstract class mapping (WP-004) | Count |
|-------------------|----------------------------------|-------|
| HS60 tier | HC-A, HC-B | 2 |
| HS30 tier | MC-A | 4 |
| HS15 tier | LC-A | 8 |
| HS05 tier | LC-B | 8 |
| H-bridge | BD-A | 2 |

Binding of a logical channel index to a class is a hardware revision attribute — **TBD** in qualification phase.

## 6. Channel identity model

| Layer | Identifier | Example |
|-------|------------|---------|
| Logical output | `outputs.<load_key>` in vehicle YAML | `fuel_pump` |
| Physical index | Channel integer 1–22, 101–102 (H-bridge) | `channel: 6` |
| Engineering class | HC-A … BD-A | Assigned per Power Board revision |
| Stable load ID | E30LD-XXX | `E30LD-005` |

A single physical channel shall support exactly one engineering class for its lifetime on a given Power Board revision.

## 7. Control and observation planes

```
┌─────────────────────────────────────────────────────────┐
│  VCM + Rules Engine + Config (Logic, STM32)             │
│       │ command: enable / PWM / retry policy            │
│       ▼                                                 │
│  Channel State Model (per channel)                      │
│       │                                                 │
│       ▼                                                 │
│  Abstract Channel Class requirements (HC-A … BD-A)      │
│       │ observable: diagnostics, faults, telemetry        │
└───────┼─────────────────────────────────────────────────┘
        │ implementation TBD (WP after component selection)
        ▼
   Vehicle load (E30LD-XXX)
```

Logic shall treat channel classes uniformly at the API boundary; class-specific limits are configuration parameters — values **TBD** until load measurement and component qualification.

## 8. E30 load mapping (provisional)

Mapping uses WP-003 inventory assignments. Current ratings **TBD**.

| Load key | E30LD | Provisional class | Notes |
|----------|-------|-------------------|-------|
| ehps | E30LD-001 | HC-A | Ch01 |
| spare_ch02 | E30LD-027 | HC-B | Ch02 reserve |
| fan1, fan2, water_pump, fuel_pump | E30LD-003–005 | MC-A | Ch03–06 |
| ecu_power, headlights_*, heater_blower | E30LD-006,010–011,020 | LC-A | Ch07–11 |
| parking_lights, wipers, spare HS05 | E30LD-012,018,032–037 | LC-B | Ch15–22 |
| window_fl, window_fr | E30LD-023–024 | BD-A | Ch101–102 |

Unassigned loads (brake lights, horn, etc.) require architect channel assignment — see [E30_Gen1_Open_Questions.md](../Vehicle_Integration/E30_Gen1_Open_Questions.md) ADR-E30-009.

## 9. Document map

| Topic | Document |
|-------|----------|
| Per-class capability | [Power_Channel_Classes.md](Power_Channel_Classes.md) |
| Normative SHALL requirements | [Power_Channel_Requirements.md](Power_Channel_Requirements.md) |
| State machine | [Power_Channel_State_Model.md](Power_Channel_State_Model.md) |
| Protection | [Power_Channel_Protection.md](Power_Channel_Protection.md) |
| Diagnostics | [Power_Channel_Diagnostics.md](Power_Channel_Diagnostics.md) |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-004 initial architecture |
