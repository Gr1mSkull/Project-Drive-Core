# DevKit Current and Power Budget Model — WP-012

**Document ID:** DOC-DK-CPBM-001  
**Version:** 1.2  
**Status:** Ready for Final Architecture Acceptance  
**Work Package:** WP-012  
**Date:** 2026-07-20

```text
Symbolic budget model only — no numeric current, voltage or power values Approved.
```

## 1. Purpose

Define current and power quantity vocabulary, measurement boundaries, domain budget relationships, and operating-profile integration for DevKit sizing. Extends Accepted WP-009 envelope analysis without approving numerics.

## 2. Measurement boundaries and quantity taxonomy

Currents measured at **different electrical boundaries shall not be directly summed**. WP-012 defines four distinct quantity classes:

| Class | Symbol (template) | Boundary | Definition |
|-------|-------------------|----------|------------|
| **Channel load / output current** | `I_LOAD_n(t)` | Load / output terminal | Current delivered to or drawn by the attached load at channel *n* output |
| **Channel source-referred input contribution** | `I_CH_IN_n(t)` | Referred to DevKit input source | **Signed net** incremental input-side contribution attributable to channel *n* — see §2.2 |
| **Domain source-referred input contribution** | `I_DOM_IN_x(t)` | Referred to DevKit input source | **Signed net** incremental input-side contribution of domain *x* ∈ {LOGIC, RADIO, POWER_CTRL} |
| **Measured DevKit entry current** | `I_ENTRY_MEAS(t)` | Input entry MP (WP-010) | Current measured at the certified DevKit input measurement boundary |

**Legacy alias note:** `I_INPUT_INST(t)` in WP-009 maps to **`I_ENTRY_MEAS(t)`** when the measurement point is the DevKit entry MP.

### 2.1 Defined quantities (extended)

| Symbol | Definition | Boundary |
|--------|------------|----------|
| `V_IN(t)` | Input voltage at entry MP | Entry |
| `I_ENTRY_MEAS(t)` | Measured entry current | Entry |
| `I_ENTRY_AVG` / `I_ENTRY_RMS` / `I_ENTRY_PEAK` | Entry statistics over profile window | Entry |
| `I_LOAD_n(t)` | Channel *n* load/output current | Channel output |
| `I_CH_IN_n(t)` | Channel *n* source-referred input contribution | Referred to entry |
| `I_DOM_IN_LOGIC(t)` | Logic domain source-referred contribution | Referred to entry |
| `I_DOM_IN_RADIO(t)` | Radio domain source-referred contribution | Referred to entry |
| `I_DOM_IN_PWR(t)` | Power-control domain source-referred contribution | Referred to entry |
| `I_BASE_IN_INST(t)` | Sum of **source-referred** base-envelope contributions | Referred to entry — see §4 |
| `I_certified_cont` | Certified base continuous envelope (TBD-DK-002) | Entry — **Open** |
| `I_simultaneous` | Concurrent profile constraint (TBD-DK-003) | Entry-referred — **Open** |
| `P_ENTRY(t)` | `V_IN(t) × I_ENTRY_MEAS(t)` | Entry |
| `P_CH_IN_n` / `P_DOM_IN_x` | Power form of source-referred contributions | Entry-referred |
| `E_TRANSIENT` / `E_FAULT` | Bounded energy integrals | Declared fault/load window |

**Prohibited:** unqualified "maximum current"; direct summation of `I_LOAD_n` at output boundaries with domain rail currents; inclusion of P6 / external-envelope currents in base `I_BASE_IN_INST` (PWR-A-001/002); **double-counting** the same energy in `I_CH_IN_n` / `I_DOM_IN_x` and in unallocated storage terms (§2.2 R3).

### 2.2 Sign convention and double-counting rules (normative)

**Sign convention (entry reference):**

```text
I > 0  →  net draw FROM the source INTO the DevKit at the entry reference
I < 0  →  net return FROM the DevKit TOWARD the source at the entry reference
```

Applies to `I_ENTRY_MEAS`, `I_DOM_IN_x`, `I_CH_IN_n`, and `I_STORAGE_NET`.

**Allocation rules:**

| Rule | Statement |
|------|-----------|
| **R1** | `I_CH_IN_n(t)` is the **signed net** source-referred contribution of channel *n*. It shall include channel-attributable conduction, driver/sense burden, switching loss equivalent, conversion effects, and **net** bidirectional/regenerative exchange referred to the entry — not gross `I_LOAD_n` alone. |
| **R2** | `I_DOM_IN_x(t)` is the **signed net** source-referred contribution of domain *x*, including rail conversion losses. |
| **R3** | Reactive energy, returned energy, or storage exchange **already attributed** to a channel in `I_CH_IN_n` or to a domain in `I_DOM_IN_x` shall **not** be counted again in `I_STORAGE_NET`. |
| **R4** | `I_STORAGE_NET(t)` is used **only** for explicitly **unallocated shared storage paths** (e.g. bulk input capacitance, shared intermediate energy storage not owned by a declared channel/domain partition). If no such path is declared, `I_STORAGE_NET(t) = 0`. |
| **R5** | Do not use separate `I_REACTIVE_NET` / `I_RETURN_NET` alongside fully allocated `I_CH_IN_n` terms for the same physical exchange. Legacy separate terms are replaced by **`I_STORAGE_NET`** for unallocated paths only. |

**Bidirectional channels:** regen or reverse power flow appears as **negative** `I_CH_IN_n` when net energy returns toward the source; it is **not** duplicated in `I_STORAGE_NET` unless an unallocated shared element is explicitly modelled.

## 3. Source-referred aggregation rules (symbolic)

Entry measurement relates to source-referred contributions through **power balance** at a **single reference**, not naive current addition at unrelated nodes:

```text
P_ENTRY(t) = V_IN(t) × I_ENTRY_MEAS(t)
```

```text
P_ENTRY(t) ≈
  P_DOM_IN_LOGIC(t)
+ P_DOM_IN_RADIO(t)
+ P_DOM_IN_PWR(t)
+ Σ P_CH_IN_n(t)
+ P_STORAGE_UNALLOCATED(t)
```

Signed current form at entry reference:

```text
I_ENTRY_MEAS(t) ≈
  I_DOM_IN_LOGIC(t)
+ I_DOM_IN_RADIO(t)
+ I_DOM_IN_PWR(t)
+ Σ I_CH_IN_n(t)
+ I_STORAGE_NET(t)
```

Where:

| Term | Meaning |
|------|---------|
| `η_conv_x` | Domain rail conversion efficiency (Open — component-dependent) — used inside referral transform to derive signed `I_DOM_IN_x`, not as a post-sum factor |
| PWM / loss terms | Absorbed into signed net `I_CH_IN_n` or `I_DOM_IN_x` — peak ≠ average without declared duty |
| `I_STORAGE_NET(t)` | **Unallocated shared storage/reactive path only** (§2.2 R4) — zero unless explicitly declared |
| `P_STORAGE_UNALLOCATED(t)` | `V_IN(t) × I_STORAGE_NET(t)` when the storage path is referenced at entry |

**External-energy envelope (P6):** `I_EXT_*` quantities are **excluded** from `I_BASE_IN_INST`, `I_STORAGE_NET`, and `I_certified_cont` unless Architect explicitly scopes a separate external certification path (ADR-020).

### 3.1 Mapping from load current to source-referred contribution (template)

For each channel *n* — **candidate analytical forms** requiring declared assumptions; not normative until validated:

```text
I_CH_IN_n(t) = signed_net_source_referred(
  I_LOAD_n(t), V_LOAD_n(t), V_IN(t), η_n, D_n(t), f_PWM, topology_n, direction_n
)
```

Positive `I_CH_IN_n` = net draw from source; negative = net return toward source. Do not assume `I_CH_IN_n = I_LOAD_n` without efficiency, voltage conversion, PWM, and bidirectional netting proof.

## 4. Current quantity definitions (by class)

For each quantity class:

| Class | Measurement point | Time window | Operating profile | Load state | Environmental | Averaging | Peak capture | Uncertainty | Margin | Protection link | Thermal link |
|-------|-------------------|-------------|-------------------|------------|---------------|-----------|--------------|-------------|--------|-----------------|--------------|
| **Instantaneous peak** | Entry MP; channel MP | Short capture (instrument-defined) | Active profile | As commanded | Nominal unless stated | None | Max hold | Instrument + load | Load uncertainty | OCP trip timing | Not thermal equivalent alone |
| **Time-bounded transient** | Entry or channel | Declared `t_transient` | P2/P5 | Inrush / fault | As test plan | Bounded integral | Peak within window | Source + DUT | Transient conservatism | Clearing coordination | `E_TRANSIENT` |
| **Steady continuous** | Entry MP (`I_ENTRY_MEAS`) | ≥ thermal soak minimum (Open) | P3 | Steady ON | T_amb declared | Mean over soak | Not peak | Measurement | Temperature derating | `I_certified_cont` | Thermal derating — see thermal framework §6 |
| **Profile average** | Entry MP | Profile duration `T` | P0–P6 | Per profile table | Per profile | `(1/T)∫I dt` | Separate peak term | Profile + instrument | Load uncertainty | Budget check | Average loss |
| **RMS / thermal equivalent** | Entry or channel | Profile `T` | P3/P4 PWM | PWM duty | T_amb | RMS formula | Peak separate | Duty + waveform | Temp derating | Heating estimate | Primary thermal input |
| **Fault current** | Channel / entry | Fault interval | P5 | Fault injection | Controlled | Not averaged as continuous | Peak fault | High uncertainty | Fault conservatism | Layer P4/P2 | `E_FAULT` |
| **Prospective SC** | DUT terminals | Fault inception | P5 | SC fixture | Controlled | N/A | First cycle peak | Source impedance | Fault conservatism | Interrupt rating | Energy limit |

## 5. Source-referred base budget (symbolic)

### 5.1 Instantaneous base input-referred sum

```text
I_BASE_IN_INST(t) =
  I_DOM_IN_LOGIC(t)
+ I_DOM_IN_RADIO(t)
+ I_DOM_IN_PWR(t)
+ Σ I_CH_IN_n(t)
```

All terms are **signed net** contributions (§2.2). **Does not include:** `I_STORAGE_NET` (reconciled in §5.2); external-envelope (P6) contributions; quantities measured only at load terminals without referral transform.

### 5.2 Consistency check with measurement

```text
I_ENTRY_MEAS(t)  ≟  I_BASE_IN_INST(t) + I_STORAGE_NET(t)
```

Where `I_STORAGE_NET` is zero unless an unallocated shared storage path is explicitly declared (§2.2 R4). **Do not** add channel/domain return or reactive components to `I_STORAGE_NET` if they are already netted in `I_CH_IN_n` / `I_DOM_IN_x` (§2.2 R3).

### 5.3 Profile statistics (entry-referred)

```text
I_BASE_IN_PROFILE_PEAK = max over t in approved profile [ I_BASE_IN_INST(t) ]

I_BASE_IN_PROFILE_AVG  = (1 / T) × ∫ I_BASE_IN_INST(t) dt

I_BASE_IN_PROFILE_RMS  = sqrt( (1 / T) × ∫ I_BASE_IN_INST(t)^2 dt )
```

Profile peak/average/RMS for **`I_ENTRY_MEAS`** use the same window at the entry MP and shall reconcile with §5.2.

### 5.4 Duty factors (independent bounds)

```text
0 ≤ D_n(t) ≤ 1   for each channel n
```

**Invalid unless explicitly Accepted:** `Σ D_n ≤ 1`. Unknown overlap → analyze as **concurrent** (WP-009-R1).

Average approximation (average only — not peak):

```text
I_avg ≈ I_dom_avg + Σ (I_CH_IN_n_on × D_n)    (average only — not peak)
```

## 6. Certified continuous coordination (symbolic)

From WP-009 limit stack — numeric terms **Open**:

```text
I_certified_cont ≤ minimum(
  I_PCB_cont,
  I_connector_cont,
  I_conductor_cont,
  I_fixture_cont,
  I_PSU_limit (when in certified path),
  thermal limit converted to current
)
```

```text
I_simultaneous ≤ I_certified_cont   (coordination — not independent of entry limit)
```

## 7. Operating profiles P0–P6 (sizing integration)

| Profile | Purpose | Energized domains | Permitted capabilities | Concurrent channels | Load type | Duration | Duty | Thermal | Protection | Fault energy | Required ED-IN | Blockers | Future verification |
|---------|---------|-------------------|------------------------|---------------------|-----------|----------|------|---------|------------|--------------|----------------|----------|---------------------|
| **P0** | Unpowered inspection | None | None | 0 | None | N/A | N/A | No | No | No | ED-IN-018 | None | DK-A prep |
| **P1** | First power | Logic, Radio | No power loads | 0 power | Logic/Radio only | Minutes | Continuous low | No | PSU limit | No | ED-IN-015, 024, 025 | Rail tolerances Open | DK-A |
| **P2** | Low-energy bench | Logic, Radio, 1 channel | HS-BASE/PWM dev | 1 | Resistive/lamp | Session | DC/PWM Open | Partial | Channel + PSU | No | ED-IN-010, 026 | PWM freq Open | DK-C dev |
| **P3** | Certified continuous | Base envelope | ADR-019 mandatory set | ≥1; typically 1 unless P4 | Representative loads | Case-defined | Per case | Yes | Full stack | No | ED-IN-002, 017 | TBD-DK-002 Open | DK-A, DK-C |
| **P4** | Simultaneous load | Base envelope | Multi-channel | >1 controlled | Declared combo | Case-defined | Explicit D_n | Yes | Per-channel + input | No | ED-IN-003 | TBD-DK-003; overlap | DK-C |
| **P5** | Fault injection | Base + fixture | OC/SC/stall | 1 typical | Fixture-limited | Pulse | Low duty | Partial | P0–P5 stack | Yes | ED-IN-009, 021 | TBD-DK-011 | DK-C, DK-A |
| **P6** | External bank | External path | HC external | Fixture-defined | Bank loads | Case-defined | Fixture | Separate | Fixture + DUT | Separate | ED-IN-022, 023 | OI-GND-001 | Phase E / fixture |

Numeric currents: **not assigned** in any profile.

## 8. Electrical power model

### 8.1 Input power

```text
P_ENTRY(t) = V_IN(t) × I_ENTRY_MEAS(t)
```

### 8.2 Domain power (source-referred)

```text
P_DOMAIN =
  P_USEFUL
+ P_CONVERSION_LOSS
+ P_CONTROL_LOSS
+ P_SWITCHING_LOSS
+ P_SENSE_LOSS
```

### 8.3 Switching channel power (symbolic)

```text
P_CHANNEL =
  P_CONDUCTION
+ P_SWITCHING
+ P_GATE_OR_CONTROL
+ P_SENSE
+ P_TRANSIENT_AVERAGED
```

Device-specific loss equations may appear in future qualification reports as **alternative evaluation methods** — not normative in WP-012.

## 9. Engineering margin categories

See [`DevKit_Electrical_Sizing_Framework.md`](DevKit_Electrical_Sizing_Framework.md) — margin percentages **not assigned** in WP-012.

| Category | Applies when | Owner | Overlap rule |
|----------|--------------|-------|--------------|
| Input uncertainty margin | Source / PSU characterization | Test Engineer | Document if additive with measurement |
| Load uncertainty margin | Unknown load impedance | Test Engineer | Separate from component tolerance |
| Component-tolerance margin | Pre-qualification bounds | Component Engineer | Not double-counted with aging |
| Temperature derating margin | Thermal sizing | Implementation Engineer | Paired with T_amb assumption |
| Aging margin | Long-life certification | Component Engineer | Justified separately |
| Measurement uncertainty | All measured quantities | Test Engineer | Combined per measurement plan |
| Manufacturing variation | Production scatter | Implementation Engineer | PCB/schematic phase |
| Future-expansion margin | Reserved capability | System Architect | Explicit approval required |
| Fault-analysis conservatism | P5 energy studies | Implementation Engineer | Not substitute for protection layer |

**Prohibited:** hidden double-counting of margins (DK-GOV-025 alignment).

## 10. Unsupported assumptions (rejected)

| Assumption | Rejection rationale |
|------------|---------------------|
| `Σ D_n ≤ 1` without policy | WP-009-R1 — unknown overlap concurrent |
| External bank raises `I_certified_cont` | ADR-020/021; PWR-A-002 |
| Fuse nominal = continuous certification | ADR-021; protection framework |
| PSU limit = sole protection | Protection framework P0/P2 |
| docs/008 30 A / devkit.yaml limits normative | Historical/candidate only |
| Direct sum of `I_LOAD_n` as entry current | Boundary violation — use signed `I_CH_IN_n` referral |
| `I_CH_IN_n = I_LOAD_n` without η/PWM/BI proof | Ignores conversion and topology |
| Double-count in `I_CH_IN_n` and `I_STORAGE_NET` | Violates §2.2 R3 |
| Datasheet RθJA as board truth | Thermal framework |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial current and power budget model — Proposed |
| 1.1 | 2026-07-20 | WP-012-R1 — measurement boundaries; source-referred aggregation; external envelope exclusion |
| 1.2 | 2026-07-20 | WP-012-R2 — sign convention; signed `I_CH_IN_n`; `I_STORAGE_NET` unallocated-only; anti double-count |
