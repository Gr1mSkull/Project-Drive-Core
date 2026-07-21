# DevKit Fixture E-Stop Architecture Decision Proposal — WP-016

**Document ID:** DOC-DK-FEADP-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Architecture DECISION PROPOSAL only. No component, contactor, relay, or rating selected.
No SIL / ASIL / other integrity level is claimed. FX-PD-006 and REQ-DCC-V-FX-071 remain Open/Blocked.
```

## 1. Issue (exact)

`FX-PD-006` (E-stop path architecture) is **DEFERRED**; `REQ-DCC-V-FX-071` requires E-stop path integrity but the physical topology is Open (`BLOCKED_BY_ARCHITECTURE`). WP-015 accepted the functional constraint: hazardous-energy authorization is inhibited when E-stop integrity is unconfirmed. WP-016 evaluates topology classes to a recommendation without selecting hardware.

## 2. Accepted constraints (inputs)

| Constraint | Source | Status |
|-----------|--------|--------|
| E-stop independent of DUT physical KILL and `nENABLE_GLOBAL` | PWR-A-021 | ACCEPTED_INPUT |
| E-stop independent of DUT firmware, Radio, Tablet, SPI/DCPI | WP-014 REQ-DCC-V-FX-010 | ACCEPTED_INPUT |
| Hazardous AUTH inhibited if E-stop integrity unconfirmed | REQ-DCC-V-FX-071 | ACCEPTED_INPUT |
| E-stop reset does not energize; new command epoch required | WP-014/WP-015 | ACCEPTED_INPUT |
| `[S]` allocations are Proposed with named blocker + proof artifact | FX-PD-020 | ACCEPTED_INPUT |

## 3. Options evaluated

`E-STOP-OPT-1` monitored single safety-effective path · `E-STOP-OPT-2` independent dual safety-effective paths · `E-STOP-OPT-3` safety-effective path plus independent observation · `E-STOP-OPT-4` series safety chain with continuity monitoring · `DEFER`.

### 3.1 Comparison

| Criterion | OPT-1 monitored single | OPT-2 dual independent | OPT-3 path + independent observation | OPT-4 series chain + continuity |
|-----------|------------------------|------------------------|--------------------------------------|----------------------------------|
| Independence from DUT firmware | Yes | Yes | Yes | Yes |
| Independence from Radio/Tablet/UI | Yes | Yes | Yes | Yes |
| Independence from ordinary AUTH logic | Yes | Yes | Yes | Yes |
| Inhibit/remove hazardous energy | Yes | Yes (redundant) | Yes | Yes (chain) |
| Integrity monitoring | Continuity/proof-test | Cross-monitoring | Discrepancy detection | Continuity monitoring |
| Stuck-contact/path failure | Detected by monitor (bounded) | Redundant path covers | Observation detects | Chain break detected |
| Open-circuit failure | Fail-safe (de-energize) if monitored | Fail-safe | Fail-safe + flagged | Fail-safe |
| Short-circuit failure | Monitor-dependent | Second path covers | Observation detects | Segment-dependent |
| Loss of auxiliary supply | Must default de-energized | Must default de-energized | Must default de-energized | Must default de-energized |
| Reset behavior | Deliberate; no energize | Deliberate | Deliberate | Deliberate |
| Stale-command invalidation | Yes | Yes | Yes | Yes |
| Diagnostic coverage | Moderate (monitor quality) | High | High | Moderate–High |
| Effect on base/external paths | Single inhibit point | Redundant inhibit | Inhibit + observe | Chain inhibits all segments |
| Interaction with `FX_LOCKOUT_UNCONFIRMED` | Enters on unconfirmed integrity | Same | Same; observation aids confirm | Same |
| Single-point residual risk | Present unless monitoring proven | Lowest | Low | Segment single-point possible |
| Detailed-design dependencies | Monitor design + proof test | Dual-path design | Observation channel design | Chain + continuity design |

## 4. Recommendation

```text
Recommended E-stop option: DEFER selection between OPT-2 and OPT-3.
```

Rationale: OPT-2 (independent dual) and OPT-3 (path + independent observation) give the lowest single-point residual risk and align with the Accepted "inhibit if integrity unconfirmed" rule and `FX_LOCKOUT_UNCONFIRMED`. Selecting between them requires proof-test/diagnostic-coverage inputs and fault-tolerance allocation not yet available; **OPT-1** is not recommended as sole basis (single-point risk unless monitoring is proven); **OPT-4** is viable but adds segment single-point considerations. Recommend the Architect either DEFER or **split** `REQ-DCC-V-FX-071` into an architecture-closed part ("independent safety-effective inhibit + integrity monitoring; dual/observed class") and an implementation-open part ("selected topology + proof test").

No SIL/ASIL/integrity level is claimed.

## 5. Scope of the recommendation

The E-stop safety-effective inhibit applies to **all hazardous fixture energy**: base energy, external energy, load-bank energy, and fault-injection energy. It does **not** replace DUT physical KILL and does not depend on it.

## 6. Residual risks / proof obligations

- Diagnostic coverage and proof-test interval are Open inputs.
- Auxiliary-supply-loss default-de-energized behavior requires detailed-design proof.
- `[S]` allocation (FX-PD-020) requires a future proof artifact.

## 7. Proposed issue disposition

| Issue | Existing status | WP-016 recommendation | Residual blocker | Proposed Architect action |
|-------|-----------------|-----------------------|------------------|---------------------------|
| FX-PD-006 | DEFERRED | Advance to OPT-2/OPT-3 class; defer final topology | Proof-test/diagnostic inputs | ACCEPT ARCHITECTURE (class); SPLIT IMPLEMENTATION / DEFER |
| REQ-DCC-V-FX-071 (realization) | BLOCKED_BY_ARCHITECTURE | SPLIT: architecture-closed (independent + monitored) + implementation-open (topology + proof) | Topology + proof test | ACCEPT ARCHITECTURE; SPLIT |

Not marked closed.

## 8. Traceability

FX-PD-006/020 · REQ-DCC-V-FX-010/011/012/013/071 · PWR-A-021/022 · ADR-022.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial E-stop architecture decision proposal — Proposed |
