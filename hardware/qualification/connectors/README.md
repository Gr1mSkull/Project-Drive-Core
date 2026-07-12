# Connectors

**Category:** connectors · **WP-002** · Status: Proposed

## Purpose

Qualify electrical connectors for DCC internal board-to-board links, vehicle harness interfaces, and CAN peripheral attachment. DriveCore Gen1 standardizes Deutsch families by signal class (DTM for logic/CAN, DT for medium current, DTP for high current) and the universal DTM12 peripheral port for Button Box and future nodes.

## Typical Components

- Board-to-board connectors (Logic ↔ Power, Logic ↔ Radio)
- Automotive circular connectors (4-pin CAN, 12-pin DTM12 universal port)
- High-current two- and four-pin outputs for HS60/HS30/H-bridge channels
- USB-C receptacle for firmware and debug
- Tag-Connect or SWD debug interface
- Input connector for kill switch, master feedback, starter, and analog signals
- ECU and Button Box harness connectors matching DCC-switched feed classes

## Selection Criteria

- Current and voltage rating per connector class vs. channel map (5 A–60 A)
- Keying and polarization to prevent cross-mating of logic vs. power families
- IP54 target compatibility with enclosure cable glands and strain relief
- Vibration and thermal cycling for race vehicle installation
- Contact resistance stability under corrosion and temperature (paddock service)
- Availability via approved supplier channels (including LCSC/AliExpress where documented)
- Mate cycle count for field-replaceable modules within 5–10 minute service goal

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

- Is DTM12 the sole qualified peripheral standard for Gen1, or are legacy Deutsch variants allowed on ECU?
- What B2B pin count margin is required on J_LP and J_EXP for Gen2 without connector change?
- Are sealed vs. open Deutsch variants specified per mounting zone (engine bay vs. cabin)?
- How are shield terminations handled on CAN harnesses at DCC and Button Box?

## Future Work

- Connector-to-channel assignment table for Power Board external interfaces
- Vibration and thermal shock test coupons per connector class
- Document One Harness routing from DCC hub to E30 load endpoints
- Cross-reference mechanical category for gland and panel cutout requirements

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
