# DevKit Component-Class Qualification Report — WP-013

**Document ID:** DOC-DK-CCQR-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer

```text
Component-CLASS qualification and symbolic preliminary calculations.
No MPN · no manufacturer · no BOM · no numeric Approved · no schematic/PCB · no VE.
Recommendation ≠ Acceptance.
```

## 1. Purpose and scope

Apply Accepted WP-011 qualification methodology and WP-012 sizing framework to:

1. compare permitted component architecture classes;
2. identify strengths, limitations, and dependencies;
3. establish conditional class recommendations;
4. reject unsuitable class assumptions;
5. perform symbolic preliminary electrical calculations;
6. identify inputs required before provisional numeric sizing;
7. prepare transition to fixture requirements and provisional electrical design.

**Out of scope:** MPN selection, procurement, BOM, schematics, PCB, firmware, EDL/ADR edits, numeric approval, VE, requirement Verified claims.

## 2. Authority hierarchy

Engineering Constitution → Accepted EDL → Accepted ADR-016…023 → WP-007…WP-012 Accepted → **this Proposed WP-013 package** → historical/candidate (non-normative).

## 3. Qualification status model

```text
CLASS_METHOD_ACCEPTABLE
CLASS_VIABLE
CLASS_CONDITIONALLY_VIABLE
CLASS_RECOMMENDED_FOR_NEXT_STAGE
CLASS_NOT_RECOMMENDED
CLASS_REJECTED
BLOCKED_BY_INPUT
BLOCKED_BY_ARCHITECTURE
BLOCKED_BY_PROTECTION_MODEL
BLOCKED_BY_THERMAL_MODEL
BLOCKED_BY_FIXTURE
NOT_READY
```

**Non-equivalent states:**

```text
Class comparison complete
≠ Class viable
≠ Class recommended
≠ Architecture class Accepted
≠ Concrete MPN qualified
≠ Concrete MPN selected
≠ Procurement authorized
≠ Schematic use authorized
≠ Physical behaviour verified
```

Implementation Engineer may recommend; System Architect accepts.

## 4. Package map

| Document | Role |
|----------|------|
| [DevKit_High_Side_Class_Comparison.md](DevKit_High_Side_Class_Comparison.md) | HS-INT-DIAG / BASIC / GATE-DISCRETE / HYBRID / ARRAY |
| [DevKit_Current_Observation_Class_Comparison.md](DevKit_Current_Observation_Class_Comparison.md) | SENSE-* classes + E_TOTAL model |
| [DevKit_Protection_Class_Comparison.md](DevKit_Protection_Class_Comparison.md) | RP / transient / replaceable / channel vs P0–P5 |
| [DevKit_Bidirectional_Class_Comparison.md](DevKit_Bidirectional_Class_Comparison.md) | BI-HB-* / RELAY / DUAL-HSLS |
| [DevKit_Symbolic_Preliminary_Calculations.md](DevKit_Symbolic_Preliminary_Calculations.md) | Symbolic losses, entry reconcile, fault, thermal, BI |
| [DevKit_Class_Recommendation_and_Readiness_Matrix.md](DevKit_Class_Recommendation_and_Readiness_Matrix.md) | Master recommendations |

## 5. Executive class recommendations (Proposed — WP-013-R1)

**WP-010 rule:** capability aliases are roles — not a single class for every physical channel. Population remains Open.

| Domain | Evaluation direction (IE) | Conditional / retain | Not recommended (scoped) |
|--------|---------------------------|----------------------|--------------------------|
| High-side | **HS-INT-DIAG** for instances claiming SENSE and/or PROTECTED | **HS-INT-BASIC** for BASE/PWM-only instances (SENSE/PROTECTED elsewhere); HS-HYBRID when external elements needed; GATE-DISCRETE / ARRAY retain | One class for entire population (**rejected assumption**) |
| Current observation | **SENSE-INTEGRATED** conditional for diag/protect when claims fit | **SENSE-HYBRID** conditional when independence/accuracy required (**not** unconditional preferred); SHUNT-HS / MAGNETIC retain | SENSE-SHUNT-LS as **primary HS**; SENSE-INDIRECT as **sole** verification |
| Reverse polarity | Direction **Open** (OI-PROT-001) | RP-ACTIVE-IDEAL / PASSIVE / HYBRID retain if arch opens | RP-RELAY primary |
| Transient | Direction **Open** (OI-PROT-002) | CLAMP-DISCONNECT / MULTISTAGE conditional | — |
| Replaceable input | **INPUT-HYBRID** philosophy | FUSE / ELECTRONIC with PWR-A-016 | Fuse = continuous cert (**rejected**) |
| Channel protection | **CH-HYBRID** when independence required | CH-INTEGRATED with HS-INT-DIAG instances | — |
| Bidirectional | **BI-HB-FULL** or **BI-HB-HYBRID** | DISCRETE / DUAL-HSLS | BI-RELAY-REVERSING primary |
| Controller IF | **CTRL-MIXED-HARDWIRED** | CTRL-SPI-MCU / SPI-SAFETY for cmd/diag only | SPI-owned physical KILL (**rejected**) |

`RECOMMENDED_FOR_NEXT_STAGE` = continued evaluation permitted — **not** Architecture class Accepted, MPN, procurement, or schematic/PCB.

## 6. Controller-interface assessment

| Class | Role | KILL | `nENABLE_GLOBAL` | Command transport | Diagnostics |
|-------|------|------|------------------|-------------------|-------------|
| **CTRL-DIRECT-GPIO** | Direct pin control | Must remain hardwired path | Separate | GPIO | Limited |
| **CTRL-SPI-MCU** | Power-board MCU SPI slave | **Must not** be sole KILL path | Separate Logic-controlled | SPI | MCU-reported |
| **CTRL-SPI-SAFETY** | Safety-oriented SPI framing | Same prohibition | Separate | SPI | Structured |
| **CTRL-MIXED-HARDWIRED** | Hardwired safety + SPI/GPIO cmd | **Direct hardware-effective branch** (PWR-A-004) | Separate inactive-default (PWR-A-005) | SPI/GPIO ≠ KILL | Separate observation path |

**Normative preservation (Accepted):**

```text
Physical KILL: direct hardware-effective branch
nENABLE_GLOBAL: Logic-controlled global enable
Command transport: separate from hardwired safety signals
Diagnostics: separate observation path
```

No class may require Logic firmware execution for physical KILL effectiveness.

**IE recommendation:** CTRL-MIXED-HARDWIRED as the DevKit Power interface pattern; SPI classes only for command/diagnostics.

Control-loss numeric **TBD-DK-007** remains Open / **BLOCKED_BY_EDL_CLARIFICATION** / NOT VERIFIED.

## 7. Symbolic calculation summary

Accepted WP-012 entry reconcile and signed-net accounting applied. WP-013-R1 corrects:

- conduction-loss duty discipline (`I_ON`/`I_RMS_PROFILE` — no double duty);
- event-based switching loss (`f_EVENT=0` if static ON/OFF);
- separated `E_SOURCE_STALL` vs `E_BRIDGE_LOSS`; thermal-state retry evolution;
- fault-energy bound only with proven `V_BOUND`/`I_BOUND`/`T_BOUND`.

All preliminary calculations remain **symbolic**. Readiness: see [DevKit_Symbolic_Preliminary_Calculations.md](DevKit_Symbolic_Preliminary_Calculations.md) §11.

## 8. Missing inputs and blockers (index)

| Blocks | Primary artifacts |
|--------|-------------------|
| Provisional numeric design baseline | TBD-DK-001…022 Open; Architect provisional authorization |
| Concrete MPN qualification | Class Accepted; CR-001; Stage [D] gates |
| Fixture requirements | OI-FIX-002; OI-SC-001; ED-IN-020/021 |
| Schematic design | Class Accepted; provisional baseline; Stage [E] **NOT AUTHORIZED** |
| PCB design | OI-PCB-001; ADR-DK-011/012; Stage [E] |
| Firmware BSP | Not authorized by WP-013 |
| Physical verification | No VE; cases NOT EXECUTED / BLOCKED |
| RP / transient direction | **OI-PROT-001**, **OI-PROT-002** |
| Control-loss numeric | **TBD-DK-007** BLOCKED_BY_EDL_CLARIFICATION |

## 9. Answers to WP-013 objective questions

| # | Answer (Proposed — WP-013-R1) |
|---|-------------------------------|
| 1 | Viable by role: HS-INT-DIAG (SENSE/PROTECTED instances); HS-INT-BASIC (BASE/PWM-only); HYBRID/GATE-DISCRETE/ARRAY; SENSE-INTEGRATED/HYBRID (conditional); SHUNT-HS/MAGNETIC; INPUT-*; CH-*; BI-HB-*; CTRL-MIXED/SPI-* (cmd only) |
| 2 | Conditionally preferred **by role**: HS-INT-DIAG for SENSE/PROTECTED instances; SENSE-INTEGRATED for diag/protect when claims fit; SENSE-HYBRID when independence/accuracy required; INPUT-HYBRID; CH-HYBRID or INTEGRATED; BI-HB-FULL/HYBRID; CTRL-MIXED-HARDWIRED |
| 3 | Reject/not recommend (scoped): one HS class for all channels; SENSE-HYBRID as unconditional preferred; SENSE-SHUNT-LS as primary HS; SENSE-INDIRECT as sole; BI-RELAY-REVERSING; SPI-owned KILL |
| 4 | Cannot evaluate numeric envelopes, R_TH, fuse ratings, dead-time, stall current, or conservative fault bounds without Open inputs |
| 5–6 | See symbolic calculations (R1) + class docs |
| 7 | Class acceptance + CR-001 evidence + thermal/protection inputs |
| 8 | Architect provisional baseline + closed symbolic models + declared assumptions |
| 9 | See §8 blockers; OI-PROT-001/002 remain Open |
| 10 | After acceptance: fixture/load-bank requirements; ADR-DK-011/012; optional provisional baseline prep; concrete MPN qual prep — **not** schematic/PCB until gates |

## 10. Explicit exclusions

```text
No MPN selected.
No manufacturer recommended.
No BOM created.
No numeric threshold approved.
No schematic or PCB authorized.
No physical verification performed.
```

## 11. Traceability

REQ-DCC-V-DK-039…055 · DK-GOV-009/024/025 · VER-DCC-DK-A/C-* (NOT EXECUTED/BLOCKED) · ADR-019…023 · TBD-DK-* Open · TBD-DK-007 BLOCKED · ED-IN-* · OI-* · PWR-A-* · WP-011 classes · WP-012 methods · WP-013 recommendations (Proposed).

CIA: `CIA-2026-008` · RHP: `RHP-2026-007`.

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial component-class qualification report — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — capability-role mapping; observation conditional; symbolic equation corrections |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #17 merged (`d1698a0` / `23bdb07`); methodology Accepted; final classes/topology Open; TBD-DK-007 BLOCKED unchanged |
