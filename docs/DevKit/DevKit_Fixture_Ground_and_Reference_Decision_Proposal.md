# DevKit Fixture Ground and Reference Decision Proposal — WP-016

**Document ID:** DOC-DK-FGRDP-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Baseline:** WP-015 Accepted (`8652340`)  
**Date:** 2026-07-21

```text
Architecture DECISION PROPOSAL only. No component, connector, conductor, rating, or numeric selected.
OI-GND-001 remains OPEN until the System Architect accepts a disposition.
A recommendation is not an acceptance; the Implementation Engineer does not self-approve.
```

## 1. Issue (exact)

`OI-GND-001` — the ground/reference relationship between the base DevKit energy envelope and the external energy envelope is undecided. `FX-PD-004` (ground/reference option) is **DEFERRED**; `FX-PD-005` (back-feed-prevention placement) is **ACCEPTED CONDITIONALLY** pending OI-GND-001/OI-PROT-001. While OI-GND-001 is Open, simultaneous BASE + external energization is prohibited and combined-energy profiles are `BLOCKED_BY_ARCHITECTURE`.

## 2. Accepted constraints (inputs)

| Constraint | Source | Status |
|-----------|--------|--------|
| Base and external envelopes distinct | PWR-A-001; ADR-021 | ACCEPTED_INPUT |
| External ratings do not extend base rating | PWR-A-002 | ACCEPTED_INPUT |
| Back-feed into base distribution prohibited | PWR-A-003 | ACCEPTED_INPUT |
| EXTERNAL_ENERGY_ARMED is authorization only | WP-015 FFA §5.1 | ACCEPTED_INPUT |
| No simultaneous BASE+EXT while OI-GND-001 Open | WP-015 (FX-PD-003 Accepted) | ACCEPTED_INPUT |
| Measurement connection = potential energy/reference/fault path until qualified | WP-015 (FX-PD-018 Accepted) | ACCEPTED_INPUT |

## 3. Options evaluated

`GND-OPTION-A` controlled common reference · `GND-OPTION-B` single-point reference · `GND-OPTION-C` galvanically separated measurement/control boundary · `GND-OPTION-D1` physically separate fixture/interconnection arrangements · `GND-OPTION-D2` shared fixture with mutually exclusive modes.

### 3.1 Comparison

| Criterion | A (common ref) | B (single-point) | C (galvanic sep) | D1 (separate fixtures) | D2 (exclusive modes) |
|-----------|----------------|------------------|------------------|------------------------|----------------------|
| Base/external relationship | Shared reference | One bonding node | Decoupled domains | No shared hazardous interconnection | Shared fixture, time-separated |
| Current return paths | Common return | Defined single return | Isolated returns | Per-arrangement returns | Per-mode returns |
| Fault-current paths | Common-mode exposure | Single-point dependent | Barrier-bounded (if qualified) | Physically separated | Mode-dependent; back-feed not inherently prevented |
| Measurement references | Simple, one frame | One reference node | Isolated sensing required | Per-arrangement | Per-mode |
| Instrument-ground behavior | Shared — risk of loops | Controlled at one node | Isolated | Independent | Shared hardware; mode risk |
| CAN/service connections | Common reference | Single-point | Isolated interface needed | Independent | Shared |
| KILL/enable observation | Common ref | Single-point ref | Isolated observe | Independent | Shared |
| Back-feed risk | Requires active prevention function | Requires directional function | Barrier reduces (if qualified) | Physical separation | **Not proven by mode exclusivity alone** |
| Common-mode fault risk | Higher | Moderate | Lower (if qualified) | Low | Moderate |
| Operator error | Moderate | Moderate | Lower | Lower (separate) | Higher (mode confusion) |
| Complexity class (no price) | Moderate | Moderate | Higher | Lower–Moderate | Lower–Moderate |
| Test coverage | Combined-mode possible (needs GND proof) | Combined-mode possible | Combined-mode possible | Combined-mode excluded | Combined-mode time-shared |
| Required protection functions | Back-feed prevention + common-mode analysis | Directional + single-point integrity | Isolation qualification | Interconnection analysis | Mode-exclusion + back-feed analysis |
| Required proof | Common-mode fault analysis; back-feed evidence | Single-point integrity analysis; back-feed evidence | Isolation qualification (normal + fault) | Separation/interconnection analysis | Mode-exclusion interlock proof **plus** separate back-feed analysis/evidence |
| Residual risks | Common-mode propagation | Single-point failure | Isolation integrity failure | Coordination overhead | Back-feed if exclusivity fails |
| Detailed-design blockers | Numeric envelopes; protection class | Same | Isolation qualification; measurement isolation | Fixture arrangement design | Interlock + back-feed proof |

## 4. Recommendation

```text
Recommended option: DEFER (primary), with GND-OPTION-D1 retained as the
lowest-residual-risk near-term configuration for the base-only + external-only
(mutually exclusive) verification already permitted while OI-GND-001 is Open.
```

Rationale: WP-015 already prohibits simultaneous BASE+EXT while OI-GND-001 is Open. **D1** (physically separate arrangements) preserves the strongest inherent back-feed separation and matches the current mutually-exclusive operating constraint without selecting an isolation topology or numeric envelope. Options **A/B/C** enabling combined-mode operation require numeric envelopes (Open) and qualification evidence not yet available, so a combined-mode selection is **premature**. **D2** is not recommended as the near-term basis because mode exclusivity alone does not prove back-feed prevention.

Primary disposition: **DEFER** the combined-mode ground/reference selection; recommend the Architect either (a) keep OI-GND-001 Open, or (b) **split** it into an architecture-closed part ("mutually-exclusive base/external operation with physical separation, D1") and an implementation-open part ("combined-mode reference topology"). Alternatives A/B/C retained as future configurations.

`OI-GND-001` is **not** marked Resolved.

## 5. External-energy and back-feed allocation (§12)

Functional elements: `EXT-SOURCE`, `EXT-ENERGY-CONTROL`, `EXT-POWER-MODULE`, `EXT-LOAD-BANK`, `BASE-ENERGY-PATH`, `BACK-FEED-PREVENTION`.

For the near-term recommended basis (D1 / mutually exclusive):

| Aspect | Allocation |
|--------|-----------|
| Permitted energy directions | Source → controlled path → DUT/sink, per active envelope only |
| Prohibited energy directions | External → base distribution (back-feed); simultaneous BASE+EXT while OI-GND-001 Open |
| Source/sink roles | EXT-SOURCE/EXT-POWER-MODULE = source; EXT-LOAD-BANK = sink-function (no independent origination) |
| Authorization dependencies | `AUTH_EXT_SOURCE` / `AUTH_EXT_POWER_MODULE` / `AUTH_LOAD_BANK`; base AUTH mutually exclusive with external AUTH |
| Observation dependencies | Envelope-tagged entry/return observation; back-feed observation |
| First protective function | Fixture back-feed-prevention function (`FX-PD-005`; topology-neutral, realization Open) |
| Backup energy-removal function | Independent external energy removal (`FX-ENERGY-REMOVAL`) |
| Safe minimum | No uncontrolled energization of base distribution |
| Lockout condition | Back-feed detected/possible → inhibit external energization; `FX_LOCKOUT_UNCONFIRMED` until confirmed |
| Recovery condition | Deliberate, from `FX_LOCKOUT_SAFE` only, after confirmation |
| Required detailed-design evidence | Back-feed-prevention characteristics; base/external V–I; accepted OI-GND-001 disposition |

Preserved: external ratings do not extend the base rating; back-feed into base distribution is prohibited; authorization revoke does not prove energy removal.

## 6. Residual risks

- Combined-mode operation remains architecturally blocked (numeric + qualification gaps).
- Back-feed-prevention realization depends on OI-GND-001 and OI-PROT-001.
- Measurement reference across envelopes remains a potential fault path (see measurement-safety architecture).

## 7. Proposed issue disposition

| Issue | Existing status | WP-016 recommendation | Residual blocker | Proposed Architect action |
|-------|-----------------|-----------------------|------------------|---------------------------|
| OI-GND-001 | OPEN | SPLIT (architecture-closed: mutually-exclusive D1 basis; implementation-open: combined-mode reference) **or** DEFER | Numeric envelopes; isolation/back-feed qualification | ACCEPT ARCHITECTURE; SPLIT IMPLEMENTATION RESIDUAL / DEFER |
| FX-PD-004 | DEFERRED | Remains DEFERRED (or advance D1 basis if Architect accepts) | OI-GND-001 | DEFER / ACCEPT CONDITIONALLY |
| FX-PD-005 | ACCEPTED CONDITIONALLY | Back-feed at external boundary retained; realization Open | OI-GND-001; OI-PROT-001 | ACCEPT CONDITIONALLY |

## 8. Downstream authorization if accepted

If the Architect accepts D1 as the near-term basis: external/base **mutually-exclusive** detailed-design inputs (non-numeric) become `READY_IF_ACCEPTED`; combined-mode remains BLOCKED. No procurement/construction/energization.

## 9. Traceability

OI-GND-001 · OI-PROT-001 · FX-PD-003/004/005/018 · PWR-A-001/002/003 · ADR-020/021 · REQ-DCC-V-FX-005/030…034.

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial ground/reference decision proposal + external-energy/back-feed allocation — Proposed |
