# Thermal Validation

**Document ID:** CQP-TH-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define evidence required for thermal qualification of power-dissipating components.

## 2. Scope

Mandatory for: smart high-side switches, H-bridges, DC-DC regulators, linear regulators in power path, MCU if significant dissipation.

Optional with justification for: signal-level ICs, passives.

## 3. Responsibilities

Implementation Engineer gathers datasheet thermal data; thermal validation WP may require bench or simulation.

## 4. Inputs

- Datasheet: Rds(on), Rth, SOA, current vs temperature curves
- PCB assumptions: copper weight, area, ambient — from hardware design doc when available
- Load profile from requirement

## 5. Outputs

- **Thermal Characteristics** section in qualification report
- Pass/fail or TBD for junction temperature at application conditions

## 6. Required analysis elements

| Element | Source |
|---------|--------|
| Power dissipation model | P = I²×R, or datasheet graph |
| Thermal resistance network | Rth_j-c, Rth_c-a, interface |
| Ambient and max junction | Application limits |
| Simultaneous operation | Other devices on shared heatsink |
| Derating strategy | Firmware/hardware — reference only |

## 7. Evidence levels

| Level | Description |
|-------|-------------|
| L1 | Datasheet thermal parameters recorded only |
| L2 | Calculated T_j at stated assumptions |
| L3 | Bench thermocouple or IR measurement |
| L4 | CFD / thermal simulation on final PCB |

Minimum level per component class — **TBD** by architect per work package.

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Distinguishes datasheet record vs calculated vs measured |
| AC-2 | No invented Rth or T_j values |

## 9. Related documents

- [docs/002_DCC_Hardware.md](../002_DCC_Hardware.md) §7 (system thermal context)
- `hardware/qualification/high_side/`

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
