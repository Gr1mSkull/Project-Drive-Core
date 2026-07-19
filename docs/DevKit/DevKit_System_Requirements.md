# DevKit System Requirements — Gen1

**Document ID:** DOC-DK-REQ-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-007  
**Date:** 2026-07-19  
**Canonical related ADR:** ADR-015  
**Related standard:** STD-REV-001  
**Related gate policy:** EDL-014  

> Normative atomic requirements for the Gen1 DevKit verification platform.  
> This document is **Proposed** and requires Architecture Review.  
> It does **not** define schematic, PCB, BOM, enclosure model, or exact MPNs.

## 1. Purpose

Define verification-ready requirements answering what the DevKit must accomplish and how satisfaction will be verified.

## 2. Authority and hierarchy

| Priority | Source |
|----------|--------|
| 1 | `.cursor/ENGINEERING_CONSTITUTION.mdc` |
| 2 | Accepted ADR/EDL (incl. EDL-014, EDL-007, EDL-011, ADR-015) |
| 3 | Approved STD-REV-001 |
| 4 | This requirements baseline (after acceptance) |
| 5 | Approved architecture docs (`docs/001`–`008`, `docs/DCC/*`) |
| 6 | Proposed conceptual docs (WP-004/005 families) |
| 7 | Operational notes / `agents_stuff/` |

Conflicts are recorded in `DevKit_Current_State_Gap_Assessment.md`. Unresolved fidelity questions are escalated as `ARCHITECTURAL DECISION REQUIRED`.

## 3. Identifier scheme

```text
REQ-DCC-V-DK-NNN
```

This baseline defines **118** atomic requirements: `REQ-DCC-V-DK-001` … `REQ-DCC-V-DK-118`.

Verification cases: `docs/DevKit/DevKit_Verification_Plan.md`.

## 4. Requirements

### 4.A — Purpose and system boundary

#### REQ-DCC-V-DK-001

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-001` |
| Requirement | The Gen1 DevKit SHALL be a laboratory verification platform used to validate DriveCore Controller (DCC) behaviours required before DCC Gen1 vehicle installation per EDL-014. |
| Source | EDL-014; docs/001 §13 |
| Rationale | Defines DevKit purpose as verification gate, not production unit. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-002

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-002` |
| Requirement | The DevKit SHALL NOT be treated as a reduced production DCC Gen1 product acceptance unit. |
| Source | WP-007 objective; EDL-014 |
| Rationale | Prevents substituting DevKit evidence for Gen1 acceptance. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-003

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-003` |
| Requirement | Successful completion of DevKit gates DK-A through DK-D SHALL NOT authorize installation of DCC Gen1 into a vehicle. |
| Source | EDL-014 |
| Rationale | Vehicle install requires Phase E critical tests on full DCC Gen1. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-020` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-004

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-004` |
| Requirement | The DevKit system boundary SHALL include Real-Time domain, Service domain, and a representative Power domain suitable for laboratory power-channel verification. |
| Source | EDL-007; docs/001; docs/008 concept |
| Rationale | Three-domain representation required for meaningful gate testing. |
| Verification method | Inspection / Analysis |
| Verification reference | `VER-DCC-DK-A-001`, `VER-DCC-DK-A-010` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-005

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-005` |
| Requirement | The DevKit SHALL exclude production vehicle-install mechanical packaging, vehicle harness interfaces, and full production channel population unless separately approved for a specific verification case. |
| Source | EDL-014; docs/008 no-HS60 concept |
| Rationale | Keeps lab platform scoped. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | Exact production exclusions for Power population remain subject to ADR-DK-004. |

#### REQ-DCC-V-DK-006

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-006` |
| Requirement | DevKit verification results SHALL be used only for laboratory validation and shall not be claimed as vehicle or track acceptance evidence. |
| Source | EDL-014; constitution §10 safety |
| Rationale | Track/vehicle claims require Gen1 evidence. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-020` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-007

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-007` |
| Requirement | The DevKit SHALL be operated only in a controlled laboratory or bench environment with supervised power application. |
| Source | docs/008 §3.3 (candidate); constitution safety |
| Rationale | Unattended high-current risk. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-A-003` |
| Status | Proposed |
| Notes | Unattended-operation prohibition — see REQ-DCC-V-DK-030. |

#### REQ-DCC-V-DK-008

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-008` |
| Requirement | Exceptions to the EDL-014 DevKit gate SHALL be recorded in a controlled engineering record and SHALL NOT be valid for track use. |
| Source | EDL-014 |
| Rationale | Preserves gate integrity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-020` |
| Status | Proposed |
| Notes | — |

### 4.B — Architecture fidelity

#### REQ-DCC-V-DK-009

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-009` |
| Requirement | The DevKit Real-Time domain SHALL represent DCC Logic control of power channels, CAN, and safety-relevant sequencing without requiring the Service domain for power execution. |
| Source | docs/001; constitution STM32 ownership; EDL-002 |
| Rationale | Fail-operational and RT independence. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-010`, `VER-DCC-DK-D-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-010

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-010` |
| Requirement | The DevKit Service domain SHALL represent Wi-Fi/REST/WebSocket/diagnostic services and SHALL NOT be required for Real-Time power execution. |
| Source | EDL-002; constitution |
| Rationale | Service failure isolation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-014`, `VER-DCC-DK-D-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-011

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-011` |
| Requirement | The DevKit SHALL provide a Logic-to-Power control and sense interface compatible with the production J_LP interface intent defined in EDL-011 and docs/002. |
| Source | EDL-011; docs/002 §5 |
| Rationale | Production interface compatibility for Power swap path. |
| Verification method | Test / Inspection |
| Verification reference | `VER-DCC-DK-A-008` |
| Status | Proposed |
| Notes | Pin-level reuse vs adapter is ADR-DK-001. |

#### REQ-DCC-V-DK-012

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-012` |
| Requirement | The DevKit SHALL provide a Logic-to-Radio communication interface compatible with DCPI as defined in docs/004 / EDL-010. |
| Source | EDL-010; docs/004 |
| Rationale | Service-layer communication fidelity. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-009`, `VER-DCC-DK-B-006` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-013

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-013` |
| Requirement | DevKit vehicle-mode and output behaviour SHALL be configuration-driven and SHALL NOT hardcode vehicle-specific E30 load assignments in common firmware. |
| Source | constitution; docs/005 |
| Rationale | Configuration-over-code. |
| Verification method | Analysis / Test |
| Verification reference | `VER-DCC-DK-D-003`, `VER-DCC-DK-D-005` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-014

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-014` |
| Requirement | The DevKit Power domain SHALL provide representative power-channel capability sufficient to verify the power-channel state, protection, and diagnostic behaviours required by the applicable Proposed power-channel requirements (DC-DCC-PWR family), subject to represented class coverage. |
| Source | DC-DCC-PWR-108; WP-004 |
| Rationale | Capability representation without MPN. |
| Verification method | Analysis / Test |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | Exact class set: ADR-DK-004. |

#### REQ-DCC-V-DK-015

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-015` |
| Requirement | Firmware and configuration equivalence rules between DevKit and DCC Gen1 SHALL follow an Accepted architectural decision defining whether identity means same physical boards, same interfaces, same source tree, same feature set, and/or same compiled binary. |
| Source | docs/008 same-binary claim (candidate); docs/007 G431 alt (conflict) |
| Rationale | Prevents silent reinterpretation of 'identical'/'same binary'. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Blocked |
| Notes | ARCHITECTURAL DECISION REQUIRED — ADR-DK-001, ADR-DK-003. |

#### REQ-DCC-V-DK-016

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-016` |
| Requirement | Every DevKit verification record SHALL identify the tested system using the composite baseline fields required by STD-REV-001 / ADR-015. |
| Source | ADR-015; STD-REV-001 |
| Rationale | Reproducible evidence. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-015`, `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-017

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-017` |
| Requirement | Where machine-readable hardware revision sensing is implemented using existing BOARD_ID architecture, DevKit verification SHALL record the observed BOARD_ID value and the interpreted revision mapping when that mapping is defined. |
| Source | EDL-011; ADR-015 OQ-3 |
| Rationale | Uses existing BOARD_ID; does not redesign. |
| Verification method | Test / Inspection |
| Verification reference | `VER-DCC-DK-A-015` |
| Status | Proposed |
| Notes | Encoding map TBD — TBD-DK-020. |

#### REQ-DCC-V-DK-018

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-018` |
| Requirement | The DevKit SHALL preserve the fail-operational principle that loss of Service domain or Tablet connectivity SHALL NOT stop Real-Time power execution required by active VCM rules. |
| Source | constitution; docs/008 §11 |
| Rationale | Safety ownership. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-012`, `VER-DCC-DK-D-013` |
| Status | Proposed |
| Notes | — |

### 4.C — Power input and bench safety

#### REQ-DCC-V-DK-019

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-019` |
| Requirement | The DevKit SHALL provide a single controlled laboratory power-entry path with means to energize and de-energize the unit under test. |
| Source | docs/008 §3 (candidate intent); safety standard |
| Rationale | Controlled first power. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-A-002`, `VER-DCC-DK-A-003` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-020

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-020` |
| Requirement | The DevKit power-entry path SHALL include replaceable overcurrent protection sized for the approved DevKit input current limit (TBD-DK-002). |
| Source | docs/008 30 A fuse candidate |
| Rationale | Bench protection; rating TBD. |
| Verification method | Inspection / Analysis |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | Limit TBD-DK-002; ADR-DK-006. |

#### REQ-DCC-V-DK-021

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-021` |
| Requirement | The DevKit SHALL support emergency isolation that de-energizes power outputs independently of Service-domain software commands. |
| Source | constitution kill/isolation; EDL-011 nKILL intent |
| Rationale | Hardware path required. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-022

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-022` |
| Requirement | Prior to first energization of a newly assembled or modified DevKit, an unpowered inspection for short circuits and assembly defects SHALL be performed and recorded. |
| Source | docs/008 Phase A intent |
| Rationale | First-power safety. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-023

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-023` |
| Requirement | On controlled first power, power outputs SHALL remain in the de-energized safe default state until explicitly commanded under authorized test procedure. |
| Source | docs/008 A1/A7 intent; power-channel safe OFF |
| Rationale | Default safe state. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-003`, `VER-DCC-DK-A-014` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-024

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-024` |
| Requirement | Exposed high-current conductors and terminals SHALL be arranged so that accidental contact risk during normal bench operation is minimized through insulation, covers, or equivalent physical measures. |
| Source | safety standard; docs/008 §3.3 intent |
| Rationale | Lab shock/burn risk. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | Does not specify enclosure model. |

#### REQ-DCC-V-DK-025

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-025` |
| Requirement | The DevKit SHALL provide a defined laboratory ground reference connection point for measurement and safety bonding. |
| Source | docs/008 bench setup intent |
| Rationale | Measurement repeatability and safety. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-026

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-026` |
| Requirement | Load connection and removal SHALL be performed only when the affected channel is commanded OFF and the procedure records the de-energized precondition. |
| Source | docs/008 §3.3 |
| Rationale | Safe load handling. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-027

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-027` |
| Requirement | The DevKit bench setup SHALL provide a means to limit or interrupt input current under fault (operator-accessible isolation and/or protection device). |
| Source | safety; docs/008 kill/fuse intent |
| Rationale | Fault interruption. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-028

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-028` |
| Requirement | Normative DevKit input operating voltage range SHALL be defined with unit, limits, and tolerance (TBD-DK-001) before Gate DK-A exit for power tests requiring that range. |
| Source | numeric discipline |
| Rationale | Threshold control. |
| Verification method | Analysis |
| Verification reference | `VER-DCC-DK-A-003` |
| Status | Proposed |
| Notes | Candidate 13.8 V in docs/008 is not automatically normative. |

#### REQ-DCC-V-DK-029

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-029` |
| Requirement | Maximum simultaneous DevKit load current SHALL be defined (TBD-DK-003) before Gate DK-C exit for multi-channel load tests. |
| Source | docs/008 30 A continuous candidate |
| Rationale | Prevents unsafe overload claims. |
| Verification method | Analysis |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | ADR-DK-006. |

#### REQ-DCC-V-DK-030

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-030` |
| Requirement | Energized DevKit power-channel testing with connected loads SHALL NOT be left unattended. |
| Source | docs/008 §3.3 intent |
| Rationale | Fire/thermal risk. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-A-003`, `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | — |

### 4.D — Kill and global enable

#### REQ-DCC-V-DK-031

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-031` |
| Requirement | The DevKit SHALL provide an independently operable kill test input path that forces power outputs to the de-energized state. |
| Source | EDL-011 nKILL; docs/008 A7 |
| Rationale | Independent kill testability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-032

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-032` |
| Requirement | Global enable state SHALL be observable to the tester through a documented diagnostic or measurement path. |
| Source | EDL-011 nENABLE; power-channel reqs |
| Rationale | Observability. |
| Verification method | Test / Demonstration |
| Verification reference | `VER-DCC-DK-A-013` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-033

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-033` |
| Requirement | When kill is asserted, power outputs SHALL de-energize through a hardware-effective path that does not depend solely on Service-domain software. |
| Source | constitution; EDL-011 |
| Rationale | Hardware de-energization. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-034

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-034` |
| Requirement | After kill de-assertion, outputs SHALL remain OFF until an explicit authorized re-enable sequence is completed (reset behaviour). |
| Source | docs/008 / fault handling intent |
| Rationale | No auto-restart hazard. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | Exact sequence TBD if not yet specified — TBD-DK-021. |

#### REQ-DCC-V-DK-035

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-035` |
| Requirement | On loss of Logic-to-Power control communication beyond the interface timeout defined by the approved interface specification, power outputs SHALL enter the defined safe de-energized response. |
| Source | EDL-011 SPI timeout >100 ms candidate |
| Rationale | Control-loss behaviour. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-008`, `VER-DCC-DK-C-012` |
| Status | Proposed |
| Notes | Timeout value TBD-DK-007 pending authoritative freeze; EDL-011 states >100 ms. |

#### REQ-DCC-V-DK-036

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-036` |
| Requirement | Kill response time from kill assertion to all DevKit power outputs de-energized SHALL meet the approved limit TBD-DK-004, or verification of that case SHALL remain BLOCKED until the limit is approved. |
| Source | docs/008 'immediately' (vague — replaced) |
| Rationale | Measurable kill timing. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Proposed |
| Notes | Vague 'immediately' prohibited; threshold open. |

#### REQ-DCC-V-DK-037

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-037` |
| Requirement | Service-domain commands, REST APIs, and Tablet UI actions SHALL NOT bypass an asserted hardware kill. |
| Source | constitution; EDL-013 dangerous API model |
| Rationale | No software bypass of kill. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012`, `VER-DCC-DK-B-013` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-038

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-038` |
| Requirement | Watchdog fault response that de-energizes outputs SHALL meet approved response-time limit TBD-DK-005, or the corresponding verification case SHALL remain BLOCKED. |
| Source | docs/008 A6 <200 ms candidate |
| Rationale | Measurable WDT response. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-011` |
| Status | Proposed |
| Notes | Candidate <200 ms not automatically normative. |

### 4.E — Representative power-channel capability

#### REQ-DCC-V-DK-039

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-039` |
| Requirement | The DevKit SHALL provide at least one switched unidirectional high-side output channel with commanded ON/OFF behaviour and observable output state. |
| Source | DC-DCC-PWR; docs/008 Phase C intent |
| Rationale | Representative HS capability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-001`, `VER-DCC-DK-C-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-040

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-040` |
| Requirement | The DevKit SHALL provide at least one PWM-capable output channel when PWM verification is in Gate DK-C scope, or PWM cases SHALL be marked N/A with Architect-approved exclusion. |
| Source | DC-DCC-PWR PWM optional; docs/008 C scenarios |
| Rationale | PWM representation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-003` |
| Status | Proposed |
| Notes | PWM frequency range TBD-DK-008. |

#### REQ-DCC-V-DK-041

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-041` |
| Requirement | The DevKit SHALL provide at least one lower-current switched output channel distinct from the highest-current represented channel class on the DevKit. |
| Source | docs/008 multi-class intent; DC-DCC-PWR-108 |
| Rationale | Class diversity without claiming full Gen1 set. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-042

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-042` |
| Requirement | The DevKit SHALL provide at least one bidirectional output channel capable of verifying forward and reverse command separation, or bidirectional verification SHALL be BLOCKED with documented fixture gap. |
| Source | docs/008 HB1 candidate; BD class Proposed |
| Rationale | H-bridge representation by capability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-010`, `VER-DCC-DK-C-011` |
| Status | Proposed |
| Notes | Does not require specific H-bridge MPN. |

#### REQ-DCC-V-DK-043

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-043` |
| Requirement | Each represented power channel SHALL provide a current observation path usable during verification (measurement accuracy TBD-DK-009). |
| Source | DC-DCC-PWR diagnostics |
| Rationale | Current observability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-004` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-044

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-044` |
| Requirement | Each represented power channel SHALL implement overcurrent reaction that de-energizes or limits the channel and records a diagnostic fault observable to the tester. |
| Source | DC-DCC-PWR protection |
| Rationale | Overcurrent behaviour. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-005` |
| Status | Proposed |
| Notes | Threshold tolerance TBD-DK-011. |

#### REQ-DCC-V-DK-045

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-045` |
| Requirement | Each represented power channel SHALL implement short-circuit reaction that transitions the channel to a safe OFF or protected state with observable fault indication. |
| Source | DC-DCC-PWR protection; docs/008 C2 |
| Rationale | Short-circuit behaviour. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-006` |
| Status | Proposed |
| Notes | Safe fixture required; else BLOCKED. |

#### REQ-DCC-V-DK-046

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-046` |
| Requirement | Where open-load detection is supported for a represented channel class, open-load fault indication SHALL be observable; where not supported, the verification case SHALL be marked N/A with rationale. |
| Source | DC-DCC-PWR open-load TBD |
| Rationale | Open-load where supported. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-007` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-047

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-047` |
| Requirement | Represented channels SHALL exhibit defined behaviour under supply undervoltage conditions used in verification (undervoltage threshold TBD-DK-001 / TBD-DK-012). |
| Source | docs/008 C4 <10.5 V candidate |
| Rationale | Supply fault behaviour. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-008` |
| Status | Proposed |
| Notes | Candidate 10.5 V not automatically normative. |

#### REQ-DCC-V-DK-048

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-048` |
| Requirement | Thermal observation relevant to Power-domain verification SHALL be available where required by represented channel protection requirements (accuracy TBD-DK-010). |
| Source | EDL-011 NTC intent; DC-DCC-PWR thermal |
| Rationale | Thermal observability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-009` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-049

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-049` |
| Requirement | Retry and latch behaviours for recoverable vs non-recoverable faults SHALL be configurable or specified per channel policy and SHALL be verifiable on the DevKit for represented channels (retry delay TBD-DK-013). |
| Source | DC-DCC-PWR; docs/008 C5 ≤3 candidate |
| Rationale | Retry/latch. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-005`, `VER-DCC-DK-C-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-050

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-050` |
| Requirement | Commanded safe OFF SHALL de-energize the represented channel within the approved time limit TBD-DK-014. |
| Source | DC-DCC-PWR safe OFF |
| Rationale | Safe OFF timing. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-051

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-051` |
| Requirement | Diagnostic readout for channel state and fault flags SHALL be available via an approved diagnostic path (CAN, DCPI-derived UI, or documented test interface). |
| Source | docs/004; DC-DCC-PWR diagnostics |
| Rationale | Diagnostic readout. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-004`, `VER-DCC-DK-B-009` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-052

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-052` |
| Requirement | The DevKit SHALL NOT claim verification coverage for channel classes that are not physically represented; such classes SHALL be deferred to external load-bank and/or DCC Gen1 Phase E evidence. |
| Source | docs/008 no-HS60 statement (candidate intent); DC-DCC-PWR-108 |
| Rationale | Honest coverage boundary. |
| Verification method | Inspection / Analysis |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | Whether any high-current class is mandatory on DevKit: ADR-DK-005. |

#### REQ-DCC-V-DK-053

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-053` |
| Requirement | Normative DevKit requirements SHALL describe channel capability and behaviour and SHALL NOT require a specific smart-switch or H-bridge manufacturer part number unless an Accepted ADR/EDL mandates that exact part. |
| Source | WP-007 §8.1; EDL-003 technology only |
| Rationale | Component independence. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-054

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-054` |
| Requirement | Conflicting bidirectional bridge commands (simultaneous opposing drive) SHALL be prevented by design behaviour and SHALL be verified when a bidirectional channel is represented. |
| Source | docs/008 HB intent; safety |
| Rationale | Bridge shoot-through / conflict prevention. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-011` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-055

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-055` |
| Requirement | Stall or locked-rotor response for bidirectional channels SHALL be verified when requirements and safe fixtures exist; otherwise the case SHALL be BLOCKED (TBD-DK-022). |
| Source | docs/008 motor stall candidate |
| Rationale | Stall response. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-010` |
| Status | Proposed |
| Notes | May be BLOCKED pending fixture. |

### 4.F — Logic and Real-Time domain

#### REQ-DCC-V-DK-056

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-056` |
| Requirement | The DevKit Real-Time domain SHALL support firmware programming through a documented debug/programming interface. |
| Source | docs/008 A2; docs/002 SWD intent |
| Rationale | Bring-up. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-004` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-057

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-057` |
| Requirement | Debug access required for bring-up and fault investigation SHALL be available without unsafe exposure of high-current paths. |
| Source | constitution prototype test points; hardware standard |
| Rationale | Safe debug. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-004` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-058

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-058` |
| Requirement | A watchdog mechanism SHALL be present in the Real-Time domain and SHALL be verifiable for reset/safe-output behaviour. |
| Source | constitution watchdog; docs/008 A6 |
| Rationale | WDT. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-011` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-059

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-059` |
| Requirement | Real-Time startup SHALL reach a defined READY or equivalent operable state with outputs default OFF unless a verified configuration commands otherwise under authorized procedure. |
| Source | DCC_StartUp_Sequence; power safe OFF |
| Rationale | Startup. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-010` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-060

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-060` |
| Requirement | A safe reset path SHALL return the Real-Time domain to a known state with outputs de-energized. |
| Source | fault handling / startup docs |
| Rationale | Safe reset. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-014` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-061

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-061` |
| Requirement | The Real-Time domain SHALL control represented power channels according to configuration and VCM/rules execution. |
| Source | docs/001; docs/005 |
| Rationale | Power-channel control. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-003`, `VER-DCC-DK-D-005` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-062

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-062` |
| Requirement | VCM/mode state-machine transitions used in DevKit scenarios SHALL be observable and reproducible. |
| Source | docs/005; DCC modules |
| Rationale | State machine. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-063

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-063` |
| Requirement | Event logging of safety-relevant faults and mode transitions SHALL be available for DevKit verification evidence. |
| Source | docs/004 events; constitution diagnostics |
| Rationale | Event logging. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-016` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-064

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-064` |
| Requirement | Persistent diagnostic information required by verification cases SHALL remain available across a controlled reset when the case so requires, or the case SHALL document volatile-only limitation. |
| Source | DCC fault/diagnostics docs |
| Rationale | Persistent diagnostics. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-017` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-065

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-065` |
| Requirement | The Real-Time domain SHALL operate power-channel control without the Service domain after Service disconnection, for functions marked fail-operational. |
| Source | constitution fail-operational |
| Rationale | Operation without Service. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-012` |
| Status | Proposed |
| Notes | — |

### 4.G — Radio and Service domain

#### REQ-DCC-V-DK-066

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-066` |
| Requirement | The DevKit Service domain SHALL support firmware programming through a documented interface. |
| Source | docs/008 A4 |
| Rationale | Radio bring-up. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-005` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-067

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-067` |
| Requirement | DCPI communication between Real-Time and Service domains SHALL transfer state and configuration data with integrity checking as defined by docs/004. |
| Source | EDL-010; docs/004 |
| Rationale | DCPI. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-006`, `VER-DCC-DK-B-007` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-068

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-068` |
| Requirement | Configuration delivery to the Real-Time domain via the Service path SHALL be verifiable on the DevKit. |
| Source | docs/005; docs/008 B7 |
| Rationale | Config delivery. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-007`, `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-069

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-069` |
| Requirement | Diagnostic information originating in the Real-Time domain SHALL be observable through the Service diagnostic path when Service is available. |
| Source | docs/004; docs/006 |
| Rationale | Diagnostics. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-009` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-070

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-070` |
| Requirement | Where REST status endpoints are in DevKit gate scope, GET status SHALL report identity and health fields required by the UI contract without inventing new wire fields in this WP. |
| Source | docs/006; docs/008 B10 |
| Rationale | REST status. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-010` |
| Status | Proposed |
| Notes | Encoded/version field mapping TBD per ADR-015. |

#### REQ-DCC-V-DK-071

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-071` |
| Requirement | Where WebSocket telemetry is in DevKit gate scope, telemetry streaming SHALL be verifiable for availability and identity of streamed data; quantitative loss criteria use TBD-DK-016. |
| Source | docs/006; docs/008 B11 20 Hz candidate |
| Rationale | WS telemetry. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-011` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-072

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-072` |
| Requirement | Service-domain failure or restart SHALL NOT force Real-Time power outputs OFF solely due to Service absence for fail-operational functions. |
| Source | constitution; docs/008 D service restart |
| Rationale | Service failure isolation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-012` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-073

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-073` |
| Requirement | Tablet or browser client disconnection SHALL NOT stop Real-Time power execution for fail-operational functions. |
| Source | constitution Tablet never required |
| Rationale | Tablet independence. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-013` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-074

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-074` |
| Requirement | OTA update capability SHALL be included in mandatory DevKit gate verification only if an Accepted architectural decision requires OTA for EDL-014 DevKit gate completion; otherwise OTA cases SHALL be optional or deferred. |
| Source | docs/008 B14 candidate; ADR-DK-008 |
| Rationale | Do not invent OTA as mandatory. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-B-014` |
| Status | Blocked |
| Notes | ARCHITECTURAL DECISION REQUIRED — ADR-DK-008. |

### 4.H — CAN and external node simulation

#### REQ-DCC-V-DK-075

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-075` |
| Requirement | The DevKit SHALL support DCP communication on the Gen1 CAN FD bus topology intent (DCC as a node). |
| Source | EDL-008; docs/004 |
| Rationale | DCP. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-076

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-076` |
| Requirement | CAN bus termination for the DevKit bench SHALL be provided in accordance with the approved topology rules in docs/004 / EDL-008. |
| Source | EDL-008; docs/004 |
| Rationale | Termination. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-B-005` |
| Status | Proposed |
| Notes | Waveform acceptance TBD-DK-015. |

#### REQ-DCC-V-DK-077

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-077` |
| Requirement | The DevKit verification environment SHALL support ECU simulation injecting DCP engine telemetry messages. |
| Source | EDL-012; docs/008 B2 |
| Rationale | ECU simulation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-078

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-078` |
| Requirement | The DevKit verification environment SHALL support Button Box event simulation via DCP. |
| Source | docs/004; docs/008 B4 |
| Rationale | Button Box simulation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-004` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-079

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-079` |
| Requirement | Stale or lost external node handling SHALL be verifiable when simulated node traffic stops beyond the approved timeout (TBD-DK-006). |
| Source | docs/004 heartbeat/LOST; docs/008 B3 >500 ms candidate |
| Rationale | Stale-node. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-003` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-080

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-080` |
| Requirement | Controlled loss-of-communication testing SHALL be possible without uncontrolled bus damage (disconnect/simulator stop procedures). |
| Source | docs/008 Phase B/D |
| Rationale | LOC testing. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-014` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-081

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-081` |
| Requirement | CAN traffic observation access SHALL be available to the tester (sniffer or equivalent). |
| Source | docs/008 USB-CAN intent |
| Rationale | Bus observation. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-B-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-082

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-082` |
| Requirement | DevKit verification SHALL NOT redefine DCP payload layouts or encoded protocol version mappings. |
| Source | ADR-015; docs/004 |
| Rationale | Interface freeze. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | — |

### 4.I — Configuration

#### REQ-DCC-V-DK-083

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-083` |
| Requirement | A DevKit configuration profile SHALL exist to declare DevKit hardware capacity and representative modes/rules for laboratory scenarios. |
| Source | docs/005; config/vehicles/devkit.yaml present |
| Rationale | DevKit profile. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-B-007`, `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | Schema field hardware.profile not in docs/005 — ADR-DK-009 related. |

#### REQ-DCC-V-DK-084

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-084` |
| Requirement | Configuration content SHALL be validated before apply to the Real-Time domain. |
| Source | docs/005 |
| Rationale | Validation before apply. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-085

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-085` |
| Requirement | Configuration apply SHALL reject profiles that exceed declared DevKit hardware channel capacity. |
| Source | DC-DCC-PWR-104 intent; docs/005 |
| Rationale | Hardware-capacity validation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | Capacity declaration mechanism TBD if schema incomplete. |

#### REQ-DCC-V-DK-086

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-086` |
| Requirement | The DevKit profile SHALL include representative modes and rules sufficient for Gate DK-D scenario coverage listed in the verification plan. |
| Source | docs/008 Phase D intent |
| Rationale | Representative rules. |
| Verification method | Analysis / Test |
| Verification reference | `VER-DCC-DK-D-003`, `VER-DCC-DK-D-005` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-087

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-087` |
| Requirement | Invalid configuration payloads SHALL be rejected without partial application of unsafe channel enables. |
| Source | docs/005 atomic apply intent |
| Rationale | Invalid rejection. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-088

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-088` |
| Requirement | Configuration apply SHALL be atomic (all-or-nothing) with respect to enabling a new active rule/output set, or shall meet an Accepted alternative apply semantics decision. |
| Source | docs/005 |
| Rationale | Atomic apply. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | If semantics undefined: escalate. |

#### REQ-DCC-V-DK-089

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-089` |
| Requirement | Compiled DCFG artifacts used on DevKit SHALL carry format version identity per existing DCFG version field; CRC coverage remains TBD and SHALL NOT be resolved in WP-007. |
| Source | ADR-015; firmware shared DCFG_VERSION |
| Rationale | DCFG identity. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-B-007` |
| Status | Proposed |
| Notes | CRC coverage open — interface CR. |

#### REQ-DCC-V-DK-090

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-090` |
| Requirement | Active configuration identity (configuration ID, schema version, and content hash when available) SHALL be recorded in verification evidence per STD-REV-001. |
| Source | STD-REV-001 §8 |
| Rationale | Config baseline recording. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | SHA-256 hashing NOT IMPLEMENTED — record NOT RECORDED/TBD until available. |

#### REQ-DCC-V-DK-091

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-091` |
| Requirement | Configuration hot-reload outside Service/Wiring modes SHALL NOT be assumed permitted unless an Accepted architectural decision allows it. |
| Source | docs/008 D10 candidate; EDL-013 mode auth |
| Rationale | Hot reload policy. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-D-015` |
| Status | Blocked |
| Notes | ARCHITECTURAL DECISION REQUIRED — ADR-DK-009. |

#### REQ-DCC-V-DK-092

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-092` |
| Requirement | DevKit verification SHALL NOT invent encoded-version mappings for DCP/DCPI/DCFG constants. |
| Source | ADR-015 |
| Rationale | Encoding discipline. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Proposed |
| Notes | — |

### 4.J — Testability and observability

#### REQ-DCC-V-DK-093

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-093` |
| Requirement | Critical sense and control signals required by Phase A–D cases SHALL be accessible for measurement without destroying the assembly. |
| Source | hardware standard test points intent |
| Rationale | Accessible measurement. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-094

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-094` |
| Requirement | Supply rail voltages used in bring-up SHALL be measurable (rail tolerances TBD-DK-017). |
| Source | docs/008 A1 ±5% candidate |
| Rationale | Voltage observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-003` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-095

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-095` |
| Requirement | Channel current SHALL be measurable with documented method during Phase C cases (accuracy TBD-DK-009). |
| Source | docs/008 Phase C |
| Rationale | Current observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-004` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-096

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-096` |
| Requirement | Temperature observation required by thermal cases SHALL be measurable (accuracy TBD-DK-010; duration TBD-DK-018; max temperature TBD-DK-019). |
| Source | docs/008 thermal candidates |
| Rationale | Temperature observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-009` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-097

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-097` |
| Requirement | Logic/channel state and fault state SHALL be observable through diagnostic interfaces during verification. |
| Source | docs/004; DC-DCC-PWR |
| Rationale | Logic/fault observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-004`, `VER-DCC-DK-B-009` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-098

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-098` |
| Requirement | CAN capture capability SHALL be available for Phase B/D communication cases. |
| Source | docs/008 |
| Rationale | CAN capture. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-B-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-099

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-099` |
| Requirement | DCPI integrity failures (e.g. CRC error injection or equivalent controlled fault) SHALL be detectable as rejection or fault indication. |
| Source | docs/004 DCPI CRC |
| Rationale | DCPI fault observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-008` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-100

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-100` |
| Requirement | Repeatable fault-injection methods required by Gate DK-C/D SHALL be defined and safe; undefined mandatory injections SHALL leave cases BLOCKED (ADR-DK-010). |
| Source | DC-DCC-PWR-089; docs/008 §12 |
| Rationale | Fault injection. |
| Verification method | Analysis / Test |
| Verification reference | `VER-DCC-DK-C-005`, `VER-DCC-DK-C-006` |
| Status | Proposed |
| Notes | Which injections mandatory: ADR-DK-010. |

#### REQ-DCC-V-DK-101

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-101` |
| Requirement | Deterministic reset to a known de-energized starting state SHALL be available between verification cases. |
| Source | verification plan need |
| Rationale | Deterministic reset. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-014` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-102

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-102` |
| Requirement | Test loads SHALL be replaceable and channels SHALL be isolatable so that a single-channel fault test does not require destructive disassembly of unrelated channels. |
| Source | docs/008 load-bank intent |
| Rationale | Serviceable loads / isolation. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | — |

### 4.K — Evidence and revision identity

#### REQ-DCC-V-DK-103

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-103` |
| Requirement | Every executed DevKit verification case that supports gate exit SHALL record a composite system baseline per STD-REV-001 applicable fields. |
| Source | ADR-015; STD-REV-001 |
| Rationale | Baseline. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-104

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-104` |
| Requirement | Firmware identity for each programmed processor SHALL be recorded (module ID, SemVer when available, commit SHA, cleanliness). |
| Source | STD-REV-001 §4 |
| Rationale | Firmware identity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-015` |
| Status | Proposed |
| Notes | Build metadata NOT IMPLEMENTED — use available IDs; dirty builds cannot certify high-assurance claims. |

#### REQ-DCC-V-DK-105

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-105` |
| Requirement | Bootloader identity SHALL be recorded when a distinct bootloader is present; otherwise evidence SHALL mark bootloader N/A with rationale. |
| Source | STD-REV-001 §5 |
| Rationale | Bootloader identity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-015` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-106

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-106` |
| Requirement | Hardware board ID, hardware revision, BOM revision, and assembly revision SHALL be recorded for boards under test; missing fields render certification NOT VERIFIED or PARTIAL. |
| Source | STD-REV-001 §6 |
| Rationale | Hardware identity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-015` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-107

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-107` |
| Requirement | Configuration ID and schema version SHALL be recorded; configuration SHA-256 SHALL be recorded when hashing is implemented, otherwise NOT RECORDED. |
| Source | STD-REV-001 §8 |
| Rationale | Config identity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-108

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-108` |
| Requirement | Applicable protocol/schema versions SHALL be recorded as semantic versions and/or legacy encoded values without inventing mappings. |
| Source | STD-REV-001 §7; ADR-015 |
| Rationale | Protocol versions. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-109

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-109` |
| Requirement | Test equipment identifiers and fixture revision SHALL be recorded for measurement-dependent cases. |
| Source | STD-REV-001 §10 |
| Rationale | Test equipment identity. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-110

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-110` |
| Requirement | Verification evidence SHALL be stored under the repository records convention when filled (docs/records/verification/), using the Verification Evidence template. |
| Source | CR-002; docs/records |
| Rationale | Evidence storage. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-111

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-111` |
| Requirement | Raw tester results SHALL be distinguishable from Independent Reviewer / Test Owner certification outcomes. |
| Source | constitution §4/§13; VE template |
| Rationale | Raw vs certified. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-112

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-112` |
| Requirement | Physical laboratory certification for DevKit gates SHALL require the human Gen1 Test Owner defined in operational project context; Implementation agents may record raw automated results only. |
| Source | .ai/project_context.md; constitution |
| Rationale | Physical Test Owner authority. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

### 4.L — Maintainability and reuse

#### REQ-DCC-V-DK-113

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-113` |
| Requirement | The DevKit Power implementation SHALL be replaceable without redesigning the Real-Time/Service domains' external production interface contracts (J_LP / DCPI intents). |
| Source | EDL-007 Gen2 Power swap; EDL-011 |
| Rationale | Replaceable Power. |
| Verification method | Analysis / Inspection |
| Verification reference | `VER-DCC-DK-A-008` |
| Status | Proposed |
| Notes | Physical board identity ADR-DK-001. |

#### REQ-DCC-V-DK-114

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-114` |
| Requirement | Logic and Radio interfaces used by DevKit SHALL remain reusable toward DCC Gen1 to the extent required by Accepted architecture (same physical board vs same interface — ADR-DK-001/002). |
| Source | EDL-007; docs/008 identical claim |
| Rationale | Reusable Logic/Radio. |
| Verification method | Analysis |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Blocked |
| Notes | ARCHITECTURAL DECISION REQUIRED — ADR-DK-001, ADR-DK-002. |

#### REQ-DCC-V-DK-115

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-115` |
| Requirement | External connections used in verification SHALL be labelled sufficiently for repeatable setup by a competent technician. |
| Source | serviceability skill |
| Rationale | Labelled connections. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-116

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-116` |
| Requirement | Test loads and sense fixtures SHALL be serviceable and replaceable without requiring a new DevKit PCB design for ordinary load changes. |
| Source | docs/008 load intent |
| Rationale | Serviceable loads. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-C-001` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-117

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-117` |
| Requirement | DevKit setup procedures referenced by verification cases SHALL be repeatable from documented steps and baseline identity alone. |
| Source | verification plan |
| Rationale | Repeatable setup. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-A-001`, `VER-DCC-DK-D-019` |
| Status | Proposed |
| Notes | — |

#### REQ-DCC-V-DK-118

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-118` |
| Requirement | Documented recovery/rollback after failed firmware or configuration apply SHALL exist before Gate DK-B exit for configuration-delivery cases. |
| Source | RHP/rollback discipline |
| Rationale | Rollback/recovery. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-B-007`, `VER-DCC-DK-D-015` |
| Status | Proposed |
| Notes | — |

## 5. Threshold Resolution Register

Unresolved numeric/procedure thresholds. Do not treat `docs/008` candidates as normative until closed.

| TBD ID | Parameter | Unit | Current candidate | Candidate source | Evidence needed | Blocks | Owner role | Closure task | Status |
|--------|-----------|------|-------------------|------------------|-----------------|--------|------------|--------------|--------|
| TBD-DK-001 | DevKit input operating voltage range | V | 13.8 V nominal (single-point) | docs/008 §3 / A1 | Architecture decision + measurement plan | REQ-DCC-V-DK-028, Gate DK-A power tests | System Architect / Test Owner | Threshold CR / WP | Open |
| TBD-DK-002 | Approved maximum DevKit input / protection current | A | 30 A fuse / continuous | docs/008 §2.3 / §3.3 | Architecture decision + thermal/electrical analysis | REQ-DCC-V-DK-020/029, ADR-DK-006 | System Architect | ADR-DK-006 | Open |
| TBD-DK-003 | Maximum simultaneous load current | A | 30 A continuous | docs/008 §3.3 | Architecture decision | REQ-DCC-V-DK-029, Gate DK-C | System Architect | ADR-DK-006 | Open |
| TBD-DK-004 | Kill response time (assert → outputs de-energized) | ms | “immediately” (vague — rejected) | docs/008 A7 | Architecture decision + measurement | REQ-DCC-V-DK-036, VER-DCC-DK-A-012 | System Architect / Test Owner | Threshold CR | Open |
| TBD-DK-005 | Watchdog response time to safe outputs | ms | <200 ms | docs/008 A6 | Architecture decision + measurement | REQ-DCC-V-DK-038, VER-DCC-DK-A-011 | System Architect / Test Owner | Threshold CR | Open |
| TBD-DK-006 | External node lost/stale timeout | ms | >500 ms | docs/008 B3 | Protocol/architecture freeze | REQ-DCC-V-DK-079, VER-DCC-DK-B-003 | System Architect | docs/004 alignment CR | Open |
| TBD-DK-007 | Logic↔Power control-loss timeout | ms | >100 ms | EDL-011 | Confirm whether EDL-011 value is normative for DevKit evidence | REQ-DCC-V-DK-035 | System Architect | Interface confirmation | Open |
| TBD-DK-008 | PWM frequency range for DevKit PWM cases | Hz | not frozen | docs/008 / WP-004 TBD | Architecture + channel class decision | REQ-DCC-V-DK-040, VER-DCC-DK-C-003 | System Architect | Power-channel WP | Open |
| TBD-DK-009 | Current-measurement accuracy | % or A | not defined | docs/008 Phase C | Instrument + sense design qualification | REQ-DCC-V-DK-043/095 | Hardware Engineer / Test Owner | Fixture WP | Open |
| TBD-DK-010 | Temperature-measurement accuracy | °C | not defined | docs/008 thermal notes | Sensor qualification | REQ-DCC-V-DK-048/096 | Hardware Engineer | Qualification | Open |
| TBD-DK-011 | Overcurrent threshold tolerance | % or A | not defined | docs/008 C2 / WP-004 TBD | Protection requirements freeze | REQ-DCC-V-DK-044 | System Architect | Power-channel WP | Open |
| TBD-DK-012 | Undervoltage test threshold | V | <10.5 V | docs/008 C4 | Architecture decision + measurement | REQ-DCC-V-DK-047, VER-DCC-DK-C-008 | System Architect | Threshold CR | Open |
| TBD-DK-013 | Fault retry delay | ms | ≤3 retries (count only) | docs/008 C5 | Protection policy freeze | REQ-DCC-V-DK-049 | System Architect | Power-channel WP | Open |
| TBD-DK-014 | Commanded safe-OFF de-energize time | ms | not defined | WP-004 safe OFF TBD | Architecture decision | REQ-DCC-V-DK-050 | System Architect | Power-channel WP | Open |
| TBD-DK-015 | CAN waveform acceptance criteria | measurable metrics | “waveform clean” (vague — rejected) | docs/008 B5 | Signal-integrity criteria definition | VER-DCC-DK-B-005 | Test Owner / Architect | Threshold CR | Open |
| TBD-DK-016 | WebSocket duration and allowed loss | s / frames | 20 Hz ≥15 s without drop | docs/008 B11 | UI contract + measurement method | VER-DCC-DK-B-011 | System Architect / Test Owner | docs/006 alignment | Open |
| TBD-DK-017 | Power-rail tolerances (e.g. 5 V / 3.3 V) | % or V | ±5 % | docs/008 A1 | Electrical design + measurement | REQ-DCC-V-DK-094 | Hardware Engineer | DevKit electrical architecture WP | Open |
| TBD-DK-018 | Thermal test duration | s or min | not defined for DevKit | docs/008 Phase E has Gen1 numbers | Test plan decision (DevKit vs Gen1 scope) | REQ-DCC-V-DK-096, ADR-DK-011 | System Architect / Test Owner | ADR-DK-011 | Open |
| TBD-DK-019 | Maximum safe surface/device temperature for DevKit tests | °C | Gen1 candidates e.g. 85 °C (not DevKit-frozen) | docs/008 / docs/002 | Safety + thermal analysis | REQ-DCC-V-DK-096, ADR-DK-011 | System Architect | ADR-DK-011 | Open |
| TBD-DK-020 | BOARD_ID bit encoding → revision map | map | pins exist; encoding TBD | EDL-011; ADR-015 OQ-3 | Architecture decision (no new HW mechanism) | REQ-DCC-V-DK-017 | System Architect | Hardware identity WP | Open |
| TBD-DK-021 | Post-kill explicit re-enable sequence definition | procedure | partial intent in docs | fault/startup docs | Architecture / safety procedure | REQ-DCC-V-DK-034 | System Architect | Safety procedure WP | Open |
| TBD-DK-022 | Bidirectional stall response criteria and fixture | A / ms / procedure | motor stall candidate in docs/008 | docs/008 | Fixture + requirement freeze | REQ-DCC-V-DK-055, VER-DCC-DK-C-010 | Test Owner / Architect | Fixture WP | Open |

## 6. Architectural decisions required (summary)

| ID | Question |
|----|----------|
| ADR-DK-001 | Same physical Logic Board vs same electrical/firmware interfaces? |
| ADR-DK-002 | Same physical Radio Board vs equivalent Service interfaces? |
| ADR-DK-003 | Same compiled RT binary mandatory vs same source/feature set? |
| ADR-DK-004 | Which representative power-channel classes must DevKit contain? |
| ADR-DK-005 | Is a high-current class required on DevKit or only external/Gen1? |
| ADR-DK-006 | Approved maximum DevKit input/simultaneous current? |
| ADR-DK-007 | Approved kill and watchdog response-time limits (with TBD-DK-004/005)? |
| ADR-DK-008 | Is OTA part of mandatory DevKit gate? |
| ADR-DK-009 | Is configuration hot reload permitted outside Service/Wiring modes? |
| ADR-DK-010 | Which fault injections are mandatory and how performed safely? |
| ADR-DK-011 | DevKit vs DCC Gen1 electrical/thermal environmental test split? |
| ADR-DK-012 | Which enclosure/connector candidates remain valid (WAGO vs screw, etc.)? |

Full options/consequences: Architect Review Package in WP-007 completion report.

## 7. Coverage summary

| Status | Count |
|--------|-------|
| Blocked | 4 |
| Proposed | 114 |
| **Total** | **118** |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial Proposed DevKit requirements baseline |
