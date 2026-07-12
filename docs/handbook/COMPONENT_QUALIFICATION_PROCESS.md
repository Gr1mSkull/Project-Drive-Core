# Component Qualification Process

**Версия:** Handbook v1.0 · **Статус:** Proposed

## Rule

**No BOM without qualification.**

A component may appear in an approved BOM only after qualification or explicit provisional authorization in the task.

## Qualification checklist

| Step | Content |
|------|---------|
| 1 | Exact MPN, manufacturer datasheet |
| 2 | Lifecycle (active / NRND / EOL) |
| 3 | Electrical: continuous vs pulse vs limit current |
| 4 | Thermal: Rds, Rth, PCB, ambient, derating |
| 5 | Alternatives and second source |
| 6 | Record in BOM doc or qualification log |

## Cursor rules

- `.cursor/rules/component-selection.mdc` — summary index
- `.cursor/rules/drivecore-engineering.mdc` §5 — full rules

## Related documents

- [007_Component_Selection.md](../007_Component_Selection.md)
- [002_DCC_Hardware.md](../002_DCC_Hardware.md) §7 (thermal)
