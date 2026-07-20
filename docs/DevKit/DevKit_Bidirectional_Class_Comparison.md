# DevKit Bidirectional Class Comparison — WP-013

**Document ID:** DOC-DK-BCC-001  
**Version:** 1.1  
**Status:** Ready for Final Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20

```text
Class comparison only — no dead time, stall current, retry timing, or MPN Approved.
```

## 1. Purpose

Compare bidirectional architecture classes for **CH-BI-REP** (ADR-019 mandatory capability alias). Owners: **OI-COMP-002**, **OI-BI-001**, **ED-IN-031**, stall fixture **ED-IN-020** / **OI-FIX-002**.

## 2. Classes under evaluation

| Class ID | Definition |
|----------|------------|
| **BI-HB-FULL** | Integrated full H-bridge |
| **BI-HB-DISCRETE** | Discrete full H-bridge with gate control |
| **BI-HB-HYBRID** | Integrated control/protection with external power devices |
| **BI-RELAY-REVERSING** | Reversing relay / contact architecture |
| **BI-DUAL-HSLS** | Coordinated high-side / low-side switching architecture |

WP-011 also listed BI-HB-HALF / BI-DUAL-SW as related concepts; WP-013 evaluates the five classes above as the comparison set.

## 3. Criterion matrix

| Criterion | BI-HB-FULL | BI-HB-DISCRETE | BI-HB-HYBRID | BI-RELAY-REVERSING | BI-DUAL-HSLS |
|-----------|------------|----------------|--------------|--------------------|--------------|
| Direction control | Integrated | Gate logic | Integrated ctrl | Contact polarity | Coordinated HS/LS |
| Safe neutral | Coast/brake modes claim-dependent | Designer-defined | Claim-dependent | Mid/off contacts | All OFF |
| Shoot-through prevention | Integrated dead-time (value Open) | External dead-time (Open) | Combined | N/A (mech) | Interlock required |
| Dead-time responsibility | Device / controller | Firmware/HW timer | Split | N/A | HW interlock / timing |
| Stall handling | Current limit + thermal (Open) | Same + layout | Same | Contact I²t | Same |
| Current direction observation | Needs BI-capable SENSE-* | Same | Hybrid preferred | Limited | Dual path sense |
| Regenerative energy path | Bridge recirculation / return | Same | Same | Limited / none | Topology-dependent |
| Braking / coast | Mode-dependent | Designer | Claim-dependent | Coast natural; brake limited | Mode-dependent |
| KILL behaviour | Hard disable all legs | Gate pull-downs | Hard disable | Drop coil / open | Hard disable both sides |
| Control-loss behaviour | Safe OFF / coast (policy Open; TBD-DK-007) | Same | Same | Drop to safe contact state | Same |
| Fault containment | Bridge-local | Layout | Combined | Contact weld risk | Cross-side faults |
| Thermal accumulation | Retry accumulation model needed | Same | Same | Contact heating | Coupled HS/LS |
| Diagnostic granularity | Device flags | External | Dual | Contact sense limited | Dual path |
| Verification complexity | High (stall fixture) | Higher | High | Medium electromechanical | High |
| CH-BI-REP compatibility | Strong if PWM/current claims met | Strong | Strong | Weak for PWM/dynamic BI verification | Viable with interlock proof |

## 4. Symbolic relationships (no numeric substitution)

### Separated energy quantities

| Symbol | Meaning |
|--------|---------|
| `E_SOURCE_STALL` | Source-referred electrical energy during stall |
| `E_BRIDGE_LOSS` | Bridge dissipation energy (not equal to source energy) |
| `E_LOAD_ABSORBED` | Energy absorbed in the load |
| `E_RETURNED` | Energy returned toward the source |
| `E_CLAMPED` | Energy absorbed in clamp/protection paths |

```text
E_SOURCE_STALL =
∫ V_ENTRY(t) × I_CH_IN_BI(t) dt
```

```text
E_BRIDGE_LOSS =
∫ P_BRIDGE_LOSS(t) dt
```

```text
P_BRIDGE_LOSS =
P_CONDUCTION_LEGS
+ P_SWITCHING
+ P_GATE_CONTROL
+ P_SENSE
+ P_CLAMP_SHARE
```

**Do not** treat `E_SOURCE_STALL` as semiconductor thermal loss.

### Retry thermal-state evolution

```text
T_END_k =
thermal_response(T_START_k, P_BRIDGE_LOSS_k(t), Z_TH(t))

T_START_(k+1) =
T_AMBIENT + cooling_model(T_END_k, T_AMBIENT, Δt_k, thermal_state)
```

Exact `Z_TH(t)` remains Open. Steady-state `P × R_TH` is **not** the sole model for short stall pulses or retry accumulation.

### Bridge conduction (profile-consistent)

Apply SPC §2 current-symbol discipline (`I_ON` / `I_RMS_PROFILE`) — no double duty factor.

### Returned energy (source-referred)

```text
I_CH_IN_BI(t) = signed_net_source_referred(... direction_n ...)
```

When net energy returns toward source: **`I_CH_IN_BI < 0`**. Do **not** also count in `I_STORAGE_NET` unless unallocated shared storage is explicitly modelled (WP-012 R3–R5).

### Source absorption dependency

```text
P_RETURN_ABSORBED = f(source sink capability, clamp path, fixture absorption)
```

If source cannot absorb return: energy must be modelled in clamp/fixture — still without double-count in entry budget.

## 5. Summary table

| Class | CH-BI-REP fit | Shoot-through model | Regen accounting | Main blockers | Qualification status | Recommendation |
|-------|---------------|---------------------|------------------|---------------|----------------------|----------------|
| **BI-HB-FULL** | Strong | Integrated (timing Open) | Signed `I_CH_IN` | ED-IN-020/031; OI-BI-001; thermal | **CLASS_CONDITIONALLY_VIABLE** | **CONDITIONALLY_RECOMMENDED** |
| **BI-HB-DISCRETE** | Strong | External (Open) | Same | Same + layout | **CLASS_CONDITIONALLY_VIABLE** | **RETAIN_FOR_COMPARISON** |
| **BI-HB-HYBRID** | Strong | Combined | Same | Same | **CLASS_CONDITIONALLY_VIABLE** | **RECOMMENDED_FOR_NEXT_STAGE** if external FET needed for envelope |
| **BI-RELAY-REVERSING** | Weak for dynamic PWM BI | N/A | Poor regen model | PWM/stall verification mismatch | **CLASS_NOT_RECOMMENDED** as primary CH-BI-REP | **NOT_RECOMMENDED** |
| **BI-DUAL-HSLS** | Viable | Interlock mandatory | Topology-dependent | OI-BI-001 interlock proof | **CLASS_CONDITIONALLY_VIABLE** | **RETAIN_FOR_COMPARISON** |

If dead-time, stall current, or retry timing required as Approved values: result is **BLOCKED_BY_INPUT** — not an invented recommendation.

## 6. Recommendations (not Accepted)

- **Preferred direction:** BI-HB-FULL when integrated ratings cover CH-BI-REP verification; else **BI-HB-HYBRID**.
- **Fallback:** BI-HB-DISCRETE or BI-DUAL-HSLS with explicit interlock architecture.
- **Reject as primary:** BI-RELAY-REVERSING for Gen1 DevKit CH-BI-REP dynamic verification.

## 7. Traceability

REQ-DCC-V-DK-042 · ADR-019 · ED-IN-020/031 · OI-COMP-002 · OI-BI-001 · OI-FIX-002 · WP-012 R1–R5 · VER-DCC-DK-C-011.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial bidirectional class comparison — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — separated stall/bridge energies; thermal-state retry model |
