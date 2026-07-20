# DevKit High-Side Class Comparison — WP-013

**Document ID:** DOC-DK-HSCC-001  
**Version:** 1.1  
**Status:** Ready for Final Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20

```text
Class comparison only — no MPN, manufacturer, package, or numeric Approved.
Recommendation ≠ Acceptance ≠ MPN selection.
Capability aliases are roles — not a requirement that one class serve every physical channel.
```

## 1. Purpose

Compare high-side switching evaluation classes against Accepted ADR-019 / WP-010 capability aliases and WP-011/WP-012 methodology. Owner decisions: **OI-COMP-001**, **ED-IN-030**.

**WP-010 rule (retained):** `CH-HS-BASE`, `CH-HS-PWM`, `CH-HS-SENSE`, and `CH-HS-PROTECTED` are **capability and verification roles**. They do **not** require one component class to implement every physical channel. Physical population and channel count remain **Open** (PWR-A-008; OI-CHAN-001).

## 2. Classes under evaluation

| Class ID | Definition |
|----------|------------|
| **HS-INT-DIAG** | Integrated protected high-side switch with diagnostics |
| **HS-INT-BASIC** | Integrated protected high-side switch without full diagnostic coverage |
| **HS-GATE-DISCRETE** | External controller/gate-driver plus discrete power device |
| **HS-HYBRID** | Integrated control/protection with external power element and/or external sense |
| **HS-ARRAY** | Multi-channel integrated high-side architecture (shared die/package family) |

## 3. Class-to-capability-role matrix

| Class | CH-HS-BASE | CH-HS-PWM | CH-HS-SENSE | CH-HS-PROTECTED | Mapping rule |
|-------|------------|-----------|-------------|-----------------|--------------|
| **HS-INT-DIAG** | Suitable | Suitable if PWM-rated | Suitable when diagnostic claim covers sense role | Suitable when OC/SC/retry-latch claims cover protection role | Prefer for **instances claiming SENSE and/or PROTECTED** |
| **HS-INT-BASIC** | Suitable | Suitable if PWM-rated | Not by this class alone | Not by this class alone | **Conditionally viable** for instances claiming **only BASE and/or PWM**, if mandatory SENSE/PROTECTED roles are mapped to **other** physical instances and independently verified |
| **HS-GATE-DISCRETE** | Suitable | Suitable with gate timing | Requires external SENSE-* | Requires external CH-PROT | Fallback; explicit external sense + protection required |
| **HS-HYBRID** | Suitable | Suitable if PWM-rated | Strong with external sense | Hybrid coordination | Conditionally viable where external sense, protection, or power element required |
| **HS-ARRAY** | Suitable (shared package) | Suitable if PWM-rated | Often limited per channel | Shared protection common-cause | Retain subject to common-cause, diagnostic granularity, thermal-coupling evaluation |

**Do not** select a single class for the entire physical channel population.

## 4. Capability coverage detail

| Alias | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-------|-------------|--------------|------------------|-----------|----------|
| **CH-HS-BASE** | Viable | Viable | Viable | Viable | Viable (shared package) |
| **CH-HS-PWM** | Viable if PWM-rated class | Viable if PWM-rated | Viable with gate timing design | Viable if PWM-rated | Viable if PWM-rated; shared thermal risk |
| **CH-HS-SENSE** | Viable (integrated) when claimed | Not covered by this class alone | Requires external sense class | Strong with external sense | Per-channel sense often limited |
| **CH-HS-PROTECTED** | Strong when OC/SC claims cover role | Not covered by this class alone | Viable with external CH-PROT | Hybrid coordination | Shared protection common-cause |
| Open-load (conditional) | Claim-dependent (PWR-A-010) | Often absent | External implementation | Claim-dependent | Claim-dependent |

## 5. Criterion evaluation (summary)

### 5.1 Functional and safety

| Criterion | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-----------|-------------|--------------|------------------|-----------|----------|
| Safe OFF without control | Typically OFF if enable chain inactive | Typically OFF | Depends on gate-driver default | Depends on enable chain | Shared enable common-cause |
| Control-loss reaction | Device + CTRL timeout (TBD-DK-007 Open) | Device + CTRL | Gate-driver / discrete fail-safe design | Combined | Array-wide fail-safe design |
| Hardware KILL compatibility | Must accept hardwired disable (PWR-A-004) | Same | Gate pull-down / hard disable path required | Same | Array-wide hard disable required |
| `nENABLE_GLOBAL` interaction | Separate from KILL (Accepted) | Same | Same | Same | Same |
| Independent verification | Strong diagnostics aid DK-C | Weak on this instance; other instances may carry SENSE/PROTECTED | Flexible but more fixture wiring | Strong if hybrid sense | Harder per-channel isolation |

### 5.2 Electrical / thermal / diagnostic

| Criterion | HS-INT-DIAG | HS-INT-BASIC | HS-GATE-DISCRETE | HS-HYBRID | HS-ARRAY |
|-----------|-------------|--------------|------------------|-----------|----------|
| Conduction-loss model | See SPC §2 — `I_ON`/`I_RMS_PROFILE` forms; **no** `I_RMS²×R×D` double duty | Same simplified | Same + gate driver loss | Device + external element | Shared thermal coupling |
| Switching-loss model | Event-based `Σ E_transition` — `f_EVENT=0` if static ON/OFF | Same | Explicit transition energies | Combined | Shared package limits |
| Current observation | Integrated class and/or mapped SENSE-* on other instances | Limited on this instance | Needs SENSE-* class | External / hybrid sense when required | Often aggregated |
| Fault-energy containment | Integrated clamp/limit + P4 | Integrated limited | External CH-PROT + P2 | Coordinated | Shared clamp risk |
| Thermal concentration | Per-device | Per-device | Layout-dominated | Split | Highest coupling risk |
| PCB dependence | Package/copper TBD (OI-PCB-001) | Same | High | High | Very high |
| Controller-interface burden | SPI/diag pins or status | Lower pin count | GPIO/PWM + sense ADC | Mixed | Shared SPI bus contention |
| Common-cause exposure | Per channel | Per channel | Per channel | Moderate | **Elevated** (shared die/rail) |

## 6. Comparison table (normative summary)

| Class | Capability coverage | Safe-state compatibility | Diagnostics | Current observation | PWM suitability | Protection model | Thermal model | Integration burden | Main blockers | Qualification status |
|-------|---------------------|--------------------------|-------------|---------------------|-----------------|------------------|---------------|--------------------|---------------|----------------------|
| **HS-INT-DIAG** | BASE+PWM; SENSE/PROTECTED when claimed | Compatible with KILL / `nENABLE_GLOBAL` if hardwired disable preserved | Strong | Integrated and/or hybrid when required | High if class PWM-rated | Integrated P4 + coord with P2 | Per-channel; R_TH Open | Moderate | ED-IN-002/010/026; TBD thermal; ADR-DK-011 | **CLASS_CONDITIONALLY_VIABLE** — recommend for SENSE/PROTECTED instances |
| **HS-INT-BASIC** | BASE and/or PWM on mapped instances | Compatible if hard disable | Weak on this instance | Incomplete for SENSE on this instance | Medium | Integrated limited | Per-channel | Low–moderate | Must map SENSE/PROTECTED elsewhere | **CLASS_CONDITIONALLY_VIABLE** for BASE/PWM-only instances |
| **HS-GATE-DISCRETE** | Full if sense+prot added | Compatible if gate default OFF + KILL path | Designer-defined | External SENSE-* required | High with careful timing | External / hybrid CH-PROT | Layout-sensitive | High | ED-IN-030; OI-SENSE-001; schematic complexity | **CLASS_CONDITIONALLY_VIABLE** — retain fallback |
| **HS-HYBRID** | Full with external element/sense | Compatible if enable chain hardwired | Strong when hybrid sense | External / hybrid when required | High | Hybrid P4 | Split loss paths | High | Same + external FET thermal | **CLASS_CONDITIONALLY_VIABLE** |
| **HS-ARRAY** | Multi-role possible on shared silicon | Compatible only if array-wide hard disable proven | Often aggregated | Often limited per ch | Medium–high | Shared protection common-cause | Coupled | Moderate pin, high thermal analysis | Common-cause; OI-CHAN-001; thermal coupling | **CLASS_CONDITIONALLY_VIABLE** — retain |

## 7. Recommendations (Implementation Engineer — not Accepted)

| Class | Recommendation | Conditions |
|-------|----------------|------------|
| **HS-INT-DIAG** | **RECOMMENDED_FOR_NEXT_STAGE** | For physical instances **claiming CH-HS-SENSE and/or CH-HS-PROTECTED**, subject to PWM, diagnostic, and thermal qualification; hardwired KILL preserved; OL only if claimed (PWR-A-010); numerics Open |
| **HS-INT-BASIC** | **CONDITIONALLY_RECOMMENDED** | For physical instances claiming **only CH-HS-BASE and/or CH-HS-PWM**, provided mandatory SENSE/PROTECTED capabilities are implemented and **independently verified** on other mapped physical instances |
| **HS-HYBRID** | **CONDITIONALLY_RECOMMENDED** | Where external sense, protection, or power elements are required |
| **HS-GATE-DISCRETE** | **RETAIN_FOR_COMPARISON** | Fallback class requiring explicit external sense and protection functions |
| **HS-ARRAY** | **RETAIN_FOR_COMPARISON** | Subject to common-cause, diagnostic granularity, and thermal-coupling evaluation |

**Population rule:** Do **not** prescribe one class for all physical channels. Architect accepts **role-to-instance mapping**, not a single universal HS class.

`RECOMMENDED_FOR_NEXT_STAGE` means class evaluation may continue — **not** Architecture class Accepted, **not** MPN, **not** procurement, **not** schematic/PCB.

## 8. Rejected assumptions

| Assumption | Disposition |
|------------|-------------|
| One HS class must implement every capability alias on every physical channel | **Rejected** — WP-010 role mapping |
| Any HS class automatically satisfies open-load | **Rejected** — PWR-A-010 conditional |
| Fuse / integrated limit = `I_certified_cont` | **Rejected** — PWR-A-016 |
| Software OFF = hardware protection | **Rejected** — aligns PWR-A-018 (PROPOSED_CONSTRAINT) |
| Historical part numbers are candidates | **Rejected** — HISTORICAL / NON-NORMATIVE CONTEXT only |
| Class recommendation = MPN authorization | **Rejected** — WP-012 Stage [D]/[E] gates |
| HS-INT-BASIC rejected solely because another instance must provide SENSE/PROTECTED | **Rejected** — that mapping is Allowed under WP-010 |

## 9. Traceability

REQ-DCC-V-DK-039…049 · ADR-019 · WP-010 aliases · ED-IN-030 · OI-COMP-001 · PWR-A-004/005/008/010/016 · WP-011 HS dimensions · WP-012 / WP-013-R1 loss methods.

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial high-side class comparison — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — capability-role mapping; HS-INT-BASIC conditional; no universal primary class |
