# DevKit Verification Governance — Gen1

**Document ID:** DOC-DK-GOV-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-007-R1  
**Date:** 2026-07-19  

> Process, evidence-use, and claim-control rules for DevKit verification.  
> These are **not** system requirements of the DevKit hardware/firmware.  
> Identifier scheme: `DK-GOV-NNN`.

Related: ADR-015 / STD-REV-001; EDL-014; constitution §4/§13.

## 1. Rules

### DK-GOV-001 — Non-substitution of DevKit for product acceptance

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-001` |
| Rule | The DevKit SHALL NOT be treated as a reduced production DCC Gen1 product acceptance unit. |
| Originating requirement ID | `REQ-DCC-V-DK-002` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-002 — Gate completion does not authorize vehicle install

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-002` |
| Rule | Successful completion of DevKit gates DK-A through DK-D SHALL NOT authorize installation of DCC Gen1 into a vehicle. |
| Originating requirement ID | `REQ-DCC-V-DK-003` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-003 — Evidence-use limitation

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-003` |
| Rule | DevKit verification results SHALL be used only for laboratory validation and SHALL NOT be claimed as vehicle or track acceptance evidence. |
| Originating requirement ID | `REQ-DCC-V-DK-006` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-004 — EDL-014 exceptions recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-004` |
| Rule | Exceptions to the EDL-014 DevKit gate SHALL be recorded in a controlled engineering record and SHALL NOT be valid for track use. |
| Originating requirement ID | `REQ-DCC-V-DK-008` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-005 — No coverage claims for unrepresented classes

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-005` |
| Rule | Verification records SHALL NOT claim coverage for channel classes that are not physically represented on the tested DevKit baseline; such classes SHALL be deferred to external load-bank and/or DCC Gen1 Phase E evidence. |
| Originating requirement ID | `REQ-DCC-V-DK-052` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-006 — MPN prohibition in normative DevKit requirements

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-006` |
| Rule | Normative DevKit system requirements SHALL describe capability and behaviour and SHALL NOT require a specific smart-switch or H-bridge manufacturer part number unless an Accepted ADR/EDL mandates that exact part. |
| Originating requirement ID | `REQ-DCC-V-DK-053` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-007 — No protocol layout redefinition during DevKit verification

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-007` |
| Rule | DevKit verification activities SHALL NOT redefine DCP payload layouts or invent encoded protocol version mappings. |
| Originating requirement ID | `REQ-DCC-V-DK-082` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-008 — No invented encoded-version mappings

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-008` |
| Rule | DevKit verification and evidence recording SHALL NOT invent encoded-version mappings for DCP/DCPI/DCFG constants. |
| Originating requirement ID | `REQ-DCC-V-DK-092` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-009 — Equivalence claims require Accepted ADR

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-009` |
| Rule | Firmware and configuration equivalence claims between DevKit and DCC Gen1 SHALL follow an Accepted architectural decision defining physical boards, interfaces, source tree, feature set, and/or compiled binary meaning. |
| Originating requirement ID | `REQ-DCC-V-DK-015` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-010 — OTA gate-scope decision dependency

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-010` |
| Rule | OTA update capability SHALL be included in mandatory DevKit gate verification only if an Accepted architectural decision requires OTA for EDL-014 DevKit gate completion; otherwise OTA cases SHALL be OPTIONAL or DEFERRED_EXCLUDED. |
| Originating requirement ID | `REQ-DCC-V-DK-074` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-011 — Hot-reload assumption prohibition

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-011` |
| Rule | Configuration hot-reload outside Service/Wiring modes SHALL NOT be assumed permitted unless an Accepted architectural decision allows it. |
| Originating requirement ID | `REQ-DCC-V-DK-091` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-012 — Composite baseline on verification records

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-012` |
| Rule | Every DevKit verification record used for gate certification SHALL identify the tested system using the composite baseline fields required by STD-REV-001 / ADR-015. |
| Originating requirement ID | `REQ-DCC-V-DK-016` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-013 — Configuration identity in evidence

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-013` |
| Rule | Active configuration identity (configuration ID, schema version, and content hash when available) SHALL be recorded in verification evidence per STD-REV-001. |
| Originating requirement ID | `REQ-DCC-V-DK-090` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-014 — Baseline required for gate-exit cases

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-014` |
| Rule | Every executed DevKit verification case that supports gate exit SHALL record a composite system baseline per STD-REV-001 applicable fields. |
| Originating requirement ID | `REQ-DCC-V-DK-103` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-015 — Firmware identity recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-015` |
| Rule | Firmware identity for each programmed processor SHALL be recorded (module ID, SemVer when available, commit SHA, cleanliness). |
| Originating requirement ID | `REQ-DCC-V-DK-104` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-016 — Bootloader identity recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-016` |
| Rule | Bootloader identity SHALL be recorded when a distinct bootloader is present; otherwise evidence SHALL mark bootloader N/A with rationale. |
| Originating requirement ID | `REQ-DCC-V-DK-105` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-017 — Hardware identity recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-017` |
| Rule | Hardware board ID, hardware revision, BOM revision, and assembly revision SHALL be recorded for boards under test; missing applicable fields block certification. |
| Originating requirement ID | `REQ-DCC-V-DK-106` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-018 — Configuration ID/schema/hash recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-018` |
| Rule | Configuration ID and schema version SHALL be recorded; configuration SHA-256 SHALL be recorded when hashing is implemented, otherwise NOT RECORDED (blocks gate PASS if applicable). |
| Originating requirement ID | `REQ-DCC-V-DK-107` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-019 — Protocol version recording without invented mapping

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-019` |
| Rule | Applicable protocol/schema versions SHALL be recorded as semantic versions and/or legacy encoded values without inventing mappings. |
| Originating requirement ID | `REQ-DCC-V-DK-108` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-020 — Test equipment and fixture identity recording

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-020` |
| Rule | Test equipment identifiers and fixture revision SHALL be recorded for measurement-dependent cases. |
| Originating requirement ID | `REQ-DCC-V-DK-109` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-021 — Evidence storage convention

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-021` |
| Rule | Filled verification evidence SHALL be stored under docs/records/verification/ using the Verification Evidence template. |
| Originating requirement ID | `REQ-DCC-V-DK-110` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-022 — Raw result vs certification separation

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-022` |
| Rule | Raw tester results SHALL be distinguishable from Independent Reviewer / Test Owner certification outcomes. |
| Originating requirement ID | `REQ-DCC-V-DK-111` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-023 — Physical Test Owner authority

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-023` |
| Rule | Physical laboratory certification for DevKit gates SHALL require the human Gen1 Test Owner defined in operational project context; Implementation agents may record raw automated results only. |
| Originating requirement ID | `REQ-DCC-V-DK-112` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-024 — Voltage range freeze before power-test gate exit

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-024` |
| Rule | Normative DevKit input operating voltage range SHALL be approved (unit, limits, tolerance) before Gate DK-A exit for power tests requiring that range; until then related cases remain BLOCKED. |
| Originating requirement ID | `REQ-DCC-V-DK-028` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

### DK-GOV-025 — Simultaneous load current freeze before multi-load DK-C

| Field | Content |
|-------|---------|
| Rule ID | `DK-GOV-025` |
| Rule | Maximum simultaneous DevKit load current SHALL be approved before Gate DK-C exit for multi-channel load tests; until then related cases remain BLOCKED. |
| Originating requirement ID | `REQ-DCC-V-DK-029` (Withdrawn — moved) |
| Verification | Document/process inspection (`VER-DCC-DK-G-*`) |
| Implementation coverage | Not applicable |

## 2. Gate outcome model

Gate outcomes: `PASS` | `FAIL` | `BLOCKED` | `NOT ASSESSED`.

A gate may be `PASS` only when:

- every MANDATORY case is certified PASS;
- every applicable CONDITIONAL_MANDATORY case is certified PASS;
- all excluded capabilities are explicitly listed;
- no blocking architectural decision affects tested scope;
- all blocking thresholds for tested scope are resolved;
- the system baseline is complete for all applicable STD-REV-001 fields;
- required evidence exists;
- no unresolved critical safety finding exists.

A gate shall be `BLOCKED` when a mandatory case cannot be executed because of an open ADR, TBD, missing fixture, missing implementation, or incomplete applicable identity.

A gate shall be `FAIL` when an executed mandatory case fails.

`PARTIAL PASS` is prohibited.

## 3. Baseline identity rule for gate PASS

- Every applicable component identity required by STD-REV-001 shall be recorded.
- Unknown applicable identity blocks certification.
- `N/A` only when the component/field genuinely does not apply.
- Applicable `NOT RECORDED`, `UNKNOWN`, or `TBD` ⇒ gate `BLOCKED` or `NOT ASSESSED` (not PASS).
- Interim external identity records may be used only under an explicitly reviewed interim procedure (escalate; do not invent).

## 4. Case classification model

`MANDATORY` · `CONDITIONAL_MANDATORY` · `DEFERRED_EXCLUDED` · `OPTIONAL`

A MANDATORY case that is `BLOCKED`, `NOT EXECUTED`, `PARTIAL`, `NOT VERIFIED`, or `FAIL` blocks gate PASS.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007-R1 — initial governance rules from withdrawn REQ-DCC-V-DK-* |
