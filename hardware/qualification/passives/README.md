# Passives

**Category:** passives · **WP-002** · Status: Proposed

## Purpose

Qualify passive components—resistors, capacitors, inductors, ferrites, and filters—used across DCC (Logic, Power, Radio), ECU, and Button Box assemblies. Passives underpin power integrity, CAN signal quality, analog accuracy, and EMI compliance; qualification ensures automotive-grade reliability at volume without per-MPN BOM chaos.

## Typical Components

- Thick-film and thin-film resistors (signal, sense, termination)
- Ceramic capacitors (X7R/X5R decoupling, C0G/NP0 timing and ADC reference)
- Electrolytic and polymer capacitors (bulk input/output filtering)
- Power inductors for buck converters
- Ferrite beads and common-mode chokes on CAN, USB, and power entry
- RC/LC filter networks on Logic analog and frequency inputs
- Gate resistors and snubbers on Power Board switching stages

## Selection Criteria

- Voltage rating derating on 12 V and switched rails including load dump exposure
- Temperature coefficient impact on current sense and analog input accuracy
- ESL/ESR suitable for MCU and CAN transceiver decoupling at CAN FD data rates
- Mechanical stress (flex cracking) under vibration for large ceramic caps on Power Board
- AEC-Q200 or equivalent for safety-relevant networks (kill input pull-ups, termination)
- Approved footprint and land pattern library per DriveCore PCB design rules
- Supplier breadth for second-source on high-quantity line items

## Qualification Status

| Status | Count |
|--------|-------|
| Candidate | 0 |
| Under Review | 0 |
| Lab Validation | 0 |
| Approved for Prototype | 0 |
| Approved for Production | 0 |
| Deprecated | 0 |
| Rejected | 0 |

## Current Candidates

None. No MPNs under evaluation in this category.

## Open Questions

- Which passive networks are safety-critical vs. general decoupling (different qualification depth)?
- Are there maximum ESR/ESL budgets for CAN 120 Ω termination + filter networks?
- Should Power Board bulk capacitors be qualified as a system with power_supply converters?
- What MLCC DC bias derating rules apply on 12 V input filters?

## Future Work

- Publish approved passive bill-of-materials families by package and dielectric
- Accelerated life test plan for Power Board hot spots near PROFET switches
- PI/EMI correlation between ferrite selections and CAN FD margin
- Align with oscillators and sensors categories for reference and filter passives

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
