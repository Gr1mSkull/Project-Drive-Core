# Power Distribution

**Category:** power_distribution · **WP-002** · Status: Proposed

## Purpose

Qualify power distribution elements beyond individual switching ICs: battery input paths, +12V_SW bus architecture, star-ground strategy, fusing, and high-current PCB conductors on DCC Power Board. Implements the One Harness hub model—single DCC entry after main contactor—with channelized outputs to EHPS, cooling, ECU, lighting, and cabin loads per E30 priorities.

## Typical Components

- High-current PCB busbars and copper pours (60 A / 30 A zones)
- Main input fuse or fusible link coordination with external contactor
- Channel output fusing (blade, MIDI, or PCB-integrated) per load class
- Distribution studs and bolt-down terminals for DTP-class harness feeds
- Star-point ground bus linking power return to Logic GND at J_LP
- Shunt or monitor placement in high-current return paths (with current_sense)
- Precharge or inrush limiting elements (if required for EHPS class loads)

## Selection Criteria

- Continuous current density and temperature rise at 130–170 A system aggregate load
- Voltage drop budget from battery input to farthest 5 A DTM output
- Fuse coordination: branch vs. channel vs. main—no single failure removes entire vehicle power incorrectly
- Creepage/clearance on 12 V high-current zones in humid/paddock environments
- Mechanical retention of heavy gauge connections under vibration
- Serviceability: fuse replacement within field service time target without full DCC disassembly
- Alignment with VCM priorities (critical loads retain power paths when non-critical channels fault)

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

- Is all high-current fusing on Power Board, or split with external harness fuse blocks?
- How is aggregate 130–170 A load managed for simultaneous channel enable in config rules?
- What derating applies to EHPS when battery voltage sags below configured thresholds?
- Are busbar materials and plating qualified for long-term corrosion in trunk mounting?

## Future Work

- IR drop and thermal simulation across Power Board Rev.A copper strategy
- Fuse clearing tests coordinated with high_side switch SOA
- Document +12V_BAT → TVS → ideal diode → +12V_SW flow with protection category
- E30 load priority table cross-check against channel class hardware limits

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
