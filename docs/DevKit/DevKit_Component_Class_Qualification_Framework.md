# DevKit Component-Class Qualification Framework — WP-011

**Document ID:** DOC-DK-CCQF-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-011  
**Date:** 2026-07-20

```text
Qualification FRAMEWORK only — no MPNs, no manufacturers, no BOM.
Component class definitions are evaluation criteria, not procurement shortlist.
Prepares future component selection under CR-001 / WP-002 methodology.
```

## 1. Purpose

Define **how** DevKit component classes will be evaluated before any concrete part is selected. This framework supports Accepted **ADR-019** representative capabilities and Accepted **WP-010** functional architecture without authorizing schematic or BOM work.

**Component class definitions are evaluation criteria, not procurement shortlist.**

**Out of scope:** MPN selection · datasheet values as Approved limits · PCB design · verification evidence.

## 2. Relationship to existing qualification policy

| Document | Role |
|----------|------|
| CR-001 / WP-002 | Platform qualification methodology |
| `.cursor/rules/05_component_selection.mdc` | No BOM without qualification |
| `docs/007_Component_Selection.md` | Conceptual classes (HS05…HS60) — not DevKit Approved BOM |
| ADR-019 | Mandatory capability set for DevKit |
| WP-010 | Functional topology and open issues (OI-COMP-001…003, OI-SENSE-001) |

DevKit component-class qualification **extends** platform methodology with DevKit-specific capability gates. A future WP shall produce class-level qualification records in `hardware/qualification/` — **not authorized in WP-011**.

## 3. Qualification workflow (class level)

```text
Requirements (ADR-019, REQ-DCC-V-DK-*)
  → Class definition (this framework)
  → Evaluation class identification (matrix — no MPN)
  → Class-level evaluation criteria scoring (future WP)
  → Architect acceptance of class direction
  → MPN qualification (future WP — CR-001 path)
  → Schematic authorization (future WP)
```

## 3.1 Qualification gating

Component class **selection** cannot proceed before the following inputs are Accepted or explicitly bounded for DevKit:

| Prerequisite | Source | Status |
|--------------|--------|--------|
| **Current envelope definition** | TBD-DK-002/003; WP-009; ADR-021 | Open |
| **Thermal assumptions** | TBD-DK-018/019; ADR-DK-011 | Open |
| **Protection philosophy** | WP-010 OI-PROT-*; TBD-DK-002 input protection | Open |
| **Verification boundary** | WP-007 verification plan; ADR-020 external path | Accepted structure; cases Not Verified |

Evaluation-class identification (WP-011 matrix) may proceed in parallel; **narrowing to a selected class** for schematic or MPN work remains gated until prerequisites close.

## 4. High-side switching class

### 4.1 Required capabilities (from ADR-019 / WP-010)

| Capability | Verification relevance |
|------------|------------------------|
| ON/OFF switching | VER-DCC-DK-C-001, C-002 |
| PWM modulation | VER-DCC-DK-C-003 |
| Current observation path | VER-DCC-DK-C-004 |
| Overcurrent reaction | VER-DCC-DK-C-005 |
| Short-circuit reaction | VER-DCC-DK-C-006 |
| Retry/latch behaviour | VER-DCC-DK-C-008 |
| Control-loss safe OFF | VER-DCC-DK-A-008, C-012 |
| Open-load detection | VER-DCC-DK-C-007 — **conditional** on implementation claim |

### 4.2 Evaluation dimensions (criteria only)

| Dimension | Evaluation questions | Evidence type (future) |
|-----------|---------------------|------------------------|
| **Switching capability** | Supports required voltage/current class symbolically? PWM frequency headroom? | Datasheet + thermal model |
| **Protection behaviour** | OC/SC detection mechanism? Energy limitation? | Datasheet + test fixture plan |
| **Diagnostic capability** | Fault codes? Status registers? Analog fault pin? | Datasheet + interface matrix |
| **Fault reporting** | Compatible with J_LP diagnostic observation path? | Interface analysis |
| **Shutdown behaviour** | OFF state leakage? Fail-safe on control loss? | Timing measurement |
| **PWM compatibility** | Frequency/duty range vs TBD-DK-008 (Open)? | Datasheet + bench test |
| **Thermal behaviour** | Rth path? Simultaneous operation? | Thermal model + ADR-DK-011 |
| **Recovery behaviour** | Retry/latch vs TBD-DK-013 (Open)? | Fault injection plan |

**Forbidden in WP-011:** naming specific PROFET families, MPNs, or headline current ratings as Approved.

## 5. Bidirectional channel class

### 5.1 Required capabilities

| Capability | Source |
|------------|--------|
| Bidirectional energy transfer | ADR-019; REQ-DCC-V-DK-042 |
| Direction conflict prevention | REQ-DCC-V-DK-054 |
| Stall behaviour (when fixture exists) | TBD-DK-022; VER-DCC-DK-C-011 |
| Safe OFF both directions | WP-010 BI topology |

### 5.2 Evaluation dimensions

| Dimension | Evaluation questions |
|-----------|---------------------|
| **Current direction handling** | Explicit forward/reverse/brake modes? Command model? |
| **Conflict prevention** | Hardware interlock vs firmware-only? |
| **Shoot-through prevention** | Dead-time? Break-before-make? Topology class? |
| **Safe shutdown** | Default OFF on power-up? Kill path interaction? |
| **State detection** | Direction feedback? Current sign? |
| **Fault containment** | Local disable scope? Propagation to global enable? |

Topology selection (half-bridge, full-bridge, dual-switch) remains **Component/Schematic scope** (OI-BI-001).

## 6. Current measurement class

Evaluate **classes** of observation — do **not** choose one in WP-011.

| Class | Description | Evaluation factors |
|-------|-------------|-------------------|
| **Integrated sensing** | Current sense via switch diagnostic | Accuracy vs TBD-DK-009 (Open); calibration |
| **External shunt** | Discrete shunt + amplifier | Burden voltage; PCB layout; range |
| **Current mirror / replica** | Scaled current representation | Linearity; temperature drift |
| **Indirect estimation** | Model-based or voltage-proxy | Plausibility; fault detection limits |

WP-010 defers topology to Component/Schematic WP. Qualification must prove observation supports VER-DCC-DK-C-004 without assuming a pre-selected method.

## 7. Protection layer class

Evaluate protection **functions** — not specific TVS/fuse MPNs.

| Function | Architecture reference | Open inputs |
|----------|------------------------|-------------|
| **Reverse polarity** | WP-010 input chain; OI-PROT-001 | Method not selected |
| **Transient protection** | OI-PROT-002 | Device class Open |
| **Overcurrent (input)** | TBD-DK-002; replaceable protection | Rating Open |
| **Undervoltage** | TBD-DK-001/012; OI-UV-001/002 | Threshold Open |
| **Thermal** | ADR-DK-011; TBD-DK-010/018/019 | Limits Open |

Protection coordination (channel vs system on SC) remains **sizing WP** scope.

## 8. Controller interface class (J_LP / Power controller)

| Dimension | Evaluation questions |
|-----------|---------------------|
| SPI slave behaviour | Command transport; timeout fail-safe mechanism |
| PWM input handling | Channel mapping; dead-time |
| Hardware safety nets | `nKILL_HW` direct branch; `nENABLE_GLOBAL`; independent of Logic CPU |
| Sense aggregation | Multiplexing vs dedicated paths — topology Open |
| BOARD_ID | Revision identity readable |
| Control-loss fail-safe | Power-side timeout hardware; TBD-DK-007 Open |

## 9. Qualification outputs (future WPs)

| Output | Owner WP |
|--------|----------|
| Class-level decision record | Component qualification WP |
| MPN qualification report | CR-001 path per MPN |
| DevKit channel-to-class mapping | Schematic WP |
| Thermal validation package | ADR-DK-011 + sizing WP |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-011 initial component-class qualification framework — Proposed |
| 1.1 | 2026-07-20 | WP-011-R1 — evaluation-class terminology; procurement disclaimer; qualification gating |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #15 |
