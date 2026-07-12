# Mechanical

**Category:** mechanical · **WP-002** · Status: Proposed

## Purpose

Qualify mechanical and thermal interface components for DCC enclosure assembly, board mounting, harness strain relief, and heat extraction from Power and Logic boards to the aluminum housing. Supports IP54 target, field-replaceable three-board structure, and paddock service within the DriveCore field serviceability principle.

## Typical Components

- Aluminum enclosure shell and lid (machined or extruded)
- Thermal interface materials (gap pads, phase-change, graphite)
- M3 standoffs and mounting hardware for Logic, Power, and Radio boards
- Cable glands and grommets for DTP/DT/DTM harness exits
- Board-to-board mechanical alignment features and stiffening brackets
- Labels, silkscreen, and identification plates for module swap traceability
- ECU and Button Box enclosures (separate mechanical qualification scope)

## Selection Criteria

- Thermal resistance from PROFET and DC-DC hotspots to enclosure lid (target θJA improvement)
- Vibration fixture survival for race/track duty without connector fretting
- IP54 ingress protection with realistic hose-down and dust exposure (not submerged)
- Mass and envelope constraints (~200×150×55 mm DCC orientation)
- Galvanic compatibility between aluminum enclosure, standoffs, and PCB mounting holes
- Service access: Radio daughtercard, USB-C, and fuse areas reachable in vehicle install
- Corrosion resistance for trunk/baggage environment and temperature cycling

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

- Is enclosure acting as sole heatsink for HS60 channels, or are local copper spreads primary?
- What minimum pad compression and tolerance stack-up apply for 1.5 mm thermal gap specification?
- Are ECU and Button Box enclosures in scope for this folder or separate qualification trees?
- How does IP54 validation account for open Deutsch connectors during maintenance?

## Future Work

- Thermal validation protocol per docs/Component_Qualification/Thermal_Validation.md
- Vibration test profile for combined DCC + harness mass representative of E30 install
- Document board removal sequence for 5–10 minute field swap goal
- Coordinate gland locations with connectors category harness bend radii

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
