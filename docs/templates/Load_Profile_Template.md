# Load Profile Template

**Document ID:** TPL-LOAD-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-003

Use when adding or updating a vehicle load record. Copy to `docs/Vehicle_Integration/` or extend `config/vehicles/{profile}_loads.yaml`.

**Do not invent numeric values.** Use `TBD` in Markdown and `null` in YAML until measured or datasheet-sourced.

---

## Load Profile

| Field | Value |
|-------|-------|
| **Load ID** | e.g. `E30LD-XXX` — stable, never reused |
| **Load key** | snake_case functional name (matches future `outputs` key if DCC-switched) |
| **Functional name** | |
| **Presence** | Confirmed \| Planned \| Optional \| TBD |
| **Physical location** | |
| **Load technology** | |
| **Load classification** | inductive \| resistive \| electronic \| mixed \| TBD |
| **DCC switched** | yes \| no |
| **DCC output key** | or N/A |
| **DCC channel** | 1–22, 101, 102, or N/A |
| **DCC channel class** | HS60 \| HS30 \| HS15 \| HS05 \| HB \| N/A |

### Electrical characteristics

| Field | Value | Evidence |
|-------|-------|----------|
| **Nominal supply voltage** | V | measured \| datasheet \| architecture_reference \| unknown |
| **Nominal current** | A | |
| **Maximum continuous current** | A | |
| **Startup / inrush current** | A | |
| **Startup duration** | s | |
| **Stall current** | A (if applicable) | |
| **PWM required** | yes \| no \| TBD | |
| **PWM frequency range** | Hz | |
| **Reverse-current behavior** | | |
| **Regenerative behavior** | | |
| **Switching frequency** | | |
| **Operating duty cycle** | | |
| **Maximum continuous operating time** | | |

### Integration requirements

| Field | Value |
|-------|-------|
| **Simultaneous-operation group** | GRP-XXX |
| **Criticality** | critical \| high \| medium \| low \| TBD |
| **Required degraded behavior** | or ARCHITECTURAL DECISION REQUIRED |
| **Safe state** | off \| on \| ARCHITECTURAL DECISION REQUIRED |
| **Diagnostic requirements** | |
| **Open-load detection required** | yes \| no \| TBD |
| **Current measurement required** | yes \| no \| TBD |
| **Retry policy required** | |
| **External fuse requirement** | TBD |
| **Connector requirement status** | TBD |
| **Wire requirement status** | TBD |

### Provenance

| Field | Value |
|-------|-------|
| **Data source** | document paths, harness survey, bench test ID |
| **Evidence status** | measured \| datasheet \| estimated \| unknown |
| **Measurement required** | yes \| no |
| **Notes** | |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-003 initial template |
