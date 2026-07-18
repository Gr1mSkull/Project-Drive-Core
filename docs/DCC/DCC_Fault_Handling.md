# DCC Fault Handling

**Document ID:** DCC-ARCH-FAULT-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-005

## 1. Purpose

Describe fault-handling **architecture** for DCC internal modules. No recovery algorithms or implementation.

Requirements: DC-DCC-ARCH-031, 032.

## 2. Fault taxonomy

| Class | Examples | Typical response |
|-------|----------|------------------|
| **F1 — Safety critical** | Kill active, watchdog, SPI timeout to Power | Immediate global disable |
| **F2 — Channel persistent** | Latched short, latched thermal | Channel OFF; manual clear **TBD** |
| **F3 — Channel transient** | Inrush retry, momentary OC | Retry Delay per WP-004 |
| **F4 — Communication** | ECU/Button Box/CAN/DCPI loss | Degraded rules/UI |
| **F5 — Configuration** | Invalid YAML, CRC fail, version mismatch | Reject apply; retain last-good |
| **F6 — Storage** | FRAM error, log full | Degraded logging |
| **F7 — Module internal** | Rule engine parse error **TBD** | Module disable; RT continues **TBD** |
| **F8 — Supply** | UV/OV | Inhibit enable / derate **TBD** |

## 3. Module failure

| Failed module | Detection | Containment | Recovery |
|---------------|-----------|-------------|----------|
| Power Channel Manager | Self-diag **TBD** | Power Manager global disable | Reset module; boot |
| Rule Engine | Eval error **TBD** | Stop rule commands | CONFIG_APPLIED re-init |
| Vehicle State Manager | Invalid transition | Hold OFF | Reset **TBD** |
| Event Manager | Queue overflow **TBD** | P0 still delivered **TBD** | Re-init |
| Configuration Manager | Validate fail | No apply | Operator fix |
| Logging Manager | Buffer full | Drop P3 logs **TBD** | Flush / wrap |
| CAN Manager | Bus-off **TBD** | Mark COMMS_DEGRADED | Bus recovery **TBD** |
| Internal Bus Manager | Timeout | F1 global disable | Link reset sequence |
| Watchdog Manager | Missed kick | Hardware reset | Startup sequence |

Module failure shall not cascade into uncontrolled energization (DC-DCC-ARCH-001).

## 4. Communication loss

### ECU loss

| Aspect | Behaviour |
|--------|-----------|
| Detection | HEARTBEAT / ENGINE_TELEM timeout **500 ms** per 004 |
| Immediate | `ECU_LOST`; cache marked stale |
| Rules | Conditions using `engine_running`, temps inhibited |
| Outputs | Cooling AUTO may freeze or fallback — **ADR-E30-004** |
| Recovery | Automatic on valid telemetry |

### Button Box loss

| Aspect | Behaviour |
|--------|-----------|
| Detection | Node 0x30 heartbeat timeout |
| Immediate | `BUTTON_BOX_LOST` |
| Rules | No new `INPUT_EVENT` |
| Outputs | Last AUTO state **TBD** — **ADR-E30-005** |
| Recovery | Automatic on heartbeat |

### CAN bus loss

| Aspect | Behaviour |
|--------|-----------|
| Detection | Bus-off, error passive **TBD** |
| Immediate | `COMMS_DEGRADED` |
| RT | Local VSM and outputs per last mode **TBD** |
| Recovery | Bus recovery procedure **TBD** |

### Service / DCPI loss

| Aspect | Behaviour |
|--------|-----------|
| Detection | DCPI PING timeout **TBD** |
| Immediate | `RADIO_LINK_DOWN` |
| RT | Unaffected — DC-DCC-ARCH-005 |
| Tablet | Offline |
| Recovery | DCPI resync on Service boot |

### Tablet loss

| Aspect | Behaviour |
|--------|-----------|
| Detection | WS disconnect |
| Impact | None on RT |
| Recovery | Client reconnect |

## 5. Configuration failure

| Failure | Response |
|---------|----------|
| Schema validation error | `CONFIG_FAILED`; no RT apply |
| Version mismatch | CONFIG_FAIL per 005 |
| CRC error on stored blob | Attempt backup **TBD** |
| Apply mid-RUN rejected | Atomic apply rule DC-DCC-ARCH-024 |

## 6. Storage failure

| Failure | Response |
|---------|----------|
| Active config corrupt | Load backup or safe defaults **TBD** |
| Log write fail | `LOG_STORAGE_FULL`; continue control |
| OTA partition error | Abort OTA; retain running image |

## 7. Watchdog reset

| Step | Action |
|------|--------|
| 1 | Hardware reset |
| 2 | Outputs OFF by hardware |
| 3 | Startup sequence; log `RESET_DETECTED` |
| 4 | Diagnostics snapshot reset reason |

## 8. Power failure

| Event | Response |
|-------|----------|
| Sudden supply removal | Hardware OFF; no software flush guaranteed |
| Brownout **TBD** | UV detection; global disable before collapse **TBD** |
| Load dump on supply | Input protection survives — thresholds **TBD** |

## 9. Unexpected restart

Combine watchdog reset, power cycle, and software panic **TBD**:

1. Assume Unknown channel states until self-test **TBD**
2. No automatic channel enable
3. VSM defaults to OFF until inputs validated **TBD**
4. Log last reset reason

## 10. DCC degraded mode

System-level degraded state when non-critical faults accumulate — entry/exit **ARCHITECTURAL DECISION REQUIRED**.

Candidate behaviours (not approved):

- Shed LC-B channels
- Limit PWM duty **TBD**
- Disable Tablet writes

Cross-reference: [E30_Gen1_Operating_Modes.md](../Vehicle_Integration/E30_Gen1_Operating_Modes.md) DCC Degraded row.

## 11. Fault reporting path

```
Fault origin module
  → Event Manager (P0/P1)
  → Diagnostics Manager (aggregate)
  → Logging Manager (persist)
  → CAN DIAGNOSTIC / STATE_PUSH
  → Tablet UI
```

## 12. Related documents

- [DCC_Event_Model.md](DCC_Event_Model.md)
- [DCC_StartUp_Sequence.md](DCC_StartUp_Sequence.md)
- [DCC_Shutdown_Sequence.md](DCC_Shutdown_Sequence.md)
- [Power_Channel_Protection.md](Power_Channel_Protection.md)

## 13. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-005 fault handling architecture |
