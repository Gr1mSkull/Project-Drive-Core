# DevKit Safety Timing Analysis — WP-009

**Document ID:** DOC-DK-TIME-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-009  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer (threshold analysis)

> Converts Accepted ADR-022 timing policy into worst-case budgets, hazard ordering analysis, EDL-011 interpretation, and post-kill re-enable proposal.  
> **No millisecond value is Approved by this document.**

## 1. Scope

| Primary TBD | Path class (ADR-022) |
|-------------|----------------------|
| `TBD-DK-004` | T-Class H — hardware kill |
| `TBD-DK-005` | T-Class R — Real-Time watchdog |
| `TBD-DK-007` | T-Class C — Logic↔Power control loss |
| `TBD-DK-014` | T-Class N — commanded safe-OFF |
| `TBD-DK-021` | Recovery procedure (not ms-only) |

Service restart and Tablet disconnect are **excluded** from emergency shutdown ordering (ADR-022 fail-operational).

## 2. Timing event vocabulary

These events are **not equivalent**:

```text
kill input asserted
≠ Logic observes kill
≠ global enable falls (nENABLE_GLOBAL)
≠ switch command clears
≠ output voltage falls
≠ load current reaches safe level
```

Each TBD shall define **start event**, **end event**, and **measurement points** (ADR-022).

## 3. Worst-case budget models

### 3.1 Hardware kill — TBD-DK-004

```text
t_kill_total =
    t_input_filter
  + t_logic_or_gate
  + t_enable_propagation
  + t_power_switch_disable
  + t_load_decay
  + t_measurement_uncertainty
```

| Term | Classification | Notes |
|------|----------------|-------|
| `t_input_filter` | COMPONENT_DEPENDENT | RC/debounce on kill net; shall be minimized for emergency path |
| `t_logic_or_gate` | FIXED / COMPONENT_DEPENDENT | Hardware combinatorial path preferred over FW-only |
| `t_enable_propagation` | COMPONENT_DEPENDENT | `nENABLE_GLOBAL` / kill HW chain |
| `t_power_switch_disable` | COMPONENT_DEPENDENT | Smart switch disable latency |
| `t_load_decay` | LOAD_DEPENDENT | Inductive freewheel; lamp thermal; **requires explicit load model** |
| `t_measurement_uncertainty` | FIXED (instrument) | Scope/probe + trigger jitter |

**Start event:** Kill input active edge at DUT kill connector (or designated test point).  
**End event:** All represented outputs de-energized — defined as: output voltage < `V_off_threshold` **AND** load current < `I_safe` for all represented channels for ≥ `t_holdoff` (holdoff TBD; measurement plan proposes 10 ms observation window, NOT APPROVED).

| Field | Value |
|-------|-------|
| Acceptance status | **BLOCKED_BY_MEASUREMENT** (+ COMPONENT_DEPENDENT terms) |
| Candidate range (study only) | **1–50 ms** total depending on load — **NOT APPROVED** |
| Historical misuse rejected | EDL-011 `>100 ms` shall **not** be applied to kill |

### 3.2 Watchdog — TBD-DK-005

```text
t_watchdog_total =
    t_watchdog_expiry
  + t_fault_handler_or_reset
  + t_global_disable
  + t_power_switch_disable
  + t_load_decay
  + t_measurement_uncertainty
```

| Term | Classification | Notes |
|------|----------------|-------|
| `t_watchdog_expiry` | CONFIGURABLE_NON_SAFETY (period) but **fixed once frozen** | Window is design parameter — not same as kill |
| `t_fault_handler_or_reset` | FIRMWARE_DEPENDENT | Bounded RT handler required |
| `t_global_disable` | COMPONENT_DEPENDENT | Must reach safe outputs |
| `t_power_switch_disable` | COMPONENT_DEPENDENT | Same as kill path possibly |
| `t_load_decay` | LOAD_DEPENDENT | Same load model requirement |
| `t_measurement_uncertainty` | FIXED | |

**Start event:** Watchdog expiry condition met (injected fault).  
**End event:** Same as TBD-DK-004 safe-output definition.

| Field | Value |
|-------|-------|
| Acceptance status | **BLOCKED_BY_COMPONENT_SELECTION** (WD period) + **BLOCKED_BY_MEASUREMENT** |
| Candidate source (rejected as Approved) | docs/008 A6 `<200 ms` — **CANDIDATE only** |
| Study band (NOT APPROVED) | `t_watchdog_expiry` typically 50–500 ms class; total safe-state **must exceed kill only where policy allows** — see ordering §5 |

### 3.3 Logic↔Power control loss — TBD-DK-007

```text
t_control_loss_total =
    t_message_period
  + t_missed_message_policy
  + t_timeout_detection
  + t_power_disable
  + t_load_decay
  + t_measurement_uncertainty
```

| Term | Classification | Notes |
|------|----------------|-------|
| `t_message_period` | CONFIGURABLE_NON_SAFETY | DCPI/J_LP update rate |
| `t_missed_message_policy` | FIRMWARE_DEPENDENT | Count of missed frames before timeout |
| `t_timeout_detection` | FIRMWARE_DEPENDENT + HW fail-safe | Power-side must fail-safe per EDL-011 |
| `t_power_disable` | COMPONENT_DEPENDENT | Hardware fail-safe path |
| `t_load_decay` | LOAD_DEPENDENT | |
| `t_measurement_uncertainty` | FIXED | |

**Start event:** Last valid Logic→Power command / last valid SPI frame timestamp.  
**End event:** All outputs OFF (same safe definition).

| Field | Value |
|-------|-------|
| Acceptance status | **READY_FOR_CONDITIONAL_ACCEPTANCE** (lower bound only) |
| Lower bound (EDL-011) | DevKit freeze **shall be > 100 ms** if EDL-011 interpreted as minimum timeout threshold |
| Upper bound | **Open** — requires message period + missed-frame policy + measurement |

### 3.4 Commanded safe-OFF — TBD-DK-014

```text
t_command_off_total =
    t_command_accept
  + t_scheduler_latency
  + t_interface_transfer
  + t_switch_disable
  + t_load_decay
  + t_measurement_uncertainty
```

| Term | Classification | Notes |
|------|----------------|-------|
| `t_command_accept` | FIRMWARE_DEPENDENT | RT command path |
| `t_scheduler_latency` | FIRMWARE_DEPENDENT | Bounded |
| `t_interface_transfer` | FIRMWARE_DEPENDENT | Logic→Power if applicable |
| `t_switch_disable` | COMPONENT_DEPENDENT | Single channel |
| `t_load_decay` | LOAD_DEPENDENT | |
| `t_measurement_uncertainty` | FIXED | |

**Start event:** Valid OFF command accepted by RT domain.  
**End event:** Channel output de-energized (single-channel definition).

| Field | Value |
|-------|-------|
| Acceptance status | **BOUND_ESTABLISHED_VALUE_OPEN** |
| Ordering expectation | Should be **≤** control-loss total for same channel where comparable; **independent** of kill |
| Numeric approval | **Open** — blocked by FW scheduling freeze + component selection + measurement |

## 4. EDL-011 interpretation

**EDL CLARIFICATION REQUIRED** — partial resolution below; formal EDL note may still be needed.

### 4.1 Source text (Accepted)

From `docs/EDL/README.md` (EDL-011):

```text
Fail-safe: SPI timeout > 100 ms или nENABLE_GLOBAL=LOW → все выходы OFF.
```

### 4.2 Analysis questions

| # | Question | WP-009 finding |
|---|----------|----------------|
| 1 | Does `>100 ms` describe timeout threshold, condition after elapsed time, candidate, or exact value? | **Minimum threshold bound** on SPI loss detection before fail-safe OFF — **not** a recommended DevKit target; **not** kill/watchdog timing |
| 2 | Relationship to TBD-DK-007 | TBD-DK-007 is DevKit **evidence freeze** for communication-loss class; **must satisfy** EDL-011 constraint (DevKit limit > 100 ms unless EDL amended) |
| 3 | Message period assumptions | If period = `T_msg`, missed-frame policy must define `N_miss × T_msg + jitter < t_control_loss_total` |
| 4 | Missed frames | Not specified in EDL-011 — **FIRMWARE_DEPENDENT**; DevKit must document for freeze |
| 5 | Clock tolerance | Affects SPI timeout counter — include in budget |
| 6 | Detection granularity | Timer tick / RT schedule quantizes detection |
| 7 | Fail-safe hardware path | `nENABLE_GLOBAL`=LOW is **parallel** hardware path — not identical to SPI timeout |
| 8 | Narrower DevKit threshold? | DevKit **may** use stricter OFF behaviour if still **> 100 ms** unless EDL superseded |
| 9 | EDL clarification/supersession? | **Recommend** EDL clarification note distinguishing: (a) minimum fail-safe timeout bound, (b) DevKit certified freeze value, (c) kill timing — **do not modify EDL in WP-009** |

### 4.3 Proposed Threshold Decision Record — TBD-DK-007

```text
PROPOSED (not Approved):
- Accept lower bound: TBD-DK-007 > 100 ms (consistent with EDL-011)
- Accept closure method: budget model §3.3 + DCPI period/missed-frame table
- Defer exact ms until firmware scheduling + hardware measurement
- Escalate EDL-011 clarification as documentation CR (not EDL edit in WP-009)
Status remains Open.
```

## 5. Hazard-based timing ordering

Required ordering (ADR-022) — **not assumed achievable without proof**:

```text
t_kill_total ≤ t_global_enable_removal (effective)
t_global_enable_removal < t_watchdog_total   (strict inequality target)
t_watchdog_total < t_control_loss_total      (strict inequality target)
```

### 5.1 Commanded OFF relationship

| Comparison | Recommended policy | Rationale |
|------------|-------------------|-----------|
| Commanded OFF vs watchdog | Commanded OFF **should be faster** than watchdog expiry for single-channel normal operation | Operator expects prompt OFF; watchdog is backstop |
| Commanded OFF vs control loss | Commanded OFF **should be faster** than communication-loss shutdown for same channel | Normal command path vs fail-safe |
| Commanded OFF vs kill | Kill **always faster** — kill is hardware emergency | ADR-022 class separation |

**Analysis result:** Ordering is **architecturally required** but **not yet proven** — **BLOCKED_BY_MEASUREMENT** and component/firmware dependencies.

### 5.2 Service / Tablet exclusion

Service crash and Tablet disconnect: **no position** in emergency ordering; RT power execution continues (fail-operational).

## 6. Candidate timing classes (study)

| Class | Paths | Relative order | Candidate upper-bound study band (NOT APPROVED) | Primary blocker |
|-------|-------|----------------|--------------------------------------------------|-----------------|
| T-Class H | Kill, global-enable | Fastest | 1–50 ms total | HW path + load model + measurement |
| T-Class R | Watchdog | Slower than H | 50–500 ms (expiry-dominated) | WD period selection + FW handler |
| T-Class C | Control loss | Slowest safety path | >100 ms lower bound; upper Open | EDL-011 + DCPI period |
| T-Class N | Commanded OFF | < C for same channel | 1–100 ms study band | FW + switch + load |

**Do not treat study bands as Approved ranges.**

## 7. Post-kill re-enable — TBD-DK-021

### 7.1 Deterministic state-machine proposal

Likely result: **procedure + state machine**, not a single millisecond threshold.

```text
                    ┌─────────────────┐
         kill ────► │ KILL_ASSERTED   │
                    └────────┬────────┘
                             │ outputs OFF; latched safe
                             ▼
                    ┌─────────────────┐
         kill ────► │ KILL_RELEASED_  │
         release    │ LOCKED          │
                    └────────┬────────┘
                             │ no auto enable
                             ▼
                    ┌─────────────────┐
         operator ─►│ OPERATOR_ACK_   │
         ack         │ REQUIRED        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
         faults ──►│ FAULT_CLEAR_    │
         cleared    │ REQUIRED        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ READY_FOR_      │
                    │ ENABLE          │
                    └────────┬────────┘
                             │ explicit enable only
                             ▼
                    ┌─────────────────┐
         per-func ─►│ EXPLICIT_       │
         enable      │ FUNCTION_ENABLE │
                    └────────┬────────┘
                             ▼
                    Outputs may energize per new commands
```

### 7.2 State rules

| State | Entry condition | Outputs | Prohibited |
|-------|-----------------|---------|------------|
| KILL_ASSERTED | Kill active | OFF | Any enable |
| KILL_RELEASED_LOCKED | Kill deasserted | OFF | Auto-restore prior ON commands |
| OPERATOR_ACK_REQUIRED | Ack event required | OFF | Service/Tablet auto-ack as sole authority |
| FAULT_CLEAR_REQUIRED | Applicable faults latched | OFF | Enable with uncleared faults |
| READY_FOR_ENABLE | Ack + faults clear + RT checks | OFF | Implicit enable |
| EXPLICIT_FUNCTION_ENABLE | Per-function enable commands | Per command | Stale command replay |

### 7.3 Logging requirements

Each transition shall produce deterministic log/diagnostic record (timestamp source: RT monotonic clock).

### 7.4 WP-009 disposition — TBD-DK-021

| Field | Value |
|-------|-------|
| Acceptance status | **READY_FOR_ACCEPTANCE** (procedure/state machine) |
| Numeric ms component | Optional sub-limits for ack timeout — **separate optional TBD**; not required for initial acceptance |
| Verification | VER-DCC-DK-A-014 |
| Blockers | Firmware implementation (future WP); Architect acceptance of sequence |

### Proposed Threshold Decision Record — TBD-DK-021

```text
PROPOSED (not Approved):
- Accept state-machine procedure as TBD-DK-021 primary artifact
- Reject kill-release-alone re-energization
- Reject Service/Tablet as re-enable authority
- Optional: add operator-ack timeout numeric in future CR
Status remains Open until Architect accepts procedure.
```

## 8. Per-threshold summary

| TBD | Budget | Candidate / bound | Uncertainty | Recommendation | Blocker |
|-----|--------|-------------------|-------------|----------------|---------|
| TBD-DK-004 | §3.1 | Study 1–50 ms | Load + instrument | Accept closure method; defer numeric | Measurement + HW |
| TBD-DK-005 | §3.2 | Expiry TBD | WD period + handler | Accept closure method; defer numeric | Component + FW + measurement |
| TBD-DK-007 | §3.3 | **Lower >100 ms** | Period/missed frames | Conditional lower bound; defer upper | EDL clarification + measurement |
| TBD-DK-014 | §3.4 | Study 1–100 ms | FW + load | Accept closure method; defer numeric | FW + component + measurement |
| TBD-DK-021 | §7 | Procedure | N/A (procedural) | **Accept state machine** pending review | Architect acceptance |

## 9. Safety acceptance metric

```text
approved_limit ≥ measured_worst_case + measurement_uncertainty + design_margin
```

**Mean values alone are insufficient** for safety limits (DK-GOV / constitution alignment).

## 10. Requirement and verification trace

| TBD | Requirements | Cases |
|-----|--------------|-------|
| TBD-DK-004 | REQ-DCC-V-DK-036 | VER-DCC-DK-A-012 |
| TBD-DK-005 | REQ-DCC-V-DK-038 | VER-DCC-DK-A-011 |
| TBD-DK-007 | REQ-DCC-V-DK-035 | VER-DCC-DK-A-008; VER-DCC-DK-C-012 |
| TBD-DK-014 | REQ-DCC-V-DK-037 | VER-DCC-DK-A-014; VER-DCC-DK-C-* |
| TBD-DK-021 | REQ-DCC-V-DK-021, 031–034 | VER-DCC-DK-A-014 |

## 11. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial safety timing analysis |
