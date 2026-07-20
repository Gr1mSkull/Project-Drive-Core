# ADR-018: DevKit Firmware Equivalence

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-018` |
| **Originating decision request** | `ADR-DK-003` |
| **Title** | DevKit Firmware Equivalence |
| **Status** | Accepted |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 / WP-008-R1 (Accepted) |
| **Deliverable status** | Accepted — Architecture Review (2026-07-20) |

> This ADR is **Accepted** by Architecture Review (2026-07-20). Implementation and verification evidence remain separate; TBD numeric thresholds (if any) remain Open unless stated otherwise.


### Context

WP-007 and `docs/008` historically imply “same firmware” as a Phase E precondition. ADR-016/017 may allow distinct DevKit Logic/Radio PCBs. ADR-015 requires identity of builds in gate baselines. No production application firmware trees are fully implemented yet (`firmware/dcc/logic` / `radio` application projects remain incomplete per gap assessment).

### Problem statement

What firmware equivalence is required between DevKit and DCC Gen1 for each firmware artifact, and what evidence may count toward gate exit?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-001 / EDL-002 | Processor and Radio separation |
| EDL-010 | Shared DCPI layouts in `firmware/shared` |
| ADR-015 | Build identity, dirty builds, composite baseline |
| Constitution | Determinism; no silent error suppression; config not hardcoded E30 |
| DK-GOV-009 | Equivalence claims require Accepted ADR |
| REQ-DCC-V-DK-013 | Configuration-driven behaviour |

### Decision drivers

Prevent false “same binary” claims; avoid production-code contamination by test hooks; preserve shared protocol/config libraries; enable board-target BSP differences; keep gate evidence meaningful.

### Options considered

#### Option A — Identical compiled binary (byte-identical application firmware)
#### Option B — Same source tree and feature set, different board-target builds
#### Option C — Same core libraries but separate DevKit application
#### Option D — Staged model (diagnostics early; production-path build required for gate certification)

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Strong if HW identical | Strong | Weak | Acceptable→Strong at gates |
| Architecture consistency | Weak unless ADR-016/017 Option A | Strong | Weak | Acceptable |
| Reuse toward DCC Gen1 | Strong | Strong | Weak | Acceptable |
| Representativeness | Strong | Strong | Weak | Acceptable→Strong |
| Verification coverage | Strong | Strong | Weak | Strong |
| Development cost | Weak | Acceptable | Weak (duplicate apps) | Acceptable |
| Hardware cost | N/A | N/A | N/A | N/A |
| Schedule | Weak | Strong | Weak | Strong |
| Complexity | Weak (forces HW identity) | Acceptable | Weak | Acceptable |
| Debuggability | Weak | Strong | Acceptable | Strong |
| Future migration | Strong | Strong | Weak | Acceptable |
| Risk | Unacceptable if claimed without HW identity | Acceptable | Unacceptable for gates | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option D for lifecycle, with Option B as the certification equivalence model for production-path artifacts.**

**Reason:** Byte-identical binaries (Option A) are only honest if Logic/Radio hardware targets are identical (ADR-016/017 Option A). Given Accepted ADR-016/017 allow separate DevKit PCBs, Option B is the coherent equivalence model: one source tree, shared `firmware/shared` protocols, board BSP/config differences producing distinct binaries with recorded identity. Separate DevKit applications (Option C) create dual maintenance and weaken gate claims.

**Residual risks:** Feature-flag drift; test hooks left enabled; dirty builds admitted as PASS contrary to ADR-015 policy.

**Evidence still required:** Build matrix documenting artifacts; BSP boundary definition; policy that test-only firmware cannot alone exit Method:Test gates that claim production behaviour.

**Decision that remains open:** Exact toolchain versions and CI gates (platform WP).

### Per-artifact proposed decisions

| Artifact | Proposed equivalence | Gate evidence rule |
|----------|---------------------|--------------------|
| Real-Time application | Option B (same tree/features; board-target build) | Required production-path build for RT Method:Test gates |
| Real-Time bootloader | Option B | Required when boot path is in scope of case |
| Service application | Option B | Required for Service Method:Test gates |
| Service bootloader | Option B | Required when OTA/boot path in scope (see ADR-DK-008) |
| Power-domain firmware (if independently programmable) | Option B or N/A if not programmable | If programmable, production-path build required for Power cases |
| Test-only / diagnostics firmware | Allowed for bring-up | **Shall not alone** support DK-A…DK-D PASS for production-behaviour claims |

### Compile-time vs runtime profile

| Mechanism | Proposed rule |
|-----------|---------------|
| Board BSP / pin map | Compile-time board target |
| Hardware capability profile (channel population) | Prefer runtime/config or BOARD_ID-driven profile; shall not silently enable channels beyond hardware |
| Feature flags | Allowed only if recorded in baseline; safety paths shall not be compilable-out for gate builds |
| Test hooks | Allowed in non-gate builds; gate builds shall document any remaining hooks; hooks shall not bypass kill |
| Dirty builds | Per ADR-015 — incomplete identity ⇒ BLOCKED / NOT ASSESSED, not PASS |
| Equivalence proof | Source revision + build flags + board target + binary hash recorded; claim “same binary” only when hashes match |

### Decision text (Accepted)

```text
DECISION (Accepted): Firmware equivalence for DevKit gate certification is Option B under staged Option D lifecycle.
DevKit and DCC Gen1 shall share one application source tree and feature set for Real-Time and Service production-path firmware, with board-support and board-target configuration permitted to produce distinct binaries.
Byte-identical binaries (Option A) shall not be claimed unless the corresponding hardware targets are the same physical assemblies and the recorded binary hashes match.
Separate DevKit-only applications (Option C) are rejected for gate certification of production behaviours.
Test-only firmware may be used for early bring-up but cannot alone generate PASS for Method:Test cases that claim production-path behaviour.
Identity recording follows ADR-015 / STD-REV-001.
This ADR does not alter build scripts or create source files.
```

### Consequences

Platform WP must define board targets and baseline recording; Phase E “same firmware” language in `docs/008` becomes “equivalent production-path build per ADR-018,” not automatic byte identity.

### Safety impact

Safety paths must exist in gate builds; test hooks must not bypass kill/global-enable.

### Verification impact

Architecture blocker for equivalence claims resolved **if Accepted**; implementation remains; evidence NOT VERIFIED.

Affected: essentially all Method:Test cases; explicitly `VER-DCC-DK-A-006`, `A-017`, `D-019`, `G-003`.

### Firmware / Hardware / Configuration / Migration impact

No file changes now. Config remains YAML→DCFG. Migration: DCC Gen1 board target added later without forking apps.

### Rejected alternatives

Option A as default claim; Option C for gates.

### Open dependencies

ADR-016, ADR-017; ADR-DK-008/009; platform WP.

### Requirements affected

`REQ-DCC-V-DK-013`, `061`–related config reqs; `DK-GOV-009`, `DK-GOV-012`; identity-related REQs.

### Verification cases affected

All Method:Test production-behaviour cases; identity cases `A-006`, `D-019`, `G-003`.

### TBDs affected

None closed.

### Follow-up Work Packages

Platform and build-system planning; firmware bring-up after architecture acceptance.

### Rollback or supersession path

Superseding ADR.


### Accepted option (Architecture Review)

```text
Accepted: staged model; Option B for certification builds
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
| **Accepted option** | staged model; Option B for certification builds |
| **Rejection / correction notes** | None — blocking architecture findings: NONE |
| **WP-008** | Accepted |
| **PR** | #12 approved for merge (merged `bdfe2b1`) |



### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |
| 1.2 | 2026-07-20 | System Architect (acceptance) | Architecture Review — ACCEPTED |
| 1.3 | 2026-07-20 | System Architect (acceptance refinement) | Review status Accepted; Accepted option recorded; acceptance conditions finalized |
