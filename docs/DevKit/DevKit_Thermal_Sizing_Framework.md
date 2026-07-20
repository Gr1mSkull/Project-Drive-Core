# DevKit Thermal Sizing Framework — WP-012

**Document ID:** DOC-DK-TSF-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20

```text
Thermal METHODOLOGY only — no temperature limit Approved.
R_TH_EFFECTIVE cannot be frozen before package, copper, board, enclosure and airflow exist.
```

## 1. Purpose

Define thermal path, loss sources, operating states, symbolic relationships, and closure dependencies for DevKit sizing. Supports future ADR-DK-011 resolution without approving numeric limits.

## 2. Thermal path

```text
electrical loss source (P_LOSS)
  → semiconductor junction or dissipating element (T_j or T_element)
  → package
  → local copper / board structure
  → PCB
  → enclosure or free air
  → ambient environment (T_AMBIENT)
```

## 3. Loss sources

| Source | Symbolic term | Domain | Notes |
|--------|---------------|--------|-------|
| Conduction loss | `P_CONDUCTION` | Channel | I²R or device-specific (alternative method) |
| Switching loss | `P_SWITCHING` | Channel PWM | Function of `f_PWM`, duty — TBD-DK-008 Open |
| Conversion loss | `P_CONV_*` | Logic/Radio rails | Regulator efficiency unknown |
| Sense-resistor loss | `P_SENSE` | Channel / input | If shunt class selected |
| Conductor loss | `P_CU` | Input / distribution | PCB + harness — layout dependent |
| Connector loss | `P_CONN` | Entry / outputs | Contact resistance — ADR-DK-012 Open |
| Protection-device loss | `P_PROT` | Input / channel | Fuse/hold; trip-dependent |
| Rail-converter loss | `P_RAIL` | Domain rails | Buck/LDO TBD |
| Transient energy averaged | `P_TRANSIENT_AVG` | Fault/retry | From `E_FAULT` / duty |

## 4. Thermal coupling and environment

| Factor | Status | Blocker |
|--------|--------|---------|
| Thermal coupling between channels | Method: concurrent heating in P4 | OI-PCB-001; layout |
| Simultaneous-load heating | Profile P3/P4 | TBD-DK-003 Open |
| Enclosure influence | OPEN_ASSUMPTION | ADR-DK-012 |
| Ambient temperature | `T_AMBIENT` — Open | ADR-DK-011 |
| Airflow assumptions | OPEN_ASSUMPTION | ADR-DK-011 |
| Mounting orientation | OPEN_ASSUMPTION | Enclosure WP |
| Duty cycle | Per profile D_n | WP-012 budget model |
| Soak duration | `t_thermal_test` | ED-IN-016; TBD-DK-018 Open |
| Thermal margin | Category defined; no % | Margin framework |

## 5. Thermal model states

| State | Losses considered | Active domains | Duration dependency | Blocked inputs | Future simulation | Future measurement |
|-------|-------------------|----------------|---------------------|----------------|-------------------|-------------------|
| **Cold startup** | Inrush + rail seq | Logic, Radio | Short | Rail seq Open | Optional | P1 rails |
| **Nominal ambient steady** | Steady P_CHANNEL + P_DOMAIN | Per P3 | Soak Open | T_amb; T_max Open | Required before freeze | DK-C thermal |
| **High ambient steady** | Derated currents | Per P3 | Soak Open | ADR-DK-011 | Required | Environmental chamber |
| **Single-channel continuous** | One channel max loss | 1 channel | Continuous Open | I_CHANNEL_CONT Open | Required | Channel thermal MP |
| **Multi-channel overlap** | Σ coupled losses | P4 profile | Profile T | TBD-DK-003 | Required | P4 trace + thermal |
| **PWM operation** | P_SWITCHING dominant | PWM channel | Duty + f_PWM | TBD-DK-008 | Required | Scope + thermal |
| **Fault/retry cycling** | E_FAULT averaged | P5 | t_fault; retry | TBD-DK-013 | Required | Fault capture |
| **External-bank bounded test** | Fixture-separated | P6 | Fixture | OI-GND-001 | Fixture model | Fixture qual |
| **Thermal soak** | All steady losses | Certified profile | TBD-DK-018 | Duration Open | Required | Soak test |
| **Post-fault cooldown** | Decay only | After P5 | Cooldown Open | Retry policy | Optional | IR camera / sensor |

## 6. Symbolic thermal relationships

```text
T_RISE = P_LOSS × R_TH_EFFECTIVE
```

```text
T_ELEMENT = T_AMBIENT + T_RISE
```

```text
R_TH_EFFECTIVE = f(R_th_junction, R_th_board, R_th_enclosure, airflow, coupling)
```

**Statement:** `R_TH_EFFECTIVE` **cannot be frozen** before package selection, copper geometry, board structure, enclosure, and airflow assumptions exist.

**Prohibited:** universal application of datasheet junction-to-ambient (`RθJA`) as board-level truth without board-specific validation.

### 6.1 Current derating (symbolic — WP-009 carry-forward)

```text
I_PCB_cont(T) = I_PCB_cont(T_ref) × sqrt((T_max - T)/(T_max - T_ref))
```

Exact form requires copper geometry — **BLOCKED_BY_PCB_DESIGN** until layout exists.

## 7. Thermal observation

| Input | ED-IN | Status |
|-------|-------|--------|
| Temperature measurement accuracy | ED-IN-012; TBD-DK-010 | Open |
| Thermal test duration | ED-IN-016; TBD-DK-018 | Open |
| Maximum safe temperature | ED-IN-017; TBD-DK-019 | Open |
| Environment split | ADR-DK-011 | BLOCKED_BY_ARCHITECTURE |

## 8. Readiness summary

| Item | Readiness |
|------|-----------|
| Thermal path definition | METHOD_ACCEPTABLE |
| Operating state catalog | METHOD_ACCEPTABLE |
| Symbolic equations | SYMBOLIC_CONSTRAINT_ACCEPTABLE |
| Numeric T_max / T_amb | BLOCKED_BY_THRESHOLD |
| R_th values | BLOCKED_BY_COMPONENT_SELECTION + BLOCKED_BY_PCB_DESIGN |
| Simulation evidence | NOT_READY |
| Measurement evidence | BLOCKED_BY_MEASUREMENT |

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial thermal sizing framework — Proposed |
