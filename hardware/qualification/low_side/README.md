# Low-Side Switches and Drivers

**Category:** low_side · **WP-002** · Status: Proposed

## Purpose

Qualify low-side switches, gate drivers, and related driver ICs that complement high-side outputs on DCC, drive indicator loads, and support peripheral interfaces where a low-side topology is required. Includes drivers for optional low-power outputs on the universal DTM12 peripheral port.

## Typical Components

- Low-side MOSFET switches
- N-channel MOSFET gate drivers (single and half-bridge)
- Low-side driver ICs with integrated protection
- Level-shifting driver stages between 3.3 V logic and 12 V loads
- Pre-driver stages for H-bridge low-side legs on Power Board

## Selection Criteria

- Voltage and current rating for 12 V automotive loads on OUT1/OUT2-class signals
- Propagation delay and shoot-through prevention when paired with high-side or H-bridge stages
- ESD and load-dump immunity on driver inputs and outputs
- Compatibility with STM32 GPIO/timer drive strength and slew requirements
- Fail-safe default state (OFF) on power-up and MCU reset
- Automotive temperature grade and qualification documentation
- Package size suitable for Logic Board and compact CAN peripherals (Button Box)

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

- Which DTM12 optional outputs require dedicated low-side drivers vs. simple GPIO?
- Are low-side switches needed on Button Box, or is it input-only for Gen1?
- Should H-bridge low-side legs share a driver family with any standalone low-side channels?
- What maximum load current is required for peripheral OUT lines on DTM12?

## Future Work

- Inventory all low-side topologies across DCC Logic, Power, and Button Box schematics
- Define shared gate-driver qualification criteria with high_side and protection categories
- Establish bench tests for inductive load switching and flyback clamp verification
- Document interaction with VCM fail-safe OFF requirements

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
