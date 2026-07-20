# DevKit High-Side Class Comparison — WP-013

**Document ID:** DOC-DK-HSCC-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-013  
**Date:** 2026-07-20

```text
Class comparison only — no MPN, manufacturer, package, or numeric Approved.
Recommendation ≠ Acceptance ≠ MPN selection.
```

## 1. Purpose

Compare high-side switching evaluation classes against Accepted ADR-019 capability aliases and WP-011/WP-012 methodology. Owner decisions: **OI-COMP-001**, **ED-IN-030**.

## 2. Classes under evaluation

| Class ID | Definition |
|----------|------------|
| **HS-INT-DIAG** | Integrated protected high-side switch with diagnostics |
| **HS-INT-BASIC** | Integrated protected high-side switch without full diagnostic coverage |
| **HS-GATE-DISCRETE** | External controller/gate-driver plus discrete power device |
| **HS-HYBRID** | Integrated control/protection with external power element and/or external sense |
| **HS-ARRAY** | Multi-channel integrated high-side architecture (shared die/package family) |

## 3. Capability coverage vs ADR-019 aliases

| Alias | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-------|-------------|--------------|------------------|-----------|----------|
| **CH-HS-BASE** | Viable | Viable | Viable | Viable | Viable (shared package) |
| **CH-HS-PWM** | Viable if PWM-rated class | Viable if PWM-rated | Viable with gate timing design | Viable if PWM-rated | Viable if PWM-rated; shared thermal risk |
| **CH-HS-SENSE** | Viable (integrated) | Weak / incomplete | Requires external sense class | Strong with external sense | Per-channel sense often limited |
| **CH-HS-PROTECTED** | Strong (integrated OC/SC) | Partial (protection without full diag) | Viable with external CH-PROT | Hybrid coordination | Shared protection common-cause |
| Open-load (conditional) | Claim-dependent (PWR-A-010) | Often absent | External implementation | Claim-dependent | Claim-dependent |

Physical channel population remains **Open** (PWR-A-008; OI-CHAN-001). Aliases are verification roles — not frozen channel counts.

## 4. Criterion evaluation (summary)

### 4.1 Functional and safety

| Criterion | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-----------|-------------|--------------|------------------|-----------|----------|
| Safe OFF without control | Typically OFF if enable chain inactive | Typically OFF | Depends on gate-driver default | Depends on enable chain | Shared enable common-cause |
| Control-loss reaction | Device + CTRL timeout (TBD-DK-007 Open) | Device + CTRL | Gate-driver / discrete fail-safe design | Combined | Array-wide fail-safe design |
| Hardware KILL compatibility | Must accept hardwired disable (PWR-A-004) | Same | Gate pull-down / hard disable path required | Same | Array-wide hard disable required |
| `nENABLE_GLOBAL` interaction | Separate from KILL (Accepted) | Same | Same | Same | Same |
| Independent verification | Strong diagnostics aid DK-C | Weak observability | Flexible but more fixture wiring | Strong if hybrid sense | Harder per-channel isolation |

### 4.2 Electrical / thermal / diagnostic

| Criterion | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-----------|-------------|--------------|------------------|-----------|----------|
| Conduction-loss model | `P_COND = f(I_RMS, R_DS(on)(T) or V_drop)` | Same simplified | Same + gate driver loss | Device + external element | Shared thermal coupling |
| Switching-loss model | `P_SW = f(V_IN, I_LOAD, E_sw, f_PWM, D)` | Same | Explicit E_sw from FET/driver | Combined | Shared package limits |
| Current observation | Integrated class (SENSE-INTEGRATED) | Limited | Needs SENSE-* class | Often SENSE-HYBRID | Often aggregated |
| Fault-energy containment | Integrated clamp/limit + P4 | Integrated limited | External CH-PROT + P2 | Coordinated | Shared clamp risk |
| Thermal concentration | Per-device | Per-device | Layout-dominated | Split | Highest coupling risk |
| PCB dependence | Package/copper TBD (OI-PCB-001) | Same | High | High | Very high |
| Controller-interface burden | SPI/diag pins or status | Lower pin count | GPIO/PWM + sense ADC | Mixed | Shared SPI bus contention |
| Common-cause exposure | Per channel | Per channel | Per channel | Moderate | **Elevated** (shared die/rail) |

## 5. Comparison table (normative summary)

| Class | Capability coverage | Safe-state compatibility | Diagnostics | Current observation | PWM suitability | Protection model | Thermal model | Integration burden | Main blockers | Qualification status |
|-------|---------------------|--------------------------|-------------|---------------------|-----------------|------------------|---------------|--------------------|---------------|----------------------|
| **HS-INT-DIAG** | BASE+PWM+SENSE+PROTECTED (claim-dependent OL) | Compatible with KILL / `nENABLE_GLOBAL` if hardwired disable preserved | Strong | Integrated or hybrid | High if class PWM-rated | Integrated P4 + coord with P2 | Per-channel; R_TH Open | Moderate | ED-IN-002/010/026; TBD thermal; ADR-DK-011 | **CLASS_CONDITIONALLY_VIABLE** → recommend next stage |
| **HS-INT-BASIC** | BASE+PWM; weak SENSE/PROTECTED observability | Compatible if hard disable | Weak | Incomplete for CH-HS-SENSE | Medium | Integrated limited | Per-channel | Low–moderate | Fails CH-HS-SENSE/PROTECTED intent without add-ons | **CLASS_NOT_RECOMMENDED** as primary DevKit HS class |
| **HS-GATE-DISCRETE** | Full if sense+prot added | Compatible if gate default OFF + KILL path | Designer-defined | External SENSE-* required | High with careful timing | External / hybrid CH-PROT | Layout-sensitive | High | ED-IN-030; OI-SENSE-001; schematic complexity | **CLASS_CONDITIONALLY_VIABLE** — retain comparison |
| **HS-HYBRID** | Full with external element/sense | Compatible if enable chain hardwired | Strong when hybrid sense | Prefer SENSE-HYBRID | High | Hybrid P4 | Split loss paths | High | Same + external FET thermal | **CLASS_CONDITIONALLY_VIABLE** — conditional next stage |
| **HS-ARRAY** | Multi-alias on shared silicon | Compatible only if array-wide hard disable proven | Often aggregated | Often limited per ch | Medium–high | Shared protection common-cause | Coupled | Moderate pin, high thermal analysis | Common-cause; OI-CHAN-001; thermal coupling | **CLASS_CONDITIONALLY_VIABLE** — retain; not preferred primary |

## 6. Recommendations (Implementation Engineer — not Accepted)

| Class | Recommendation | Conditions |
|-------|----------------|------------|
| **HS-INT-DIAG** | **RECOMMENDED_FOR_NEXT_STAGE** | Hardwired KILL disable preserved; PWM rating covers CH-HS-PWM; diagnostic claim covers CH-HS-SENSE/PROTECTED; open-load only if claimed (PWR-A-010); numerics remain Open |
| **HS-HYBRID** | **CONDITIONALLY_RECOMMENDED** | When precision observation or external power element required for envelope; else secondary to HS-INT-DIAG |
| **HS-GATE-DISCRETE** | **RETAIN_FOR_COMPARISON** | Acceptable fallback if integrated class cannot meet envelope/PWM/diag; requires external SENSE + CH-PROT architecture |
| **HS-ARRAY** | **RETAIN_FOR_COMPARISON** | Only if Architect accepts elevated common-cause and thermal-coupling analysis |
| **HS-INT-BASIC** | **NOT_RECOMMENDED** | Insufficient diagnostic/current-observation coverage for mandatory CH-HS-SENSE / CH-HS-PROTECTED without additional classes that effectively become HS-HYBRID |

**Preferred primary class (recommendation only):** HS-INT-DIAG.  
**Permitted fallback (recommendation only):** HS-GATE-DISCRETE or HS-HYBRID — Architect choice.

## 7. Rejected assumptions

| Assumption | Disposition |
|------------|-------------|
| Any HS class automatically satisfies open-load | **Rejected** — PWR-A-010 conditional |
| Fuse / integrated limit = `I_certified_cont` | **Rejected** — PWR-A-016 |
| Software OFF = hardware protection | **Rejected** — aligns PWR-A-018 (PROPOSED_CONSTRAINT) |
| Historical part numbers are candidates | **Rejected** — HISTORICAL / NON-NORMATIVE CONTEXT only |
| Class recommendation = MPN authorization | **Rejected** — WP-012 Stage [D]/[E] gates |

## 8. Traceability

REQ-DCC-V-DK-039…049 · ADR-019 · ED-IN-030 · OI-COMP-001 · PWR-A-004/005/008/010/016 · WP-011 HS dimensions · WP-012 loss/thermal methods.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial high-side class comparison — Proposed |
