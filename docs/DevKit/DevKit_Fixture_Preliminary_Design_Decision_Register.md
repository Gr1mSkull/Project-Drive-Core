# DevKit Fixture Preliminary Design Decision Register — WP-015

**Document ID:** DOC-DK-FPDDR-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review (2026-07-21); per-entry dispositions applied  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
This register contains the final WP-015 Architecture Review dispositions.

Entries are classified as:
- ACCEPTED;
- ACCEPTED CONDITIONALLY;
- DEFERRED.

Accepted and conditionally accepted entries remain preliminary architecture
decisions. They do not authorize detailed design, procurement, construction,
energization, verification, or closure of dependent OI/TBD items.

Deferred entries remain Open/Blocked and are not rejected.

The original proposals were authored by the Implementation Engineer and were
accepted only through System Architect review; no entry was self-approved.
```

## 0. Architect disposition (Architecture Review 2026-07-21)

WP-015 Accepted (reviewed head `227ea78`, PR #19). Per-entry dispositions:

- **ACCEPTED** (preliminary architecture/constraint): FX-PD-001, 002, 003, 007, 008, 010, 011, 012, 013, 014, 015, 016, 018, 019, 020, 021.
- **ACCEPTED CONDITIONALLY** (realization blocked): FX-PD-005 (back-feed placement — depends on OI-GND-001/OI-PROT-001); FX-PD-009 (sink-function accepted; regenerative/returned-energy realization blocked by OI-BI-001/OI-GND-001 + future bounded-energy design).
- **DEFERRED** (remains Open/Blocked, not rejected): FX-PD-004 (ground/reference option), FX-PD-006 (E-stop physical topology), FX-PD-017 (enclosure/containment realization).

Acceptance of a decision does not authorize detailed design, procurement, construction, or energization, and does not resolve any Open OI/TBD entry.

## 1. Decision register

| ID | Decision topic | Options | Recommendation | Status | Authority needed | Dependencies | Risk if deferred | Closure artifact |
|----|----------------|---------|----------------|--------|------------------|--------------|------------------|------------------|
| FX-PD-001 | Fixture module decomposition | §11 functional module set | Adopt as preliminary decomposition | PROPOSED_DESIGN → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | REQ-DCC-V-FX-* | Rework of downstream design | WP-015 acceptance |
| FX-PD-002 | Base-energy control architecture | source-gated single path · segmented path | Source-gated with independent removal | PROPOSED_DESIGN → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | thresholds Open | Ambiguous energy control | WP-015 acceptance |
| FX-PD-003 | External-energy exclusivity | mutually exclusive modes · concurrent (needs GND) | Mutually exclusive while OI-GND-001 Open | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | OI-GND-001 | Combined-energy hazard | OI-GND-001 package |
| FX-PD-004 | Ground/reference option | GND-OPTION-A/B/C/D1/D2 | Defer to dedicated package | BLOCKED_BY_ARCHITECTURE → **DEFERRED** (Architecture Review 2026-07-21; remains Open/Blocked, not rejected) | Architect | OI-GND-001 | Blocks external/measurement design | OI-GND-001 decision |
| FX-PD-005 | Back-feed-prevention functional placement | at ext boundary · at base entry · dual | At external-energy boundary (topology-neutral) | PROPOSED_DESIGN → **ACCEPTED CONDITIONALLY** (Architecture Review 2026-07-21; realization remains blocked) | Architect | OI-GND-001; OI-PROT-001 | Base overstress risk | Protection package |
| FX-PD-006 | E-stop path architecture | E-STOP-OPT-1…4 | Defer selection; keep AUTH-inhibit-if-unconfirmed | BLOCKED_BY_ARCHITECTURE → **DEFERRED** (Architecture Review 2026-07-21; remains Open/Blocked, not rejected) | Architect | REQ-DCC-V-FX-071 | Unsafe E-stop assumption | E-stop package |
| FX-PD-007 | Energy-removal observation | command-confirm · independent observe | Independent physical observation required | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | measurement design | False safe belief | Measurement design |
| FX-PD-008 | Discharge observation | assume decay · confirm residual | Confirm safe residual before recovery | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | timing Open | Residual-energy hazard | Discharge design |
| FX-PD-009 | Load-bank architecture | resistive · electronic · hybrid | Sink-function architecture; independent energy origination prohibited; returned-energy reverse-flow separately controlled (BLOCKED_BY_ARCHITECTURE until OI-BI-001/OI-GND-001) | ALTERNATIVE_UNDER_EVALUATION → **ACCEPTED CONDITIONALLY** (Architecture Review 2026-07-21; realization remains blocked) | Architect | ratings Open (ED-IN-022); OI-BI-001; OI-GND-001 | Premature selection; unbounded returned energy | Load-bank design |
| FX-PD-010 | Load-bank stuck-on containment | AUTH revoke only · upstream removal | Upstream inhibit/remove + lockout | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | — | Stuck-on hazard | WP-015 acceptance |
| FX-PD-011 | DAQ responsibility split | DUT-diagnostic-as-evidence · independent reference | Independent reference for evidence candidates | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | OI-SENSE-001 | Non-independent evidence | Measurement design |
| FX-PD-012 | Reference measurement independence | shared · independent instrument | Independent reference where verification depends on it | PROPOSED_DESIGN → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | calibration Open | Weak verification | Measurement design |
| FX-PD-013 | Fault-injection authorization | UI-authorized · safety-layer-authorized | Safety-layer-authorized, default inhibited | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | ADR-023 | Unauthorized fault | Fault package |
| FX-PD-014 | DUT interface grouping | combined · grouped by energy/safety class | Grouped by energy/safety class | PROPOSED_DESIGN → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | — | Cross-class coupling | DUT interface design |
| FX-PD-015 | Operator control authority | UI-authoritative · request-only + safety layer | Request-only; safety layer decides | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | PWR-A-024 | UI-owned hazard | WP-015 acceptance |
| FX-PD-016 | Lockout/recovery authority | auto-recover · deliberate operator | Deliberate operator + interlock validation | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | — | Unsafe auto-recovery | WP-015 acceptance |
| FX-PD-017 | Preliminary enclosure/containment boundary | single enclosure · modular · open-bench-with-guarding | Defer; containment functional only | BLOCKED_BY_DETAILED_DESIGN → **DEFERRED** (Architecture Review 2026-07-21; remains Open/Blocked, not rejected) | Architect | ADR-DK-011/012 | Exposed-energy risk | ADR-DK-011/012 |
| FX-PD-018 | Measurement-connection energy/fault model | treat as potential energy/reference/fault path · assume non-energy | Treat every measurement connection as potential energy/reference/fault path until qualified | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | OI-GND-001; OI-SENSE-001; fault-energy/impedance/protection Open | Unsafe measurement path; cross-envelope link | Measurement design + OI-GND-001 |
| FX-PD-019 | Regenerative/returned-energy containment | sink-only (rejected as absolute) · sink-function + explicit reverse-flow containment | Sink-function + explicit returned-energy containment; no independent origination | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | OI-BI-001; OI-GND-001 | Uncontained returned energy | OI-BI-001 disposition |
| FX-PD-020 | Interlock effective-action allocation | AUTH/control gating vs hardware-effective [S] | [A]/[C] by default; [S] only as Proposed allocation with named blocker + proof artifact | PROPOSED_CONSTRAINT → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | REQ-DCC-V-FX-071; energy-removal/back-feed proofs | Over-claimed safety-effective paths | Detailed safety design |
| FX-PD-021 | GND-OPTION-D split | single D option (rejected) · D1 physically separate / D2 mutually exclusive modes | Split into D1/D2; D2 requires separate back-feed analysis/evidence | PROPOSED_DESIGN → **ACCEPTED** (Architecture Review 2026-07-21) | Architect | OI-GND-001 | Conflated fault/back-feed properties | OI-GND-001 decision package |

## 2. Governance

- Architect Review (2026-07-21) has assigned ACCEPT / ACCEPT CONDITIONALLY / DEFER per entry (see §0). No entry was self-approved by the Implementation Engineer; deferred entries remain Open/Blocked (not rejected).
- Recommendations are Implementation Engineer proposals only; they do not constitute approval or selection.
- Options do not name manufacturers, MPNs, connectors, conductors, or ratings.

## 3. Traceability

REQ-DCC-V-FX-* · OI-GND-001 · OI-PROT-001/002 · OI-SC-001 · OI-FIX-002 · OI-BI-001 · OI-SENSE-001 · ADR-022/023 · ADR-DK-011/012 · PWR-A-024 · ED-IN-022 · REQ-DCC-V-FX-071.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial preliminary design decision register (FX-PD-001…017) — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — FX-PD-009 sink-function wording; added FX-PD-018 (measurement path), FX-PD-019 (returned energy), FX-PD-020 (interlock [S] allocation), FX-PD-021 (GND-D1/D2 split) |
| 1.2 | 2026-07-21 | Architecture Review Accepted — per-entry FX-PD dispositions (accept/conditional/defer); Open decisions retained |
