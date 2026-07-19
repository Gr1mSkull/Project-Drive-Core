# DevKit Verification Plan — Gen1

**Document ID:** DOC-DK-VER-001  
**Version:** 1.1.1  
**Status:** Proposed  
**Work Package:** WP-007 / WP-007-R1  
**Date:** 2026-07-19  

System requirements: [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md)  
Governance: [`DevKit_Verification_Governance.md`](DevKit_Verification_Governance.md)  
Identity: ADR-015 / STD-REV-001 · Gate policy: EDL-014

> No case is marked PASS. No physical tests were executed in WP-007 / R1.

## 1. Methods and schemas

Each case uses a method-specific field set (Inspection / Analysis / Demonstration / Test). Shared safety preamble: supervised energization; kill accessible; loads connected only when channel OFF; abort on smoke/uncontrolled current. This preamble does **not** replace case procedures.

## 2. Classifications and gate outcomes

See governance §2–§4. Outcomes: PASS / FAIL / BLOCKED / NOT ASSESSED. Incomplete applicable baseline identity ⇒ cannot PASS.

## 3. System verification cases

### 3.A — Phase A: Bring-up and safety

#### VER-DCC-DK-A-001 — DevKit system-boundary documentation inspection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-001` |
| Title | DevKit system-boundary documentation inspection |
| Linked IDs | `REQ-DCC-V-DK-001`, `REQ-DCC-V-DK-004`, `REQ-DCC-V-DK-005` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Confirm documented DevKit purpose and system boundary match active system requirements. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | docs/DevKit/README.md; docs/DevKit/DevKit_System_Requirements.md §4.A (REQ-001/004/005); EDL-014 statement in docs/EDL/README.md |
| Checklist | README states laboratory verification platform role; REQ-001 purpose SHALL is present and unambiguous; REQ-004 includes RT, Service, and representative Power domains; REQ-005 excludes vehicle-install packaging/harness/full production population unless separately approved |
| Pass criterion | All checklist items PASS; no contradiction with EDL-014 gate intent. |
| Evidence to retain | Annotated checklist export or review note with document revisions |
| Procedure | 1. Open listed artifacts at the commit under review 2. Complete checklist item-by-item 3. Record document versions/SHAs in the inspection record |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-002 — Unpowered assembly and bench safety inspection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-002` |
| Title | Unpowered assembly and bench safety inspection |
| Linked IDs | `REQ-DCC-V-DK-019`, `REQ-DCC-V-DK-020`, `REQ-DCC-V-DK-022`, `REQ-DCC-V-DK-024`, `REQ-DCC-V-DK-025`, `REQ-DCC-V-DK-027`, `REQ-DCC-V-DK-093`, `REQ-DCC-V-DK-115` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Confirm power-entry, protection presence, ground reference, labels, and measurement access before any energization. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | Physical DevKit assembly; Bench setup photo set; Protection device marking |
| Checklist | Single controlled power-entry path identified; Replaceable overcurrent protection device present and identifiable; Ground reference point labelled; High-current terminals insulated/covered or equivalently protected for normal bench use; Critical sense/control points accessible without destructive disassembly; External connections labelled for repeatable setup; Continuity/short check completed with no power-rail short recorded |
| Pass criterion | Every checklist item marked PASS with recorded evidence pointer; if any power-rail short is found, energization is prohibited and this case is FAIL. |
| Evidence to retain | Inspection checklist; Photos of labels/protection/ground; Multimeter continuity log |
| Procedure | 1. Ensure PSU disconnected and locked out 2. Perform continuity/short checks on power rails 3. Complete checklist 4. Store photos and measurements |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-003 — Controlled first power — rails measurable, outputs default OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-003` |
| Title | Controlled first power — rails measurable, outputs default OFF |
| Linked IDs | `REQ-DCC-V-DK-007`, `REQ-DCC-V-DK-023`, `REQ-DCC-V-DK-030`, `REQ-DCC-V-DK-094` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Energize DevKit without loads and confirm default OFF plus measurable rails. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-006; TBD: TBD-DK-001, TBD-DK-017; fixture: Documented rail test points; impl: Programmed RT image capable of default OFF |
| Preconditions | A-002 PASS; no loads connected; supervised operator present |
| Topology | Bench PSU → IF-DK-PWR-IN; GND bonded; no channel loads; meters on designated rail TP |
| Equipment | Lab PSU; DMM; baseline identity sheet |
| Hazards | Electrical shock; unintended energization of outputs |
| Test configuration | No active output-enable configuration; factory/default safe config or empty enable mask |
| Stimuli | Apply approved input voltage once TBD-DK-001 approved; do not command outputs ON |
| Procedure | 1. Capture interim identity record (commit SHA, HW IDs available) 2. Confirm A-002 complete 3. Connect PSU only; set voltage to approved TBD-DK-001 value 4. Energize; wait startup complete (observe READY/operable indication if available) 5. Measure each required rail at documented test points 6. Measure each represented channel output terminal voltage relative to ground 7. Confirm no channel is commanded ON via diagnostic readout 8. De-energize |
| Measurements | Vin_V; Vrail_*_V; Vout_chN_V for each represented channel; diagnostic output state |
| Expected result | All represented channel outputs electrically OFF; rails within TBD-DK-017 when approved |
| Pass criterion | For every represented channel: Vout indicates OFF per documented OFF threshold AND diagnostic state OFF; rails within approved TBD-DK-017. If TBD unresolved: status remains BLOCKED (no qualitative PASS). |
| Abort criterion | Any represented channel energizes; smoke; overcurrent trip unexpected; operator uncertainty |
| Evidence | Measurement table; diagnostic snapshot; identity sheet |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

##### VER-DCC-DK-A-004 — Real-Time programming and safe debug access

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-004` |
| Title | Real-Time programming and safe debug access |
| Linked IDs | `REQ-DCC-V-DK-056`, `REQ-DCC-V-DK-057` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Program the Real-Time domain via the documented interface and confirm debug access is available without requiring output enable. |
| Status | `NOT EXECUTED` |
| Preconditions | DevKit de-energized or in documented programming-safe state; programming adapter connected to IF-DK-SWD (or documented RT programming path); no channel loads connected |
| Topology | Host programmer ↔ IF-DK-SWD (or documented RT program port) ↔ Real-Time MCU; Power domain unpowered or held in reset/safe per programming guide |
| Equipment | Host with approved programming toolchain; SWD/USB adapter per programming guide |
| Hazards | Incorrect image; accidental energization during debug |
| Test configuration | No output-enable configuration applied |
| Stimuli | Program known RT firmware image identity (commit SHA / build artifact ID); optional halt/resume via debugger |
| Procedure | 1. Record image identity (artifact path, commit SHA, hash if available) 2. Connect programming adapter with PSU off or programming-safe 3. Erase/program/verify RT image using documented commands 4. Confirm tool verify success 5. Establish debug session (halt) with outputs uncommanded 6. Confirm no represented channel is ON (measure or diagnostic) 7. Resume/disconnect per guide |
| Measurements | program/verify result; debug session establish (yes/no); Vout_chN or diagnostic output state |
| Expected result | Verify success; debug session possible; outputs remain OFF |
| Pass criterion | Tool reports verify success for the recorded RT image identity AND debug halt/session establishes AND every represented channel remains OFF during the session. |
| Abort criterion | Unexpected channel ON; adapter overcurrent; verify failure after two documented retries |
| Evidence | Host programming log; image identity record; output-state snapshot |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-006 — Baseline identity recording (STD-REV-001)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-006` |
| Title | Baseline identity recording (STD-REV-001) |
| Linked IDs | `REQ-DCC-V-DK-117` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Confirm every applicable STD-REV-001 identity field is recorded so setup is repeatable from baseline identity (system testability); evidence-claim rules remain DK-GOV-*. |
| Status | `BLOCKED` |
| Blocked by | TBD-DK-001…004; interim identity procedure escalation if semantic firmware metadata unimplemented |
| Artifacts inspected | Baseline identity record for the candidate DevKit artifact set; STD-REV-001 applicable field checklist; build/provenance notes if semantic firmware metadata absent |
| Checklist | Every applicable Logic/Power/Radio/firmware/configuration identity field listed; each field valued, justified N/A, or marked UNKNOWN/NOT RECORDED/TBD; no certification claim with applicable UNKNOWN/NOT RECORDED/TBD (DK-GOV-014…016); if semantic firmware metadata unimplemented, escalate for reviewed interim procedure rather than invent |
| Pass criterion | Every applicable field valued or justified N/A; zero applicable UNKNOWN/NOT RECORDED/TBD remain for a PASS claim. Missing applicable identity ⇒ gate outcome BLOCKED or NOT ASSESSED (not PASS). |
| Evidence to retain | Completed identity checklist; escalation note if interim procedure required |
| Procedure | 1. Open STD-REV-001 applicable checklist 2. Fill each field from the tested artifact set 3. Mark genuine non-applicable fields N/A with justification 4. Escalate if interim identity procedure is required |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-007 — Interface matrix and documentation cross-reference integrity

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-007` |
| Title | Interface matrix and documentation cross-reference integrity |
| Linked IDs | `REQ-DCC-V-DK-011`, `REQ-DCC-V-DK-012`, `REQ-DCC-V-DK-019`, `REQ-DCC-V-DK-117` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Confirm DevKit interfaces required by active system requirements appear in the Interface Matrix and that docs/008 cross-references resolve without duplicate normative Phase A–D cases. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | `docs/DevKit/DevKit_Interface_Matrix.md`; `docs/008_Testing_and_Validation.md`; `docs/DevKit/README.md`; System Requirements; Verification Plan; Governance |
| Checklist | IF-DK-JLP, IF-DK-DCPI, IF-DK-PWR-IN, IF-DK-CAN rows present with owner/TBD markers; no invented pin assignments claimed as approved; every Markdown link from docs/008 DevKit section and DevKit README resolves; docs/008 contains no duplicate normative Phase A–D case tables; legacy candidate IDs not presented as approved; EDL-014 meaning preserved |
| Pass criterion | All checklist items PASS. |
| Evidence to retain | Annotated checklist; link-check log; document revisions/SHAs |
| Procedure | 1. Inventory required interfaces from REQ-011/012/019 2. Match each to Interface Matrix rows 3. Walk docs/008 and DevKit README links 4. Confirm no duplicate normative Phase A–D tables |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

### VER-DCC-DK-A-005 — Service-domain programming

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-005` |
| Title | Service-domain programming |
| Linked IDs | `REQ-DCC-V-DK-066`, `REQ-DCC-V-DK-010` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Program Service domain via documented interface. |
| Status | `NOT EXECUTED` |
| Preconditions | Documented Service programming path available |
| Topology | Host ↔ Service programming interface (USB or documented alt) |
| Equipment | Host tools per Service programming guide |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Program/verify Service firmware image from known commit |
| Procedure | 1. Record image identity 2. Program and verify 3. Capture tool log |
| Measurements | program/verify result |
| Expected result | Verify success |
| Pass criterion | Tool reports verify OK for recorded Service image identity. |
| Abort criterion | Repeated verify failure |
| Evidence | Host log; image identity |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-008 — Logic-to-Power interface bring-up and no spurious output enable

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-008` |
| Title | Logic-to-Power interface bring-up and no spurious output enable |
| Linked IDs | `REQ-DCC-V-DK-011`, `REQ-DCC-V-DK-035`, `REQ-DCC-V-DK-113` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Establish Logic↔Power control/sense communication and prove outputs remain OFF unless commanded. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-001; TBD: TBD-DK-007; fixture: J_LP connection access; impl: RT+Power firmware supporting J_LP |
| Preconditions | A-003/A-004 complete or equivalent safe power+RT programmed; outputs uncommanded |
| Topology | Logic powered; Power powered via J_LP (IF-DK-JLP); no loads or loads open; scope/logic analyzer optional on SPI |
| Equipment | PSU; DMM on outputs; optional SPI capture |
| Hazards | Unexpected channel enable |
| Test configuration | Configuration with all outputs disabled/OFF |
| Stimuli | 1) Valid J_LP/SPI bring-up sequence as implemented 2) Optional: induce communication loss longer than TBD-DK-007 |
| Procedure | 1. Record baseline identity 2. Power Logic then Power per startup doc 3. Transmit documented link-init / status poll on J_LP 4. Observe expected status/response frame or documented ready indication within TBD-DK-007 5. Measure all represented channel outputs — must remain OFF 6. If loss test in scope: disconnect SPI/J_LP control path for > TBD-DK-007; confirm safe de-energize response 7. Restore link; confirm outputs still OFF until explicit command |
| Measurements | link response timestamp_ms; Vout_chN; fault flags |
| Expected result | Link response accepted; no channel ON; on loss, safe OFF per interface timeout |
| Pass criterion | (a) Documented ready/status response received within approved TBD-DK-007 AND (b) every represented channel remains OFF (electrical + diagnostic) throughout bring-up AND (c) if loss step executed, outputs remain/enter OFF with fault/loss indication recorded. |
| Abort criterion | Any spurious ON; thermal event |
| Evidence | SPI/status log; output measurement table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-009 — DCPI bring-up — valid exchange then CRC rejection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-009` |
| Title | DCPI bring-up — valid exchange then CRC rejection |
| Linked IDs | `REQ-DCC-V-DK-012`, `REQ-DCC-V-DK-067`, `REQ-DCC-V-DK-099` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Prove DCPI accepts valid integrity-checked frames and rejects corrupted frames without unsafe apply. |
| Status | `NOT EXECUTED` |
| Preconditions | RT and Service programmed; DCPI linked |
| Topology | Logic ↔ Radio via IF-DK-DCPI |
| Equipment | Optional SPI capture; Service/RT logs |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | N/A for basic exchange; no output-enable config apply during corruption step |
| Stimuli | Send ≥20 valid DCPI state/ping frames over ≥10 s; then inject ≥5 frames with corrupted CRC (bit-flip after CRC compute) |
| Procedure | 1. Start DCPI link 2. Exchange valid frames for ≥10 s (count ≥20) 3. Record accepted count and any error counters 4. Inject corrupted-CRC frames (≥5) 5. Confirm each corrupted frame is rejected (no CONFIG apply, no output enable) 6. Confirm error counter or diagnostic indication increments or equivalent observable rejection flag 7. Resume valid frames (≥5) and confirm acceptance resumes |
| Measurements | valid_accept_count; corrupt_reject_count; error_counter_or_flag; output states |
| Expected result | Valid frames accepted; corrupted rejected; outputs remain OFF |
| Pass criterion | valid_accept_count ≥ 20 over ≥10 s AND corrupt_reject_count ≥ 5 with zero successful apply of corrupted payload AND all represented outputs remain OFF. |
| Abort criterion | Corrupted frame accepted as valid config/command; any output ON |
| Evidence | DCPI log/capture; counters snapshot |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-010 — Real-Time startup to operable state with outputs OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-010` |
| Title | Real-Time startup to operable state with outputs OFF |
| Linked IDs | `REQ-DCC-V-DK-009`, `REQ-DCC-V-DK-059` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Observe RT startup reaches documented operable state with outputs OFF. |
| Status | `NOT EXECUTED` |
| Preconditions | RT programmed; safe power |
| Topology | DevKit powered; no loads |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Power cycle RT domain |
| Procedure | 1. Power cycle 2. Record time to documented READY/operable indication 3. Read diagnostic mode/state 4. Measure represented outputs |
| Measurements | t_ready_ms; state_enum; Vout_chN |
| Expected result | Operable/READY reached; outputs OFF |
| Pass criterion | Documented READY/operable state observed AND every represented channel OFF electrically and in diagnostics. |
| Abort criterion | Output ON during startup |
| Evidence | state log; measurement table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-011 — Watchdog fault forces safe outputs OFF within approved time

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-011` |
| Title | Watchdog fault forces safe outputs OFF within approved time |
| Linked IDs | `REQ-DCC-V-DK-038`, `REQ-DCC-V-DK-058` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Induce watchdog fault and measure time to outputs de-energized. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-007; TBD: TBD-DK-005; fixture: Safe WDT injection method; impl: — |
| Preconditions | Method to safely hang/starve WDT without uncontrolled hazards; outputs may be briefly commanded ON on a low-risk channel if needed to prove de-energize |
| Topology | DevKit powered; optional low-risk load on one channel only |
| Equipment | As required; models not mandated |
| Hazards | Unexpected channel behaviour during fault inject |
| Test configuration | — |
| Stimuli | Documented WDT starve/hang injection |
| Procedure | 1. Optionally command one low-risk channel ON and confirm ON 2. Inject WDT fault at t0 3. Measure time until that channel and all represented channels are OFF 4. Record reset/recovery behaviour |
| Measurements | t_off_ms from t0; output states |
| Expected result | All represented outputs OFF within TBD-DK-005 |
| Pass criterion | t_off_ms ≤ approved TBD-DK-005 for all represented channels. If TBD-DK-005 open: BLOCKED. |
| Abort criterion | Channel remains ON beyond abort timeout set by lab safety plan |
| Evidence | timing capture; log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-012 — Kill assertion de-energizes outputs; Service/UI cannot bypass

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-012` |
| Title | Kill assertion de-energizes outputs; Service/UI cannot bypass |
| Linked IDs | `REQ-DCC-V-DK-021`, `REQ-DCC-V-DK-031`, `REQ-DCC-V-DK-033`, `REQ-DCC-V-DK-036`, `REQ-DCC-V-DK-037` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Assert hardware kill; measure de-energize time; attempt Service/UI bypass. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-007; TBD: TBD-DK-004; fixture: —; impl: — |
| Preconditions | Kill input accessible; Service path available for negative test |
| Topology | Kill switch → IF-DK-KILL; optional low-risk load |
| Equipment | As required; models not mandated |
| Hazards | High current if kill fails |
| Test configuration | — |
| Stimuli | Assert kill at t0; while asserted, send Service/REST/UI output-ON commands |
| Procedure | 1. Optionally turn one low-risk channel ON 2. Assert kill at t0 3. Measure time to all represented outputs OFF 4. While kill asserted, send ≥3 unauthorized/authorized Service ON commands 5. Confirm outputs remain OFF 6. De-assert kill; confirm outputs remain OFF until explicit re-enable (see A-14) |
| Measurements | t_off_ms; bypass_command_results; output states |
| Expected result | Outputs OFF within TBD-DK-004; bypass commands do not energize |
| Pass criterion | t_off_ms ≤ approved TBD-DK-004 AND zero successful energizations from Service/UI while kill asserted. If TBD-DK-004 open: BLOCKED. |
| Abort criterion | Any output remains ON after kill beyond lab abort limit |
| Evidence | timing log; API/command log; output table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-013 — Global enable observability

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-013` |
| Title | Global enable observability |
| Linked IDs | `REQ-DCC-V-DK-032` |
| Method | Demonstration |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Show global enable state via documented diagnostic or measurement path. |
| Status | `NOT EXECUTED` |
| Setup state | DevKit powered; documented enable observation path available |
| Procedure | 1. Read enable state via documented path (diag field or probe point) 2. Toggle enable if safe/procedure allows, or observe both documented states across reset 3. Record values |
| Expected observable | Tester can read enable state unambiguously |
| Pass criterion | Enable-state value is read from the documented observation path; record (a) path identifier, (b) observed value, and (c) either one commanded state transition with before/after values or one steady state held ≥5 s with constant value. |
| Evidence | screenshot/log or meter reading with path ID |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-014 — Safe reset and post-kill outputs remain OFF until explicit re-enable

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-014` |
| Title | Safe reset and post-kill outputs remain OFF until explicit re-enable |
| Linked IDs | `REQ-DCC-V-DK-034`, `REQ-DCC-V-DK-060`, `REQ-DCC-V-DK-101` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | After kill clear/reset, outputs remain OFF until documented re-enable sequence. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-021; fixture: —; impl: — |
| Preconditions | Kill and reset paths available |
| Topology | As A-12 |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Kill assert/deassert; safe reset command/power cycle as documented |
| Procedure | 1. Assert kill; confirm OFF 2. De-assert kill 3. Confirm outputs still OFF 4. Perform safe reset 5. Confirm outputs OFF and state known 6. Execute documented re-enable sequence 7. Only then allow a single low-risk ON command to prove re-enable works 8. Command OFF |
| Measurements | states after each step |
| Expected result | No auto re-energize; re-enable required |
| Pass criterion | After kill de-assert and after reset, all represented outputs remain OFF until the documented re-enable sequence is completed; one controlled ON succeeds only after that sequence. If re-enable sequence undefined (TBD-DK-021): BLOCKED. |
| Abort criterion | Auto ON without re-enable |
| Evidence | step log; output table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-015 — BOARD_ID / hardware revision observability when implemented

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-015` |
| Title | BOARD_ID / hardware revision observability when implemented |
| Linked IDs | `REQ-DCC-V-DK-017` |
| Method | Test |
| Gate | DK-A |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | If BOARD_ID sensing is implemented, record observed value; mapping may remain TBD. |
| Status | `BLOCKED` |
| Notes | Condition: BOARD_ID readout feature present in tested baseline. If not implemented: DEFERRED_EXCLUDED with statement. |
| Blocked by | ADR: —; TBD: TBD-DK-020; fixture: —; impl: BOARD_ID readout |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Determine if BOARD_ID readout exists in tested build 2. If no: mark DEFERRED_EXCLUDED for this baseline 3. If yes: read BOARD_ID; record raw value; record mapping status TBD-DK-020 |
| Measurements | — |
| Expected result | — |
| Pass criterion | If feature present: raw BOARD_ID recorded. Mapping not required for this case PASS. If feature absent: case classified DEFERRED_EXCLUDED (not PASS). |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | diag readout |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-016 — Default OFF across all represented channels after reset

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-016` |
| Title | Default OFF across all represented channels after reset |
| Linked IDs | `REQ-DCC-V-DK-023`, `REQ-DCC-V-DK-050` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | After reset, every represented channel is OFF. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-014; fixture: —; impl: — |
| Preconditions | Represented channel inventory signed (C-001 or interim list) |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Reset to known state 2. For each represented channel measure output and read diagnostic state |
| Measurements | per-channel Vout and state |
| Expected result | — |
| Pass criterion | 100% of represented channels OFF by measurement and diagnostics. Timing to OFF after command uses TBD-DK-014 when commanding OFF in related cases. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | channel table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-A-017 — Logic/Radio reuse constraint documentation (blocked fidelity)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-017` |
| Title | Logic/Radio reuse constraint documentation (blocked fidelity) |
| Linked IDs | `REQ-DCC-V-DK-114` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Confirm REQ-114 remains Blocked pending ADR-DK-001/002 and is not silently assumed. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | DevKit_System_Requirements.md REQ-114; gap assessment ADR-DK-001/002 |
| Checklist | REQ-114 status Blocked; ADR-DK-001/002 referenced; No document claims physical board identity is decided |
| Pass criterion | All checklist items true. |
| Evidence to retain | inspection note |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

### 3.B — Phase B: Communication and service

#### VER-DCC-DK-B-001 — DCP HEARTBEAT observation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-001` |
| Title | DCP HEARTBEAT observation |
| Linked IDs | `REQ-DCC-V-DK-075`, `REQ-DCC-V-DK-081`, `REQ-DCC-V-DK-098` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Observe DCC HEARTBEAT on the Gen1 CAN FD bus using tester capture access. |
| Status | `NOT EXECUTED` |
| Preconditions | DK-A bring-up complete; RT programmed; CAN sniffer/capture attached to IF-DK-CAN; bus terminated per B-005 intent |
| Topology | DevKit CAN ↔ linear stub to sniffer; ECU/Button Box simulators may be silent |
| Equipment | CAN FD sniffer; PSU |
| Hazards | Bus contention if multiple transmitters misconfigured |
| Test configuration | Default safe config; outputs OFF |
| Stimuli | Power DevKit to operable state; do not require ECU sim for this case |
| Procedure | 1. Connect sniffer; start capture 2. Energize DevKit to READY/operable 3. Capture ≥10 s of bus traffic 4. Identify DCC HEARTBEAT frames (node/ID per docs/004 when defined; otherwise record observed ID and mark protocol-ID TBD) 5. Compute inter-frame period statistics (min/mean/max) 6. Confirm sniffer access remained available (REQ-098) |
| Measurements | heartbeat_count; period_ms_min/mean/max; can_id_observed |
| Expected result | HEARTBEAT present with stable period record |
| Pass criterion | ≥1 HEARTBEAT frame observed in each of ≥10 consecutive 1 s windows OR ≥10 frames over ≥10 s with period_ms_mean recorded; sniffer capture file retained. If HEARTBEAT ID/layout undefined in Accepted protocol baseline: status BLOCKED (do not invent ID). |
| Abort criterion | Bus storm; unintended output enable |
| Evidence | candump/pcap; period table; baseline identity |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-002 — ECU simulator telemetry reception

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-002` |
| Title | ECU simulator telemetry reception |
| Linked IDs | `REQ-DCC-V-DK-077` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Transmit ECU simulator telemetry on CAN and confirm DCC receives/consumes it (diagnostic or VCM input path). |
| Status | `NOT EXECUTED` |
| Preconditions | B-001 path available; ECU simulator tool connected to IF-DK-CAN |
| Topology | ECU sim ↔ CAN ↔ DevKit; sniffer optional tap |
| Equipment | ECU simulator; CAN sniffer; PSU |
| Hazards | Case-specific electrical as applicable |
| Test configuration | CFG-DK-ECU-TELEM-01 (or documented equivalent) enabling ECU telem consumption |
| Stimuli | Stream ENGINE_TELEM (or documented ECU telem message) at defined rate for ≥10 s with known payload values |
| Procedure | 1. Start sniffer 2. Start ECU sim telem with recorded payload set P1 3. Confirm DevKit diagnostic/API/VCM input shows matching received values within documented scaling 4. Change payload to P2 mid-stream 5. Confirm observed values update to P2 6. Stop sim (lost handling is B-003) |
| Measurements | telem_rx_count; value_match P1/P2; latency_ms if available |
| Expected result | P1 then P2 observed on DevKit receive path |
| Pass criterion | DevKit-observed telemetry matches P1 then P2 for each required signal in CFG-DK-ECU-TELEM-01 within documented scaling tolerance; ≥10 s continuous reception without requiring Service domain for RT acceptance. If message ID/layout undefined: BLOCKED. |
| Abort criterion | Unintended output enable |
| Evidence | sim script; sniffer log; DevKit diagnostic snapshot |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

### VER-DCC-DK-B-003 — Stale/lost ECU node handling

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-003` |
| Title | Stale/lost ECU node handling |
| Linked IDs | `REQ-DCC-V-DK-079` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Stop ECU sim and observe lost/stale indication after approved timeout. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-006; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Stop ENGINE_TELEM at t0 after valid stream |
| Procedure | 1. Establish valid telem 2. Stop sim at t0 3. Poll DCC ecu status until LOST/stale or timeout window ends |
| Measurements | t_lost_ms |
| Expected result | — |
| Pass criterion | Lost/stale indication true at t_lost_ms where approved TBD-DK-006 ≤ t_lost_ms ≤ TBD-DK-006 + documented tolerance. If TBD-DK-006 open: BLOCKED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | timeline log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-004 — Button Box event simulation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-004` |
| Title | Button Box event simulation |
| Linked IDs | `REQ-DCC-V-DK-078` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Inject a Button Box DCP event and observe configured response. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | Test profile CFG-DK-BB-01 mapping a specific control_id to a low-risk output or logged event |
| Stimuli | Single Button Box EVENT with control_id=CFG-DK-BB-01.id |
| Procedure | 1. Load CFG-DK-BB-01 2. Confirm target output OFF 3. Inject event 4. Observe expected output or event log entry within 1 s |
| Measurements | — |
| Expected result | — |
| Pass criterion | Expected effect defined in CFG-DK-BB-01 expected-results table occurs exactly once and is logged with timestamp. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | sim frame; event log; output state |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-005 — CAN termination presence inspection and waveform metrics

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-005` |
| Title | CAN termination presence inspection and waveform metrics |
| Linked IDs | `REQ-DCC-V-DK-076` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Confirm termination installation and record waveform metrics against TBD-DK-015. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-015; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Inspect termination resistors presence/location per topology 2. Capture differential CAN waveform during HEARTBEAT 3. Measure metrics required by TBD-DK-015 when defined |
| Measurements | — |
| Expected result | — |
| Pass criterion | Termination inspection PASS AND waveform metrics meet approved TBD-DK-015. If TBD-DK-015 open: BLOCKED (inspection alone cannot PASS integrity claim). |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | photo of terminators; scope capture |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-006 — DCPI sustained valid transfer

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-006` |
| Title | DCPI sustained valid transfer |
| Linked IDs | `REQ-DCC-V-DK-012`, `REQ-DCC-V-DK-067` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Sustain valid DCPI transfers for a defined duration. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Valid DCPI traffic for 60 s |
| Procedure | 1. Link up 2. Run 60 s 3. Count CRC errors |
| Measurements | duration_s; crc_error_count; frames |
| Expected result | — |
| Pass criterion | duration ≥ 60 s AND crc_error_count == 0 for valid traffic AND frames ≥ 100. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | transfer log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-007 — Configuration transfer apply and recovery docs

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-007` |
| Title | Configuration transfer apply and recovery docs |
| Linked IDs | `REQ-DCC-V-DK-068`, `REQ-DCC-V-DK-083`, `REQ-DCC-V-DK-089`, `REQ-DCC-V-DK-118` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Deliver valid DevKit DCFG/profile and confirm apply ack; confirm recovery doc exists. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | CFG-DK-VALID-01 compiled to DCFG with format version field present |
| Stimuli | — |
| Procedure | 1. Inspect recovery/rollback doc exists 2. Transfer CFG-DK-VALID-01 3. Observe apply ACK 4. Read back active config ID |
| Measurements | — |
| Expected result | — |
| Pass criterion | Apply ACK success AND active configuration_id == CFG-DK-VALID-01 AND DCFG version field present AND recovery procedure document path recorded. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | transfer log; doc path |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-008 — DCPI corrupted frame rejection during config path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-008` |
| Title | DCPI corrupted frame rejection during config path |
| Linked IDs | `REQ-DCC-V-DK-099` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Reject corrupted DCPI config frames. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | CONFIG frame with inverted CRC |
| Procedure | 1. Note active config 2. Send corrupted CONFIG 3. Confirm reject 4. Confirm active config unchanged 5. Confirm outputs unchanged |
| Measurements | — |
| Expected result | — |
| Pass criterion | Corrupted CONFIG rejected AND active configuration_id unchanged AND no represented output changes state. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | DCPI log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-009 — Diagnostic event visibility via Service path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-009` |
| Title | Diagnostic event visibility via Service path |
| Linked IDs | `REQ-DCC-V-DK-051`, `REQ-DCC-V-DK-069`, `REQ-DCC-V-DK-097` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Generate a known fault/event and observe it on Service diagnostics. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | Documented test fault or OUTPUT_TEST generating EVENT |
| Procedure | 1. Clear/observe baseline 2. Inject event 3. Read Service diagnostic/logger API or UI feed |
| Measurements | — |
| Expected result | — |
| Pass criterion | Event with expected type/code appears on Service path with timestamp within 2 s of injection. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | event record |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-010 — REST status identity/health fields

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-010` |
| Title | REST status identity/health fields |
| Linked IDs | `REQ-DCC-V-DK-070` |
| Method | Test |
| Gate | DK-B |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | GET /status returns required identity/health fields when REST is in baseline scope. |
| Status | `NOT EXECUTED` |
| Notes | Condition: REST included in tested DevKit Service baseline. Else DEFERRED_EXCLUDED. |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Determine REST in scope 2. GET /status 3. Validate required fields per docs/006 list cited in record |
| Measurements | — |
| Expected result | — |
| Pass criterion | HTTP 200 AND each required field present and non-empty per cited docs/006 list. If REST out of scope: DEFERRED_EXCLUDED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | HTTP response body |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-011 — WebSocket telemetry availability and loss metrics

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-011` |
| Title | WebSocket telemetry availability and loss metrics |
| Linked IDs | `REQ-DCC-V-DK-071` |
| Method | Test |
| Gate | DK-B |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Subscribe telemetry and measure loss against TBD-DK-016. |
| Status | `BLOCKED` |
| Notes | Condition: WS in baseline scope. |
| Blocked by | ADR: —; TBD: TBD-DK-016; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Subscribe 2. Run duration 3. Compute loss |
| Measurements | — |
| Expected result | — |
| Pass criterion | Meets approved TBD-DK-016. If open: BLOCKED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | WS capture stats |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-012 — Unauthorized outputs API rejected

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-012` |
| Title | Unauthorized outputs API rejected |
| Linked IDs | `REQ-DCC-V-DK-037` |
| Method | Test |
| Gate | DK-B |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | POST outputs without auth rejected when auth model applies. |
| Status | `NOT EXECUTED` |
| Notes | Condition: REST auth model in baseline (EDL-013). |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Ensure no token 2. POST /outputs enable 3. Expect 401/403 per docs/006 |
| Measurements | — |
| Expected result | — |
| Pass criterion | Request denied with documented unauthorized status AND no output state change. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | HTTP log; output state |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-013 — Service commands cannot bypass asserted kill

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-013` |
| Title | Service commands cannot bypass asserted kill |
| Linked IDs | `REQ-DCC-V-DK-037` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | With kill asserted, Service ON commands fail to energize outputs. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Assert kill 2. Send authenticated ON if possible 3. Measure outputs |
| Measurements | — |
| Expected result | — |
| Pass criterion | All represented outputs remain OFF during ≥3 ON attempts. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | command log; measurements |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-014 — OTA gate-scope classification check

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-014` |
| Title | OTA gate-scope classification check |
| Linked IDs | `DK-GOV-010` |
| Method | Inspection |
| Gate | DK-B |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Classify OTA case per DK-GOV-010 / ADR-DK-008; do not execute OTA as mandatory without ADR. |
| Status | `BLOCKED` |
| Notes | Maps formerly to governance; keep inspection of scope. Prefer VER-DCC-DK-G for pure gov — retained as conditional gate scope check. |
| Blocked by | ADR: ADR-DK-008; TBD: —; fixture: —; impl: — |
| Artifacts inspected | DK-GOV-010; ADR-DK-008 status |
| Checklist | OTA not silently marked MANDATORY; Classification matches ADR state |
| Pass criterion | Classification recorded consistently with ADR-DK-008. Until ADR exists: case BLOCKED for mandatory OTA execution claims. |
| Evidence to retain | classification record |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-B-015 — Protocol version fields recorded without invented mapping

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-015` |
| Title | Protocol version fields recorded without invented mapping |
| Linked IDs | `REQ-DCC-V-DK-089` |
| Method | Inspection |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Record DCFG/DCP/DCPI version fields as raw/semantic without inventing mappings. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | baseline sheet; proto.h / runtime readout |
| Checklist | Legacy encoded values labelled legacy; No 0x01=MAJOR.MINOR claim |
| Pass criterion | Checklist PASS. |
| Evidence to retain | baseline sheet |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

### 3.C — Phase C: Representative power capability

#### VER-DCC-DK-C-001 — Represented channel inventory and coverage declaration

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-001` |
| Title | Represented channel inventory and coverage declaration |
| Linked IDs | `REQ-DCC-V-DK-014`, `REQ-DCC-V-DK-039`, `REQ-DCC-V-DK-041`, `REQ-DCC-V-DK-102`, `REQ-DCC-V-DK-116` |
| Method | Analysis |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Produce a signed inventory of represented vs excluded channel capabilities for the tested baseline. |
| Status | `NOT EXECUTED` |
| Inputs | Hardware as-built channel list; ADR-DK-004/005 status; required capability categories from active power-channel requirements |
| Assumptions | Unrepresented classes are excluded from DK-C coverage claims; no MPN inferred as capability proof |
| Calculation or comparison method | Compare each as-built physical channel ID to required capability categories (HS/PWM/BD/etc.); mark each category Represented (with channel ID) or DEFERRED_EXCLUDED (with rationale) |
| Equations or tool | Coverage matrix spreadsheet or equivalent controlled table; no thermal derating calculation required for this case |
| Acceptance rule | Signed coverage matrix lists every applicable capability category as Represented or DEFERRED_EXCLUDED; every Represented claim cites a physical channel ID; no Represented claim without hardware |
| Uncertainty or unresolved input treatment | If ADR-DK-004 leaves a category undecided, mark that category BLOCKED for representation decision (gate cannot claim coverage) |
| Pass criterion | Signed coverage matrix complete per acceptance rule; excluded capabilities explicitly listed for the gate statement. |
| Evidence | Signed coverage matrix; ADR-DK-004/005 citations |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-002 — High-side channel normal ON/OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-002` |
| Title | High-side channel normal ON/OFF |
| Linked IDs | `REQ-DCC-V-DK-039`, `REQ-DCC-V-DK-050`, `REQ-DCC-V-DK-026` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Command a represented HS channel ON then OFF with safe load. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-014; fixture: —; impl: — |
| Preconditions | Load connected only while channel commanded OFF (REQ-026) |
| Topology | Selected HS channel → safe load; meter/shunt in series |
| Equipment | As required; models not mandated |
| Hazards | Load heating |
| Test configuration | Wiring/test mode authorized |
| Stimuli | ON command; wait; OFF command |
| Procedure | 1. Connect load while OFF 2. Command ON 3. Measure V/I and diag ON 4. Command OFF at t0 5. Measure t_off |
| Measurements | I_load; Vout; t_off_ms; diag state |
| Expected result | — |
| Pass criterion | Diag+electrical ON while commanded ON; after OFF, channel OFF with t_off_ms ≤ TBD-DK-014 when approved. If TBD-DK-014 open: BLOCKED. |
| Abort criterion | Uncontrolled current |
| Evidence | scope/meter log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-003 — PWM channel behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-003` |
| Title | PWM channel behaviour |
| Linked IDs | `REQ-DCC-V-DK-040` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | PWM output within approved frequency range. |
| Status | `BLOCKED` |
| Notes | Condition: PWM-capable channel represented and in DK-C scope. |
| Blocked by | ADR: —; TBD: TBD-DK-008; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Command PWM 50% 2. Measure frequency/duty |
| Measurements | f_Hz; duty_% |
| Expected result | — |
| Pass criterion | Measured frequency within TBD-DK-008 at commanded duty 50%. If TBD open: BLOCKED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | scope capture |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-004 — Current observation path cross-check

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-004` |
| Title | Current observation path cross-check |
| Linked IDs | `REQ-DCC-V-DK-043`, `REQ-DCC-V-DK-095`, `REQ-DCC-V-DK-051` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Compare physical current measurement to diagnostic current readout. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-009; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Command ON into known load 2. Measure shunt/clamp current 3. Read diag current 4. Compute error |
| Measurements | — |
| Expected result | — |
| Pass criterion | |I_diag - I_meter| within approved TBD-DK-009. If open: record both values; case BLOCKED for accuracy PASS. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | measurement table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-005 — Overcurrent reaction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-005` |
| Title | Overcurrent reaction |
| Linked IDs | `REQ-DCC-V-DK-044`, `REQ-DCC-V-DK-100` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Controlled overcurrent causes protect/OFF and observable fault. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-010; TBD: TBD-DK-011; fixture: overcurrent fixture; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Arm fixture 2. Command ON 3. Apply overcurrent 4. Capture t_protect and fault flag |
| Measurements | — |
| Expected result | — |
| Pass criterion | Channel enters protected/OFF AND fault OVERCURRENT (or documented code) true AND t_protect within approved limit when defined. |
| Abort criterion | Fixture unsafe |
| Evidence | fault log; timing |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-006 — Short-circuit reaction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-006` |
| Title | Short-circuit reaction |
| Linked IDs | `REQ-DCC-V-DK-045`, `REQ-DCC-V-DK-100` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Controlled short causes safe protected state and fault. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-010; TBD: —; fixture: safe short fixture; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Verify fixture approved 2. Apply short under procedure 3. Record response |
| Measurements | — |
| Expected result | — |
| Pass criterion | Protected/OFF + short fault indication; no persistent hazardous current. |
| Abort criterion | Uncontrolled fault energy |
| Evidence | log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-007 — Open-load indication where supported

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-007` |
| Title | Open-load indication where supported |
| Linked IDs | `REQ-DCC-V-DK-046` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Open-load fault visible if implementation claims support. |
| Status | `NOT EXECUTED` |
| Notes | Condition: selected channel claims open-load detection. |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Check claim 2. If no: DEFERRED_EXCLUDED 3. If yes: open load and read fault |
| Measurements | — |
| Expected result | — |
| Pass criterion | If claimed: open-load fault true within documented latency. If not claimed: DEFERRED_EXCLUDED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | diag |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-008 — Undervoltage behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-008` |
| Title | Undervoltage behaviour |
| Linked IDs | `REQ-DCC-V-DK-047` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Reduce supply to approved UV threshold and observe defined behaviour. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-012; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Set Vin to UV procedure 2. Observe lockout/fault |
| Measurements | — |
| Expected result | — |
| Pass criterion | When Vin is reduced to the approved undervoltage stimulus in TBD-DK-012, observed output/diagnostic states equal the approved reaction table in TBD-DK-012 (including timing if specified). If TBD-DK-012 open: BLOCKED. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | PSU log; fault |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-009 — Thermal observation path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-009` |
| Title | Thermal observation path |
| Linked IDs | `REQ-DCC-V-DK-048`, `REQ-DCC-V-DK-096` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Record temperature sense during loaded run. |
| Status | `BLOCKED` |
| Notes | Condition: thermal observation required for represented protection. |
| Blocked by | ADR: ADR-DK-011; TBD: TBD-DK-010, TBD-DK-018, TBD-DK-019; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Run load 2. Log temperature |
| Measurements | — |
| Expected result | — |
| Pass criterion | Temperature samples recorded at ≥1 Hz for approved duration. Absolute limit PASS only if TBD-DK-019 approved. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | temp CSV |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-010 — Bidirectional forward and reverse direction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-010` |
| Title | Bidirectional forward and reverse direction |
| Linked IDs | `REQ-DCC-V-DK-042`, `REQ-DCC-V-DK-054` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Command forward then reverse; confirm direction; no conflicting drive. |
| Status | `NOT EXECUTED` |
| Supersession | Supersedes stall portion of prior compound C-010 |
| Notes | Condition: bidirectional channel represented. Stall is separate case C-013. |
| Preconditions | — |
| Topology | BD channel → safe motor/load |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Command forward 2 s 2. Coast/OFF per config 3. Command reverse 2 s 4. Attempt conflicting drive command sequence 5. Confirm prevention |
| Measurements | direction indicator or back-EMF/current signature; fault flags |
| Expected result | — |
| Pass criterion | Forward command produces forward direction signature; reverse produces reverse; conflicting command does not produce simultaneous opposing drive (fault or rejection recorded). |
| Abort criterion | Shoot-through suspicion |
| Evidence | video/log; current waveform |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-011 — Conflicting bridge command prevention (dedicated)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-011` |
| Title | Conflicting bridge command prevention (dedicated) |
| Linked IDs | `REQ-DCC-V-DK-054` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Attempt simultaneous opposing drive; confirm prevention. |
| Status | `NOT EXECUTED` |
| Notes | Condition: BD represented. May be combined evidence with C-010 but separate status. |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Issue conflicting commands via test API 2. Observe driver enables/fault |
| Measurements | — |
| Expected result | — |
| Pass criterion | No simultaneous opposing enable measured; rejection/fault recorded. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | logic capture |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-012 — Logic-to-Power control-loss safe OFF

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-012` |
| Title | Logic-to-Power control-loss safe OFF |
| Linked IDs | `REQ-DCC-V-DK-035` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | On J_LP/control-path loss beyond the approved timeout, all represented outputs enter/remain safe OFF. |
| Status | `BLOCKED` |
| Supersession | Split from prior compound C-012; retry/latch is C-014 |
| Blocked by | ADR: —; TBD: TBD-DK-007; fixture: controllable J_LP/SPI disconnect; impl: RT+Power timeout handler |
| Preconditions | Channel capable of brief ON on one low-risk represented channel; loads connected only while OFF then commanded |
| Topology | Logic ↔ Power via IF-DK-JLP; series switch or connector break on control path; DMM/shunt on low-risk channel |
| Equipment | Controllable disconnect; timer/log sync; PSU |
| Hazards | Unexpected sustained drive after disconnect |
| Test configuration | CFG-DK-CTRL-LOSS-01 authorizing one low-risk channel |
| Stimuli | Command low-risk channel ON; at t0 open J_LP control path (SPI/CS/documented control lines) for duration > TBD-DK-007 |
| Procedure | 1. Record baseline 2. Command low-risk channel ON; confirm ON electrically 3. At t0 disconnect control path 4. Sample output until OFF 5. Record fault/loss indication 6. Restore control path 7. Confirm outputs remain OFF until explicit re-enable command |
| Measurements | t_off_ms from t0; Vout/I; fault flag timestamp |
| Expected result | Outputs OFF within approved timeout; no auto re-enable on link restore |
| Pass criterion | t_off_ms ≤ approved TBD-DK-007 (+ documented tolerance) AND all represented channels OFF AND fault/loss indication recorded AND no auto ON on restore. If TBD-DK-007 open: BLOCKED. |
| Abort criterion | Output remains ON beyond 2× provisional EDL-011 intent discussion without approved TBD — stop and safe-OFF; smoke |
| Evidence | timing log; output table; fault snapshot |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-013 — Bidirectional stall / locked-rotor response

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-013` |
| Title | Bidirectional stall / locked-rotor response |
| Linked IDs | `REQ-DCC-V-DK-055` |
| Method | Test |
| Gate | DK-C |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | With a stall/locked-rotor fixture, confirm the documented protect response. |
| Status | `BLOCKED` |
| Notes | Condition: bidirectional channel physically represented AND stall verification included in tested baseline. Else DEFERRED_EXCLUDED. |
| Blocked by | ADR: —; TBD: TBD-DK-022; fixture: stall/locked-rotor fixture; impl: stall detect/protect path |
| Preconditions | C-010 direction check available or equivalent BD channel commissioned; stall fixture rated for test |
| Topology | BD channel → stall fixture (locked rotor or equivalent); current sense |
| Equipment | Stall fixture; current probe; PSU |
| Hazards | Motor/driver thermal event; fixture mechanical hazard |
| Test configuration | CFG-DK-BD-STALL-01 |
| Stimuli | Command forward (or reverse) into stall fixture at t0 |
| Procedure | 1. Confirm fixture locked 2. Command drive at t0 3. Capture current waveform and fault flags until protect/OFF 4. Record t_protect_ms and peak current 5. Confirm latched or held safe state per TBD-DK-022 6. Clear per documented sequence |
| Measurements | I_peak; t_protect_ms; fault code; output state |
| Expected result | Protect/OFF within approved stall criteria |
| Pass criterion | Meets approved TBD-DK-022 numeric criteria (current and/or time and required fault state). If TBD or fixture missing: BLOCKED (not qualitative PASS). |
| Abort criterion | Uncontrolled current; fixture failure; temperature beyond approved limit |
| Evidence | current waveform; fault log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-C-014 — Fault retry and latch behaviour

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-C-014` |
| Title | Fault retry and latch behaviour |
| Linked IDs | `REQ-DCC-V-DK-049` |
| Method | Test |
| Gate | DK-C |
| Classification | `MANDATORY` |
| Objective | Confirm recoverable faults retry N times then latch per approved policy. |
| Status | `BLOCKED` |
| Supersession | Split from prior compound C-012 |
| Blocked by | ADR: —; TBD: TBD-DK-013; fixture: recoverable fault injection method; impl: retry/latch policy |
| Preconditions | Documented recoverable fault injection that does not require unresolved overcurrent ADR if a milder recoverable fault exists; else blocked with C-005 dependency noted |
| Topology | Selected channel + fault fixture; diagnostic path |
| Equipment | Fault fixture; logs |
| Hazards | Escalating thermal if retries continue unexpectedly |
| Test configuration | CFG-DK-RETRY-01 with recorded retry_count_max and retry_delay |
| Stimuli | Inject the same recoverable fault condition repeatedly |
| Procedure | 1. Clear faults 2. Inject fault #1; observe retry/OFF/re-attempt 3. Repeat until retry_count_max 4. Confirm latch (no further auto ON) 5. Perform documented clear sequence 6. Confirm channel can be commanded again only after clear |
| Measurements | retry_attempt_count; retry_delay_ms; latch_state; clear_result |
| Expected result | Retries then latch per policy |
| Pass criterion | retry_attempt_count equals approved TBD-DK-013 max AND latch prevents further auto ON AND clear sequence restores commandability. If TBD-DK-013 open: BLOCKED. |
| Abort criterion | Retries exceed 2× expected without latch; smoke; uncontrolled current |
| Evidence | fault timeline CSV; config identity |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

### 3.D — Phase D: System integration

#### VER-DCC-DK-D-002 — VCM mode transition sequence

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-002` |
| Title | VCM mode transition sequence |
| Linked IDs | `REQ-DCC-V-DK-062` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Execute a defined VCM transition sequence with required and disallowed transitions. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | CFG-DK-VCM-01 defining modes OFF → READY → ENGINE_RUN (names per profile) |
| Stimuli | Documented input events/telemetry for each transition |
| Procedure | 1. Reset to OFF 2. Apply event E1 expecting OFF→READY; record mode+timestamp 3. Apply event E2 expecting READY→ENGINE_RUN 4. Apply disallowed event E_bad expecting no transition 5. Export event log fields: mode_from, mode_to, reason, timestamp |
| Measurements | — |
| Expected result | — |
| Pass criterion | Observed sequence equals [OFF→READY, READY→ENGINE_RUN]; E_bad produces zero mode change; each required transition appears in event log with mode_from/mode_to/timestamp. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | event log JSON; mode timeline |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-003 — Configuration-driven behaviour with two config variants

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-003` |
| Title | Configuration-driven behaviour with two config variants |
| Linked IDs | `REQ-DCC-V-DK-013`, `REQ-DCC-V-DK-061`, `REQ-DCC-V-DK-086` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Prove output behaviour changes with configuration while firmware identity is held constant. |
| Status | `NOT EXECUTED` |
| Preconditions | Same RT firmware image identity for entire case; two compiled/config records available |
| Topology | DevKit + one low-risk represented channel + safe load; Service/config path |
| Equipment | Config transfer tool; meter; logs |
| Hazards | Unexpected channel mapping |
| Test configuration | CFG-DK-VAR-A: channel CH_X function mapping F_A (e.g. enable on event EA); CFG-DK-VAR-B: same CH_X mapping F_B differing from F_A (e.g. enable on event EB or inverted polarity/policy). Record both config IDs/hashes. |
| Stimuli | Apply identical firmware; load CFG-DK-VAR-A; apply stimulus S_A expecting ON and S_B expecting OFF; then load CFG-DK-VAR-B without firmware rebuild; repeat S_A/S_B with expected inverted/different table |
| Procedure | 1. Record firmware identity (commit SHA / artifact) 2. Apply CFG-DK-VAR-A; confirm config identity accepted 3. Apply S_A; measure CH_X ON 4. Apply S_B; measure CH_X OFF (per VAR-A table) 5. Apply CFG-DK-VAR-B; confirm config identity changed; firmware identity unchanged 6. Apply S_A; measure per VAR-B table 7. Apply S_B; measure per VAR-B table 8. Export evidence proving firmware identity constant |
| Measurements | Vout/I for CH_X per step; firmware identity; config identity |
| Expected result | Behaviour follows active config table; firmware identity unchanged across steps 5–7 |
| Pass criterion | Results match the VAR-A expected-output table then the VAR-B expected-output table AND firmware identity fields equal across both variants AND config identities differ. |
| Abort criterion | Spurious ON on unintended channel |
| Evidence | config IDs; firmware identity; output table; transfer logs |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-004 — ECU simulation integration scenario

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-004` |
| Title | ECU simulation integration scenario |
| Linked IDs | `REQ-DCC-V-DK-077`, `REQ-DCC-V-DK-086` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Execute a scripted ECU DCP scenario and confirm VCM/output/event response including stale-node handling where applicable. |
| Status | `NOT EXECUTED` |
| Preconditions | B-002 path available; VCM profile loaded |
| Topology | ECU sim ↔ CAN ↔ DevKit; sniffer tap; optional low-risk load |
| Equipment | ECU sim; sniffer; logs |
| Hazards | Rule-driven unexpected load enable — use low-risk channel only |
| Test configuration | CFG-DK-SCEN-ECU-01 with initial VCM mode OFF; rule R1: on coolant_temp ≥ T_th (documented test threshold) enable CH_COOL; stale ECU → inhibit new enable per TBD-DK-006 |
| Stimuli | DCP messages: HEARTBEAT peer optional; ENGINE_TELEM coolant_temp sequence: T_low for 5 s, then T_high≥T_th for 10 s at period P; then stop telem at t_stop |
| Procedure | 1. Reset to VCM OFF/READY per profile 2. Start telem at T_low; confirm CH_COOL remains OFF 3. Raise to T_high; confirm rule R1 enables CH_COOL within documented response window 4. Log events (mode, rule, output) 5. Stop ECU telem at t_stop 6. Observe stale/LOST handling per TBD-DK-006 (no new enable; required inhibit/safe action) 7. Export scenario log |
| Measurements | coolant_temp timeline; CH_COOL state; t_enable_ms; t_stale_ms; event fields |
| Expected result | OFF at T_low; ON at T_high per R1; stale handling per rules |
| Pass criterion | Scenario log contains: timestamps; DCP message IDs/values used; VCM mode; CH_COOL OFF then ON per R1; stale/LOST indication after t_stop with required inhibit; allowed deviations only as listed in CFG-DK-SCEN-ECU-01. If TBD-DK-006 required for stale step and open: case BLOCKED. |
| Abort criterion | Unintended multi-channel enable |
| Evidence | scenario log JSON; sniffer; config identity |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-005 — Representative cooling/load rule execution

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-005` |
| Title | Representative cooling/load rule execution |
| Linked IDs | `REQ-DCC-V-DK-086` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Execute one documented rule from CFG-DK-RULE-01. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | CFG-DK-RULE-01 with threshold T_on from config (not invented) |
| Stimuli | Simulated coolant_temp from T_on-5 to T_on+5 |
| Procedure | 1. Load config 2. Ramp temp 3. Observe fan/output at crossings |
| Measurements | — |
| Expected result | — |
| Pass criterion | Output turns ON when temp crosses configured T_on upward; turns OFF per configured off rule; thresholds used equal config values. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | telemetry; output log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-006 — Button Box integration scenario

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-006` |
| Title | Button Box integration scenario |
| Linked IDs | `REQ-DCC-V-DK-078` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Integrated Button Box event changes output per CFG-DK-BB-02. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | CFG-DK-BB-02 |
| Stimuli | Long-press/event as defined in CFG-DK-BB-02 |
| Procedure | 1. Apply config 2. Inject event 3. Compare to expected-results table |
| Measurements | — |
| Expected result | — |
| Pass criterion | Actual outputs/events equal CFG-DK-BB-02 expected-results table row for that event. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | logs |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-012 — Service restart isolation for fail-operational output

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-012` |
| Title | Service restart isolation for fail-operational output |
| Linked IDs | `REQ-DCC-V-DK-018`, `REQ-DCC-V-DK-065`, `REQ-DCC-V-DK-072`, `REQ-DCC-V-DK-010` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Service restart does not force RT fail-operational output OFF. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Enable fail-op output via RT path 2. Confirm ON 3. Restart Service (power cycle Radio or reboot cmd) 4. Monitor output during restart window 10 s |
| Measurements | — |
| Expected result | — |
| Pass criterion | Fail-operational output remains ON continuously (sample ≥10 Hz) during Service restart window; no OFF pulse longer than approved glitch limit if defined, else no OFF sample. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | output sample log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-013 — Tablet disconnect isolation

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-013` |
| Title | Tablet disconnect isolation |
| Linked IDs | `REQ-DCC-V-DK-073` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Browser/Tablet disconnect does not stop fail-operational output. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Enable fail-op output 2. Disconnect WS/client 3. Monitor 10 s |
| Measurements | — |
| Expected result | — |
| Pass criterion | Output remains ON with no OFF sample over 10 s at ≥10 Hz sampling. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | sample log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-014 — CAN node loss integration reaction

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-014` |
| Title | CAN node loss integration reaction |
| Linked IDs | `REQ-DCC-V-DK-080`, `REQ-DCC-V-DK-079` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Losing simulated ECU yields defined reaction without bus damage. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-006; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Establish telem 2. Disconnect sim 3. Observe status and rule inhibits |
| Measurements | — |
| Expected result | — |
| Pass criterion | Lost/stale per TBD-DK-006 AND ENGINE_RUN entry inhibited if required by CFG; no bus hardware damage procedure used beyond disconnect. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | timeline |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-015 — Configuration apply, reject, atomicity; hot-reload policy

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-015` |
| Title | Configuration apply, reject, atomicity; hot-reload policy |
| Linked IDs | `REQ-DCC-V-DK-084`, `REQ-DCC-V-DK-085`, `REQ-DCC-V-DK-087`, `REQ-DCC-V-DK-088` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Valid apply; invalid reject without partial unsafe enables; atomicity. |
| Status | `BLOCKED` |
| Notes | Hot-reload permission governed by DK-GOV-011; this case tests apply/reject mechanics. Hot-reload outside Service mode remains blocked until ADR-DK-009. |
| Blocked by | ADR: ADR-DK-009; TBD: —; fixture: —; impl: — |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Apply valid 2. Apply invalid oversize capacity 3. Confirm reject and outputs safe 4. Apply truncated/corrupt payload 5. Confirm no partial enable |
| Measurements | — |
| Expected result | — |
| Pass criterion | Valid apply success; invalid/corrupt rejected; no represented channel newly ON due to rejected apply. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | apply logs |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-016 — Event logging and persistence across reset when required

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-016` |
| Title | Event logging and persistence across reset when required |
| Linked IDs | `REQ-DCC-V-DK-063`, `REQ-DCC-V-DK-064` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Safety-relevant fault is logged; persistence per case definition. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Inject fault F 2. Read log contains F 3. If persistence required: reset and confirm F still present; else document volatile-only |
| Measurements | — |
| Expected result | — |
| Pass criterion | Fault F present in log with type+timestamp before reset; after reset present iff case marked persistent, else absence documented as volatile-only limitation. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | logs before/after |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-017 — Restart recovery to safe defaults

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-017` |
| Title | Restart recovery to safe defaults |
| Linked IDs | `REQ-DCC-V-DK-060`, `REQ-DCC-V-DK-101` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Power cycle recovers to outputs OFF until authorized re-enable/config. |
| Status | `NOT EXECUTED` |
| Preconditions | — |
| Topology | — |
| Equipment | As required; models not mandated |
| Hazards | Case-specific electrical/thermal as applicable |
| Test configuration | — |
| Stimuli | — |
| Procedure | 1. Power cycle 2. Measure outputs 3. Confirm config re-apply rules |
| Measurements | — |
| Expected result | — |
| Pass criterion | All represented outputs OFF after recovery until explicit authorized enable/config apply. |
| Abort criterion | Unsafe current/temperature/smoke; stop and safe-OFF |
| Evidence | post-reset table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-019 — Gate evidence package baseline completeness inspection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-019` |
| Title | Gate evidence package baseline completeness inspection |
| Linked IDs | `REQ-DCC-V-DK-117` |
| Method | Inspection |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Inspect that a candidate gate evidence package has complete applicable STD-REV-001 identity (process enforced by DK-GOV-*). |
| Status | `NOT EXECUTED` |
| Artifacts inspected | Draft evidence package / baseline sheet; STD-REV-001 field list |
| Checklist | Every applicable identity field filled with value or explicit N/A with rationale; No applicable field left NOT RECORDED/UNKNOWN/TBD; Setup steps reproducible from package alone |
| Pass criterion | Checklist PASS. Any applicable NOT RECORDED/UNKNOWN/TBD ⇒ this inspection FAIL (and gate cannot PASS). |
| Evidence to retain | baseline sheet |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

## 4. Governance inspection cases (separated)

#### VER-DCC-DK-D-020 — EDL-014 relationship and exception controls (superseded by governance cases)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-020` |
| Title | EDL-014 relationship and exception controls |
| Linked IDs | `DK-GOV-001`, `DK-GOV-002`, `DK-GOV-003`, `DK-GOV-004` |
| Method | Inspection |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Historical case ID retained; normative governance inspection moved to VER-DCC-DK-G-*. |
| Status | `NOT EXECUTED` |
| Supersession | Superseded for execution by `VER-DCC-DK-G-001` and `VER-DCC-DK-G-003`. Do not execute D-020 as a separate procedure; certify via G-* results. |
| Artifacts inspected | See G-001 / G-003 |
| Checklist | See G-001 / G-003 |
| Pass criterion | G-001 and G-003 certified PASS (D-020 does not independently PASS). |
| Evidence to retain | Cross-reference to G-* inspection records |
| Procedure | Record pointer to G-001/G-003 execution records; do not duplicate energized-test steps |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-G-001 — Governance rules presence and non-substitution statements

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-G-001` |
| Title | Governance rules presence and non-substitution statements |
| Linked IDs | `DK-GOV-001`, `DK-GOV-002`, `DK-GOV-003`, `DK-GOV-004` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Inspect governance document for non-substitution, evidence-use, and exception rules. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | docs/DevKit/DevKit_Verification_Governance.md |
| Checklist | DK-GOV-001…004 present; EDL-014 vehicle-install prohibition explicit; Track exception ban explicit |
| Pass criterion | All checklist items true. |
| Evidence to retain | inspection note |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-G-002 — MPN policy and protocol non-invention rules

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-G-002` |
| Title | MPN policy and protocol non-invention rules |
| Linked IDs | `DK-GOV-005`, `DK-GOV-006`, `DK-GOV-007`, `DK-GOV-008` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Inspect coverage-claim and MPN/protocol invention prohibitions. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | DevKit_Verification_Governance.md; sample REQ SHALL lines |
| Checklist | GOV rules present; No MPN in active REQ SHALL lines |
| Pass criterion | Checklist PASS. |
| Evidence to retain | rg log of MPN scan |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-G-003 — Evidence authority and baseline recording rules

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-G-003` |
| Title | Evidence authority and baseline recording rules |
| Linked IDs | `DK-GOV-012`, `DK-GOV-014`, `DK-GOV-015`, `DK-GOV-016`, `DK-GOV-017`, `DK-GOV-018`, `DK-GOV-019`, `DK-GOV-020`, `DK-GOV-021`, `DK-GOV-022`, `DK-GOV-023` |
| Method | Inspection |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Inspect evidence/baseline governance rules including complete-identity gate rule. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | DevKit_Verification_Governance.md § baseline identity |
| Checklist | Complete applicable identity required for gate PASS; N/A only when genuinely inapplicable; Test Owner certification authority stated |
| Pass criterion | Checklist PASS. |
| Evidence to retain | inspection note |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-G-004 — Threshold and ADR dependency freezes for gates

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-G-004` |
| Title | Threshold and ADR dependency freezes for gates |
| Linked IDs | `DK-GOV-009`, `DK-GOV-010`, `DK-GOV-011`, `DK-GOV-024`, `DK-GOV-025` |
| Method | Inspection |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Inspect governance dependencies for equivalence/OTA/hot-reload/threshold freezes. |
| Status | `NOT EXECUTED` |
| Artifacts inspected | Governance doc; ADR-DK list; TBD register |
| Checklist | Rules present; No silent resolution of ADR-DK-001…012 |
| Pass criterion | Checklist PASS. |
| Evidence to retain | inspection note |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

## 5. Blocked-case dependency summary

| Verification ID | Gate | Classification | Blocking ADR | Blocking TBD | Fixture dependency | Resulting gate effect |
|-----------------|------|----------------|--------------|--------------|--------------------|-----------------------|
| `VER-DCC-DK-A-006` | DK-A | MANDATORY | — | TBD-DK-001…004 | — | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-003` | DK-A | MANDATORY | ADR-DK-006 | TBD-DK-001, TBD-DK-017 | Documented rail test points | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-008` | DK-A | MANDATORY | ADR-DK-001 | TBD-DK-007 | J_LP connection access | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-011` | DK-A | MANDATORY | ADR-DK-007 | TBD-DK-005 | Safe WDT injection method | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-012` | DK-A | MANDATORY | ADR-DK-007 | TBD-DK-004 | — | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-014` | DK-A | MANDATORY | — | TBD-DK-021 | — | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-015` | DK-A | CONDITIONAL_MANDATORY | — | TBD-DK-020 | — | Blocks DK-A PASS only when BOARD_ID sensing is included in tested baseline; else DEFERRED_EXCLUDED (not counted verified) |
| `VER-DCC-DK-A-016` | DK-A | MANDATORY | — | TBD-DK-014 | — | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-003` | DK-B | MANDATORY | — | TBD-DK-006 | — | Gate DK-B cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-005` | DK-B | MANDATORY | — | TBD-DK-015 | — | Gate DK-B cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-011` | DK-B | CONDITIONAL_MANDATORY | — | TBD-DK-016 | — | Gate DK-B cannot PASS while this CONDITIONAL_MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-014` | DK-B | CONDITIONAL_MANDATORY | ADR-DK-008 | — | — | Gate DK-B cannot PASS while this CONDITIONAL_MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-002` | DK-C | MANDATORY | — | TBD-DK-014 | — | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-003` | DK-C | CONDITIONAL_MANDATORY | — | TBD-DK-008 | — | Gate DK-C cannot PASS while this CONDITIONAL_MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-004` | DK-C | MANDATORY | — | TBD-DK-009 | — | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-005` | DK-C | MANDATORY | ADR-DK-010 | TBD-DK-011 | overcurrent fixture | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-006` | DK-C | MANDATORY | ADR-DK-010 | — | safe short fixture | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-008` | DK-C | MANDATORY | — | TBD-DK-012 | — | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-009` | DK-C | CONDITIONAL_MANDATORY | ADR-DK-011 | TBD-DK-010, TBD-DK-018, TBD-DK-019 | — | Gate DK-C cannot PASS while this CONDITIONAL_MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-012` | DK-C | MANDATORY | — | TBD-DK-007 | — | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-013` | DK-C | CONDITIONAL_MANDATORY | — | TBD-DK-022 | stall fixture | Gate DK-C cannot PASS while this CONDITIONAL_MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-014` | DK-C | MANDATORY | — | TBD-DK-013 | — | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-014` | DK-D | MANDATORY | — | TBD-DK-006 | — | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-015` | DK-D | MANDATORY | ADR-DK-009 | — | — | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |

## 6. Gates DK-A…DK-D

### Gate DK-A

- **MANDATORY:** `VER-DCC-DK-A-001`, `VER-DCC-DK-A-002`, `VER-DCC-DK-A-003`, `VER-DCC-DK-A-004`, `VER-DCC-DK-A-005`, `VER-DCC-DK-A-006`, `VER-DCC-DK-A-007`, `VER-DCC-DK-A-008`, `VER-DCC-DK-A-009`, `VER-DCC-DK-A-010`, `VER-DCC-DK-A-011`, `VER-DCC-DK-A-012`, `VER-DCC-DK-A-013`, `VER-DCC-DK-A-014`, `VER-DCC-DK-A-016`, `VER-DCC-DK-A-017`, `VER-DCC-DK-G-001`, `VER-DCC-DK-G-002`, `VER-DCC-DK-G-004`
- **CONDITIONAL_MANDATORY:** `VER-DCC-DK-A-015`

| Field | Content |
|-------|---------|
| Outcomes | PASS / FAIL / BLOCKED / NOT ASSESSED |
| PASS requires | All MANDATORY certified PASS; all applicable CONDITIONAL_MANDATORY certified PASS; exclusions listed; no blocking ADR/TBD for tested scope; **complete applicable STD-REV-001 baseline**; evidence present; no critical safety finding |
| Identity rule | Applicable NOT RECORDED/UNKNOWN/TBD ⇒ BLOCKED/NOT ASSESSED (not PASS) |
| Prohibited | Mandatory case remaining BLOCKED while declaring gate PASS |

### Gate DK-B

- **MANDATORY:** `VER-DCC-DK-B-001`, `VER-DCC-DK-B-002`, `VER-DCC-DK-B-003`, `VER-DCC-DK-B-004`, `VER-DCC-DK-B-005`, `VER-DCC-DK-B-006`, `VER-DCC-DK-B-007`, `VER-DCC-DK-B-008`, `VER-DCC-DK-B-009`, `VER-DCC-DK-B-013`, `VER-DCC-DK-B-015`
- **CONDITIONAL_MANDATORY:** `VER-DCC-DK-B-010`, `VER-DCC-DK-B-011`, `VER-DCC-DK-B-012`, `VER-DCC-DK-B-014`

| Field | Content |
|-------|---------|
| Outcomes | PASS / FAIL / BLOCKED / NOT ASSESSED |
| PASS requires | All MANDATORY certified PASS; all applicable CONDITIONAL_MANDATORY certified PASS; exclusions listed; no blocking ADR/TBD for tested scope; **complete applicable STD-REV-001 baseline**; evidence present; no critical safety finding |
| Identity rule | Applicable NOT RECORDED/UNKNOWN/TBD ⇒ BLOCKED/NOT ASSESSED (not PASS) |
| Prohibited | Mandatory case remaining BLOCKED while declaring gate PASS |

### Gate DK-C

- **MANDATORY:** `VER-DCC-DK-C-001`, `VER-DCC-DK-C-002`, `VER-DCC-DK-C-004`, `VER-DCC-DK-C-005`, `VER-DCC-DK-C-006`, `VER-DCC-DK-C-008`, `VER-DCC-DK-C-012`, `VER-DCC-DK-C-014`
- **CONDITIONAL_MANDATORY:** `VER-DCC-DK-C-003`, `VER-DCC-DK-C-007`, `VER-DCC-DK-C-009`, `VER-DCC-DK-C-010`, `VER-DCC-DK-C-011`, `VER-DCC-DK-C-013`

| Field | Content |
|-------|---------|
| Outcomes | PASS / FAIL / BLOCKED / NOT ASSESSED |
| PASS requires | All MANDATORY certified PASS; all applicable CONDITIONAL_MANDATORY certified PASS; exclusions listed; no blocking ADR/TBD for tested scope; **complete applicable STD-REV-001 baseline**; evidence present; no critical safety finding |
| Identity rule | Applicable NOT RECORDED/UNKNOWN/TBD ⇒ BLOCKED/NOT ASSESSED (not PASS) |
| Prohibited | Mandatory case remaining BLOCKED while declaring gate PASS |

### Gate DK-D

- **MANDATORY:** `VER-DCC-DK-D-002`, `VER-DCC-DK-D-003`, `VER-DCC-DK-D-004`, `VER-DCC-DK-D-005`, `VER-DCC-DK-D-006`, `VER-DCC-DK-D-012`, `VER-DCC-DK-D-013`, `VER-DCC-DK-D-014`, `VER-DCC-DK-D-015`, `VER-DCC-DK-D-016`, `VER-DCC-DK-D-017`, `VER-DCC-DK-D-019`, `VER-DCC-DK-G-003` (D-020 superseded by G-001/G-003 — do not separately certify)

| Field | Content |
|-------|---------|
| Outcomes | PASS / FAIL / BLOCKED / NOT ASSESSED |
| PASS requires | All MANDATORY certified PASS; all applicable CONDITIONAL_MANDATORY certified PASS; exclusions listed; no blocking ADR/TBD for tested scope; **complete applicable STD-REV-001 baseline**; evidence present; no critical safety finding |
| Identity rule | Applicable NOT RECORDED/UNKNOWN/TBD ⇒ BLOCKED/NOT ASSESSED (not PASS) |
| Prohibited | Mandatory case remaining BLOCKED while declaring gate PASS |

## 7. EDL-014 relationship

- Passing DK-A…DK-D does not authorize vehicle installation.
- Phase E on full DCC Gen1 remains required.
- DevKit evidence supports but does not replace Gen1 evidence.
- Exceptions: DK-GOV-004.

## 8. Counts

| Set | Count |
|-----|-------|
| System cases A–D | 59 |
| Governance cases G | 4 |
| Total cases | 63 |
| BLOCKED | (see §5 table) |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial plan |
| 1.1 | 2026-07-19 | WP-007-R1 — method schemas; splits; gate classifications; identity rule |
| 1.1.1 | 2026-07-19 | WP-007-R1 corrections — restore A-004/B-001/B-002 meanings; add A-006/A-007; D-020 supersession; schema fixes |
