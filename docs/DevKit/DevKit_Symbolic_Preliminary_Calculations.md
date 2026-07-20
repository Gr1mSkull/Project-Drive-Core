# DevKit Symbolic Preliminary Calculations — WP-013

**Document ID:** DOC-DK-SPC-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
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

### 2.1 Current quantity distinctions (mandatory)

| Symbol | Meaning |
|--------|---------|
| `I_ON` | Current during the ON conduction interval (assumed constant in simplified forms) |
| `I_RMS_ON` | RMS over the ON interval only |
| `I_RMS_PROFILE` | RMS over the complete profile window `T_PROFILE` (includes OFF intervals) |
| `I_AVG_ON` | Average over the ON interval only |
| `I_AVG_PROFILE` | Average over the complete profile window |

**Prohibited ambiguous form:** `I_LOAD_RMS² × R × D` when `I_LOAD_RMS` is already `I_RMS_PROFILE` (double-counts duty).

### 2.2 General relationship

```text
P_COND =
(1 / T_PROFILE) ×
∫ i_path(t)^2 × R_path(i, T_j, state) dt
```

### 2.3 Constant ON-state current (resistive ON model)

```text
P_COND =
I_ON^2 × R_ON(T_j) × D
```

where `D` is the ON duty over `T_PROFILE`.

### 2.4 When RMS is already over the complete profile

```text
P_COND =
I_RMS_PROFILE^2 × R_EFFECTIVE
```

**Do not** multiply by duty again.

### 2.5 Voltage-drop model

General:

```text
P_COND =
(1 / T_PROFILE) ×
∫ |i_path(t)| × V_DROP(i, T_j, state) dt
```

Constant ON-state:

```text
P_COND =
I_ON × V_DROP × D
```

### 2.6 Class application notes

| Class | Notes |
|-------|-------|
| HS-INT-DIAG / BASIC | Apply §2.2–2.5 to the integrated path; declare which current symbol is used |
| HS-GATE-DISCRETE | Same FET term + `P_GATE_DRIVE` (separate) |
| HS-HYBRID | Integrated path + external element terms — allocate once |
| HS-ARRAY | Per-channel terms + coupling residual (not double-counted) |

Referral: convert to source-referred contribution inside `I_CH_IN_n` / `P_CH_IN_n` — do not add `I_LOAD` at entry.

## 3. Switching loss (event-based)

### 3.1 General form

```text
P_SWITCH =
(1 / T_PROFILE) ×
Σ_events E_transition(
  V_IN,
  I_LOAD,
  T_j,
  transition_direction,
  load_state
)
```

### 3.2 Periodic active PWM

When switching events actually occur:

```text
P_SWITCH ≈
f_EVENT ×
(E_ON + E_OFF + E_RECOVERY + E_CLAMP_SHARE)
```

where terms apply only if present for the class/topology.

### 3.3 Static duty — no assumed events

```text
f_EVENT = 0
```

when the output remains statically ON or OFF **without** switching events.

**Do not** assume configured `f_PWM` (ED-IN-010) means switching occurs at `D=0` or `D=1`.

`f_PWM` / event energies remain **Open** — no numeric Approved.

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
| SENSE-INTEGRATED | Device quiescent + sense-path loss (class data TBD) |
| SENSE-SHUNT-HS/LS | Use profile-consistent `I²R` form (§2 discipline) — if `I_RMS_PROFILE` used, do not also ×D |
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

### 7.1 Exact integral

```text
E_FAULT =
∫ V(t) × I(t) dt
```

### 7.2 Conservative bound (conditional)

```text
E_FAULT_BOUND =
V_BOUND × I_BOUND × T_BOUND
```

May be described as **conservative only when** all of the following hold over the declared boundary and interval:

```text
|V(t)| ≤ V_BOUND
|I(t)| ≤ I_BOUND
fault duration ≤ T_BOUND
```

If those conditions are **not** established, status is **BLOCKED_BY_INPUT**.

**Prohibited:** calling `V_nom × I_FAULT_PEAK × T_FAULT_CLEAR` a conservative bound without proven upper-bound justification.

### 7.3 Class-specific required inputs (Open)

| Protection class family | Required symbolic inputs |
|-------------------------|--------------------------|
| RP-* | Reverse V profile; conduction path; clearing/block behaviour |
| TRANSIENT-* | Surge waveform class; clamp/disconnect timing; energy share vs P0/P1 |
| INPUT-* | Replaceable clearing integral; electronic limit trajectory; coordination with continuous envelope |
| CH-* | Bound quantities or measured V(t), I(t); channel clamp path; P5 interaction |

## 8. Thermal relationship

Steady-state candidate (not sole model for short pulses/retry):

```text
T_ELEMENT = T_AMBIENT + P_LOSS × R_TH_EFFECTIVE
R_TH_EFFECTIVE = f(R_th_junction, R_th_board, R_th_enclosure, airflow, coupling)
```

**Steady-state `P × R_TH` shall not be used as the only model for short fault pulses or retry accumulation.**

PCB derating candidate (non-normative):

```text
I_PCB_cont(T) = I_PCB_cont(T_ref) × sqrt((T_max - T)/(T_max - T_ref))
```

**Candidate analytical form only** — not normative (WP-012-R1). ADR-DK-011 Open. Exact thermal impedance `Z_TH(t)` remains Open.

## 9. Bidirectional stall, regeneration, and retry thermal state

### 9.1 Separated energy quantities

| Symbol | Meaning |
|--------|---------|
| `E_SOURCE_STALL` | Source-referred electrical energy during stall interval |
| `E_BRIDGE_LOSS` | Energy dissipated in bridge loss mechanisms |
| `E_LOAD_ABSORBED` | Energy absorbed in the load |
| `E_RETURNED` | Energy returned toward the source (signed `I_CH_IN_BI < 0` when net return) |
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

Returned energy uses signed `I_CH_IN_BI`; do **not** double-count in `I_STORAGE_NET` (R3–R5).

### 9.2 Retry thermal-state evolution

Replace energy-sum-only retry models with thermal-state evolution:

```text
T_END_k =
thermal_response(
  T_START_k,
  P_BRIDGE_LOSS_k(t),
  Z_TH(t)
)

T_START_(k+1) =
T_AMBIENT
+ cooling_model(
    T_END_k,
    T_AMBIENT,
    Δt_k,
    thermal_state
  )
```

Exact `Z_TH(t)` and cooling model remain **Open**.

## 10. Uncertainty register (per calculation family)

| Uncertainty type | Owner | Notes |
|------------------|-------|-------|
| Input uncertainty | Architect / ED-IN owners | Thresholds Open |
| Model uncertainty | Implementation Engineer | Candidate forms labelled |
| Component-class uncertainty | Component Engineer | Until class Accepted |
| Temperature uncertainty | Thermal (ADR-DK-011) | R_TH / Z_TH Open |
| Measurement uncertainty | Test / fixture WP | E_TOTAL model § sense doc |
| Margin owner | System Architect | Categories only — no % Approved |
| Double-count risk | IE — WP-012 R3–R5; duty×RMS discipline | Audit entry reconciliation |

## 11. Calculation readiness table

| Calculation | Required inputs | Available inputs | Missing inputs | Permitted output | Readiness | Blocking artifact |
|-------------|-----------------|------------------|----------------|------------------|-----------|-------------------|
| HS conduction loss | Declared I symbol; R_ON/V_DROP; T; D or profile | Symbolic method §2 | ED-IN-002/026; T; R_TH; MPN data | Symbolic / candidate | **SYMBOLIC_READY** | Threshold + component |
| HS switching loss | Event list or f_EVENT; E_ON/OFF/… | Event-based method §3 | ED-IN-010; transition energies | Symbolic / candidate | **SYMBOLIC_READY** | ED-IN-010 |
| Sense burden | Sense class; consistent I²R form | Method; class comparison | ED-IN-011/032 | Symbolic | **SYMBOLIC_READY** | OI-SENSE-001 |
| Domain conversion | η_x; P_DOM_LOAD | Method | η_x; rail loads | Symbolic | **PROVISIONAL_INPUT_REQUIRED** | Component / ED-IN |
| Entry reconciliation | Signed I_DOM/I_CH; I_STORAGE_NET policy | WP-012 Accepted equations | Numerics | Symbolic identity | **SYMBOLIC_READY** | Thresholds Open |
| Fault energy integral | V(t), I(t) | Method; P0–P5 | Waveforms | Symbolic | **SYMBOLIC_READY** (method) | — |
| Fault energy bound | Proven V_BOUND, I_BOUND, T_BOUND | Bound form §7.2 | Bounds not established | Bound only if proven | **BLOCKED_BY_INPUT** until bounds proven | ED-IN-009/021 |
| Thermal steady-state | P_LOSS; R_TH; T_AMB | Method | ADR-DK-011; ED-IN-016/017 | Symbolic candidate | **BLOCKED_BY_ARCHITECTURE** (limits) | ADR-DK-011 |
| Thermal retry pulse | Z_TH(t); cooling_model; P_BRIDGE_LOSS(t) | State model §9.2 | Z_TH Open | Symbolic state evolution | **PROVISIONAL_INPUT_REQUIRED** | ADR-DK-011 |
| PCB derating candidate | T_ref; T_max; I_ref | Candidate form only | PCB design | Candidate only | **NOT_READY** (normative) | OI-PCB-001 |
| BI stall / regen | Separated E_* quantities; fixture | Method §9 | ED-IN-020; OI-FIX-002 | Symbolic | **PROVISIONAL_INPUT_REQUIRED** | Fixture + OI-BI-001 |
| E_TOTAL sense error | Error contributors § sense doc | Symbolic f(...) | Accuracy target | Symbolic | **SYMBOLIC_READY** | ED-IN-011 Open |

## 12. Traceability

WP-012 CPBM / Thermal / Protection · ADR-019…023 · ED-IN-* · TBD-DK-* · PWR-A-001/002 · R1–R5 · WP-013-R1 equation corrections.

## 13. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial symbolic preliminary calculations — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — conduction duty discipline; event-based switching; separated stall/bridge energies; thermal-state retry; fault-energy bound |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #17 merged (`d1698a0` / `23bdb07`); methodology Accepted; final classes/topology Open; TBD-DK-007 BLOCKED unchanged |
