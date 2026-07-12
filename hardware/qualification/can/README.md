# CAN

**Category:** can · **WP-002** · Status: Proposed

## Purpose

Qualify CAN FD transceivers and associated bus interface components for the single linear CAN FD backbone connecting DCC (config master), ECU, and Button Box. Includes termination strategy, stub handling, and optional second transceiver on DCC Logic Board for Gen2 reserve.

## Typical Components

- CAN FD transceivers (5 V or 3.3 V IO compatible)
- Common-mode choke / EMI filter networks for harness interfaces
- CAN ESD protection devices (paired with protection category)
- Termination resistors (120 Ω) and test points
- CAN connector pin-filter components at DTM06-4S interfaces
- Optional CAN FD controller-less mode support verification with STM32 peripherals

## Selection Criteria

- CAN FD support: 500 kbit/s nominal, 2 Mbit/s data phase per Gen1 architecture
- Bus fault tolerance: short to battery/ground, dominant timeout recovery
- Standby and silent mode for power-saving without blocking wake-on-CAN
- Loop delay and propagation symmetry on linear DCC → ECU → Button Box topology
- EMC performance on unshielded race harness segments
- Compatible with DriveCore Protocol node addressing (DCC, ECU 0x2, Button Box)
- Automotive temperature grade and AEC-Q100 where available

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

- Is the second CAN transceiver on DCC Logic (J_CAN2) qualified for Gen1 stub use or depopulated?
- What maximum harness length and stub count are assumed for E30 installation?
- Should all three nodes use an identical qualified transceiver family for spares commonality?
- What bus-off recovery timing is required for VCM and ECU cooling_request latency?

## Future Work

- Bench network with three nodes and dual termination at DCC and Button Box
- Eye diagram and BER margin tests at maximum cable length
- Validate coexistence with Wi-Fi/BLE on Radio Board (EMI coupling)
- Document DTM12 pin 3/4 CAN routing for future peripherals (Dash, telemetry)

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
