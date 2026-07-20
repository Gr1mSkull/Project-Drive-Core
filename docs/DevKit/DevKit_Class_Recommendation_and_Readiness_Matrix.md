# DevKit Class Recommendation and Readiness Matrix — WP-013

**Document ID:** DOC-DK-CRRM-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-013  
**Date:** 2026-07-20

```text
Recommendations are class-level only.
Recommendation ≠ Architecture Acceptance ≠ MPN qualification ≠ procurement ≠ schematic use.
```

## 1. Qualification status legend

| Status | Meaning |
|--------|---------|
| CLASS_METHOD_ACCEPTABLE | Comparison method applicable |
| CLASS_VIABLE | Technically viable pending inputs |
| CLASS_CONDITIONALLY_VIABLE | Viable under stated conditions |
| CLASS_RECOMMENDED_FOR_NEXT_STAGE | IE recommends Architect consider for next WP |
| CLASS_NOT_RECOMMENDED | Poor fit; retain reason |
| CLASS_REJECTED | Incompatible with Accepted requirement/constraint |
| BLOCKED_BY_* / NOT_READY | Cannot close recommendation |

Recommendation values: `RECOMMENDED_FOR_NEXT_STAGE` · `CONDITIONALLY_RECOMMENDED` · `RETAIN_FOR_COMPARISON` · `NOT_RECOMMENDED` · `REJECTED` · `BLOCKED`.

## 2. Master matrix

| Function | Evaluation class | Capability coverage | Main advantage | Main limitation | Required inputs | Architecture blockers | Qualification blockers | Symbolic calculation readiness | Recommendation | Architect action |
|----------|------------------|---------------------|----------------|-----------------|-----------------|----------------------|------------------------|--------------------------------|----------------|-------------------|
| High-side | **HS-INT-DIAG** | BASE+PWM+SENSE+PROTECTED | Integrated diag + protect | Accuracy/thermal Open | ED-IN-002/010/026/030 | OI-COMP-001 | Class data; thermal ADR-DK-011 | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept/reject preferred HS class |
| High-side | **HS-HYBRID** | Full with external element | Precision / power flexibility | Complexity | Same + external FET | OI-COMP-001 | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept as conditional primary/fallback |
| High-side | **HS-GATE-DISCRETE** | Full if sense+prot added | Design freedom | Integration burden | Same + SENSE/CH-PROT | OI-COMP-001; OI-SENSE-001 | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Permit as fallback? |
| High-side | **HS-ARRAY** | Multi-ch shared | Density | Common-cause / thermal couple | OI-CHAN-001; thermal | Common-cause policy | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Accept elevated common-cause? |
| High-side | **HS-INT-BASIC** | BASE+PWM; weak SENSE | Simplicity | Fails SENSE/PROTECTED intent | — | ADR-019 SENSE/PROTECTED | — | SYMBOLIC_READY | **NOT_RECOMMENDED** | Confirm rejection as primary |
| Current obs. | **SENSE-HYBRID** | CH-HS-SENSE + independence | Dual path | Dual cal | ED-IN-011/032 | OI-SENSE-001 | Accuracy Open | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept hybrid observation? |
| Current obs. | **SENSE-INTEGRATED** | Claim-limited SENSE | Low parts | Coupled; BW Open | ED-IN-011/032 | OI-SENSE-001 | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Sole path acceptable? |
| Current obs. | **SENSE-SHUNT-HS** | Precision I_LOAD | Independent | Loss/layout | Same | Same | PCB | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Fallback precision path? |
| Current obs. | **SENSE-MAGNETIC** | Isolated / BI-friendly | Isolation | Cal/fixture | Same | Fixture | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Use for isolated/P6? |
| Current obs. | **SENSE-SHUNT-LS** | LS path | Simple | Poor HS fault observation | — | Topology | — | SYMBOLIC_READY | **NOT_RECOMMENDED** | Confirm not primary HS |
| Current obs. | **SENSE-INDIRECT** | Estimate only | No shunt | Not independent VE path | — | Verification independence | — | SYMBOLIC_READY | **NOT_RECOMMENDED** | Confirm rejection as sole |
| RP | **RP-ACTIVE-IDEAL** | P2 reverse | Low loss | Active failure modes | OI-PROT-001 | **OI-PROT-001** | — | SYMBOLIC_READY | **BLOCKED** (arch) / conditional prefer | Resolve OI-PROT-001 |
| RP | **RP-SERIES-PASSIVE** | P2 reverse | Simple | Conduction loss | OI-PROT-001 | OI-PROT-001 | — | SYMBOLIC_READY | **BLOCKED** / RETAIN | Resolve OI-PROT-001 |
| RP | **RP-RELAY-CONTACT** | Galvanic break | Isolation | Weld/latency | OI-PROT-001 | OI-PROT-001 | — | SYMBOLIC_READY | **NOT_RECOMMENDED** primary | Confirm |
| RP | **RP-HYBRID** | Diverse | Redundancy | Complexity | OI-PROT-001 | OI-PROT-001 | — | SYMBOLIC_READY | **BLOCKED** / RETAIN | Resolve OI-PROT-001 |
| Transient | **TRANSIENT-CLAMP-DISCONNECT** | P2 surge | Absorb + interrupt | Coordination design | OI-PROT-002 | OI-PROT-002 | Waveform Open | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept direction? |
| Transient | **TRANSIENT-MULTISTAGE** | P1+P2 staged | Fixture/DevKit split | Fixture dependency | OI-PROT-002; fixture | Same | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept staging? |
| Transient | **TRANSIENT-CLAMP** | Clamp only | Simple | Energy share Open | OI-PROT-002 | OI-PROT-002 | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Transient | **TRANSIENT-DISCONNECT** | Interrupt only | Limits clamp stress | Needs backup absorb | OI-PROT-002 | OI-PROT-002 | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Replaceable input | **INPUT-HYBRID** | P2 replaceable+electronic | Enforces fuse≠continuous | Dual design | ED-IN-008 | — | Rating Open | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept philosophy? |
| Replaceable input | **INPUT-FUSE** | Replaceable | Simple | Rating Open; ≠ continuous | ED-IN-008 | — | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | — |
| Replaceable input | **INPUT-ELECTRONIC-LIMIT** | Electronic | Controllable | ≠ sole continuous cert | ED-IN-008 | PWR-A-016 | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | — |
| Replaceable input | **INPUT-BREAKER** | Resettable | Serviceable | Trip curve Open | ED-IN-008 | — | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Channel prot. | **CH-HYBRID-PROTECTION** | P4 dual | Independence | Complexity | ED-IN-021 | OI-SC-001 | — | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept split? |
| Channel prot. | **CH-INTEGRATED-PROTECTION** | P4 integrated | Fits HS-INT-DIAG | Coupled to switch | Same | — | — | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | With HS-INT-DIAG |
| Channel prot. | **CH-EXTERNAL-HARDWARE** | P4 external | Fits discrete HS | Parts count | Same | — | — | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | With HS-GATE-DISCRETE |
| Bidirectional | **BI-HB-HYBRID** | CH-BI-REP | Envelope flexibility | Complexity | ED-IN-020/031; OI-BI-001 | OI-BI-001 | Stall fixture | PROVISIONAL_INPUT_REQUIRED | **RECOMMENDED_FOR_NEXT_STAGE** if FET needed | Accept BI direction |
| Bidirectional | **BI-HB-FULL** | CH-BI-REP | Integration | Rating/thermal Open | Same | Same | Same | PROVISIONAL_INPUT_REQUIRED | **CONDITIONALLY_RECOMMENDED** | Prefer if ratings cover |
| Bidirectional | **BI-HB-DISCRETE** | CH-BI-REP | Freedom | Layout/dead-time | Same | Same | Same | PROVISIONAL_INPUT_REQUIRED | **RETAIN_FOR_COMPARISON** | Fallback? |
| Bidirectional | **BI-DUAL-HSLS** | CH-BI-REP | Explicit rails | Interlock proof | Same | OI-BI-001 | Same | PROVISIONAL_INPUT_REQUIRED | **RETAIN_FOR_COMPARISON** | — |
| Bidirectional | **BI-RELAY-REVERSING** | Weak PWM BI | Simple polarity | Poor dynamic/PWM/stall | — | ADR-019 dynamic BI | — | NOT_READY for PWM BI | **NOT_RECOMMENDED** | Confirm rejection |
| Controller IF | **CTRL-MIXED-HARDWIRED** | KILL HW + SPI cmd | Preserves PWR-A-004 | Design care | TBD-DK-007 semantics | OI-EDL-011 numeric | CTRL timing Open | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept IF pattern |
| Controller IF | **CTRL-SPI-MCU** | Power MCU slave | Flexible | Must not own KILL | Same | Same | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | MCU allowed if KILL hardwired |
| Controller IF | **CTRL-SPI-SAFETY** | Safety-oriented SPI | Structured diag | SPI ≠ physical KILL | Same | Same | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | SPI for cmd/diag only |
| Controller IF | **CTRL-DIRECT-GPIO** | Direct pins | Simple | Limited for rich Power | — | — | — | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Aux channels only? |

## 3. Conditional recommendation register

| Class | Exact conditions |
|-------|------------------|
| HS-INT-DIAG | Hardwired KILL disable; PWM claim covers CH-HS-PWM; diag covers SENSE/PROTECTED; OL only if claimed |
| HS-HYBRID | Used when integrated device cannot meet envelope/precision; external element thermal modelled |
| SENSE-HYBRID | Precision path class-defined; integrated path for protection flags; referral model documented |
| SENSE-INTEGRATED sole | Architect accepts claim-limited accuracy/BW for DK-C-004 |
| TRANSIENT-CLAMP-DISCONNECT | P0/P1/P2 energy share declared; clamp voltage remains Open until Architect |
| INPUT-HYBRID | Fuse rating ≠ `I_certified_cont`; electronic not sole continuous certification |
| CH-HYBRID-PROTECTION | Diverse path from switch die for critical SC cases where required |
| BI-HB-FULL / HYBRID | Shoot-through prevention architecture declared (OI-BI-001); stall fixture defined before numeric |
| CTRL-SPI-* | Physical KILL remains direct hardware-effective; `nENABLE_GLOBAL` separate |

## 4. Rejected / not-recommended with traceable reasons

| Class | Disposition | Reason |
|-------|-------------|--------|
| HS-INT-BASIC as primary | NOT_RECOMMENDED | Insufficient for mandatory CH-HS-SENSE / CH-HS-PROTECTED (ADR-019) without becoming hybrid |
| SENSE-SHUNT-LS as primary HS | NOT_RECOMMENDED | Does not observe HS path under many fault conditions |
| SENSE-INDIRECT as sole | NOT_RECOMMENDED | Lacks independent physical observation for verification |
| BI-RELAY-REVERSING as primary CH-BI-REP | NOT_RECOMMENDED | Weak PWM/dynamic bidirectional verification fit |
| RP-RELAY-CONTACT as primary RP | NOT_RECOMMENDED | Mechanical latency/weld risk vs DevKit RP needs (Architect may override) |
| Any class → MPN | REJECTED assumption | WP-012 Stage [D]/[E]; CR-001 |
| Cost-only safety architecture | REJECTED | Constitution / safety ownership |

## 5. Architect decision list (prepared)

1. Preferred high-side class?  
2. Permitted fallback high-side class?  
3. Preferred current-observation class or hybrid?  
4. Reverse-polarity architecture direction (OI-PROT-001)?  
5. Transient-protection architecture direction (OI-PROT-002)?  
6. Replaceable-protection philosophy?  
7. Channel-protection responsibility split?  
8. Bidirectional architecture direction?  
9. Controller-interface class direction?  
10. Authorization level for next WP?

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial class recommendation and readiness matrix — Proposed |
