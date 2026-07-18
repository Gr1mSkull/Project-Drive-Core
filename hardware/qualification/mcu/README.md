# MCU

**Category:** mcu · **WP-002** · Status: Proposed

## Purpose

Qualify microcontrollers for all DriveCore Real-Time nodes: STM32-class MCUs on DCC Logic Board (CAN, VCM, power channel control, diagnostics), ECU (engine control only), and Button Box (debounced inputs, encoder events). Selection emphasizes deterministic peripherals, safety integration, and a common toolchain where practical.

## Typical Components

- Main automotive MCU on DCC Logic (CAN FD, timers, ADC, SPI to Radio)
- ECU engine-control MCU (crank/cam capture, injector/ignition drivers, analog inputs)
- Button Box MCU (CAN FD, GPIO matrix, quadrature decode)
- Companion security or storage MCUs (if introduced)
- Debug/programming interface support (SWD, bootloader ROM)

## Selection Criteria

- CAN FD peripheral count and mailbox depth for config master + high message rate
- Timer channels for PWM to Power Board via J_LP (four PWM lines minimum)
- ADC resolution and speed for Logic analog inputs and ECU sensor conditioning
- Flash/RAM headroom for DriveCore firmware, diagnostics, and ECU algorithms
- Hardware watchdog integration path with external supervisor (protection category)
- Operating temperature grade for engine bay (ECU) vs. cabin/trunk (DCC, Button Box)
- Toolchain, long-term silicon availability, and second-source MCU family policy
- Bootloader and secure update alignment with USB-C (DCC) and field service model

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

- Is a single MCU family across DCC Logic and Button Box required for firmware reuse?
- What ECU MCU performance headroom is needed for Gen1 engine features vs. Gen2 expansion?
- Should DCC Logic MCU expose a second CAN controller for J_CAN2 reserve in Gen1 BOM?
- What SIL/ASIL expectations apply to race vehicle ECU vs. DCC VCM (inform qualification depth)?

## Future Work

- Peripheral matrix per board (CAN, SPI, timers, ADC) against SRS volumes 2 and 3
- Silicon errata review process and waiver tracking
- Long-run temperature cycling on ECU MCU location
- Document MCU reset and ENABLE interaction with Power Board fail-safe OFF

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
