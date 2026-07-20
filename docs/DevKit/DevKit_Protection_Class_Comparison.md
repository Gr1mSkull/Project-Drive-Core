# DevKit Protection Class Comparison — WP-013

**Document ID:** DOC-DK-PCC-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20

```text
Protection philosophy comparison — no fuse type, clamp voltage, rating, or MPN Approved.
Layers P0–P5 remain distinct (WP-012).
```

## 1. Purpose

Compare protection architecture classes for reverse-polarity, input transient, replaceable input, and channel protection. Coordinate with Accepted P0–P5 hierarchy. Owners: **OI-PROT-001**, **OI-PROT-002**, ED-IN-008/009/027.

## 2. Layer reminder (non-interchangeable)

| Layer | Name | Shall not substitute for |
|-------|------|--------------------------|
| P0 | Source-side limitation | DevKit input or channel protection |
| P1 | Fixture protection | DevKit P2–P5 |
| P2 | DevKit input protection | Channel-local P4 |
| P3 | Domain protection | Entry P2 |
| P4 | Channel-local protection | Input replaceable device alone |
| P5 | Functional safe-state control | Hardware energy limiting |

PWR-A-017 (**ACCEPTED_CONSTRAINT** — WP-012 protection framework + WP-014 Architecture Review disposition): PSU current limiting is not the sole protection layer. No component, fuse, current, or clearing time approved. 
PWR-A-016: Fuse nominal ≠ continuous certification.

## 3. Reverse-polarity classes

| Class | Protected boundary | Energy source | Conduction-loss model | Fault-energy model | Response dependency | Backup layer | Diagnostics | Reset/retry | Single-point failure | KILL interaction | Source limiting | Required data | Fixture | Unresolved |
|-------|-------------------|---------------|----------------------|--------------------|---------------------|--------------|-------------|-------------|----------------------|------------------|-----------------|---------------|---------|------------|
| **RP-SERIES-PASSIVE** | Entry (P2) | Reverse V_IN | Series diode/drop | Limited reverse energy | Passive | P0/P1 | Polarity sense optional | N/A | Series device fail short | Independent of KILL | Complements P0 | Vf, I_cont, surge | Reverse polarity fixture | **OI-PROT-001** |
| **RP-ACTIVE-IDEAL** | Entry (P2) | Reverse V_IN | Low R_DS(on) ideal diode | Active control energy | Active controller/FET | Passive or clamp | Status optional | Recovery policy Open | Control/FET fail | Must not defeat KILL | Complements P0 | FET/ctrl class data | Same | **OI-PROT-001** |
| **RP-RELAY-CONTACT** | Entry (P2) | Reverse V_IN | Contact R | Mechanical energy | Coil control | Series passive optional | Contact sense | Mechanical life | Contact weld | Independent if series | Complements P0 | Contact rating | Same | **OI-PROT-001** |
| **RP-HYBRID** | Entry (P2) | Reverse V_IN | Combined | Combined | Multi-path | Dual path | Richer | Policy Open | Reduced if diverse | Must not defeat KILL | Complements P0 | Dual class data | Same | **OI-PROT-001** |

**Status:** All RP classes **BLOCKED_BY_ARCHITECTURE** until OI-PROT-001 direction Accepted. Comparison permitted; selection not.

| Class | Qualification status | Recommendation |
|-------|----------------------|----------------|
| RP-SERIES-PASSIVE | BLOCKED_BY_ARCHITECTURE | **RETAIN_FOR_COMPARISON** — simple; loss penalty |
| RP-ACTIVE-IDEAL | BLOCKED_BY_ARCHITECTURE | **CONDITIONALLY_RECOMMENDED** — if Architect accepts active RP with hard fail-safe |
| RP-RELAY-CONTACT | BLOCKED_BY_ARCHITECTURE | **NOT_RECOMMENDED** for primary DevKit RP (mechanical latency / weld risk) unless Architect requires galvanic break |
| RP-HYBRID | BLOCKED_BY_ARCHITECTURE | **RETAIN_FOR_COMPARISON** |

## 4. Input transient protection classes

| Class | Boundary | Energy source | Loss model | Fault-energy | Backup | Diagnostics | KILL | Unresolved | Status |
|-------|----------|---------------|------------|--------------|--------|-------------|------|------------|--------|
| **TRANSIENT-CLAMP** | P2 entry | Surge / load dump class energy | Clamp leakage | Clamp absorbs E_FAULT | P0/P1 | Optional | Independent | **OI-PROT-002** | BLOCKED_BY_ARCHITECTURE / COMPONENT |
| **TRANSIENT-DISCONNECT** | P2 | Same | Low steady | Disconnect interrupts | Clamp optional | Status | Must not defeat KILL | OI-PROT-002 | Same |
| **TRANSIENT-CLAMP-DISCONNECT** | P2 | Same | Combined | Clamp then/or disconnect | Dual | Status | Same | OI-PROT-002 | Same |
| **TRANSIENT-MULTISTAGE** | P2 (+ fixture) | Staged energy | Staged | Coordinated stages | P0/P1/P2 | Richer | Same | OI-PROT-002; fixture | Same |

| Class | Recommendation |
|-------|----------------|
| TRANSIENT-CLAMP | **RETAIN_FOR_COMPARISON** |
| TRANSIENT-DISCONNECT | **RETAIN_FOR_COMPARISON** |
| TRANSIENT-CLAMP-DISCONNECT | **CONDITIONALLY_RECOMMENDED** — preferred direction if Architect wants coordinated energy absorb + interrupt |
| TRANSIENT-MULTISTAGE | **CONDITIONALLY_RECOMMENDED** — when fixture (P1) and DevKit (P2) roles explicitly partitioned |

No clamp voltage Approved.

## 5. Replaceable input protection classes

| Class | Boundary | Role vs continuous | Loss | Fault-energy | Backup | Diagnostics | Reset | Vs PWR-A-016 | Status |
|-------|----------|-------------------|------|--------------|--------|-------------|-------|--------------|--------|
| **INPUT-FUSE** | P2 | Replaceable interrupt — **≠** `I_certified_cont` | Low | Melting integral | Electronic optional | Continuity | Manual replace | Enforced | NOT_READY (ED-IN-008 Open) |
| **INPUT-BREAKER** | P2 | Resettable interrupt | Low | Trip curve | Same | Status | Reset policy | Enforced | NOT_READY |
| **INPUT-ELECTRONIC-LIMIT** | P2 | Electronic limit / disconnect | Quiescent + R | Controlled limiting | Fuse backup optional | Rich | Retry/latch Open | Must not self-cert continuous | NOT_READY |
| **INPUT-HYBRID** | P2 | Fuse + electronic | Combined | Coordinated | Dual | Rich | Combined | Preferred discipline | **CLASS_CONDITIONALLY_VIABLE** |

| Class | Recommendation |
|-------|----------------|
| INPUT-FUSE | **CONDITIONALLY_RECOMMENDED** as replaceable layer — rating Open (ED-IN-008) |
| INPUT-BREAKER | **RETAIN_FOR_COMPARISON** |
| INPUT-ELECTRONIC-LIMIT | **CONDITIONALLY_RECOMMENDED** — not sole continuous certification |
| INPUT-HYBRID | **RECOMMENDED_FOR_NEXT_STAGE** (philosophy) — fuse≠continuous; electronic≠sole; coordination with P0–P2 |

## 6. Channel protection classes

| Class | Boundary | Energy | Loss | Fault-energy | Backup | Diagnostics | Retry/latch | SPF | KILL | Source limit | Data | Fixture | Unresolved |
|-------|----------|--------|------|--------------|--------|-------------|-------------|-----|------|--------------|------|---------|------------|
| **CH-INTEGRATED-PROTECTION** | P4 | Channel fault | Device | Integrated clearing | P2/P5 | Device flags | Device + firmware policy Open | Device | Hard disable required | Complements | Class SOA | SC inject (OI-SC-001) | ED-IN-021 |
| **CH-EXTERNAL-HARDWARE** | P4 | Channel fault | External | Comparator/HW path | Integrated optional | External | Policy Open | Discrete path | Hard disable | Complements | Discrete data | Same | OI-COMP-001 |
| **CH-HYBRID-PROTECTION** | P4 | Channel fault | Combined | Coordinated | Dual | Dual | Policy Open | Reduced if diverse | Hard disable | Complements | Dual | Same | Same |

| Class | Qualification status | Recommendation |
|-------|----------------------|----------------|
| CH-INTEGRATED-PROTECTION | CLASS_CONDITIONALLY_VIABLE | **CONDITIONALLY_RECOMMENDED** with HS-INT-DIAG |
| CH-EXTERNAL-HARDWARE | CLASS_CONDITIONALLY_VIABLE | **RETAIN** — pairs with HS-GATE-DISCRETE |
| CH-HYBRID-PROTECTION | CLASS_CONDITIONALLY_VIABLE | **RECOMMENDED_FOR_NEXT_STAGE** when independence of diagnostic/protection path required |

## 7. Symbolic fault energy (class-agnostic)

```text
E_FAULT =
∫ V(t) × I(t) dt
```

Conservative bound form (conditional):

```text
E_FAULT_BOUND =
V_BOUND × I_BOUND × T_BOUND
```

Conservative **only when** `|V(t)| ≤ V_BOUND`, `|I(t)| ≤ I_BOUND`, and fault duration ≤ `T_BOUND` over the declared boundary/interval. If bounds are not established: **BLOCKED_BY_INPUT**.

**Prohibited:** presenting `V_nom × I_FAULT_PEAK × T_FAULT_CLEAR` as a conservative bound without proven upper-bound justification.

Required inputs remain Open: ED-IN-009 (`I_psc`), ED-IN-021, TBD-DK-011 — numeric/bound closure **BLOCKED_BY_INPUT**.

**OI-PROT-001** and **OI-PROT-002** remain **Open** in WP-013-R1.

## 8. Traceability

WP-012 protection framework · ADR-021/023 · OI-PROT-001/002 · ED-IN-008/009/021/027 · PWR-A-016/017 · P0–P5.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial protection class comparison — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — fault-energy bound form; OI-PROT-001/002 remain Open |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #17 merged (`d1698a0` / `23bdb07`); methodology Accepted; final classes/topology Open; TBD-DK-007 BLOCKED unchanged |
