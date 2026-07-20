# Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-2026-004 |
| **Impact Level** | 2 — Full CIA |
| **Title** | WP-009 Gen1 DevKit Current Envelope and Safety Timing Threshold Analysis |
| **Author** | Implementation Engineer (cloud agent) |
| **Author role** | Implementation Engineer |
| **Date** | 2026-07-20 |
| **Status** | Draft — Under Architecture Review |
| **Related WP / CR** | WP-009 / WP-009-R1; depends on WP-008 Accepted (`8bc5710`+); ADR-021/022 Accepted |

### Reason for Change

Accepted ADR-021 and ADR-022 established current-envelope and timing **architecture** but left numeric thresholds Open (`TBD-DK-002`, `003`, `004`, `005`, `007`, `014`, `021`). DK-A and DK-C gates remain blocked for numeric freeze claims. Threshold analysis is required before electrical architecture sizing and verification execution.

### Current Behaviour

* WP-008 Accepted; ADR-016…023 Accepted; TBD-DK-001…022 **Open**.
* Candidate 30 A, 13.8 V, >100 ms, <200 ms values exist in docs/008 and register as **CANDIDATE** only.
* No threshold analysis package; no measurement plan; no closure matrix.
* Verification evidence **NOT VERIFIED**; cases **NOT EXECUTED / BLOCKED**.

### Proposed Behaviour

* Four analysis documents: current envelope, safety timing, closure matrix, measurement plan.
* Proposed Threshold Decision Records embedded in analysis (not Approved).
* TBD register §4 updated with analysis references, closure methods, readiness — **Status remains Open**.
* Traceability and DevKit indexes gain WP-009 navigation.
* **No** numeric threshold Approved; **no** VE records; **no** hardware/firmware/PCB work.

### Affected Requirements

| Requirement ID | Source | Impact |
|----------------|--------|--------|
| REQ-DCC-V-DK-020 | DevKit_System_Requirements | TBD-DK-002 analysis reference; NOT VERIFIED unchanged |
| REQ-DCC-V-DK-021, 031–038 | DevKit_System_Requirements | Timing TBDs analyzed; NOT VERIFIED unchanged |
| REQ-DCC-V-DK-035, 036, 037, 038 | DevKit_System_Requirements | TBD-DK-004/005/007/014 budgets |
| REQ-DCC-V-DK-044, 045, 049, 058 | DevKit_System_Requirements | Current/fault interaction notes |
| DK-GOV-024, 025 | Verification_Governance | Freeze rules informed by analysis |
| EDL-011 | docs/EDL | Interpretation documented; **file unchanged** |

### Affected Modules

Documentation / threshold analysis only. No firmware, hardware, tools, or config schema changes.

### Affected Interfaces

| Interface | Current version | Proposed version | Breaking? |
|-----------|-----------------|------------------|-----------|
| J_LP / DCPI / DCP | Accepted | Unchanged | NO |
| DevKit threshold register | Open TBDs | Open + analysis refs | NO |

### Affected Files

Created: `DevKit_Current_Envelope_Analysis.md`, `DevKit_Safety_Timing_Analysis.md`, `DevKit_Threshold_Closure_Matrix.md`, `DevKit_Threshold_Measurement_Plan.md`; this CIA; RHP-2026-003.  
Modified: TBD register §4; DevKit README; gap assessment; crosswalk; verification plan notes; roadmap; traceability; `.ai/current_phase.md`; root README.

### Affected Tests

No test execution. Measurement **plans** defined; cases remain NOT EXECUTED / BLOCKED. No PASS.

### Affected Documentation

DevKit set, traceability, roadmap, agent phase file.

### Compatibility Assessment

| Aspect | Assessment |
|--------|------------|
| Backward compatibility | Compatible — no runtime change |
| Forward compatibility | Compatible — enables electrical architecture WP with bounds |
| Silent field reinterpretation risk | None — Open status explicit |

### Migration Requirements

After Architect threshold acceptance: update TBD register values via controlled CR; electrical architecture WP consumes Scenario C2 recommendation.

### Rollback Method

Revert WP-009 PR; WP-008 baseline unchanged.

### Safety Impact

| Area | Impact |
|------|--------|
| Safe states | Analysis proposes kill/re-enable procedure — not implemented |
| Kill / isolation | Budget models — numerics Open |
| Fail-operational behaviour | Unchanged — Service/Tablet excluded from kill ordering |

### Validation Required

WP-009 §30 documentation validation; Architecture Review of proposed thresholds; **no** physical validation in this WP.

### Open Questions

* Architect accept Scenario **C2 calculation architecture** (no ampere ceiling from WP-009)?
* Accept TBD-DK-003 profile/overlap closure model?
* Accept TBD-DK-021 state-machine + command epoch procedure?
* Authorize EDL-011 clarification CR with question A/B/C/D?
* Decompose TBD-DK-002 register in follow-on CR?

### WP-009-R1 Lightweight Impact Note (Level 1)

| Correction | Change |
|------------|--------|
| EDL-011 interpretation | Removed unsupported `>100 ms` lower bound; TBD-DK-007 → **BLOCKED_BY_EDL_CLARIFICATION** |
| Current scenarios | Removed 3–8 / 8–15 / 15–25 A bands; symbolic C1–C3 only |
| Simultaneous load | Removed invalid `ΣD_n ≤ 1`; added instantaneous/avg/RMS + overlap table |
| Post-kill FSM | Command epoch; ack ≠ reset; flexible ack/fault-clear order |
| Timing ordering | Normalized path segments; no unqualified cross-path comparisons |

### Approvals (architecture / policy)

| Field | Value |
|-------|-------|
| **ADR Required** | NO — analysis under Accepted ADR-021/022 |
| **Architect Approval Required** | YES — for threshold values/procedures |
| **ADR / EDL reference** | ADR-021, ADR-022 Accepted; EDL-011 unchanged |
| **Architect approver (name/agent)** | TBD |
| **Architect role** | System Architect |
| **Architect approval date** | TBD |

### Review acknowledgment (not architecture approval)

| Field | Value |
|-------|-------|
| **Reviewer (name/agent)** | TBD |
| **Reviewer role** | Independent Reviewer |
| **Review date** | TBD |
| **Evidence / CIA review note** | TBD |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial CIA |
| 1.1 | 2026-07-20 | WP-009-R1 Level 1 corrections — EDL ambiguity; symbolic scenarios; profile model |
