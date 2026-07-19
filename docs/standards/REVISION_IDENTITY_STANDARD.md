# DriveCore Revision Identity Standard

**Document ID:** STD-REV-001  
**Version:** 1.0.1  
**Status:** Approved  
**Canonical ADR ID:** ADR-015  
**Originating Decision Request:** ADR-CR002-001  
**Originating Change Request:** CR-002  
**ADR:** [ADR-015-platform-revision-identity.md](../ADR/ADR-015-platform-revision-identity.md)  
**Date:** 2026-07-19  
**Related CIA:** [CIA-2026-001](../records/change_impact/CIA-2026-001_revision-identity-baseline.md)

> Normative source for revision identity fields, formats, compatibility rules, and verification baseline requirements.  
> Authoritative rationale: **ADR-015**. Engineering policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6.  
> Approval of this standard does **not** mean runtime mechanisms are implemented or verified.

---

## 1. Purpose

Every tested DriveCore system state shall be reproducible and unambiguously identifiable.

The system shall answer:

* Which source revision produced the firmware?
* Which firmware and bootloader versions were installed?
* Which physical board revisions were tested?
* Which BOM and assembly variants were used?
* Which protocol and schema versions were active?
* Which vehicle configuration was loaded?
* Which compiled DCFG format and payload were used?
* Which complete system baseline produced a verification result?

---

## 2. Composite identity model

DriveCore shall use a **composite system identity**.

Each independently deployable, replaceable, configurable, or testable artifact shall have an independent identity. The complete **system baseline** combines these identities.

The following shall **not** be treated as equivalent:

| Identity class | Not a substitute for |
|----------------|----------------------|
| Project / handbook version | Firmware, protocol, hardware, or config identity |
| Firmware version | Bootloader, protocol, hardware, or config identity |
| Protocol version | Firmware release or config content |
| Hardware revision | BOM, assembly, or serial identity |
| Configuration version / hash | Firmware or protocol identity |
| System test baseline | Any single component identity |

No single version number shall replace the individual component identities.

---

## 3. Module identifiers

Stable module identifiers (board / node families present in current Gen1 architecture):

| Module ID | Artifact / role |
|-----------|-----------------|
| `DCC-LOGIC` | DCC Logic Board / STM32 application domain |
| `DCC-RADIO` | DCC Radio Board / ESP32 service domain |
| `DCC-POWER` | DCC Power Board (including DevKit Power Rev.DK family) |
| `ECU` | Engine Control Unit node |
| `BUTTON-BOX` | Button Box HMI node |
| `DEVKIT` | DevKit platform / fixture identity (lab gate per EDL-014) |

Rules:

* Module identifiers shall remain stable across ordinary version changes.
* Renaming a module identifier requires compatibility and migration analysis (Level 2 CIA).
* Do not invent additional module identifiers without architecture approval.
* CAN Device Type / node IDs (`docs/004`, `firmware/shared`) remain protocol addressing; they do not replace module identifiers above.

---

## 4. Firmware identity

Each independently deployable firmware image shall define:

| Field | Requirement |
|-------|-------------|
| Module identifier | Stable ID from §3 (e.g. `DCC-LOGIC`, `DCC-RADIO`, `ECU`, `BUTTON-BOX`) |
| Release version | `MAJOR.MINOR.PATCH` (SemVer) |
| Source commit SHA | Full Git commit SHA in diagnostic / build metadata |
| Build type | e.g. release / development — exact enumeration **TBD** at implementation |
| Build cleanliness | `clean` or `dirty` |
| Toolchain identity | Recorded where required for reproducibility |

### 4.1 Semantic version meaning

* `MAJOR` — incompatible behaviour, interface, configuration, or deployment change
* `MINOR` — backward-compatible functionality
* `PATCH` — backward-compatible correction

### 4.2 Development builds

Development builds shall include Git identity.

Recommended human-readable build identity:

```text
<semver>-dev+g<short-git-sha>
```

Example (illustrative format only — not a claimed current build):

```text
0.2.0-dev+g9082ad0bd0d9
```

Rules:

* Full commit SHA shall be available in diagnostic or build metadata.
* Shortened SHA may be used only for human-readable display.
* Build timestamps shall **not** be the primary identity.
* Firmware built from a dirty working tree shall be marked `dirty`.
* Dirty builds shall **not** support `Verified`, `Qualified`, `Approved for DevKit`, or `Approved for Prototype` evidence.
* Release version and Git SHA shall not be manually duplicated in multiple source files.
* Build metadata should be generated from an authoritative source during the build process.

**Implementation status:** build-metadata generation is **NOT IMPLEMENTED**. This standard defines the rule only.

HEARTBEAT field `fw_version` (BCD major.minor) in `docs/004` remains a wire representation — mapping to full SemVer + SHA is a future implementation concern and shall not silently redefine the CAN payload in this standard.

---

## 5. Bootloader identity

Every independently deployable bootloader shall have an identity **separate** from application firmware.

Record:

| Field | Requirement |
|-------|-------------|
| Bootloader module identifier | Stable module ID (§3) |
| Bootloader semantic version | `MAJOR.MINOR.PATCH` |
| Bootloader source commit SHA | Full SHA in metadata |
| Bootloader build cleanliness | `clean` or `dirty` |

Rules:

* Application firmware version shall not imply bootloader version.
* Updating application firmware shall not silently overwrite or reinterpret bootloader identity.

**Implementation status:** bootloader identity metadata is **NOT IMPLEMENTED**.

---

## 6. Hardware identity

Each physical board used for development, qualification, or vehicle testing shall record:

| Field | Meaning | Example representation |
|-------|---------|------------------------|
| Board identifier | Board family | `DCC-LOGIC` |
| Hardware design revision | Electrical / PCB design revision | `Rev.A` |
| BOM revision | Approved component population | `BOM-001` |
| Assembly revision | Built assembly definition / variant | `ASSY-001` |
| Unit serial number | One physical unit | Manufacturing identity (separate) |

Rules:

* Board ID identifies the board family.
* Hardware revision identifies electrical or PCB design revision.
* BOM revision identifies the approved component population.
* Assembly revision identifies the built assembly definition or variant.
* Serial number identifies one physical unit and is **not** a design revision.
* Physical revision marking is mandatory for testable hardware.
* Machine-readable revision identity shall be used where existing architecture supports it.
* This standard shall **not** introduce a new EEPROM, resistor network, MCU, connector, or other hardware mechanism.
* Existing `BOARD_ID` architecture (`docs/002`, EDL-011) shall be referenced, not redesigned.
* `BOARD_ID` bit encoding map (value → design revision) remains **TBD** / **NOT IMPLEMENTED**.

Hardware qualification evidence without board, hardware, BOM, and assembly identity shall be classified as **non-reproducible**.

---

## 7. Protocol and interface versions

Each persistent or cross-module contract shall have an independent version.

Applicable contracts include, where present:

* DCP
* DCPI
* CAN message catalog
* REST API
* WebSocket telemetry schema
* Configuration YAML schema
* DCFG binary format
* Persistent logs
* Calibration formats
* Firmware metadata structures
* Hardware identification structures

### 7.1 Semantic version vs encoded representation

Three distinct concepts shall be kept separate:

| Concept | Meaning |
|---------|---------|
| Human-readable semantic contract version | Normative `MAJOR.MINOR` for the interface |
| Encoded wire or binary-format value | Compact numeric/byte representation on the wire or in a binary header |
| Mapping | Explicit rule relating the encoded value to the semantic version |

```text
An encoded numeric value shall not be interpreted as MAJOR.MINOR
unless the interface specification explicitly defines the encoding.
```

The normative human-readable version uses `MAJOR.MINOR`.

A protocol or binary format may use a compact encoded representation, but its bit/byte encoding and mapping to `MAJOR.MINOR` shall be defined by that interface specification.

Existing raw values remain **legacy encodings** until such mapping is approved.

* `MAJOR` — breaking or incompatible change
* `MINOR` — backward-compatible additive change

### 7.2 Rules

* Editorial documentation corrections shall not increment a wire-format version.
* Field meaning, unit, scaling, sign, offset, endianness, timeout, stale behaviour, or safety reaction shall not change without a version decision.
* An unsupported major version shall not be silently accepted.
* Each interface specification shall define its own mismatch reaction.
* This standard does **not** define one universal mismatch reaction for all interfaces.
* Silent reinterpretation is prohibited.
* Compatibility shall be explicit and testable.

For every applicable interface, future specifications shall define:

* semantic version;
* encoded representation;
* byte width;
* byte order where applicable;
* mapping rule;
* unsupported-version reaction;
* compatibility rule.

### 7.3 Current repository anchors

Do not invent new values or mappings here.

| Contract | Current documented / coded identity | Status |
|----------|-------------------------------------|--------|
| DCP | Doc title v0.1; encoded `DCP_PROTO_VER = 0x01` — legacy encoded value; semantic mapping TBD | PARTIAL |
| DCPI | Encoded `DCPI_PROTO_VER = 0x01`; CRC-16/CCITT on frames — legacy encoded value; semantic mapping TBD | PARTIAL |
| DCFG format | Encoded `DCFG_VERSION = 0x0001` — legacy encoded value; semantic mapping TBD | PARTIAL |
| YAML schema | Human-readable `config_version: "0.1"` in vehicle profiles | PARTIAL |
| REST | Base path `/api/v1/` | PARTIAL |
| WebSocket telemetry schema | No explicit schema version field found | NOT IMPLEMENTED |

Do **not** state or imply `0x01 = 0.1`, `0x01 = 1.0`, `0x0001 = 0.1`, or `0x0001 = 1.0` unless an approved interface specification explicitly defines that mapping.

Do not change existing protocol constants or payload layouts under this standard alone.

---

## 8. Configuration identity

Each active vehicle configuration shall define:

| Field | Requirement |
|-------|-------------|
| `configuration_id` | Human-readable stable profile ID (e.g. existing `e30_gen1`, `devkit`) |
| `schema_version` | Configuration YAML schema version (`MAJOR.MINOR` string or equivalent) |
| `content_hash` | SHA-256 of deterministic canonical configuration content |

Rules:

* Do not rename existing profiles in documentation-only work without an authorized task.
* Full lowercase hexadecimal SHA-256 shall be stored in verification evidence.
* A shortened form may be shown in diagnostic UI, but shall not replace the full evidence value.
* The hash shall identify deterministic canonical configuration content.
* The exact canonical byte range shall be defined in the configuration or DCFG format specification **before** implementation.
* If deterministic canonical output is not currently guaranteed, record status as `NOT VERIFIED`.
* A CRC shall **not** be used as the configuration identity hash.
* A content hash shall **not** replace schema version.

**Implementation status:** configuration content hashing and canonicalization are **NOT IMPLEMENTED**. Deterministic canonical output is **NOT VERIFIED**.

---

## 9. DCFG binary identity and integrity

The compiled DCFG artifact shall define:

| Field | Purpose |
|-------|---------|
| DCFG format version | Human-readable semantic format version (`MAJOR.MINOR`); encoded wire/binary value separate per §7 |
| Source configuration schema version | Schema that produced the blob |
| Configuration ID or reference | Link to active profile |
| Content identity hash or linkage | SHA-256 identity (§8) |
| Integrity CRC | Accidental corruption detection |

`DCFG_VERSION = 0x0001` is a **legacy encoded value with interface-specific semantic mapping TBD**. It shall not be interpreted as `0.1` or `1.0` unless an approved DCFG interface specification defines that mapping.

### 9.1 Hash vs CRC

| Mechanism | Purpose |
|-----------|---------|
| SHA-256 | Identifies configuration **content** |
| CRC | Detects accidental **corruption** of the binary payload |

### 9.2 Existing CRC

Repository already defines CRC-16/CCITT-FALSE (`poly 0x1021`, `init 0xFFFF`) in `firmware/shared` and `tools/config_compiler/crc16.py`.

Do **not** select a new CRC algorithm in this standard.

**OPEN ISSUE / TBD — preserved:**

```text
CRC-16/CCITT-FALSE algorithm family is known.
Exact DCFG CRC coverage remains TBD.
```

Two current interpretations (neither selected by ADR-015 or this standard):

* Compiler implementation (`tools/config_compiler/compiler.py`): CRC over `blob[8:]`.
* Informal note (`agents_stuff/config_binary_v0.1.md`): CRC over payload after the full header.

A separate interface Change Request shall resolve coverage after ADR-015 is merged. Do not modify the config compiler, shared headers, informal notes, or `docs/005` under this standard alone.

---

## 10. System baseline

Every qualification, DevKit, bench, or vehicle-test record shall be associated with a complete system baseline.

Record where applicable:

* Repository commit SHA
* Firmware version and SHA for every processor
* Bootloader version and SHA
* Hardware board IDs
* Hardware revisions
* BOM revisions
* Assembly revisions
* Physical serial numbers
* DCP version
* DCPI version
* API or telemetry schema versions
* Configuration ID
* Configuration schema version
* Configuration SHA-256
* DCFG format version
* Test fixture revision
* Test equipment identifiers
* Compiler or toolchain version when relevant

The baseline may be embedded in verification evidence or referenced from a controlled baseline record.

Do **not** create a separate baseline-record subsystem unless later architecture requires it. Prefer a stable reference over manual duplication across evidence records.

Insufficient alone (examples):

```text
latest firmware
current board
test version
working build
main branch
prototype board
```

---

## 11. Verification rules

A verification result shall not be certified unless the tested baseline is sufficiently identified.

Verification evidence shall reference immutable identities. The Independent Reviewer or Test Owner shall be able to determine exactly what was tested.

If identity information is incomplete:

```text
Result may be recorded as raw evidence,
but verification certification shall remain NOT VERIFIED or PARTIAL.
```

Authority remains per constitution §4 / §13: Implementation Engineer may record raw results; Independent Reviewer / Test Owner certifies verification outcomes.

---

## 12. Source-of-truth rules

Each version or revision value shall have one authoritative source.

Prohibited:

* Manually maintaining the same firmware version in multiple files
* Manually copying protocol versions into unrelated documentation
* Using filenames as the only revision identity
* Using branch names as immutable identity
* Using timestamps as the only build identity
* Using CRC as a substitute for configuration identity
* Using Git SHA as a substitute for semantic release version
* Using semantic version as a substitute for exact source commit

Generated artifacts shall derive identity from authoritative sources where practical. Supporting documentation shall cross-reference rather than duplicate normative values.

---

## 13. Evidence field mapping

When filling `docs/templates/Verification_Evidence_Template.md`, map fields to this standard:

| VE template field | Standard reference |
|-------------------|--------------------|
| Commit SHA | Repository commit (§10) |
| Hardware Revision | Hardware identity (§6) — expand BOM/assembly/serial as applicable |
| Firmware Version | Firmware identity (§4) — per processor / module |
| Bootloader Version | Bootloader identity (§5) |
| Configuration ID | §8 `configuration_id` |
| Configuration Hash | §8 SHA-256 (full hex in evidence) |
| Protocol Version | §7 — record each applicable contract version |

Use `N/A` only when a field does not apply. Unknown applicable fields: `TBD`, `UNKNOWN`, or `NOT RECORDED`.

---

## 14. Related documents

| Document | Role |
|----------|------|
| [ADR-015](../ADR/ADR-015-platform-revision-identity.md) | Decision and rationale (canonical ID); originating request ADR-CR002-001 |
| `.cursor/ENGINEERING_CONSTITUTION.mdc` §6 | Policy requirement for baseline identity |
| `docs/002_DCC_Hardware.md` | BOARD_ID / board revisions |
| `docs/004_Communication_Protocol.md` | DCP / DCPI / HEARTBEAT |
| `docs/005_Configuration_Model.md` | YAML / DCFG |
| `docs/008_Testing_and_Validation.md` | DevKit / vehicle test process |
| `docs/templates/Verification_Evidence_Template.md` | Evidence scaffold |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | Initial Proposed standard (originating request ADR-CR002-001) |
| 1.0.1 | 2026-07-19 | ADR-015-R1 — Approved; canonical ADR-015; semantic vs encoded version rules |
