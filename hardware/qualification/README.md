# DriveCore Component Qualification

**Work Package:** WP-002 · **Change Request:** CR-001 · **Status:** Proposed

Infrastructure for qualifying every electronic component before BOM approval.

## Rule

**No BOM without qualification.** This tree holds category folders and completed qualification reports — not conceptual BOM.

## Process documentation

| Role | Document | Link |
|------|----------|------|
| **Overview** (navigation) | Component Qualification Process | [COMPONENT_QUALIFICATION_PROCESS.md](../../docs/COMPONENT_QUALIFICATION_PROCESS.md) |
| **Normative methodology** | Qualification Methodology | [Qualification_Methodology.md](../../docs/Component_Qualification/Qualification_Methodology.md) |
| Policies & templates | Component Qualification folder | [Component_Qualification/](../../docs/Component_Qualification/README.md) |
| Report template | Qualification Report Template | [Qualification_Report_Template.md](../../docs/Component_Qualification/Qualification_Report_Template.md) |
| Decision matrix | Engineering Decision Matrix | [Engineering_Decision_Matrix_Template.md](../../docs/Component_Qualification/Engineering_Decision_Matrix_Template.md) |

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

Completed reports:

```
hardware/qualification/{category}/{manufacturer}_{mpn}_qualification.md
```

Example (illustrative only): `hardware/qualification/high_side/Infineon_BTS50085-1TMA_qualification.md`

## Qualification status

See [Qualification_Status_Definitions.md](../../docs/Component_Qualification/Qualification_Status_Definitions.md).

## Current state

| Metric | Count |
|--------|-------|
| Qualified records | 0 |
| Under review | 0 |

Conceptual reference only (not qualification): [007_Component_Selection.md](../../docs/007_Component_Selection.md).

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 root folder |
| 2.0 | 2026-07-12 | WP-002 category structure |
| 2.1 | 2026-07-12 | CR-001 link and path template fixes |
