# DevKit System Requirements — Gen1

**Document ID:** DOC-DK-REQ-001  
**Version:** 1.2  
**Status:** Accepted  
**Work Package:** WP-007 / WP-007-R1  
**Date:** 2026-07-19  
**Governance:** [DevKit_Verification_Governance.md](DevKit_Verification_Governance.md)  
**Verification plan:** [DevKit_Verification_Plan.md](DevKit_Verification_Plan.md)  

> Normative **system** requirements for the Gen1 DevKit.  
> Governance/evidence-claim rules live in `DK-GOV-*` (not in this ID range).

## 1. Taxonomy (WP-007-R1)

| Class | Count |
|-------|-------|
| Active system requirements | 93 |
| Withdrawn — moved to DK-GOV-* | 25 |
| Governance rules | 25 |
| Blocked active system requirements | 1 |

Withdrawn IDs are preserved and **not reused**.

## 2. Active system requirements

### 2.A — Purpose and system boundary

#### REQ-DCC-V-DK-001

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-001` |
| Requirement | The Gen1 DevKit SHALL be a laboratory verification platform used to validate DriveCore Controller (DCC) behaviours required before DCC Gen1 vehicle installation per EDL-014. |
| Source | EDL-014; docs/001 §13 |
| Rationale | Defines DevKit purpose as verification gate, not production unit. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-004

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-004` |
| Requirement | The DevKit system boundary SHALL include Real-Time domain, Service domain, and a representative Power domain suitable for laboratory power-channel verification. |
| Source | EDL-007; docs/001; docs/008 concept |
| Rationale | Three-domain representation required for meaningful gate testing. |
| Verification method | Inspection / Analysis |
| Verification reference | `VER-DCC-DK-A-001` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | Exact production exclusions for Power population remain subject to ADR-DK-004. |

#### REQ-DCC-V-DK-007

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-007` |
| Requirement | The DevKit SHALL be operated only in a controlled laboratory or bench environment with supervised power application. |
| Source | docs/008 §3.3 (candidate); constitution safety |
| Rationale | Unattended high-current risk. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-A-003` |
| Status | Accepted |
| Notes | Unattended-operation prohibition — see REQ-DCC-V-DK-030. |

### 2.B — Architecture fidelity

#### REQ-DCC-V-DK-009

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-009` |
| Requirement | The DevKit Real-Time domain SHALL represent DCC Logic control of power channels, CAN, and safety-relevant sequencing without requiring the Service domain for power execution. |
| Source | docs/001; constitution STM32 ownership; EDL-002 |
| Rationale | Fail-operational and RT independence. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-010` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-010

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-010` |
| Requirement | The DevKit Service domain SHALL represent Wi-Fi/REST/WebSocket/diagnostic services and SHALL NOT be required for Real-Time power execution. |
| Source | EDL-002; constitution |
| Rationale | Service failure isolation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-005`, `VER-DCC-DK-D-012` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-011

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-011` |
| Requirement | The DevKit SHALL provide a Logic-to-Power control and sense interface compatible with the production J_LP interface intent defined in EDL-011 and docs/002. |
| Source | EDL-011; docs/002 §5 |
| Rationale | Production interface compatibility for Power swap path. |
| Verification method | Test / Inspection |
| Verification reference | `VER-DCC-DK-A-007`, `VER-DCC-DK-A-008` |
| Status | Accepted |
| Notes | Pin-level reuse vs adapter is ADR-DK-001. |

#### REQ-DCC-V-DK-012

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-012` |
| Requirement | The DevKit SHALL provide a Logic-to-Radio communication interface compatible with DCPI as defined in docs/004 / EDL-010. |
| Source | EDL-010; docs/004 |
| Rationale | Service-layer communication fidelity. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-007`, `VER-DCC-DK-A-009`, `VER-DCC-DK-B-006` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-013

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-013` |
| Requirement | DevKit vehicle-mode and output behaviour SHALL be configuration-driven and SHALL NOT hardcode vehicle-specific E30 load assignments in common firmware. |
| Source | constitution; docs/005 |
| Rationale | Configuration-over-code. |
| Verification method | Analysis / Test |
| Verification reference | `VER-DCC-DK-D-003` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | Exact class set: ADR-DK-004. |

#### REQ-DCC-V-DK-017

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-017` |
| Requirement | Where machine-readable hardware revision sensing is implemented using existing BOARD_ID architecture, DevKit verification SHALL record the observed BOARD_ID value and the interpreted revision mapping when that mapping is defined. |
| Source | EDL-011; ADR-015 OQ-3 |
| Rationale | Uses existing BOARD_ID; does not redesign. |
| Verification method | Test / Inspection |
| Verification reference | `VER-DCC-DK-A-015` |
| Status | Accepted |
| Notes | Encoding map TBD — TBD-DK-020. |

#### REQ-DCC-V-DK-018

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-018` |
| Requirement | The DevKit SHALL preserve the fail-operational principle that loss of Service domain or Tablet connectivity SHALL NOT stop Real-Time power execution required by active VCM rules. |
| Source | constitution; docs/008 §11 |
| Rationale | Safety ownership. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-012` |
| Status | Accepted |
| Notes | — |

### 2.C — Power input and bench safety

#### REQ-DCC-V-DK-019

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-019` |
| Requirement | The DevKit SHALL provide a single controlled laboratory power-entry path with means to energize and de-energize the unit under test. |
| Source | docs/008 §3 (candidate intent); safety standard |
| Rationale | Controlled first power. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-A-002`, `VER-DCC-DK-A-007` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-023

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-023` |
| Requirement | On controlled first power, power outputs SHALL remain in the de-energized safe default state until explicitly commanded under authorized test procedure. |
| Source | docs/008 A1/A7 intent; power-channel safe OFF |
| Rationale | Default safe state. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-003`, `VER-DCC-DK-A-016` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-026

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-026` |
| Requirement | Load connection and removal SHALL be performed only when the affected channel is commanded OFF and the procedure records the de-energized precondition. |
| Source | docs/008 §3.3 |
| Rationale | Safe load handling. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-C-002` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-027

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-027` |
| Requirement | The DevKit bench setup SHALL provide a means to limit or interrupt input current under fault (operator-accessible isolation and/or protection device). |
| Source | safety; docs/008 kill/fuse intent |
| Rationale | Fault interruption. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-030

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-030` |
| Requirement | Energized DevKit power-channel testing with connected loads SHALL NOT be left unattended. |
| Source | docs/008 §3.3 intent |
| Rationale | Fire/thermal risk. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-A-003` |
| Status | Accepted |
| Notes | — |

### 2.D — Kill and global enable

#### REQ-DCC-V-DK-031

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-031` |
| Requirement | The DevKit SHALL provide an independently operable kill test input path that forces power outputs to the de-energized state. |
| Source | EDL-011 nKILL; docs/008 A7 |
| Rationale | Independent kill testability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-034

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-034` |
| Requirement | After kill de-assertion, outputs SHALL remain OFF until an explicit authorized re-enable sequence is completed (reset behaviour). |
| Source | docs/008 / fault handling intent |
| Rationale | No auto-restart hazard. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-014` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | Vague 'immediately' prohibited; threshold open. |

#### REQ-DCC-V-DK-037

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-037` |
| Requirement | Service-domain commands, REST APIs, and Tablet UI actions SHALL NOT bypass an asserted hardware kill. |
| Source | constitution; EDL-013 dangerous API model |
| Rationale | No software bypass of kill. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-012`, `VER-DCC-DK-B-012`, `VER-DCC-DK-B-013` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | Candidate <200 ms not automatically normative. |

### 2.E — Representative power-channel capability

#### REQ-DCC-V-DK-039

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-039` |
| Requirement | The DevKit SHALL provide at least one switched unidirectional high-side output channel with commanded ON/OFF behaviour and observable output state. |
| Source | DC-DCC-PWR; docs/008 Phase C intent |
| Rationale | Representative HS capability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-001`, `VER-DCC-DK-C-002` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-042

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-042` |
| Requirement | The DevKit SHALL provide at least one bidirectional output channel capable of verifying forward and reverse command separation, or bidirectional verification SHALL be BLOCKED with documented fixture gap. |
| Source | docs/008 HB1 candidate; BD class Proposed |
| Rationale | H-bridge representation by capability. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-010` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-049

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-049` |
| Requirement | Retry and latch behaviours for recoverable vs non-recoverable faults SHALL be configurable or specified per channel policy and SHALL be verifiable on the DevKit for represented channels (retry delay TBD-DK-013). |
| Source | DC-DCC-PWR; docs/008 C5 ≤3 candidate |
| Rationale | Retry/latch. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-014` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-050

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-050` |
| Requirement | Commanded safe OFF SHALL de-energize the represented channel within the approved time limit TBD-DK-014. |
| Source | DC-DCC-PWR safe OFF |
| Rationale | Safe OFF timing. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-016`, `VER-DCC-DK-C-002` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-051

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-051` |
| Requirement | Diagnostic readout for channel state and fault flags SHALL be available via an approved diagnostic path (CAN, DCPI-derived UI, or documented test interface). |
| Source | docs/004; DC-DCC-PWR diagnostics |
| Rationale | Diagnostic readout. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-009`, `VER-DCC-DK-C-004` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-054

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-054` |
| Requirement | Conflicting bidirectional bridge commands (simultaneous opposing drive) SHALL be prevented by design behaviour and SHALL be verified when a bidirectional channel is represented. |
| Source | docs/008 HB intent; safety |
| Rationale | Bridge shoot-through / conflict prevention. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-010`, `VER-DCC-DK-C-011` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-055

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-055` |
| Requirement | Stall or locked-rotor response for bidirectional channels SHALL be verified when requirements and safe fixtures exist; otherwise the case SHALL be BLOCKED (TBD-DK-022). |
| Source | docs/008 motor stall candidate |
| Rationale | Stall response. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-C-013` |
| Status | Accepted |
| Notes | May be BLOCKED pending fixture. |

### 2.F — Logic and Real-Time domain

#### REQ-DCC-V-DK-056

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-056` |
| Requirement | The DevKit Real-Time domain SHALL support firmware programming through a documented debug/programming interface. |
| Source | docs/008 A2; docs/002 SWD intent |
| Rationale | Bring-up. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-004` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-060

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-060` |
| Requirement | A safe reset path SHALL return the Real-Time domain to a known state with outputs de-energized. |
| Source | fault handling / startup docs |
| Rationale | Safe reset. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-014`, `VER-DCC-DK-D-017` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-061

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-061` |
| Requirement | The Real-Time domain SHALL control represented power channels according to configuration and VCM/rules execution. |
| Source | docs/001; docs/005 |
| Rationale | Power-channel control. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-003` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-064

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-064` |
| Requirement | Persistent diagnostic information required by verification cases SHALL remain available across a controlled reset when the case so requires, or the case SHALL document volatile-only limitation. |
| Source | DCC fault/diagnostics docs |
| Rationale | Persistent diagnostics. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-016` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

### 2.G — Radio and Service domain

#### REQ-DCC-V-DK-066

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-066` |
| Requirement | The DevKit Service domain SHALL support firmware programming through a documented interface. |
| Source | docs/008 A4 |
| Rationale | Radio bring-up. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-005` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-067

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-067` |
| Requirement | DCPI communication between Real-Time and Service domains SHALL transfer state and configuration data with integrity checking as defined by docs/004. |
| Source | EDL-010; docs/004 |
| Rationale | DCPI. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-009`, `VER-DCC-DK-B-006` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-068

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-068` |
| Requirement | Configuration delivery to the Real-Time domain via the Service path SHALL be verifiable on the DevKit. |
| Source | docs/005; docs/008 B7 |
| Rationale | Config delivery. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-007` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

### 2.H — CAN and external node simulation

#### REQ-DCC-V-DK-075

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-075` |
| Requirement | The DevKit SHALL support DCP communication on the Gen1 CAN FD bus topology intent (DCC as a node). |
| Source | EDL-008; docs/004 |
| Rationale | DCP. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-001` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | Waveform acceptance TBD-DK-015. |

#### REQ-DCC-V-DK-077

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-077` |
| Requirement | The DevKit verification environment SHALL support ECU simulation injecting DCP engine telemetry messages. |
| Source | EDL-012; docs/008 B2 |
| Rationale | ECU simulation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-002`, `VER-DCC-DK-D-004` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-078

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-078` |
| Requirement | The DevKit verification environment SHALL support Button Box event simulation via DCP. |
| Source | docs/004; docs/008 B4 |
| Rationale | Button Box simulation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-004`, `VER-DCC-DK-D-006` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-079

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-079` |
| Requirement | Stale or lost external node handling SHALL be verifiable when simulated node traffic stops beyond the approved timeout (TBD-DK-006). |
| Source | docs/004 heartbeat/LOST; docs/008 B3 >500 ms candidate |
| Rationale | Stale-node. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-003`, `VER-DCC-DK-D-014` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

### 2.I — Configuration

#### REQ-DCC-V-DK-083

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-083` |
| Requirement | A DevKit configuration profile SHALL exist to declare DevKit hardware capacity and representative modes/rules for laboratory scenarios. |
| Source | docs/005; config/vehicles/devkit.yaml present |
| Rationale | DevKit profile. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-B-007` |
| Status | Accepted |
| Notes | Schema field hardware.profile not in docs/005 — ADR-DK-009 related. |

#### REQ-DCC-V-DK-084

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-084` |
| Requirement | Configuration content SHALL be validated before apply to the Real-Time domain. |
| Source | docs/005 |
| Rationale | Validation before apply. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015`, `VER-DCC-DK-D-011` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-085

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-085` |
| Requirement | Configuration apply SHALL reject profiles that exceed declared DevKit hardware channel capacity. |
| Source | DC-DCC-PWR-104 intent; docs/005 |
| Rationale | Hardware-capacity validation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-007`, `VER-DCC-DK-D-008` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-087

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-087` |
| Requirement | Invalid configuration payloads SHALL be rejected without partial application of unsafe channel enables. |
| Source | docs/005 atomic apply intent |
| Rationale | Invalid rejection. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-015`, `VER-DCC-DK-D-018` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-088

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-088` |
| Requirement | Configuration apply SHALL be atomic (all-or-nothing) with respect to enabling a new active rule/output set, or shall meet an Accepted alternative apply semantics decision. |
| Source | docs/005 |
| Rationale | Atomic apply. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-D-007`, `VER-DCC-DK-D-018` |
| Status | Accepted |
| Notes | If semantics undefined: escalate. |

#### REQ-DCC-V-DK-089

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-089` |
| Requirement | Compiled DCFG artifacts used on DevKit SHALL carry format version identity per existing DCFG version field; CRC coverage remains TBD and SHALL NOT be resolved in WP-007. |
| Source | ADR-015; firmware shared DCFG_VERSION |
| Rationale | DCFG identity. |
| Verification method | Inspection / Test |
| Verification reference | `VER-DCC-DK-B-007`, `VER-DCC-DK-B-015` |
| Status | Accepted |
| Notes | CRC coverage open — interface CR. |

### 2.J — Testability and observability

#### REQ-DCC-V-DK-093

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-093` |
| Requirement | Critical sense and control signals required by Phase A–D cases SHALL be accessible for measurement without destroying the assembly. |
| Source | hardware standard test points intent |
| Rationale | Accessible measurement. |
| Verification method | Inspection |
| Verification reference | `VER-DCC-DK-A-002` |
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-097

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-097` |
| Requirement | Logic/channel state and fault state SHALL be observable through diagnostic interfaces during verification. |
| Source | docs/004; DC-DCC-PWR |
| Rationale | Logic/fault observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-B-009` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-099

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-099` |
| Requirement | DCPI integrity failures (e.g. CRC error injection or equivalent controlled fault) SHALL be detectable as rejection or fault indication. |
| Source | docs/004 DCPI CRC |
| Rationale | DCPI fault observation. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-009`, `VER-DCC-DK-B-008` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | Which injections mandatory: ADR-DK-010. |

#### REQ-DCC-V-DK-101

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-101` |
| Requirement | Deterministic reset to a known de-energized starting state SHALL be available between verification cases. |
| Source | verification plan need |
| Rationale | Deterministic reset. |
| Verification method | Test |
| Verification reference | `VER-DCC-DK-A-014`, `VER-DCC-DK-D-017` |
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

### 2.L — Maintainability and reuse

#### REQ-DCC-V-DK-113

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-113` |
| Requirement | The DevKit Power implementation SHALL be replaceable without redesigning the Real-Time/Service domains' external production interface contracts (J_LP / DCPI intents). |
| Source | EDL-007 Gen2 Power swap; EDL-011 |
| Rationale | Replaceable Power. |
| Verification method | Analysis / Inspection |
| Verification reference | `VER-DCC-DK-A-008` |
| Status | Accepted |
| Notes | Physical board identity ADR-DK-001. |

#### REQ-DCC-V-DK-114

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-114` |
| Requirement | Logic and Radio interfaces used by DevKit SHALL remain reusable toward DCC Gen1 to the extent required by Accepted architecture (same physical board vs same interface — ADR-DK-001/002). |
| Source | EDL-007; docs/008 identical claim |
| Rationale | Reusable Logic/Radio. |
| Verification method | Analysis |
| Verification reference | `VER-DCC-DK-A-017` |
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
| Status | Accepted |
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
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-117

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-117` |
| Requirement | DevKit setup procedures referenced by verification cases SHALL be repeatable from documented steps and baseline identity alone. |
| Source | verification plan |
| Rationale | Repeatable setup. |
| Verification method | Demonstration |
| Verification reference | `VER-DCC-DK-A-006`, `VER-DCC-DK-A-007`, `VER-DCC-DK-D-019` |
| Status | Accepted |
| Notes | — |

#### REQ-DCC-V-DK-118

| Field | Content |
|-------|---------|
| Requirement ID | `REQ-DCC-V-DK-118` |
| Requirement | Documented recovery/rollback after failed firmware or configuration apply SHALL exist before Gate DK-B exit for configuration-delivery cases. |
| Source | RHP/rollback discipline |
| Rationale | Rollback/recovery. |
| Verification method | Inspection / Demonstration |
| Verification reference | `VER-DCC-DK-B-007` |
| Status | Accepted |
| Notes | — |

## 3. Withdrawn requirements (moved to governance)

| Withdrawn ID | Status | Moved to |
|--------------|--------|----------|
| `REQ-DCC-V-DK-002` | Withdrawn — moved to DK-GOV-001 | `DK-GOV-001` — Non-substitution of DevKit for product acceptance |
| `REQ-DCC-V-DK-003` | Withdrawn — moved to DK-GOV-002 | `DK-GOV-002` — Gate completion does not authorize vehicle install |
| `REQ-DCC-V-DK-006` | Withdrawn — moved to DK-GOV-003 | `DK-GOV-003` — Evidence-use limitation |
| `REQ-DCC-V-DK-008` | Withdrawn — moved to DK-GOV-004 | `DK-GOV-004` — EDL-014 exceptions recording |
| `REQ-DCC-V-DK-015` | Withdrawn — moved to DK-GOV-009 | `DK-GOV-009` — Equivalence claims require Accepted ADR |
| `REQ-DCC-V-DK-016` | Withdrawn — moved to DK-GOV-012 | `DK-GOV-012` — Composite baseline on verification records |
| `REQ-DCC-V-DK-028` | Withdrawn — moved to DK-GOV-024 | `DK-GOV-024` — Voltage range freeze before power-test gate exit |
| `REQ-DCC-V-DK-029` | Withdrawn — moved to DK-GOV-025 | `DK-GOV-025` — Simultaneous load current freeze before multi-load DK-C |
| `REQ-DCC-V-DK-052` | Withdrawn — moved to DK-GOV-005 | `DK-GOV-005` — No coverage claims for unrepresented classes |
| `REQ-DCC-V-DK-053` | Withdrawn — moved to DK-GOV-006 | `DK-GOV-006` — MPN prohibition in normative DevKit requirements |
| `REQ-DCC-V-DK-074` | Withdrawn — moved to DK-GOV-010 | `DK-GOV-010` — OTA gate-scope decision dependency |
| `REQ-DCC-V-DK-082` | Withdrawn — moved to DK-GOV-007 | `DK-GOV-007` — No protocol layout redefinition during DevKit verification |
| `REQ-DCC-V-DK-090` | Withdrawn — moved to DK-GOV-013 | `DK-GOV-013` — Configuration identity in evidence |
| `REQ-DCC-V-DK-091` | Withdrawn — moved to DK-GOV-011 | `DK-GOV-011` — Hot-reload assumption prohibition |
| `REQ-DCC-V-DK-092` | Withdrawn — moved to DK-GOV-008 | `DK-GOV-008` — No invented encoded-version mappings |
| `REQ-DCC-V-DK-103` | Withdrawn — moved to DK-GOV-014 | `DK-GOV-014` — Baseline required for gate-exit cases |
| `REQ-DCC-V-DK-104` | Withdrawn — moved to DK-GOV-015 | `DK-GOV-015` — Firmware identity recording |
| `REQ-DCC-V-DK-105` | Withdrawn — moved to DK-GOV-016 | `DK-GOV-016` — Bootloader identity recording |
| `REQ-DCC-V-DK-106` | Withdrawn — moved to DK-GOV-017 | `DK-GOV-017` — Hardware identity recording |
| `REQ-DCC-V-DK-107` | Withdrawn — moved to DK-GOV-018 | `DK-GOV-018` — Configuration ID/schema/hash recording |
| `REQ-DCC-V-DK-108` | Withdrawn — moved to DK-GOV-019 | `DK-GOV-019` — Protocol version recording without invented mapping |
| `REQ-DCC-V-DK-109` | Withdrawn — moved to DK-GOV-020 | `DK-GOV-020` — Test equipment and fixture identity recording |
| `REQ-DCC-V-DK-110` | Withdrawn — moved to DK-GOV-021 | `DK-GOV-021` — Evidence storage convention |
| `REQ-DCC-V-DK-111` | Withdrawn — moved to DK-GOV-022 | `DK-GOV-022` — Raw result vs certification separation |
| `REQ-DCC-V-DK-112` | Withdrawn — moved to DK-GOV-023 | `DK-GOV-023` — Physical Test Owner authority |

Full governance text: [DevKit_Verification_Governance.md](DevKit_Verification_Governance.md).

## 4. Threshold Resolution Register

```text
The Threshold Resolution Register in
docs/DevKit/DevKit_System_Requirements.md
is the authoritative source for TBD-DK identifiers.
```

Other DevKit documents, CIA, and RHP **shall reference** this register and **shall not** redefine TBD-DK meanings.

Unresolved numeric/procedure thresholds. Candidates from `docs/008` or other sources are **not** normative until closed.
**Status of all entries: Open.** No `TBD-DK-*` value is resolved in WP-007 / R1 / R2.

### 4.1 Summary

| TBD ID | Parameter | Unit | Status | Gates affected |
|--------|-----------|------|--------|----------------|
| `TBD-DK-001` | DevKit input operating voltage range | V | Open | DK-A; DK-C (UV path with TBD-DK-012) |
| `TBD-DK-002` | Approved maximum DevKit input / protection current | A | Open | DK-A |
| `TBD-DK-003` | Maximum simultaneous load current | A | Open | DK-C |
| `TBD-DK-004` | Kill response time (assert → outputs de-energized) | ms | Open | DK-A |
| `TBD-DK-005` | Watchdog response time to safe outputs | ms | Open | DK-A |
| `TBD-DK-006` | External node lost/stale timeout | ms | Open | DK-B; DK-D |
| `TBD-DK-007` | Logic↔Power control-loss timeout | ms | Open | DK-A; DK-C |
| `TBD-DK-008` | PWM frequency range for DevKit PWM cases | Hz | Open | DK-C |
| `TBD-DK-009` | Current-measurement accuracy | % or A | Open | DK-C |
| `TBD-DK-010` | Temperature-measurement accuracy | °C | Open | DK-C |
| `TBD-DK-011` | Overcurrent threshold tolerance | % or A | Open | DK-C |
| `TBD-DK-012` | Undervoltage test threshold and approved reaction table | V (plus reaction table N/A numeric) | Open | DK-C |
| `TBD-DK-013` | Fault retry delay and retry-count policy | ms (and count) | Open | DK-C |
| `TBD-DK-014` | Commanded safe-OFF de-energize time | ms | Open | DK-A; DK-C |
| `TBD-DK-015` | CAN waveform acceptance criteria | measurable metrics (N/A single unit) | Open | DK-B |
| `TBD-DK-016` | WebSocket telemetry duration and allowed loss | s / frames | Open | DK-B |
| `TBD-DK-017` | Power-rail tolerances (e.g. 5 V / 3.3 V) | % or V | Open | DK-A |
| `TBD-DK-018` | Thermal test duration (DevKit scope) | s or min | Open | DK-C |
| `TBD-DK-019` | Maximum safe surface/device temperature for DevKit tests | °C | Open | DK-C |
| `TBD-DK-020` | BOARD_ID bit encoding → revision map | N/A (map) | Open | DK-A |
| `TBD-DK-021` | Post-kill explicit re-enable sequence definition | N/A (procedure) | Open | DK-A |
| `TBD-DK-022` | Bidirectional stall response criteria and fixture definition | A / ms / procedure | Open | DK-C |

### 4.2 Controlled definitions

#### TBD-DK-001

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-001` |
| Parameter | DevKit input operating voltage range |
| Unit | V |
| Current candidate | 13.8 V nominal (single-point) |
| Candidate source | docs/008 §3 / A1 |
| Evidence required | Architecture decision + measurement plan |
| Requirements blocked | REQ-DCC-V-DK-047; DK-GOV-024 (from withdrawn REQ-028) |
| Verification cases blocked | VER-DCC-DK-A-003 |
| Gates affected | DK-A; DK-C (UV path with TBD-DK-012) |
| Owner role | System Architect / Test Owner |
| Closure artifact | Threshold CR / WP |
| Status | Open |
| Notes | Candidate is not normative. DK-GOV-024 freezes approval before DK-A power-test exit. |

#### TBD-DK-002

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-002` |
| Parameter | Approved maximum DevKit input / protection current |
| Unit | A |
| Current candidate | 30 A fuse / continuous |
| Candidate source | docs/008 §2.3 / §3.3 |
| Evidence required | Proposed ADR-021 architecture + thermal/electrical analysis + measurement (numerics remain Open until threshold WP) |
| Requirements blocked | REQ-DCC-V-DK-020; DK-GOV-025 related (withdrawn REQ-029); originating ADR-DK-006 → Proposed ADR-021 |
| Verification cases blocked | — (blocks protection sizing claims; energization cases when current limit required) |
| Gates affected | DK-A |
| Owner role | System Architect |
| Closure artifact | Threshold WP after Proposed ADR-021 Accepted (architecture); numeric approval separate |
| Status | Open |
| Notes | Pairs with Proposed ADR-021. Continuous vs fuse rating distinguished in ADR-021; candidate 30 A not approved. Status remains Open. |

#### TBD-DK-003

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-003` |
| Parameter | Maximum simultaneous load current |
| Unit | A |
| Current candidate | 30 A continuous |
| Candidate source | docs/008 §3.3 |
| Evidence required | Proposed ADR-021 simultaneous-load policy + analysis/measurement |
| Requirements blocked | DK-GOV-025 (from withdrawn REQ-029); originating ADR-DK-006 → Proposed ADR-021 |
| Verification cases blocked | — (no Phase C case IDs yet cite this ID; multi-channel simultaneous-load claims blocked) |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | Threshold WP after Proposed ADR-021 Accepted (architecture); numeric approval separate |
| Status | Open |
| Notes | Architecture direction in Proposed ADR-021 (lower base + external bank). Status remains Open. |

#### TBD-DK-004

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-004` |
| Parameter | Kill response time (assert → outputs de-energized) |
| Unit | ms |
| Current candidate | “immediately” (vague — rejected as criterion) |
| Candidate source | docs/008 A7 |
| Evidence required | Proposed ADR-022 timing hierarchy + hardware path budget + measurement plan |
| Requirements blocked | REQ-DCC-V-DK-036 |
| Verification cases blocked | VER-DCC-DK-A-012 |
| Gates affected | DK-A |
| Owner role | System Architect / Test Owner |
| Closure artifact | Threshold CR/WP; Proposed ADR-022 (policy) |
| Status | Open |
| Notes | Must become a measurable limit; vague wording rejected. Policy Proposed in ADR-022; numeric Status remains Open. |

#### TBD-DK-005

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-005` |
| Parameter | Watchdog response time to safe outputs |
| Unit | ms |
| Current candidate | <200 ms |
| Candidate source | docs/008 A6 |
| Evidence required | Proposed ADR-022 real-time safety class + measurement |
| Requirements blocked | REQ-DCC-V-DK-038 |
| Verification cases blocked | VER-DCC-DK-A-011 |
| Gates affected | DK-A |
| Owner role | System Architect / Test Owner |
| Closure artifact | Threshold CR/WP; Proposed ADR-022 (policy) |
| Status | Open |
| Notes | Candidate <200 ms not approved. Policy Proposed in ADR-022; Status remains Open. |

#### TBD-DK-006

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-006` |
| Parameter | External node lost/stale timeout |
| Unit | ms |
| Current candidate | >500 ms |
| Candidate source | docs/008 B3 |
| Evidence required | Protocol/architecture freeze |
| Requirements blocked | REQ-DCC-V-DK-079 |
| Verification cases blocked | VER-DCC-DK-B-003; VER-DCC-DK-D-004; VER-DCC-DK-D-014 |
| Gates affected | DK-B; DK-D |
| Owner role | System Architect |
| Closure artifact | docs/004 alignment CR |
| Status | Open |
| Notes | Align with DCP stale/LOST handling when frozen. |

#### TBD-DK-007

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-007` |
| Parameter | Logic↔Power control-loss timeout |
| Unit | ms |
| Current candidate | >100 ms |
| Candidate source | EDL-011 |
| Evidence required | Confirm DevKit freeze consistent with EDL-011 >100 ms; Proposed ADR-022 communication-loss class + measurement |
| Requirements blocked | REQ-DCC-V-DK-035 |
| Verification cases blocked | VER-DCC-DK-A-008; VER-DCC-DK-C-012 |
| Gates affected | DK-A; DK-C |
| Owner role | System Architect |
| Closure artifact | Threshold WP; Proposed ADR-022; EDL-011 unchanged |
| Status | Open |
| Notes | EDL-011 states >100 ms; DevKit evidence freeze still Open. ADR-022 does not change EDL-011. |

#### TBD-DK-008

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-008` |
| Parameter | PWM frequency range for DevKit PWM cases |
| Unit | Hz |
| Current candidate | not frozen |
| Candidate source | docs/008 / WP-004 TBD |
| Evidence required | Architecture + channel class decision |
| Requirements blocked | REQ-DCC-V-DK-040 |
| Verification cases blocked | VER-DCC-DK-C-003 |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | Power-channel WP |
| Status | Open |
| Notes | Conditional on PWM channel representation. |

#### TBD-DK-009

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-009` |
| Parameter | Current-measurement accuracy |
| Unit | % or A |
| Current candidate | not defined |
| Candidate source | docs/008 Phase C |
| Evidence required | Instrument + sense design qualification |
| Requirements blocked | REQ-DCC-V-DK-043; REQ-DCC-V-DK-095 |
| Verification cases blocked | VER-DCC-DK-C-004 |
| Gates affected | DK-C |
| Owner role | Hardware Engineer / Test Owner |
| Closure artifact | Fixture WP / qualification |
| Status | Open |
| Notes | Accuracy claim blocked until closed; raw dual measurements may still be recorded. |

#### TBD-DK-010

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-010` |
| Parameter | Temperature-measurement accuracy |
| Unit | °C |
| Current candidate | not defined |
| Candidate source | docs/008 thermal notes |
| Evidence required | Sensor qualification |
| Requirements blocked | REQ-DCC-V-DK-048; REQ-DCC-V-DK-096 |
| Verification cases blocked | VER-DCC-DK-C-009 |
| Gates affected | DK-C |
| Owner role | Hardware Engineer |
| Closure artifact | Qualification record |
| Status | Open |
| Notes | Used with TBD-DK-018/019 and ADR-DK-011 for thermal cases. |

#### TBD-DK-011

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-011` |
| Parameter | Overcurrent threshold tolerance |
| Unit | % or A |
| Current candidate | not defined |
| Candidate source | docs/008 C2 / WP-004 TBD |
| Evidence required | Channel-class / qualification analysis; fault-injection method per Proposed ADR-023 |
| Requirements blocked | REQ-DCC-V-DK-044 |
| Verification cases blocked | VER-DCC-DK-C-005 |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | Threshold WP; Proposed ADR-023 (method); Proposed ADR-019 (capability) |
| Status | Open |
| Notes | Numeric tolerance Open. Injection method gated by originating ADR-DK-010 → Proposed ADR-023. |

#### TBD-DK-012

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-012` |
| Parameter | Undervoltage test threshold and approved reaction table |
| Unit | V (plus reaction table N/A numeric) |
| Current candidate | <10.5 V |
| Candidate source | docs/008 C4 |
| Evidence required | Architecture decision + measurement |
| Requirements blocked | REQ-DCC-V-DK-047 |
| Verification cases blocked | VER-DCC-DK-C-008 |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | Threshold CR |
| Status | Open |
| Notes | REQ-047 also cites TBD-DK-001 for supply context; UV stimulus/reaction is this ID. |

#### TBD-DK-013

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-013` |
| Parameter | Fault retry delay and retry-count policy |
| Unit | ms (and count) |
| Current candidate | ≤3 retries (count only; delay not frozen) |
| Candidate source | docs/008 C5 |
| Evidence required | Protection policy freeze |
| Requirements blocked | REQ-DCC-V-DK-049 |
| Verification cases blocked | VER-DCC-DK-C-014 |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | Power-channel WP |
| Status | Open |
| Notes | Pass criteria need both count and delay when approved. |

#### TBD-DK-014

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-014` |
| Parameter | Commanded safe-OFF de-energize time |
| Unit | ms |
| Current candidate | not defined |
| Candidate source | WP-004 safe OFF TBD |
| Evidence required | Proposed ADR-022 commanded-shutdown class + measurement |
| Requirements blocked | REQ-DCC-V-DK-050 |
| Verification cases blocked | VER-DCC-DK-A-016; VER-DCC-DK-C-002 |
| Gates affected | DK-A; DK-C |
| Owner role | System Architect |
| Closure artifact | Threshold WP; Proposed ADR-022 |
| Status | Open |
| Notes | Used for commanded OFF timing on represented channels. |

#### TBD-DK-015

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-015` |
| Parameter | CAN waveform acceptance criteria |
| Unit | measurable metrics (N/A single unit) |
| Current candidate | “waveform clean” (vague — rejected as criterion) |
| Candidate source | docs/008 B5 |
| Evidence required | Signal-integrity criteria definition |
| Requirements blocked | REQ-DCC-V-DK-076 |
| Verification cases blocked | VER-DCC-DK-B-005 |
| Gates affected | DK-B |
| Owner role | Test Owner / System Architect |
| Closure artifact | Threshold CR |
| Status | Open |
| Notes | Must define measurable metrics (e.g. amplitude, edges); qualitative wording rejected. |

#### TBD-DK-016

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-016` |
| Parameter | WebSocket telemetry duration and allowed loss |
| Unit | s / frames |
| Current candidate | 20 Hz ≥15 s without drop |
| Candidate source | docs/008 B11 |
| Evidence required | UI contract + measurement method |
| Requirements blocked | REQ-DCC-V-DK-071 |
| Verification cases blocked | VER-DCC-DK-B-011 |
| Gates affected | DK-B |
| Owner role | System Architect / Test Owner |
| Closure artifact | docs/006 alignment |
| Status | Open |
| Notes | Conditional on WebSocket telemetry in gate scope. |

#### TBD-DK-017

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-017` |
| Parameter | Power-rail tolerances (e.g. 5 V / 3.3 V) |
| Unit | % or V |
| Current candidate | ±5 % |
| Candidate source | docs/008 A1 |
| Evidence required | Electrical design + measurement |
| Requirements blocked | REQ-DCC-V-DK-094 |
| Verification cases blocked | VER-DCC-DK-A-003 |
| Gates affected | DK-A |
| Owner role | Hardware Engineer |
| Closure artifact | DevKit electrical architecture WP |
| Status | Open |
| Notes | Per-rail list must be explicit when closed. |

#### TBD-DK-018

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-018` |
| Parameter | Thermal test duration (DevKit scope) |
| Unit | s or min |
| Current candidate | not defined for DevKit |
| Candidate source | docs/008 Phase E has Gen1 numbers |
| Evidence required | Test plan decision (DevKit vs Gen1 scope) |
| Requirements blocked | REQ-DCC-V-DK-096 |
| Verification cases blocked | VER-DCC-DK-C-009 |
| Gates affected | DK-C |
| Owner role | System Architect / Test Owner |
| Closure artifact | ADR-DK-011 |
| Status | Open |
| Notes | Do not import Gen1 Phase E durations without ADR-DK-011. |

#### TBD-DK-019

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-019` |
| Parameter | Maximum safe surface/device temperature for DevKit tests |
| Unit | °C |
| Current candidate | Gen1 candidates e.g. 85 °C (not DevKit-frozen) |
| Candidate source | docs/008 / docs/002 |
| Evidence required | Safety + thermal analysis |
| Requirements blocked | REQ-DCC-V-DK-096 |
| Verification cases blocked | VER-DCC-DK-C-009 |
| Gates affected | DK-C |
| Owner role | System Architect |
| Closure artifact | ADR-DK-011 |
| Status | Open |
| Notes | Candidate not approved for DevKit gate evidence. |

#### TBD-DK-020

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-020` |
| Parameter | BOARD_ID bit encoding → revision map |
| Unit | N/A (map) |
| Current candidate | pins exist; encoding not defined |
| Candidate source | EDL-011; ADR-015 OQ-3 |
| Evidence required | Architecture decision (no new HW mechanism) |
| Requirements blocked | REQ-DCC-V-DK-017 |
| Verification cases blocked | VER-DCC-DK-A-015 |
| Gates affected | DK-A |
| Owner role | System Architect |
| Closure artifact | Hardware identity WP |
| Status | Open |
| Notes | Conditional when BOARD_ID sensing included in baseline. |

#### TBD-DK-021

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-021` |
| Parameter | Post-kill explicit re-enable sequence definition |
| Unit | N/A (procedure) |
| Current candidate | partial intent in fault/startup docs |
| Candidate source | fault/startup documentation (repository) |
| Evidence required | Explicit sequence definition per Proposed ADR-022 path 8 |
| Requirements blocked | REQ-DCC-V-DK-034 |
| Verification cases blocked | VER-DCC-DK-A-014 |
| Gates affected | DK-A |
| Owner role | System Architect |
| Closure artifact | Threshold/procedure WP; Proposed ADR-022 |
| Status | Open |
| Notes | Sequence must be explicit and testable. |

#### TBD-DK-022

| Field | Content |
|-------|---------|
| TBD ID | `TBD-DK-022` |
| Parameter | Bidirectional stall response criteria and fixture definition |
| Unit | A / ms / procedure |
| Current candidate | motor stall candidate in docs/008 |
| Candidate source | docs/008 |
| Evidence required | Fixture + requirement freeze |
| Requirements blocked | REQ-DCC-V-DK-055 |
| Verification cases blocked | VER-DCC-DK-C-013 |
| Gates affected | DK-C |
| Owner role | Test Owner / System Architect |
| Closure artifact | Fixture WP; Proposed ADR-023 (CONDITIONAL stall class) |
| Status | Open |
| Notes | Split from former compound C-010; direction case C-010 does not use this ID. ADR-023 classifies stall as CONDITIONAL_MANDATORY. |


## 5. Architectural decisions required

`ADR-DK-001`…`ADR-DK-007` and `ADR-DK-010` now map to **Proposed** canonical ADR-016…023 (WP-008) — **not Accepted**. `ADR-DK-008`, `009`, `011`, `012` remain open requests without WP-008 ADR files. **TBDs remain Open.**

Crosswalk: [`DevKit_P0_Decision_Crosswalk.md`](DevKit_P0_Decision_Crosswalk.md).

| Originating request | Canonical ADR | Question | WP-008 status |
|---------------------|---------------|----------|---------------|
| ADR-DK-001 | [ADR-016](../ADR/ADR-016-devkit-logic-board-fidelity.md) | Same physical Logic Board vs same electrical/firmware interfaces? | Proposed |
| ADR-DK-002 | [ADR-017](../ADR/ADR-017-devkit-radio-board-fidelity.md) | Same physical Radio Board vs equivalent Service interfaces? | Proposed |
| ADR-DK-003 | [ADR-018](../ADR/ADR-018-devkit-firmware-equivalence.md) | Same compiled RT binary mandatory vs same source/feature set? | Proposed |
| ADR-DK-004 | [ADR-019](../ADR/ADR-019-devkit-represented-power-capabilities.md) | Which representative power-channel capabilities must DevKit contain? | Proposed |
| ADR-DK-005 | [ADR-020](../ADR/ADR-020-devkit-high-current-verification-scope.md) | Is a high-current class required on DevKit or only external/Gen1? | Proposed |
| ADR-DK-006 | [ADR-021](../ADR/ADR-021-devkit-input-current-architecture.md) | Approved maximum DevKit input/simultaneous current architecture? | Proposed (numerics Open) |
| ADR-DK-007 | [ADR-022](../ADR/ADR-022-devkit-kill-watchdog-timing-policy.md) | Kill/watchdog/control-loss timing policy (with TBD-DK-004/005/007/014/021)? | Proposed (numerics Open) |
| ADR-DK-008 | — | Is OTA part of mandatory DevKit gate? | Open request (not in WP-008) |
| ADR-DK-009 | — | Is configuration hot reload permitted outside Service/Wiring modes? | Open request (not in WP-008) |
| ADR-DK-010 | [ADR-023](../ADR/ADR-023-devkit-fault-injection-scope.md) | Which fault injections are mandatory and how performed safely? | Proposed |
| ADR-DK-011 | — | DevKit vs DCC Gen1 electrical/thermal environmental test split? | Open request (not in WP-008) |
| ADR-DK-012 | — | Which enclosure/connector candidates remain valid (WAGO vs screw, etc.)? | Open request (not in WP-008) |

Threshold numeric values associated with ADR-DK-006 / ADR-DK-007 / ADR-DK-011 are defined only in §4 (`TBD-DK-*`) and remain Open.


## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial Proposed baseline |
| 1.1 | 2026-07-19 | WP-007-R1 — taxonomy split; governance moved to DK-GOV-* |
| 1.1.1 | 2026-07-19 | WP-007-R1 mapping corrections for A-006/A-007 and restored case IDs |
| 1.1.2 | 2026-07-19 | WP-007-R2 — restore authoritative Threshold Resolution Register (TBD-DK-001…022) |
| 1.1.3 | 2026-07-19 | WP-007-R3 — verification references for D-015 split cases |
| 1.2 | 2026-07-20 | Architecture Review — ACCEPTED; PR #11 approved for merge (requirements structure, governance, verification-plan structure, traceability baseline) |
| 1.3 | 2026-07-20 | WP-008 — TBD register ADR references for Proposed ADR-016…023; Status Open unchanged |
