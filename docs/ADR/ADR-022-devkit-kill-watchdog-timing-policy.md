# ADR-022: DevKit Kill and Watchdog Timing Policy

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-022` |
| **Originating decision request** | `ADR-DK-007` |
| **Title** | DevKit Kill and Watchdog Timing Policy |
| **Status** | Proposed |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 |
| **Deliverable status** | Proposed — requires Architecture Review |

> This ADR is **Proposed**. Recommendations are not Accepted. Implementation Engineer cannot approve.


### Context

Multiple Open thresholds block DK-A/DK-C safety cases: `TBD-DK-004` (kill), `005` (watchdog), `007` (Logic↔Power control-loss), `014` (commanded safe-OFF), `021` (post-kill re-enable). These timings are **not** identical hazards. EDL-011 Accepted states SPI timeout **>100 ms** or `nENABLE_GLOBAL`=LOW → all outputs OFF — an authoritative constraint for the control-loss path, not automatically the kill or watchdog number.

### Problem statement

What timing **policy architecture** shall DevKit use across safety and non-safety paths, and how shall numeric thresholds be closed?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-011 | Control-loss / global-enable fail-safe; SPI timeout >100 ms → OFF |
| Constitution | Kill/isolation independent of Service/UI; per-function safe state; STM32 owns RT safety |
| REQ-DCC-V-DK-021, 031–038, 034, 035 | Kill, re-enable, control-loss, commanded OFF, watchdog |
| ADR-015 | Identity of builds under test |

**Do not change EDL-011 or protocol payloads in this ADR.**

### Decision drivers

Determinism; testability; hierarchy of urgency; prevent Service/tablet timeouts from being treated as hardware emergency; avoid inventing millisecond values without analysis.

### Options considered

#### Option A — One common safety timeout for all paths
#### Option B — Hierarchical timing classes (hardware emergency / RT safety / communication loss / commanded shutdown / service-layer)
#### Option C — Per-channel configurable timing for all paths including kill
#### Option D — Mixed: fixed safety timing classes + configurable non-safety timing

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Weak | Strong | Unacceptable for kill | Strong |
| Architecture consistency | Weak | Strong | Weak | Strong |
| Reuse toward DCC Gen1 | Acceptable | Strong | Weak | Strong |
| Representativeness | Weak | Strong | Acceptable | Strong |
| Verification coverage | Weak | Strong | Weak (combinatorial) | Strong |
| Development cost | Strong | Acceptable | Weak | Acceptable |
| Hardware cost | N/A | N/A | N/A | N/A |
| Schedule | Strong (false) | Acceptable | Weak | Acceptable |
| Complexity | Strong | Acceptable | Weak | Acceptable |
| Debuggability | Weak | Strong | Weak | Strong |
| Future migration | Weak | Strong | Weak | Strong |
| Risk | Unacceptable | Acceptable | Unacceptable | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option D (fixed safety timing + configurable non-safety), implemented using the hierarchical classes of Option B.**

**Reason:** Kill and hardware global-enable removal must be deterministic and non-bypassable by configuration. Communication-loss and commanded OFF may have different budgets. Service/tablet failures are fail-operational for power execution and must not share the hardware-emergency timeout. Per-channel configurable kill (Option C) is Unacceptable. One common timeout (Option A) conflates hazards and falsifies test meaning.

```text
Recommendation: select the architecture model now;
retain the numeric threshold as Open pending analysis or measurement.
```

**Residual risks:** Designers copying EDL-011 >100 ms into kill without analysis; configurable paths accidentally affecting safety.

**Evidence still required:** Hazard analysis; hardware path delay budget; measurement plan (start/end events); threshold CR/WP.

**Decision that remains open:** Exact ms for TBD-DK-004/005/007/014; procedure detail TBD-DK-021; TBD-DK-006 node-loss (related, not fully owned here).

### Timing paths (Proposed policy)

| # | Path | Trigger | Controlling domain | HW vs FW | Resulting state | Start event | End event | Measurement point | Timing class | Deterministic? | Auto-restart |
|---|------|---------|--------------------|----------|-----------------|-------------|-----------|-------------------|--------------|----------------|--------------|
| 1 | Hardware KILL assertion | Kill input asserted | Hardware (+ RT observe) | **Hardware-effective** | All represented outputs de-energized | Kill assert edge | All outputs de-energized | Output sense / enable chain | hardware emergency | **Fixed** | **Prohibited** |
| 2 | Global-enable removal | `nENABLE_GLOBAL` LOW | Logic→Power HW | Hardware | All outputs OFF | Enable release | Outputs OFF | Power enable rail / outputs | hardware emergency | **Fixed** | **Prohibited** until re-enable |
| 3 | Real-Time watchdog expiry | RT WD fault | Real-Time | FW+HW path to safe outputs | Safe outputs OFF | WD expiry | Outputs safe | Output state | real-time safety | **Fixed** | Policy: no auto channel re-enable |
| 4 | Logic↔Power communication timeout | SPI/comm loss > limit | Power fail-safe + Logic detect | Hardware fail-safe per EDL-011; FW detect | All outputs OFF | Last valid command / timeout start | Outputs OFF | Power side | communication loss | **Fixed** (must satisfy EDL-011 >100 ms constraint analysis) | **Prohibited** auto |
| 5 | Commanded channel OFF | Valid OFF command | Real-Time | FW | Channel OFF | Command accept | Channel de-energized | Channel output | normal commanded shutdown | Fixed upper bound; may be tighter in config **non-safety** | N/A |
| 6 | Service-domain failure | Service crash/reset | Service | FW Service | RT power continues | Service loss detect | RT still executing rules | RT outputs unchanged (fail-op) | service-layer timeout | Configurable observability | N/A (not power kill) |
| 7 | Tablet disconnect | WS/UI loss | Service | FW | RT power continues | Disconnect | RT unchanged | RT outputs | service-layer | Configurable | N/A |
| 8 | Re-enable after kill release | Kill deassert + sequence | RT + operator | FW gated by HW | Outputs remain OFF until explicit sequence | Kill release | Authorized ready | State machine | hardware emergency recovery | **Fixed sequence** (TBD-DK-021) | **Automatic restart prohibited** |

### Allowable design ranges (non-approved)

Until threshold WP closes values:

| Path | Proposed design guidance | Numeric status |
|------|--------------------------|----------------|
| Kill (1) | Shall be as fast as hardware path allows; target class ≪ communication-loss class; **no invented ms** | Open `TBD-DK-004` |
| Global enable (2) | Same hardware-emergency class as kill chain interaction | Open (tied to 004/021) |
| Watchdog (3) | Real-time safety class; must de-energize within approved `TBD-DK-005` | Open |
| Control-loss (4) | Must be consistent with EDL-011 **>100 ms** SPI timeout fail-safe; exact DevKit limit Open `TBD-DK-007` | Open (constraint exists) |
| Commanded OFF (5) | Upper bound Open `TBD-DK-014`; may be ≤ control-loss | Open |
| Service/Tablet (6–7) | Not safety power timeouts | Observability only |
| Re-enable (8) | Explicit sequence; no auto | Open procedure `TBD-DK-021` |

### Closure method

| Item | Owner role | Required analysis | Verification method |
|------|------------|-------------------|---------------------|
| TBD-DK-004/005/007/014 | System Architect (accept) after Implementation Engineer measurement plan | Path delay budget; hazard; HW feasibility | Method:Test with defined start/end |
| TBD-DK-021 | System Architect | Sequence definition | Test A-014 |
| Numeric approval artifact | Threshold CR / WP | Calculations + bench measurements | VE records later (not this WP) |

### Proposed decision text

```text
PROPOSED: Kill/watchdog/control-loss timing policy is Option D using hierarchical classes (Option B taxonomy).
Hardware emergency paths (kill, global-enable removal, post-kill re-enable rules) use fixed deterministic timing and prohibit automatic output restart.
Real-time safety (watchdog) uses fixed timing separate from kill.
Communication-loss timing is fixed and shall remain consistent with EDL-011; exact millisecond limit TBD-DK-007 remains Open.
Commanded safe-OFF has a fixed upper bound (TBD-DK-014 Open) distinct from kill.
Service-domain and Tablet failures shall not be modeled as hardware-emergency power timeouts and shall not stop required RT power execution.
Per-channel configurable kill timing is rejected.
Exact millisecond thresholds remain Open pending hazard analysis, hardware budget, and measurement plan.
EDL-011 and protocol payloads are unchanged.
```

### Consequences

Unblocks firmware/hardware timing architecture; threshold WP gets clear path list; prevents one-number safety model.

### Safety impact

High — defines which paths are non-configurable. Incorrect acceptance of Option A/C would be hazardous.

### Verification impact

Architecture blocker for timing *policy* resolved **if Accepted**; **Threshold blocker remains** for A-011, A-012, A-014, C-012; evidence NOT VERIFIED.

### Firmware / Hardware / Configuration / Migration

FW implements classes; HW kill path independent of Service; config shall not override hardware emergency timing; migrates to DCC Gen1 unchanged in policy.

### Rejected alternatives

Option A; Option C for safety paths.

### Open dependencies

Threshold WP; electrical architecture kill path; ADR-023 measurement supervision.

### Requirements affected

`REQ-DCC-V-DK-021`, `031`–`038`, `034`, `035`, `058`; related.

### Verification cases affected

`VER-DCC-DK-A-011`, `A-012`, `A-013`, `A-014`, `C-012`, `B-013`, `D-012`, `D-013`.

### TBDs affected

Closure method for `TBD-DK-004`, `005`, `007`, `014`, `021` — **all remain Open**. Notes may reference this ADR.

### Follow-up Work Packages

Threshold-analysis WP; electrical architecture; firmware planning.

### Rollback or supersession path

Superseding ADR; must not silently weaken EDL-011.

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

