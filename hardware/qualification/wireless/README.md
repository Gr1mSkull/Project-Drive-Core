# Wireless

**Category:** wireless · **WP-002** · Status: Proposed

## Purpose

Qualify wireless connectivity components on the DCC Radio Board: Wi-Fi/BLE module, antenna, RF matching, and coexistence elements. The Service layer (REST, WebSocket, OTA, YAML→binary) runs here; failure of wireless must not affect vehicle safety—STM32 Real-Time layer continues CAN, power channels, and VCM independently.

## Typical Components

- Wi-Fi / BLE combo module (SPI-attached to Logic Board)
- PCB trace or external antenna for 2.4 GHz
- RF matching network (π-filter, balun as required)
- Module crystal or clock reference (if not integrated)
- Coexistence filtering between RF front-end and CAN/USB harness exits
- Module enable and reset control circuitry

## Selection Criteria

- SPI interface bandwidth for OTA firmware and Web UI asset transfer
- BLE and Wi-Fi concurrent operation without starving STM32 SPI bus
- Regulatory modular certification (FCC/CE) vs. intentional radiator approval path
- Antenna placement inside aluminum DCC enclosure without detuning CAN or USB
- Power consumption peaks vs. Radio Board 5 V/3.3 V budget
- Boot and OTA failure modes: must not block Logic Board or assert spurious enables
- Supply availability and module lifecycle for field-replaceable Radio Board Rev.A→B

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

- Is external antenna mandatory for IP54 aluminum enclosure, or is on-module PCB antenna sufficient for paddock range?
- What OTA image size and transfer time targets drive SPI clock and module selection?
- Should BLE remain enabled during ENGINE_RUN and RACE modes, or be config-gated?
- How is RF coexistence validated alongside CAN FD and switching noise on Power Board?

## Future Work

- Define RF performance acceptance in enclosure with lid on (not bare PCB only)
- OTA rollback and brick-recovery test plan via USB-C on Logic Board
- Document degradation behavior when tablet Web UI client disconnects mid-session
- Align qualification with DevKit → DCC migration path for Radio Board

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../docs/Component_Qualification/)
