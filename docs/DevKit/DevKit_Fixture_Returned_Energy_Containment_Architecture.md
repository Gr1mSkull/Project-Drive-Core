# DevKit Fixture Returned-Energy Containment Architecture — WP-016

**Document ID:** DOC-DK-FRECA-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Architecture DECISION PROPOSAL only. No absorber, clamp, resistor, rating, or numeric energy bound selected.
The load bank does not originate an independent source envelope. Returned energy is a reverse-flow condition.
OI-BI-001 and OI-GND-001 remain OPEN.
```

## 1. Issue (exact)

`FX-PD-009` (load-bank architecture) is **ACCEPTED CONDITIONALLY**: sink-function accepted; regenerative/returned-energy realization blocked by `OI-BI-001` and `OI-GND-001` and future bounded-energy design. WP-016 evaluates a Gen1 returned-energy policy without selecting hardware or a numeric energy bound.

## 2. Accepted constraints (inputs)

```text
The load bank does not originate an independent source envelope. (PWR-A-023)
Returned energy remains a reverse-flow energy condition requiring explicit containment.
Do not assume the source can absorb returned energy.
E_FAULT / bounded-energy uses proven bounds only; else BLOCKED_BY_INPUT.
```

## 3. Options evaluated

`RE-OPTION-A` source capable of controlled absorption · `RE-OPTION-B` separate absorption/dump function · `RE-OPTION-C` local clamp with bounded stored energy · `RE-OPTION-D` prohibit regenerative profiles in Gen1 fixture · `RE-OPTION-E` physically separate returned-energy fixture · `DEFER`.

### 3.1 Comparison

| Criterion | A source absorb | B separate dump | C local clamp | D prohibit (Gen1) | E separate fixture |
|-----------|-----------------|-----------------|---------------|-------------------|--------------------|
| Energy origin | DUT/bridge return | DUT/bridge return | DUT/bridge return | n/a (excluded) | DUT/bridge return |
| Direction | Reverse to source | Reverse to dump | Reverse to clamp | — | Reverse to separate rig |
| Storage mechanism | Source input stage | Dump element | Clamp + bounded store | — | Separate rig |
| Source absorption capability | **Assumed — must be proven** | Not required | Not required | Not required | Not required |
| Upstream overvoltage risk | High if source cannot absorb | Low | Bounded | None | Low |
| Back-feed risk | Toward source | Contained at dump | Contained locally | None | Separated |
| Measurement requirements | Signed I; source V | Signed I; dump state | Signed I; clamp V | None | Signed I (separate) |
| Energy-removal behavior | Source-dependent | Dump removal | Clamp + removal | n/a | Separate removal |
| Discharge behavior | Source-dependent | Dump discharge | Bounded decay | n/a | Separate discharge |
| Failure behavior | OV if absorb fails | Dump fail → OV | Clamp fail → OV | Safe (excluded) | Separated |
| Thermal dependency | Source rating | Dump rating | Clamp rating | None | Separate rating |
| OI-GND-001 dependency | Yes | Yes | Yes | Low | Yes (separate) |
| OI-BI-001 dependency | Yes | Yes | Yes | Resolves by exclusion | Yes |
| Proof requirements | Source absorption proof | Dump sizing proof | Clamp energy proof | Exclusion interlock proof | Separate-rig proof |

## 4. Recommendation

```text
Recommended Gen1 returned-energy policy: D (prohibit regenerative profiles in the
Gen1 fixture), with RE-OPTION-B / RE-OPTION-E retained as future options for a later
bidirectional-capable fixture.
```

Rationale: Gen1 verification scope does not require regenerative operation to be executed now, and RE-OPTION-A (source absorption) must not be assumed. **D** removes the reverse-flow hazard by exclusion (with an exclusion interlock), is consistent with the current `BLOCKED_BY_ARCHITECTURE` status of returned energy, and does not require a numeric energy bound. If the Architect later requires regenerative testing, **B** (separate dump) or **E** (separate fixture) are preferred over **A**; **C** (local clamp) requires a proven bounded-energy design (`BLOCKED_BY_INPUT`).

This does not reclassify the load bank as an independent source. Sink-function architecture (`FX-PD-009`) is unchanged.

## 5. Residual risks / proof obligations

- If regenerative profiles are later authorized, source-absorption assumptions must be proven or avoided (B/E).
- Exclusion interlock (D) requires proof that regenerative profiles cannot be commanded.
- No numeric energy bound approved.

## 6. Proposed issue disposition

| Issue | Existing status | WP-016 recommendation | Residual blocker | Proposed Architect action |
|-------|-----------------|-----------------------|------------------|---------------------------|
| FX-PD-009 (returned-energy realization) | ACCEPTED CONDITIONALLY | Adopt Gen1 policy D (prohibit regen); keep sink-function | OI-BI-001; OI-GND-001; bounded-energy design (if regen later) | ACCEPT CONDITIONALLY (policy D) |
| OI-BI-001 | OPEN | SPLIT: architecture-closed (Gen1 excludes regen) + implementation-open (future bidirectional topology) | Future regen design | ACCEPT ARCHITECTURE; SPLIT / DEFER |

`OI-BI-001` remains Open; no numeric energy bound approved.

## 7. Traceability

FX-PD-009/019 · OI-BI-001 · OI-GND-001 · OI-FIX-002 · PWR-A-023 · ED-IN-021/022 · WP-014 E_FAULT governance.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial returned-energy containment architecture — Proposed |
