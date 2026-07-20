# DevKit Verification Plan — Gen1

**Document ID:** DOC-DK-VER-001  
**Version:** 1.2  
**Status:** Accepted  
**Work Package:** WP-007 / WP-007-R4  
**Date:** 2026-07-19  

System requirements: [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md)  
Governance: [`DevKit_Verification_Governance.md`](DevKit_Verification_Governance.md)  
Identity: ADR-015 / STD-REV-001 · Gate policy: EDL-014  
P0 architecture decisions: Accepted ADR-016…023 — [`DevKit_P0_Decision_Crosswalk.md`](DevKit_P0_Decision_Crosswalk.md) (WP-008).  
Threshold analysis (Accepted): [`DevKit_Threshold_Closure_Matrix.md`](DevKit_Threshold_Closure_Matrix.md) (WP-009 — TBDs remain Open).

Functional electrical architecture (Accepted): [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md) (WP-010 / WP-010-R1 Accepted).

> **TBD authority:** The Threshold Resolution Register in [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md) §4 is the authoritative source for `TBD-DK-*` identifiers. This plan references those IDs; it does not redefine them.

> No case is marked PASS. No physical tests were executed in WP-007 / R1 / R2 / R3 / WP-008 / WP-009 / WP-010.

## 1. Methods and schemas

Each case uses a method-specific field set (Inspection / Analysis / Demonstration / Test). Shared safety preamble: supervised energization; kill accessible; loads connected only when channel OFF; abort on smoke/uncontrolled current. This preamble does **not** replace case procedures.

### 1.1 Placeholder policy (WP-007-R3)

For `Method: Test` cases, `—`, `As required`, or equivalent generic placeholder is permitted **only** when the case is `BLOCKED` and the missing definition is explicitly listed in `Blocked by`.

Inspection and Analysis cases may use `N/A — reason` where the field genuinely does not apply.
Prefer `N/A — reason` over a bare dash.

A mandatory or conditional Test case that is not `BLOCKED` shall be fully reproducible from this document without requiring the operator to design the test.

### 1.2 Semantic placeholder enforcement (WP-007-R4)

A case being generally `BLOCKED` does **not** by itself justify unrelated placeholders.
An open numeric threshold (`TBD-DK-*`) does **not** justify omitting topology, equipment, stimulus, or measurement definitions.
Every remaining bare `—` / `As required` in a Test field shall correspond to an exact item named in `Blocked by`.
Prefer completing the field; use `N/A — reason` when genuinely not applicable.

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
| Blocked by | Architectural/process escalation: interim revision-identity procedure required where runtime metadata is not implemented (ADR-015 / STD-REV-001; DK-GOV-012, DK-GOV-014, DK-GOV-015). Not blocked by electrical operating thresholds (TBD-DK-001, TBD-DK-002, TBD-DK-003, TBD-DK-017). |
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

#### VER-DCC-DK-A-005 — Service-domain programming

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-A-005` |
| Title | Service-domain programming |
| Linked IDs | `REQ-DCC-V-DK-066`, `REQ-DCC-V-DK-010` |
| Method | Test |
| Gate | DK-A |
| Classification | `MANDATORY` |
| Objective | Program Service domain via documented interface and verify image identity. |
| Status | `NOT EXECUTED` |
| Preconditions | Documented Service programming path available; PSU off or programming-safe state; no channel loads connected |
| Topology | Host programmer ↔ IF-DK-USB (or documented Service program port) ↔ Service MCU/module |
| Equipment | Host with Service programming toolchain; USB (or documented) adapter |
| Hazards | Incorrect image; accidental domain energization |
| Test configuration | N/A — programming image only; no output-enable configuration applied |
| Stimuli | Program/verify Service firmware image with recorded commit SHA / artifact ID |
| Procedure | 1. Record Service image identity 2. Connect adapter in programming-safe state 3. Erase/program/verify per Service programming guide 4. Capture tool log 5. Confirm RT outputs remain uncommanded OFF if Power domain present |
| Measurements | program/verify result (pass/fail); image identity fields |
| Expected result | Tool verify success for recorded identity; no represented channel ON |
| Pass criterion | Tool reports verify success for the recorded Service image identity AND every represented channel remains OFF. |
| Abort criterion | Unexpected channel ON; verify failure after two documented retries |
| Evidence | Host programming log; image identity record |
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
| Preconditions | RT programmed (A-004); A-002 unpowered inspection complete; no loads connected |
| Topology | Bench PSU → IF-DK-PWR-IN; DevKit Logic (+Power if present); DMM on represented channel outputs; diagnostic/status path |
| Equipment | Lab PSU; DMM; diagnostic host or local status indicator as documented |
| Hazards | Unexpected output enable during startup |
| Test configuration | Default/safe config with all outputs disabled |
| Stimuli | Power cycle RT domain (apply Vin, wait, remove, re-apply) once |
| Procedure | 1. Record baseline identity 2. Energize 3. Record time to documented READY/operable indication 4. Read diagnostic mode/state 5. Measure each represented channel Vout 6. Confirm diagnostic output mask OFF 7. De-energize |
| Measurements | t_ready_ms; state_enum; Vout_chN for each represented channel |
| Expected result | Operable/READY reached; all represented outputs electrically and diagnostically OFF |
| Pass criterion | Documented READY/operable state observed AND every represented channel OFF electrically and in diagnostics. |
| Abort criterion | Any represented channel ON during startup; smoke; unexpected overcurrent |
| Evidence | state log; measurement table; identity sheet |
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
| Blocked by | ADR: ADR-DK-007; TBD: TBD-DK-005 (response-time acceptance); fixture: Safe WDT injection method; impl: RT watchdog path that de-energizes outputs |
| Preconditions | Safe WDT injection method available (debugger halt, test hook, or documented starve method); outputs may be briefly ON on one low-risk channel to prove de-energize; kill accessible |
| Topology | Bench PSU → DevKit; optional CH_LR → safe load; DMM on represented outputs; debugger/WDT inject interface on RT |
| Equipment | Lab PSU; DMM; optional safe load; SWD/debugger or documented WDT inject tool; timing log/host |
| Hazards | Uncontrolled hang — supervised; kill ready |
| Test configuration | CFG-DK-WDT-01: optional single low-risk channel authorized ON for proof; others OFF |
| Stimuli | If needed, command CH_LR ON; at t0 inject WDT fault (halt/starve per fixture method) |
| Procedure | 1. Record baseline 2. Optionally ON CH_LR 3. Inject WDT at t0 4. Sample all represented outputs until OFF 5. Record t_off_ms and fault indication 6. Recover per documented reset sequence |
| Measurements | t_off_ms; Vout_chN; fault/WDT indication |
| Expected result | All represented outputs OFF; t_off within TBD-DK-005 when approved |
| Pass criterion | All represented outputs OFF with t_off_ms ≤ approved TBD-DK-005. If TBD-DK-005 or WDT fixture/ADR-DK-007 open: BLOCKED. |
| Abort criterion | Inability to regain control; smoke; sustained ON after inject |
| Evidence | timing log; inject method note; output table |
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
| Objective | Assert kill; confirm outputs de-energize within approved time; Service/UI cannot re-energize while asserted. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-007; TBD: TBD-DK-004 (kill response-time acceptance); fixture: kill switch or nKILL_HW assert method on IF-DK-KILL; impl: kill de-energize path independent of Service |
| Preconditions | Kill path accessible; optional low-risk channel for ON→OFF proof; Service command path available for bypass attempt |
| Topology | Kill switch/fixture → IF-DK-KILL; Bench PSU → DevKit; DMM on represented outputs; Service/UI host |
| Equipment | Kill switch or jumper fixture; lab PSU; DMM; Service/HTTP or diagnostic command client; optional safe load |
| Hazards | Unexpected enable — supervised |
| Test configuration | CFG-DK-KILL-01 authorizing at most one low-risk channel CH_LR |
| Stimuli | Command CH_LR ON if used; assert kill at t0; while asserted send Service/UI enable for CH_LR |
| Procedure | 1. Optionally ON CH_LR 2. Assert kill at t0 3. Measure t_off_ms to all outputs OFF 4. Send Service/UI enable attempts for ≥5 s 5. Confirm still OFF 6. Leave kill asserted until commands stop |
| Measurements | t_off_ms; Vout_chN; kill state; Service command results |
| Expected result | Outputs OFF within TBD-DK-004 when approved; zero successful Service/UI energizations under kill |
| Pass criterion | t_off_ms ≤ approved TBD-DK-004 AND zero successful energizations from Service/UI while kill asserted AND all represented channels OFF. If TBD-DK-004 or ADR-DK-007 open: BLOCKED. |
| Abort criterion | Channel ON under kill; smoke |
| Evidence | timing log; command log; output table |
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
| Objective | After kill de-assert and after reset, outputs remain OFF until the documented re-enable sequence. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-021 (post-kill explicit re-enable sequence definition); fixture: kill switch/fixture; impl: documented re-enable sequence in software/procedure |
| Preconditions | Kill path available (A-012 method); reset method available (power cycle or RT reset); diagnostic host |
| Topology | Kill → IF-DK-KILL; PSU → DevKit; DMM on represented outputs |
| Equipment | Kill fixture; lab PSU; DMM; diagnostic/command host |
| Hazards | Unexpected enable after kill clear |
| Test configuration | CFG-DK-KILL-01; no auto-enable mask |
| Stimuli | Assert kill; de-assert kill; attempt command ON before re-enable sequence; perform documented re-enable sequence (when defined); then authorized ON; separately: power-cycle reset and confirm OFF |
| Procedure | 1. Assert kill; confirm OFF 2. De-assert kill 3. Attempt ON without re-enable sequence — expect remain OFF 4. Execute TBD-DK-021 sequence when defined 5. Confirm one controlled ON succeeds only after sequence 6. Power-cycle; confirm all OFF until authorized enable |
| Measurements | Vout_chN; kill state; mode; command results |
| Expected result | OFF after kill clear until re-enable sequence; OFF after reset until authorized enable |
| Pass criterion | After kill de-assert and after reset, all represented outputs remain OFF until documented re-enable sequence completes; one controlled ON succeeds only after that sequence. If TBD-DK-021 open: BLOCKED. |
| Abort criterion | Spurious ON; smoke |
| Evidence | sequence log; output table |
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
| Objective | When BOARD_ID sensing is implemented, read and record raw BOARD_ID and mapping status. |
| Status | `BLOCKED` |
| Notes | Condition: BOARD_ID sensing included in tested baseline. Else DEFERRED_EXCLUDED. |
| Blocked by | ADR: —; TBD: TBD-DK-020 (encoding→revision map acceptance); fixture: N/A — uses on-board BOARD_ID sense path; impl: BOARD_ID readout path in RT/diagnostics |
| Preconditions | Determine whether BOARD_ID readout exists in tested build; Power domain present with BOARD_ID circuit |
| Topology | DevKit powered; diagnostic/host path to BOARD_ID sense (via J_LP / ADC / documented API) |
| Equipment | Lab PSU; diagnostic host or debugger capable of reading BOARD_ID value |
| Hazards | N/A — read-only identity |
| Test configuration | N/A — identity read; no output-enable configuration required |
| Stimuli | Issue BOARD_ID read command / diagnostic query |
| Procedure | 1. If readout absent: mark DEFERRED_EXCLUDED for this baseline 2. If present: power DevKit 3. Read raw BOARD_ID 4. Record value 5. Record mapping status vs TBD-DK-020 (mapped revision or unmapped) |
| Measurements | BOARD_ID_raw; mapping_status; revision_interpreted_or_UNMAPPED |
| Expected result | Raw value recorded; interpretation only if TBD-DK-020 map approved |
| Pass criterion | Raw BOARD_ID recorded AND mapping applied only when TBD-DK-020 approved (otherwise mapping_status=UNMAPPED accepted for recording, but revision-claim PASS blocked). If readout impl missing when sensing claimed: BLOCKED. |
| Abort criterion | N/A — read-only |
| Evidence | diagnostic snapshot; identity sheet |
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
| Objective | After reset, every represented channel is OFF; quantitative commanded-OFF timing uses TBD-DK-014 when that step is included. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-014 (blocks quantitative commanded-OFF timing if OFF-command timing step is certified); fixture: N/A for default-OFF survey; impl: RT default-OFF behaviour on represented channels |
| Preconditions | Represented channel list from C-001 or interim inventory; RT programmed; no loads required for voltage OFF survey (optional loads remain disconnected) |
| Topology | Bench PSU → DevKit; DMM probing each represented channel output terminal to GND; diagnostic host |
| Equipment | Lab PSU; DMM; diagnostic host |
| Hazards | Unexpected enable — no loads attached for this survey |
| Test configuration | Default/safe config with no auto-enable mask |
| Stimuli | Power-cycle or RT reset; optionally command ON then OFF on one channel to exercise TBD-DK-014 timing (separate quantitative step) |
| Procedure | 1. Reset/power-cycle 2. Wait READY 3. For each represented channel: measure Vout and read diag 4. Confirm OFF per C-002 observation convention 5. Optional: command ON/OFF on one channel and record t_off_ms for TBD-DK-014 |
| Measurements | Vout_chN; diag_state_chN; optional t_off_ms |
| Expected result | 100% of represented channels OFF after reset; optional t_off recorded |
| Pass criterion | 100% of represented channels OFF by measurement and diagnostics after reset. If certifying commanded OFF timing: t_off_ms ≤ TBD-DK-014 when approved; if TBD-DK-014 open, timing step remains blocked and overall case stays BLOCKED when timing is in scope for the run. Default-OFF survey still requires impl default-OFF path. |
| Abort criterion | Any channel ON after reset; smoke |
| Evidence | post-reset measurement table |
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

#### VER-DCC-DK-B-003 — Stale/lost ECU node handling

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
| Blocked by | ADR: —; TBD: TBD-DK-006 (lost/stale timeout acceptance); fixture: ECU simulator with clean stop/silent; impl: ECU node status / LOST path in RT |
| Preconditions | B-002 path available; ECU simulator streaming valid telem; diagnostic status readable |
| Topology | ECU sim ↔ IF-DK-CAN ↔ DevKit; CAN sniffer tap; diagnostic host |
| Equipment | ECU simulator; CAN FD sniffer; lab PSU; diagnostic host |
| Hazards | N/A — communication/status case; outputs remain uncommanded ON |
| Test configuration | CFG-DK-SAFE-01 or CFG-DK-ECU-TELEM-01 with ECU telem consumption enabled; outputs OFF |
| Stimuli | Establish valid ENGINE_TELEM stream; at t0 stop simulator (silent ECU node) |
| Procedure | 1. Start sniffer 2. Establish valid telem 3. Stop sim at t0 4. Poll DCC ecu status until LOST/stale 5. Record t_lost_ms 6. Confirm DevKit HEARTBEAT continues |
| Measurements | t_lost_ms; ecu_status; HEARTBEAT continuity |
| Expected result | LOST/stale indication; bus remains valid (DevKit traffic continues) |
| Pass criterion | Lost/stale indication true with t_lost_ms in approved TBD-DK-006 window (+ documented tolerance). If TBD-DK-006 open: BLOCKED. |
| Abort criterion | Bus shorting; unintended output enable |
| Evidence | timeline log; sniffer |
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
| Objective | Inject a Button Box DCP event and observe the configured diagnostic/event reception path. |
| Status | `NOT EXECUTED` |
| Preconditions | DK-A bring-up complete; CAN path available (B-001); Button Box simulator tool available |
| Topology | Button Box simulator ↔ IF-DK-CAN ↔ DevKit; CAN sniffer tap |
| Equipment | Button Box / DCP event simulator; CAN FD sniffer; PSU |
| Hazards | Unintended output enable if config maps event to a channel — use config with diagnostic-only mapping for this Phase B case |
| Test configuration | CFG-DK-BB-01: maps control_id `BB_EVT_1` (Button Box instance per docs/004 when defined) to diagnostic event `EVT_BB_1` only; no power-channel enable |
| Stimuli | Transmit one Button Box event frame for control_id `BB_EVT_1` at t0; repeat once after 500 ms |
| Procedure | 1. Start sniffer 2. Apply CFG-DK-BB-01 3. Inject BB_EVT_1 4. Confirm DevKit diagnostic/API/event log shows EVT_BB_1 with timestamp 5. Inject second event; confirm second log entry 6. Confirm no represented channel ON |
| Measurements | event_rx_count; event_id; timestamps; channel output states |
| Expected result | Two EVT_BB_1 receptions logged; outputs remain OFF |
| Pass criterion | event_rx_count ≥ 2 for BB_EVT_1/EVT_BB_1 AND all represented channels OFF. If Button Box DCP ID/layout undefined in Accepted protocol baseline: Status BLOCKED (do not invent ID). |
| Abort criterion | Any channel ON |
| Evidence | sniffer capture; event log; config identity |
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
| Objective | Confirm termination installation and record waveform metrics against TBD-DK-015 when approved. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-015 (waveform acceptance metrics); fixture: CAN differential probe / scope; impl: N/A for termination presence (physical); DevKit CAN transceiver operating |
| Preconditions | Linear CAN topology for bench; termination resistors installed per intended topology; HEARTBEAT or traffic available (B-001) |
| Topology | DevKit CAN_H/CAN_L with termination at documented ends; scope differential probe across CAN_H–CAN_L; sniffer optional |
| Equipment | Oscilloscope with differential CAN probe (or two single-ended probes); lab PSU; optional CAN sniffer |
| Hazards | N/A — signal measurement |
| Test configuration | N/A — bus traffic from DevKit HEARTBEAT; outputs OFF |
| Stimuli | Energize DevKit to operable; capture CAN differential waveform during HEARTBEAT |
| Procedure | 1. Inspect termination resistors presence/location; photograph/record 2. Probe CAN_H/CAN_L 3. Capture ≥10 HEARTBEAT frames 4. Measure metrics required by TBD-DK-015 when defined (e.g. differential amplitude, recessive/dominant levels) 5. Export captures |
| Measurements | termination_present (checklist); Vdiff_dom; Vdiff_rec; other TBD-DK-015 metrics when defined |
| Expected result | Termination present per topology; waveform metrics meet TBD-DK-015 when approved |
| Pass criterion | Termination inspection PASS AND waveform metrics meet approved TBD-DK-015. If TBD-DK-015 open: termination evidence may be recorded; integrity acceptance remains BLOCKED. |
| Abort criterion | N/A |
| Evidence | photos; scope captures; metric table |
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
| Objective | Sustain valid DCPI transfers beyond basic bring-up (A-009). |
| Status | `NOT EXECUTED` |
| Preconditions | A-009 path available or equivalent DCPI link up; RT and Service programmed |
| Topology | Logic ↔ Radio via IF-DK-DCPI; optional SPI capture |
| Equipment | Optional SPI/logic analyzer; Service/RT logs; PSU |
| Hazards | N/A — no output-enable config applied during this case |
| Test configuration | N/A — state/ping exchange only; no CONFIG apply of output enables |
| Stimuli | Continuous valid DCPI state/ping frames for ≥60 s at the documented link rate (or ≥1 Hz if rate TBD — record actual rate) |
| Procedure | 1. Establish DCPI link 2. Exchange valid frames for ≥60 s 3. Record accept count and error counters at t=0, 30 s, 60 s 4. Confirm outputs remain OFF 5. Stop and export logs |
| Measurements | valid_accept_count; error_counter; duration_s; output states |
| Expected result | Sustained acceptance without cumulative unexplained errors; outputs OFF |
| Pass criterion | duration_s ≥ 60 AND valid_accept_count ≥ 60 AND error_counter does not indicate accepted corrupt frames AND all represented outputs OFF. |
| Abort criterion | Link hard-fault with undefined recovery; any output ON |
| Evidence | DCPI log; counters snapshot |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-B-007 — Configuration transfer apply and recovery docs

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-007` |
| Title | Configuration transfer apply and recovery docs |
| Linked IDs | `REQ-DCC-V-DK-068`, `REQ-DCC-V-DK-083`, `REQ-DCC-V-DK-118` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Transfer a valid safe configuration via Service path and confirm apply ack; confirm recovery/rollback doc exists. |
| Status | `NOT EXECUTED` |
| Preconditions | Service programmed; DCPI or documented config path available; recovery/rollback procedure document available for inspection |
| Topology | Host/Service ↔ IF-DK-CFG / DCPI ↔ RT; DevKit powered; outputs uncommanded |
| Equipment | Config transfer host tool; PSU; logs |
| Hazards | Mis-applied enable mask — use safe config only |
| Test configuration | CFG-DK-SAFE-01: all represented channels disabled/OFF; recorded config ID + schema version (+ hash when available) |
| Stimuli | Transfer CFG-DK-SAFE-01; request apply in authorized mode (boot or Service/Wiring mode as documented) |
| Procedure | 1. Record firmware identity 2. Transfer CFG-DK-SAFE-01 3. Observe apply ack/reject 4. Read back active config identity 5. Confirm all outputs OFF 6. Inspect recovery/rollback document exists and names failure-apply steps (REQ-118) |
| Measurements | apply_result; active_config_id; output states |
| Expected result | Apply accepted; active identity matches CFG-DK-SAFE-01; outputs OFF; recovery doc present |
| Pass criterion | apply_result = accepted AND active_config_id matches CFG-DK-SAFE-01 AND all represented outputs OFF AND recovery/rollback document path recorded. |
| Abort criterion | Any channel ON after apply |
| Evidence | transfer log; config identity; recovery doc citation |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-B-008 — DCPI corrupted frame rejection during config path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-008` |
| Title | DCPI corrupted frame rejection during config path |
| Linked IDs | `REQ-DCC-V-DK-099`, `REQ-DCC-V-DK-085` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | Reject corrupted DCPI config-path frames without unsafe apply. |
| Status | `NOT EXECUTED` |
| Preconditions | B-007 path available or equivalent config transfer path; outputs OFF |
| Topology | Host/Service ↔ IF-DK-DCPI ↔ RT; optional SPI capture |
| Equipment | Frame injector or modified transfer tool capable of CRC bit-flip; logs; PSU |
| Hazards | Accidental valid apply of enable mask — keep payload as disabled-outputs config or non-enable fragment |
| Test configuration | Target payload = CFG-DK-SAFE-01 bytes; corruption = flip ≥1 bit after CRC compute on ≥5 frames |
| Stimuli | Send ≥5 corrupted-CRC config frames; then send ≥1 valid CFG-DK-SAFE-01 frame |
| Procedure | 1. Note active config identity 2. Inject corrupted frames 3. Confirm each rejected (no apply ack; error counter/flag) 4. Confirm no channel ON 5. Send valid frame; confirm accept 6. Export evidence |
| Measurements | corrupt_reject_count; valid_accept; error_counter_or_flag; output states |
| Expected result | Corrupt rejected; valid accepted; outputs OFF throughout |
| Pass criterion | corrupt_reject_count ≥ 5 with zero successful apply of corrupted payload AND subsequent valid apply succeeds AND all represented outputs OFF throughout. |
| Abort criterion | Corrupted frame accepted; any output ON |
| Evidence | DCPI/config log; counters |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-B-009 — Diagnostic event visibility via Service path

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-009` |
| Title | Diagnostic event visibility via Service path |
| Linked IDs | `REQ-DCC-V-DK-069`, `REQ-DCC-V-DK-051`, `REQ-DCC-V-DK-097` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | A generated diagnostic event is visible via the Service diagnostic path. |
| Status | `NOT EXECUTED` |
| Preconditions | Service running; RT operable; documented event-generation method available (test API, controlled fault, or Button Box diagnostic event) |
| Topology | RT → DCPI/Service → REST/diagnostic API or log; host client |
| Equipment | Host HTTP/diagnostic client; PSU; optional CAN/BB simulator if used as event source |
| Hazards | Use non-destructive event source only |
| Test configuration | CFG-DK-SAFE-01 (outputs OFF); event source = BB_EVT_1→EVT_BB_1 from CFG-DK-BB-01 or documented test-event inject |
| Stimuli | Generate one diagnostic event E1 at t0 |
| Procedure | 1. Clear/observe baseline event list 2. Inject E1 3. Query Service diagnostic/events API or equivalent 4. Confirm E1 present with type and timestamp 5. Confirm outputs OFF |
| Measurements | event_visible (yes/no); event_type; timestamp; output states |
| Expected result | E1 visible on Service path; outputs OFF |
| Pass criterion | E1 visible with type+timestamp via Service diagnostic path within 5 s of injection AND all represented outputs OFF. |
| Abort criterion | Any channel ON |
| Evidence | API/log capture; config identity |
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
| Objective | REST status endpoint returns required identity/health fields when REST is in gate scope. |
| Status | `NOT EXECUTED` |
| Notes | Condition: REST API represented in tested DevKit baseline. Else DEFERRED_EXCLUDED. |
| Preconditions | Service Wi-Fi/REST available; host on DevKit network |
| Topology | Host HTTP client ↔ Service REST `/api/v1/` (docs/006) |
| Equipment | Host with curl or equivalent HTTP client; PSU |
| Hazards | N/A — read-only status |
| Test configuration | N/A — status read; no output commands |
| Stimuli | GET documented status/health resource (e.g. `/api/v1/status` or equivalent per docs/006) |
| Procedure | 1. Associate host to Service network 2. GET status 3. Record JSON fields present 4. Compare to required field list: health/state, firmware identity fields available, config identity when available |
| Measurements | HTTP status code; field presence checklist |
| Expected result | HTTP 200; required fields present (values may be NOT RECORDED where unimplemented, but keys present or explicitly documented absent) |
| Pass criterion | HTTP 200 AND checklist of required status/health keys satisfied per docs/006 DevKit-applicable subset recorded in the test record. If REST not in baseline: DEFERRED_EXCLUDED. |
| Abort criterion | N/A — read-only |
| Evidence | response JSON; field checklist |
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
| Objective | Subscribe telemetry and measure loss against TBD-DK-016 when approved. |
| Status | `BLOCKED` |
| Notes | Condition: WebSocket telemetry in tested gate scope. Else DEFERRED_EXCLUDED. |
| Blocked by | ADR: —; TBD: TBD-DK-016 (duration and allowed loss); fixture: N/A — host WS client; impl: Service WebSocket telemetry path |
| Preconditions | Service Wi-Fi/WS available; host on DevKit network; RT providing telemetry source data |
| Topology | Host WebSocket client ↔ Service WS endpoint (docs/006); DevKit powered |
| Equipment | Host with WebSocket client (script or browser tooling); lab PSU; packet/frame counter in client |
| Hazards | N/A — telemetry subscribe |
| Test configuration | N/A — subscribe-only; no output commands |
| Stimuli | Open WS telemetry subscription; collect for duration D (D from TBD-DK-016 when approved; provisional collect ≥15 s for evidence even if acceptance blocked) |
| Procedure | 1. Associate host 2. Open WS telemetry 3. Count frames/messages and gaps for duration D 4. Compute loss metrics per TBD-DK-016 definition when approved 5. Close subscription |
| Measurements | duration_s; frame_count; gap_count; loss_metric |
| Expected result | Continuous telemetry stream meeting TBD-DK-016 when approved |
| Pass criterion | Meets approved TBD-DK-016. If open: record duration/frame_count/gaps; case remains BLOCKED. |
| Abort criterion | N/A |
| Evidence | client log CSV; subscription parameters |
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
| Objective | Unauthorized REST attempt to command outputs is rejected and does not energize channels. |
| Status | `NOT EXECUTED` |
| Notes | Condition: REST outputs API exists in tested baseline. Else DEFERRED_EXCLUDED. |
| Preconditions | Service REST available; kill not asserted; represented channels OFF |
| Topology | Host HTTP client ↔ Service REST; DMM on one low-risk represented channel |
| Equipment | HTTP client; DMM; PSU |
| Hazards | Accidental authorized enable — use unauthorized/unauthenticated request only |
| Test configuration | CFG-DK-SAFE-01; no valid auth token / intentionally unauthorized session |
| Stimuli | POST/PUT to documented outputs enable endpoint for channel CH_X without authorization |
| Procedure | 1. Measure CH_X OFF 2. Send unauthorized enable request 3. Record HTTP status 4. Measure CH_X 5. Confirm diagnostic state OFF |
| Measurements | HTTP status; Vout_CH_X; diagnostic enable state |
| Expected result | Request rejected (4xx/401/403 as documented); channel remains OFF |
| Pass criterion | HTTP status in documented unauthorized set AND CH_X remains OFF electrically and in diagnostics. |
| Abort criterion | Channel ON |
| Evidence | HTTP log; measurement |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-B-013 — Service commands cannot bypass asserted kill

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-B-013` |
| Title | Service commands cannot bypass asserted kill |
| Linked IDs | `REQ-DCC-V-DK-037`, `REQ-DCC-V-DK-033` |
| Method | Test |
| Gate | DK-B |
| Classification | `MANDATORY` |
| Objective | With kill asserted, Service/UI output commands cannot energize represented channels. |
| Status | `NOT EXECUTED` |
| Preconditions | Kill path available (A-012 method); Service command path available; optional low-risk channel |
| Topology | Kill switch → IF-DK-KILL; Host/Service command path; DMM on represented channels |
| Equipment | Kill switch/fixture; HTTP or Service command client; DMM; PSU |
| Hazards | Kill path failure — keep loads minimal/safe |
| Test configuration | CFG-DK-SAFE-01 or config authorizing CH_X only for this negative test |
| Stimuli | Assert kill at t0; while asserted, send Service/UI enable for CH_X |
| Procedure | 1. Assert kill; confirm outputs OFF 2. Send Service enable CH_X 3. Measure all represented outputs for ≥5 s 4. Confirm rejection/ignored command in logs 5. De-assert kill only after commands stopped; confirm still OFF until explicit re-enable sequence |
| Measurements | Vout_chN; command result; kill state |
| Expected result | No channel ON while kill asserted |
| Pass criterion | Zero successful energizations from Service/UI while kill asserted AND all represented channels OFF. |
| Abort criterion | Any channel ON under kill |
| Evidence | command log; measurement table |
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
| Objective | Command a represented HS channel ON then OFF with a safe load; separate qualitative ON/OFF from quantitative OFF-time. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-014 (blocks quantitative t_off_ms criterion only); fixture: safe resistive load sized for CH_HS continuous verification current; impl: HS channel command + diagnostic path; electrical OFF observation convention not recorded as a closed threshold (use procedure convention below — do not invent a new TBD-DK ID) |
| Preconditions | Represented HS channel CH_HS selected; load connected only while channel commanded OFF (REQ-026); kill accessible; C-001 inventory lists CH_HS as Represented |
| Topology | Bench PSU → DevKit; CH_HS → safe resistive load; DMM or shunt measuring Vout (load+ to GND) and I_load in series; diagnostic host for channel state |
| Equipment | Lab PSU; DMM; current shunt or clamp; safe resistive load; diagnostic/command host |
| Hazards | Load heating — supervised; abort on smoke/uncontrolled current |
| Test configuration | CFG-DK-HS-ONOFF-01 authorizing CH_HS only; all other represented channels disabled |
| Stimuli | Command CH_HS ON; hold ≥5 s; command CH_HS OFF at t0 |
| Procedure | 1. Connect safe load while CH_HS OFF 2. Record Vin and ambient 3. Command ON 4. Measure Vout and I_load; read diagnostic state ON 5. Command OFF at t0 6. Sample Vout/I/diag until OFF 7. Record t_off_ms from t0 to electrical+diagnostic OFF |
| Measurements | Vin_V; Vout_V; I_load_A; diag_state; t_off_ms |
| Expected result | While ON: diagnostic state ON AND Vout indicates energized load (Vout ≈ Vin minus switch drop under load) AND I_load > 0. While OFF: diagnostic state OFF AND electrical OFF per observation convention: Vout ≤ 1.0 V relative to ground OR Vout ≤ 5% of Vin (verification observation convention only — not an approved product freeze) AND I_load ≈ 0. Quantitative t_off_ms acceptance remains TBD-DK-014. |
| Pass criterion | (Qualitative) ON: diag ON + Vout energized + I_load > 0; OFF: diag OFF + electrical OFF per observation convention. (Quantitative) t_off_ms ≤ approved TBD-DK-014. If TBD-DK-014 open: qualitative evidence may be recorded but case status remains BLOCKED (no full PASS). |
| Abort criterion | Uncontrolled current; smoke; load overtemperature |
| Evidence | measurement table; load identity; config identity; scope/meter log |
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
| Objective | Command PWM on a represented PWM channel and measure frequency/duty; acceptance vs approved frequency range blocked by TBD-DK-008. |
| Status | `BLOCKED` |
| Notes | Condition: PWM-capable channel physically represented and in DK-C scope. Else DEFERRED_EXCLUDED. Stimulus duty points below are verification stimuli, not approved product operating requirements. |
| Blocked by | ADR: —; TBD: TBD-DK-008 (blocks frequency-range acceptance only); fixture: safe load or measurement-only probe on CH_PWM; impl: PWM command path on represented channel |
| Preconditions | CH_PWM represented; kill accessible; scope/logic analyser available; load connected only while OFF if a load is used |
| Topology | Bench PSU → DevKit; CH_PWM output → (a) safe load OR (b) measurement-only high-impedance probe to GND; oscilloscope or logic analyser on CH_PWM switched node (and GND reference) |
| Equipment | Lab PSU; oscilloscope or logic analyser (≥10× expected PWM frequency sample capability); optional safe load; diagnostic/command host |
| Hazards | Load heating if loaded; probe ground loops |
| Test configuration | CFG-DK-PWM-01 authorizing CH_PWM PWM commands; record commanded frequency setpoint if config defines one |
| Stimuli | Verification stimulus duty points (not product requirements): 0%, 25%, 50%, 75%, 100% duty, each held ≥2 s; use commanded frequency from CFG-DK-PWM-01 if present, else firmware default (record actual) |
| Procedure | 1. Connect probe (and load if used) while OFF 2. For each duty point: command duty; capture ≥20 PWM periods 3. Measure frequency and duty from waveform 4. Record values without inventing tolerance 5. Return to 0%/OFF |
| Measurements | f_Hz; duty_meas_%; duty_cmd_%; waveform capture ID per point |
| Expected result | Output waveform is PWM (periodic pulsed drive) at each non-zero duty; at 0% output remains OFF per C-002 OFF convention; measured duty tracks commanded duty directionally (record measured duty; do not certify numeric duty tolerance unless an approved tolerance exists) |
| Pass criterion | Waveforms captured for all five stimulus points AND measured frequency within approved TBD-DK-008 when closed. If TBD-DK-008 open: record f_Hz/duty_meas; case remains BLOCKED for frequency acceptance. |
| Abort criterion | Uncontrolled current; smoke; shoot-through suspicion |
| Evidence | scope captures; measurement table; config identity |
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
| Blocked by | ADR: —; TBD: TBD-DK-009; fixture: calibrated shunt or clamp meter; impl: diagnostic current observation path on selected channel |
| Preconditions | Represented HS channel CH_I with current sense; safe known load; C-002 path available |
| Topology | CH_I → known resistive load; series shunt or clamp; diagnostic readout path |
| Equipment | Calibrated shunt or clamp meter; DMM; PSU; diagnostic host |
| Hazards | Load heating |
| Test configuration | CFG-DK-ISENSE-01 authorizing CH_I ON into the known load |
| Stimuli | Command CH_I ON for ≥5 s at steady load |
| Procedure | 1. Connect known load while OFF 2. Command ON 3. Measure I_meter at shunt/clamp 4. Read I_diag from diagnostic path 5. Compute abs(I_diag - I_meter) 6. Command OFF |
| Measurements | I_meter_A; I_diag_A; abs_error_A |
| Expected result | Error within approved TBD-DK-009 when closed |
| Pass criterion | abs(I_diag - I_meter) within approved TBD-DK-009. If TBD-DK-009 open: record both values; case remains BLOCKED (no qualitative accuracy PASS). |
| Abort criterion | Uncontrolled current; smoke |
| Evidence | measurement table; instrument identity |
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
| Blocked by | ADR: ADR-DK-010; TBD: TBD-DK-011; fixture: overcurrent fixture; impl: overcurrent protect path |
| Preconditions | Safe overcurrent fixture rated for test; kill accessible; single channel CH_OC |
| Topology | CH_OC → overcurrent fixture; current probe; diagnostic path |
| Equipment | Overcurrent fixture; current probe; PSU; diagnostic host |
| Hazards | Thermal/fire — supervised; abort on smoke |
| Test configuration | CFG-DK-OC-01 authorizing CH_OC only |
| Stimuli | Command CH_OC ON into overcurrent fixture at t0 |
| Procedure | 1. Arm fixture 2. Command ON at t0 3. Capture I(t) and fault flags until OFF/protect 4. Record t_protect_ms and peak current 5. Confirm latched/held safe state per policy 6. Clear per documented sequence |
| Measurements | I_peak_A; t_protect_ms; fault_code; output state |
| Expected result | Protect/OFF with fault; tolerance per TBD-DK-011 when approved |
| Pass criterion | Protect/OFF with observable fault AND timing/current meet approved TBD-DK-011. If TBD or fixture/ADR-DK-010 open: BLOCKED. |
| Abort criterion | Uncontrolled current beyond fixture rating; smoke |
| Evidence | waveform; fault log |
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
| Objective | Safe short-circuit fixture produces protect/OFF and fault indication. |
| Status | `BLOCKED` |
| Blocked by | ADR: ADR-DK-010; TBD: —; fixture: safe short fixture; impl: short protect path |
| Preconditions | Safe short fixture; kill accessible; CH_SC selected |
| Topology | CH_SC → safe short fixture; current probe; diagnostic path |
| Equipment | Safe short fixture; current probe; PSU; diagnostic host |
| Hazards | High current pulse — fixture-limited only |
| Test configuration | CFG-DK-SC-01 authorizing CH_SC only |
| Stimuli | Command CH_SC ON into short fixture at t0 |
| Procedure | 1. Verify fixture safe 2. Command ON at t0 3. Capture protect/OFF and fault 4. Confirm channel remains safe until clear 5. Clear per doc |
| Measurements | I_peak_A; t_protect_ms; fault_code |
| Expected result | Protect/OFF with fault; no fixture/DUT damage procedure beyond abort rules |
| Pass criterion | Channel enters protect/OFF with observable fault AND no continued commanded drive into short. If fixture/ADR-DK-010 open: BLOCKED. |
| Abort criterion | Fixture failure; smoke; sustained uncontrolled current |
| Evidence | waveform; fault log |
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
| Objective | Confirm open-load indication on a channel that claims that diagnostic. |
| Status | `BLOCKED` |
| Notes | Condition: selected implementation claims open-load diagnostic on the tested channel. Else DEFERRED_EXCLUDED. |
| Blocked by | ADR: —; TBD: —; fixture: open-load / disconnected-load fixture; impl: open-load diagnostic claimed on channel + firmware support |
| Preconditions | Channel CH_OL selected with claimed open-load diagnostic; C-002 path available |
| Topology | CH_OL output open (no load) or open-load fixture; diagnostic path |
| Equipment | Open-load fixture or safe open connection; diagnostic host; PSU |
| Hazards | Do not short; supervised |
| Test configuration | CFG-DK-OL-01 authorizing CH_OL ON for diagnostic probe |
| Stimuli | Command CH_OL ON with load open at t0 |
| Procedure | 1. Confirm open connection 2. Command ON 3. Observe open-load indication within documented window 4. Command OFF 5. Export diag log |
| Measurements | open_load_flag; timestamps; Vout |
| Expected result | Open-load indication asserted while commanded ON into open load |
| Pass criterion | open_load_flag true while ON into open load per implementation claim. If claim absent: DEFERRED_EXCLUDED. If claim present but fixture/impl missing: BLOCKED. |
| Abort criterion | Uncontrolled current; smoke |
| Evidence | diagnostic log; fixture note |
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
| Objective | Apply a controlled supply undervoltage and observe output/diagnostic reaction per approved TBD-DK-012 table when closed. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-012 (UV threshold, reaction table, recovery threshold); fixture: programmable PSU capable of controlled ramp/step; impl: UV detection/reaction path on DevKit |
| Preconditions | A-003 bring-up path available; programmable PSU; optional low-risk represented channel may be ON only if reaction table requires observing an ON→OFF transition; kill accessible |
| Topology | Programmable PSU → IF-DK-PWR-IN; DMM/logger on Vin at power-entry sense point (IF-DK-VBATT-SENSE or entry TP); diagnostic host; optional CH_UV → safe load if ON-state observation required by reaction table |
| Equipment | Programmable lab PSU with voltage programming; DMM or data logger on Vin; diagnostic/command host; optional safe load |
| Hazards | Brown-out instability — supervised; abort on smoke/uncontrolled behaviour |
| Test configuration | CFG-DK-UV-01: either all outputs OFF, or single low-risk CH_UV authorized ON if needed to observe UV reaction on an energized channel (record choice) |
| Stimuli | 1) Start at nominal Vin candidate 13.8 V (docs/008 candidate — not normative; actual start value recorded) 2) Controlled step or ramp to UV stimulus voltage defined by TBD-DK-012 when approved 3) Hold ≥5 s 4) Recover to nominal per TBD-DK-012 recovery threshold when approved |
| Procedure | 1. Energize at recorded nominal Vin; note output/diag states 2. If CFG requires CH_UV ON, command ON and confirm 3. Apply UV stimulus (ramp rate or step recorded) measuring Vin at entry sense point 4. Observe diagnostic UV/fault flags and all represented output states 5. Hold 6. Recover Vin to nominal 7. Observe recovery behaviour per table 8. Export Vin and state timelines |
| Measurements | Vin_V timeline; output states; diagnostic UV/fault flags; timestamps |
| Expected result | Per approved TBD-DK-012 reaction table (outputs/diagnostics at UV and after recovery). Until closed: procedure is ready; no qualitative PASS. |
| Pass criterion | Observed states equal approved TBD-DK-012 reaction table including timing if specified. If TBD-DK-012 open: BLOCKED. |
| Abort criterion | Smoke; uncontrolled current; loss of safe control |
| Evidence | Vin CSV; diagnostic timeline; config identity; PSU program record |
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
| Objective | Record temperature and electrical data under a controlled load profile for thermal observation. |
| Status | `BLOCKED` |
| Notes | Condition: thermal observation required for represented channel protection in tested scope. Else DEFERRED_EXCLUDED. |
| Blocked by | ADR: ADR-DK-011; TBD: TBD-DK-010, TBD-DK-018, TBD-DK-019; fixture: controlled load and temperature-measurement fixture not defined; impl: on-board or external temperature observation path for Power domain |
| Preconditions | Represented channel CH_TH selected; kill accessible; temperature sensor path identified (on-board NTC/IF-DK-TEMP or external meter at documented point) |
| Topology | Bench PSU → DevKit; CH_TH → controlled load (when fixture defined); temperature sensor at documented measurement point; DMM/shunt for V/I; diagnostic host |
| Equipment | Lab PSU; controlled load (when fixture defined); temperature meter or logged sensor; DMM/shunt; diagnostic host; stopwatch/logger |
| Hazards | Thermal burn / load overheating — abort if temperature rises uncontrollably or exceeds provisional operator-safe stop (operator judgment until TBD-DK-019 approved) |
| Test configuration | CFG-DK-THERM-01 authorizing CH_TH only; load profile: steady ON into controlled load for duration D (D from TBD-DK-018 when approved) |
| Stimuli | Command CH_TH ON at t0; hold for duration D; command OFF |
| Procedure | 1. Record ambient temperature T_amb 2. Confirm sensor point 3. Command ON 4. Sample temperature at ≥1 Hz for duration D 5. Concurrently sample V/I at ≥1 Hz 6. Command OFF 7. Continue sampling ≥30 s cooldown 8. Export dataset |
| Measurements | T_amb_C; T_sensor_C timeline; Vout; I_load; timestamps; sample_interval_s |
| Expected result | Complete dataset: ambient, temperature timeline, V/I timeline for ON and cooldown. Absolute limit / accuracy PASS only after TBD-DK-010/018/019 and ADR-DK-011 closure. |
| Pass criterion | Dataset complete at ≥1 Hz for approved TBD-DK-018 duration AND temperature accuracy/limit criteria meet TBD-DK-010/019 when approved. If ADR/TBD/fixture open: BLOCKED. |
| Abort criterion | Smoke; uncontrolled current; temperature rise judged unsafe by operator before TBD-DK-019 exists |
| Evidence | temp/electrical CSV; fixture definition note; config identity |
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
| Supersession | Stall portion split to C-013 |
| Notes | Condition: bidirectional channel physically represented. Else DEFERRED_EXCLUDED. |
| Preconditions | BD channel CH_BD represented; safe motor/load connected while OFF; kill accessible |
| Topology | CH_BD → safe bidirectional load/motor; current probe; diagnostic path |
| Equipment | Safe motor/load; current probe or shunt; PSU; command host |
| Hazards | Shoot-through; mechanical hazard — use low voltage/current safe load |
| Test configuration | CFG-DK-BD-DIR-01 authorizing CH_BD forward/reverse commands |
| Stimuli | Forward command 2 s; OFF/coast per config; reverse command 2 s; then conflicting simultaneous forward+reverse command attempt |
| Procedure | 1. Connect load while OFF 2. Command forward 2 s; record direction signature (current/back-EMF/diag) 3. OFF/coast 4. Command reverse 2 s; record signature 5. Issue conflicting command sequence 6. Confirm prevention/fault 7. OFF |
| Measurements | direction indicator or current signature; fault flags; V/I |
| Expected result | Forward and reverse signatures distinct; conflicting command rejected/faulted without simultaneous opposing drive |
| Pass criterion | Forward command produces forward direction signature; reverse produces reverse; conflicting command does not produce simultaneous opposing drive (fault or rejection recorded). |
| Abort criterion | Shoot-through suspicion; smoke; uncontrolled current |
| Evidence | current waveform; logs; video optional |
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
| Notes | Condition: BD represented. May share evidence with C-010 but has separate status. |
| Preconditions | CH_BD represented; safe load; test API or dual-command path available |
| Topology | CH_BD → safe load; logic/enable capture if available; diagnostic path |
| Equipment | Command host; optional logic analyzer on bridge enables; PSU |
| Hazards | Shoot-through |
| Test configuration | CFG-DK-BD-DIR-01 |
| Stimuli | Issue simultaneous opposing drive commands (forward+reverse) via test API at t0 |
| Procedure | 1. Ensure OFF 2. Issue conflicting commands 3. Observe driver enables/fault for ≥2 s 4. Confirm no simultaneous opposing enable 5. Clear fault per doc |
| Measurements | enable_line states or diag fault; I_load |
| Expected result | Rejection/fault; no simultaneous opposing enable |
| Pass criterion | No simultaneous opposing enable measured; rejection/fault recorded. |
| Abort criterion | Shoot-through suspicion; smoke |
| Evidence | logic capture or diag log |
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
| Preconditions | RT programmed; CFG-DK-VCM-01 available; diagnostic/event log export available |
| Topology | DevKit powered; Service/diagnostic host; no loads required for mode-only steps |
| Equipment | Config/diagnostic host; PSU; event log capture |
| Hazards | Mode rules enabling outputs — keep output enables disabled in this config except where mode table requires |
| Test configuration | CFG-DK-VCM-01 defining modes OFF → READY → ENGINE_RUN (names per profile) and disallowed transition E_bad |
| Stimuli | Documented input events/telemetry E1 (OFF→READY), E2 (READY→ENGINE_RUN), E_bad (disallowed) |
| Procedure | 1. Reset to OFF 2. Apply E1; record mode+timestamp 3. Apply E2; record 4. Apply E_bad; confirm no mode change 5. Export event log fields mode_from, mode_to, reason, timestamp |
| Measurements | mode timeline; event log fields |
| Expected result | Sequence [OFF→READY, READY→ENGINE_RUN]; E_bad ignored |
| Pass criterion | Observed sequence equals [OFF→READY, READY→ENGINE_RUN]; E_bad produces zero mode change; each required transition appears in event log with mode_from/mode_to/timestamp. |
| Abort criterion | Unexpected channel ON; smoke |
| Evidence | event log JSON; mode timeline; config identity |
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
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-006; fixture: ECU simulator; impl: VCM telem path |
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
| Objective | Execute one documented cooling/load rule and prove thresholds come from configuration. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: —; fixture: safe load on CH_COOL; impl: VCM rule engine + CFG-DK-RULE-01 artifact buildable/loadable on DevKit; ECU/telem injector |
| Preconditions | D-002/D-004 paths available or equivalent; CH_COOL represented; safe load available |
| Topology | ECU/telem injector ↔ CAN ↔ DevKit; CH_COOL → safe load; DMM/shunt; diagnostic host |
| Equipment | Telem injector (ECU sim); CAN sniffer; DMM or current shunt; PSU; config tool |
| Hazards | Unexpected multi-channel enable — authorize only CH_COOL |
| Test configuration | CFG-DK-RULE-01 identity recorded (config ID/schema/hash when available). Rule R_COOL: when `coolant_temp` ≥ `T_on` enable CH_COOL; when `coolant_temp` ≤ `T_off` disable CH_COOL. Values `T_on` and `T_off` SHALL be read from the loaded configuration record (not hardcoded in the procedure). Expected transition table: (temp=`T_on`-5 → CH_COOL OFF); (temp=`T_on`+5 → CH_COOL ON); (temp=`T_off`-1 → CH_COOL OFF). |
| Stimuli | Inject ENGINE_TELEM (or documented coolant_temp signal) sequence: hold `T_on`-5 for 5 s; step to `T_on`+5 for 10 s; step to `T_off`-1 for 10 s. Period P as in injector script (record actual). |
| Procedure | 1. Load CFG-DK-RULE-01; export `T_on`,`T_off` from active config 2. Connect safe load to CH_COOL while OFF 3. Inject temp=`T_on`-5; observe CH_COOL OFF 4. Step to `T_on`+5; measure t_on_ms from step to ON 5. Step to `T_off`-1; measure t_off_ms to OFF 6. Verify thresholds used equal exported config values 7. Export scenario log |
| Measurements | coolant_temp timeline; CH_COOL V/I or diag state; t_on_ms; t_off_ms; config `T_on`/`T_off` |
| Expected result | Transitions match CFG-DK-RULE-01 expected transition table; thresholds equal config |
| Pass criterion | CH_COOL OFF at `T_on`-5; ON after crossing `T_on`+5; OFF after `T_off`-1; exported `T_on`/`T_off` equal values used in the stimulus plan; scenario log contains timestamps, temps, output states. If CFG-DK-RULE-01 cannot be built/loaded: remain BLOCKED. |
| Abort criterion | Unintended channel ON; smoke; uncontrolled current |
| Evidence | config export; scenario log JSON; sniffer; output samples |
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
| Objective | Integrated Button Box event changes a represented output per an explicit expected-results table. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: —; fixture: Button Box DCP simulator; impl: CFG-DK-BB-02 artifact + RT mapping of BB event to channel; DCP Button Box message ID defined in Accepted protocol baseline |
| Preconditions | B-004 path available; CH_BB represented; safe load |
| Topology | Button Box simulator ↔ IF-DK-CAN ↔ DevKit; sniffer tap; CH_BB → safe load; DMM |
| Equipment | BB/DCP simulator; CAN sniffer; DMM; PSU; config tool |
| Hazards | Unexpected enable — single-channel authorization only |
| Test configuration | CFG-DK-BB-02 with explicit expected-results table embedded in the config package / accompanying test record: Event `BB_EVT_TOGGLE_1` (control_id recorded); Initial CH_BB=OFF; After first event → CH_BB=ON; After second event → CH_BB=OFF. Debounce: ignore duplicate events within 100 ms if config defines debounce; else record actual. |
| Stimuli | From BB simulator: send `BB_EVT_TOGGLE_1` at t1; wait ≥500 ms; send second `BB_EVT_TOGGLE_1` at t2 |
| Procedure | 1. Load CFG-DK-BB-02; confirm expected-results table present in evidence pack 2. Set initial CH_BB OFF 3. Start sniffer 4. Inject first event; observe CH_BB ON 5. Inject second event; observe CH_BB OFF 6. Compare to expected-results table 7. Export CAN + output log |
| Measurements | event timestamps; CH_BB state before/after each event; CAN frames |
| Expected result | Per CFG-DK-BB-02 expected-results table (OFF→ON→OFF) |
| Pass criterion | Actual CH_BB states equal CFG-DK-BB-02 expected-results table for both events AND sniffer shows both BB frames AND no other represented channel changes state. If DCP ID or CFG-DK-BB-02 unavailable: BLOCKED. |
| Abort criterion | Unintended multi-channel enable; smoke |
| Evidence | CFG-DK-BB-02 expected-results table copy; sniffer; output log |
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
| Objective | Service restart does not force an RT fail-operational represented output OFF. |
| Status | `NOT EXECUTED` |
| Preconditions | Fail-operational function F_FO mapped to represented channel CH_FO; RT path can hold CH_FO ON without Service; Service restart method documented (Radio power-cycle or Service reboot command) |
| Topology | DevKit Logic+Power (+Radio); CH_FO → safe load; DMM/shunt sampling CH_FO; Service restart actuator |
| Equipment | DMM or data-logger sampling Vout/I at ≥10 Hz; PSU; Service reboot method; safe load |
| Hazards | Loss of cooling/load during test — use low-risk CH_FO only |
| Test configuration | CFG-DK-FO-01: rule/state that holds CH_FO ON from RT/VCM without Service dependency |
| Stimuli | Place CH_FO ON via RT path; at t0 restart Service (Radio power-cycle or documented reboot); observe for restart window 10 s |
| Procedure | 1. Apply CFG-DK-FO-01 2. Command/establish CH_FO ON via RT; confirm ON 3. Start sampling ≥10 Hz 4. Restart Service at t0 5. Sample continuously for 10 s 6. Record Service down/up indications 7. Confirm CH_FO still ON at end |
| Measurements | Vout_CH_FO or I_CH_FO samples at ≥10 Hz for 10 s; Service state timeline |
| Expected result | CH_FO remains ON; Service may restart independently |
| Pass criterion | Over the 10 s window at ≥10 Hz sampling, zero samples indicate CH_FO OFF (criterion = zero observed OFF samples). Instrument limitation: OFF pulses shorter than one sample period (≤100 ms at 10 Hz) may be undetected — record sample rate and instrument model. No separate approved glitch TBD is used; if a future TBD defines a glitch limit it shall supersede this criterion via register update. |
| Abort criterion | Uncontrolled current; smoke; inability to confirm RT ownership of CH_FO |
| Evidence | sample CSV; Service restart log; config identity |
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
| Objective | Browser/Tablet disconnect does not stop fail-operational RT output. |
| Status | `NOT EXECUTED` |
| Preconditions | Active Tablet/WebSocket (or REST long-poll) client connected; CH_FO ON via RT fail-operational path (CFG-DK-FO-01); Service may remain up |
| Topology | Tablet/browser client ↔ Service Wi-Fi/WS; DevKit RT+Power; CH_FO → safe load; DMM sampling |
| Equipment | Tablet or browser client; DMM/data-logger ≥10 Hz; PSU; safe load |
| Hazards | Low-risk channel only |
| Test configuration | CFG-DK-FO-01; client subscribed to telemetry/status |
| Stimuli | Disconnect client: close WebSocket / disable Wi-Fi on client / navigate away — record method used |
| Procedure | 1. Establish client connection; confirm telemetry flowing 2. Confirm CH_FO ON 3. Start ≥10 Hz sampling 4. Disconnect client at t0 5. Sample 10 s 6. Record Service health (may stay up) and RT mode 7. Confirm CH_FO ON |
| Measurements | Vout/I samples; client connection state; Service health; RT mode |
| Expected result | CH_FO remains ON; RT continues; Service may show client lost without forcing outputs OFF |
| Pass criterion | Zero CH_FO OFF samples over 10 s at ≥10 Hz AND RT remains in operable mode executing F_FO AND client shows disconnected. |
| Abort criterion | CH_FO OFF due to disconnect; smoke |
| Evidence | sample CSV; client disconnect note; Service/RT state snapshot |
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
| Objective | Losing simulated ECU yields defined stale/LOST reaction without damaging the bus. |
| Status | `BLOCKED` |
| Blocked by | ADR: —; TBD: TBD-DK-006; fixture: ECU simulator with clean disconnect; impl: stale/LOST handling + VCM inhibit rules in CFG-DK-SCEN-ECU-01 |
| Preconditions | B-002/B-003 paths available; CFG-DK-SCEN-ECU-01 loaded; initial VCM state READY or ENGINE_RUN per config |
| Topology | ECU sim ↔ linear CAN ↔ DevKit; sniffer tap; optional CH_COOL load; termination per B-005 intent |
| Equipment | ECU simulator; CAN sniffer; PSU; diagnostic host |
| Hazards | Rule-driven enables — low-risk channels only |
| Test configuration | CFG-DK-SCEN-ECU-01: ENGINE_TELEM period P; on LOST/stale after TBD-DK-006 inhibit new CH_COOL enable and/or required safe action recorded in config |
| Stimuli | Stream ENGINE_TELEM for ≥10 s; at t_stop stop simulator (silent bus from ECU node); do not short CAN_H/CAN_L |
| Procedure | 1. Start sniffer 2. Establish telem; note VCM state 3. Stop ECU sim at t_stop 4. Poll status until LOST/stale 5. Confirm expected inhibit/output behaviour per CFG 6. Confirm sniffer still sees DevKit HEARTBEAT (bus remains valid) 7. Export timeline |
| Measurements | t_lost_ms; VCM/status; CH_COOL state; HEARTBEAT continuity |
| Expected result | LOST/stale per TBD-DK-006; configured inhibit; bus still carries DevKit traffic |
| Pass criterion | Lost/stale indication within approved TBD-DK-006 window AND configured output inhibition/unchanged behaviour met AND DevKit HEARTBEAT continues (bus not destroyed). If TBD-DK-006 open: BLOCKED. |
| Abort criterion | Bus shorting; smoke; unintended multi-channel enable |
| Evidence | timeline log; sniffer; config identity |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |


#### VER-DCC-DK-D-015 — Valid configuration apply (authorized path)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-015` |
| Title | Valid configuration apply (authorized path) |
| Linked IDs | `REQ-DCC-V-DK-084`, `REQ-DCC-V-DK-087` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Apply a valid safe configuration via the authorized boot-time or Service/Wiring-mode path. |
| Status | `NOT EXECUTED` |
| Supersession | Hot-reload and reject/atomicity portions split to D-007, D-008, D-011, D-018 |
| Preconditions | Config transfer path available (B-007); authorized apply mode available (boot or Service/Wiring as documented) |
| Topology | Host/Service ↔ IF-DK-CFG/DCPI ↔ RT; outputs uncommanded; DMM on represented channels |
| Equipment | Config transfer tool; PSU; DMM; logs |
| Hazards | Mis-enable — valid config must be safe |
| Test configuration | CFG-DK-SAFE-01 (all channels disabled); record config ID/schema/hash |
| Stimuli | Transfer and apply CFG-DK-SAFE-01 in authorized mode |
| Procedure | 1. Record firmware identity 2. Transfer CFG-DK-SAFE-01 3. Apply in authorized mode 4. Confirm apply ack 5. Read back active config identity 6. Measure all represented outputs OFF |
| Measurements | apply_result; active_config_id; Vout_chN |
| Expected result | Apply accepted; identity matches; outputs OFF |
| Pass criterion | apply_result=accepted AND active_config_id matches CFG-DK-SAFE-01 AND all represented outputs OFF. |
| Abort criterion | Any channel ON |
| Evidence | apply log; config identity; output table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |



#### VER-DCC-DK-D-007 — Invalid configuration capacity/schema rejection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-007` |
| Title | Invalid configuration capacity/schema rejection |
| Linked IDs | `REQ-DCC-V-DK-085`, `REQ-DCC-V-DK-088` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Reject a configuration that exceeds channel capacity or fails schema checks without energizing outputs. |
| Status | `NOT EXECUTED` |
| Preconditions | D-015 valid-apply path available; ability to craft invalid config (oversize channel count or invalid schema field) |
| Topology | Host/Service ↔ config path ↔ RT; DMM on represented channels |
| Equipment | Config transfer tool; PSU; DMM |
| Hazards | None if reject works — monitor outputs |
| Test configuration | CFG-DK-INVALID-CAP-01: deliberately exceeds represented channel capacity or violates schema (document exact violation in test record) |
| Stimuli | Attempt apply of CFG-DK-INVALID-CAP-01 in authorized mode |
| Procedure | 1. Note baseline outputs OFF and active config 2. Transfer/apply invalid config 3. Confirm reject (no apply ack) 4. Confirm active config unchanged or safe 5. Measure outputs remain OFF |
| Measurements | apply_result; active_config_id; Vout_chN |
| Expected result | Rejected; no new channel ON |
| Pass criterion | apply_result=rejected AND no represented channel newly ON AND prior safe active config retained or system remains in documented safe config state. |
| Abort criterion | Any channel ON due to rejected apply |
| Evidence | apply/reject log; output table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-008 — Corrupt configuration payload rejection

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-008` |
| Title | Corrupt configuration payload rejection |
| Linked IDs | `REQ-DCC-V-DK-085`, `REQ-DCC-V-DK-099` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Reject truncated/corrupt configuration payloads without partial unsafe enable. |
| Status | `NOT EXECUTED` |
| Preconditions | Config path available; corrupt-payload injection method available |
| Topology | Host/Service ↔ DCPI/config path ↔ RT; DMM on outputs |
| Equipment | Transfer tool with truncation/bit-flip capability; PSU; DMM |
| Hazards | Partial apply |
| Test configuration | Base payload CFG-DK-SAFE-01; create truncated and CRC-corrupted variants (≥1 each) |
| Stimuli | Apply truncated payload; apply CRC-corrupted payload |
| Procedure | 1. Baseline OFF 2. Send truncated payload; expect reject 3. Send corrupted payload; expect reject 4. Confirm no channel ON 5. Optionally apply valid CFG-DK-SAFE-01 to confirm path recovery |
| Measurements | reject counts; output states |
| Expected result | Both invalid payloads rejected; outputs OFF |
| Pass criterion | Truncated and corrupted payloads rejected AND zero represented channels newly ON. |
| Abort criterion | Partial enable observed |
| Evidence | transfer log; output table |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-011 — Configuration hot-reload authorization policy

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-011` |
| Title | Configuration hot-reload authorization policy |
| Linked IDs | `REQ-DCC-V-DK-084` |
| Method | Test |
| Gate | DK-D |
| Classification | `CONDITIONAL_MANDATORY` |
| Objective | Determine whether hot-reload outside Service/Wiring modes is authorized; execute only if ADR-DK-009 accepts it. |
| Status | `BLOCKED` |
| Notes | Governed by DK-GOV-011 and ADR-DK-009. Condition: ADR-DK-009 Accepted allowing hot-reload in scope. Else DEFERRED_EXCLUDED from gate (do not claim hot-reload verified). |
| Blocked by | ADR: ADR-DK-009; TBD: —; fixture: —; impl: hot-reload path if authorized; governance: DK-GOV-011 |
| Preconditions | D-015 path available; system in non-Service/Wiring mode if testing negative authorization |
| Topology | Host/Service ↔ config path ↔ RT |
| Equipment | Config tool; PSU; logs |
| Hazards | Unexpected mode change |
| Test configuration | CFG-DK-SAFE-01 variant B differing only in non-safety annotation/field |
| Stimuli | Attempt apply while not in authorized mode (negative) OR in authorized hot-reload mode if ADR accepts |
| Procedure | 1. Record ADR-DK-009 status 2. If not Accepted for hot-reload: mark DEFERRED_EXCLUDED / keep BLOCKED — do not invent permission 3. If Accepted: execute authorized hot-reload apply and confirm success without unsafe enable |
| Measurements | apply_result; mode; output states |
| Expected result | Per ADR-DK-009 decision |
| Pass criterion | Only if ADR-DK-009 Accepted: hot-reload apply behaves per ADR; outputs remain safe. Otherwise case shall not be certified PASS. |
| Abort criterion | Unsafe enable |
| Evidence | ADR citation; apply log |
| Test owner (raw) | Implementation Engineer / lab operator |
| Certification owner | Independent Reviewer / Test Owner |

#### VER-DCC-DK-D-018 — Configuration apply atomicity (no partial unsafe enable)

| Field | Content |
|-------|---------|
| Verification ID | `VER-DCC-DK-D-018` |
| Title | Configuration apply atomicity (no partial unsafe enable) |
| Linked IDs | `REQ-DCC-V-DK-087`, `REQ-DCC-V-DK-088` |
| Method | Test |
| Gate | DK-D |
| Classification | `MANDATORY` |
| Objective | Interrupted or failed apply does not leave a partial unsafe enable mask. |
| Status | `NOT EXECUTED` |
| Preconditions | Config path available; method to interrupt transfer (disconnect Service/DCPI mid-apply) or force fail apply |
| Topology | Host/Service ↔ config path ↔ RT; DMM on all represented channels |
| Equipment | Config tool; controllable link interrupt; DMM; PSU |
| Hazards | Partial enable |
| Test configuration | CFG-DK-PARTIAL-01: multi-channel enable mask that would turn ON ≥2 channels if fully applied; use only with interrupt/fail before completion |
| Stimuli | Start apply of CFG-DK-PARTIAL-01; interrupt mid-transfer OR inject fail; observe end state |
| Procedure | 1. Baseline all OFF with CFG-DK-SAFE-01 2. Start apply PARTIAL-01 3. Interrupt/fail before completion 4. Wait settle 5. Measure all channels 6. Confirm active config not a partial unsafe mask (SAFE retained or documented fail state with all OFF) |
| Measurements | Vout_chN; active_config_id; apply_result |
| Expected result | No subset of PARTIAL-01 enables active; outputs OFF |
| Pass criterion | Zero represented channels ON after interrupted/failed apply AND active config is not a partially applied enable mask. |
| Abort criterion | Any channel ON after failed apply |
| Evidence | apply log; output table |
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
| Objective | Safety-relevant fault is logged; persistence behaviour is explicit. |
| Status | `NOT EXECUTED` |
| Preconditions | Documented fault-injection or diagnostic event F_SAFE available that does not require unresolved ADR-DK-010 destructive fixtures (prefer software/test-event inject); log export path available |
| Topology | DevKit powered; diagnostic/log host; no destructive loads required |
| Equipment | Diagnostic host; PSU; optional non-destructive event injector |
| Hazards | Prefer non-destructive F_SAFE |
| Test configuration | CFG-DK-SAFE-01; test record declares persistence_required = YES or NO for this run |
| Stimuli | Inject fault/event F_SAFE at t0 |
| Procedure | 1. Clear or note log baseline 2. Inject F_SAFE 3. Read log contains F_SAFE with type+timestamp 4. If persistence_required=YES: power-cycle/reset; confirm F_SAFE still present 5. If NO: reset; confirm absence and document volatile-only |
| Measurements | log entries before/after reset; timestamps |
| Expected result | F_SAFE logged; persistence matches declared requirement |
| Pass criterion | F_SAFE present with type+timestamp before reset; after reset present iff persistence_required=YES, else absence documented as volatile-only. |
| Abort criterion | Destructive fault escalation; smoke |
| Evidence | logs before/after; persistence declaration |
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
| Preconditions | Represented channels exist; optional prior ON on low-risk channel to prove transition to OFF after cycle |
| Topology | Bench PSU → DevKit; DMM on all represented channel outputs |
| Equipment | Lab PSU; DMM; diagnostic host |
| Hazards | Unexpected residual enable |
| Test configuration | After recovery, active config shall be absent or CFG-DK-SAFE-01 only — no auto-enable mask |
| Stimuli | Full power cycle (remove Vin ≥5 s; re-apply) |
| Procedure | 1. Optionally command one low-risk channel ON 2. Power cycle 3. Wait READY/operable 4. Measure all represented outputs 5. Confirm diagnostic enables OFF 6. Confirm authorized config re-apply required before ON |
| Measurements | Vout_chN; diagnostic enable mask; mode |
| Expected result | All outputs OFF until explicit authorized enable/config apply |
| Pass criterion | All represented outputs OFF after recovery until explicit authorized enable/config apply. |
| Abort criterion | Any channel ON after recovery without authorization; smoke |
| Evidence | post-reset measurement table; identity sheet |
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

> TBD meanings: authoritative register in [`DevKit_System_Requirements.md`](DevKit_System_Requirements.md) §4. Exact IDs only.
> Placeholder policy (R3/R4): bare `—` / `As required` only when the missing item is named in `Blocked by`. Numeric TBDs do not conceal undefined topology/equipment.

| Verification ID | Gate | Classification | Blocking ADR | Blocking TBD | Fixture dependency | Implementation dependency | Resulting gate effect |
|-----------------|------|----------------|--------------|--------------|--------------------|---------------------------|-----------------------|
| `VER-DCC-DK-A-003` | DK-A | MANDATORY | ADR-DK-006 | TBD-DK-001, TBD-DK-017 | Documented rail test points | Programmed RT image capable of default OFF | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-008` | DK-A | MANDATORY | ADR-DK-001 | TBD-DK-007 | J_LP connection access | RT+Power firmware supporting J_LP | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-011` | DK-A | MANDATORY | ADR-DK-007 | TBD-DK-005 (response-time acceptance) | Safe WDT injection method | RT watchdog path that de-energizes outputs | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-012` | DK-A | MANDATORY | ADR-DK-007 | TBD-DK-004 (kill response-time acceptance) | kill switch or nKILL_HW assert method on IF-DK-KILL | kill de-energize path independent of Service | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-014` | DK-A | MANDATORY | — | TBD-DK-021 (post-kill explicit re-enable sequence definition) | kill switch/fixture | documented re-enable sequence in software/procedure | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-A-015` | DK-A | CONDITIONAL_MANDATORY | — | TBD-DK-020 (encoding→revision map acceptance) | N/A — uses on-board BOARD_ID sense path | BOARD_ID readout path in RT/diagnostics | Blocks DK-A PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-A-016` | DK-A | MANDATORY | — | TBD-DK-014 (blocks quantitative commanded-OFF timing if OFF-command timing step is certified) | N/A for default-OFF survey | RT default-OFF behaviour on represented channels | Gate DK-A cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-003` | DK-B | MANDATORY | — | TBD-DK-006 (lost/stale timeout acceptance) | ECU simulator with clean stop/silent | ECU node status / LOST path in RT | Gate DK-B cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-005` | DK-B | MANDATORY | — | TBD-DK-015 (waveform acceptance metrics) | CAN differential probe / scope | N/A for termination presence (physical) | Gate DK-B cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-B-011` | DK-B | CONDITIONAL_MANDATORY | — | TBD-DK-016 (duration and allowed loss) | N/A — host WS client | Service WebSocket telemetry path | Blocks DK-B PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-C-002` | DK-C | MANDATORY | — | TBD-DK-014 (blocks quantitative t_off_ms criterion only) | safe resistive load sized for CH_HS continuous verification current | HS channel command + diagnostic path | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-003` | DK-C | CONDITIONAL_MANDATORY | — | TBD-DK-008 (blocks frequency-range acceptance only) | safe load or measurement-only probe on CH_PWM | PWM command path on represented channel | Blocks DK-C PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-C-004` | DK-C | MANDATORY | — | TBD-DK-009 | calibrated shunt or clamp meter | diagnostic current observation path on selected channel | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-005` | DK-C | MANDATORY | ADR-DK-010 | TBD-DK-011 | overcurrent fixture | overcurrent protect path | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-006` | DK-C | MANDATORY | ADR-DK-010 | — | safe short fixture | short protect path | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-007` | DK-C | CONDITIONAL_MANDATORY | — | — | open-load / disconnected-load fixture | open-load diagnostic claimed on channel + firmware support | Blocks DK-C PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-C-008` | DK-C | MANDATORY | — | TBD-DK-012 (UV threshold, reaction table, recovery threshold) | programmable PSU capable of controlled ramp/step | UV detection/reaction path on DevKit | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-009` | DK-C | CONDITIONAL_MANDATORY | ADR-DK-011 | TBD-DK-010, TBD-DK-018, TBD-DK-019 | controlled load and temperature-measurement fixture not defined | on-board or external temperature observation path for Power domain | Blocks DK-C PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-C-012` | DK-C | MANDATORY | — | TBD-DK-007 | controllable J_LP/SPI disconnect | RT+Power timeout handler | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-C-013` | DK-C | CONDITIONAL_MANDATORY | — | TBD-DK-022 | stall/locked-rotor fixture | stall detect/protect path | Blocks DK-C PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-C-014` | DK-C | MANDATORY | — | TBD-DK-013 | recoverable fault injection method | retry/latch policy | Gate DK-C cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-004` | DK-D | MANDATORY | — | TBD-DK-006 | ECU simulator | VCM telem path | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-005` | DK-D | MANDATORY | — | — | safe load on CH_COOL | VCM rule engine + CFG-DK-RULE-01 artifact buildable/loadable on DevKit | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-006` | DK-D | MANDATORY | — | — | Button Box DCP simulator | CFG-DK-BB-02 artifact + RT mapping of BB event to channel | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |
| `VER-DCC-DK-D-011` | DK-D | CONDITIONAL_MANDATORY | ADR-DK-009 | — | — | hot-reload path if authorized | Blocks DK-D PASS only when condition applies; else DEFERRED_EXCLUDED |
| `VER-DCC-DK-D-014` | DK-D | MANDATORY | — | TBD-DK-006 | ECU simulator with clean disconnect | stale/LOST handling + VCM inhibit rules in CFG-DK-SCEN-ECU-01 | Gate DK-D cannot PASS while this MANDATORY case is BLOCKED |


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

- **MANDATORY:** `VER-DCC-DK-D-002`, `VER-DCC-DK-D-003`, `VER-DCC-DK-D-004`, `VER-DCC-DK-D-005`, `VER-DCC-DK-D-006`, `VER-DCC-DK-D-007`, `VER-DCC-DK-D-008`, `VER-DCC-DK-D-012`, `VER-DCC-DK-D-013`, `VER-DCC-DK-D-014`, `VER-DCC-DK-D-015`, `VER-DCC-DK-D-016`, `VER-DCC-DK-D-017`, `VER-DCC-DK-D-018`, `VER-DCC-DK-D-019`, `VER-DCC-DK-G-003` (D-020 superseded by G-001/G-003 — do not separately certify)
- **CONDITIONAL_MANDATORY:** `VER-DCC-DK-D-011` (ADR-DK-009 hot-reload)

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
| System cases A–D | 63 |
| Governance cases G | 4 |
| Total cases | 67 |
| Method: Test | 51 |
| Test BLOCKED | 26 |
| Test NOT EXECUTED (complete setup) | 25 |


## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial plan |
| 1.1 | 2026-07-19 | WP-007-R1 — method schemas; splits; gate classifications; identity rule |
| 1.1.1 | 2026-07-19 | WP-007-R1 corrections — restore A-004/B-001/B-002 meanings; add A-006/A-007; D-020 supersession; schema fixes |
| 1.1.2 | 2026-07-19 | WP-007-R2 — TBD register references; A-006 identity-only blockers; blocked matrix exact IDs |
| 1.1.3 | 2026-07-19 | WP-007-R3 — Test-case completeness audit; D-015 split; placeholder policy |
| 1.1.4 | 2026-07-19 | WP-007-R4 — semantic placeholder enforcement; C-002/003/008/009 and related Test cases completed |
| 1.2 | 2026-07-20 | Architecture Review — ACCEPTED; PR #11 approved for merge (requirements structure, governance, verification-plan structure, traceability baseline) |
| 1.2.2 | 2026-07-20 | WP-009 — link threshold analysis; no case PASS changes |
| 1.2.3 | 2026-07-20 | WP-010 — link functional electrical architecture; no case PASS changes |
