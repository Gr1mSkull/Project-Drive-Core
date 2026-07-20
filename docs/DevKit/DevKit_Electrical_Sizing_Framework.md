# DevKit Electrical Sizing Framework — WP-012

**Document ID:** DOC-DK-ESF-001  
**Version:** 1.3  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer

```text
Sizing ARCHITECTURE FRAMEWORK only — no numeric current, voltage, power, temperature or timing Approved.
No component selection · no schematic · no PCB · no BOM · no VE records.
```

## 1. Purpose

Define the controlled engineering flow, sizing domains, readiness states, and review gates for future DevKit electrical sizing. Converts Accepted WP-007…WP-011 baseline into a methodology package — **not** final electrical sizing.

**Authority hierarchy:** Engineering Constitution → Accepted EDL → Accepted ADR-016…023 → Accepted WP-007 governance → Accepted WP-009 methods → Accepted WP-010 functional architecture → Accepted WP-011 qualification methodology → **this Proposed framework** → historical/candidate sources (`docs/002`, `docs/008`, yaml).

## 2. Staged and iterative closure model

WP-012 defines a **staged, iterative** sizing process — not a single linear pipeline. Stages may repeat until closure criteria are met. WP-012-R1 does **not** approve any numeric value.

### 2.1 Mandatory value-state separation

These states are **not equivalent** and shall not be collapsed:

```text
Provisional numeric design input
Architect-approved design baseline
Candidate calculation
Verified physical value
Certified threshold
Verification evidence
```

| State | Meaning | Who may set | WP-012-R1 status |
|-------|---------|-------------|------------------|
| **Provisional numeric design input** | Working number for calculation exploration; labelled provisional | Architect authorization only (future WP) | **Not approved in WP-012-R1** |
| **Architect-approved design baseline** | Controlled baseline permitting qualification / schematic / PCB prep | System Architect acceptance record | **Permitted future state** — not created here |
| **Candidate calculation** | Output of symbolic or provisional-input calculation; labelled candidate | Implementation Engineer | Method only — no numeric Approved |
| **Verified physical value** | Measured on instrumented DUT under declared profile | Test Engineer + VE path | NOT VERIFIED |
| **Certified threshold** | Architect-frozen TBD-DK-* or design limit | System Architect | All Open |
| **Verification evidence** | Certified VE record | Test Engineer | No VE in WP-012 |

**Future authorization:** An Architect may accept a **provisional design baseline** before component qualification, schematic capture, and PCB layout — provided it is explicitly labelled provisional, traceable, and distinct from certified threshold. WP-012 defines the methodology only.

### 2.2 Closure stages (iterative)

```text
[A] Symbolic architecture
      ↕ iterate
[B] Provisional numeric design input (Architect — future)
      ↕ iterate
[C] Candidate calculation
      ↕ iterate with qualification / protection / thermal
[D] Component qualification · protection coordination · thermal evaluation
      ↕ iterate — may return to [B]/[C] when inputs change
[E] Schematic · PCB (NOT AUTHORIZED until Architect provisional baseline + gates)
      ↕ iterate with measurement feedback
[F] Physical measurement
      ↕
[G] Certified threshold acceptance (Architect)
      ↕
[H] Verification evidence (VE)
```

Supporting tracks (parallel, any stage): operating profiles P0–P6 · ED-IN dependencies · evaluation-class comparison · fixture definition.

### 2.3 Stage governance

| Stage | Required inputs | Permitted outputs | Responsible role | Review authority | Evidence required | Downstream dependency | Prohibited claims |
|-------|-----------------|-------------------|------------------|------------------|-------------------|----------------------|-------------------|
| [A] Symbolic architecture | Accepted REQ; WP-009…011 | Methods; symbolic constraints | Implementation Engineer | Architect | WP-012 package | Provisional input prep | Numeric Approved |
| [B] Provisional numeric input | Closed symbolic model; Architect authorization | **Provisional** labelled inputs | System Architect | Architect | Acceptance record | Candidate calc | Certified threshold |
| [C] Candidate calculation | Provisional or symbolic inputs | **Candidate** labelled results | Implementation Engineer | Architect | Calculation record | Qualification | Numeric freeze |
| [D] Qualification / protection / thermal | Class direction; fault model | Study reports (symbolic) | Component / IE | Architect | CR-001 / framework | Schematic prep | MPN selected or approved without completed qualification and explicit Architect authorization |
| [E] Schematic / PCB | Provisional baseline + qual | Design files (future) | Implementation Engineer | Architect | Design review | Measurement | **NOT AUTHORIZED in WP-012** |
| [F] Measurement | Fixture; MP-* | Raw traces | Test Engineer | Architect | Measurement plan | Threshold acceptance | PASS without VE |
| [G] Certified threshold | Measurement + model | Architect freeze | System Architect | Architect | Accepted CR | Verification | Silent approval |
| [H] Verification evidence | Certified threshold | VE record | Test Engineer | Architect | VE | Gate PASS | Requirement Verified without VE |

### 2.4 Iteration rules

1. Return from [D] or [E] to [B]/[C] is **expected** when component data, layout, or measurement invalidates prior assumptions.
2. Provisional baseline **does not** replace certified threshold or VE.
3. External-energy envelope (P6) calculations shall **not** feed base-envelope [B]/[G] without explicit Architect scope separation (PWR-A-001/002).

### 2.5 Component qualification authority (Stage [D])

| Statement | Detail |
|-----------|--------|
| WP-012 selects **no MPN** | Evaluation classes only — no part numbers |
| Future qualification WP | A future **Architect-authorized** qualification WP may qualify a **concrete MPN** under CR-001 |
| Qualification ≠ procurement | Completed qualification **does not** silently authorize procurement |
| Qualification ≠ schematic | Completed qualification **does not** silently authorize schematic capture or PCB layout |
| Prohibited claim | MPN selected or approved **without** completed qualification **and** explicit Architect authorization for the intended use |

Stage [E] schematic/PCB remains gated on provisional baseline + qualification gates + explicit Architect authorization — unchanged from §2.3.

## 3. Sizing readiness status model

Every sizing parameter shall receive one readiness state:

| Status | Meaning |
|--------|---------|
| **METHOD_ACCEPTABLE** | Calculation or analysis method Accepted; numeric Open |
| **SYMBOLIC_CONSTRAINT_ACCEPTABLE** | Inequality or relationship Accepted without numeric bound |
| **INPUTS_INCOMPLETE** | Method defined; required ED-IN / TBD inputs missing |
| **BLOCKED_BY_THRESHOLD** | Numeric TBD-DK-* Open blocks closure |
| **BLOCKED_BY_ARCHITECTURE** | ADR-DK-* or OI-* architecture decision Open |
| **BLOCKED_BY_COMPONENT_CLASS** | Evaluation class not narrowed |
| **BLOCKED_BY_COMPONENT_SELECTION** | MPN qualification incomplete |
| **BLOCKED_BY_SCHEMATIC** | Schematic not authorized / absent |
| **BLOCKED_BY_PCB_DESIGN** | PCB layout / copper unknown |
| **BLOCKED_BY_FIXTURE** | Fixture specification absent |
| **BLOCKED_BY_MEASUREMENT** | Physical evidence required |
| **NOT_READY** | Prerequisites not met |

### 3.1 Non-equivalent concepts (mandatory separation)

Extends §2.1 value-state separation:

```text
Sizing method accepted          ≠  provisional numeric design input
Provisional design input        ≠  Architect-approved design baseline
Architect-approved baseline     ≠  certified threshold
Candidate calculation           ≠  verified physical value
Verified physical value         ≠  certified threshold
Certified threshold             ≠  verification evidence
Input assumption documented     ≠  approved design input
```

## 4. Sizing domains

### 4.1 Input power domain

| Topic | Symbolic quantities | Primary ED-IN / TBD | Readiness |
|-------|---------------------|---------------------|-----------|
| Input operating envelope | `V_IN`, UV/OV behaviour | ED-IN-001; TBD-DK-001/012 | INPUTS_INCOMPLETE |
| Source impedance | `Z_source` | OPEN_ASSUMPTION | NOT_READY |
| Source current limiting | `I_PSU_limit` | WP-009 L1 | METHOD_ACCEPTABLE |
| Continuous input current | `I_INPUT_AVG`, `I_certified_cont` | ED-IN-002; TBD-DK-002 | BLOCKED_BY_THRESHOLD |
| Transient input current | `I_INPUT_PEAK`, inrush | ED-IN-027 | INPUTS_INCOMPLETE |
| Prospective SC current | `I_psc`, `I_fault_peak` | ED-IN-009; TBD-DK-011 | INPUTS_INCOMPLETE |
| Reverse-polarity responsibility | Layer P2 | OI-PROT-001 | BLOCKED_BY_ARCHITECTURE |
| Transient protection | Layer P2 | OI-PROT-002 | BLOCKED_BY_ARCHITECTURE |
| Replaceable input protection | `I_protection_rating` | ED-IN-008 | BLOCKED_BY_THRESHOLD |
| Input disconnect | Procedure | Fixture WP | BLOCKED_BY_FIXTURE |
| Measurement boundary | MP-* at entry | WP-010 MP register | METHOD_ACCEPTABLE |

### 4.2 Logic domain

| Topic | Symbolic quantities | Primary ED-IN | Readiness |
|-------|---------------------|---------------|-----------|
| Processor-domain current | `I_LOGIC(t)` | ED-IN-024 | INPUTS_INCOMPLETE |
| Communication interfaces | SPI/CAN loads | WP-010 §3.1 | INPUTS_INCOMPLETE |
| Sensing / ADC load | `I_sense_logic` | OI-SENSE-001 | BLOCKED_BY_COMPONENT_CLASS |
| Debug/programming states | USB/UART peak | IF-DK-USB | INPUTS_INCOMPLETE |
| Startup peak | `I_LOGIC_PEAK` | ED-IN-024 | INPUTS_INCOMPLETE |
| Watchdog / safety monitoring | `I_WD_monitor` | TBD-DK-005 | BLOCKED_BY_THRESHOLD |
| Rail conversion losses | `P_CONV_LOGIC` | OI-RAIL-001 | INPUTS_INCOMPLETE |
| Future interface margin | Symbolic reserve | OPEN_ASSUMPTION | NOT_READY |

### 4.3 Radio domain

| Topic | Symbolic quantities | Primary ED-IN | Readiness |
|-------|---------------------|---------------|-----------|
| Idle state | `I_RADIO_IDLE` | ED-IN-025 | INPUTS_INCOMPLETE |
| Active service state | `I_RADIO_ACTIVE` | ED-IN-025 | INPUTS_INCOMPLETE |
| Transmit peak | `I_RADIO_TX_PEAK` | ED-IN-025 | INPUTS_INCOMPLETE |
| Startup / reset | `I_RADIO_STARTUP` | WP-010 §3.2 | INPUTS_INCOMPLETE |
| Service unavailable | Fail-operational current | ADR-017 | METHOD_ACCEPTABLE |
| Independent rail behaviour | Rail isolation | WP-010 power domains | METHOD_ACCEPTABLE |
| Rail conversion losses | `P_CONV_RADIO` | OI-RAIL-001 | INPUTS_INCOMPLETE |
| Base budget impact | Entry-referred domain sum | Budget model §4 | METHOD_ACCEPTABLE |

**Constraint (PWR-A-006):** Radio has no direct output-enable authority.

### 4.4 Power-control domain

| Topic | Symbolic quantities | Primary ED-IN | Readiness |
|-------|---------------------|---------------|-----------|
| Power controller load | `I_POWER_CTRL(t)` | WP-010 §12 | INPUTS_INCOMPLETE |
| Gate-driver / smart-switch control | `I_GATE_CTRL_n` | Evaluation class | BLOCKED_BY_COMPONENT_CLASS |
| Diagnostic circuits | `I_DIAG` | WP-010 | INPUTS_INCOMPLETE |
| Current-observation circuits | `I_SENSE_BURDEN` | ED-IN-011/032 | BLOCKED_BY_COMPONENT_CLASS |
| BOARD_ID | Identity read current | ED-IN-018 | INPUTS_INCOMPLETE |
| Control-loss fail-safe | T-Class C budget | ED-IN-006; TBD-DK-007 | BLOCKED_BY_THRESHOLD |
| Global enable chain | `nENABLE_GLOBAL` | WP-010 safe-state | METHOD_ACCEPTABLE |
| Hardware KILL path | Direct branch | ADR-022; OI-KILL-001 | METHOD_ACCEPTABLE |

### 4.5 Representative output-channel domain

| Topic | Symbolic quantities | Primary ED-IN | Readiness |
|-------|---------------------|---------------|-----------|
| Continuous channel current | `I_CHANNEL_CONT` | ED-IN-026; TBD-DK-002 | BLOCKED_BY_THRESHOLD |
| Instantaneous / peak | `I_CHANNEL_PEAK`, inrush | ED-IN-027 | INPUTS_INCOMPLETE |
| Average / RMS | `I_CHANNEL_AVG`, `I_CHANNEL_RMS` | Budget model | METHOD_ACCEPTABLE |
| PWM operation | `f_PWM`, duty | ED-IN-010; TBD-DK-008 | BLOCKED_BY_THRESHOLD |
| Conduction / switching loss | `P_CONDUCTION`, `P_SWITCHING` | Thermal framework | METHOD_ACCEPTABLE |
| Fault current / duration | `I_FAULT`, `t_fault`, `E_FAULT` | ED-IN-009 | INPUTS_INCOMPLETE |
| Retry/latch | Policy | ED-IN-014; TBD-DK-013 | BLOCKED_BY_THRESHOLD |
| Simultaneous profiles | `I_simultaneous` | ED-IN-003; TBD-DK-003 | BLOCKED_BY_THRESHOLD |

### 4.6 External energy domain

Distinct treatment required — **base envelope not inherited** (PWR-A-001…003):

| Path | Symbol | Scope | Readiness |
|------|--------|-------|-----------|
| **EXT-SOURCE** | External supply entry | Fixture / bench only | BLOCKED_BY_FIXTURE |
| **EXT-LOAD-BANK** | `I_loadbank_limit` | ADR-020 P6 | BLOCKED_BY_FIXTURE |
| **EXT-POWER-MODULE** | Module-rated envelope | Separate qualification | NOT_READY |

External-envelope ratings shall **not** increase `I_certified_cont` (PWR-A-002).

## 5. Capability aliases and physical population

WP-010 rule retained: aliases are verification roles, not physical channel counts.

| Capability alias | Physical instance | Current class | Power-loss model | Verification independence | Status |
|------------------|-------------------|---------------|------------------|---------------------------|--------|
| CH-HS-BASE | TBD | Open | Symbolic | Required | Open |
| CH-HS-PWM | TBD | Open | Symbolic | Required | Open |
| CH-HS-SENSE | TBD | Open | Symbolic | Required | Open |
| CH-HS-PROTECTED | TBD | Open | Symbolic | Required | Open |
| CH-BI-REP | TBD | Open | Symbolic | Required | Open |
| CH-HC-EXTERNAL | External only | Open | Fixture scope | Separate evidence | Open |

See [`DevKit_Current_and_Power_Budget_Model.md`](DevKit_Current_and_Power_Budget_Model.md) §6 and [`DevKit_Sizing_Dependency_and_Closure_Matrix.md`](DevKit_Sizing_Dependency_and_Closure_Matrix.md).

## 6. Downstream work boundaries

### 6.1 WP-012 may authorize preparation for

- component-class qualification comparison;
- symbolic preliminary calculation;
- protection philosophy decision records;
- thermal-model setup (assumption-level);
- fixture requirement definition.

### 6.2 WP-012 shall not authorize

- component MPN selection · procurement · final numeric freeze;
- schematic capture · PCB layout · firmware · fixture construction.

| Transition | Owning future WP |
|------------|------------------|
| Evaluation class → MPN qualification | Component-class qualification WP |
| Symbolic calc → numeric freeze | Electrical sizing + Architect acceptance WP |
| Protection philosophy → device selection | Protection coordination + schematic WP |
| Thermal model → copper/stack-up | PCB electrical constraints WP |
| Fixture requirements → build | Fixture/load-bank WP |
| Schematic → layout | Schematic WP → PCB WP |

## 7. Related documents

| Document | Role |
|----------|------|
| [`DevKit_Current_and_Power_Budget_Model.md`](DevKit_Current_and_Power_Budget_Model.md) | Current/power quantities and profiles |
| [`DevKit_Thermal_Sizing_Framework.md`](DevKit_Thermal_Sizing_Framework.md) | Thermal methodology |
| [`DevKit_Protection_Coordination_Framework.md`](DevKit_Protection_Coordination_Framework.md) | Protection layers and faults |
| [`DevKit_Power_Path_Assumption_Register.md`](DevKit_Power_Path_Assumption_Register.md) | Assumptions and constraints |
| [`DevKit_Sizing_Dependency_and_Closure_Matrix.md`](DevKit_Sizing_Dependency_and_Closure_Matrix.md) | Blockers and closure |
| [`DevKit_Electrical_Design_Input_Register.md`](DevKit_Electrical_Design_Input_Register.md) | ED-IN dependency references |

## 8. Traceability

| Source | WP-012 reference |
|--------|------------------|
| REQ-DCC-V-DK-002, 011, 035, 039–055, 093–097 | Domain sizing |
| DK-GOV-009, 024, 025 | Qualification and threshold freeze |
| ADR-019…023 | Capability, envelope, timing, fault scope |
| TBD-DK-001…022 | Numeric Open — not Resolved |
| ED-IN-001…032 | Dependency references — not frozen |
| VER-DCC-DK-A/C-* | Cases remain NOT EXECUTED / BLOCKED |

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial electrical sizing framework — Proposed |
| 1.1 | 2026-07-20 | WP-012-R1 — staged iterative closure; provisional baseline path; measurement-boundary cross-ref |
| 1.2 | 2026-07-20 | WP-012-R2 — Stage [D] qualification authority; MPN/procurement/schematic separation |
| 1.3 | 2026-07-20 | Architecture Review Accepted — PR #16 merged (`9c5c7e7` / `fe700d4`); numeric Open; TBD-DK-007 BLOCKED unchanged |
