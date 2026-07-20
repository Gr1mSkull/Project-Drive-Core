# DevKit P0 Decision Crosswalk — WP-008

**Document ID:** DOC-DK-P0-XWALK-001  
**Version:** 1.2  
**Status:** Accepted  
**Work Package:** WP-008 / WP-008-R1 (Accepted)  
**Date:** 2026-07-20

> Maps Accepted ADR-016…023 recommendations to requirements, cases, TBDs, and next Work Packages.  
> Architecture Review Accepted (2026-07-20). Evidence remains **NOT VERIFIED**. ADR-021/022 numerics remain **Open**.

## 1. Decision summary table

| Topic | ADR | Accepted decision | Requirements affected (primary) | Cases affected (primary) | TBDs affected | Next WP |
|-------|-----|----------------------------------|----------------------------------|--------------------------|---------------|---------|
| Logic fidelity | ADR-016 | Option D; Option B min for DK-A…DK-D; EDL-001 processor | 009, 011, 012, 017, 018, 102, 103 | A-007…A-017, B-006 | — (identity map later) | Electrical architecture; platform |
| Radio fidelity | ADR-017 | Option D; Option B min for DK-B/D Service/DCPI | 010, 012, 018, 102, 103 | A-005, A-009, B-006…B-015, D-012, D-013 | TBD-DK-006 (timing only) | Electrical; Radio qual; ADR-DK-008 |
| Firmware equivalence | ADR-018 | Option D lifecycle; Option B certification model | 013; DK-GOV-009/012 | A-006, A-017, D-019, G-003; Method:Test set | — | Platform/build system |
| Represented power capabilities | ADR-019 | Min capability set Option B (+ staged D); open-load CONDITIONAL_ON_DEVKIT | 005, 014, 039–055, 026 | C-001…C-014 (C-007 conditional), A-016 | Constrains 002/003/011/018/019/022 | Electrical architecture |
| Highest-current scope | ADR-020 | Option D: external discovery + Phase E confirm | 005, 014, 041 | C-001; C-005/006 scope notes | Constrains 002/003 | Fixture; Phase E plan |
| Input / simultaneous current | ADR-021 | Option B + D distinction; numerics Open | 020, 007, 030; DK-GOV-024/025 | A-002, A-003; multi-load C; G-004 | **002, 003** method; constrains 001/012/017/018/019 | Threshold analysis |
| Kill / watchdog timing | ADR-022 | Option D hierarchical fixed safety | 021, 031–038, 034, 035, 058 | A-011…A-014, C-012, B-013, D-012/013 | **004, 005, 007, 014, 021** | Threshold analysis |
| Fault injection / fixture boundary | ADR-023 | Gate-tiered Option B + method Option D; open-load CONDITIONAL_MANDATORY; supply interruption MANDATORY_DK_A + MANDATORY_DK_D | 017, 018, 023, 035, 038, 043–048, 054, 055, 058, 060, 067, 072, 073, 079, 080, 085, 087, 099, 100 (not 114) | A-003, A-008/009/011/015; B-003/008; C-005…014 (C-007 conditional); D-007/008/012…014/017 | 011, 022; energy notes | Fixture/load-bank reqs |

## 2. Dependency graph

```text
ADR-016 Logic fidelity
    → ADR-018 firmware equivalence
    → electrical architecture (Logic)
    → DK-A / DK-B readiness

ADR-017 Radio fidelity
    → ADR-018 firmware equivalence
    → electrical architecture (Radio)
    → DK-B / DK-D readiness
    → ADR-DK-008 (OTA) sequencing [not in P0 ADRs]

ADR-019 represented capabilities
    → ADR-020 highest-current scope
    → ADR-021 input-current architecture
    → fixture requirements (with ADR-023)
    → DK-C readiness

ADR-021 input current
    → WP-009 Accepted (methods); threshold numeric Open
    → functional electrical architecture WP (authorized)

ADR-022 safety timing
    → WP-009 Accepted (methods); timing numeric Open
    → EDL-011 clarification (TBD-DK-007)
    → DK-A / DK-C readiness

ADR-023 fault injection scope
    → fixture/load-bank requirements
    → DK-B / DK-C / DK-D readiness
```

## 3. Circular dependency check

| Pair | Relationship | Circular? |
|------|--------------|-----------|
| ADR-016 ↔ ADR-018 | 016 constrains whether Option A binary is possible; 018 defines build model for 016 Option B | **No cycle** — one-way constraint with documented feedback note |
| ADR-019 → ADR-020 → ADR-021 | Capability set → HC location → envelope | **No cycle** |
| ADR-021 ↔ ADR-023 | Envelope constrains fixture energy; fixture may inform envelope evidence | **Soft coupling, not a logic cycle** — threshold WP closes numbers using both |
| ADR-022 ↔ ADR-023 | Timing paths measured under fixture supervision | **Soft coupling** — policy then measurement |
| ADR-017 ↔ ADR-DK-008 | Radio fidelity vs OTA scope | **No cycle** — 008 remains open, sequenced after P0 |

No hidden circular dependencies identified. Soft couplings shall be closed by threshold/fixture WPs without re-opening P0 architecture without a superseding ADR.

## 4. Blocker state after Architecture Review acceptance (2026-07-20)

| Area | After P0 ADRs Accepted | Still blocked by |
|------|---------------------|------------------|
| Architecture direction | Architecture blocker reduced | — |
| Numeric thresholds | Methods **Accepted** (WP-009); values **Open** | EDL-011 clarification; electrical architecture; measurement |
| Electrical design start | **Authorized** — functional architecture WP | Sizing/freeze not authorized |
| Fixtures | Boundary known | Fixture WP; implementation |
| Evidence | — | Remains NOT VERIFIED |

```text
Architecture blocker resolved (Accepted)
Implementation blocker remains
Fixture blocker remains
Threshold methods resolved (Accepted); numeric values Open
Functional electrical architecture authorized
Evidence remains NOT VERIFIED
```

## 5. Out-of-package decisions (sequencing)

| Request | Topic | Proposed sequence |
|---------|-------|-------------------|
| ADR-DK-008 | OTA gate scope | After ADR-017/018 Accepted |
| ADR-DK-009 | Configuration hot-reload | After ADR-018; with config WP |
| ADR-DK-011 | Environmental/thermal split | After ADR-019/021; with threshold/thermal analysis |
| ADR-DK-012 | Connector/enclosure candidates | After electrical architecture outline |

## 6. Conflict disposition (Accepted)

```text
EDL-001 remains authoritative.
The STM32G431 DevKit-only candidate in docs/007 is not authorized for DK-A…DK-D gate evidence.
This acceptance update does not rewrite the BOM or select a component.
```

## 7. Accepted options summary

| ADR | Accepted option |
|-----|-----------------|
| ADR-016 | Option D, with Option B minimum for DK-A…DK-D |
| ADR-017 | Option D, with Option B minimum for applicable DK-B/D evidence |
| ADR-018 | staged model; Option B for certification builds |
| ADR-019 | Option B via Option D staging |
| ADR-020 | Option D |
| ADR-021 | Option B + Option D envelope model |
| ADR-022 | Option D using Option B timing classes |
| ADR-023 | Option B scope using Option D injection-method rules |

## 8. WP-010 functional electrical architecture mapping

| ADR | Architecture artifact | Status |
|-----|----------------------|--------|
| ADR-016 | Logic domain — [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md) §3.1 | Proposed |
| ADR-017 | Radio domain — §3.2 | Proposed |
| ADR-019 | Representative channels — [`DevKit_Representative_Channel_Allocation.md`](DevKit_Representative_Channel_Allocation.md) | Proposed |
| ADR-020 | External bank — §16; CH-HC-EXTERNAL | Proposed |
| ADR-021 | Input chain — §5, §11 | Proposed |
| ADR-022 | Safe-state paths — [`DevKit_Safe_State_Path_Matrix.md`](DevKit_Safe_State_Path_Matrix.md) | Proposed |
| ADR-023 | Fault containment — §18 | Accepted |

**Next authorized work:** Component-class qualification execution · electrical sizing · fixture requirements.

**Not authorized by WP-011:** MPN selection · BOM · schematics · PCB · numeric threshold approval · EDL file edit. `TBD-DK-007` remains **BLOCKED_BY_EDL_CLARIFICATION** (not Resolved).

## 9. WP-011 EDL-011 + component-class preparation mapping

| Artifact | Document | Status |
|----------|----------|--------|
| EDL-011 interpretation (Option D) | [`DevKit_EDL011_Clarification_Proposal.md`](DevKit_EDL011_Clarification_Proposal.md) | Accepted |
| Component-class qualification framework | [`DevKit_Component_Class_Qualification_Framework.md`](DevKit_Component_Class_Qualification_Framework.md) | Accepted |
| Evaluation-class matrix | [`DevKit_Component_Class_Matrix.md`](DevKit_Component_Class_Matrix.md) | Accepted |
| Electrical design input register | [`DevKit_Electrical_Design_Input_Register.md`](DevKit_Electrical_Design_Input_Register.md) | Accepted |

## 10. WP-012 electrical sizing architecture framework mapping

| Artifact | Document | Status |
|----------|----------|--------|
| Electrical sizing framework | [`DevKit_Electrical_Sizing_Framework.md`](DevKit_Electrical_Sizing_Framework.md) | **Accepted** |
| Current and power budget model | [`DevKit_Current_and_Power_Budget_Model.md`](DevKit_Current_and_Power_Budget_Model.md) | **Accepted** |
| Thermal sizing framework | [`DevKit_Thermal_Sizing_Framework.md`](DevKit_Thermal_Sizing_Framework.md) | **Accepted** |
| Protection coordination framework | [`DevKit_Protection_Coordination_Framework.md`](DevKit_Protection_Coordination_Framework.md) | **Accepted** |
| Power-path assumption register | [`DevKit_Power_Path_Assumption_Register.md`](DevKit_Power_Path_Assumption_Register.md) | **Accepted** |
| Sizing dependency and closure matrix | [`DevKit_Sizing_Dependency_and_Closure_Matrix.md`](DevKit_Sizing_Dependency_and_Closure_Matrix.md) | **Accepted** |

**Next authorized work (after WP-012 acceptance):** Component-class qualification · symbolic preliminary calculation · fixture requirements — **WP-013 Proposed**.

**Not authorized by WP-012:** MPN selection · numeric freeze · schematic · PCB · fixture build. `TBD-DK-007` remains **BLOCKED_BY_EDL_CLARIFICATION**.

## 11. WP-013 component-class qualification mapping

| Artifact | Document | Status |
|----------|----------|--------|
| Qualification report | [`DevKit_Component_Class_Qualification_Report.md`](DevKit_Component_Class_Qualification_Report.md) | **Accepted** (methodology) |
| High-side comparison | [`DevKit_High_Side_Class_Comparison.md`](DevKit_High_Side_Class_Comparison.md) | **Accepted** (evaluation) |
| Current-observation comparison | [`DevKit_Current_Observation_Class_Comparison.md`](DevKit_Current_Observation_Class_Comparison.md) | **Accepted** (evaluation) |
| Protection comparison | [`DevKit_Protection_Class_Comparison.md`](DevKit_Protection_Class_Comparison.md) | **Accepted** (evaluation) |
| Bidirectional comparison | [`DevKit_Bidirectional_Class_Comparison.md`](DevKit_Bidirectional_Class_Comparison.md) | **Accepted** (evaluation) |
| Symbolic preliminary calculations | [`DevKit_Symbolic_Preliminary_Calculations.md`](DevKit_Symbolic_Preliminary_Calculations.md) | **Accepted** (methodology) |
| Class recommendation matrix | [`DevKit_Class_Recommendation_and_Readiness_Matrix.md`](DevKit_Class_Recommendation_and_Readiness_Matrix.md) | **Accepted** (directions); final classes Open |

**Not authorized by WP-013:** MPN selection · manufacturer preference · BOM · numeric freeze · schematic · PCB · VE.

## 12. WP-014 fixture and load-bank requirements mapping

| Artifact | Document | Status |
|----------|----------|--------|
| Fixture requirements | [`DevKit_Fixture_and_Load_Bank_Requirements.md`](DevKit_Fixture_and_Load_Bank_Requirements.md) | **Proposed** |
| Functional architecture | [`DevKit_Fixture_Functional_Architecture.md`](DevKit_Fixture_Functional_Architecture.md) | **Proposed** |
| Energy/safety boundary | [`DevKit_Fixture_Energy_and_Safety_Boundary.md`](DevKit_Fixture_Energy_and_Safety_Boundary.md) | **Proposed** |
| Load/fault catalog | [`DevKit_Load_and_Fault_Profile_Catalog.md`](DevKit_Load_and_Fault_Profile_Catalog.md) | **Proposed** |
| Interface/measurement | [`DevKit_Fixture_Interface_and_Measurement_Register.md`](DevKit_Fixture_Interface_and_Measurement_Register.md) | **Proposed** |
| Verification capability | [`DevKit_Fixture_Verification_Capability_Matrix.md`](DevKit_Fixture_Verification_Capability_Matrix.md) | **Proposed** |
| Hazard/interlock | [`DevKit_Fixture_Hazard_and_Interlock_Register.md`](DevKit_Fixture_Hazard_and_Interlock_Register.md) | **Proposed** |
| Dependency/readiness | [`DevKit_Fixture_Dependency_and_Readiness_Matrix.md`](DevKit_Fixture_Dependency_and_Readiness_Matrix.md) | **Proposed** |

**ADR-023 / ADR-020 fixture consumers:** fault-injection authority, external envelope separation, and evidence scopes map to REQ-DCC-V-FX-* (Proposed).

**Not authorized by WP-014:** fixture MPN · BOM · ratings · schematics · PCB · harness · procurement · construction · energization · VE · numeric freeze.

## 13. Related records

| Record | Path |
|--------|------|
| CIA (WP-008) | [`docs/records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md`](../records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md) |
| RHP (WP-008) | [`docs/records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md`](../records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md) |
| CIA (WP-014) | [`docs/records/change_impact/CIA-2026-009_wp014-fixture-load-bank-requirements.md`](../records/change_impact/CIA-2026-009_wp014-fixture-load-bank-requirements.md) |
| RHP (WP-014) | [`docs/records/review_handoffs/RHP-2026-008_wp014-fixture-load-bank-requirements.md`](../records/review_handoffs/RHP-2026-008_wp014-fixture-load-bank-requirements.md) |
| ADR index | [`docs/ADR/README.md`](../ADR/README.md) |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-008 initial crosswalk |
| 1.1 | 2026-07-20 | WP-008-R1 — open-load conditional; ADR-023 REQs without 114; supply interruption DK-A/DK-D |
| 1.2 | 2026-07-20 | Architecture Review — ADR-016…023 Accepted; WP-008 Accepted |
| 1.3 | 2026-07-20 | Acceptance metadata alignment — conflict disposition; accepted-options summary |
| 1.4 | 2026-07-20 | WP-009 — threshold analysis dependency on ADR-021/022 |
| 1.5 | 2026-07-20 | WP-009 Architecture Review — methods Accepted; functional electrical architecture authorized |
| 1.6 | 2026-07-20 | WP-010 — functional electrical architecture Proposed; ADR-019/020/021 architecture refs |
| 1.7 | 2026-07-20 | WP-010 Architecture Review — functional electrical architecture Accepted |
| 1.8 | 2026-07-20 | WP-011 Architecture Review — EDL-011 + component-class prep Accepted; TBD-DK-007 BLOCKED retained |
| 1.9 | 2026-07-20 | WP-012 — electrical sizing architecture framework (Proposed) |
| 1.10 | 2026-07-20 | WP-012 Accepted status alignment; WP-013 class qualification mapping (Proposed) |
| 1.11 | 2026-07-20 | WP-013 Accepted status; WP-014 fixture/load-bank mapping (Proposed) |
| 1.12 | 2026-07-20 | WP-015 fixture preliminary design mapping (Proposed) |

## 13. WP-015 fixture preliminary design mapping

WP-015 converts Accepted `REQ-DCC-V-FX-*` into a preliminary design architecture (`FX-*` modules, `FX-PD-001…017`). ADR-020/021/022/023 remain the accepted authority; WP-015 selects no topology, MPN, numeric, ground/reference, or E-stop circuit. OI-GND-001 / OI-PROT-001/002 / OI-SC-001 / OI-FIX-002 / OI-BI-001 / OI-SENSE-001 remain Open (options compared, not selected). **Not authorized by WP-015:** detailed design · schematic · PCB · harness · BOM · MPN · numeric freeze · procurement · construction · energization · VE.

| Artifact | Document | Status |
|----------|----------|--------|
| Preliminary design anchor | [`DevKit_Fixture_Preliminary_Design_Architecture.md`](DevKit_Fixture_Preliminary_Design_Architecture.md) | Proposed |
| Decision register | [`DevKit_Fixture_Preliminary_Design_Decision_Register.md`](DevKit_Fixture_Preliminary_Design_Decision_Register.md) | Proposed |
| Implementation readiness | [`DevKit_Fixture_Implementation_Readiness_Matrix.md`](DevKit_Fixture_Implementation_Readiness_Matrix.md) | Proposed |
