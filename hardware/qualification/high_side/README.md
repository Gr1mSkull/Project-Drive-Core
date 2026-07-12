# High-Side Switches

**Category:** high_side · **WP-002** · Status: Proposed

## Purpose

Qualify high-side power switches and drivers used on the DCC Power Board to commutate vehicle loads across the Gen1 channel classes (60 A, 30 A, 15 A, 5 A). Outputs must support fail-safe OFF, VCM-driven enable logic, and integration with current sense and diagnostic feedback to the STM32 Logic Board.

## Typical Components

- Smart high-side switches (single- and multi-channel)
- High-current PROFET-class switches for 30–60 A channels
- Standard high-side switches for 5–15 A channels
- H-bridge motor drivers for window lift outputs
- PWM-capable high-side channels for fans, pumps, and blower loads
- Gate-driver companion ICs where required by switch topology

## Selection Criteria

- Continuous and inrush current rating vs. assigned channel class (HS60, HS30, HS15, HS05)
- RDS(on) and thermal derating at worst-case ambient (engine bay / trunk)
- Fail-safe behavior when ENABLE is deasserted or Logic Board communication is lost
- Diagnostic coverage: open load, short to battery/ground, overtemperature
- PWM frequency and duty-cycle range compatible with STM32 timer outputs via J_LP
- AEC-Q100 or equivalent automotive qualification where applicable
- Availability, second-source policy, and lifecycle status per DriveCore supplier rules
- PCB footprint and thermal pad requirements for aluminum enclosure heat spreading

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

- Do all 30 A channels require PWM, or only the four hardware PWM lines (fans, pump, blower)?
- Is a single switch family acceptable across HS15/HS05, or should channel classes use distinct qualified families?
- What minimum diagnostic granularity is required for race-event logging vs. paddock troubleshooting?
- How should EHPS inrush (up to ~100 A) be bounded relative to HS60 switch SOA?

## Future Work

- Map each DCC output channel (Ch01–Ch22, HB01–HB02) to a channel class and load profile from E30 config
- Define bench validation fixtures for inrush, PWM dimming, and fault injection per channel class
- Complete qualification reports per [Qualification_Report_Template.md](../../../docs/Component_Qualification/Qualification_Report_Template.md)
- Cross-reference thermal validation with Power Board layout and enclosure conduction path

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
