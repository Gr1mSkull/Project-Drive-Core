# DevKit Safety Timing Analysis — WP-009

**Document ID:** DOC-DK-TIME-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-009 / WP-009-R1 (Accepted)  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer (threshold analysis)

> Converts Accepted ADR-022 timing policy into worst-case budgets, hazard ordering analysis, EDL-011 interpretation, and post-kill re-enable proposal.  
> **Architecture Review Accepted (2026-07-20).** Budget structures and measurement methods Accepted. **No millisecond value is Approved.**

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
| Candidate range | **Open** — no numeric direction authorized pending measurement |
| Historical misuse rejected | EDL-011 `>100 ms` shall **not** be applied to kill; shall **not** be treated as an accepted lower bound for TBD-DK-007 |

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
| Study note | Expiry-dominated; numeric Open pending WD period selection |

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
| Acceptance status | **BLOCKED_BY_EDL_CLARIFICATION** |
| Numeric direction | **None authorized** — do not infer `>100 ms` or `≤100 ms` from EDL-011 |
| Budget and measurement | Retained — see §3.3 and Measurement Plan §3.3 |

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

**EDL CLARIFICATION REQUIRED** — WP-009-R1 removes any inferred numeric direction from EDL-011 for TBD-DK-007.

### 4.1 Source text (Accepted)

From `docs/EDL/README.md` (EDL-011):

```text
Fail-safe: SPI timeout > 100 ms или nENABLE_GLOBAL=LOW → все выходы OFF.
```

This text is **semantically ambiguous**. WP-009-R1 documents plausible readings without selecting one.

### 4.2 Plausible readings

#### Reading A — Timeout threshold interpretation

If no valid SPI exchange occurs for approximately 100 ms, the fail-safe condition becomes true.

This **could** imply a nominal detection threshold around 100 ms.

#### Reading B — Requirement-condition interpretation

Whenever elapsed SPI silence exceeds 100 ms, outputs shall already be or shall become OFF.

This **could** imply an upper response requirement, not a lower bound.

#### Reading C — Historical implementation statement

The text records an earlier architecture candidate rather than a fully toleranced threshold.

### 4.3 Mandatory disposition — TBD-DK-007

```text
Acceptance readiness: BLOCKED_BY_EDL_CLARIFICATION
```

**Do not recommend:**

- `TBD-DK-007 > 100 ms` as an accepted lower bound
- `TBD-DK-007 ≤ 100 ms` as accepted either

Architecture Review may accept **closure method only** (budget §3.3 + measurement plan) — not a numerical direction until EDL clarification is completed.

### 4.4 Proposed EDL clarification question

```text
Does EDL-011 intend:

A. a nominal communication-loss detection timeout of 100 ms;
B. a maximum elapsed communication-loss interval before outputs are OFF;
C. a minimum filtering interval before declaring communication loss;
D. another explicitly defined timing contract?
```

**Do not silently choose an answer.**

### 4.5 Relationship to budget and measurement

| Item | Status |
|------|--------|
| Control-loss budget model §3.3 | Retained |
| Measurement plan §3.3 | Retained |
| Numeric pass criterion for TBD-DK-007 | **Blocked** until EDL clarification + Architect acceptance |
| Kill / watchdog paths | Unaffected — EDL-011 text shall not be copied to those paths |

### 4.6 Proposed Threshold Decision Record — TBD-DK-007

```text
PROPOSED (not Approved):
- Accept closure method: budget model §3.3 + DCPI period/missed-frame table + measurement plan
- Reject numeric direction inferred from EDL-011 until clarification CR completes
- Escalate EDL-011 clarification question §4.4 (not EDL file edit in WP-009-R1)
Status remains Open.
```

## 5. Hazard-based timing ordering

Required safety intent (ADR-022) — **not assumed achievable without proof** using **compatible measurement boundaries**.

### 5.1 Normalized path segments

Do **not** compare a full end-to-end path with an internal sub-path without normalizing start/end events.

| Segment ID | Start event | End event |
|------------|-------------|-----------|
| `t_kill_input_to_global_disable` | Kill input active edge | `nENABLE_GLOBAL` inactive / global disable effective |
| `t_global_disable_to_output_safe` | Global disable effective | All outputs safe (voltage + current criteria) |
| `t_kill_input_to_output_safe` | Kill input active edge | All outputs safe |

Legacy composite (use only when boundaries explicitly defined):

```text
t_kill_total = t_kill_input_to_global_disable + t_global_disable_to_output_safe (+ uncertainty)
```

### 5.2 Ordering intent (requires proof per segment)

```text
hardware kill is the highest-urgency path;
watchdog and communication-loss paths shall not be faster merely by assumption;
all orderings require proof against common start/end definitions.
```

Target relationships (to be verified, not assumed):

```text
t_kill_input_to_output_safe  ≪  t_watchdog_expiry_to_output_safe   (class separation)
t_watchdog_expiry_to_output_safe  ≪  t_control_loss_to_output_safe   (class separation)
```

**Do not** assert `t_kill_total ≤ t_global_enable_removal` without defining whether comparing full paths or sub-segments.

### 5.3 Commanded OFF relationship

| Comparison | Recommended policy | Rationale |
|------------|-------------------|-----------|
| Commanded OFF vs watchdog | Commanded OFF **should be faster** than watchdog expiry for single-channel normal operation | Operator expects prompt OFF; watchdog is backstop |
| Commanded OFF vs control loss | Commanded OFF **should be faster** than communication-loss shutdown for same channel | Normal command path vs fail-safe |
| Commanded OFF vs kill | Kill **always faster** — kill is hardware emergency | ADR-022 class separation |

**Analysis result:** Ordering is **architecturally required** but **not yet proven** — **BLOCKED_BY_MEASUREMENT** and component/firmware dependencies.

### 5.4 Service / Tablet exclusion

Service crash and Tablet disconnect: **no position** in emergency ordering; RT power execution continues (fail-operational).

## 6. Candidate timing classes (study)

| Class | Paths | Relative order | Instrument-planning note | Primary blocker |
|-------|-------|----------------|--------------------------|-----------------|
| T-Class H | Kill, global-enable | Fastest | Scope bandwidth/sampling for sub-ms edges — **not** an architecture bound | HW path + load model + measurement |
| T-Class R | Watchdog | Slower than H | Expiry-dominated — numeric Open | WD period + FW handler |
| T-Class C | Control loss | Fail-safe class | **BLOCKED_BY_EDL_CLARIFICATION** — no numeric direction | EDL clarification + DCPI period |
| T-Class N | Commanded OFF | Normal shutdown | Per-channel OFF capture — numeric Open | FW + switch + load |

**No timing study band in this table is an Approved architecture bound.**

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

### 7.2 State rules and WP-009-R1 clarifications

| State | Entry condition | Outputs | Prohibited |
|-------|-----------------|---------|------------|
| KILL_ASSERTED | Kill active | OFF | Any enable |
| KILL_RELEASED_LOCKED | Kill deasserted | OFF | Auto-restore prior ON commands |
| OPERATOR_ACK_REQUIRED | Ack event required | OFF | Service/Tablet as **sole** re-enable authority; **reset ≠ operator acknowledgement** |
| FAULT_CLEAR_REQUIRED | Applicable faults latched | OFF | Enable with uncleared faults |
| READY_FOR_ENABLE | **Both** ack and fault-clear complete (order between ack and fault-clear may vary unless hazard analysis mandates strict ordering) | OFF | Implicit enable |
| EXPLICIT_FUNCTION_ENABLE | Per-function **new** enable commands after kill event | Per command | Stale command replay |

**Stale command invalidation:** All pre-kill function commands shall be invalidated using a **command epoch**, **generation counter**, or equivalent normative concept before any output re-energization.

**Re-enable authority:** Re-enable is **per-function** and based on **new commands issued after the kill event** — not restoration of prior command state.

**Ack / fault-clear ordering:** Acknowledgement and fault clearing may occur in either controlled order unless a hazard analysis requires strict ordering; **both** are required before `READY_FOR_ENABLE`.

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
| TBD-DK-004 | §3.1 | Open | Load + instrument | Accept budget + measurement method only | Measurement + HW |
| TBD-DK-005 | §3.2 | Open | WD period + handler | Accept budget + measurement method only | Component + FW + measurement |
| TBD-DK-007 | §3.3 / §4 | **No numeric direction** | EDL ambiguity | Accept closure method only; **BLOCKED_BY_EDL_CLARIFICATION** | EDL clarification CR + measurement |
| TBD-DK-014 | §3.4 | Open | FW + load | Accept budget + measurement method only | FW + component + measurement |
| TBD-DK-021 | §7 | Procedural | N/A | Accept deterministic procedural/state-machine contract | Architect acceptance |

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

## 11. Architecture Review acceptance (2026-07-20)

| Field | Value |
|-------|-------|
| **Status** | Accepted — Architecture Review |
| **Review date** | 2026-07-20 |
| **Approver role** | System Architect |
| **PR** | #13 merged (`6f3845e`) |

Accepted: timing budget structures, normalized path segments, measurement plan structure, TBD-DK-021 procedural contract, EDL-011 ambiguity documentation.  
Not Accepted: numeric ms limits; EDL-011 numeric direction (BLOCKED_BY_EDL_CLARIFICATION).

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial safety timing analysis |
| 1.1 | 2026-07-20 | WP-009-R1 — EDL-011 ambiguity; normalized timing segments; FSM clarifications |
| 1.2 | 2026-07-20 | Architecture Review — methods Accepted; numeric Open |
