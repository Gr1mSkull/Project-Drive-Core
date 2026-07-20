# DriveCore Gen1 DevKit — Document Set

**Document ID:** DOC-DK-INDEX-001  
**Version:** 1.12  
**Status:** Accepted (index); WP-012 **Proposed**  
**Work Package:** WP-007 / WP-008 (Accepted) / WP-009 (Accepted) / WP-010 (Accepted) / WP-011 (Accepted) / WP-012 (Proposed)  
**Date:** 2026-07-20

```text
The DevKit is a controlled verification platform.
It is not a reduced production DCC and not a substitute for DCC Gen1 acceptance.
```

## Purpose

This folder holds the **verification-ready Gen1 DevKit requirements baseline**, interface matrix, verification plan, and current-state gap assessment produced by WP-007.

It defines **what the DevKit must accomplish and how it will be verified**.  
It does **not** define the final circuit, PCB, component set, enclosure, or BOM.

## Document map

| Document | Authority role | Status |
|----------|----------------|--------|
| [DevKit_System_Requirements.md](DevKit_System_Requirements.md) | Normative **system** requirements (`REQ-DCC-V-DK-NNN`) | Accepted |
| [DevKit_Verification_Governance.md](DevKit_Verification_Governance.md) | Evidence/claim/gate process rules (`DK-GOV-NNN`) | Accepted |
| [DevKit_Interface_Matrix.md](DevKit_Interface_Matrix.md) | Interface boundaries and testability | Accepted |
| [DevKit_Verification_Plan.md](DevKit_Verification_Plan.md) | Phase A–D + governance inspection; gates DK-A…DK-D | Accepted |
| [DevKit_Current_State_Gap_Assessment.md](DevKit_Current_State_Gap_Assessment.md) | Audit of existing claims vs baseline | Accepted |
| [DevKit_P0_Decision_Crosswalk.md](DevKit_P0_Decision_Crosswalk.md) | WP-008 P0 Accepted ADR-016…023 crosswalk | Accepted |
| [DevKit_Current_Envelope_Analysis.md](DevKit_Current_Envelope_Analysis.md) | WP-009 current limit stack, profiles P0–P6, scenarios C1–C3 | Accepted |
| [DevKit_Safety_Timing_Analysis.md](DevKit_Safety_Timing_Analysis.md) | WP-009 timing budgets, EDL-011 interpretation, re-enable FSM | Accepted |
| [DevKit_Threshold_Closure_Matrix.md](DevKit_Threshold_Closure_Matrix.md) | WP-009 TBD disposition and blockers | Accepted |
| [DevKit_Threshold_Measurement_Plan.md](DevKit_Threshold_Measurement_Plan.md) | WP-009 measurement plan (not evidence) | Accepted |
| [DevKit_Functional_Electrical_Architecture.md](DevKit_Functional_Electrical_Architecture.md) | WP-010 functional domains, views, fault containment | Accepted |
| [DevKit_Functional_Block_Diagram.md](DevKit_Functional_Block_Diagram.md) | WP-010 energy/control/safety diagrams | Accepted |
| [DevKit_Power_Domain_Matrix.md](DevKit_Power_Domain_Matrix.md) | WP-010 power domains and symbolic rails | Accepted |
| [DevKit_Safe_State_Path_Matrix.md](DevKit_Safe_State_Path_Matrix.md) | WP-010 independent safe-state paths | Accepted |
| [DevKit_Representative_Channel_Allocation.md](DevKit_Representative_Channel_Allocation.md) | WP-010 functional channel aliases (ADR-019) | Accepted |
| [DevKit_Measurement_Point_Register.md](DevKit_Measurement_Point_Register.md) | WP-010 measurement points (MP-*) | Accepted |
| [DevKit_Electrical_Interface_Register.md](DevKit_Electrical_Interface_Register.md) | WP-010 interface register (IF-DK-*) | Accepted |
| [DevKit_Electrical_Architecture_Open_Issues.md](DevKit_Electrical_Architecture_Open_Issues.md) | WP-010 open issues and downstream WPs | Accepted |
| [DevKit_EDL011_Clarification_Proposal.md](DevKit_EDL011_Clarification_Proposal.md) | WP-011 EDL-011 interpretation proposal (EDL unchanged) | Accepted |
| [DevKit_Component_Class_Qualification_Framework.md](DevKit_Component_Class_Qualification_Framework.md) | WP-011 component-class qualification criteria | Accepted |
| [DevKit_Component_Class_Matrix.md](DevKit_Component_Class_Matrix.md) | WP-011 evaluation component classes (no MPN) | Accepted |
| [DevKit_Electrical_Design_Input_Register.md](DevKit_Electrical_Design_Input_Register.md) | WP-011 electrical design inputs (ED-IN-*) | Accepted |
| [DevKit_Electrical_Sizing_Framework.md](DevKit_Electrical_Sizing_Framework.md) | WP-012 sizing lifecycle, domains, readiness states | Proposed |
| [DevKit_Current_and_Power_Budget_Model.md](DevKit_Current_and_Power_Budget_Model.md) | WP-012 current/power quantities and P0–P6 integration | Proposed |
| [DevKit_Thermal_Sizing_Framework.md](DevKit_Thermal_Sizing_Framework.md) | WP-012 thermal methodology | Proposed |
| [DevKit_Protection_Coordination_Framework.md](DevKit_Protection_Coordination_Framework.md) | WP-012 protection layers P0–P5 and fault classes | Proposed |
| [DevKit_Power_Path_Assumption_Register.md](DevKit_Power_Path_Assumption_Register.md) | WP-012 PWR-A assumptions and constraints | Proposed |
| [DevKit_Sizing_Dependency_and_Closure_Matrix.md](DevKit_Sizing_Dependency_and_Closure_Matrix.md) | WP-012 sizing blockers and closure | Proposed |
| This README | Navigation and authority statement | Accepted |

## Relationship to EDL-014

**EDL-014** (Accepted): DCC Gen1 shall not be installed in the vehicle until Phase A–D are passed on DevKit and Phase E critical items are passed on full DCC Gen1.

WP-007 normalizes Phase A–D into gates **DK-A…DK-D**. Passing those gates:

* supports readiness for DCC Gen1 hardware/firmware progression;
* does **not** authorize vehicle installation;
* does **not** replace Phase E evidence.

## Relationship to DCC Gen1

| Topic | Statement |
|-------|-----------|
| Architecture family | Same three-board DCC concept (Logic + Power + Radio) — EDL-007 |
| Production fidelity | Exact “identical board / same binary” rules: **Accepted** ADR-016…018 (originating ADR-DK-001…003) |
| Power domain | Representative capability for laboratory verification; not full production channel population by default |
| Acceptance | DevKit ≠ DCC Gen1 product acceptance |

## Relationship to `docs/008`

`docs/008_Testing_and_Validation.md` remains the **system-level validation strategy** (Phase A–F overview) and navigates here for detailed DevKit requirements and Phase A–D verification cases.

After WP-007, `docs/008` is **not** a competing normative source for detailed DevKit test cases.

## Relationship to ADR-015 / STD-REV-001

Every DevKit gate evidence package shall record a **composite system baseline** per Approved `STD-REV-001` (ADR-015 Accepted). Incomplete applicable identity ⇒ gate outcome `BLOCKED` or `NOT ASSESSED` (not `PASS`).

## Related records

| Record | Path |
|--------|------|
| CIA (WP-007) | [`docs/records/change_impact/CIA-2026-002_wp007-devkit-requirements.md`](../records/change_impact/CIA-2026-002_wp007-devkit-requirements.md) |
| CIA (WP-008) | [`docs/records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md`](../records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md) |
| Review Handoff (WP-007) | [`docs/records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md`](../records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md) |
| CIA (WP-009) | [`docs/records/change_impact/CIA-2026-004_wp009-devkit-threshold-analysis.md`](../records/change_impact/CIA-2026-004_wp009-devkit-threshold-analysis.md) |
| Review Handoff (WP-009) | [`docs/records/review_handoffs/RHP-2026-003_wp009-devkit-threshold-analysis.md`](../records/review_handoffs/RHP-2026-003_wp009-devkit-threshold-analysis.md) |
| CIA (WP-010) | [`docs/records/change_impact/CIA-2026-005_wp010-devkit-functional-electrical-architecture.md`](../records/change_impact/CIA-2026-005_wp010-devkit-functional-electrical-architecture.md) |
| Review Handoff (WP-010) | [`docs/records/review_handoffs/RHP-2026-004_wp010-devkit-functional-electrical-architecture.md`](../records/review_handoffs/RHP-2026-004_wp010-devkit-functional-electrical-architecture.md) |
| CIA (WP-011) | [`docs/records/change_impact/CIA-2026-006_wp011-edl011-component-class.md`](../records/change_impact/CIA-2026-006_wp011-edl011-component-class.md) |
| Review Handoff (WP-011) | [`docs/records/review_handoffs/RHP-2026-005_wp011-edl011-component-class.md`](../records/review_handoffs/RHP-2026-005_wp011-edl011-component-class.md) |
| CIA (WP-012) | [`docs/records/change_impact/CIA-2026-007_wp012-electrical-sizing-framework.md`](../records/change_impact/CIA-2026-007_wp012-electrical-sizing-framework.md) |
| Review Handoff (WP-012) | [`docs/records/review_handoffs/RHP-2026-006_wp012-electrical-sizing-framework.md`](../records/review_handoffs/RHP-2026-006_wp012-electrical-sizing-framework.md) |
| P0 ADR package | [`docs/ADR/README.md`](../ADR/README.md) — ADR-016…023 **Accepted** |
| Traceability | [`docs/traceability/TRACEABILITY_MATRIX.md`](../traceability/TRACEABILITY_MATRIX.md) |
| SRS pointer | [`docs/SRS/Volume_2_DCC.md`](../SRS/Volume_2_DCC.md) §8.1 |

## Current status

| Item | Status |
|------|--------|
| Requirements baseline | **Accepted** — Architecture Review (2026-07-20); verification evidence still NOT VERIFIED |
| Governance rules | **Accepted** (`DK-GOV-*`) |
| Verification plan | **Accepted** (structure) — cases NOT EXECUTED / BLOCKED; no PASS claims |
| P0 ADRs ADR-016…023 | **Accepted** (WP-008; ADR-021/022 numerics Open) |
| WP-009 threshold analysis | **Accepted** (2026-07-20) — methods Accepted; numeric values **Open** |
| WP-010 functional electrical architecture | **Accepted** (2026-07-20) — WP-010-R1 Accepted |
| WP-011 EDL-011 + component-class prep | **Accepted** (2026-07-20) — WP-011-R1 Accepted |
| WP-012 electrical sizing architecture framework | **Proposed** — Architecture Review pending |
| Hardware design | **NOT IMPLEMENTED** — detailed sizing/schematic/PCB **NOT AUTHORIZED** |
| Firmware bring-up | NOT IMPLEMENTED |
| Physical verification | NOT VERIFIED |
| Filled VE records | None |

## Known blocking decisions

P0 ADRs ADR-016…023 (ADR-DK-001…007, 010) are **Accepted** (WP-008 Architecture Review 2026-07-20). ADR-021/022 numeric limits remain **Open**.

Still open decision **requests** (no Accepted ADR yet): `ADR-DK-008`, `ADR-DK-009`, `ADR-DK-011`, `ADR-DK-012`.

Open thresholds: `TBD-DK-001` … `TBD-DK-022` (Status Open — WP-009 methods Accepted; numeric values not Approved). `TBD-DK-007` remains **BLOCKED_BY_EDL_CLARIFICATION** — not Resolved.

**Next step:** Architecture Review of WP-012 (electrical sizing architecture framework).

**Not authorized:** MPN selection · BOM · schematics · PCB · numeric threshold approval · EDL file edit · final electrical sizing completion.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 DevKit document set |
| 1.1 | 2026-07-19 | WP-007-R1 — governance document; taxonomy/gate corrections |
| 1.1.1 | 2026-07-19 | WP-007-R1 — identity gate language aligned (no PARTIAL PASS) |
| 1.2 | 2026-07-20 | Architecture Review — ACCEPTED; PR #11 approved for merge (requirements structure, governance, verification-plan structure, traceability baseline) |
| 1.3 | 2026-07-20 | WP-008 — P0 Proposed ADR package navigation (ADR-016…023); CIA-2026-003 / RHP-2026-002 |
| 1.4 | 2026-07-20 | Architecture Review — ADR-016…023 Accepted; WP-008 Accepted; PR #12 approved for merge |
| 1.5 | 2026-07-20 | WP-009 — threshold analysis package navigation; CIA-2026-004 / RHP-2026-003 |
| 1.6 | 2026-07-20 | WP-009 Architecture Review — analysis package Accepted; functional electrical architecture authorized |
| 1.7 | 2026-07-20 | WP-010 — functional electrical architecture package (Proposed) |
| 1.8 | 2026-07-20 | WP-010 Architecture Review — functional electrical architecture Accepted; WP-011 authorized |
| 1.9 | 2026-07-20 | WP-011 — EDL-011 clarification proposal + component-class qualification prep (Proposed) |
| 1.10 | 2026-07-20 | WP-011-R1 — review corrections; Ready for Final Architecture Review |
| 1.11 | 2026-07-20 | Architecture Review — WP-011 Accepted; PR #15 merged (`07c550c`); TBD-DK-007 BLOCKED unchanged |
| 1.12 | 2026-07-20 | WP-012 — electrical sizing architecture framework (Proposed) |
