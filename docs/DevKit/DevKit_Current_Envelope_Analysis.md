# DevKit Current Envelope Analysis — WP-009

**Document ID:** DOC-DK-ENV-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-009 / WP-009-R1 (Accepted)  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer (threshold analysis)

> Converts Accepted ADR-021 architecture into explicit current-envelope definitions, calculation models, operating profiles, and symbolic scenarios.  
> **Architecture Review Accepted (2026-07-20).** Analytical structure and closure methods Accepted. **No numeric limit is Approved.** All `TBD-DK-*` numeric values remain **Open**.

## 1. Scope and authority

| Field | Value |
|-------|-------|
| Primary TBDs | `TBD-DK-002`, `TBD-DK-003` |
| Related TBDs | `TBD-DK-001`, `012`, `017`, `018`, `019`, `022` |
| Authoritative ADRs | ADR-019, ADR-020, ADR-021, ADR-023 (Accepted) |
| Candidate sources treated as non-normative | docs/008 §2.3/§3.3 (30 A); devkit.yaml `current_limit_a` fields |

Historical **30 A**, **13.8 V**, fuse ratings, and config `current_limit_a` values are **CANDIDATE** only.

## 2. Current limit stack (distinct layers)

The following quantities **shall not be collapsed** into one “maximum current” (ADR-021):

| Layer ID | Symbol | Definition | Typical owner of numeric freeze |
|----------|--------|------------|--------------------------------|
| L1 | `I_PSU_limit` | Bench PSU programmable current limit | Test procedure / fixture WP |
| L2 | `I_conductor_cont` | Input harness / busbar continuous capability | Electrical architecture WP |
| L3 | `I_connector_cont` | Input connector continuous rating | Component qualification |
| L4 | `I_protection_rating` | Replaceable fuse/breaker **nominal interrupt rating** | Electrical architecture + protection study |
| L5 | `I_PCB_cont` | Power-entry / distribution copper continuous limit | PCB thermal/electrical design |
| L6 | `I_PCB_transient` | Allowed PCB surge before protection clears | Protection coordination |
| L7 | `I_channel_n_cont` | Per-channel continuous limit (switch + copper + thermal) | Component qualification |
| L8 | `I_channel_n_peak` | Per-channel permitted peak / inrush (time-bounded) | Component qualification |
| L9 | `I_simultaneous` | Sum of concurrent channel currents under certified profile | Threshold acceptance (TBD-DK-003) |
| L10 | `I_fixture_cont` | Fixture wiring / terminals continuous limit | Fixture WP |
| L11 | `I_fixture_pulse` | Fixture permitted pulse / fault-test envelope | Fixture WP + ADR-023 |
| L12 | `I_loadbank_limit` | External load-bank certified envelope (P6) | Fixture WP |
| L13 | `I_certified_cont` | **Certified DevKit base continuous envelope** (TBD-DK-002 intent) | Architect threshold acceptance |
| L14 | `I_fault_peak` | Prospective peak during controlled fault injection (P5) | Fixture + protection study |
| L15 | `I_psc` | Prospective short-circuit current at DUT terminals | Electrical design + PSU class |

### 2.1 Coordination rule (certified continuous)

```text
I_certified_cont ≤ minimum(
    I_PCB_cont,
    I_connector_cont,
    I_conductor_cont,
    I_fixture_cont,
    I_PSU_limit (when PSU is part of certified path),
    applicable thermal limit converted to current
)
```

### 2.2 Simultaneous-load rule

```text
I_simultaneous = Σ (I_channel_n × duty_factor_n)
```

**Duty / diversity factors are prohibited** unless the operating pattern is controlled, documented in a certified profile, and verifiable (DK-GOV-025).

### 2.3 Fault energy

```text
E_fault = ∫ V(t) × I(t) dt
```

Conservative approximation permitted when justified:

```text
E_fault ≈ V_nom × I_fault_peak × t_fault
```

### 2.4 Protection coordination (relationships)

| Relationship | Rule |
|--------------|------|
| PSU vs protection | PSU limit may be **lower** than fuse rating for bring-up; shall not be sole protection |
| Fuse vs continuous | `I_protection_rating` **≠** `I_certified_cont` (ADR-021 Option D) |
| DUT vs fixture | Fixture protection shall coordinate with DUT protection; fault energy bounded per ADR-023 |
| Software ceiling | Config/firmware `current_limit_a` shall not exceed certified envelope once frozen |
| External bank | `I_loadbank_limit` does **not** increase `I_certified_cont` by implication |

## 3. Operating profiles P0–P6

### Profile P0 — Unpowered inspection

| Field | Value |
|-------|-------|
| Purpose | Mechanical, continuity, identity, connector inspection without energization |
| Permitted channel count | 0 energized |
| Load type | None |
| Supervision | Visual / DMM passive checks only |
| Current class | 0 A |
| Duration | N/A |
| Duty cycle | N/A |
| Abort | N/A |
| Required evidence | Inspection record; BOARD_ID read if powered subsystems isolated |
| Gate relevance | DK-A prep |

### Profile P1 — Controlled first power

| Field | Value |
|-------|-------|
| Purpose | Logic/Radio rail bring-up; J_LP idle; outputs default OFF |
| Permitted channel count | 0 power loads |
| Load type | Logic + Radio + sense rails only |
| Supervision | Operator present; PSU current-limited to **I_P1_limit** (symbolic; << certified envelope) |
| Current class | `I_P1_limit` — **CANDIDATE** analysis band 0.5–2 A equivalent input (NOT APPROVED) |
| Duration | Minutes (bounded bring-up script) |
| Duty cycle | Continuous low input until rails stable |
| Abort | PSU trip; kill assert; mains disconnect |
| Required evidence | Rail tolerance check vs TBD-DK-017 (when closed); no output energization |
| Gate relevance | DK-A |

### Profile P2 — Low-energy functional bench

| Field | Value |
|-------|-------|
| Purpose | Single low/medium channel; ON/OFF, PWM, diagnostics development |
| Permitted channel count | 1 |
| Load type | Resistive or lamp-equivalent; no motor stall |
| Supervision | Operator; fixture overcurrent if used |
| Current class | ≤ one representative medium/low channel class (ADR-019); within `I_certified_cont` once approved |
| Duration | Continuous test sessions bounded by thermal policy |
| Duty cycle | 100 % DC or PWM per TBD-DK-008 when closed |
| Abort | Kill; PSU limit; channel protection trip |
| Required evidence | Channel behaviour logs; not gate exit alone |
| Gate relevance | DK-C development |

### Profile P3 — Base DevKit certified continuous envelope

| Field | Value |
|-------|-------|
| Purpose | Mandatory on-board capabilities (ADR-019) under certified continuous budget |
| Permitted channel count | ≥1 per capability map; typically **one active power channel** at a time unless P4 certified |
| Load type | Representative resistive/inductive per channel class |
| Supervision | Documented procedure; protection coordination verified |
| Current class | **`I_certified_cont`** — primary subject of TBD-DK-002 |
| Duration | As required by verification case; thermal limits apply (TBD-DK-018/019) |
| Duty cycle | Defined per case; no uncontrolled diversity |
| Abort | Kill; global disable; protection trip |
| Required evidence | Measurement per `DevKit_Threshold_Measurement_Plan.md` |
| Gate relevance | DK-A (input/protection); DK-C (capability) |

### Profile P4 — Simultaneous-load verification

| Field | Value |
|-------|-------|
| Purpose | Multi-channel concurrent operation within **`I_simultaneous`** (TBD-DK-003) |
| Permitted channel count | >1 only when simultaneous budget certified |
| Load type | Combinations declared in test plan; resistive preferred for first evidence |
| Supervision | Mandatory; thermal observation if TBD-DK-019 applicable |
| Current class | `I_simultaneous` ≤ `I_certified_cont` coordination (not independent of entry limit) |
| Duration | Case-defined |
| Duty cycle | **Explicit per-channel duty factors required** — no implicit diversity |
| Abort | Kill; per-channel and input protection |
| Required evidence | Simultaneous current trace; DK-GOV-025 freeze |
| Gate relevance | DK-C |

### Profile P5 — Controlled fault injection

| Field | Value |
|-------|-------|
| Purpose | OC, SC, stall (where applicable) per ADR-023 |
| Permitted channel count | 1 (typical) |
| Load type | Fixture-limited fault loads |
| Supervision | **Mandatory** operator + abort |
| Current class | **`I_fault_peak`** / **`E_fault`** — separate from `I_certified_cont` |
| Duration | Pulse / bounded (`t_fault`) |
| Duty cycle | Low duty; repetition limited |
| Abort | Fixture disconnect; kill; PSU foldback |
| Required evidence | Fault capture; protection operation; no sustained energy |
| Gate relevance | DK-C; DK-A (supply interruption cases) |

### Profile P6 — External load-bank / high-energy path

| Field | Value |
|-------|-------|
| Purpose | HC discovery / ADR-020 external path; not base DevKit certified envelope |
| Permitted channel count | As fixture defines |
| Load type | External bank loads |
| Supervision | Separate fixture safety interlocks |
| Current class | **`I_loadbank_limit`** — electrically distinct entry or branch |
| Duration | Case-defined |
| Duty cycle | Fixture-certified |
| Abort | Bank enable removal; kill; fixture E-stop |
| Required evidence | Fixture qualification; explicit scope separation from P3 |
| Gate relevance | DK-C (HC scope notes); Phase E planning |

## 4. Calculation framework (symbolic)

### 4.1 Input variables

| Variable | Description |
|----------|-------------|
| `I_input_cont` | Measured continuous input current at DevKit entry |
| `I_input_peak` | Peak input current during inrush or fault |
| `V_in` | Input voltage (pairs with TBD-DK-001) |
| `P_loss_entry` | Entry path dissipation |
| `R_th_entry` | Thermal resistance entry → ambient |
| `T_amb` | Ambient temperature |
| `T_max_safe` | Safe temperature limit (TBD-DK-019) |
| `η_simul` | **Not used** unless explicit profile defines verifiable duty factors |

### 4.2 Certified continuous bound (template)

```text
I_certified_cont = min(
    I_PCB_cont(T_amb, T_max_safe),
    I_connector_cont,
    I_conductor_cont,
    I_fixture_cont,
    I_PSU_limit_certified
)
```

Until hardware exists, each term is **UNKNOWN** or **BOUNDED BY ASSUMPTION** (documented in closure matrix).

### 4.3 Simultaneous and concurrent current model

Per-channel duty factor (independent bounds):

```text
0 ≤ D_n(t) ≤ 1
```

Instantaneous input current:

```text
I_inst(t) =
I_logic_radio(t)
+ Σ I_channel_n(t)
```

Profile peak (within window `T`):

```text
I_profile_peak =
max over t in [0, T] [ I_inst(t) ]
```

Profile average:

```text
I_profile_avg =
(1 / T) × ∫ I_inst(t) dt
```

Thermal / RMS quantity where applicable:

```text
I_profile_rms =
sqrt( (1 / T) × ∫ I_inst(t)^2 dt )
```

For controlled periodic channels, duty-factor approximation for **average** current only:

```text
I_avg ≈ I_logic_radio_avg + Σ (I_channel_n_on × D_n)
```

**Do not** use duty-factor sums for instantaneous peak unless switching overlap is explicitly controlled in the approved profile.

**Invalid constraint (removed in WP-009-R1):** `Σ D_n ≤ 1` — not valid unless a separate power-allocation policy explicitly enforces it.

Each `I_channel_n(t)` shall respect `I_channel_n_cont` when defined.

### 4.4 Channel overlap profile table (controlled)

| Profile ID | Channel | ON current | Duty `D_n` | Overlap class | May overlap with | Max overlap duration | Quantity affected |
|------------|---------|------------|------------|---------------|------------------|----------------------|-------------------|
| EXAMPLE-P4-A | CH-MED | TBD | TBD | concurrent by design | CH-LOW | TBD | instantaneous / average |
| EXAMPLE-P4-B | CH-LOW | TBD | TBD | never concurrent | — | 0 | average only |
| *TBD* | *TBD* | TBD | TBD | unknown | *TBD* | TBD | analyze as concurrent |

**Overlap class vocabulary:**

```text
never concurrent
concurrent by design
concurrent transiently
concurrency prohibited
unknown
```

**Unknown overlap shall be analyzed conservatively as concurrent** until an approved profile defines otherwise.

### 4.5 Thermal current derating (symbolic)

```text
I_PCB_cont(T) = I_PCB_cont(T_ref) × sqrt((T_max - T)/(T_max - T_ref))
```

Exact form requires copper geometry — **BLOCKED_BY_ELECTRICAL_ARCHITECTURE**.

## 5. Candidate scenarios C1–C3 (symbolic)

> **WP-009-R1:** Numeric ampere bands removed. Scenarios are **architecture patterns** only. **No provisional ampere ceiling is authorized by WP-009.**

### Scenario C1 — Bring-up envelope

```text
I_C1 =
I_logic
+ I_radio
+ I_sensing_rail_margin
+ (no energized power load)
```

One explicitly low-energy channel may be included only when the operating profile (P1/P2) permits it.

| Aspect | Assessment |
|--------|------------|
| Purpose | P1 controlled first power; Logic/Radio/sense rails |
| Coverage | DK-A bring-up |
| Electrical implications | Minimal entry energy |
| **Recommendation** | Use for **P1/P2** only — not P3 certified envelope |

### Scenario C2 — Functional single-channel envelope (RECOMMENDED architecture pattern)

```text
I_C2 =
I_logic_radio_max
+ max(I_representative_channel_cont)
+ I_auxiliary_margin
```

Limited concurrent low-power channels permitted **only** through an explicit overlap profile (§4.4).

| Aspect | Assessment |
|--------|------------|
| Purpose | ADR-019 mandatory capabilities with one active representative power channel |
| Coverage | DK-A input/protection; core DK-C single-channel |
| Electrical implications | Entry sized from calculated stack — not from WP-009 bands |
| **Recommendation** | **Select C2 architecture** for downstream electrical analysis |

**No provisional ampere ceiling is authorized by WP-009.** The electrical architecture WP shall calculate the first candidate current ceiling from:

- selected representative channel classes;
- actual load assumptions;
- connector and conductor candidates;
- PCB distribution concept;
- protection coordination;
- thermal assumptions;
- operating profiles.

### Scenario C3 — Multi-channel base envelope

```text
I_C3 =
I_logic_radio_max
+ max over approved concurrent profiles (
    Σ I_channel_n_profile
  )
```

| Aspect | Assessment |
|--------|------------|
| Purpose | Multi-channel concurrent operation within approved overlap profiles |
| Coverage | DK-C simultaneous-load verification (P4) |
| **Recommendation** | **Not automatically recommended** — requires explicit overlap profiles and thermal/protection study |

### Scenario comparison summary

| Criterion | C1 | C2 (recommended pattern) | C3 |
|-----------|----|--------------------------|-----|
| ADR-021 alignment | Strong | **Strongest** | Conditional |
| ADR-019 coverage | Partial | **Full staged** | Full (if profiles approved) |
| Operator safety | Strong | **Strong** | Requires overlap discipline |
| External bank reliance | High | **Moderate** | Lower |
| Numeric authorization | **None** | **None** | **None** |

## 6. TBD-DK-002 disposition

### 6.1 Semantic clarification

Historical register text conflates **protection rating** and **continuous input**. ADR-021 requires separation.

**Recommended controlled structure** (for future register decomposition — **do not create canonical IDs in WP-009**):

| Proposed sub-ID | Quantity | Notes |
|-----------------|----------|-------|
| TBD-DK-002A (future) | Certified continuous DevKit input current `I_certified_cont` | Primary P3 limit |
| TBD-DK-002B (future) | Replaceable protection nominal rating `I_protection_rating` | ≥ fault coordination; ≠ continuous |
| TBD-DK-002C (future) | Permitted transient/fault-test input envelope | P5 only; energy-limited |

### 6.2 WP-009 disposition

| Field | Value |
|-------|-------|
| Acceptance status | **BOUND_ESTABLISHED_VALUE_OPEN** |
| Architecture direction | Option B + D (ADR-021 Accepted) |
| Calculation model | Section 4 — **established** |
| Recommended scenario pattern | **C2** (not an ampere range) |
| Candidate numeric approval | **None** |
| Exact blockers | Electrical architecture (conductor/connector/PCB); component qualification; physical measurement |
| Closure artifact | Architect threshold decision on tuple; electrical architecture WP calculates first ceiling |

### 6.3 Proposed Threshold Decision Record — TBD-DK-002

```text
PROPOSED (not Approved):
- Accept closure method: limit stack + Scenario C2 calculation architecture
- Reject provisional ampere ceiling from WP-009 — electrical architecture WP derives first candidate
- Defer numeric fuse rating until protection coordination complete
- Recommend register decomposition CR for 002A/B/C
Status remains Open.
```

## 7. TBD-DK-003 disposition

| Field | Value |
|-------|-------|
| Acceptance status | **READY_FOR_ACCEPTANCE** (profile-based closure model only) |
| Controlled meaning | Profile-based simultaneous-current envelope — **not necessarily one universal scalar** |
| Minimum separable quantities | Maximum instantaneous concurrent input; maximum continuous concurrent input; approved channel-overlap profiles; maximum transient overlap duration |
| Register decomposition | Recommend future CR if needed — **do not create canonical IDs in WP-009-R1** |
| Numeric simultaneous current | **NOT READY** |
| Blockers | Overlap profile approval; P4 measurement; thermal simultaneous model |
| Closure artifact | Architect acceptance of profile/overlap model; numeric freeze after electrical design |

### Proposed Threshold Decision Record — TBD-DK-003

```text
PROPOSED (not Approved):
- Accept profile-based simultaneous model (P4) and overlap table (§4.4)
- Accept instantaneous / average / RMS distinction
- Reject implicit diversity factors and invalid ΣD_n ≤ 1 constraint
- Numeric amperes remain Open pending electrical design + P4 measurement
Status remains Open.
```

## 8. Related threshold interactions

| TBD | Interaction with current envelope |
|-----|-----------------------------------|
| TBD-DK-001 | `V_in` sets power at fixed `I`; UV may reduce available channel current — pairs with 012 |
| TBD-DK-012 | UV table may force output shutdown during P3/P4 — does not change ampere limits directly |
| TBD-DK-017 | Rail tolerance affects Logic/Power readiness before P3 |
| TBD-DK-018/019 | Thermal duration/max temp constrain **duration** at given current, not ampere value alone |
| TBD-DK-022 | Stall current is **P5** fault class; not part of `I_certified_cont` |

## 9. Parallel electrical-architecture boundary

### May proceed while TBD-DK-002/003 Open

- Interface decomposition (PSU → protection → entry → distribution)
- Base DevKit vs external bank separation (P3 vs P6)
- Measurement point requirements (input, channel, enable chain)
- Protection-layer responsibility matrix
- Identity / test-point requirements

### Must wait for Architect threshold acceptance or electrical-architecture-calculated ceiling

> WP-009 does **not** authorize a provisional ampere ceiling. First numeric candidate comes from electrical architecture WP inputs.

- Conductor sizing
- Connector sizing
- Fuse rating selection
- PCB copper sizing
- Thermal design sign-off
- Switch current rating
- Fault-energy design
- Software `current_limit_a` freeze in config

## 10. Requirement and verification trace

| TBD | Requirements | Verification cases |
|-----|--------------|-------------------|
| TBD-DK-002 | REQ-DCC-V-DK-020; DK-GOV-024/025 | VER-DCC-DK-A-002 |
| TBD-DK-003 | DK-GOV-025 | VER-DCC-DK-C-002, C-005, C-006 (multi-load notes) |

## 11. Architecture Review acceptance (2026-07-20)

| Field | Value |
|-------|-------|
| **Status** | Accepted — Architecture Review |
| **Review date** | 2026-07-20 |
| **Approver role** | System Architect |
| **PR** | #13 merged (`6f3845e`) |

Accepted: analytical structure, limit stack, profiles P0–P6, symbolic C1–C3, C2 calculation architecture, profile/overlap simultaneous model.  
Not Accepted: numeric current limits, physical measurements, ampere ceiling.

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial current envelope analysis |
| 1.1 | 2026-07-20 | WP-009-R1 — symbolic scenarios; corrected simultaneous model; no ampere bands |
| 1.2 | 2026-07-20 | Architecture Review — methods Accepted; numeric Open |
