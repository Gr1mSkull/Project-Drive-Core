# DevKit Symbolic Preliminary Calculations — WP-013

**Document ID:** DOC-DK-SPC-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-013  
**Date:** 2026-07-20

```text
Symbolic calculations only — no numeric current, voltage, power, temperature, or timing Approved.
Uses Accepted WP-012 sign convention and anti double-count rules R1–R5.
```

## 1. Sign convention (Accepted WP-012)

```text
I > 0  →  net draw FROM the source INTO the DevKit at the entry reference
I < 0  →  net return FROM the DevKit TOWARD the source at the entry reference
```

Applies to `I_ENTRY_MEAS`, `I_DOM_IN_x`, `I_CH_IN_n`, `I_STORAGE_NET`.

`I_STORAGE_NET` = unallocated shared storage paths only; else 0. No double-count with channel/domain terms (R3–R5).  
P6 / external envelope excluded from base `I_BASE_IN_INST` / `I_certified_cont` (PWR-A-001/002).

## 2. High-side conduction loss

```text
P_COND_HS =
f(
  I_CH_IN_RMS,          # or I_LOAD_RMS with declared referral — do not mix boundaries
  effective on-state resistance or voltage drop,
  temperature,
  duty profile
)
```

Class forms:

| Class | Candidate form (symbolic) |
|-------|---------------------------|
| HS-INT-DIAG / BASIC | `P_COND ≈ I_LOAD_RMS² × R_DS(on)(T) × D` or `I_LOAD_AVG × V_drop(T) × D` |
| HS-GATE-DISCRETE | Same FET term + `P_GATE_DRIVE` |
| HS-HYBRID | Integrated path + external element terms |
| HS-ARRAY | Per-channel terms + coupling residual (not double-counted) |

Referral: convert to source-referred contribution inside `I_CH_IN_n` / `P_CH_IN_n` — do not add `I_LOAD` at entry.

## 3. PWM switching loss

```text
P_SWITCH_HS =
f(
  V_IN,
  I_LOAD,
  switching transition energy,
  f_PWM,
  duty,
  load type,
  temperature
)
```

Candidate:

```text
P_SWITCH_HS ≈ E_sw(V_IN, I_LOAD, T) × f_PWM
```

`f_PWM` = ED-IN-010 **Open**. No numeric f Approved.

## 4. Current-observation burden

```text
P_SENSE =
f(
  measurement class,
  load current,
  burden resistance or equivalent loss,
  duty,
  temperature
)
```

| Class | Symbolic burden |
|-------|-----------------|
| SENSE-INTEGRATED | Device quiescent + sense-path loss (datasheet class TBD) |
| SENSE-SHUNT-HS/LS | `I_LOAD_RMS² × R_SHUNT` (+ amp supply) |
| SENSE-MAGNETIC | Sensor supply + negligible series R |
| SENSE-INDIRECT | Compute only (no electrical burden) |
| SENSE-HYBRID | Integrated + shunt terms — allocate once |

Include sense burden in `I_CH_IN_n` or domain term — **not** again in `I_STORAGE_NET`.

## 5. Domain conversion

```text
P_DOM_IN_x = P_DOM_LOAD_x / η_x
I_DOM_IN_x = signed_source_referred(P_DOM_IN_x, V_IN)
```

`η_x` Open — component/topology dependent. Domains: LOGIC, RADIO, POWER_CTRL.

## 6. Entry power reconciliation

```text
P_ENTRY(t) = V_IN(t) × I_ENTRY_MEAS(t)

I_ENTRY_MEAS(t) ≈
  I_DOM_IN_LOGIC(t)
+ I_DOM_IN_RADIO(t)
+ I_DOM_IN_PWR(t)
+ Σ I_CH_IN_n(t)
+ I_STORAGE_NET(t)
```

No cross-boundary sum of `I_LOAD_n` with rail currents.

## 7. Fault energy

```text
E_FAULT = ∫ V(t) × I(t) dt
```

Class-specific required inputs (all Open unless noted):

| Protection class family | Required symbolic inputs |
|-------------------------|--------------------------|
| RP-* | Reverse V profile; conduction path; clearing/block behaviour |
| TRANSIENT-* | Surge waveform class; clamp/disconnect timing; energy share vs P0/P1 |
| INPUT-* | Replaceable clearing integral; electronic limit trajectory; coordination with continuous envelope |
| CH-* | `I_FAULT_PEAK`, `T_FAULT_CLEAR`, channel clamp path; P5 interaction |

## 8. Thermal relationship

```text
T_ELEMENT = T_AMBIENT + P_LOSS × R_TH_EFFECTIVE
R_TH_EFFECTIVE = f(R_th_junction, R_th_board, R_th_enclosure, airflow, coupling)
```

PCB derating candidate (non-normative):

```text
I_PCB_cont(T) = I_PCB_cont(T_ref) × sqrt((T_max - T)/(T_max - T_ref))
```

**Candidate analytical form only** — not normative (WP-012-R1). ADR-DK-011 Open.

## 9. Bidirectional stall and regeneration

```text
E_STALL = ∫ V_BRIDGE(t) × I_STALL(t) dt
E_RETRY_ACCUM = Σ_k E_STALL_k   # with cooling intervals — model Open
P_COND_BRIDGE = f(I_RMS_leg, R_on_leg(T), conducting devices, duty)
I_CH_IN_BI = signed_net_source_referred(... direction ...)
```

Returned energy → negative `I_CH_IN_BI` when net return to source; source absorption dependency explicit; no double-count in `I_STORAGE_NET`.

## 10. Uncertainty register (per calculation family)

| Uncertainty type | Owner | Notes |
|------------------|-------|-------|
| Input uncertainty | Architect / ED-IN owners | Thresholds Open |
| Model uncertainty | Implementation Engineer | Candidate forms labelled |
| Component-class uncertainty | Component Engineer | Until class Accepted |
| Temperature uncertainty | Thermal (ADR-DK-011) | R_TH Open |
| Measurement uncertainty | Test / fixture WP | E_TOTAL model § sense doc |
| Margin owner | System Architect | Categories only — no % Approved |
| Double-count risk | IE — WP-012 R3–R5 | Audit entry reconciliation |

## 11. Calculation readiness table

| Calculation | Required inputs | Available inputs | Missing inputs | Permitted output | Readiness | Blocking artifact |
|-------------|-----------------|------------------|----------------|------------------|-----------|-------------------|
| HS conduction loss | Class R_on/V_drop model; I profile; T; D | Symbolic method; class options | ED-IN-002/026; T; R_TH; MPN data | Symbolic / candidate | **SYMBOLIC_READY** | Threshold + component |
| HS switching loss | E_sw model; f_PWM; V_IN; I_LOAD | Method | ED-IN-010; E_sw class data | Symbolic / candidate | **SYMBOLIC_READY** | ED-IN-010 |
| Sense burden | Sense class; R_shunt or equiv | Method; class comparison | ED-IN-011/032 | Symbolic | **SYMBOLIC_READY** | OI-SENSE-001 |
| Domain conversion | η_x; P_DOM_LOAD | Method | η_x; rail loads | Symbolic | **PROVISIONAL_INPUT_REQUIRED** | Component / ED-IN |
| Entry reconciliation | Signed I_DOM/I_CH; I_STORAGE_NET policy | WP-012 Accepted equations | Numerics | Symbolic identity | **SYMBOLIC_READY** | Thresholds Open |
| Fault energy | V(t), I(t) or peak×time; clearing | Method; P0–P5 | ED-IN-009/021; TBD-DK-011 | Symbolic | **BLOCKED_BY_INPUT** (numeric) | ED-IN-009 |
| Thermal T_ELEMENT | P_LOSS; R_TH; T_AMB | Method | ADR-DK-011; ED-IN-016/017; PCB | Symbolic | **BLOCKED_BY_ARCHITECTURE** (limits) | ADR-DK-011 |
| PCB derating candidate | T_ref; T_max; I_ref | Candidate form only | PCB design | Candidate only | **NOT_READY** (normative) | OI-PCB-001 |
| BI stall / regen | Stall fixture; bridge model; absorption | Method; BI class comparison | ED-IN-020; OI-FIX-002; dead-time | Symbolic | **PROVISIONAL_INPUT_REQUIRED** | Fixture + OI-BI-001 |
| E_TOTAL sense error | Error contributors §4 sense doc | Symbolic f(...) | Accuracy target | Symbolic | **SYMBOLIC_READY** | ED-IN-011 Open |

## 12. Traceability

WP-012 CPBM / Thermal / Protection · ADR-019…023 · ED-IN-* · TBD-DK-* · PWR-A-001/002 · R1–R5.

## 13. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial symbolic preliminary calculations — Proposed |
