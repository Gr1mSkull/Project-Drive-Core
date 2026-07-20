# DevKit Class Recommendation and Readiness Matrix — WP-013

**Document ID:** DOC-DK-CRRM-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20

```text
Recommendations are class-level evaluation directions.
Architecture Review acceptance of WP-013 accepts the comparison framework and conditional directions.
It does not convert conditional recommendations into final component-class selections.
Recommendation ≠ Final class selection ≠ MPN qualification ≠ procurement ≠ schematic use.
RECOMMENDED_FOR_NEXT_STAGE = evaluation may continue — not class Accepted for every physical channel.
OI-PROT-001 / OI-PROT-002 remain Open.
OI-COMP-001/002 · OI-SENSE-001 · OI-BI-001 remain Open.
TBD-DK-007 remains BLOCKED_BY_EDL_CLARIFICATION.
Numeric values remain Open.
```

## 1. Qualification status legend

| Status | Meaning |
|--------|---------|
| CLASS_METHOD_ACCEPTABLE | Comparison method applicable |
| CLASS_VIABLE | Technically viable pending inputs |
| CLASS_CONDITIONALLY_VIABLE | Viable under stated conditions |
| CLASS_RECOMMENDED_FOR_NEXT_STAGE | IE recommends Architect permit continued evaluation |
| CLASS_NOT_RECOMMENDED | Poor fit for stated role; retain reason |
| CLASS_REJECTED | Incompatible with Accepted requirement/constraint |
| BLOCKED_BY_* / NOT_READY | Cannot close recommendation |

Recommendation values: `RECOMMENDED_FOR_NEXT_STAGE` · `CONDITIONALLY_RECOMMENDED` · `RETAIN_FOR_COMPARISON` · `NOT_RECOMMENDED` · `REJECTED` · `BLOCKED`.

## 2. Master matrix

| Function | Evaluation class | Capability coverage | Main advantage | Main limitation | Required inputs | Architecture blockers | Qualification blockers | Symbolic calculation readiness | Recommendation | Architect action |
|----------|------------------|---------------------|----------------|-----------------|-----------------|----------------------|------------------------|--------------------------------|----------------|-------------------|
| High-side | **HS-INT-DIAG** | SENSE and/or PROTECTED instances (+ BASE/PWM as claimed) | Integrated diag + protect | Accuracy/thermal Open | ED-IN-002/010/026/030 | OI-COMP-001 | Class data; thermal ADR-DK-011 | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** (role-mapped instances) | Accept role mapping? |
| High-side | **HS-INT-BASIC** | BASE and/or PWM only on mapped instances | Simplicity | No SENSE/PROTECTED on this instance | ED-IN-030; role map | OI-COMP-001; OI-CHAN-001 | Must map SENSE/PROTECTED elsewhere | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept BASE/PWM-only use? |
| High-side | **HS-HYBRID** | External sense/prot/power as needed | Flexibility | Complexity | Same + external FET | OI-COMP-001 | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept when external elements needed? |
| High-side | **HS-GATE-DISCRETE** | Full if sense+prot added | Design freedom | Integration burden | Same + SENSE/CH-PROT | OI-COMP-001; OI-SENSE-001 | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Permit as fallback? |
| High-side | **HS-ARRAY** | Multi-role possible; shared silicon | Density | Common-cause / thermal couple | OI-CHAN-001; thermal | Common-cause policy | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Accept elevated common-cause? |
| Current obs. | **SENSE-INTEGRATED** | Diag/protect observation when claims fit role | Low parts | Coupled; BW Open | ED-IN-011/032 | OI-SENSE-001 | Accuracy Open | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept for diag/protect role? |
| Current obs. | **SENSE-HYBRID** | When independence/accuracy required | Dual path | Dual cal; inputs Open | ED-IN-011/032 | OI-SENSE-001 | Accuracy Open | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** (not unconditional preferred) | Require hybrid when? |
| Current obs. | **SENSE-SHUNT-HS** | Precision I_LOAD | Independent | Loss/layout | Same | Same | PCB | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Precision class? |
| Current obs. | **SENSE-MAGNETIC** | Isolated / BI / external envelope | Isolation | Cal/fixture | Same | Fixture | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | Use for isolated/P6? |
| Current obs. | **SENSE-SHUNT-LS** | Not primary HS path | Simple | Poor HS fault observation | — | Topology for HS-primary | — | SYMBOLIC_READY | **NOT_RECOMMENDED** as primary HS (not global reject) | Confirm scope |
| Current obs. | **SENSE-INDIRECT** | Estimate only | No shunt | Not sole VE path | — | Verification independence | — | SYMBOLIC_READY | **NOT_RECOMMENDED** as sole verification | Confirm rejection |
| RP | **RP-ACTIVE-IDEAL** | P2 reverse | Low loss | Active failure modes | OI-PROT-001 | **OI-PROT-001 Open** | — | SYMBOLIC_READY | **BLOCKED** (arch) / retain if opened | Resolve OI-PROT-001 |
| RP | **RP-SERIES-PASSIVE** | P2 reverse | Simple | Conduction loss | OI-PROT-001 | OI-PROT-001 Open | — | SYMBOLIC_READY | **BLOCKED** / RETAIN | Resolve OI-PROT-001 |
| RP | **RP-RELAY-CONTACT** | Galvanic break | Isolation | Weld/latency | OI-PROT-001 | OI-PROT-001 Open | — | SYMBOLIC_READY | **NOT_RECOMMENDED** primary | Confirm |
| RP | **RP-HYBRID** | Diverse | Redundancy | Complexity | OI-PROT-001 | OI-PROT-001 Open | — | SYMBOLIC_READY | **BLOCKED** / RETAIN | Resolve OI-PROT-001 |
| Transient | **TRANSIENT-CLAMP-DISCONNECT** | P2 surge | Absorb + interrupt | Coordination design | OI-PROT-002 | **OI-PROT-002 Open** | Waveform Open | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept direction? |
| Transient | **TRANSIENT-MULTISTAGE** | P1+P2 staged | Fixture/DevKit split | Fixture dependency | OI-PROT-002; fixture | OI-PROT-002 Open | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | Accept staging? |
| Transient | **TRANSIENT-CLAMP** | Clamp only | Simple | Energy share Open | OI-PROT-002 | OI-PROT-002 Open | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Transient | **TRANSIENT-DISCONNECT** | Interrupt only | Limits clamp stress | Needs backup absorb | OI-PROT-002 | OI-PROT-002 Open | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Replaceable input | **INPUT-HYBRID** | P2 replaceable+electronic | Enforces fuse≠continuous | Dual design | ED-IN-008 | — | Rating Open | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept philosophy? |
| Replaceable input | **INPUT-FUSE** | Replaceable | Simple | Rating Open; ≠ continuous | ED-IN-008 | — | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | — |
| Replaceable input | **INPUT-ELECTRONIC-LIMIT** | Electronic | Controllable | ≠ sole continuous cert | ED-IN-008 | PWR-A-016 | Same | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | — |
| Replaceable input | **INPUT-BREAKER** | Resettable | Serviceable | Trip curve Open | ED-IN-008 | — | Same | SYMBOLIC_READY | **RETAIN_FOR_COMPARISON** | — |
| Channel prot. | **CH-HYBRID-PROTECTION** | P4 dual | Independence | Complexity | ED-IN-021 | OI-SC-001 | — | SYMBOLIC_READY | **RECOMMENDED_FOR_NEXT_STAGE** | Accept split? |
| Channel prot. | **CH-INTEGRATED-PROTECTION** | P4 integrated | Fits HS-INT-DIAG instances | Coupled to switch | Same | — | — | SYMBOLIC_READY | **CONDITIONALLY_RECOMMENDED** | With HS-INT-DIAG instances |
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
| HS-INT-DIAG | Instance claims SENSE and/or PROTECTED; hardwired KILL; PWM claim if PWM role; OL only if claimed |
| HS-INT-BASIC | Instance claims only BASE and/or PWM; SENSE/PROTECTED on other independently verified instances |
| HS-HYBRID | External sense, protection, or power element required |
| SENSE-INTEGRATED | Accuracy/BW/PWM/fault claims satisfy mapped verification role |
| SENSE-HYBRID | Accepted requirement demands accuracy, independence, cal separation, or diagnostic diversity |
| TRANSIENT-CLAMP-DISCONNECT | P0/P1/P2 energy share declared; clamp voltage remains Open; OI-PROT-002 still Open |
| INPUT-HYBRID | Fuse rating ≠ `I_certified_cont`; electronic not sole continuous certification |
| CH-HYBRID-PROTECTION | Diverse path from switch die for critical SC cases where required |
| BI-HB-FULL / HYBRID | Shoot-through prevention architecture declared (OI-BI-001); stall fixture before numeric |
| CTRL-SPI-* | Physical KILL remains direct hardware-effective; `nENABLE_GLOBAL` separate |

## 4. Rejected / not-recommended with traceable reasons

| Class | Disposition | Reason |
|-------|-------------|--------|
| One HS class for entire population | REJECTED assumption | WP-010 capability-role mapping |
| HS-INT-BASIC solely because SENSE/PROTECTED elsewhere | Not a valid rejection | WP-010 allows role distribution |
| SENSE-HYBRID as unconditional preferred | Corrected in R1 | ED-IN-011/032 / OI-SENSE-001 Open |
| SENSE-SHUNT-LS as primary HS | NOT_RECOMMENDED (not global reject) | Poor HS fault-path observation |
| SENSE-INDIRECT as sole | NOT_RECOMMENDED | Lacks independent physical observation |
| BI-RELAY-REVERSING as primary CH-BI-REP | NOT_RECOMMENDED | Weak PWM/dynamic bidirectional verification |
| RP-RELAY-CONTACT as primary RP | NOT_RECOMMENDED | Mechanical latency/weld risk (Architect may override) |
| Any class → MPN | REJECTED assumption | WP-012 Stage [D]/[E]; CR-001 |
| Cost-only safety architecture | REJECTED | Constitution / safety ownership |

## 5. Architect decision list (prepared)

1. Accept HS role-to-instance mapping (HS-INT-DIAG for SENSE/PROTECTED instances; HS-INT-BASIC for BASE/PWM-only)?  
2. Permitted fallback high-side classes (HYBRID / GATE-DISCRETE / ARRAY)?  
3. Accept observation **evaluation directions** (INTEGRATED conditional; HYBRID conditional — not preferred while inputs Open)?  
4. Reverse-polarity architecture direction (OI-PROT-001 — remains Open)?  
5. Transient-protection architecture direction (OI-PROT-002 — remains Open)?  
6. Accept INPUT-HYBRID replaceable-protection philosophy?  
7. Accept channel-protection responsibility split?  
8. Accept bidirectional architecture direction?  
9. Accept CTRL-MIXED-HARDWIRED interface pattern?  
10. Which next WP is authorized?

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial class recommendation and readiness matrix — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — role mapping; HS-INT-BASIC conditional; SENSE-HYBRID conditional; Open OI-PROT retained |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #17 merged (`d1698a0` / `23bdb07`); methodology Accepted; final classes/topology Open; TBD-DK-007 BLOCKED unchanged |
