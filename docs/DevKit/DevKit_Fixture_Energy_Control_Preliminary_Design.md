# DevKit Fixture Energy-Control Preliminary Design — WP-015

**Document ID:** DOC-DK-FECPD-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Functional energy/control paths, OI-GND-001 option comparison, authorization-vs-physical-state,
and fault-injection boundaries. No ratings, isolation/grounding topology, devices, or numerics selected.
```

## 1. Functional energy/control paths

| Path | Role | Envelope | Authority | Status |
|------|------|----------|-----------|--------|
| `BASE-SOURCE` | Base energy origin control | Base | `AUTH_BASE_SOURCE` | PROPOSED_DESIGN |
| `BASE-ENERGY-CONTROL` | Enable/limit/interrupt base energy | Base | via source AUTH | PROPOSED_DESIGN |
| `BASE-DUT-ENERGY` | Deliver base energy to DUT | Base | gated | PROPOSED_DESIGN |
| `EXT-SOURCE` | External energy origin control | External | `AUTH_EXT_SOURCE` | BLOCKED_BY_ARCHITECTURE (OI-GND-001) |
| `EXT-ENERGY-CONTROL` | Enable/limit/interrupt external energy | External | via ext AUTH | BLOCKED_BY_ARCHITECTURE |
| `EXT-LOAD-BANK` | External/base sink | Load | `AUTH_LOAD_BANK` | PROPOSED_DESIGN |
| `EXT-POWER-MODULE` | Representative switching/protection | External | `AUTH_EXT_POWER_MODULE` | BLOCKED_BY_ARCHITECTURE |
| `ENERGY-REMOVAL` | Inhibit/remove hazardous energy | All | overrides AUTH | PROPOSED_DESIGN |
| `DISCHARGE` | Controlled stored-energy decay | All | under removal | PROPOSED_DESIGN |
| `BACK-FEED-PREVENTION` | Prevent external→base energization | Base boundary | function | BLOCKED_BY_ARCHITECTURE (OI-GND-001) |

## 2. Preserved energy invariants

```text
1. Base and external energy envelopes are distinct.
2. External ratings do not extend the base DevKit rating.
3. Back-feed into base distribution is prohibited.
4. EXTERNAL_ENERGY_ARMED is authorization only.
5. Authorization does not prove physical de-energization.
6. Removal of authorization alone is not an energy-removal mechanism.
7. Safe state requires actual inhibition or removal of hazardous energy.
8. Physical state is observed independently where required.
9. Recovery requires deliberate operator action.
10. Stale commands shall not restore energy.
```

## 3. OI-GND-001 boundary (Open)

While OI-GND-001 is Open: simultaneous BASE + externally energized operation is **PROHIBITED**; combined-energy profiles are **BLOCKED_BY_ARCHITECTURE**; `BASE_ENERGIZED → externally energized` is **PROHIBITED**; `EXTERNAL_ENERGY_ARMED while BASE_ENERGIZED` may represent an **inactive authorization request only**. Galvanic isolation, common reference, and single-point reference are **NOT SELECTED**.

### 3.1 Ground/reference options (compared, not selected)

| Option | Description | Functional | Safety | Measurement | Back-feed | Fault-injection | Complexity class (no price) | Required evidence | Blocked downstream |
|--------|-------------|------------|--------|-------------|-----------|-----------------|-----------------------------|-------------------|--------------------|
| `GND-OPTION-A` | Controlled common reference | Shared reference simplifies measurement | Common-mode fault risk if reference fails | Single reference frame | Requires active back-feed prevention | Return-path defined | Moderate | Common-mode fault analysis; back-feed proof | Ext detailed design |
| `GND-OPTION-B` | Single-point reference | One bonding point | Ground-loop control; single-point integrity critical | Reference at one node | Requires directional prevention | Defined return | Moderate | Single-point integrity analysis | Ext detailed design |
| `GND-OPTION-C` | Galvanically isolated measurement/control boundary | Decoupled domains | Highest separation; isolation integrity critical | Isolated sensing needed | Strong inherent barrier | Isolated injection | Higher | Isolation qualification | Ext + measurement design |
| `GND-OPTION-D` | Separate fixtures / mutually exclusive modes | No simultaneous combined operation | Avoids combined-energy hazard by exclusion | Per-mode reference | Exclusion prevents cross-feed | Per-mode injection | Lower–Moderate | Mode-exclusion interlock proof | Combined-mode tests only |

**WP-015 selects none.** Disposition is reserved to the Architect (dedicated OI-GND-001 decision package).

## 4. Authorization versus physical energy state (§15)

Distinct signals/states:

```text
AUTH_REQUESTED · AUTH_GRANTED · ENERGY_PATH_COMMANDED
ENERGY_PATH_OBSERVED_ACTIVE · ENERGY_PATH_OBSERVED_INACTIVE
ENERGY_REMOVAL_REQUESTED · ENERGY_REMOVAL_CONFIRMED
DISCHARGE_COMPLETE · LOCKOUT_ACTIVE · RECOVERY_PERMITTED
```

Prohibited equivalences:

```text
AUTH revoked            ≠  Energy physically removed
Control command OFF     ≠  Observed safe electrical state
```

**Required observations before safe recovery:** `ENERGY_PATH_OBSERVED_INACTIVE` (applicable paths) + `ENERGY_REMOVAL_CONFIRMED` + `DISCHARGE_COMPLETE` (where stored energy applies) + valid identity/config. No numeric confirmation timing is approved (Open).

## 5. Fault-injection preliminary architecture (§23)

| Fault capability | Authorization owner | Permitted state | Required energy limits | Required protection | Observation | Abort path | Lockout | Reset | Blocker | Future detailed-design owner |
|------------------|--------------------|-----------------|------------------------|---------------------|-------------|-----------|---------|-------|---------|------------------------------|
| open load | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | bounded (Open) | P4/P2 | OL observe | E-stop/removal | yes | deliberate | PWR-A-010 | Fault WP |
| controlled overload | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | bounded (Open) | P4→P2 | I observe | E-stop/removal | yes | deliberate | bounds Open | Fault WP |
| short-to-return | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | BLOCKED | SC path | I_fault observe | E-stop/removal | yes | deliberate | OI-SC-001; ED-IN-021 | Fault WP |
| short-to-source | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | BLOCKED | SC path | I_fault observe | E-stop/removal | yes | deliberate | OI-SC-001 | Fault WP |
| input interruption | FX-AUTHORIZATION / source | FAULT_INJECTION_ARMED | n/a | P5 decay | supply observe | E-stop/removal | yes | deliberate | — | Fault WP |
| undervoltage profile | FX-AUTHORIZATION / source | FAULT_INJECTION_ARMED | source-limited | P3 UV | V observe | E-stop/removal | yes | deliberate | UV table Open | Fault WP |
| control loss | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | n/a | P5 | link observe | E-stop/removal | yes | deliberate | TBD-DK-007 | Fault WP |
| watchdog challenge | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | n/a | P5 | WD observe | E-stop/removal | yes | deliberate | TBD-DK-005 | Fault WP |
| KILL challenge | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | n/a | direct KILL | KILL observe | E-stop/removal | yes | deliberate | — | Fault WP |
| bidirectional stall | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | BLOCKED | P4/P5 | stall observe | E-stop/removal | yes | deliberate | OI-FIX-002; TBD-DK-022 | Fault WP |
| measurement-path fault | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | n/a | block dependent | plausibility | E-stop/removal | yes | deliberate | method Open | Fault WP |
| communication loss | FX-AUTHORIZATION | FAULT_INJECTION_ARMED | n/a | P5 | link observe | E-stop/removal | yes | deliberate | — | Fault WP |

No physical fault injection is authorized. Unknown fault energy remains **BLOCKED_BY_INPUT**.

## 6. Fault-energy governance (§24)

```text
E_FAULT = ∫ V(t) × I(t) dt
E_FAULT_BOUND = V_BOUND × I_BOUND × T_BOUND   # only if every term is a justified conservative bound
```

`V_nom`, `I_nom`, typical current, and expected clearing time are **not** conservative bounds without proof. Any simplified equation is a **candidate analytical form**, **non-normative**, and **not conservative unless every input is a proven bound**. Where bounds are unavailable: **BLOCKED_BY_INPUT**.

## 7. Traceability

REQ-DCC-V-FX-005/020…026/030…034/052…056 · PWR-A-001/002/003/017/018 · OI-GND-001 · OI-SC-001 · OI-PROT-001/002 · OI-FIX-002 · OI-BI-001 · TBD-DK-005/007/011/022 · ED-IN-021.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial energy-control preliminary design — Proposed |
