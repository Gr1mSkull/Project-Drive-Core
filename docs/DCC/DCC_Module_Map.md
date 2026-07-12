# DCC Module Map

**Document ID:** DCC-ARCH-MOD-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-005

Logical module definitions for DCC internal architecture. See [DCC_Internal_Architecture.md](DCC_Internal_Architecture.md) for overview and `DC-DCC-ARCH-xxx` requirements.

**Legend:** RT = Real-Time domain; SVC = Service domain.

---

## 1. Power Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Coordinate DCC power-path readiness, global output enable policy, and supply-quality gating for channel energization. |
| **Responsibilities** | Monitor supply state; enforce global enable/kill interlock policy; gate Power Channel Manager; coordinate board-level power fault reporting. |
| **Inputs** | Supply sense **TBD**; kill input; master contactor feedback; Internal Bus diag from Power board; Watchdog status. |
| **Outputs** | Global enable permission; supply quality flags; power fault events. |
| **Dependencies** | Internal Bus Manager, Watchdog Manager, Power Channel Manager, Diagnostics Manager, Time Base. |
| **Owned Data** | `supply_state`, `global_enable_permitted`, `power_fault_summary`. |
| **Published Events** | `POWER_SUPPLY_OK`, `POWER_SUPPLY_DEGRADED`, `POWER_GLOBAL_DISABLE`, `POWER_UNDERVOLT`, `POWER_OVERVOLT` **TBD** |
| **Consumed Events** | `WATCHDOG_FAULT`, `CHANNEL_LATCHED_FAULT` (aggregate policy **TBD**), `CONFIG_APPLIED`. |
| **Configuration** | UV/OV thresholds **TBD**; derating enables **TBD**. |
| **Failure Behaviour** | Withdraw global enable; all channels de-energized. |
| **Recovery Behaviour** | Re-enable when supply and interlocks valid — timing **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-001, 011; DC-DCC-PWR-003, 069 |
| **Future Expansion** | Multi-rail monitoring; Gen2 auxiliary inputs. |

---

## 2. Power Channel Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Own per-channel output state machine and command execution for all DCC power channels. |
| **Responsibilities** | Translate enable/PWM/direction commands to Internal Bus operations; apply retry/latch policy; report channel faults. |
| **Inputs** | Commands from Rule Engine / VCM table; PWM duty; channel config; Power Manager enable gate. |
| **Outputs** | Channel state; current/fault telemetry **TBD**; SPI/Power board commands. |
| **Dependencies** | Power Manager, Internal Bus Manager, Configuration Manager (active config), Diagnostics Manager, Event Manager. |
| **Owned Data** | Per-channel state, duty, fault flags, retry counters per WP-004. |
| **Published Events** | `CHANNEL_ENABLED`, `CHANNEL_DISABLED`, `CHANNEL_FAULT`, `CHANNEL_LATCHED`, `CHANNEL_RETRY` |
| **Consumed Events** | `VEHICLE_MODE_CHANGED`, `CONFIG_APPLIED`, `POWER_GLOBAL_DISABLE`, `SERVICE_OUTPUT_TEST` **TBD** |
| **Configuration** | Per-output: channel index, type, retry, mode table, limits **TBD**. |
| **Failure Behaviour** | Channel → Fault Detected / Latched; never uncontrolled ON. |
| **Recovery Behaviour** | Per [Power_Channel_State_Model.md](Power_Channel_State_Model.md); manual clear **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-012; DC-DCC-PWR-041–055 |
| **Future Expansion** | Additional PWM lines; Gen2 channel count. |

---

## 3. Configuration Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Ingest, validate, compile, and apply vehicle configuration to Real-Time runtime. |
| **Responsibilities** | Schema validation; binary compilation; CONFIG_LOAD via Internal Bus; version mismatch handling; expose config to Service API. |
| **Inputs** | YAML/JSON from Tablet Interface or file; active hardware capacity descriptor. |
| **Outputs** | DCFG binary; CONFIG_OK / CONFIG_FAIL; active config snapshot id. |
| **Dependencies** | Persistent Storage Manager, Internal Bus Manager, Radio Interface, Communication Manager. |
| **Owned Data** | `active_config_id`, `pending_config`, validation error list. |
| **Published Events** | `CONFIG_RECEIVED`, `CONFIG_VALIDATED`, `CONFIG_APPLIED`, `CONFIG_FAILED` |
| **Consumed Events** | `STORAGE_READ_OK`, `OTA_COMPLETE` **TBD** |
| **Configuration** | `config_version` schema binding. |
| **Failure Behaviour** | Reject apply; retain last known-good active config. |
| **Recovery Behaviour** | Operator correction via UI; rollback from backup blob **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-003, 013, 024; DC-DCC-PWR-101–108 |
| **Future Expansion** | Schema v0.2 migration; merge `e30_gen1_loads.yaml` metadata **TBD**. |

---

## 4. Rule Engine

| Field | Definition |
|-------|------------|
| **Purpose** | Evaluate configured conditional logic and produce output/mode actions. |
| **Responsibilities** | Evaluate `rules[]` against mode, ECU cache, inputs, telemetry; emit output commands and log/notify actions. |
| **Inputs** | Active rules; vehicle mode; ECU bindings; input events; analog/digital inputs **TBD**. |
| **Outputs** | `output_on` / `output_off` commands; `set_mode` requests; `log_event`; `notify`. |
| **Dependencies** | Vehicle State Manager, ECU Interface, Button Box Interface, Power Channel Manager, Event Manager, Logging Manager. |
| **Owned Data** | Rule evaluation context; last-fired rule ids **TBD**. |
| **Published Events** | `RULE_FIRED`, `RULE_OUTPUT_COMMAND`, `RULE_MODE_REQUEST` |
| **Consumed Events** | `VEHICLE_MODE_CHANGED`, `ECU_TELEMETRY_UPDATED`, `INPUT_EVENT`, `CONFIG_APPLIED` |
| **Configuration** | Full `rules` and `ecu_bindings` sections. |
| **Failure Behaviour** | Disable rule evaluation; outputs follow mode table only — **ADR** for partial failure. |
| **Recovery Behaviour** | Re-init on CONFIG_APPLIED; clear transient state. |
| **Related Requirements** | DC-DCC-ARCH-009, 014 |
| **Future Expansion** | Expression language v0.2; cooling_level direct follow. |

---

## 5. Event Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Central publish/subscribe bus for internal asynchronous notification. |
| **Responsibilities** | Register subscribers; dispatch by priority; optional persistence handoff to Logging Manager. |
| **Inputs** | Published events from all modules. |
| **Outputs** | Delivered callbacks / queued deliveries to subscribers. |
| **Dependencies** | Time Base, Logging Manager (optional persist path). |
| **Owned Data** | Subscriber registry; dispatch queues; rate-limit counters **TBD**. |
| **Published Events** | Meta: `EVENT_DROPPED` **TBD** (rate limit overflow) |
| **Consumed Events** | All module-published events. |
| **Configuration** | Priority tables; rate limits per category — [DCC_Event_Model.md](DCC_Event_Model.md). |
| **Failure Behaviour** | Safety events SHALL still be delivered — implementation **TBD**. |
| **Recovery Behaviour** | Reset queues on INIT; preserve latched fault events in Diagnostics. |
| **Related Requirements** | DC-DCC-ARCH-004, 015, 033, 034 |
| **Future Expansion** | Cross-core event bridge RT↔SVC **TBD**. |

---

## 6. Diagnostics Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Aggregate health, faults, and diagnostic snapshots for internal and external reporting. |
| **Responsibilities** | Collect module fault status; merge channel faults; expose diag read API; drive DCP DIAGNOSTIC class **TBD**. |
| **Inputs** | Module fault reports; channel faults; comms staleness; storage errors. |
| **Outputs** | System health summary; per-channel diag; DCP diag responses. |
| **Dependencies** | Power Channel Manager, CAN Manager, ECU Interface, Button Box Interface, Internal Bus Manager, Persistent Storage Manager. |
| **Owned Data** | `system_health`, `node_presence`, `diag_snapshot`. |
| **Published Events** | `DIAG_FAULT_SUMMARY_CHANGED`, `NODE_LOST`, `NODE_PRESENT` |
| **Consumed Events** | `CHANNEL_FAULT`, `CAN_NODE_TIMEOUT`, `STORAGE_ERROR`, `CONFIG_FAILED` |
| **Configuration** | Heartbeat timeout **500 ms** per DCP; diag verbosity **TBD**. |
| **Failure Behaviour** | Report own degradation; shall not clear latched channel faults silently. |
| **Recovery Behaviour** | Refresh on node rediscovery; fault clear only via defined paths. |
| **Related Requirements** | DC-DCC-ARCH-010; DC-DCC-PWR-081–090 |
| **Future Expansion** | Remote diag over Tablet; UDS mapping **TBD**. |

---

## 7. Logging Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Record timestamped operational and safety events for audit and UI export. |
| **Responsibilities** | Format log entries; ring buffer management; archive policy; export via Radio Interface. |
| **Inputs** | `log_event` from Rule Engine; module events; fault transitions. |
| **Outputs** | Persisted log records; EVENT_PUSH to Service **TBD** frequency. |
| **Dependencies** | Persistent Storage Manager, Time Base, Event Manager, Radio Interface. |
| **Owned Data** | Active ring buffer metadata; sequence numbers. |
| **Published Events** | `LOG_ENTRY_RECORDED`, `LOG_BUFFER_WRAP`, `LOG_STORAGE_FULL` |
| **Consumed Events** | `RULE_FIRED` (log actions), `CHANNEL_LATCHED`, `VEHICLE_MODE_CHANGED`, `CONFIG_APPLIED` |
| **Configuration** | Retention size **TBD**; severity filters for export. |
| **Failure Behaviour** | Continue RT control; drop non-critical log entries if storage full — policy **TBD**. |
| **Recovery Behaviour** | Resume append after storage recovery; mark gap in sequence **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-016, 035; DC-DCC-PWR-051–055 |
| **Future Expansion** | Structured log schema; cloud export Gen2. |

---

## 8. Vehicle State Manager (VCM)

| Field | Definition |
|-------|------------|
| **Purpose** | Authoritative owner of vehicle operating mode and legal mode transitions. |
| **Responsibilities** | Execute mode state machine; apply `outputs.*.modes` baseline; accept valid `set_mode` requests; publish mode changes. |
| **Inputs** | Transition triggers **TBD** (ignition, engine_running, kill, rules); digital inputs; ECU flags. |
| **Outputs** | `vehicle_mode`; mode change events; baseline output permissions. |
| **Dependencies** | Rule Engine, Power Channel Manager, ECU Interface, Event Manager, Logging Manager, Configuration Manager. |
| **Owned Data** | `current_mode`, `previous_mode`, `mode_entry_timestamp`. |
| **Published Events** | `VEHICLE_MODE_CHANGED`, `VEHICLE_MODE_REJECTED` |
| **Consumed Events** | `RULE_MODE_REQUEST`, `ECU_ENGINE_RUNNING_CHANGED`, `INPUT_EVENT`, `KILL_ACTIVE`, `CONFIG_APPLIED` |
| **Configuration** | `modes[]` list ordering; per-output mode table. |
| **Failure Behaviour** | Transition to safe mode **TBD** (OFF or MASTER_ON); **ADR** for degraded VCM. |
| **Recovery Behaviour** | Reconcile mode from inputs after restart; prime/ready sequencing per config. |
| **Related Requirements** | DC-DCC-ARCH-002, 009 |
| **Future Expansion** | CRANKING explicit mode; SERVICE mode **ADR**. |

---

## 9. Communication Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Orchestrate external and internal protocol gateways as a single logical façade. |
| **Responsibilities** | Route DCP CAN traffic; coordinate DCPI exchanges; delegate REST/WebSocket to Service; enforce protocol version policy. |
| **Inputs** | CAN frames; DCPI commands; REST requests **SVC**; module publish requests for telemetry. |
| **Outputs** | Routed messages; protocol errors; gateway health. |
| **Dependencies** | CAN Manager, Internal Bus Manager, Radio Interface, Tablet Interface, Diagnostics Manager. |
| **Owned Data** | `protocol_health`, `seq_counters` **TBD**. |
| **Published Events** | `COMMS_DEGRADED`, `COMMS_LOST`, `COMMS_RECOVERED` |
| **Consumed Events** | `RADIO_LINK_DOWN`, `CAN_BUS_OFF` **TBD**, `NODE_LOST` |
| **Configuration** | DCP `proto_ver`; DCPI command map. |
| **Failure Behaviour** | RT continues on CAN if Service lost; CAN loss → degraded per **ADR**. |
| **Recovery Behaviour** | Rediscovery sequence per DCP §8. |
| **Related Requirements** | DC-DCC-ARCH-006, 045, 032 |
| **Future Expansion** | Second CAN bridge Gen2. |

---

## 10. CAN Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Own CAN FD transport and DCP framing for vehicle bus. |
| **Responsibilities** | TX/RX scheduling; heartbeat supervision; message encode/decode; bus error reporting **TBD**. |
| **Inputs** | Raw CAN HW **TBD**; TX requests from ECU/Button Box interfaces and DCC telemetry. |
| **Outputs** | Parsed DCP messages; TX confirmations; timeout events. |
| **Dependencies** | Time Base, Communication Manager, Diagnostics Manager. |
| **Owned Data** | Node tables; RX caches; heartbeat timestamps. |
| **Published Events** | `CAN_RX`, `CAN_TX_COMPLETE`, `CAN_NODE_TIMEOUT`, `CAN_BUS_ERROR` **TBD** |
| **Consumed Events** | Telemetry publish requests; DISCOVER responses. |
| **Configuration** | Bitrate **per 004**; node ID map fixed Gen1. |
| **Failure Behaviour** | Mark nodes LOST; stop using stale ECU data in rules. |
| **Recovery Behaviour** | Node PRESENT on heartbeat resume within 500 ms window. |
| **Related Requirements** | DC-DCC-ARCH-017, 041, 042 |
| **Future Expansion** | FD data phase optimization; expansion nodes 0x50+. |

---

## 11. Internal Bus Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Manage non-CAN internal links: Logic↔Power (safety SPI) and Logic↔Radio (DCPI). |
| **Responsibilities** | Schedule SPI transactions; enforce timeout fail-safe; multiplex sense/diag reads; DCPI command dispatch. |
| **Inputs** | Channel commands; CONFIG_LOAD; STATE_PUSH requests; Power diag responses. |
| **Outputs** | Power board control frames; DCPI responses; link timeout events. |
| **Dependencies** | Power Channel Manager, Configuration Manager, Radio Interface, Watchdog Manager, Time Base. |
| **Owned Data** | `spi_link_state`, `last_power_exchange_ts`, `dcpi_sequence`. |
| **Published Events** | `INTERNAL_BUS_TIMEOUT`, `POWER_BOARD_FAULT`, `DCPI_COMMAND_COMPLETE` |
| **Consumed Events** | Channel command requests; `CONFIG_APPLY_REQUEST`, `STATE_PUSH_TICK` |
| **Configuration** | SPI timeout **100 ms** per 002; DCPI CRC policy. |
| **Failure Behaviour** | SPI timeout → global output disable per architecture. |
| **Recovery Behaviour** | Link reset sequence **TBD**; re-init Power comms. |
| **Related Requirements** | DC-DCC-ARCH-018; DC-DCC-PWR-049 |
| **Future Expansion** | Separate SPI buses; higher bandwidth diag. |

---

## 12. Firmware Update Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Orchestrate OTA and firmware update workflows for Service and Real-Time targets. |
| **Responsibilities** | ESP32 self-OTA; STM32 OTA via DCPI **TBD**; version reporting; safe-state coordination before update. |
| **Inputs** | HTTP OTA upload; OTA_BEGIN/CHUNK commands; version manifests **TBD**. |
| **Outputs** | OTA progress; reboot requests; version telemetry in HEARTBEAT. |
| **Dependencies** | Radio Interface, Internal Bus Manager, Persistent Storage Manager, Communication Manager, Watchdog Manager. |
| **Owned Data** | `ota_session_state`, `target_versions`. |
| **Published Events** | `OTA_STARTED`, `OTA_PROGRESS`, `OTA_COMPLETE`, `OTA_FAILED` |
| **Consumed Events** | `VEHICLE_MODE_SERVICE` **TBD**, `POWER_GLOBAL_DISABLE` |
| **Configuration** | Allowed update modes; signature policy **TBD**. |
| **Failure Behaviour** | Abort session; retain last bootable image. |
| **Recovery Behaviour** | USB/SWD recovery path documented in 004 — outside module. |
| **Related Requirements** | DC-DCC-ARCH-019 |
| **Future Expansion** | Power board update Gen2; dual-bank policy **TBD**. |

---

## 13. Persistent Storage Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Abstract non-volatile storage for config, logs, and calibration **TBD**. |
| **Responsibilities** | FRAM active config; Flash backup; file storage on Service **TBD**; wear policy **TBD**. |
| **Inputs** | Read/write requests from Config, Logging, Diagnostics. |
| **Outputs** | Data blobs; integrity status; CRC results. |
| **Dependencies** | Time Base, Watchdog Manager (long write stall **TBD**). |
| **Owned Data** | Storage layout map **TBD**; health counters. |
| **Published Events** | `STORAGE_READ_OK`, `STORAGE_WRITE_OK`, `STORAGE_ERROR`, `STORAGE_CORRUPT` |
| **Consumed Events** | `CONFIG_APPLIED`, `LOG_ENTRY_RECORDED`, `OTA_STARTED` |
| **Configuration** | Partition sizes **TBD**. |
| **Failure Behaviour** | Reject config apply if active storage corrupt; use backup if valid **TBD**. |
| **Recovery Behaviour** | Format/recover policy **ADR**. |
| **Related Requirements** | DC-DCC-ARCH-035; DC-DCC-PWR-107 |
| **Future Expansion** | External SD via Radio **TBD**. |

---

## 14. Time Base

| Field | Definition |
|-------|------------|
| **Purpose** | Provide monotonic and wall-clock time references for scheduling, logging, and timeouts. |
| **Responsibilities** | Tick source; uptime; optional RTC sync **TBD**; timestamp for events. |
| **Inputs** | Hardware tick **TBD**; optional SNTP from Service **TBD**. |
| **Outputs** | `now_ms`, `uptime_ms`, scheduled deadlines. |
| **Dependencies** | None (foundation module). |
| **Owned Data** | Clock drift estimate **TBD**. |
| **Published Events** | `TIME_SYNC_LOST` **TBD** |
| **Consumed Events** | None required. |
| **Configuration** | Tick rate **TBD**. |
| **Failure Behaviour** | Monotonic uptime shall remain for watchdog and timeouts. |
| **Recovery Behaviour** | Resync wall clock when Service available **TBD**. |
| **Related Requirements** | DC-DCC-PWR-055 |
| **Future Expansion** | GNSS time Gen2. |

---

## 15. Watchdog Manager

| Field | Definition |
|-------|------------|
| **Purpose** | Supervise Real-Time liveness and hardware watchdog integration. |
| **Responsibilities** | Kick policy; detect starvation; assert fail-safe path with Power Manager. |
| **Inputs** | Hardware WDT status **TBD**; task heartbeat counters **TBD**. |
| **Outputs** | Watchdog fault; reset reason; enable withdrawal request. |
| **Dependencies** | Power Manager, Internal Bus Manager, Diagnostics Manager, Time Base. |
| **Owned Data** | `wdt_last_kick`, `reset_reason`. |
| **Published Events** | `WATCHDOG_WARNING`, `WATCHDOG_FAULT`, `RESET_DETECTED` |
| **Consumed Events** | Module health ticks **TBD** |
| **Configuration** | Timeout values **TBD**. |
| **Failure Behaviour** | Hardware WDT reset → startup from [DCC_StartUp_Sequence.md](DCC_StartUp_Sequence.md). |
| **Recovery Behaviour** | Log reset reason; safe state until INIT complete. |
| **Related Requirements** | DC-DCC-ARCH-001, 020, 023 |
| **Future Expansion** | Separate WDT domains per task group **TBD**. |

---

## 16. Radio Interface

| Field | Definition |
|-------|------------|
| **Purpose** | Service-side adapter for DCPI and Wi-Fi/BLE transport to Logic and Tablet. |
| **Responsibilities** | DCPI slave/mirror role **TBD**; assemble REST/WS from STATE_PUSH; forward CONFIG_LOAD. |
| **Inputs** | DCPI from Internal Bus; HTTP/WS from Tablet Interface. |
| **Outputs** | DCPI commands; API responses; link status. |
| **Dependencies** | Internal Bus Manager, Configuration Manager, Firmware Update Manager, Tablet Interface, Communication Manager. |
| **Owned Data** | `radio_link_state`, `last_state_push_ts`. |
| **Published Events** | `RADIO_LINK_UP`, `RADIO_LINK_DOWN`, `STATE_PUSH_RECEIVED` |
| **Consumed Events** | `CONFIG_VALIDATED`, `OTA_STARTED` |
| **Configuration** | API base path; WS rate **20 Hz** per 004. |
| **Failure Behaviour** | RT unaffected; API unavailable. |
| **Recovery Behaviour** | Reconnect DCPI; resume STATE_PUSH consumption. |
| **Related Requirements** | DC-DCC-ARCH-005, 043 |
| **Future Expansion** | BLE provisioning; mesh **TBD**. |

---

## 17. Button Box Interface

| Field | Definition |
|-------|------------|
| **Purpose** | Normalize Button Box DCP events into internal input events. |
| **Responsibilities** | Map `control_id` + `action` to configured `inputs`; debounce not performed here (on Button Box). |
| **Inputs** | DCP EVENT from CAN Manager; `inputs` config. |
| **Outputs** | `INPUT_EVENT` to Rule Engine and VCM **TBD**. |
| **Dependencies** | CAN Manager, Configuration Manager, Event Manager, Diagnostics Manager. |
| **Owned Data** | Input routing table; last event per control_id **TBD**. |
| **Published Events** | `INPUT_EVENT`, `BUTTON_BOX_LOST` |
| **Consumed Events** | `CAN_RX` (Button Box), `CONFIG_APPLIED`, `CAN_NODE_TIMEOUT` (node 0x30) |
| **Configuration** | `inputs.*` with `source: button_box`. |
| **Failure Behaviour** | Stop delivering input events; rules depending on BB stall — **ADR**. |
| **Recovery Behaviour** | Resume on heartbeat; no replay of lost events **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-042, 032 |
| **Future Expansion** | Multiple Button Box instances Gen2. |

---

## 18. ECU Interface

| Field | Definition |
|-------|------------|
| **Purpose** | Maintain ECU telemetry cache and cooling request inputs for Rule Engine and VCM. |
| **Responsibilities** | Parse ENGINE_TELEM and COOLING_REQ; detect staleness; expose `ecu_bindings` namespace. |
| **Inputs** | DCP TELEMETRY from CAN Manager; `ecu_bindings` config. |
| **Outputs** | Cached telemetry; `engine_running` edge events; ECU LOST status. |
| **Dependencies** | CAN Manager, Configuration Manager, Rule Engine, Diagnostics Manager, Event Manager. |
| **Owned Data** | `ecu_cache`, `ecu_last_heartbeat`, `cooling_level`. |
| **Published Events** | `ECU_TELEMETRY_UPDATED`, `ECU_ENGINE_RUNNING_CHANGED`, `ECU_LOST`, `ECU_PRESENT` |
| **Consumed Events** | `CAN_RX` (ECU), `CAN_NODE_TIMEOUT` (node 0x20), `CONFIG_APPLIED` |
| **Configuration** | `ecu_bindings` map. |
| **Failure Behaviour** | Rules using `engine_running` / temps do not fire; cooling fallback **ADR**. |
| **Recovery Behaviour** | Cache refresh on valid telemetry; VCM may hold READY until ECU sync **TBD**. |
| **Related Requirements** | DC-DCC-ARCH-041, 032; docs/003 |
| **Future Expansion** | DriveCore ECU native vs adapter ECU **TBD**. |

---

## 19. Tablet Interface

| Field | Definition |
|-------|------------|
| **Purpose** | Presentation-layer gateway for Web UI client (REST/WebSocket). |
| **Responsibilities** | Authenticate **TBD**; serve telemetry; accept config PUT; restrict writes to Service mode **TBD**. |
| **Inputs** | HTTP/WS client requests; assembled state from Radio Interface. |
| **Outputs** | JSON responses; config upload to Configuration Manager. |
| **Dependencies** | Radio Interface, Configuration Manager, Communication Manager, Firmware Update Manager. |
| **Owned Data** | Session table **TBD**; client subscriptions. |
| **Published Events** | `TABLET_CONNECTED`, `TABLET_DISCONNECTED`, `CONFIG_UPLOAD_REQUEST` |
| **Consumed Events** | `STATE_PUSH_RECEIVED`, `CONFIG_FAILED`, `CONFIG_APPLIED` |
| **Configuration** | API paths per [docs/006](../006_Web_Interface.md). |
| **Failure Behaviour** | No impact on RT; client shows offline. |
| **Recovery Behaviour** | Client reconnects WS; REST poll fallback. |
| **Related Requirements** | DC-DCC-ARCH-005, 044 |
| **Future Expansion** | Multiple clients; role-based access **TBD**. |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-005 module map — 19 modules |
