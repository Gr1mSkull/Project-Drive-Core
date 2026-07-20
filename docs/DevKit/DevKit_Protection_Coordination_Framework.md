# DevKit Protection Coordination Framework — WP-012

**Document ID:** DOC-DK-PCF-001  
**Version:** 1.1  
**Status:** Ready for Final Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20

```text
Protection PHILOSOPHY and coordination methodology — no fuse value, device MPN or numeric curve Approved.
```

## 1. Purpose

Define distinct protection layers, fault classes, coordination principles, and symbolic fault-energy methodology for DevKit sizing. Layers **shall not** be treated as interchangeable.

## 2. Protection layers

| Layer | Name | Scope | Examples (class-level) | Not equivalent to |
|-------|------|-------|------------------------|-------------------|
| **P0** | Source-side limitation | Bench PSU / external source | Programmable `I_PSU_limit`; OV/OC foldback | Sole protection (principle 1) |
| **P1** | Fixture protection | Test fixture wiring and controls | Fixture fuse/breaker; E-stop; energy interlock | DUT channel protection |
| **P2** | DevKit input protection | Entry to base DevKit | Replaceable fuse/OCP; RP; transient clamp | Continuous current certification |
| **P3** | Domain protection | Logic/Radio/Power rails | Rail polyfuse/electronic limit | Channel SC containment alone |
| **P4** | Channel-local protection | Per output channel | Switch OC/SC; comparator disable | KILL / watchdog |
| **P5** | Functional safe-state control | System safety nets | KILL; `nENABLE_GLOBAL`; watchdog; control-loss; commanded OFF | Overcurrent protection |

## 3. Coordination principles

1. Bench PSU current limit is **not** the sole protection layer.
2. Fuse **nominal rating** is **not** continuous-current certification (`I_protection_rating` ≠ `I_certified_cont`).
3. **Interrupt rating** is **not** current rating.
4. Channel protection shall act before unacceptable upstream damage where selective containment is required.
5. Upstream protection shall remove energy where local containment fails.
6. Hardware KILL does **not** replace overcurrent protection.
7. Software shutdown does **not** replace hardware fault containment.
8. External-bank protection does **not** extend base DevKit rating.
9. Protection timing shall coordinate with conductor and component withstand.
10. Retry behaviour shall not create uncontrolled thermal accumulation.
11. Fault-energy calculations shall include source impedance and clearing time.
12. Unknown fault energy shall be treated **conservatively**.

## 4. Protection coordination model (symbolic)

```text
I_SOURCE_LIMIT          — P0
I_PROTECTION_NOMINAL    — P1/P2 nominal (≠ continuous)
I_PROTECTION_CLEAR(t)   — time-dependent clearing current
I_CONDUCTOR_WITHSTAND(t)
I_CONNECTOR_WITHSTAND(t)
I_PCB_WITHSTAND(t)
I_CHANNEL_LIMIT(t)      — P4
I_FAULT_PEAK
T_FAULT_CLEAR
E_FAULT
```

```text
E_FAULT = ∫ V(t) × I(t) dt
```

Conservative approximation when justified:

```text
E_FAULT ≈ V_nom × I_FAULT_PEAK × T_FAULT_CLEAR
```

**No protection curves defined numerically in WP-012.**

## 5. Fault class analysis (16 classes)

Table population: **16 fault classes** (§5.1).

| Fault class | Origin | Energy source | First layer | Backup layer | Safe minimum outcome | Diagnostic req | Latch/retry | Calculation needed | Component data | Measurement | Residual risk |
|-------------|--------|---------------|-------------|--------------|---------------------|----------------|-------------|-------------------|------------------|-------------|---------------|
| Input reverse polarity | Wrong connection | External source | P2 RP | P0 disconnect | No energization of DUT | Fault log if powered | Open | RP device class | RP MPN qual | Bench test | Fire if RP absent |
| Input OV transient | Source/load dump | External | P2 clamp | P0 foldback | No damage to P3/P4 | Capture event | Open | Clamp energy | TVS/clamp qual | Injection fixture | Downstream damage |
| Input undervoltage | Source dip | External | P3 UV reaction | P5 safe state | Defined de-energize | UV log | TBD-DK-012 Open | UV table | Rail monitor | DK-C-012 | Undefined resume |
| Input interruption | Supply removal | External | P5 decay | None | Safe OFF | Supply loss detect | Open | Decay model | Load types | DK-A/D | Unexpected restart |
| Input overcurrent | Aggregate overload | Source | P0 then P2 | P5 disable | No sustained heat | Input OC log | Open | I_certified_cont | Fuse curve | P3 profile | Harness damage |
| Input short circuit | Entry SC | Source | P0/P1/P2 | Physical disconnect | Energy bounded | SC capture | Open | I_psc, E_FAULT | Interrupt rating | P5 fixture | Arc / fire |
| Domain rail SC | Regulator failure | Rail cap | P3 | P2 upstream | Rail disabled | Rail fault | Open | I_rail_fault | Regulator qual | Rail MP | Domain loss |
| Channel overload | Excess load | Channel | P4 OC | P2 if sustained | Channel OFF | Channel fault | TBD-DK-013 | I_CHANNEL_CONT | Switch qual | DK-C-005 | Upstream trip |
| Channel hard SC | Output SC | Source+channel | P4 | P2/P1 | Energy limited | SC fault code | Open | E_FAULT channel | Switch I²t | TBD-DK-011 fixture | PCB damage |
| Inductive turn-off | Inductive load | Stored energy | P4 clamp/snub | Channel disable | Voltage bounded | Capture peak | Open | V_peak, E | Flyback/clamp | Inductive load | FET avalanche |
| BI shoot-through | Bridge overlap | Source | P4 topology | P5 disable | No cross-conduction | Direction fault | Open | Dead-time | Bridge class | OI-BI-001 | Thermal runaway |
| BI stalled load | Mechanical stall | Source | P4 current limit | P5 / fixture | Bounded stall current | Stall detect | TBD-DK-022 | Stall I, duration | BI class | Fixture | Heat damage |
| Thermal overload | Excess loss | Electrical | P4 thermal | P5 global | Channel/system OFF | Thermal fault | Open | P_LOSS, R_th | Thermal qual | DK-C thermal | Fire |
| External-bank back-feed | Wrong fixture | External | Fixture interlock | P2 isolation | No base energization | Interlock status | Open | Isolation proof | Fixture design | OI-GND-001 | Base damage |
| External-bank misconnection | Wiring error | External | P1/P6 interlock | Operator abort | No energy | Fixture check | Open | Procedure | Fixture qual | Phase E | Hazard |
| Measurement-ground fault | Scope/fixture GND | External | Fixture GND policy | Abort | No hazardous current | Procedure | Open | GND model | OI-GND-001 | Fixture WP | Measurement hazard |

## 6. Layer vs timing class (ADR-022 alignment)

| Mechanism | ADR-022 class | Protection layer | Numeric status |
|-----------|---------------|------------------|----------------|
| KILL | H | P5 | TBD-DK-004 Open |
| Watchdog | R | P5 | TBD-DK-005 Open |
| Control-loss | C | P5 | TBD-DK-007 BLOCKED_BY_EDL_CLARIFICATION |
| Commanded OFF | — | P5 | TBD-DK-014 Open |
| Channel OC | — | P4 | TBD-DK-002/013 Open |

## 7. Readiness

| Item | Readiness |
|------|-----------|
| Layer definitions P0–P5 | METHOD_ACCEPTABLE |
| Coordination principles | METHOD_ACCEPTABLE |
| Fault class catalog | METHOD_ACCEPTABLE |
| Fault-energy methodology | SYMBOLIC_CONSTRAINT_ACCEPTABLE |
| Device selection | BLOCKED_BY_COMPONENT_CLASS |
| Numeric clearing times | BLOCKED_BY_THRESHOLD / MEASUREMENT |

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial protection coordination framework — Proposed |
| 1.1 | 2026-07-20 | WP-012-R1 — explicit 16-class population count |
