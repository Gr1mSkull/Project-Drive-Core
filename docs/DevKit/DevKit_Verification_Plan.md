# DevKit Verification Plan — Gen1

**Document ID:** DOC-DK-VER-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-007  
**Date:** 2026-07-19  

Normative requirements: [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md).  
Revision identity: ADR-015 / STD-REV-001.  
Gate policy: EDL-014.

> No verification case in this document is marked PASS. No physical tests were executed in WP-007.

## 1. Verification methods

| Method | Acceptable when |
|--------|-----------------|
| Inspection | Documentation, labelling, presence of interfaces, baseline completeness |
| Analysis | Capacity coverage, schema/capacity checks, conflict assessment |
| Demonstration | Setup repeatability, observation access, non-energized procedures |
| Test | Bench-executed behaviour with measurements |

Safety-relevant functional behaviour shall not be verified by documentation inspection alone when bench testing is feasible.

## 2. System baseline (every Test/Demonstration supporting gate exit)

Record applicable STD-REV-001 fields: repository SHA; firmware identities; bootloader; hardware/BOM/assembly/serial; protocol versions; configuration ID/schema/hash; DCFG format version; fixture/equipment IDs; toolchain when relevant.

Incomplete baseline ⇒ certification `NOT VERIFIED` or `PARTIAL`.

## 3. Common fields for each case

Unless overridden: **Test owner** = Implementation Engineer or lab operator recording raw results; **Certification owner** = Independent Reviewer / human Test Owner (`.ai/project_context.md`). **Evidence** = VE record under `docs/records/verification/` when executed (none in WP-007).

## 4. Verification cases

### 4.A — Phase A: Bring-up and safety

#### VER-DCC-DK-A-001 — DevKit purpose and boundary documentation inspection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-001` |
| Title | DevKit purpose and boundary documentation inspection |
| Linked requirements | `REQ-DCC-V-DK-001`, `REQ-DCC-V-DK-002`, `REQ-DCC-V-DK-005`, `REQ-DCC-V-DK-053`, `REQ-DCC-V-DK-082`, `REQ-DCC-V-DK-092` |
| Method | Inspection |
| Objective | Confirm lab-verification scope and component-independence rules. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Documents state DevKit is not production acceptance. |
| Pass criterion | Inspection checklist PASS against listed requirements. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-002 — Unpowered inspection and bench safety provisions

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-002` |
| Title | Unpowered inspection and bench safety provisions |
| Linked requirements | `REQ-DCC-V-DK-019`, `REQ-DCC-V-DK-020`, `REQ-DCC-V-DK-022`, `REQ-DCC-V-DK-024`, `REQ-DCC-V-DK-025`, `REQ-DCC-V-DK-027`, `REQ-DCC-V-DK-093`, `REQ-DCC-V-DK-115` |
| Method | Inspection |
| Objective | Confirm power entry, protection, ground, labels, measurement access. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | No shorts; protection present; access documented. |
| Pass criterion | All mandatory inspection items OK before energization. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-003 — Controlled first power and default OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-003` |
| Title | Controlled first power and default OFF |
| Linked requirements | `REQ-DCC-V-DK-007`, `REQ-DCC-V-DK-023`, `REQ-DCC-V-DK-028`, `REQ-DCC-V-DK-030`, `REQ-DCC-V-DK-094` |
| Method | Test |
| Objective | Energize without loads; measure rails; confirm outputs OFF. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs OFF; rail values recorded. |
| Pass criterion | Outputs OFF AND measurements recorded; unresolved TBD-DK-001/017 blocks DK-A power-test exit. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-004 — Real-Time programming and safe debug access

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-004` |
| Title | Real-Time programming and safe debug access |
| Linked requirements | `REQ-DCC-V-DK-056`, `REQ-DCC-V-DK-057` |
| Method | Test |
| Objective | Program RT domain via documented interface. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Image verified on target. |
| Pass criterion | Program/verify success with identity fields recorded or NOT RECORDED. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-005 — Service-domain programming

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-005` |
| Title | Service-domain programming |
| Linked requirements | `REQ-DCC-V-DK-066` |
| Method | Test |
| Objective | Program Service domain. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Image verified. |
| Pass criterion | Program/verify success recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-008 — Logic-to-Power interface bring-up

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-008` |
| Title | Logic-to-Power interface bring-up |
| Linked requirements | `REQ-DCC-V-DK-011`, `REQ-DCC-V-DK-035`, `REQ-DCC-V-DK-113` |
| Method | Test |
| Objective | Establish Logic↔Power control/sense communication. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Link up or safe fault; no uncontrolled enable. |
| Pass criterion | Link criteria met OR safe fault; outputs not spuriously ON. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-009 — Logic-to-Radio DCPI link bring-up

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-009` |
| Title | Logic-to-Radio DCPI link bring-up |
| Linked requirements | `REQ-DCC-V-DK-012` |
| Method | Test |
| Objective | Establish DCPI link. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Integrity-checked exchange observed. |
| Pass criterion | ≥1 valid exchange succeeds. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-010 — Logic startup operable with outputs OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-010` |
| Title | Logic startup operable with outputs OFF |
| Linked requirements | `REQ-DCC-V-DK-009`, `REQ-DCC-V-DK-059` |
| Method | Test |
| Objective | Observe RT startup. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Operable state; outputs OFF. |
| Pass criterion | State observed AND outputs OFF. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-011 — Watchdog safe-output response

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-011` |
| Title | Watchdog safe-output response |
| Linked requirements | `REQ-DCC-V-DK-038`, `REQ-DCC-V-DK-058` |
| Method | Test |
| Objective | Induce watchdog fault under controlled procedure. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs de-energized within TBD-DK-005. |
| Pass criterion | PASS only if time ≤ approved TBD-DK-005. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-005 not approved (docs/008 candidate <200 ms not frozen). |

#### VER-DCC-DK-A-012 — Kill assertion de-energizes outputs

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-012` |
| Title | Kill assertion de-energizes outputs |
| Linked requirements | `REQ-DCC-V-DK-021`, `REQ-DCC-V-DK-031`, `REQ-DCC-V-DK-033`, `REQ-DCC-V-DK-036`, `REQ-DCC-V-DK-037` |
| Method | Test |
| Objective | Assert kill; attempt Service/UI bypass. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs OFF; bypass fails; time vs TBD-DK-004. |
| Pass criterion | Outputs OFF AND no bypass AND timing approved. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-004 kill response time not approved. |

#### VER-DCC-DK-A-013 — Global enable observability

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-013` |
| Title | Global enable observability |
| Linked requirements | `REQ-DCC-V-DK-032` |
| Method | Test / Demonstration |
| Objective | Observe global enable via documented path. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Enable state visible. |
| Pass criterion | Method and value recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-014 — Safe reset and post-kill re-enable behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-014` |
| Title | Safe reset and post-kill re-enable behaviour |
| Linked requirements | `REQ-DCC-V-DK-034`, `REQ-DCC-V-DK-060`, `REQ-DCC-V-DK-101` |
| Method | Test |
| Objective | Reset / clear kill; confirm no auto re-energize. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs remain OFF until explicit re-enable. |
| Pass criterion | Outputs OFF until explicit re-enable recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-015 — Revision identity availability on bring-up

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-015` |
| Title | Revision identity availability on bring-up |
| Linked requirements | `REQ-DCC-V-DK-016`, `REQ-DCC-V-DK-017`, `REQ-DCC-V-DK-104`, `REQ-DCC-V-DK-105`, `REQ-DCC-V-DK-106`, `REQ-DCC-V-DK-015` |
| Method | Inspection / Demonstration |
| Objective | Capture STD-REV-001 baseline fields; escalate fidelity ADRs. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Fields recorded or NOT RECORDED/TBD; no silent same-binary assumption. |
| Pass criterion | Baseline sheet complete. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-016 — Default OFF across represented channels

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-016` |
| Title | Default OFF across represented channels |
| Linked requirements | `REQ-DCC-V-DK-023`, `REQ-DCC-V-DK-050` |
| Method | Test |
| Objective | Measure represented channels after reset. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | All de-energized. |
| Pass criterion | 100% represented channels OFF. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-A-017 — Blocked physical-board reuse decisions documented

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-017` |
| Title | Blocked physical-board reuse decisions documented |
| Linked requirements | `REQ-DCC-V-DK-114` |
| Method | Inspection |
| Objective | Confirm ADR-DK-001/002 escalation. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Blocked requirements reference ADRs. |
| Pass criterion | Blocked status present. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

### 4.B — Phase B: Communication and service

#### VER-DCC-DK-B-001 — DCP HEARTBEAT observation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-001` |
| Title | DCP HEARTBEAT observation |
| Linked requirements | `REQ-DCC-V-DK-075`, `REQ-DCC-V-DK-081` |
| Method | Test |
| Objective | Observe DCC HEARTBEAT on CAN. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | HEARTBEAT present; period recorded. |
| Pass criterion | Sniffer log shows HEARTBEAT with recorded period. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-002 — ECU simulator telemetry reception

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-002` |
| Title | ECU simulator telemetry reception |
| Linked requirements | `REQ-DCC-V-DK-077` |
| Method | Test |
| Objective | Inject ECU telemetry. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | DCC state/cache updates. |
| Pass criterion | Observable update recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-003 — Stale/lost ECU node handling

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-003` |
| Title | Stale/lost ECU node handling |
| Linked requirements | `REQ-DCC-V-DK-079` |
| Method | Test |
| Objective | Stop simulator beyond TBD-DK-006. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Lost/stale indicated. |
| Pass criterion | PASS only with approved timeout; else BLOCKED. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-006 communication timeout not approved. |

#### VER-DCC-DK-B-004 — Button Box event simulation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-004` |
| Title | Button Box event simulation |
| Linked requirements | `REQ-DCC-V-DK-078` |
| Method | Test |
| Objective | Inject Button Box event. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Configured response observed. |
| Pass criterion | Expected effect recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-005 — CAN termination and signal integrity

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-005` |
| Title | CAN termination and signal integrity |
| Linked requirements | `REQ-DCC-V-DK-076` |
| Method | Test / Inspection |
| Objective | Verify termination; capture waveform vs TBD-DK-015. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Termination present; metrics recorded. |
| Pass criterion | PASS only if TBD-DK-015 approved and met. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-015 CAN waveform criteria not approved. |

#### VER-DCC-DK-B-006 — DCPI integrity-checked state transfer

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-006` |
| Title | DCPI integrity-checked state transfer |
| Linked requirements | `REQ-DCC-V-DK-012`, `REQ-DCC-V-DK-067` |
| Method | Test |
| Objective | Observe DCPI frames with CRC OK. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Valid frames received. |
| Pass criterion | Capture recorded with CRC OK evidence. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-007 — Configuration transfer via Service path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-007` |
| Title | Configuration transfer via Service path |
| Linked requirements | `REQ-DCC-V-DK-068`, `REQ-DCC-V-DK-083`, `REQ-DCC-V-DK-089`, `REQ-DCC-V-DK-118` |
| Method | Test |
| Objective | Load DevKit profile/DCFG. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Valid apply or safe reject; recovery documented. |
| Pass criterion | Result logged; recovery procedure available. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-008 — DCPI CRC rejection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-008` |
| Title | DCPI CRC rejection |
| Linked requirements | `REQ-DCC-V-DK-099` |
| Method | Test |
| Objective | Present corrupted DCPI frame. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Rejected; no unsafe apply. |
| Pass criterion | Rejection observed; outputs not spuriously enabled. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-009 — Diagnostic event visibility via Service

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-009` |
| Title | Diagnostic event visibility via Service |
| Linked requirements | `REQ-DCC-V-DK-051`, `REQ-DCC-V-DK-069`, `REQ-DCC-V-DK-097` |
| Method | Test |
| Objective | Generate diagnostic event; observe Service path. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Event visible. |
| Pass criterion | Event identity/timestamp recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-010 — REST status identity/health

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-010` |
| Title | REST status identity/health |
| Linked requirements | `REQ-DCC-V-DK-070` |
| Method | Test |
| Objective | GET status when REST in scope. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Success with identity/health fields per docs/006. |
| Pass criterion | Required fields present or N/A if REST deferred. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-011 — WebSocket telemetry availability

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-011` |
| Title | WebSocket telemetry availability |
| Linked requirements | `REQ-DCC-V-DK-071` |
| Method | Test |
| Objective | Subscribe telemetry for TBD-DK-016 duration. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Stream available; loss recorded. |
| Pass criterion | PASS only against approved TBD-DK-016. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-016 WS duration/loss criteria not approved. |

#### VER-DCC-DK-B-012 — Authorization negative test for outputs API

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-012` |
| Title | Authorization negative test for outputs API |
| Linked requirements | `REQ-DCC-V-DK-037` |
| Method | Test |
| Objective | Unauthorized output control attempt. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Rejected per auth model. |
| Pass criterion | Unauthorized attempt denied. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-013 — Service cannot bypass kill

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-013` |
| Title | Service cannot bypass kill |
| Linked requirements | `REQ-DCC-V-DK-037` |
| Method | Test |
| Objective | Assert kill; send Service/UI enables. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs remain OFF. |
| Pass criterion | No energization while kill asserted. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-B-014 — OTA mandatory-scope decision gate

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-014` |
| Title | OTA mandatory-scope decision gate |
| Linked requirements | `REQ-DCC-V-DK-074` |
| Method | Inspection / Test |
| Objective | Execute OTA only if ADR-DK-008 mandates. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Decision recorded; no silent PASS. |
| Pass criterion | Remains Blocked/N/A until ADR-DK-008. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | ADR-DK-008 OTA mandatory-for-gate decision required. |

#### VER-DCC-DK-B-015 — Protocol version recording without invented mapping

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-015` |
| Title | Protocol version recording without invented mapping |
| Linked requirements | `REQ-DCC-V-DK-082`, `REQ-DCC-V-DK-092`, `REQ-DCC-V-DK-108` |
| Method | Inspection |
| Objective | Record semantic and/or legacy encoded versions. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | No invented 0xNN=MAJOR.MINOR mapping. |
| Pass criterion | Baseline lists versions with mapping TBD where applicable. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

### 4.C — Phase C: Representative power capability

#### VER-DCC-DK-C-001 — Represented channel inventory and coverage declaration

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-001` |
| Title | Represented channel inventory and coverage declaration |
| Linked requirements | `REQ-DCC-V-DK-014`, `REQ-DCC-V-DK-039`, `REQ-DCC-V-DK-041`, `REQ-DCC-V-DK-052`, `REQ-DCC-V-DK-102`, `REQ-DCC-V-DK-116` |
| Method | Inspection / Analysis |
| Objective | Declare represented vs deferred capability classes. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Coverage matrix complete. |
| Pass criterion | No claim of unrepresented classes. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-002 — Normal ON/OFF switched high-side channel

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-002` |
| Title | Normal ON/OFF switched high-side channel |
| Linked requirements | `REQ-DCC-V-DK-039`, `REQ-DCC-V-DK-050`, `REQ-DCC-V-DK-026` |
| Method | Test |
| Objective | Command ON/OFF with safe load. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | State matches command. |
| Pass criterion | Measured state matches; OFF timing vs TBD-DK-014 when approved. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-003 — PWM-capable channel behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-003` |
| Title | PWM-capable channel behaviour |
| Linked requirements | `REQ-DCC-V-DK-040` |
| Method | Test |
| Objective | Command PWM within TBD-DK-008. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | PWM metrics recorded. |
| Pass criterion | PASS only with approved range; else N/A/BLOCKED. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-008 PWM frequency range not approved. |

#### VER-DCC-DK-C-004 — Current observation path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-004` |
| Title | Current observation path |
| Linked requirements | `REQ-DCC-V-DK-043`, `REQ-DCC-V-DK-095`, `REQ-DCC-V-DK-051` |
| Method | Test |
| Objective | Compare physical current measurement and diagnostic readout. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Both values recorded. |
| Pass criterion | Both recorded; accuracy TBD-DK-009 noted. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-005 — Overcurrent reaction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-005` |
| Title | Overcurrent reaction |
| Linked requirements | `REQ-DCC-V-DK-044`, `REQ-DCC-V-DK-049`, `REQ-DCC-V-DK-100` |
| Method | Test |
| Objective | Controlled overcurrent fixture. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Protect/OFF + fault observable. |
| Pass criterion | Safe protect AND fault flag; abort if unsafe. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-006 — Short-circuit reaction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-006` |
| Title | Short-circuit reaction |
| Linked requirements | `REQ-DCC-V-DK-045`, `REQ-DCC-V-DK-100` |
| Method | Test |
| Objective | Controlled short fixture. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Safe protected state + fault. |
| Pass criterion | Requires approved safe fixture. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | Safe short-circuit fixture / ADR-DK-010 not defined. |

#### VER-DCC-DK-C-007 — Open-load indication where supported

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-007` |
| Title | Open-load indication where supported |
| Linked requirements | `REQ-DCC-V-DK-046` |
| Method | Test |
| Objective | Open-load condition if supported. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Indication or N/A. |
| Pass criterion | Supported⇒indication; else N/A rationale. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-008 — Undervoltage supply behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-008` |
| Title | Undervoltage supply behaviour |
| Linked requirements | `REQ-DCC-V-DK-047` |
| Method | Test |
| Objective | Reduce supply per TBD-DK-012. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Defined behaviour observed. |
| Pass criterion | PASS only with approved threshold. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | TBD-DK-012 undervoltage threshold not approved. |

#### VER-DCC-DK-C-009 — Thermal observation path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-009` |
| Title | Thermal observation path |
| Linked requirements | `REQ-DCC-V-DK-048`, `REQ-DCC-V-DK-096` |
| Method | Test |
| Objective | Record temperature during loaded run. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Temperature values logged. |
| Pass criterion | Logged vs TBD-DK-018/019; no fabricated temperature PASS. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-010 — Bidirectional forward/reverse

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-010` |
| Title | Bidirectional forward/reverse |
| Linked requirements | `REQ-DCC-V-DK-042`, `REQ-DCC-V-DK-055` |
| Method | Test |
| Objective | Forward/reverse with safe load. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Direction correct; stall per TBD-DK-022. |
| Pass criterion | Direction OK; stall may remain BLOCKED. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-011 — Conflicting bridge command prevention

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-011` |
| Title | Conflicting bridge command prevention |
| Linked requirements | `REQ-DCC-V-DK-054` |
| Method | Test |
| Objective | Attempt conflicting drive commands. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Conflict prevented. |
| Pass criterion | No simultaneous opposing drive. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-C-012 — Control-loss and retry/latch behaviours

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-012` |
| Title | Control-loss and retry/latch behaviours |
| Linked requirements | `REQ-DCC-V-DK-035`, `REQ-DCC-V-DK-049` |
| Method | Test |
| Objective | Induce Logic↔Power loss and recoverable fault. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Safe OFF on loss; retry/latch recorded. |
| Pass criterion | Safe OFF; retry metrics vs TBD-DK-013. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

### 4.D — Phase D: System integration

#### VER-DCC-DK-D-002 — VCM mode transition observability

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-002` |
| Title | VCM mode transition observability |
| Linked requirements | `REQ-DCC-V-DK-062` |
| Method | Test |
| Objective | Drive representative mode transitions. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Modes observed. |
| Pass criterion | Required transitions logged. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-003 — Configuration-driven output behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-003` |
| Title | Configuration-driven output behaviour |
| Linked requirements | `REQ-DCC-V-DK-013`, `REQ-DCC-V-DK-061`, `REQ-DCC-V-DK-086` |
| Method | Test |
| Objective | Confirm outputs follow active config. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Matches config; not hardcoded E30 map in common FW. |
| Pass criterion | Behaviour matches config. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-004 — ECU simulation integration scenario

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-004` |
| Title | ECU simulation integration scenario |
| Linked requirements | `REQ-DCC-V-DK-077` |
| Method | Test |
| Objective | Integrated ECU sim scenario. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | System reacts per rules. |
| Pass criterion | Scenario log complete. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-005 — Representative rule execution

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-005` |
| Title | Representative rule execution |
| Linked requirements | `REQ-DCC-V-DK-086` |
| Method | Test |
| Objective | Execute one documented rule scenario. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Rule effect matches configuration thresholds. |
| Pass criterion | Expected output/event recorded. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-006 — Button Box simulation integration scenario

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-006` |
| Title | Button Box simulation integration scenario |
| Linked requirements | `REQ-DCC-V-DK-078` |
| Method | Test |
| Objective | Integrated Button Box scenario. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | System reacts per rules. |
| Pass criterion | Scenario log complete. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-012 — Service restart isolation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-012` |
| Title | Service restart isolation |
| Linked requirements | `REQ-DCC-V-DK-018`, `REQ-DCC-V-DK-065`, `REQ-DCC-V-DK-072` |
| Method | Test |
| Objective | Restart Service during fail-operational output. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | RT continues required outputs. |
| Pass criterion | No unintended OFF solely due to Service restart. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-013 — Tablet disconnect isolation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-013` |
| Title | Tablet disconnect isolation |
| Linked requirements | `REQ-DCC-V-DK-073` |
| Method | Test |
| Objective | Disconnect Tablet during fail-operational output. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Outputs continue. |
| Pass criterion | No unintended OFF. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-014 — CAN node loss integration

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-014` |
| Title | CAN node loss integration |
| Linked requirements | `REQ-DCC-V-DK-080`, `REQ-DCC-V-DK-079` |
| Method | Test |
| Objective | Lose simulated node; observe reaction. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Defined stale handling. |
| Pass criterion | Reaction matches approved timeout policy. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-015 — Configuration apply and invalid rejection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-015` |
| Title | Configuration apply and invalid rejection |
| Linked requirements | `REQ-DCC-V-DK-084`, `REQ-DCC-V-DK-085`, `REQ-DCC-V-DK-087`, `REQ-DCC-V-DK-088`, `REQ-DCC-V-DK-091` |
| Method | Test |
| Objective | Apply valid/invalid configs. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Valid applies; invalid rejected; hot-reload per ADR-DK-009. |
| Pass criterion | Hot-reload remains Blocked until ADR-DK-009. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `BLOCKED` |
| Blocked reason | ADR-DK-009 hot-reload policy required for full case closure. |

#### VER-DCC-DK-D-016 — Event logging and persistent fault reporting

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-016` |
| Title | Event logging and persistent fault reporting |
| Linked requirements | `REQ-DCC-V-DK-063`, `REQ-DCC-V-DK-064` |
| Method | Test |
| Objective | Generate fault; confirm log/persistence expectations. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Events logged. |
| Pass criterion | Evidence includes event records. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-017 — Restart recovery to safe defaults

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-017` |
| Title | Restart recovery to safe defaults |
| Linked requirements | `REQ-DCC-V-DK-060`, `REQ-DCC-V-DK-101` |
| Method | Test |
| Objective | Power cycle / reset recovery. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Safe defaults. |
| Pass criterion | Outputs OFF until authorized re-enable/config. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-019 — Composite baseline recording for gate evidence

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-019` |
| Title | Composite baseline recording for gate evidence |
| Linked requirements | `REQ-DCC-V-DK-016`, `REQ-DCC-V-DK-090`, `REQ-DCC-V-DK-103`, `REQ-DCC-V-DK-107`, `REQ-DCC-V-DK-108`, `REQ-DCC-V-DK-109`, `REQ-DCC-V-DK-110`, `REQ-DCC-V-DK-111`, `REQ-DCC-V-DK-112`, `REQ-DCC-V-DK-117` |
| Method | Inspection |
| Objective | Assemble evidence package with STD-REV-001 baseline. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Baseline complete or certification NOT VERIFIED/PARTIAL. |
| Pass criterion | No gate certification with incomplete mandatory identity. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

#### VER-DCC-DK-D-020 — EDL-014 relationship and exception controls

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-020` |
| Title | EDL-014 relationship and exception controls |
| Linked requirements | `REQ-DCC-V-DK-003`, `REQ-DCC-V-DK-006`, `REQ-DCC-V-DK-008` |
| Method | Inspection |
| Objective | Confirm DK-A..D ≠ vehicle install; exceptions not for track. |
| Preconditions | DevKit de-energized or as specified; baseline sheet prepared; authorized operator present for energized tests |
| System baseline | STD-REV-001 applicable fields |
| Equipment | PSU, meters, loads/fixtures, CAN sniffer, programming adapters as applicable — models not mandated here |
| Safety hazards | Electrical shock, burns, fire from loads; short fixtures |
| Setup | Per case objective; loads connected only when channel OFF (REQ-DCC-V-DK-026) |
| Procedure | 1) Capture baseline 2) Establish preconditions 3) Execute objective actions 4) Record measurements 5) Safe shutdown |
| Measurements | As required by objective; SI units; no vague qualitative-only claims |
| Expected result | Explicit statements present. |
| Pass criterion | Statements present in docs/evidence. |
| Abort criterion | Smoke, uncontrolled current, loss of isolation, temperature beyond approved limit, operator uncertainty about safety |
| Evidence | Logs, captures, photos, measurement tables → VE record when executed |
| Test owner | Implementation Engineer / lab operator (raw) |
| Certification owner | Independent Reviewer / Test Owner |
| Status | `NOT EXECUTED` |

## 5. Gates

### Gate DK-A

| Field | Content |
|-------|---------|
| Entry criteria | Unpowered inspection complete; programming adapters available; no open short defects |
| Mandatory cases | VER-DCC-DK-A-001..A-005, A-008..A-010, A-013..A-017; A-011/A-012 may be BLOCKED only if listed in allowed TBD class below |
| Allowed open TBD classes | Non-safety cosmetic labels; deferred unrepresented channel classes; identity fields marked NOT RECORDED with certification limited |
| Prohibited unresolved issues | Undefined kill/WDT timing for certified safety claims; missing baseline for certification; unrepresented class claimed covered; mandatory FAIL |
| Required evidence | VE records + baseline; Review Handoff for gate decision |
| Responsible reviewer | Independent Reviewer / Test Owner (physical); System Architect for architecture exceptions |
| Exit decision | Accept gate / Revision required / Blocked |
| Rollback | Re-enter prior gate if safety regression found |

A gate shall **not** pass if: mandatory safety tests not executed; baseline incomplete for certification; mandatory case `FAIL`; blocking threshold undefined for a certified claim; critical fault cannot be safely injected/observed when mandatory; evidence absent.

### Gate DK-B

| Field | Content |
|-------|---------|
| Entry criteria | Gate DK-A exited; RT+Service programmed; CAN/DCPI fixtures available |
| Mandatory cases | VER-DCC-DK-B-001,B-002,B-004,B-006..B-010,B-012,B-013,B-015; quantitative B-003/B-005/B-011/B-014 per ADR/TBD closure |
| Allowed open TBD classes | Non-safety cosmetic labels; deferred unrepresented channel classes; identity fields marked NOT RECORDED with certification limited |
| Prohibited unresolved issues | Undefined kill/WDT timing for certified safety claims; missing baseline for certification; unrepresented class claimed covered; mandatory FAIL |
| Required evidence | VE records + baseline; Review Handoff for gate decision |
| Responsible reviewer | Independent Reviewer / Test Owner (physical); System Architect for architecture exceptions |
| Exit decision | Accept gate / Revision required / Blocked |
| Rollback | Re-enter prior gate if safety regression found |

A gate shall **not** pass if: mandatory safety tests not executed; baseline incomplete for certification; mandatory case `FAIL`; blocking threshold undefined for a certified claim; critical fault cannot be safely injected/observed when mandatory; evidence absent.

### Gate DK-C

| Field | Content |
|-------|---------|
| Entry criteria | Gate DK-B exited; safe loads/fixtures available; coverage inventory signed |
| Mandatory cases | VER-DCC-DK-C-001,C-002,C-004,C-005,C-007,C-009..C-012; C-003/C-006/C-008 until thresholds/fixtures approved |
| Allowed open TBD classes | Non-safety cosmetic labels; deferred unrepresented channel classes; identity fields marked NOT RECORDED with certification limited |
| Prohibited unresolved issues | Undefined kill/WDT timing for certified safety claims; missing baseline for certification; unrepresented class claimed covered; mandatory FAIL |
| Required evidence | VE records + baseline; Review Handoff for gate decision |
| Responsible reviewer | Independent Reviewer / Test Owner (physical); System Architect for architecture exceptions |
| Exit decision | Accept gate / Revision required / Blocked |
| Rollback | Re-enter prior gate if safety regression found |

A gate shall **not** pass if: mandatory safety tests not executed; baseline incomplete for certification; mandatory case `FAIL`; blocking threshold undefined for a certified claim; critical fault cannot be safely injected/observed when mandatory; evidence absent.

### Gate DK-D

| Field | Content |
|-------|---------|
| Entry criteria | Gate DK-C exited for represented classes; simulators available |
| Mandatory cases | VER-DCC-DK-D-002..D-006,D-012..D-014,D-016,D-017,D-019,D-020; D-015 until ADR-DK-009 |
| Allowed open TBD classes | Non-safety cosmetic labels; deferred unrepresented channel classes; identity fields marked NOT RECORDED with certification limited |
| Prohibited unresolved issues | Undefined kill/WDT timing for certified safety claims; missing baseline for certification; unrepresented class claimed covered; mandatory FAIL |
| Required evidence | VE records + baseline; Review Handoff for gate decision |
| Responsible reviewer | Independent Reviewer / Test Owner (physical); System Architect for architecture exceptions |
| Exit decision | Accept gate / Revision required / Blocked |
| Rollback | Re-enter prior gate if safety regression found |

A gate shall **not** pass if: mandatory safety tests not executed; baseline incomplete for certification; mandatory case `FAIL`; blocking threshold undefined for a certified claim; critical fault cannot be safely injected/observed when mandatory; evidence absent.

## 6. Relationship to EDL-014

* Passing DK-A through DK-D does **not** approve DCC Gen1 for vehicle installation.
* EDL-014 still requires Phase E critical tests on full DCC Gen1.
* DevKit evidence may support but shall not replace DCC Gen1 evidence.
* Exceptions require an explicit controlled record and are not valid for track use.

## 7. Case count summary

| Phase | Cases | Blocked |
|-------|-------|---------|
| A | 15 | 2 |
| B | 15 | 4 |
| C | 12 | 3 |
| D | 13 | 1 |
| **Total** | **55** | **10** |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial Proposed verification plan |
