# DevKit Safe-State Path Matrix — WP-010

**Document ID:** DOC-DK-SSM-001  
**Version:** 1.1  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010 / WP-010-R1  
**Date:** 2026-07-20

Companion to [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md) View D.

## 1. Safe-state path register

| Trigger | Detection domain | Hardware/FW | Control signal | Affected outputs | Expected safe state (unconditional minimum) | Latching | Re-enable authority | Timing TBD | Measurement point | Single-point dependency |
|---------|------------------|-------------|----------------|------------------|---------------------------------------------|----------|---------------------|------------|-------------------|----------------------|
| Physical KILL asserted | DOM-HW-KILL | HW — direct branch | `nKILL_HW` hardware-effective path | All channels | All outputs inhibited; `I < I_safe` | KILL latched until released | Operator ack + explicit enable (TBD-DK-021) | TBD-DK-004 | MP-KILL-RAW, MP-KILL-COND, MP-KILL-OBS, MP-GLOBAL-ENABLE, MP-CH-HS-VOUT | Direct branch must not depend on Logic CPU |
| Global enable removed | DOM-GLOBAL-EN | HW+FW | `nENABLE_GLOBAL` inactive | All channels | All outputs inhibited | Until Logic re-asserts after valid sequence | Logic RT after ack sequence | Part of TBD-DK-004 | MP-GLOBAL-ENABLE | Logic stuck-high mitigated by KILL direct branch |
| Logic watchdog expires | Logic RT | FW→HW | WD → global disable | All channels | All outputs inhibited | Until WD serviced + re-enable | Logic RT + operator ack | TBD-DK-005 | MP-GLOBAL-ENABLE | WD period Open |
| Logic↔Power comm lost | Power + Logic | HW fail-safe | SPI timeout | All channels | All outputs inhibited | Until comm restored + re-enable | Logic RT + operator ack | TBD-DK-007 **BLOCKED** | MP-JLP-CMD, MP-JLP-FAULT | Power-side timeout hardware |
| Invalid BOARD_ID | Logic RT | FW | Identity check | All channels | **Outputs inhibited** | Until valid ID or Accepted compatibility table authorizes detected identity | Logic + config; compatibility table (future) | Open | BOARD_ID sense | BOARD_ID read path |
| Input undervoltage | Power / Logic | HW+FW | UV comparator | All channels | Represented outputs transition to defined safe state; prior ON commands **not** auto-restored | Outputs inhibited until input valid, RT init complete, faults cleared, explicit enable/new commands | Operator + Logic RT | TBD-DK-001/012 | MP-IN-V | UV threshold Open; brief non-resetting UV hysteresis **Open** (OI-UV-002) |
| Input interruption / power restoration | DOM-INPUT-PROTECT | HW | Protection open / PSU off / supply removed | All channels | All outputs inhibited; pre-interruption commands stale | Normal safe startup sequence on restoration | Operator restores supply; then startup sequence | Energy-removal / rail-collapse / load-decay dependent; numeric Open | MP-IN-V, MP-IN-I | Replaceable protection |
| Channel overcurrent | Power local | HW | OC detect | Affected channel | Affected channel de-energized | Per TBD-DK-013 retry/latch | Logic command after fault clear | Open | MP-CH-HS-IOUT | Local switch + sense path |
| Channel short circuit | Power + protection | HW | SC detect + fuse layer | Affected channel minimum; system scope TBD | Affected channel de-energized **or** upstream energy removed; no continued uncontrolled energization | Fuse replace if blown; channel latch per policy | Operator + fault clear | TBD-DK-011 | MP-CH-HS-IOUT | Channel-vs-system containment — protection-coordination scope |
| Thermal condition (if impl.) | Power | HW+FW | TEMP threshold | Affected channel | Affected channel de-energized (unconditional minimum) | Until cooled | Logic command after fault clear | TBD-DK-010/018/019 | TEMP sense | Derate option requires ADR-DK-011 |
| Radio reset | Radio | FW | Service reset | **None on RT path** | RT outputs unchanged | N/A | N/A | N/A | MP-RADIO-RAIL | Fail-operational required |
| Tablet disconnect | Service | FW | WS loss | **None on RT path** | RT outputs unchanged | N/A | N/A | N/A | DCPI/REST diag | Fail-operational required |
| Configuration invalid | Logic RT | FW | Config validation | All channels | **Outputs inhibited; invalid configuration not executed** | Until valid config loaded | Logic + operator | Open | Diagnostics | No undefined "last safe" retention — OI-CONFIG-001 |
| External fixture E-stop | Fixture | HW | E-stop circuit | External path (EXT-LOAD-BANK / EXT-SOURCE) | External energy removed | Until fixture reset | Fixture operator | Energy-removal dependent; numeric Open | Fixture MP | Fixture design |
| Valid commanded OFF | Logic RT | FW | OFF command | Target channel | Target channel de-energized | None | Logic operator | TBD-DK-014 | MP-CH-HS-VOUT | Normal operation |
| Service/REST kill bypass attempt | Logic RT | FW | Auth check | None — rejected | KILL direct branch remains effective | N/A | N/A | N/A | MP-KILL-COND | REQ-DCC-V-DK-037 |
| Power controller reset | Logic → Power | HW | `nRESET_PWR` | All channels | All outputs inhibited during reset | Until re-init + enable | Logic RT | Open | MP-GLOBAL-ENABLE | Reset ≠ operator ack |
| Bidirectional conflict | Logic + Power | FW+HW | Direction interlock | BI channel | Both directions inhibited | Until valid command | Logic RT | Open | MP-CH-BI-* | Interlock hardware |
| External bank misconnection | Fixture + operator | Procedure | Pre-check | Base input | Base outputs inhibited; must not energize base distribution | Until corrected | Operator | N/A | MP-IN-V | OI-GND-001; fixture WP |

## 2. Recovery policies (WP-010-R1)

### Input undervoltage

```text
On undervoltage:
- represented outputs transition to the defined safe state;
- prior ON commands are not automatically restored;
- outputs remain inhibited until input validity is established,
  RT initialization is complete, applicable faults are cleared,
  and explicit enable/new commands are issued.
```

Whether a brief, non-resetting undervoltage event may resume operation under a separate controlled hysteresis policy remains **Open** (OI-UV-002) and requires a future Accepted UV reaction table (TBD-DK-012).

### Input interruption / power restoration

```text
Power restoration shall enter the normal safe startup sequence.
All outputs default OFF.
Pre-interruption commands are stale and shall not re-energize loads.
```

### Invalid BOARD_ID

```text
Unconditional safe default: outputs inhibited.
Derated or compatibility operation allowed only if a future Accepted
compatibility table explicitly authorizes the detected identity.
```

### Invalid configuration

```text
Outputs inhibited; invalid configuration not executed.
No "last safe" retention unless a future Accepted configuration-retention
policy defines retained state, freshness, identity compatibility,
command epoch, authorization, and recovery conditions.
```

## 3. Path classification legend

| Class | Description | Examples |
|-------|-------------|----------|
| **hardware-effective OFF** | Output disable without Service participation | KILL direct branch, global disable, control-loss fail-safe, input energy removal |
| **firmware-requested OFF** | Normal or diagnostic command path | Commanded OFF |
| **local channel protection** | Channel-scoped reaction | OC, SC, thermal |
| **input-energy removal** | Upstream energy gone | Protection open, PSU off |
| **observability-only fault** | Logged; may not de-energize | Some Service degradations |

## 4. Post-kill re-enable sequence (TBD-DK-021)

```text
KILL_ASSERTED → KILL_RELEASED_LOCKED → OPERATOR_ACK_REQUIRED →
FAULT_CLEAR_REQUIRED → READY_FOR_ENABLE → EXPLICIT_FUNCTION_ENABLE
```

- KILL release alone does **not** restore outputs.
- Reset does **not** substitute operator acknowledgement.
- Stale commands invalidated via command epoch (future FW normative definition).

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial safe-state path matrix — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — recovery policies; deterministic safe-state language; KILL direct branch |
