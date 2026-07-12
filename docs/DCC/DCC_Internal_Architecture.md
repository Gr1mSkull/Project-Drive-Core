# DCC Internal Architecture

**Document ID:** DCC-ARCH-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-005

## 1. Purpose

Document the **logical** internal architecture of the DriveCore Controller (DCC): modules, ownership, interfaces, and responsibilities.

This work package does **not** introduce hardware implementation, firmware source code, PCB design, RTOS selection, or peripheral assignment.

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Logical module boundaries and data ownership | Component / MPN selection |
| Service versus Real-Time responsibilities | Algorithm implementation |
| Startup, shutdown, fault architecture | UML static diagrams, MCU pin maps |
| Event-driven interaction model | Communication IC selection |
| Traceable `DC-DCC-ARCH-xxx` requirements | Platform architecture redesign |

## 3. Platform context (unchanged)

Per [docs/001_System_Architecture.md](../001_System_Architecture.md):

| Layer | Platform | DCC role |
|-------|----------|----------|
| **Real-Time** | Logic processor | Safety-critical control, CAN, power channels, VCM |
| **Service** | Radio processor | REST, WebSocket, config ingest, OTA orchestration |
| **Presentation** | Tablet / browser | UI client only |

DCC comprises three boards (Logic, Power, Radio) documented in [docs/002_DCC_Hardware.md](../002_DCC_Hardware.md). WP-005 documents **software/logical** modules, not board-level redesign.

## 4. Document map

| Document | Content |
|----------|---------|
| [DCC_Module_Map.md](DCC_Module_Map.md) | Per-module purpose, I/O, dependencies |
| [DCC_Service_Model.md](DCC_Service_Model.md) | Layer ownership and API boundaries |
| [DCC_Data_Flow.md](DCC_Data_Flow.md) | Commands, events, telemetry, persistence |
| [DCC_Event_Model.md](DCC_Event_Model.md) | Event sources, subscribers, priorities |
| [DCC_StartUp_Sequence.md](DCC_StartUp_Sequence.md) | Initialization order |
| [DCC_Shutdown_Sequence.md](DCC_Shutdown_Sequence.md) | Controlled shutdown |
| [DCC_Fault_Handling.md](DCC_Fault_Handling.md) | Fault classes and recovery architecture |
| [Power_Channel_Requirements.md](Power_Channel_Requirements.md) | WP-004 channel requirements (related) |

## 5. Logical structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DCC — Logical Architecture                       │
├────────────────────────────── Real-Time Domain ─────────────────────────┤
│  Vehicle State Manager │ Rule Engine │ Power Manager │ Power Channel Mgr│
│  Event Manager │ Diagnostics Manager │ Logging Manager │ CAN Manager    │
│  ECU / Button Box Interface │ Internal Bus Manager │ Watchdog │ Time   │
│  Persistent Storage (active) │ Communication Manager (RT side)           │
├────────────────────────────── Service Domain ────────────────────────────┤
│  Configuration Manager │ Firmware Update Manager │ Radio Interface       │
│  Tablet Interface │ Communication Manager (Service side)                │
└─────────────────────────────────────────────────────────────────────────┘
         │ CAN FD                    │ DCPI (SPI)              │ Wi-Fi/BLE
         ▼                           ▼                         ▼
    ECU, Button Box            Logic ↔ Radio              Tablet (client)
```

## 6. Architectural principles

1. **Fail-safe OFF** — Loss of control or critical fault shall de-energize power channels (DC-DCC-ARCH-001).
2. **Single VCM authority** — Vehicle State Manager owns mode transitions (DC-DCC-ARCH-002).
3. **Config-driven behaviour** — Outputs and rules from validated configuration, not hardcoded vehicle logic (DC-DCC-ARCH-003).
4. **Event notification, not tight coupling** — Modules interact via published events where possible (DC-DCC-ARCH-004).
5. **Service layer non-critical** — Real-Time shall operate if Service or Tablet is unavailable (DC-DCC-ARCH-005).
6. **Bounded interfaces** — External protocols (DCP, DCPI, REST) are the only cross-boundary contracts (DC-DCC-ARCH-006).

## 7. Normative requirements

### 7.1 Architecture

| ID | Requirement |
|----|-------------|
| **DC-DCC-ARCH-001** | The DCC Real-Time domain SHALL de-energize all power channels when global enable is withdrawn, kill is active, or critical control path failure is detected. |
| **DC-DCC-ARCH-002** | Exactly one logical Vehicle State Manager SHALL own authoritative vehicle mode state. |
| **DC-DCC-ARCH-003** | Load output behaviour SHALL be derived from validated configuration applied through the Configuration Manager. |
| **DC-DCC-ARCH-004** | Internal modules SHALL use the Event Manager for asynchronous notification unless synchronous command path is required for safety. |
| **DC-DCC-ARCH-005** | Loss of the Service layer or Tablet SHALL NOT prevent Real-Time vehicle control within configured degraded policy. |
| **DC-DCC-ARCH-006** | Cross-layer communication SHALL use documented protocol contracts (DCP, DCPI) without undocumented shared memory coupling. |
| **DC-DCC-ARCH-007** | Each logical module SHALL have a single primary owner domain (Real-Time or Service). |
| **DC-DCC-ARCH-008** | Power Channel Manager SHALL delegate channel class semantics to WP-004 requirements without duplicating normative channel rules. |
| **DC-DCC-ARCH-009** | Rule Engine evaluation SHALL NOT bypass Vehicle State Manager mode permissions. |
| **DC-DCC-ARCH-010** | Diagnostics Manager SHALL aggregate module and channel health without masking latched power faults. |

### 7.2 Modules

| ID | Requirement |
|----|-------------|
| **DC-DCC-ARCH-011** | Power Manager SHALL coordinate supply state, global enable policy, and Power Channel Manager enable gates. |
| **DC-DCC-ARCH-012** | Power Channel Manager SHALL own per-channel state per [Power_Channel_State_Model.md](Power_Channel_State_Model.md). |
| **DC-DCC-ARCH-013** | Configuration Manager SHALL validate configuration before apply to Real-Time. |
| **DC-DCC-ARCH-014** | Rule Engine SHALL consume vehicle mode, ECU telemetry cache, and input events to produce output commands. |
| **DC-DCC-ARCH-015** | Event Manager SHALL deliver events to subscribers with defined priority ordering. |
| **DC-DCC-ARCH-016** | Logging Manager SHALL persist safety-relevant events through Persistent Storage Manager. |
| **DC-DCC-ARCH-017** | CAN Manager SHALL implement DCP framing for external nodes only. |
| **DC-DCC-ARCH-018** | Internal Bus Manager SHALL isolate Logic↔Power and Logic↔Radio exchanges from CAN traffic. |
| **DC-DCC-ARCH-019** | Firmware Update Manager SHALL not apply firmware changes without defined safe-state entry **TBD**. |
| **DC-DCC-ARCH-020** | Watchdog Manager SHALL trigger fail-safe path independent of application task health **TBD** timing. |

### 7.3 Lifecycle

| ID | Requirement |
|----|-------------|
| **DC-DCC-ARCH-021** | Startup SHALL follow the ordered sequence in [DCC_StartUp_Sequence.md](DCC_StartUp_Sequence.md). |
| **DC-DCC-ARCH-022** | Shutdown SHALL follow [DCC_Shutdown_Sequence.md](DCC_Shutdown_Sequence.md) when controlled shutdown is possible. |
| **DC-DCC-ARCH-023** | Uncontrolled reset SHALL enter startup from safe hardware state with outputs de-energized. |
| **DC-DCC-ARCH-024** | Configuration apply during RUN SHALL be atomic from Real-Time perspective or rejected. |
| **DC-DCC-ARCH-025** | Module initialization failure SHALL be reported and SHALL prevent promotion to RUN unless degradation policy allows **TBD**. |

### 7.4 Fault and events

| ID | Requirement |
|----|-------------|
| **DC-DCC-ARCH-031** | Fault handling SHALL follow [DCC_Fault_Handling.md](DCC_Fault_Handling.md) without undocumented recovery paths. |
| **DC-DCC-ARCH-032** | Communication loss of ECU, Button Box, or Service layer SHALL have defined degraded behaviour **TBD** per architect. |
| **DC-DCC-ARCH-033** | Events SHALL conform to [DCC_Event_Model.md](DCC_Event_Model.md). |
| **DC-DCC-ARCH-034** | Rate-limited event categories SHALL not drop safety-critical events. |
| **DC-DCC-ARCH-035** | Persistent event storage SHALL survive power cycle for configured retention window **TBD**. |

### 7.5 External interfaces

| ID | Requirement |
|----|-------------|
| **DC-DCC-ARCH-041** | ECU Interface SHALL maintain telemetry cache with staleness detection per DCP heartbeat rules. |
| **DC-DCC-ARCH-042** | Button Box Interface SHALL translate DCP events to internal input events without interpreting physical wiring. |
| **DC-DCC-ARCH-043** | Radio Interface SHALL expose Real-Time state to Service layer via DCPI only. |
| **DC-DCC-ARCH-044** | Tablet Interface SHALL be read-mostly for telemetry; write paths SHALL be restricted to Service mode **TBD**. |
| **DC-DCC-ARCH-045** | Communication Manager SHALL coordinate CAN, Internal Bus, and external client protocol gateways. |

## 8. Module index

| Module | Primary owner | Document |
|--------|---------------|----------|
| Power Manager | Real-Time | [DCC_Module_Map.md](DCC_Module_Map.md) §1 |
| Power Channel Manager | Real-Time | §2 |
| Configuration Manager | Service (+ RT apply) | §3 |
| Rule Engine | Real-Time | §4 |
| Event Manager | Real-Time | §5 |
| Diagnostics Manager | Real-Time | §6 |
| Logging Manager | Real-Time | §7 |
| Vehicle State Manager | Real-Time | §8 |
| Communication Manager | Split | §9 |
| CAN Manager | Real-Time | §10 |
| Internal Bus Manager | Real-Time | §11 |
| Firmware Update Manager | Service | §12 |
| Persistent Storage Manager | Split | §13 |
| Time Base | Real-Time | §14 |
| Watchdog Manager | Real-Time | §15 |
| Radio Interface | Service | §16 |
| Button Box Interface | Real-Time | §17 |
| ECU Interface | Real-Time | §18 |
| Tablet Interface | Service | §19 |

## 9. Related documents

- [docs/004_Communication_Protocol.md](../004_Communication_Protocol.md)
- [docs/005_Configuration_Model.md](../005_Configuration_Model.md)
- [docs/006_Web_Interface.md](../006_Web_Interface.md)
- [docs/003_ECU_Architecture.md](../003_ECU_Architecture.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-005 initial internal architecture |
