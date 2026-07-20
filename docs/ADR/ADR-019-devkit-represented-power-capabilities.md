# ADR-019: DevKit Represented Power Capabilities

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-019` |
| **Originating decision request** | `ADR-DK-004` |
| **Title** | DevKit Represented Power Capabilities |
| **Status** | Proposed |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 / WP-008-R1 |
| **Deliverable status** | Proposed — requires Architecture Review |

> This ADR is **Proposed**. Recommendations are not Accepted. Implementation Engineer cannot approve.


### Context

DevKit Power is a laboratory representative domain, not full production channel population (`REQ-DCC-V-DK-005`, `014`). Historical candidate channel counts and MPNs in `docs/002`/`007`/`008` are not authoritative freezes. DK-C cases require a declared representative capability set (`VER-DCC-DK-C-001`).

### Problem statement

Which power-channel **capabilities** must be physically represented on the DevKit (minimum set), which may be fixture-assisted or deferred, without selecting switch MPNs or final channel counts?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-003 | Smart high-side switch architecture direction (Accepted) |
| EDL-007 / EDL-014 | Three-board; DevKit gate before vehicle |
| EDL-011 | Control/sense paths via J_LP |
| Power Channel Classes (Proposed) | Abstract classes HC-A… without ampere assignment |
| REQ-DCC-V-DK-014, 039–055 | Representative outputs, PWM, sense, protection, bidirectional |
| docs/008 no-HS60 concept | Candidate exclusion of highest class on DevKit — subject to ADR-020 |

### Decision drivers

Unlock DK-C behavioural verification; keep lab energy bounded; avoid MPN-driven design; allow one physical channel to cover multiple capabilities when behaviours are not materially distinct.

### Options considered (representation strategies)

#### Option A — Maximal on-board representation (all Gen1 capability classes physically on DevKit Power)
#### Option B — Minimum representative capability set on DevKit; highest-current class per ADR-020; full population deferred to Phase E
#### Option C — Mostly fixture-emulated power behaviours (minimal on-board switches)
#### Option D — Staged: bring-up subset first, expand before DK-C exit to Option B minimum

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Weak (energy) | Strong | Unacceptable | Acceptable→Strong |
| Architecture consistency | Acceptable | Strong | Weak | Strong |
| Reuse toward DCC Gen1 | Strong | Acceptable | Weak | Acceptable |
| Representativeness | Strong | Strong | Weak | Strong at DK-C |
| Verification coverage | Strong | Strong | Weak | Strong |
| Development cost | Weak | Strong | Acceptable | Acceptable |
| Hardware cost | Weak | Strong | Acceptable | Acceptable |
| Schedule | Weak | Strong | Acceptable | Strong |
| Complexity | Weak | Strong | Weak | Acceptable |
| Debuggability | Acceptable | Strong | Weak | Strong |
| Future migration | Strong | Acceptable | Weak | Acceptable |
| Risk | Weak | Acceptable | Unacceptable | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option B (minimum representative capability set), implemented via Option D staging for bring-up.**

**Reason:** Matches DevKit purpose (EDL-014 laboratory gate) and Accepted exclusion of full production population. Option C cannot credibly verify smart-switch protection/diagnostics. Option A recreates vehicle-class energy hazards on the bench without necessity.

### Capability classification (Proposed)

| Capability | Classification | Why physical representation | Key REQs | Key cases | Multi-cap note | Cannot claim |
|------------|----------------|------------------------------|----------|-----------|----------------|--------------|
| Switched high-side ON/OFF | **MANDATORY_ON_DEVKIT** | Core PDM behaviour | 039, 050 | C-002, A-016 | Base for others | Full channel count |
| PWM-capable high-side | **MANDATORY_ON_DEVKIT** | Distinct timing/EMI/diag path | 040 | C-003 | May share HS channel if PWM truly supported | PWM on non-PWM silicon |
| Current-sensed output | **MANDATORY_ON_DEVKIT** | Protection/diag evidence | 043, 051 | C-004 | Usually same as HS | Accuracy numbers until TBD closed |
| Lower-current output (if behaviour differs materially) | **CONDITIONAL_ON_DEVKIT** | Required only if protection/diag class differs from medium | 041 | C-001 | One channel may cover if class identical | Other class ratings |
| Medium-current output | **MANDATORY_ON_DEVKIT** | Primary lab workhorse class | 014, 041 | C-001–C-006, C-014; C-007 only if OL claimed | — | Highest-class continuous |
| High-current / HC-A class continuous | **EXTERNAL_FIXTURE** or per ADR-020 | Energy/thermal burden | ADR-020 | C-* high-energy | Not required on DevKit PCB | Vehicle HC thermal |
| Bidirectional output | **MANDATORY_ON_DEVKIT** | REQ-042 requires channel or BLOCKED | 042, 054, 055 | C-010, C-011, C-013 | Dedicated bridge channel | Stall energy beyond fixture limit |
| Open-load diagnostics (where claimed) | **CONDITIONAL_ON_DEVKIT** | Required only when the selected representative channel or implementation claims open-load diagnostic capability (`REQ-DCC-V-DK-046`). If not claimed: **DEFERRED_EXCLUDED** and gate coverage shall explicitly exclude that capability. | 046 | C-007 (CONDITIONAL_MANDATORY) | May share sensed HS when claimed | Open-load on channels that do not claim the diagnostic; do not mandate OL on every smart HS |
| Overcurrent protection | **MANDATORY_ON_DEVKIT** | Hazard mitigation + DK-C | 044 | C-005 | — | Unlimited fault energy |
| Short-circuit protection | **MANDATORY_ON_DEVKIT** | Hazard mitigation + DK-C | 045 | C-006 | Fixture-limited | Vehicle harness SC |
| Thermal observation | **CONDITIONAL_ON_DEVKIT** | Required if thermal cases in DK-C scope | 048; TBD-018/019; ADR-DK-011 | C-009 | Board-level NTC may suffice | Junction accuracy |
| Retry/latch behaviour | **MANDATORY_ON_DEVKIT** | State-model evidence | 049 | C-014 | On protected channel | Infinite retry policies |
| Control-loss safe OFF | **MANDATORY_ON_DEVKIT** | EDL-011 fail-safe | 035 | C-012, A-008 | Interface + Power | Service-path dependency |

### Proposed decision text

```text
PROPOSED: The DevKit minimum representative power capability set is Option B as tabulated above.
Unconditional minimum on DevKit: switched HS, PWM-capable HS, current sense, medium-current class behaviour, overcurrent protection, short-circuit protection behaviour, retry/latch, control-loss safe OFF, and one bidirectional channel (or bidirectional Method:Test cases remain BLOCKED).
Open-load diagnostics are CONDITIONAL_ON_DEVKIT: required only when the selected representative channel or implementation claims open-load diagnostic capability. If not claimed, open-load verification is DEFERRED_EXCLUDED and gate coverage shall explicitly exclude that capability. This ADR does not require every DevKit smart high-side channel to provide open-load diagnostics and does not select an MPN to obtain that capability.
Highest-current continuous class representation follows ADR-020 (not assumed on DevKit Power PCB).
Lower-current distinct class is CONDITIONAL_ON_DEVKIT if behaviour is not materially covered by the medium-current representative.
Thermal observation is CONDITIONAL_ON_DEVKIT pending ADR-DK-011 / thermal TBDs.
This decision defines capabilities, not channel counts, connectors, or switch MPNs.
Full production population remains DCC Gen1 Phase E.
```

### Consequences

Electrical architecture WP designs to capability set; fixture WP covers EXTERNAL_FIXTURE items; DK-C inventory case becomes writable.

### Safety impact

Bounds on-board energy; bidirectional and SC tests still require fixture safety (ADR-023).

### Verification impact

Architecture blocker for capability inventory resolved **if Accepted**; implementation/fixture/threshold blockers remain; NOT VERIFIED.

### Firmware / Hardware / Configuration / Migration impact

Firmware must support represented capabilities only; config `devkit.yaml` maps logical functions to represented channels; Phase E adds full population.

### Rejected alternatives

Option C (fixture-only power); Option A as mandatory DevKit PCB population.

### Open dependencies

ADR-020, ADR-021, ADR-023; ADR-DK-011; qualification WP for switches (later).

### Requirements affected

`REQ-DCC-V-DK-005`, `014`, `039`–`055`, `026`; related power REQs.

### Verification cases affected

`VER-DCC-DK-C-001`–`C-014`; `A-016`; related D load-rule cases.

### TBDs affected

Constrains but does not close `TBD-DK-002/003/011/013/018/019/022`.

### Follow-up Work Packages

Electrical architecture; fixture/load-bank; qualification; ADR-020 acceptance.

### Rollback or supersession path

Superseding ADR.

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
| 1.1 | 2026-07-20 | Implementation Engineer (WP-008-R1) | Open-load → CONDITIONAL_ON_DEVKIT; unconditional min set clarified |

