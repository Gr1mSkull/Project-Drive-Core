# Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-2026-008 |
| **Impact Level** | 2 — Full CIA |
| **Title** | WP-013 Gen1 DevKit Component-Class Qualification and Symbolic Preliminary Calculations |
| **Author** | Implementation Engineer (cloud agent) |
| **Author role** | Implementation Engineer |
| **Date** | 2026-07-20 |
| **Status** | Draft — Under Architecture Review |
| **Related WP / CR** | WP-013; depends on WP-012 Accepted (`fe700d4` / `653264d`+); WP-011 Accepted; ADR-016…023 Accepted |

### Reason for Change

WP-011 defined evaluation classes and qualification criteria; WP-012 defined sizing methodology. No class-level comparison, conditional recommendations, or symbolic preliminary calculation package existed to guide Architect decisions before MPN qualification, fixture requirements, or provisional numeric baseline work.

### Current Behaviour

* Evaluation classes listed (WP-011) without comparative recommendation matrix.
* Sizing methods Accepted (WP-012) without class-tied symbolic preliminary calculation readiness.
* OI-COMP-001/002, OI-SENSE-001, OI-PROT-001/002, OI-BI-001 remain open without structured class options.
* ED-IN-030/031/032 open without IE recommendations.

### Proposed Behaviour

* Class comparisons for high-side, current-observation, protection, and bidirectional domains.
* Controller-interface assessment preserving hardwired KILL.
* Symbolic preliminary calculations under WP-012 sign convention.
* Class recommendation and readiness matrix (Proposed — not Accepted).
* Explicit blockers for provisional baseline, MPN qual, fixture, schematic, PCB.

### Scope exclusions (mandatory)

```text
No MPN selected.
No manufacturer recommended.
No BOM created.
No numeric threshold approved.
No schematic or PCB authorized.
No physical verification performed.
```

### Affected architecture classes

HS-INT-DIAG, HS-INT-BASIC, HS-GATE-DISCRETE, HS-HYBRID, HS-ARRAY; SENSE-*; RP-*; TRANSIENT-*; INPUT-*; CH-*-PROTECTION; BI-*; CTRL-*.

### Affected Requirements

| Requirement ID | Impact |
|----------------|--------|
| REQ-DCC-V-DK-039…055, 042, 043 | Class methodology references — NOT VERIFIED unchanged |
| DK-GOV-009, 024, 025 | Qualification discipline alignment |
| TBD-DK-001…022 | Remain Open |
| TBD-DK-007 | BLOCKED_BY_EDL_CLARIFICATION retained |
| VER-DCC-DK-* | NOT EXECUTED / BLOCKED unchanged |

### Affected Interfaces

| Interface | Impact |
|-----------|--------|
| IF-DK-* | Unchanged definitions; future class mapping Proposed |
| J_LP / KILL / nENABLE_GLOBAL | Authority boundaries preserved; CTRL class recommendations Proposed |

### Affected future design stages

MPN qualification · fixture/load-bank · provisional numeric baseline · schematic partitioning · PCB thermal · protection coordination calculations · firmware BSP (later) — **none authorized by this CIA alone**.

### Safety Impact

| Area | Impact |
|------|--------|
| Physical KILL | Preserved hardwired — no SPI-owned KILL |
| Protection layers P0–P5 | Remain distinct |
| Numeric thresholds | All Open |
| Safe states | Methodology only |

### Traceability Impact

Navigation and matrix notes only; no requirement Verified; no VE.

### Rejected assumptions

* Class recommendation = MPN selection  
* Fuse nominal = continuous certification  
* Software OFF = hardware protection  
* PSU limit = sole protection  
* LS shunt as primary HS observation  
* Indirect sense as sole verification observation  
* Relay reversing as primary CH-BI-REP  
* Historical part numbers as candidates  
* Cross-boundary current summation  
* Double-count of regen in `I_CH_IN` and `I_STORAGE_NET`

### Rollback Method

Revert WP-013 PR; WP-012 Accepted baseline preserved.

### Unresolved decisions

OI-PROT-001/002 · OI-COMP-001/002 · OI-SENSE-001 · OI-BI-001 · ADR-DK-011/012 · TBD-DK-007 numeric · Architect class acceptances (RHP questions).

### Validation Required

Architecture Review of WP-013 package. No physical tests. No VE.

### Approvals (architecture / policy)

| Field | Value |
|-------|-------|
| **ADR Required** | NO (class recommendations may drive future ADR-DK resolution) |
| **Architect Approval Required** | YES |
| **Architect approver** | TBD |
| **Architect approval date** | TBD |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial CIA — Draft |
