# Oscillators

**Category:** oscillators · **WP-002** · Status: Proposed

## Purpose

Qualify clock sources for STM32 MCUs on DCC Logic, ECU, and Button Box, and for any wireless module reference clocks on Radio Board. Stable HSE/LSE performance is required for CAN FD bit timing, PWM accuracy to Power Board channels, and ECU crank/cam capture precision.

## Typical Components

- HSE crystals (8 MHz or MCU-specific fundamental)
- LSE crystals (32.768 kHz RTC)
- Crystal load capacitors (paired with passives category)
- Ceramic resonators (only if explicitly allowed by MCU errata)
- Clock generator ICs (if multi-output reference required)
- TCXO or clock modules (if wireless or ECU precision demands)

## Selection Criteria

- Frequency tolerance and stability over automotive temperature for CAN FD clock tree
- Load capacitance match to MCU Pierce oscillator pins and PCB stray capacitance
- Drive level and aging characteristics per MCU manufacturer crystal selection guide
- G-sensitivity and vibration immunity for ECU engine-bay mounting
- EMC: harmonic content and layout sensitivity near CAN and switching noise
- Footprint compatibility with pick-and-place and rework in field service
- Dual-source crystal vendors for identical electrical spec

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

- Is a common HSE frequency and crystal part strategy shared across DCC, ECU, and Button Box?
- What ppm budget is allocated for CAN FD 2 Mbit/s data phase across temperature?
- Are separate crystals required for wireless module vs. STM32, or shared clock architecture?
- Does ECU crank capture require dedicated high-stability clocking beyond standard HSE?

## Future Work

- Pierce oscillator margin analysis per board layout (Logic, ECU, Button Box)
- Temperature chamber frequency drift tests tied to CAN bit error rate
- Document crystal keep-out and ground guard rules under aluminum enclosure
- Validate startup time vs. VCM MASTER_ON to READY timing requirements

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
