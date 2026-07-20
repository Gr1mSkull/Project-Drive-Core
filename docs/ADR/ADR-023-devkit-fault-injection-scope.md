# ADR-023: DevKit Fault Injection Scope and Fixture Boundary

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-023` |
| **Originating decision request** | `ADR-DK-010` |
| **Title** | DevKit Fault Injection Scope and Fixture Boundary |
| **Status** | Proposed |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 |
| **Deliverable status** | Proposed — requires Architecture Review |

> This ADR is **Proposed**. Recommendations are not Accepted. Implementation Engineer cannot approve.


### Context

`REQ-DCC-V-DK-114` / related fault-injection requirements and DK-C/D cases need a defined mandatory injection set and safe fixture boundary. Physical fixture design is **out of scope**; this ADR defines what must be injectable and under what safety rules.

### Problem statement

Which fault injections are mandatory at which DevKit gates, and what fixture boundary/safety requirements apply?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-014 | Lab verification before vehicle |
| Constitution | Supervised power; per-function safe state; no invented ratings |
| REQ fault/diag categories | Open-load, OC, SC, UV, control-loss, CRC, WD, Service/tablet, config, bidirectional |
| ADR-019–022 Proposed | Capabilities, HC scope, current envelope, timing policy |
| DK-GOV | Evidence rules; no PASS without VE |

### Decision drivers

Hazard coverage; operator safety; repeatability; energy limits; distinguish SW vs physical injection; avoid destructive testing as default.

### Options considered (scope strategies)

#### Option A — Maximal physical injection of all listed faults on DevKit before any gate exit
#### Option B — Gate-tiered mandatory set with energy limits; defer vehicle-only faults to Phase E
#### Option C — Software-only fault injection for all gates
#### Option D — Staged: SW injection for bring-up; physical injection required where hardware path is the claim

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Weak | Strong | Weak (misses HW) | Strong |
| Architecture consistency | Weak | Strong | Weak | Strong |
| Reuse toward DCC Gen1 | Acceptable | Strong | Weak | Strong |
| Representativeness | Strong | Strong | Weak | Strong |
| Verification coverage | Strong | Strong | Weak | Strong |
| Development cost | Weak | Acceptable | Strong | Acceptable |
| Hardware cost | Weak | Acceptable | Strong | Acceptable |
| Schedule | Weak | Acceptable | Strong | Acceptable |
| Complexity | Weak | Acceptable | Strong | Acceptable |
| Debuggability | Acceptable | Strong | Acceptable | Strong |
| Future migration | Acceptable | Strong | Weak | Strong |
| Risk | Unacceptable energy | Acceptable | Unacceptable for HW claims | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option B gate-tiered mandatory set, executed with Option D injection-method rules (physical where the claim is hardware-effective).**

**Reason:** Matches DevKit purpose and ADR-020/021 energy architecture. Software-only injection cannot validate hardware kill, SC protection energy path, or open-load sense authenticity.

### Fault classification (Proposed)

| Fault | Class | Reason / hazard | REQs (indicative) | Cases | Fixture capability | Max energy | Supervision | Abort | Destructive? | Sacrificial OK? | Repeatable? | Injection means |
|-------|-------|-----------------|-------------------|-------|--------------------|------------|-------------|-------|---------------|-----------------|-------------|-----------------|
| Output open load | **MANDATORY_DK_C** | False load / missing load detect | 046 | C-007 | Open / remove load | Low | Yes | Remove power | Prohibited | N/A | Yes | Physical + SW inhibit |
| Controlled overcurrent | **MANDATORY_DK_C** | Overcurrent hazard | 044 | C-005 | Adjustable load | **Limited** per envelope | Continuous | E-stop/kill | Prohibited as goal | Fuse OK | Yes | Physical fixture |
| Output short circuit | **MANDATORY_DK_C** | Fire/arc | 045 | C-006 | Controllable SC path | **Strictly limited**; pulse budget Open | Continuous | Hardware abort | Prohibited sustained | Fuse/element OK | Yes (non-destructive intent) | Physical only for HW claim |
| Supply undervoltage | **MANDATORY_DK_C** | Brownout misbehaviour | 047; TBD-001/012 | C-008 | UV supply control | Low | Yes | Restore/abort | Prohibited | N/A | Yes | PSU / fixture |
| Supply interruption | **MANDATORY_DK_A** (safe default) / **MANDATORY_DK_C** (reaction) | Unexpected power loss | 023, 060 | A-003, D-017 | Switchable input | Low | Yes | — | Prohibited | N/A | Yes | Physical switch |
| Logic↔Power comm loss | **MANDATORY_DK_A** / **C** | Stuck-on risk | 035 | A-008, C-012 | Disconnect / clock stop | N/A signal | Yes | Kill | Prohibited | N/A | Yes | Interface disconnect and/or FW test hook (hook not for PASS alone if HW claim) |
| CAN node loss | **MANDATORY_DK_B** / **D** | Stale control | TBD-006 | B-003, D-014 | Stop sim traffic | N/A | Yes | — | Prohibited | N/A | Yes | SW/sim |
| DCPI CRC rejection | **MANDATORY_DK_A** / **B** | Corrupt Service path | 012 | A-009, B-008 | Corrupt frame gen | N/A | Yes | — | Prohibited | N/A | Yes | SW/protocol tool |
| Watchdog expiry | **MANDATORY_DK_A** | RT hang | 038, 058 | A-011 | WD test stimulus | N/A | Yes | Kill available | Prohibited | N/A | Yes | SW test hook **or** fault pin — documented |
| Service-domain restart | **MANDATORY_DK_D** | Fail-op | 018 | D-012 | Reset Service | N/A | Yes | — | Prohibited | N/A | Yes | SW/power domain reset |
| Tablet disconnect | **MANDATORY_DK_D** | UI loss | fail-op reqs | D-013 | Drop WS | N/A | Yes | — | Prohibited | N/A | Yes | SW |
| Configuration corruption | **MANDATORY_DK_D** | Bad config | config reqs | D-008 | Bad payload | N/A | Yes | — | Prohibited | N/A | Yes | SW |
| Configuration capacity violation | **MANDATORY_DK_D** | Overflow | D-007 | D-007 | Oversize map | N/A | Yes | — | Prohibited | N/A | Yes | SW |
| Bidirectional conflicting command | **MANDATORY_DK_C** if BI present | Shoot-through | 054 | C-011 | Command stimulus | Low | Yes | Kill | Prohibited | N/A | Yes | SW (+ observe HW) |
| Bidirectional stall / locked rotor | **CONDITIONAL_MANDATORY** | Motor overcurrent | 055; TBD-022 | C-013 | Stall fixture | Limited | Continuous | Abort | Prefer non-destructive | Element OK | Yes | Physical CONDITIONAL |
| Temperature-sensor fault | **CONDITIONAL_MANDATORY** | Thermal derate loss | 048; ADR-DK-011 | C-009 | Open/short sensor | Low | Yes | — | Prohibited | N/A | Yes | Physical/SW |
| Current-sense fault | **CONDITIONAL_MANDATORY** | Blind OC | 043 | C-004 variant | Sense disrupt | Low | Yes | Kill | Prohibited | N/A | Yes | Physical/SW |
| BOARD_ID invalid/unsupported | **MANDATORY_DK_A** when BOARD_ID implemented | Wrong Power profile | 017 | A-015 | Invalid ID fixture/config | N/A | Yes | Inhibit outputs | Prohibited | N/A | Yes | Physical straps/SW |

Additional classifications:

| Fault | Class |
|-------|-------|
| Highest-current continuous overload beyond ADR-021 envelope | **DCC_GEN1_PHASE_E_ONLY** (or external bank under separate permit) |
| Vehicle harness-specific faults | **DCC_GEN1_PHASE_E_ONLY** / **OUT_OF_SCOPE** for DevKit |
| RF/antenna faults | **OPTIONAL** / deferred with ADR-017 |
| OTA failure modes | **CONDITIONAL_MANDATORY** after ADR-DK-008 |

### Fixture boundary and safety requirements (Proposed — not a schematic)

```text
1. Fixture is laboratory equipment, electrically isolated conceptually from vehicle harness authority.
2. All high-energy injections (OC, SC, stall) shall have: documented max energy/pulse budget (numeric Open until threshold/fixture WP),
   supervised operation, reachable kill/E-stop, and abort that de-energizes independent of DUT software where feasible.
3. Destructive testing of DUT is prohibited as a planned PASS method; sacrificial protection elements in the fixture are permitted if replaced and logged.
4. Repeatability required for mandatory Method:Test cases.
5. Software injection may support cases whose claim is software behaviour; hardware-effective claims require physical or interface-disconnect injection.
6. Fixture shall not require operators to exceed the certified DevKit envelope without explicit escalation (ADR-021).
7. No fixture schematic, relay/contactor/resistor/electronic-load MPN is selected here.
```

### Proposed decision text

```text
PROPOSED: Mandatory fault-injection scope follows the gate-tiered table in this ADR (Option B) with Option D method rules.
DK-A emphasizes bring-up safety faults (supply interruption defaults, comm-loss, DCPI CRC, watchdog, BOARD_ID when implemented).
DK-B emphasizes communications/node/DCPI config-path faults.
DK-C emphasizes power-channel physical faults (open, OC, SC, UV, control-loss, BI conflicts; stall CONDITIONAL).
DK-D emphasizes integration/fail-operational and configuration faults.
Highest-current continuous and vehicle-harness faults remain Phase E / out of DevKit default scope per ADR-020.
Fixture boundary safety rules above are mandatory for fixture requirements WP; this ADR does not design the fixture.
```

### Consequences

Unblocks fixture/load-bank **requirements** WP; clarifies which cases stay BLOCKED until fixtures exist.

### Safety impact

High — defines energy supervision expectations without inventing joule limits yet.

### Verification impact

Architecture blocker for “which injections” resolved **if Accepted**; **Fixture blocker remains**; threshold energy budgets Open; NOT VERIFIED; no VE created.

### Firmware / Hardware / Configuration / Migration

May require test hooks (ADR-018 rules); no HW design now; config corruption cases use test payloads.

### Rejected alternatives

Option A unbounded energy; Option C-only for hardware claims.

### Open dependencies

ADR-019–022; fixture WP; threshold WP; ADR-DK-011; TBD-DK-022.

### Requirements affected

`REQ-DCC-V-DK-044`–`047`, `054`, `055`, `114` (and peer fault-injection reqs), related.

### Verification cases affected

`VER-DCC-DK-A-008`, `A-009`, `A-011`, `A-015`; `B-003`, `B-008`; `C-005`–`C-008`, `C-010`–`C-014`; `D-007`, `D-008`, `D-012`–`D-014`, `D-017`.

### TBDs affected

`TBD-DK-011` (SC method), `022` (stall); energy-related notes for `002/003` — **remain Open**.

### Follow-up Work Packages

Fixture/load-bank requirements; threshold analysis; electrical architecture.

### Rollback or supersession path

Superseding ADR.

### Architecture Review section

| Field | Value |
|-------|-------|
| **Review status** | Pending Architecture Review |
| **Architect decision** | TBD |
| **Acceptance conditions** | TBD |
| **Rejection / correction notes** | TBD |

### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |

