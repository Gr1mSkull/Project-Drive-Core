# ADR-015: DriveCore Platform Revision Identity and System Baseline

| Field | Value |
|-------|-------|
| **Decision ID** | ADR-CR002-001 |
| **File ID** | ADR-015 |
| **Status** | Proposed |
| **Date** | 2026-07-19 |
| **Deciders** | System Architect (direction approved); Implementation Engineer (formalization) |
| **Work Package / CR** | ADR task following CR-002 / CR-002-R1 / CR-002-R2 |
| **Normative standard** | [docs/standards/REVISION_IDENTITY_STANDARD.md](../standards/REVISION_IDENTITY_STANDARD.md) |
| **CIA** | [CIA-2026-001](../records/change_impact/CIA-2026-001_revision-identity-baseline.md) |

---

## 1. Title

DriveCore Platform Revision Identity and System Baseline

## 2. Decision ID

**ADR-CR002-001**

File sequence per `docs/ADR/README.md` convention: **ADR-015**.

## 3. Status

**Proposed**

Do not treat as Accepted / Approved until System Architect review.

## 4. Date

2026-07-19

## 5. Context

CR-002 introduced evidence-backed validation and required every testable system state to be uniquely identifiable (constitution §6 Baseline and revision identity). The constitution explicitly states that a project-wide version-numbering scheme, if undefined, is **ARCHITECTURAL DECISION REQUIRED**.

The repository today has partial, disconnected identity fragments:

* Protocol constants (`DCP_PROTO_VER`, `DCPI_PROTO_VER`, `DCFG_VERSION`)
* HEARTBEAT `fw_version` (BCD) in `docs/004`
* YAML `config_version` / `vehicle.profile`
* Hardware prose revisions and `BOARD_ID` pins in `docs/002` / EDL-011
* Verification Evidence template fields
* No filled composite baseline records

Without a coherent decision, implementers risk inventing a single global version, treating Git SHA as release identity, or certifying tests against unidentified hardware and configuration.

## 6. Problem Statement

DriveCore must answer, for any verification result:

1. Which source revision produced the firmware?
2. Which firmware and bootloader versions were installed?
3. Which physical board revisions were tested?
4. Which BOM and assembly variants were used?
5. Which protocol and schema versions were active?
6. Which vehicle configuration was loaded?
7. Which compiled DCFG format and payload were used?
8. Which complete system baseline produced the result?

These questions cannot be answered by one opaque project version.

## 7. Decision

DriveCore shall use **independent artifact identities with a composite system baseline**.

* Each independently deployable, replaceable, configurable, or testable artifact has its own identity.
* Qualification, DevKit, bench, and vehicle-test evidence shall reference a complete baseline composed of those identities.
* No single version number shall replace the individual component identities.

Normative field definitions, formats, compatibility rules, and evidence requirements are in:

```text
docs/standards/REVISION_IDENTITY_STANDARD.md
```

This ADR is the authoritative explanation of **why** the standard exists. The standard is the normative **how**.

## 8. Identity Model

| Layer | Identity | Notes |
|-------|----------|-------|
| Firmware | Module ID + SemVer + commit SHA + cleanliness (+ toolchain when required) | Per image |
| Bootloader | Separate from application firmware | Same shape as firmware identity |
| Hardware | Board ID + hardware rev + BOM rev + assembly rev + serial | Serial ≠ design revision |
| Protocol / schema | `MAJOR.MINOR` per contract | DCP, DCPI, REST, WS, YAML, DCFG, etc. |
| Configuration | configuration ID + schema version + SHA-256 content hash | CRC ≠ content hash |
| DCFG binary | Format version + schema linkage + hash linkage + integrity CRC | Hash and CRC differ in purpose |
| System baseline | Composite of the above + fixture / equipment / toolchain as applicable | Used by verification |

Module identifiers (minimum, current architecture): `DCC-LOGIC`, `DCC-RADIO`, `DCC-POWER`, `ECU`, `BUTTON-BOX`, `DEVKIT`.

Existing `BOARD_ID` architecture is referenced, not redesigned. No new hardware identity mechanism is introduced by this ADR.

## 9. Alternatives Considered

| Option | Decision | Why insufficient / selected |
|--------|----------|-----------------------------|
| One global DriveCore version | **Rejected** | Hides firmware vs protocol vs hardware vs config divergence; makes evidence non-reproducible when only some artifacts change |
| Git SHA only | **Rejected** | Identifies source snapshot but not semantic release intent, hardware BOM/assembly, protocol contract, or configuration content |
| SemVer only | **Rejected** | Does not pin exact source commit; does not identify hardware unit or configuration bytes; dirty/local builds remain ambiguous |
| Independent artifact versions with a composite system baseline | **Selected** | Preserves each artifact’s identity and composes them into a reproducible test baseline |

## 10. Consequences

### Positive

* Verification can state exactly what was tested.
* Dirty builds and incomplete identity are excluded from high-assurance claims.
* Protocol, firmware, hardware, and configuration can evolve on independent schedules with explicit compatibility rules.
* Evidence templates and DevKit/vehicle testing gain a single normative identity vocabulary.

### Negative / cost

* More fields to record than a single version string.
* Implementation WPs required for build metadata, config hashing, and baseline capture.
* Existing partial mechanisms (HEARTBEAT BCD, DCFG CRC coverage ambiguity) need migration alignment.

### Neutral

* ADR/EDL numbering OPEN ISSUE remains; this record uses File ID ADR-015 and Decision ID ADR-CR002-001 as assigned by this task.

## 11. Compatibility Implications

* Wire formats (`docs/004`, `firmware/shared`) are **not** changed by this ADR.
* YAML profiles are **not** renamed.
* DCFG layout and CRC algorithm family remain as currently defined; CRC **coverage** remains TBD pending an interface decision.
* Unsupported major protocol/schema versions shall not be silently accepted; each interface defines its own mismatch reaction (no universal reaction in this ADR).
* Silent reinterpretation of fields, units, scaling, or safety reactions is prohibited.

## 12. Verification Implications

* Incomplete baseline identity → raw results may be recorded; certification remains `NOT VERIFIED` or `PARTIAL`.
* Phrases such as “latest firmware”, “main branch”, or “prototype board” are insufficient alone.
* Dirty firmware builds shall not support `Verified`, `Qualified`, `Approved for DevKit`, or `Approved for Prototype` evidence.
* Independent Reviewer / Test Owner certifies verification; System Architect approves architecture/policy statuses (constitution §4 / §13).

## 13. Migration Strategy

1. Accept this ADR and the Proposed standard (Architecture Review).
2. Implement firmware/bootloader build-metadata generation from authoritative Git/toolchain sources.
3. Record hardware / BOM / assembly / serial in qualification and test evidence; complete `BOARD_ID` encoding map without redesigning the hardware mechanism.
4. Align protocol/schema version documentation and mismatch reactions per interface spec.
5. Define canonical configuration bytes; implement SHA-256 content identity; keep CRC for integrity only.
6. Resolve DCFG CRC coverage TBD; add DCFG metadata linkage to schema/config hash as needed.
7. Integrate composite baseline into Verification Evidence and DevKit/vehicle test records.

Do not claim compliance for unimplemented layers.

## 14. Implementation Boundaries

This ADR and standard task shall **not**:

* Modify firmware, build scripts, hardware, KiCad, CAN messages, DCP/DCPI structures, REST/WS contracts, YAML profile contents, or DCFG binary layout
* Choose a new CRC algorithm without evidence
* Generate fake hashes, firmware versions, or hardware revisions
* Mark unverified systems compliant
* Expand into DevKit requirements redesign

## 15. Open Questions

| ID | Question | Status |
|----|----------|--------|
| OQ-1 | Exact DCFG CRC coverage (`blob[8:]` vs after full header) | TBD — interface decision required |
| OQ-2 | Canonical byte range for configuration SHA-256 | TBD — define before hash implementation |
| OQ-3 | BOARD_ID bit encoding → design revision map | TBD — existing pins; encoding NOT IMPLEMENTED |
| OQ-4 | Mapping HEARTBEAT BCD `fw_version` ↔ full SemVer + SHA metadata | TBD — do not silently change CAN payload |
| OQ-5 | Unified ADR vs EDL numbering scheme | OPEN ISSUE (pre-existing in `docs/ADR/README.md`) |
| OQ-6 | Whether a separate controlled baseline-record store is required later | Not required by this ADR; revisit if evidence duplication becomes harmful |

## 16. Related Requirements

| Reference | Relationship |
|-----------|--------------|
| Constitution §6 Baseline and revision identity | Policy driver; this ADR supplies the missing scheme |
| Constitution §6 Evidence-backed validation | Evidence must reference immutable identities |
| EDL-014 | DevKit gate — baselines apply to Phase A–F evidence |
| Traceability scaffold | Status remains NOT VERIFIED until atomic requirements + evidence exist |

No new SRS requirement IDs are invented in this ADR.

## 17. Related ADR / EDL Records

| ID | Relationship |
|----|--------------|
| EDL-007 | Three-board DCC — board families for module IDs |
| EDL-009 | DCP naming — protocol versioning context |
| EDL-010 | Binary DCPI — protocol versioning context |
| EDL-011 | J_LP / BOARD_ID — hardware revision sensing (referenced, not redesigned) |
| EDL-014 | DevKit gate — verification baseline applicability |
| CR-002 / R1 / R2 | Evidence, CIA, VE templates, status authority |

## 18. Revision History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Implementation Engineer | Initial Proposed ADR-CR002-001 / ADR-015 |
