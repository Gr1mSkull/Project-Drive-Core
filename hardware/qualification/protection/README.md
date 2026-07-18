# Protection

**Category:** protection · **WP-002** · Status: Proposed

## Purpose

Qualify circuit protection and safety-supervision components across DCC, ECU, and Button Box: input TVS, ideal-diode ORing, watchdog timers, ESD devices, and fault-isolation elements. These parts enforce the Gen1 safety model—fail-safe OFF, independent kill switch path, and graceful degradation when a single channel faults.

## Typical Components

- Automotive TVS diodes (load dump, ISO pulse)
- Ideal-diode / smart high-side protection controllers on battery input
- Hardware watchdog timers with programmable timeout
- ESD protection arrays on CAN, USB, and GPIO
- Fuse holders and polyfuse elements (coordination with power_distribution)
- Reverse-battery protection MOSFETs or controllers
- EMI filter and TVS combinations on external harness interfaces

## Selection Criteria

- Clamp voltage and peak pulse energy vs. 12 V automotive transients
- Coordination with main contactor: protection must not replace physical ground disconnect
- Watchdog timeout and reset behavior compatible with STM32 ENABLE gating on Power Board
- Fail-safe output state when watchdog expires or MCU hangs
- Leakage and voltage drop on protected 12 V paths feeding +12V_SW
- CAN bus protection without violating 120 Ω termination topology
- Qualification evidence for repeated transient exposure (not single-shot lab only)

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

- What watchdog timeout aligns with VCM state transitions and CAN heartbeat periods?
- Is a single TVS strategy sufficient at DCC input, or are additional clamps required per harness class?
- How does kill-switch hardware interact with ENABLE and watchdog—explicit interlock requirements?
- Should Button Box and ECU carry independent input protection, or rely on DCC-switched feeds only?

## Future Work

- Document protection coordination diagram from battery through contactor to channel outputs
- Define transient test plan shared with power_supply and can categories
- Validate watchdog + ENABLE timing under deliberate firmware hang tests
- Align with fail-safe requirements in system architecture (§9)

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
