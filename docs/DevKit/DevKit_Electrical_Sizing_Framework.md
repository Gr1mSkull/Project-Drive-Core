# DevKit Electrical Sizing Framework — WP-012

**Document ID:** DOC-DK-ESF-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
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

## 2. Sizing lifecycle

```text
Accepted requirement (REQ-DCC-V-DK-*)
  → functional capability (ADR-019 / WP-010 alias)
  → operating profile (P0…P6)
  → electrical design input (ED-IN-*)
  → symbolic sizing model (this framework)
  → evaluation-class requirements (WP-011)
  → preliminary calculation (future WP — symbolic only)
  → component qualification (CR-001 path)
  → protection coordination
  → thermal evaluation
  → schematic implementation (future WP — NOT AUTHORIZED)
  → PCB implementation (future WP — NOT AUTHORIZED)
  → physical measurement
  → threshold acceptance (Architect)
  → verification evidence (VE)
```

### 2.1 Stage governance

| Stage | Required inputs | Permitted outputs | Responsible role | Review authority | Evidence required | Downstream dependency | Prohibited claims |
|-------|-----------------|-------------------|------------------|------------------|-------------------|----------------------|-------------------|
| Requirement | Accepted SRS / DevKit REQ | Capability mapping | System Architect | Architecture Review | Traceability | Profile definition | Verified without VE |
| Functional capability | ADR-019; WP-010 aliases | Capability-to-domain map | Implementation Engineer | Architect | WP-010 package | ED-IN identification | Physical channel count frozen |
| Operating profile | P0…P6 definition | Profile record (no numeric I) | Test Engineer | Architect | WP-009 profiles | Symbolic budget | Certified continuous current |
| Design input | TBD-DK-*; ED-IN-* | Dependency reference | System Architect | Architect | ED-IN register | Symbolic model | Approved design input |
| Symbolic sizing model | This framework | Equations, inequalities (symbolic) | Implementation Engineer | Architect | WP-012 package | Class comparison | Numeric limit Approved |
| Evaluation class | WP-011 matrix | Class readiness table | Component Engineer | Architect | Qualification framework | Preliminary calc | MPN selected |
| Preliminary calculation | Closed symbolic inputs | Candidate calculation (labelled) | Implementation Engineer | Architect | Calculation record | Qualification | Numeric freeze |
| Component qualification | Class direction; datasheet | Qualification report | Component Engineer | Architect | CR-001 report | Schematic auth | Continuous rating Approved |
| Protection coordination | Fault classes; layers P0–P5 | Coordination study (symbolic) | Implementation Engineer | Architect | Protection framework | Schematic | Fuse value selected |
| Thermal evaluation | Loss model; R_th assumptions | Thermal study (symbolic) | Implementation Engineer | Architect | Thermal framework | PCB constraints | T_max Approved |
| Schematic | Qualified components | Schematic (future) | Implementation Engineer | Architect | Design review | PCB | **NOT AUTHORIZED in WP-012** |
| PCB | Schematic; constraints | Layout (future) | Implementation Engineer | Architect | DRC/thermal sim | Measurement | **NOT AUTHORIZED in WP-012** |
| Measurement | Fixture; MP-* | Raw traces | Test Engineer | Architect | Measurement plan | Threshold acceptance | PASS without VE |
| Threshold acceptance | Measurement + model | Architect freeze | System Architect | Architect | Accepted CR | Verification | Silent numeric approval |
| Verification evidence | Certified threshold | VE record | Test Engineer | Architect | VE | Gate PASS | Requirement Verified without VE |

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

```text
Sizing method accepted          ≠  numeric value approved
Symbolic inequality accepted    ≠  candidate calculation produced
Input assumption documented     ≠  approved design input
Candidate calculation produced  ≠  numeric value approved
Numeric value approved          ≠  physical value verified
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
| Base budget impact | Δ`I_BASE_INST` | Budget model | METHOD_ACCEPTABLE |

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
