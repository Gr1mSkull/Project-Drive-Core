# Sensors

**Category:** sensors · **WP-002** · Status: Proposed

## Purpose

Qualify sensors and sensing elements for vehicle and module feedback: Logic Board analog and frequency inputs, Power Board thermal monitoring, ECU engine sensors, and optional expansion on SPI/I2C/UART. DCC consumes ECU telemetry over CAN; local sensors support VCM rules, diagnostics, and config-driven thresholds—not engine control algorithms on DCC.

## Typical Components

- NTC thermistors for Power Board and enclosure hotspot monitoring
- Analog 0–5 V sensor interfaces on DCC Logic (AIN1–4)
- Frequency/speed and tachometer input conditioning (FREQ1–2)
- Digital position and pressure sensors on ECU (MAP, lambda, oil pressure, etc.)
- Hall or magnetic speed sensors (optional vehicle inputs)
- IMU / GNSS modules on Logic expansion port (optional Gen1)
- Kill switch and master feedback sense circuits (digital, not autonomous sensors)

## Selection Criteria

- Accuracy and latency vs. VCM rule thresholds (cooling, warnings, mode transitions)
- Automotive temperature, vibration, and fluid compatibility for ECU bay installation
- EMC immunity on analog front ends near switching loads and CAN harness
- Sensor fault detection (open/short) and safe default behavior in config rules
- Calibration and linearization burden in firmware vs. sensor intrinsic linearity
- Interface type alignment: analog to STM32 ADC, digital pulse capture, or CAN peripheral
- Supply and harness routing from DCC-switched channels or dedicated sensor feeds

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

- Which E30 sensors are mandatory on ECU vs. optional on DCC Logic analog inputs?
- Is on-board NTC on Power Board required per PROFET channel or per board zone?
- How are sensor failures surfaced on DriveCore Protocol vs. local DCC diagnostics only?
- What expansion sensors (IMU, GNSS) are in Gen1 scope vs. Gen2 for qualification priority?

## Future Work

- Sensor-to-signal map for E30 vehicle config and ECU telemetry fields
- Bench validation of analog input accuracy through Logic Board front end
- Thermal correlation between NTC readings and PROFET junction estimates
- Document boundary: ECU engine sensors vs. DCC vehicle-level inputs per docs/003

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
