# DevKit Fixture Protection Architecture Decision Proposal — WP-016

**Document ID:** DOC-DK-FPADP-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Architecture CLASS decision proposal only. No component, device, MPN, rating, or numeric selected.
OI-PROT-001 and OI-PROT-002 remain OPEN until the System Architect accepts a disposition.
```

## 1. Issues (exact)

- `OI-PROT-001` — reverse-polarity protection architecture undecided.
- `OI-PROT-002` — transient-protection architecture undecided.

Related Accepted constraints: `PWR-A-003` (back-feed prohibited), `PWR-A-017` (PSU current limit is not the sole protection layer — ACCEPTED_CONSTRAINT), `PWR-A-018` (software-commanded OFF is not hardware fault containment — ACCEPTED_CONSTRAINT).

## 2. Protection layers (distinct; carried from WP-012)

```text
P0 source limitation              — bench/source current limit (not sole protection, PWR-A-017)
P1 fixture protection             — fixture wiring/controls; E-stop; energy interlock
P2 DevKit input protection        — entry to base DevKit (RP, transient clamp, replaceable OCP)
P3 domain protection              — Logic/Radio/Power rails
P4 channel protection             — per-output channel
P5 functional safe-state control  — KILL / nENABLE_GLOBAL / watchdog / control-loss (not overcurrent, PWR-A-018)
```

Layers are not interchangeable; a single layer is not sole protection.

## 3. Architecture classes evaluated (no components/ratings)

`series blocking function` · `controlled ideal-diode function` · `directional protection function` · `replaceable protection function` · `clamping function` · `crowbar/diversion function` · `source-side shutdown` · `hybrid layered architecture`.

### 3.1 OI-PROT-001 reverse-polarity architecture

| Class | Normal | Single-fault | Recovery | Downstream impact | Proof required |
|-------|--------|--------------|----------|-------------------|----------------|
| Series blocking function | Low loss block on reverse | Must handle continuous reverse | Auto after correction | Conduction loss budget | Reverse withstand; loss/thermal |
| Controlled ideal-diode function | Low loss; active | Control-fault behavior | Auto/latched per design | Control integrity | Fault-mode behavior proof |
| Directional protection function | Directional allow/block | Directional-fault behavior | Per design | Coordination with P0/P2 | Directional integrity |
| Source-side shutdown (P0) | Prevent reverse at source | Not sole protection (PWR-A-017) | Deliberate | Requires backup | Not sufficient alone |

Recommendation (class): **hybrid** — a P2 reverse-blocking/directional function backed by P0 source behavior; **series blocking or controlled ideal-diode class** as the primary P2 reverse-polarity function, with backup energy removal. Final class selection **DEFERRED** pending numeric envelopes and component-class qualification. Status: `READY_FOR_ARCHITECT_DECISION` (class direction) / `BLOCKED_BY_THRESHOLD` (final selection).

### 3.2 OI-PROT-002 transient-protection architecture

| Class | Normal | Single-fault | Recovery | Downstream impact | Proof required |
|-------|--------|--------------|----------|-------------------|----------------|
| Clamping function | Absorb bounded transient | Clamp energy exceed → fail | Auto if within rating | Energy share vs P0/P1 | Clamp energy; coordination |
| Crowbar/diversion function | Divert on threshold | Nuisance/latch risk | Deliberate | Interrupt coordination | Threshold/timing proof |
| Source-side foldback (P0) | Limit at source | Not sole protection | Auto | Requires backup | Not sufficient alone |
| Hybrid layered | Clamp + upstream removal | Layered | Per design | Coordination | Layer coordination proof |

Recommendation (class): **hybrid layered** — a P2 clamping function coordinated with P0 foldback and P1/P2 energy removal; crowbar/diversion retained as alternative where clamp energy is insufficient. Final class **DEFERRED** pending transient waveform envelope (Open). Status: `READY_FOR_ARCHITECT_DECISION` (class direction) / `BLOCKED_BY_INPUT` (waveform/energy bounds).

## 4. Per-hazard protection allocation (architecture-level)

| Hazard | First layer | Backup layer | Energy source | Protected path | Safe minimum | Containment boundary | Diagnostic | Retry/latch | Proof | Numeric dependency |
|--------|-------------|--------------|---------------|----------------|--------------|----------------------|------------|-------------|-------|--------------------|
| Reverse polarity (input) | P2 RP function | P0 source + P1 removal | External source | Base entry | No DUT energization on reverse | Entry boundary | Fault log if powered | Open | RP withstand | I/V envelope Open |
| Input transient/OV | P2 clamp | P0 foldback + P1 removal | Source/load dump | P3/P4 downstream | No downstream damage | Entry boundary | Event capture | Open | Clamp energy | Waveform Open |
| Input overcurrent | P0 then P2 | P5 disable | Source | Harness/entry | No sustained heat | Entry/domain | OC log | Open | Fuse/OCP curve | I_certified_cont Open |
| Input short circuit | P0/P1/P2 | Physical disconnect | Source | Entry conductors | Energy bounded | Entry | SC capture | Open | Interrupt/withstand | I_psc Open (BLOCKED_BY_INPUT) |
| External back-feed | Fixture back-feed-prevention (P1/P2) | External/upstream removal | External | Base distribution | No uncontrolled base energization | Boundary | Interlock status | Open | Back-feed evidence | OI-GND-001 |

## 5. Recommendation summary

```text
OI-PROT-001: PROPOSED_DISPOSITION — accept reverse-polarity CLASS direction
             (series blocking / controlled ideal-diode, P2, backed by P0/P1);
             final class + rating DEFERRED (numeric + component qualification).
OI-PROT-002: PROPOSED_DISPOSITION — accept transient-protection CLASS direction
             (hybrid layered clamp + P0 foldback + removal);
             final class + energy bound DEFERRED (waveform Open → BLOCKED_BY_INPUT).
```

Both remain **OPEN** pending Architecture Review. No device or rating selected; PSU limit is not sole protection; software OFF is not fault containment.

## 6. Proposed issue disposition

| Issue | Existing status | WP-016 recommendation | Residual blocker | Proposed Architect action |
|-------|-----------------|-----------------------|------------------|---------------------------|
| OI-PROT-001 | OPEN | SPLIT: architecture-closed (class direction) + implementation-open (class/rating) | Numeric envelope; component qual | ACCEPT ARCHITECTURE; SPLIT / DEFER |
| OI-PROT-002 | OPEN | SPLIT: architecture-closed (hybrid layered) + implementation-open (energy bound/class) | Transient waveform/energy bound | ACCEPT ARCHITECTURE; SPLIT / DEFER |

## 7. Traceability

OI-PROT-001/002 · PWR-A-003/017/018 · WP-012 protection framework (P0–P5) · ADR-021/023 · ED-IN-008/009 · FX-PD-005.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial protection architecture decision proposal — Proposed |
