# DevKit Current and Power Budget Model — WP-012

**Document ID:** DOC-DK-CPBM-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-012  
**Date:** 2026-07-20

```text
Symbolic budget model only — no numeric current, voltage or power values Approved.
```

## 1. Purpose

Define current and power quantity vocabulary, measurement boundaries, domain budget relationships, and operating-profile integration for DevKit sizing. Extends Accepted WP-009 envelope analysis without approving numerics.

## 2. Defined quantities

| Symbol | Definition | Time basis | Domain |
|--------|------------|------------|--------|
| `V_IN(t)` | Input voltage at DevKit entry measurement boundary | Instantaneous | Input |
| `I_INPUT_INST(t)` | Instantaneous input current at entry MP | Instantaneous | Input |
| `I_INPUT_AVG` | Time-averaged input over profile window `T` | `(1/T)∫I dt` | Input |
| `I_INPUT_RMS` | RMS input over profile window | `sqrt((1/T)∫I² dt)` | Input / thermal |
| `I_INPUT_PEAK` | Peak input over profile window | `max I_INPUT_INST(t)` | Input |
| `I_LOGIC(t)` | Logic-board domain input current contribution | Instantaneous | Logic |
| `I_RADIO(t)` | Radio-board domain input current contribution | Instantaneous | Radio |
| `I_POWER_CTRL(t)` | Power-controller auxiliary load | Instantaneous | Power-control |
| `I_CHANNEL_n(t)` | nth representative channel current | Instantaneous | Channel |
| `I_BASE_INST(t)` | Sum of domain and channel contributions | See §4 | Base envelope |
| `I_PROFILE_PEAK` | Peak of `I_BASE_INST` over approved profile | Profile max | Base |
| `I_PROFILE_AVG` | Average of `I_BASE_INST` over profile | Profile avg | Base |
| `I_PROFILE_RMS` | RMS of `I_BASE_INST` over profile | Profile RMS | Base / thermal |
| `I_certified_cont` | Certified base continuous envelope (TBD-DK-002) | Steady / bounded | Base — **Open** |
| `I_simultaneous` | Concurrent channel sum under certified profile (TBD-DK-003) | Profile-defined | Base — **Open** |
| `P_INPUT(t)` | `V_IN(t) × I_INPUT_INST(t)` | Instantaneous | Input |
| `P_DOMAIN` | Useful + loss power in a domain | Steady or averaged | Per domain |
| `P_CHANNEL` | Channel dissipation sum | See §7 | Channel |
| `P_LOSS` | Aggregate loss term | Symbolic sum | Thermal input |
| `E_TRANSIENT` | `∫ P dt` over bounded transient | Energy | Protection |
| `E_FAULT` | `∫ V(t)×I(t) dt` over fault interval | Energy | Protection |

**Prohibited:** unqualified "maximum current" — every use shall specify peak / transient / continuous / average / RMS / fault class.

## 3. Current quantity definitions

For each quantity class:

| Class | Measurement point | Time window | Operating profile | Load state | Environmental | Averaging | Peak capture | Uncertainty | Margin | Protection link | Thermal link |
|-------|-------------------|-------------|-------------------|------------|---------------|-----------|--------------|-------------|--------|-----------------|--------------|
| **Instantaneous peak** | Entry MP; channel MP | Short capture (instrument-defined) | Active profile | As commanded | Nominal unless stated | None | Max hold | Instrument + load | Load uncertainty | OCP trip timing | Not thermal equivalent alone |
| **Time-bounded transient** | Entry or channel | Declared `t_transient` | P2/P5 | Inrush / fault | As test plan | Bounded integral | Peak within window | Source + DUT | Transient conservatism | Clearing coordination | `E_TRANSIENT` |
| **Steady continuous** | Entry MP | ≥ thermal soak minimum (Open) | P3 | Steady ON | T_amb declared | Mean over soak | Not peak | Measurement | Temperature derating | `I_certified_cont` | `I_PCB_cont(T)` |
| **Profile average** | Entry MP | Profile duration `T` | P0–P6 | Per profile table | Per profile | `(1/T)∫I dt` | Separate peak term | Profile + instrument | Load uncertainty | Budget check | Average loss |
| **RMS / thermal equivalent** | Entry or channel | Profile `T` | P3/P4 PWM | PWM duty | T_amb | RMS formula | Peak separate | Duty + waveform | Temp derating | Heating estimate | Primary thermal input |
| **Fault current** | Channel / entry | Fault interval | P5 | Fault injection | Controlled | Not averaged as continuous | Peak fault | High uncertainty | Fault conservatism | Layer P4/P2 | `E_FAULT` |
| **Prospective SC** | DUT terminals | Fault inception | P5 | SC fixture | Controlled | N/A | First cycle peak | Source impedance | Fault conservatism | Interrupt rating | Energy limit |

## 4. Domain current budget

### 4.1 Instantaneous base current

```text
I_BASE_INST(t) =
  I_LOGIC(t)
+ I_RADIO(t)
+ I_POWER_CTRL(t)
+ Σ I_CHANNEL_n(t)
```

### 4.2 Profile peak

```text
I_BASE_PROFILE_PEAK =
  max over t in approved profile [ I_BASE_INST(t) ]
```

### 4.3 Profile average

```text
I_BASE_PROFILE_AVG =
  (1 / T) × ∫ I_BASE_INST(t) dt
```

### 4.4 Profile RMS (thermal-relevant)

```text
I_BASE_PROFILE_RMS =
  sqrt( (1 / T) × ∫ I_BASE_INST(t)^2 dt )
```

### 4.5 Duty factors (independent bounds)

```text
0 ≤ D_n(t) ≤ 1   for each channel n
```

**Invalid unless explicitly Accepted:** `Σ D_n ≤ 1`. Unknown overlap → analyze as **concurrent** (WP-009-R1).

Average approximation (average only — not peak):

```text
I_avg ≈ I_logic_radio_avg + Σ (I_channel_n_on × D_n)
```

## 5. Certified continuous coordination (symbolic)

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

## 6. Operating profiles P0–P6 (sizing integration)

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

## 7. Electrical power model

### 7.1 Input power

```text
P_INPUT(t) = V_IN(t) × I_INPUT_INST(t)
```

### 7.2 Domain power

```text
P_DOMAIN =
  P_USEFUL
+ P_CONVERSION_LOSS
+ P_CONTROL_LOSS
+ P_SWITCHING_LOSS
+ P_SENSE_LOSS
```

### 7.3 Switching channel power (symbolic)

```text
P_CHANNEL =
  P_CONDUCTION
+ P_SWITCHING
+ P_GATE_OR_CONTROL
+ P_SENSE
+ P_TRANSIENT_AVERAGED
```

Device-specific loss equations may appear in future qualification reports as **alternative evaluation methods** — not normative in WP-012.

## 8. Engineering margin categories

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

## 9. Unsupported assumptions (rejected)

| Assumption | Rejection rationale |
|------------|---------------------|
| `Σ D_n ≤ 1` without policy | WP-009-R1 — unknown overlap concurrent |
| External bank raises `I_certified_cont` | ADR-020/021; PWR-A-002 |
| Fuse nominal = continuous certification | ADR-021; protection framework |
| PSU limit = sole protection | Protection framework P0/P2 |
| docs/008 30 A / devkit.yaml limits normative | Historical/candidate only |
| Headline switch `I_D` = DevKit continuous | WP-011 forbidden assumption |
| Datasheet RθJA as board truth | Thermal framework |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-012 initial current and power budget model — Proposed |
