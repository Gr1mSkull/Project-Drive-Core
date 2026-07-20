# ADR-016: DevKit Logic Board Fidelity and Reuse

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-016` |
| **Originating decision request** | `ADR-DK-001` |
| **Title** | DevKit Logic Board Fidelity and Reuse |
| **Status** | Proposed |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 |
| **Deliverable status** | Proposed — requires Architecture Review |

> This ADR is **Proposed**. Recommendations are not Accepted. Implementation Engineer cannot approve.


### Context

Accepted WP-007 requires the DevKit Real-Time domain to represent DCC Logic control of power channels, CAN, and safety sequencing without Service-domain dependency (`REQ-DCC-V-DK-009`, `REQ-DCC-V-DK-011`). Historical candidates in `docs/008` / `docs/007` claim “Logic identical to DCC Gen1 Rev.A,” while also listing a DevKit-only MCU alternate. Gate DK-A case `VER-DCC-DK-A-017` remains blocked until fidelity rules are decided. Electrical architecture, BOARD_ID handling, kill/global-enable path representativeness, and firmware build strategy all depend on this decision.

### Problem statement

What level of Logic-domain fidelity is required for DevKit laboratory verification versus DCC Gen1 migration, and which physical implementation forms are permitted at each gate?

### Existing authoritative constraints

| Source | Constraint | Status |
|--------|------------|--------|
| EDL-001 | Real-Time MCU family is STM32G474 (not H7); ESP32 is not the vehicle MCU | Accepted |
| EDL-007 | DCC is Logic + Power + Radio three-board architecture; Gen2 may replace Power only | Accepted |
| EDL-011 | J_LP contract: SPI control, `nKILL_HW`, `nENABLE_GLOBAL`, `FAULT_N`, sense/PWM paths; SPI timeout >100 ms or global enable LOW → all outputs OFF | Accepted |
| EDL-014 | DevKit Phase A–D (DK-A…DK-D) before vehicle; Phase E on full DCC Gen1 | Accepted |
| ADR-015 / STD-REV-001 | Composite baseline and BOARD_ID / revision identity recording | Accepted / Approved |
| Constitution | STM32 owns safety-relevant real-time; ESP32 never safety-critical | Authoritative |
| REQ-DCC-V-DK-011 | Logic↔Power interface shall be production-intent or explicitly mapped | Accepted (req) |
| REQ-DCC-V-DK-102 / 103 | Reuse / fidelity documentation | Accepted (req) |

#### ARCHITECTURAL CONFLICT (candidate documents vs Accepted EDL)

| Source A | Source B | Conflict |
|----------|----------|----------|
| EDL-001 Accepted — STM32G474 | `docs/007` §5 candidate table — STM32G431RET6 “только DevKit” | Candidate MCU alternate conflicts with Accepted processor decision |
| `docs/008` / `docs/007` “identical Logic Rev.A” wording | Gap assessment notes pin/adapter undefined | “Identical” is candidate language, not Accepted ADR |

**WP-008 does not silently resolve this conflict.** Recommendation below treats **EDL-001 as higher authority** than `docs/007` candidate BOM rows. Selecting G431 for gate certification would require an Accepted ADR that supersedes or narrowly amends EDL-001 — out of scope to invent here.

### Decision drivers

1. Safety representativeness of kill, global-enable, watchdog, and J_LP fail-safe paths.
2. Consistency with EDL-001 / EDL-007 / EDL-011.
3. Reuse toward DCC Gen1 and Gen2 Power-swap model.
4. Laboratory debug access and schedule for first certified Logic implementation.
5. Avoid claiming electrical-fault evidence from non-representative adapters.

### Fidelity vocabulary (not synonyms)

| Term | Meaning |
|------|---------|
| same physical board | Identical PCB/assembly revision shared by DevKit and DCC Gen1 Logic |
| same processor | Same Accepted MCU architecture/family (EDL-001: STM32G474 class) |
| same electrical interface | J_LP, CAN, DCPI, programming/debug, power/reset electrical contracts preserved |
| same firmware interface | HAL/BSP contracts allow shared application source per ADR-018 |
| same behavioural contract | Observable sequencing, safe states, timeouts, identity behaviour match DCC Logic intent |

### Options considered

#### Option A — Same physical production-intent Logic Board

DevKit and DCC Gen1 share the same Logic PCB/assembly revision; only Power (and possibly enclosure/fixtures) differ.

#### Option B — Separate DevKit Logic PCB with identical external contracts

Distinct laboratory Logic PCB allowed if it preserves: EDL-001 processor class; J_LP electrical/logical contract; DCPI; CAN; programming/debug; power/reset behaviour; firmware-facing interface contract.

#### Option C — Generic development board / evaluation module

Commercial STM32 eval hardware represents Logic via adapters.

#### Option D — Hybrid staged approach

Early software bring-up may use evaluation hardware; **gate certification DK-A…DK-D** requires a production-interface-conformant Logic implementation (Option B minimum); DCC Gen1 Phase E uses production-intent Logic (Option A when that PCB exists).

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Strong | Strong | Unacceptable | Acceptable→Strong at gates |
| Architecture consistency | Strong | Strong | Unacceptable | Acceptable |
| Reuse toward DCC Gen1 | Strong | Acceptable | Weak | Acceptable |
| Representativeness | Strong | Strong | Weak | Acceptable→Strong at gates |
| Verification coverage | Strong | Strong | Weak | Strong |
| Development cost | Weak | Acceptable | Strong | Acceptable |
| Hardware cost | Weak | Acceptable | Strong | Acceptable |
| Schedule | Weak | Acceptable | Strong | Strong |
| Complexity | Acceptable | Acceptable | Weak (adapters) | Acceptable |
| Debuggability | Acceptable | Strong | Strong | Strong |
| Future migration | Strong | Acceptable | Weak | Acceptable |
| Risk | Acceptable | Acceptable | Unacceptable for gates | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**. Rationale appears under each option and in the recommendation section.

### Recommended option

**Recommended option: Option D (Hybrid staged), with Option B as the minimum certification bar for DK-A…DK-D.**

**Reason:** Preserves Accepted EDL contracts and safety-path representativeness for gate evidence without forcing an immediate shared production PCB (Option A) before that PCB exists. Allows early bring-up on eval hardware without contaminating gate evidence. Rejects Option C for any Method:Test gate evidence that claims Logic electrical/safety behaviour.

**Residual risks:** Separate DevKit Logic PCB can drift from production Logic; migration surprises appear at Phase E. Mitigate with contract freeze, interface compliance checklist, and BOARD_ID / revision identity under ADR-015.

**Evidence still required:** Written J_LP/CAN/DCPI/debug contract compliance checklist; BOARD_ID encoding map; proof that DevKit Logic implements `nKILL_HW` / `nENABLE_GLOBAL` / SPI timeout fail-safe per EDL-011.

**Decision that remains open:** Whether DevKit eventually adopts the exact production Logic PCB/assembly (Option A preferred when available) — optional optimization, not a DK-A…DK-D blocker under this recommendation.

### Gate fidelity requirements

| Fidelity level | Early bring-up (pre-gate) | DK-A | DK-B | DK-C | DK-D | DCC Gen1 Phase E |
|----------------|---------------------------|------|------|------|------|------------------|
| same physical board | Not required | Not required | Not required | Not required | Not required | **Required** (production Logic) |
| same processor (EDL-001) | Preferred | **Required** | **Required** | **Required** | **Required** | **Required** |
| same electrical interface | Not required | **Required** | **Required** | **Required** | **Required** | **Required** |
| same firmware interface | As needed for experiments | **Required** for RT app evidence | **Required** | **Required** | **Required** | **Required** |
| same behavioural contract | Partial OK | **Required** for exercised paths | **Required** | **Required** | **Required** | **Required** |

### Proposed decision text

```text
PROPOSED: DevKit Logic fidelity shall follow a staged model (Option D).
Pre-gate bring-up may use evaluation hardware that does not generate DK-A…DK-D PASS evidence for Logic electrical/safety behaviour.
For Gates DK-A through DK-D, the Logic implementation shall be production-interface-conformant (Option B minimum):
  - STM32G474-class processor per EDL-001 (DevKit-only G431 candidate in docs/007 is not authorized for gate evidence without superseding EDL-001);
  - preserved J_LP, CAN, DCPI, programming/debug, power/reset, and firmware-facing contracts;
  - behavioural contracts for kill, global enable, watchdog interaction, BOARD_ID observability, and control-loss safe OFF as required by Accepted requirements.
Same physical Logic PCB/assembly as DCC Gen1 (Option A) is preferred when available but is not required to exit DK-A…DK-D.
DCC Gen1 Phase E shall use the production-intent Logic board/assembly.
Generic eval-module-only Logic (Option C) is Unacceptable as the sole Logic platform for Method:Test gate evidence claiming electrical or safety behaviour.
```

### Consequences

- Unblocks electrical architecture WP to design DevKit Logic either as shared production PCB or contract-compliant lab PCB.
- Forces ADR-018 to assume board-target builds may differ unless Option A is later chosen.
- Requires documentation of any pin adapters (still must preserve electrical contract meaning).

### Safety impact

Kill/global-enable/watchdog paths used for gate evidence must be electrically representative of EDL-011 intent. Adapter-only kill paths that do not exercise the same hardware-effective chain are insufficient for `VER-DCC-DK-A-012` claims.

### Verification impact

| Effect | Status |
|--------|--------|
| Architecture blocker for `VER-DCC-DK-A-017` | Resolved **if Accepted** |
| Implementation blocker | Remains |
| Evidence | Remains **NOT VERIFIED** |

Affected cases include: `VER-DCC-DK-A-007`, `A-008`, `A-010`…`A-017`, `B-006`, and downstream cases relying on Logic bring-up.

### Firmware impact

Board support may diverge (ADR-018). No firmware files changed by this ADR.

### Hardware impact

Authorizes concept of separate DevKit Logic PCB **or** shared production Logic; does not authorize schematics/PCB layout.

### Configuration impact

`BOARD_ID` / revision fields must distinguish DevKit Logic revision from DCC Gen1 Logic when PCBs differ (ADR-015).

### Migration impact

Phase E remains the first mandatory production-Logic evidence gate for vehicle-path hardware.

### Rejected alternatives

| Option | Rejection for certification use |
|--------|----------------------------------|
| C as sole Logic for gates | Cannot represent J_LP/kill electrical behaviour with credible fault energy paths |
| G431 DevKit-only MCU for gates | Conflicts with EDL-001 unless superseded |

### Open dependencies

- ADR-018 firmware equivalence
- BOARD_ID map (hardware identity WP)
- ADR-DK-012 connectors/enclosure (P1 — not decided here)

### Requirements affected

`REQ-DCC-V-DK-009`, `011`, `012`, `017`, `018`, `102`, `103`; related `DK-GOV-009` (equivalence claims).

### Verification cases affected

`VER-DCC-DK-A-007`, `A-008`, `A-010`–`A-017`, `B-006`; indirectly all Method:Test cases using Logic.

### TBDs affected

None closed. May inform later identity/threshold work; `TBD-DK-*` remain Open.

### Follow-up Work Packages

1. DevKit electrical architecture (Logic contract compliance)
2. Platform/build-system planning (with ADR-018)
3. DCC Gen1 Logic PCB (for Option A / Phase E)

### Rollback or supersession path

Superseding ADR; do not delete. If Architect selects Option A immediately, this ADR is Accepted with Option A as the sole certified form (still document fidelity vocabulary).

### Architecture Review section

| Field | Value |
|-------|-------|
| **Review status** | Pending Architecture Review |
| **Architect decision** | TBD |
| **Acceptance conditions** | TBD |
| **Rejection / correction notes** | TBD |

### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |

