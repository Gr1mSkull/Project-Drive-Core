# DCC Service Model

**Document ID:** DCC-ARCH-SVC-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-005

## 1. Purpose

Define how DCC logical modules partition across **Real-Time** and **Service** domains, and the allowed interaction patterns between them.

No RTOS, task priority, or processor peripheral assignment is specified.

## 2. Domain summary

| Domain | Criticality | Modules (primary owner) |
|--------|-------------|-------------------------|
| **Real-Time** | Vehicle safety and control | Power Manager, Power Channel Manager, VSM, Rule Engine, Event Manager, Diagnostics, Logging, CAN Manager, Internal Bus Manager, ECU/Button Box Interface, Time Base, Watchdog, Persistent Storage (active runtime) |
| **Service** | Configuration, UI, OTA | Configuration Manager, Firmware Update Manager, Radio Interface, Tablet Interface, Persistent Storage (files/UI assets) |
| **Split** | Defined contract only | Communication Manager, Persistent Storage Manager |

## 3. Layer responsibilities

### 3.1 Real-Time domain

| Responsibility | Owner module |
|----------------|--------------|
| Fail-safe output control | Power Manager + Power Channel Manager |
| Vehicle mode authority | Vehicle State Manager |
| CAN vehicle bus | CAN Manager |
| Power board exchange | Internal Bus Manager (Power leg) |
| ECU/Button Box protocol adapters | ECU Interface, Button Box Interface |
| Rule evaluation cycle | Rule Engine |
| Safety event dispatch | Event Manager |
| Watchdog and reset handling | Watchdog Manager |

Real-Time **shall not** parse JSON or serve HTTP (DC-DCC-ARCH-005).

### 3.2 Service domain

| Responsibility | Owner module |
|----------------|--------------|
| YAML/JSON config ingest and validation | Configuration Manager |
| Config binary compilation | Configuration Manager |
| REST / WebSocket API | Tablet Interface + Radio Interface |
| ESP32 OTA | Firmware Update Manager |
| STM32 OTA orchestration | Firmware Update Manager via DCPI |
| UI static assets | Persistent Storage (Service partition) **TBD** |

Service **shall not** directly energize vehicle power channels without Real-Time consent via DCPI test command in authorized mode **TBD**.

## 4. Cross-domain contracts

| Contract | Direction | Content | Document |
|----------|-----------|---------|----------|
| **DCPI** | Bidirectional Logic↔Radio | STATE_PUSH, EVENT_PUSH, CONFIG_LOAD, OTA, PING | [004](../004_Communication_Protocol.md) §4 |
| **DCP CAN** | RT only to vehicle bus | ECU, Button Box | [004](../004_Communication_Protocol.md) §2–3 |
| **REST/WS** | Service↔Tablet | Telemetry mirror, config, events | [004](../004_Communication_Protocol.md) §5–6, [006](../006_Web_Interface.md) |

No undocumented shared RAM coupling between domains (DC-DCC-ARCH-006).

## 5. Data ownership rules

| Data class | Authoritative owner | Service copy |
|------------|---------------------|--------------|
| Vehicle mode | Vehicle State Manager (RT) | Mirror in STATE_PUSH |
| Channel state | Power Channel Manager (RT) | Mirror in STATE_PUSH |
| ECU telemetry cache | ECU Interface (RT) | Mirror in STATE_PUSH |
| Active configuration | Configuration Manager (apply on RT) | YAML/JSON cache on Service |
| Event log | Logging Manager (RT) | Export via GET /events |
| Node presence | Diagnostics Manager (RT) | Exposed in /status |

Service copies are **read-only mirrors** except configuration upload path.

## 6. Degraded operation

| Failure | Real-Time behaviour | Service behaviour |
|---------|---------------------|-------------------|
| Service offline | Full RT control | N/A |
| Tablet offline | Unchanged | N/A |
| CAN ECU lost | Rules using ECU data inhibited | Telemetry shows stale **TBD** |
| Button Box lost | Input events stop | UI shows node LOST |
| SPI DCPI timeout | Fail-safe outputs OFF | Link down |

Detailed policies: [DCC_Fault_Handling.md](DCC_Fault_Handling.md).

## 7. Service mode (maintenance)

Entry, exit, and permitted write operations: **ARCHITECTURAL DECISION REQUIRED**.

Candidate capabilities (not authorized until ADR):

- Single-channel output test via DCPI OUTPUT_TEST
- Config apply without vehicle motion **TBD**
- Fault latch clear **TBD**

## 8. Related documents

- [DCC_Internal_Architecture.md](DCC_Internal_Architecture.md)
- [DCC_Data_Flow.md](DCC_Data_Flow.md)
- [DCC_Module_Map.md](DCC_Module_Map.md)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-005 service model |
