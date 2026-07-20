# DevKit Safe-State Path Matrix — WP-010

**Document ID:** DOC-DK-SSM-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010  
**Date:** 2026-07-20

Companion to [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md) View D.

## 1. Safe-state path register

| Trigger | Detection domain | Hardware/FW | Control signal | Affected outputs | Expected safe state | Latching | Re-enable authority | Timing TBD | Measurement point | Single-point dependency |
|---------|------------------|-------------|----------------|------------------|---------------------|----------|---------------------|------------|-------------------|----------------------|
| Physical KILL asserted | DOM-HW-KILL | HW | `nKILL_HW` | All channels | All OFF; `I < I_safe` | KILL latched until released | Operator ack + explicit enable (TBD-DK-021) | TBD-DK-004 | MP-KILL-RAW, MP-KILL-COND, MP-GLOBAL-ENABLE | KILL net must not depend on Radio |
| Global enable removed | DOM-GLOBAL-EN | HW+FW | `nENABLE_GLOBAL` inactive | All channels | All OFF | Until Logic re-asserts | Logic RT after ack sequence | Part of TBD-DK-004 | MP-GLOBAL-ENABLE | Logic stuck-high mitigated by KILL |
| Logic watchdog expires | Logic RT | FW→HW | WD → global disable | All channels | All OFF | Until WD serviced + re-enable | Logic RT + operator ack | TBD-DK-005 | MP-GLOBAL-ENABLE | WD period Open |
| Logic↔Power comm lost | Power + Logic | HW fail-safe | SPI timeout | All channels | All OFF | Until comm restored + re-enable | Logic RT + operator ack | TBD-DK-007 **BLOCKED** | MP-JLP-CMD, MP-JLP-FAULT | Power-side timeout hardware |
| Invalid BOARD_ID | Logic RT | FW | Identity check | All or derated | Safe degraded — outputs OFF or limited | Until valid ID | Logic + config | Open | BOARD_ID sense | BOARD_ID read path |
| Input undervoltage | Power / Logic | HW+FW | UV comparator | All channels | Controlled shutdown | Until `V_IN` valid | Auto when voltage restored — subject to REQ-DCC-V-DK-023 | TBD-DK-001/012 | MP-IN-V | UV threshold Open |
| Input interruption | DOM-INPUT-PROTECT | HW | Protection open / PSU off | All channels | Immediate OFF | Until operator restores | Operator | Immediate | MP-IN-V, MP-IN-I | Replaceable protection |
| Channel overcurrent | Power local | HW | OC detect | Affected channel | Channel OFF | Per TBD-DK-013 retry/latch | Logic command after fault clear | Open | MP-CH-HS-IOUT | Local switch + sense |
| Channel short circuit | Power + protection | HW | SC detect + fuse | Channel / system | Channel or system OFF | Fuse replace if blown | Operator + fault clear | TBD-DK-011 | MP-CH-HS-IOUT | Protection coordination Open |
| Thermal condition (if impl.) | Power | HW+FW | TEMP threshold | Affected channel | Derate or OFF | Until cooled | Logic command | TBD-DK-010/018/019 | TEMP sense | Conditional on ADR-DK-011 |
| Radio reset | Radio | FW | Service reset | **None on RT path** | RT outputs unchanged | N/A | N/A | N/A | MP-RADIO-RAIL | Fail-operational required |
| Tablet disconnect | Service | FW | WS loss | **None on RT path** | RT outputs unchanged | N/A | N/A | N/A | DCPI/REST diag | Fail-operational required |
| Configuration invalid | Logic RT | FW | Config validation | Channels as policy | OFF or last safe | Until valid config | Logic + operator | Open | Diagnostics | Config compiler WP |
| External fixture E-stop | Fixture | HW | E-stop circuit | External path | External energy OFF | Until reset | Fixture operator | Immediate | Fixture MP | Fixture design |
| Valid commanded OFF | Logic RT | FW | OFF command | Target channel | Channel OFF | None | Logic operator | TBD-DK-014 | MP-CH-HS-VOUT | Normal operation |
| Service/REST kill bypass attempt | Logic RT | FW | Auth check | None — rejected | KILL remains effective | N/A | N/A | N/A | MP-KILL-COND | REQ-DCC-V-DK-037 |
| Power controller reset | Logic → Power | HW | `nRESET_PWR` | All channels | OFF during reset | Until re-init + enable | Logic RT | Open | MP-GLOBAL-ENABLE | Reset ≠ operator ack |
| Bidirectional conflict | Logic + Power | FW+HW | Direction interlock | BI channel | Both directions OFF | Until valid command | Logic RT | Open | MP-CH-BI-* | Interlock hardware |
| External bank misconnection | Fixture + operator | Procedure | Pre-check | Base input | Must not energize base | Until corrected | Operator | N/A | MP-IN-V | **Open** — fixture WP |

## 2. Path classification legend

| Class | Description | Examples |
|-------|-------------|----------|
| **hardware-effective OFF** | Output disable without Service participation | KILL, global disable, control-loss fail-safe, input removal |
| **firmware-requested OFF** | Normal or diagnostic command path | Commanded OFF, config invalid |
| **local channel protection** | Channel-scoped reaction | OC, SC, thermal |
| **input-energy removal** | Upstream energy gone | Protection open, PSU off |
| **observability-only fault** | Logged; may not de-energize | Some Service degradations |

## 3. Post-kill re-enable sequence (TBD-DK-021)

```text
KILL_ASSERTED → KILL_RELEASED_LOCKED → OPERATOR_ACK_REQUIRED →
FAULT_CLEAR_REQUIRED → READY_FOR_ENABLE → EXPLICIT_FUNCTION_ENABLE
```

- KILL release alone does **not** restore outputs.
- Reset does **not** substitute operator acknowledgement.
- Stale commands invalidated via command epoch (future FW normative definition).

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial safe-state path matrix — Proposed |
