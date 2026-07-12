# Power Supply

**Category:** power_supply · **WP-002** · Status: Proposed

## Purpose

Qualify DC-DC converters, LDO regulators, and power-management ICs that generate stable rails for DCC Logic Board, Radio Board, ECU, and Button Box from the protected vehicle 12 V bus. Covers input tolerance, efficiency, noise, and sequencing after the main contactor and ideal-diode stage on Power Board.

## Typical Components

- Synchronous buck converters (5 V and intermediate rails)
- Low-noise LDO regulators (3.3 V for MCU, CAN transceiver, memory)
- PMIC or multi-rail regulators where a single IC serves Logic + Radio
- Reverse-polarity and input protection controller ICs (paired with protection category)
- Bootstrap / bias supplies for gate drivers on Power Board
- Local LDOs on ECU and Button Box from DCC-switched 12 V feeds

## Selection Criteria

- Input voltage range including cranking, load dump, and nominal 12–14.4 V operation
- Output accuracy and load regulation under CAN traffic bursts and Wi-Fi transmit peaks
- EMI/conducted noise limits compatible with CAN FD and analog inputs on Logic Board
- Efficiency and thermal dissipation at maximum Logic + Radio load
- Enable/sequencing compatibility with VCM states and watchdog reset behavior
- Quiescent current impact on battery when MASTER_ON but IGNITION off
- Automotive qualification, availability, and second-source options

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

- Is all Logic Board regulation local (5 V + 3.3 V on Logic), or does any rail originate on Power Board via J_LP?
- What peak current budget is required for ESP32 Wi-Fi/BLE transmit on Radio Board?
- Are separate qualified LDO families required for analog reference vs. digital 3.3 V?
- What hold-up time is needed across brief contactor bounce or battery sag during engine start?

## Future Work

- Build consolidated power budget for Logic, Radio, and standby states
- Define input transient test matrix aligned with ISO 16750-style vehicle conditions
- Qualify ripple and PSRR impact on HSE crystal and CAN FD eye diagram
- Coordinate with power_distribution for +12V_SW feed architecture

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
