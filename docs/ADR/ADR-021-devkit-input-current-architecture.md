# ADR-021: DevKit Input and Simultaneous-Current Architecture

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-021` |
| **Originating decision request** | `ADR-DK-006` |
| **Title** | DevKit Input and Simultaneous-Current Architecture |
| **Status** | Accepted |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 / WP-008-R1 (Accepted) |
| **Deliverable status** | Accepted — Architecture Review (2026-07-20) |

> This ADR is **Accepted** by Architecture Review (2026-07-20) for **architecture direction**. Numeric limits (`TBD-DK-002`, `TBD-DK-003`, and related constrained TBDs) remain **Open** pending threshold analysis and measurement.


### Context

`TBD-DK-002` (input/protection current) and `TBD-DK-003` (simultaneous load current) block DK-A/DK-C freezes. Candidate “30 A” values in `docs/008` are not Approved. Fuse rating ≠ continuous operating current. ADR-019/020 shape on-board vs external energy.

### Problem statement

What bench input and simultaneous-current **architecture** shall DevKit use, and how shall numeric limits be closed without inventing unsupported ratings?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| REQ-DCC-V-DK-020 | Replaceable overcurrent protection sized to approved input limit TBD-DK-002 |
| DK-GOV-025 | Simultaneous load current freeze before multi-load DK-C |
| Constitution | Protection coordination: fuse, switch, wiring, connector, software limits |
| ADR-019/020 Accepted | Capability/HC scope |
| EDL-014 | Lab gate before vehicle |

### Decision drivers

Operator safety; separable limit stack; early bring-up with current-limited first power; avoid approving 30 A by inertia; support external load bank.

### Limit stack (shall remain distinct)

PSU limit · conductor limit · connector limit · PCB limit · switch limit · fixture limit · fuse/protection rating · certified continuous operating current · peak/fault test current.

### Options considered

#### Option A — Single 30 A-class DevKit power envelope
#### Option B — Lower-current base DevKit plus external load bank for higher-energy tests
#### Option C — Multiple selectable current envelopes (operator-selected certified profiles)
#### Option D — Protection sized for higher fault current but lower certified continuous operation

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Weak (if 30 A assumed) | Strong | Acceptable | Acceptable |
| Architecture consistency | Weak | Strong | Acceptable | Acceptable |
| Reuse toward DCC Gen1 | Acceptable | Acceptable | Acceptable | Acceptable |
| Representativeness | Acceptable | Acceptable | Strong | Acceptable |
| Verification coverage | Acceptable | Strong | Strong | Acceptable |
| Development cost | Strong | Acceptable | Weak | Acceptable |
| Hardware cost | Acceptable | Acceptable | Weak | Acceptable |
| Schedule | Strong (false precision risk) | Strong | Weak | Acceptable |
| Complexity | Strong | Acceptable | Weak | Acceptable |
| Debuggability | Acceptable | Strong | Acceptable | Acceptable |
| Future migration | Acceptable | Strong | Acceptable | Acceptable |
| Risk | Unacceptable if numbers approved without evidence | Acceptable | Acceptable | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option B as the primary architecture, combined with Option D’s distinction between fault/protection sizing and certified continuous operation.**

**Reason:** Aligns with ADR-020 external high-energy path; keeps base DevKit bench envelope lower and safer for unsupervised mistakes; prevents treating candidate 30 A as approved. Option C may be added later as profiles but is not required to start. Option A alone invites false precision.

```text
Decision scope: architecture proposed; numeric limits remain Open.
```

**Residual risks:** Operators connecting external bank incorrectly; unclear labeling of envelopes.

**Evidence still required:** Thermal/copper/connector analysis; PSU capability; coordinated protection study; measurement plan — threshold WP.

**Decision that remains open:** Exact amperes for TBD-DK-002/003; related TBD-DK-001/012/017/018/019 constrained but not resolved here.

### Architecture definition (Proposed)

| Element | Proposed architecture rule |
|---------|----------------------------|
| Bench input | Lab PSU → replaceable protection → DevKit power entry; first power current-limited |
| Base DevKit continuous envelope | **Lower-current certified class** (numeric Open) covering mandatory on-board capabilities (ADR-019) |
| External load bank | Used for higher-energy / multi-load / HC discovery per ADR-020/023 |
| Simultaneous-load policy | Multi-channel simultaneous tests only within certified simultaneous budget (TBD-DK-003); otherwise single-channel or external-bank-scoped |
| Continuous vs peak/fault | Certified continuous < protection/fault test allowance; fault tests energy-limited (ADR-023) |
| Fuse/protection role | Interrupt fault energy; **not** equal to continuous rating |
| PSU role | Settable current limit for bring-up; shall not be sole protection |
| Cable/connector assumptions | Documented classes only; **no MPN selected here** |
| Thermal-analysis boundary | On-board DevKit vs external bank analyzed separately |
| Escalation | Exceeding certified envelope requires Architect-approved exception or Phase E |

### Constrained but not resolved TBDs

`TBD-DK-001`, `012`, `017`, `018`, `019` — architecture may assume separate closure; values remain Open.

### Decision text (Accepted)

```text
DECISION (Accepted): DevKit input/simultaneous-current architecture is Option B + Option D distinction.
A lower-current certified continuous base envelope applies to on-board DevKit Power operation.
Higher-energy tests use an external load bank / module under fixture safety rules.
Protection devices may be sized for higher fault interruption than the certified continuous envelope; fuse rating shall not be treated as continuous operating current.
Candidate 30 A figures remain non-approved.
TBD-DK-002 and TBD-DK-003 remain Open pending calculation and measurement evidence in a threshold Work Package.
No PSU, fuse, cable, or connector MPN is selected.
```

### Consequences

Threshold WP becomes clearly scoped; electrical architecture designs for dual-path energy.

### Safety impact

Positive — reduces default bench energy; requires explicit escalation for high energy.

### Verification impact

Architecture direction for DK-GOV-025 / REQ-020; numeric freeze still Threshold blocker; NOT VERIFIED.

### Firmware / Hardware / Configuration / Migration

Software current ceilings shall not exceed certified envelope; hardware protection coordination TBD; config shall not enable simultaneous maps beyond envelope.

### Rejected alternatives

Approving Option A 30 A without evidence; equating fuse rating to continuous current.

### Open dependencies

ADR-019, ADR-020, ADR-023; threshold analysis WP.

### Requirements affected

`REQ-DCC-V-DK-020`, `007`, `030`; `DK-GOV-024`, `DK-GOV-025`.

### Verification cases affected

`VER-DCC-DK-A-002`, `A-003`, multi-load DK-C cases, `G-004`.

### TBDs affected

**Closure method defined for** `TBD-DK-002`, `TBD-DK-003` — **Status remains Open**. Constrains `TBD-DK-001`, `012`, `017`, `018`, `019`.

### Follow-up Work Packages

Threshold-analysis WP; electrical architecture; fixture WP.

### Rollback or supersession path

Superseding ADR.

### Architecture Review section

| Field | Value |
|-------|-------|
| **Review status** | Complete |
| **Architect decision** | Accepted |
| **Approver role** | System Architect |
| **Acceptance date** | 2026-07-20 |
| **Acceptance conditions** | Architecture Accepted; numeric input/simultaneous current limits remain Open (TBD-DK-002, TBD-DK-003). |
| **Rejection / correction notes** | None — blocking architecture findings: NONE |
| **WP-008** | Accepted |
| **PR** | #12 approved for merge |


### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |
| 1.2 | 2026-07-20 | System Architect (acceptance) | Architecture Review — ACCEPTED (numerics remain Open) |
