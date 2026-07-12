# DriveCore Component Qualification

**Work Package:** WP-002 · **Status:** Proposed

Infrastructure for qualifying every electronic component before BOM approval.

## Rule

**No BOM without qualification.** This tree holds category folders and completed qualification reports — not conceptual BOM.

## Process documentation

| Document | Location |
|----------|----------|
| Overview | [docs/COMPONENT_QUALIFICATION_PROCESS.md](../docs/COMPONENT_QUALIFICATION_PROCESS.md) |
| Methodology & policies | [docs/Component_Qualification/](../docs/Component_Qualification/README.md) |
| Report template | [docs/Component_Qualification/Qualification_Report_Template.md](../docs/Component_Qualification/Qualification_Report_Template.md) |
| Decision matrix | [docs/Component_Qualification/Engineering_Decision_Matrix_Template.md](../docs/Component_Qualification/Engineering_Decision_Matrix_Template.md) |

## Category index

| Category | Path | DriveCore context |
|----------|------|-------------------|
| High-side switches | [high_side/](high_side/) | DCC Power PROFET outputs |
| Low-side / drivers | [low_side/](low_side/) | Gate drivers, low-side switches |
| Power supply | [power_supply/](power_supply/) | Buck, LDO, input protection ICs |
| Current sense | [current_sense/](current_sense/) | Shunt monitors, PROFET sense |
| Protection | [protection/](protection/) | TVS, ideal diode, watchdog |
| CAN | [can/](can/) | CAN FD transceivers |
| Wireless | [wireless/](wireless/) | ESP32 module, antenna |
| MCU | [mcu/](mcu/) | STM32 Logic, Button Box, ECU |
| Memory | [memory/](memory/) | FRAM, flash |
| Connectors | [connectors/](connectors/) | Deutsch, board-to-board |
| Passives | [passives/](passives/) | R, C, L, ferrites |
| Oscillators | [oscillators/](oscillators/) | HSE, LSE crystals |
| Sensors | [sensors/](sensors/) | ECU inputs, NTC on Power |
| Power distribution | [power_distribution/](power_distribution/) | Busbars, fusing strategy |
| Mechanical | [mechanical/](mechanical/) | Enclosure, thermal interface |

## Record naming

Completed reports (per category or root):

```
hardware/qualification/<category>/<Manufacturer>_<MPN>_qualification.md
```

## Qualification status

See [docs/Component_Qualification/Qualification_Status_Definitions.md](../docs/Component_Qualification/Qualification_Status_Definitions.md).

## Current state

| Metric | Count |
|--------|-------|
| Qualified records | 0 |
| Under review | 0 |

Conceptual reference only (not qualification): `docs/007_Component_Selection.md`.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 root folder |
| 2.0 | 2026-07-12 | WP-002 category structure |
