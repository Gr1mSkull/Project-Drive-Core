# DevKit Fixture Preliminary Design Decision Register — WP-015

**Document ID:** DOC-DK-FPDDR-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Proposed decisions and options only. No entry is Accepted, selected, frozen, or authorized for procurement.
All new entries remain PROPOSED_DESIGN / ALTERNATIVE_UNDER_EVALUATION / BLOCKED_BY_ARCHITECTURE until Architect Review.
The Implementation Engineer shall not self-approve any decision.
```

## 1. Decision register

| ID | Decision topic | Options | Recommendation | Status | Authority needed | Dependencies | Risk if deferred | Closure artifact |
|----|----------------|---------|----------------|--------|------------------|--------------|------------------|------------------|
| FX-PD-001 | Fixture module decomposition | §11 functional module set | Adopt as preliminary decomposition | PROPOSED_DESIGN | Architect | REQ-DCC-V-FX-* | Rework of downstream design | WP-015 acceptance |
| FX-PD-002 | Base-energy control architecture | source-gated single path · segmented path | Source-gated with independent removal | PROPOSED_DESIGN | Architect | thresholds Open | Ambiguous energy control | WP-015 acceptance |
| FX-PD-003 | External-energy exclusivity | mutually exclusive modes · concurrent (needs GND) | Mutually exclusive while OI-GND-001 Open | PROPOSED_CONSTRAINT | Architect | OI-GND-001 | Combined-energy hazard | OI-GND-001 package |
| FX-PD-004 | Ground/reference option | GND-OPTION-A/B/C/D | Defer to dedicated package | BLOCKED_BY_ARCHITECTURE | Architect | OI-GND-001 | Blocks external/measurement design | OI-GND-001 decision |
| FX-PD-005 | Back-feed-prevention functional placement | at ext boundary · at base entry · dual | At external-energy boundary (topology-neutral) | PROPOSED_DESIGN | Architect | OI-GND-001; OI-PROT-001 | Base overstress risk | Protection package |
| FX-PD-006 | E-stop path architecture | E-STOP-OPT-1…4 | Defer selection; keep AUTH-inhibit-if-unconfirmed | BLOCKED_BY_ARCHITECTURE | Architect | REQ-DCC-V-FX-071 | Unsafe E-stop assumption | E-stop package |
| FX-PD-007 | Energy-removal observation | command-confirm · independent observe | Independent physical observation required | PROPOSED_CONSTRAINT | Architect | measurement design | False safe belief | Measurement design |
| FX-PD-008 | Discharge observation | assume decay · confirm residual | Confirm safe residual before recovery | PROPOSED_CONSTRAINT | Architect | timing Open | Residual-energy hazard | Discharge design |
| FX-PD-009 | Load-bank architecture | resistive · electronic · hybrid | Keep class-neutral; sink-only | ALTERNATIVE_UNDER_EVALUATION | Architect | ratings Open (ED-IN-022) | Premature selection | Load-bank design |
| FX-PD-010 | Load-bank stuck-on containment | AUTH revoke only · upstream removal | Upstream inhibit/remove + lockout | PROPOSED_CONSTRAINT | Architect | — | Stuck-on hazard | WP-015 acceptance |
| FX-PD-011 | DAQ responsibility split | DUT-diagnostic-as-evidence · independent reference | Independent reference for evidence candidates | PROPOSED_CONSTRAINT | Architect | OI-SENSE-001 | Non-independent evidence | Measurement design |
| FX-PD-012 | Reference measurement independence | shared · independent instrument | Independent reference where verification depends on it | PROPOSED_DESIGN | Architect | calibration Open | Weak verification | Measurement design |
| FX-PD-013 | Fault-injection authorization | UI-authorized · safety-layer-authorized | Safety-layer-authorized, default inhibited | PROPOSED_CONSTRAINT | Architect | ADR-023 | Unauthorized fault | Fault package |
| FX-PD-014 | DUT interface grouping | combined · grouped by energy/safety class | Grouped by energy/safety class | PROPOSED_DESIGN | Architect | — | Cross-class coupling | DUT interface design |
| FX-PD-015 | Operator control authority | UI-authoritative · request-only + safety layer | Request-only; safety layer decides | PROPOSED_CONSTRAINT | Architect | PWR-A-024 | UI-owned hazard | WP-015 acceptance |
| FX-PD-016 | Lockout/recovery authority | auto-recover · deliberate operator | Deliberate operator + interlock validation | PROPOSED_CONSTRAINT | Architect | — | Unsafe auto-recovery | WP-015 acceptance |
| FX-PD-017 | Preliminary enclosure/containment boundary | single enclosure · modular · open-bench-with-guarding | Defer; containment functional only | BLOCKED_BY_DETAILED_DESIGN | Architect | ADR-DK-011/012 | Exposed-energy risk | ADR-DK-011/012 |

## 2. Governance

- No `FX-PD-*` entry is Accepted by WP-015. Architect Review assigns ACCEPT / ACCEPT CONDITIONALLY / DEFER / REJECT per entry.
- Recommendations are Implementation Engineer proposals only; they do not constitute approval or selection.
- Options do not name manufacturers, MPNs, connectors, conductors, or ratings.

## 3. Traceability

REQ-DCC-V-FX-* · OI-GND-001 · OI-PROT-001/002 · OI-SC-001 · OI-FIX-002 · OI-BI-001 · OI-SENSE-001 · ADR-022/023 · ADR-DK-011/012 · PWR-A-024 · ED-IN-022 · REQ-DCC-V-FX-071.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial preliminary design decision register (FX-PD-001…017) — Proposed |
