# DevKit Fixture Detailed-Design Readiness and Gate Matrix — WP-016

**Document ID:** DOC-DK-FDDRGM-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Honest readiness assessment. "READY_IF_ACCEPTED" means ready for DETAILED DESIGN only if the
Architect accepts the relevant WP-016 recommendation. Procurement/construction/energization are NOT ready.
```

## 1. Legend

`READY_IF_ACCEPTED` · `PARTIAL` · `NOT_READY` · `BLOCKED` · `NOT_AUTHORIZED`

## 2. Readiness / gate matrix

| Subsystem | Architecture decision ready | Numeric inputs ready | Component class ready | Safety allocation ready | Detailed design authorized if accepted | Main blocker | Required next artifact |
|-----------|-----------------------------|----------------------|-----------------------|--------------------------|----------------------------------------|--------------|-----------------------|
| Base source control | READY_IF_ACCEPTED | NOT_READY | NOT_READY | PARTIAL | Base-only detailed design (non-numeric) | Numeric envelopes (TBD-DK-002) | Sizing + source design |
| Base energy path | READY_IF_ACCEPTED | NOT_READY | NOT_READY | PARTIAL | Base-only path design | Numeric; protection class | Energy-path design |
| External energy boundary | BLOCKED | NOT_READY | NOT_READY | BLOCKED | No (combined-mode) | OI-GND-001 | GND disposition |
| E-stop | PARTIAL (OPT-2/3 class) | NOT_READY | NOT_READY | BLOCKED | No (topology deferred) | REQ-DCC-V-FX-071 topology/proof | E-stop package |
| Reverse-polarity protection | PARTIAL (class direction) | NOT_READY | NOT_READY | PARTIAL | No (final class deferred) | OI-PROT-001; numeric | Protection package |
| Transient protection | PARTIAL (hybrid class) | NOT_READY | NOT_READY | PARTIAL | No | OI-PROT-002; waveform bound | Protection package |
| Back-feed prevention | BLOCKED | NOT_READY | NOT_READY | BLOCKED | No | OI-GND-001; OI-PROT-001 | GND + protection |
| Load bank | READY_IF_ACCEPTED (sink) | NOT_READY | NOT_READY | PARTIAL | Sink-only detailed design | Ratings Open | Load-bank design |
| Returned-energy handling | READY_IF_ACCEPTED (policy D) | NOT_READY | NOT_READY | PARTIAL | Exclusion interlock design | OI-BI-001 | RE policy acceptance |
| Measurement connections | PARTIAL | NOT_READY | BLOCKED | PARTIAL | No | OI-SENSE-001; OI-GND-001 | Measurement package |
| DAQ | PARTIAL | NOT_READY | NOT_READY | PARTIAL | No | Accuracy/BW Open | DAQ design |
| Discharge | PARTIAL | NOT_READY | NOT_READY | PARTIAL | No | Timing Open | Discharge design |
| Fault injection | PARTIAL | NOT_READY | NOT_READY | PARTIAL | No | OI-SC-001; bounds | Fault package |
| DUT interface | READY_IF_ACCEPTED | NOT_READY | NOT_READY | PARTIAL | Interface detailed design | Connector/pinout Open | DUT interface design |
| Wiring | PARTIAL | NOT_READY | NOT_READY | PARTIAL | No | Sizing/connector Open | Wiring design |
| Containment | BLOCKED | NOT_READY | NOT_READY | BLOCKED | No | ADR-DK-011/012 | Enclosure decision |
| Operator controls | READY_IF_ACCEPTED | NOT_READY | NOT_READY | PARTIAL | Panel detailed design | — | Operator-panel design |

## 3. Procurement / construction / energization

All **NOT_AUTHORIZED** regardless of architecture readiness. WP-016 does not authorize final schematic release, BOM release, procurement, construction, energization, physical fault injection, or verification execution.

## 4. Downstream readiness summary

- **Ready-if-accepted for detailed design (non-numeric, base-only / sink-only / interface / operator):** base source control, base energy path, load bank (sink), returned-energy (policy D exclusion), DUT interface, operator controls.
- **Partial / blocked pending decisions:** E-stop, protection (RP/transient), measurement, DAQ, discharge, fault injection, wiring.
- **Blocked pending Architect disposition:** external energy boundary, back-feed prevention, containment.

## 5. Traceability

FX-DD-IN-* · FX-PD-* · OI-GND-001 · OI-PROT-001/002 · OI-BI-001 · OI-SENSE-001 · OI-SC-001 · ADR-DK-011/012 · REQ-DCC-V-FX-071 · TBD-DK-002.

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial detailed-design readiness and gate matrix — Proposed |
