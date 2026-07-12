# Current Sense

**Category:** current_sense · **WP-002** · Status: Proposed

## Purpose

Qualify current measurement components for DCC Power Board channel monitoring, PROFET integrated sense lines, and any shunt-based measurement on Logic or ECU inputs. Accurate current feedback supports diagnostics, config-driven derating (e.g., EHPS at low battery), and event logging without blocking fail-safe OFF behavior.

## Typical Components

- High-side current sense amplifiers
- Bidirectional shunt monitors for H-bridge or bidirectional loads
- Integrated sense outputs from smart high-side switches
- Precision shunt resistors (metal foil / metal strip)
- Analog front-end conditioning for STM32 ADC on Logic Board
- Hall-effect or magnetic current sensors for high-current channels (if used)

## Selection Criteria

- Measurement range and resolution per channel class (5 A through 60 A)
- Accuracy and drift over automotive temperature range
- Common-mode voltage rating for high-side sensing topology
- Bandwidth sufficient for inrush detection and PWM average current
- Integration path: analog to STM32 ADC vs. digital bus to Logic Board
- Fault detection alignment with PROFET diagnostic pins
- Shunt power dissipation and Kelvin layout requirements at high current

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

- Is integrated PROFET sense sufficient for all channels, or are external shunts required for HS60?
- What current reporting granularity does DriveCore Protocol diagnostics require per channel?
- Should sense data feed real-time derating rules in VCM or remain logging-only for Gen1?
- How is sense calibration handled across production units and field replacement modules?

## Future Work

- Define per-channel sense architecture map (integrated vs. external shunt)
- Establish calibration procedure and accuracy acceptance limits for prototype builds
- Correlate sense readings with thermal validation under sustained EHPS and fan loads
- Document API between Power Board sense signals and Logic Board firmware

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
