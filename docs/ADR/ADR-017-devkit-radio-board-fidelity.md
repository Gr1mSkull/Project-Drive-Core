# ADR-017: DevKit Radio Board Fidelity and Reuse

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-017` |
| **Originating decision request** | `ADR-DK-002` |
| **Title** | DevKit Radio Board Fidelity and Reuse |
| **Status** | Accepted |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 / WP-008-R1 (Accepted) |
| **Deliverable status** | Accepted — Architecture Review (2026-07-20) |

> This ADR is **Accepted** by Architecture Review (2026-07-20). Implementation and verification evidence remain separate; TBD numeric thresholds (if any) remain Open unless stated otherwise.


### Context

EDL-002 and EDL-007 require a separate Radio Board (ESP32-class) inside the DCC three-board architecture. EDL-010 requires binary DCPI between Real-Time and Service domains. WP-007 requirements demand Service-domain representation and fail-operational independence (`REQ-DCC-V-DK-010`, `012`, `018`). Historical “identical Radio Rev.A” language is candidate-only pending this decision.

### Problem statement

What Radio-domain fidelity is required for DevKit gates DK-B and DK-D, which behaviours may defer to DCC Gen1 / product qualification, and which physical forms are permitted?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-002 | Separate Radio Board; ESP32 service layer; STM32 remains vehicle MCU |
| EDL-007 | Three-board architecture |
| EDL-010 | Binary DCPI + CRC; JSON only for browser clients |
| EDL-014 | DevKit gates before vehicle |
| Constitution | ESP32 never safety-critical; Service loss shall not stop RT power execution |
| REQ-DCC-V-DK-010, 012, 018, 102, 103 | Service representation, DCPI, fail-operational, reuse |

### Decision drivers

Service/UI/OTA representativeness for gate claims; DCPI contract fidelity; reset/power-domain isolation; failure isolation; debug access; migration to production Radio; antenna/environmental fidelity vs lab needs.

### Fidelity vocabulary

Same distinctions as ADR-016: same physical board ≠ same processor class ≠ same electrical interface ≠ same firmware interface ≠ same behavioural contract.

### Options considered

#### Option A — Same physical Radio Board as DCC Gen1
#### Option B — Separate DevKit Radio Board preserving DCPI and Service contracts
#### Option C — Commercial ESP32-class development board with adapter
#### Option D — Staged approach (eval early; contract-conformant Radio for DK-B/D Method:Test service evidence)

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Acceptable | Acceptable | Weak | Acceptable |
| Architecture consistency | Strong | Strong | Weak | Acceptable |
| Reuse toward DCC Gen1 | Strong | Acceptable | Weak | Acceptable |
| Representativeness | Strong | Strong | Weak | Acceptable→Strong at gates |
| Verification coverage | Strong | Strong | Weak | Strong |
| Development cost | Weak | Acceptable | Strong | Acceptable |
| Hardware cost | Weak | Acceptable | Strong | Acceptable |
| Schedule | Weak | Acceptable | Strong | Strong |
| Complexity | Acceptable | Acceptable | Weak | Acceptable |
| Debuggability | Acceptable | Strong | Strong | Strong |
| Future migration | Strong | Acceptable | Weak | Acceptable |
| Risk | Acceptable | Acceptable | Unacceptable for DCPI/UI gate claims | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option D, with Option B as minimum for DK-B/D Service and DCPI Method:Test evidence.**

**Reason:** Service-domain behaviours needed for gates (DCPI, REST/WS, config path, fail-operational isolation) require a contract-conformant Radio implementation. Antenna pattern, RF regulatory, and environmental Radio qualification are **not** DevKit gate substitutes and may defer to DCC Gen1 / product qualification. Option C alone is Unacceptable for claiming production DCPI electrical behaviour or OTA/radio identity evidence.

**Residual risks:** DevKit Radio PCB drift; Wi-Fi lab multipath differences vs vehicle; OTA scope still open (ADR-DK-008).

**Evidence still required:** DCPI electrical compliance checklist; Service identity fields per ADR-015; documented which RF behaviours are out of DevKit scope.

**Decision that remains open:** Exact Radio module MPN (qualification WP); ADR-DK-008 OTA gate scope; whether Option A is later adopted.

### Behaviours by gate

| Behaviour | DK-B | DK-D | Defer beyond DevKit |
|-----------|------|------|---------------------|
| DCPI valid + CRC reject | **Required representative** | Sustained / config path | — |
| REST / WebSocket contracts | **Required** | Integration | — |
| Fail-operational on Service restart / tablet loss | Supporting | **Required** | — |
| OTA | Classification only until ADR-DK-008 | Per ADR-DK-008 | Product RF/reg if needed |
| Antenna / EMC / environmental RF | Not required for DK-B exit | Not required for DK-D exit | **DCC Gen1 / product qual** |
| Production Radio PCB identity | Preferred | Preferred | Phase E / product |

### Decision text (Accepted)

```text
DECISION (Accepted): DevKit Radio fidelity follows Option D.
Pre-gate bring-up may use commercial ESP32-class modules.
For DK-B and DK-D Method:Test evidence claiming DCPI, Service APIs, configuration transport, or fail-operational Service isolation, Radio shall be production-interface-conformant (Option B minimum): separate Radio domain, DCPI binary+CRC per EDL-010, power/reset isolation from Real-Time safety path, and firmware identity under ADR-015.
Same physical Radio PCB as DCC Gen1 (Option A) is preferred when available but not required to exit DK-B/D.
Antenna, EMC, and environmental Radio fidelity are out of DevKit mandatory scope unless a specific Accepted requirement later mandates them.
Option C alone is Unacceptable for those Method:Test claims.
No Radio module MPN is selected by this ADR.
```

### Consequences

Unblocks Service-domain electrical/architecture planning; clarifies RF deferral; couples to ADR-018 Service builds.

### Safety impact

Radio/Service failure must not be required for safe power execution. Gate evidence must still prove RT independence (`VER-DCC-DK-D-012`, `D-013`).

### Verification impact

Architecture blocker for Radio reuse documentation cases resolved **if Accepted**; implementation/fixture blockers remain; evidence NOT VERIFIED.

Affected: `VER-DCC-DK-A-005`, `A-009`, `B-006`–`B-015`, `D-012`, `D-013`, and Service-path cases.

### Firmware impact

Service application/bootloader board targets may differ (ADR-018).

### Hardware impact

Allows DevKit-specific Radio PCB with contract freeze; no schematic authorized.

### Configuration impact

Service identity / NVS / config path must remain compatible with `docs/005` intent.

### Migration impact

Phase E / product Radio remains authoritative for vehicle RF packaging.

### Rejected alternatives

Option C as sole Radio for DCPI/UI gate evidence — insufficient electrical/protocol representativeness.

### Open dependencies

ADR-018; ADR-DK-008; Radio module qualification; ADR-DK-012 mechanical.

### Requirements affected

`REQ-DCC-V-DK-010`, `012`, `018`, `102`, `103`; Service-related reqs in categories covering REST/WS/DCPI.

### Verification cases affected

`VER-DCC-DK-A-005`, `A-009`, `B-006`–`B-015`, `D-012`, `D-013`, related D-config cases using Service path.

### TBDs affected

None closed. `TBD-DK-006` (node loss) remains Open (timing).

### Follow-up Work Packages

Electrical architecture; platform/build; Radio qualification; ADR-DK-008 sequencing.

### Rollback or supersession path

Superseding ADR.


### Accepted option (Architecture Review)

```text
Accepted: Option D, with Option B minimum for applicable DK-B/D evidence
```

### Architecture Review section

| Field | Value |
|-------|-------|
| **Review status** | Accepted |
| **Architect decision** | Accepted |
| **Review date** | 2026-07-20 |
| **Approver role** | System Architect |
| **Acceptance date** | 2026-07-20 |
| **Acceptance conditions** | Architecture decision Accepted. Implementation, fixtures, verification evidence, and open TBD numerics (where applicable) remain outstanding per ADR text. |
| **Accepted option** | Option D, with Option B minimum for applicable DK-B/D evidence |
| **Rejection / correction notes** | None — blocking architecture findings: NONE |
| **WP-008** | Accepted |
| **PR** | #12 approved for merge (merged `bdfe2b1`) |



### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |
| 1.2 | 2026-07-20 | System Architect (acceptance) | Architecture Review — ACCEPTED |
| 1.3 | 2026-07-20 | System Architect (acceptance refinement) | Review status Accepted; Accepted option recorded; acceptance conditions finalized |
