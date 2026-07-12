# Memory

**Category:** memory · **WP-002** · Status: Proposed

## Purpose

Qualify non-volatile and volatile memory components for configuration persistence, event logs, firmware storage, and ECU calibration data. DCC Logic requires reliable storage across power cycles and VCM transitions; ECU may require fast write endurance for adaptive tables; Button Box needs minimal persistent state.

## Typical Components

- Ferroelectric RAM (FRAM) for config snapshots and high-endurance logs
- Serial NOR flash for firmware images and Web UI asset staging (Radio path)
- EEPROM or emulated-EEPROM regions (if used on ECU)
- SDRAM or PSRAM (if required by wireless module architecture)
- SD or external flash sockets (if introduced for logging expansion)

## Selection Criteria

- Write endurance vs. expected config save frequency and diagnostic log rate
- Retention across temperature cycles in trunk-mounted DCC enclosure
- SPI or parallel interface compatibility with STM32 Logic without blocking CAN ISR latency
- Data integrity across unexpected power loss during MASTER_ON → OFF transitions
- Capacity for vehicle YAML binary, event ring buffer, and OTA staging partitions
- Automotive or industrial temperature grade; radiation/single-event concerns (track use)
- Supply chain and obsolescence risk for niche memory technologies

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

- Is FRAM mandatory for config on Logic Board, or is flash with wear-leveling acceptable?
- What maximum log depth and retention policy drive memory sizing for Gen1?
- Does ECU calibration storage live on ECU MCU internal flash only, or external memory?
- How is memory qualified for field module swap with auto-discovery over CAN?

## Future Work

- Define memory map partitions (config, logs, OTA, bootloader) per board
- Power-cut write tests during simulated contactor drop
- Endurance modeling for paddock config edits and race logging burst rates
- Align with configuration model binary format in docs/005

## Related Documents

- [hardware/qualification/README.md](../README.md)
- [docs/Component_Qualification/](../../../docs/Component_Qualification/)
