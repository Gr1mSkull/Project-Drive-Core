# DCC Event Model

**Document ID:** DCC-ARCH-EVT-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-005

## 1. Purpose

Define the event-driven internal architecture: sources, subscribers, priorities, persistence, filtering, and rate limiting.

Event delivery mechanics (queues, callbacks) are **not** specified.

## 2. Event anatomy

| Field | Description |
|-------|-------------|
| `event_id` | Stable identifier (e.g. `VEHICLE_MODE_CHANGED`) |
| `source_module` | Publishing module name |
| `timestamp_ms` | From Time Base |
| `priority` | See §4 |
| `payload` | Typed data **TBD** per event |
| `persist` | Whether Logging Manager shall record |

## 3. Event sources

| Module | Example events |
|--------|----------------|
| Power Manager | `POWER_GLOBAL_DISABLE`, `POWER_SUPPLY_DEGRADED` |
| Power Channel Manager | `CHANNEL_ENABLED`, `CHANNEL_FAULT`, `CHANNEL_LATCHED` |
| Vehicle State Manager | `VEHICLE_MODE_CHANGED` |
| Rule Engine | `RULE_FIRED`, `RULE_OUTPUT_COMMAND` |
| ECU Interface | `ECU_TELEMETRY_UPDATED`, `ECU_LOST` |
| Button Box Interface | `INPUT_EVENT`, `BUTTON_BOX_LOST` |
| CAN Manager | `CAN_NODE_TIMEOUT`, `CAN_RX` |
| Internal Bus Manager | `INTERNAL_BUS_TIMEOUT`, `POWER_BOARD_FAULT` |
| Configuration Manager | `CONFIG_APPLIED`, `CONFIG_FAILED` |
| Diagnostics Manager | `NODE_LOST`, `DIAG_FAULT_SUMMARY_CHANGED` |
| Logging Manager | `LOG_BUFFER_WRAP`, `LOG_STORAGE_FULL` |
| Watchdog Manager | `WATCHDOG_FAULT`, `RESET_DETECTED` |
| Firmware Update Manager | `OTA_STARTED`, `OTA_FAILED` |
| Radio Interface | `RADIO_LINK_DOWN` |
| Tablet Interface | `TABLET_CONNECTED`, `CONFIG_UPLOAD_REQUEST` |
| Persistent Storage Manager | `STORAGE_ERROR`, `STORAGE_CORRUPT` |
| Event Manager | `EVENT_DROPPED` **TBD** |

## 4. Priorities

| Priority | Class | Examples | Delivery policy |
|----------|-------|----------|-----------------|
| **P0 — Safety** | Immediate fail-safe | `WATCHDOG_FAULT`, `INTERNAL_BUS_TIMEOUT`, `KILL_ACTIVE` **TBD**, `POWER_GLOBAL_DISABLE` | SHALL NOT be rate-limited (DC-DCC-ARCH-034) |
| **P1 — Fault** | Channel/system faults | `CHANNEL_LATCHED`, `ECU_LOST`, `STORAGE_CORRUPT` | Logged; may trigger degraded mode |
| **P2 — Operational** | Mode and control | `VEHICLE_MODE_CHANGED`, `RULE_FIRED`, `CHANNEL_ENABLED` | Normal dispatch |
| **P3 — Informational** | UI/telemetry hooks | `TABLET_CONNECTED`, `STATE_PUSH_TICK` **TBD** | May be rate-limited |

Subscribers register minimum priority they wish to receive **TBD**.

## 5. Subscribers

| Subscriber | Typical subscriptions |
|------------|----------------------|
| Rule Engine | `VEHICLE_MODE_CHANGED`, `ECU_TELEMETRY_UPDATED`, `INPUT_EVENT`, `CONFIG_APPLIED` |
| Power Channel Manager | `VEHICLE_MODE_CHANGED`, `POWER_GLOBAL_DISABLE`, `CONFIG_APPLIED` |
| Power Manager | `WATCHDOG_FAULT`, `CHANNEL_LATCHED` **TBD** |
| Vehicle State Manager | `RULE_MODE_REQUEST`, `ECU_ENGINE_RUNNING_CHANGED`, `KILL_ACTIVE` **TBD** |
| Diagnostics Manager | All P0–P1 fault events |
| Logging Manager | P0–P2 with `persist=true`; `log_event` from rules |
| Radio Interface | Mirror subset for STATE_PUSH assembly **TBD** |
| Configuration Manager | `STORAGE_READ_OK` **TBD** |

## 6. Persistence

| Policy | Events |
|--------|--------|
| **Always persist** | P0, P1, `VEHICLE_MODE_CHANGED`, `CONFIG_APPLIED` / `CONFIG_FAILED`, `CHANNEL_LATCHED` |
| **Configurable** | `RULE_FIRED`, `INPUT_EVENT` |
| **Never persist** | High-rate telemetry ticks **TBD** |

Persistence path: Event Manager → Logging Manager → Persistent Storage (DC-DCC-ARCH-035).

Retention window **TBD**.

## 7. Filtering

| Filter type | Purpose |
|-------------|---------|
| Module filter | Subscriber receives only selected sources |
| Severity filter | Logging export to Tablet |
| Duplicate suppress | Repeated `ECU_TELEMETRY_UPDATED` not logged per cycle **TBD** |
| Mode filter | Ignore non-applicable rules events in OFF **TBD** |

Filters **shall not** drop P0 events (DC-DCC-ARCH-034).

## 8. Rate limiting

| Category | Limit **TBD** | On overflow |
|----------|---------------|-------------|
| `INPUT_EVENT` rotate bursts | debounce at source | coalesce **TBD** |
| `ECU_TELEMETRY_UPDATED` | 1 log / second max | drop log only |
| `STATE_PUSH` | fixed 50 ms | N/A (not Event Manager) |
| Diagnostic poll | **TBD** | `EVENT_DROPPED` informational |

## 9. Relationship to DCP CAN events

| Internal event | External DCP mapping |
|----------------|-------------------|
| `INPUT_EVENT` | Originated from DCP EVENT MC=2 |
| `ECU_TELEMETRY_UPDATED` | From DCP TELEMETRY MC=1 DT=2 |
| `NODE_LOST` | Heartbeat timeout per 004 |
| DCC-originated notifications | DCP EVENT from DCC **TBD** |

CAN events enter via CAN Manager; internal Event Manager is separate layer.

## 10. Future event categories

| Category | Description | Status |
|----------|-------------|--------|
| `THERMAL_DERATE` | Board temperature policy | **TBD** |
| `SIMULTANEOUS_LOAD_WARNING` | Aggregate current **TBD** | WP-003 measurement |
| `SERVICE_MODE_*` | Maintenance session | **ADR** |
| `EXPANSION_NODE_*` | Gen2 peripherals 0x50+ | Reserved |
| `SECURITY_*` | Auth failures Tablet | **TBD** |

## 11. Requirements cross-reference

- DC-DCC-ARCH-004, 015, 033, 034, 035

## 12. Related documents

- [DCC_Module_Map.md](DCC_Module_Map.md) §5 Event Manager
- [DCC_Data_Flow.md](DCC_Data_Flow.md) §5
- [DCC_Fault_Handling.md](DCC_Fault_Handling.md)

## 13. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-005 event model |
