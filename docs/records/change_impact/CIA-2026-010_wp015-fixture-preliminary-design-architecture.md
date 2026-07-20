# Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-2026-010 |
| **Impact Level** | 2 — Full CIA |
| **Title** | WP-015 Gen1 DevKit Fixture Preliminary Design Architecture |
| **Author** | Implementation Engineer (cloud agent) |
| **Author role** | Implementation Engineer |
| **Date** | 2026-07-20 |
| **Status** | Draft — Under Architecture Review |
| **Related WP / CR** | WP-015; baseline WP-014 Accepted (`bc7c6b6`); ADR-016…023 Accepted |

### Reason for Change

Accepted WP-014 fixture requirements (`REQ-DCC-V-FX-*`) lack a coherent preliminary design architecture. WP-015 proposes functional modules, block design, energy/control paths, interlock/state model, load-bank preliminary design, measurement/DAQ architecture, interface/wiring architecture, a preliminary design decision register (`FX-PD-*`), and an implementation readiness matrix — without freezing physical implementation.

### Impact Level Rationale (Level 2)

The preliminary architecture will later constrain fixture detailed design, protection design, operator controls, energy-control implementation, E-stop implementation, load-bank implementation, measurement/DAQ implementation, fault-injection implementation, harness/interface design, fixture BOM, procurement, construction, commissioning, and DevKit verification.

### Current Behaviour

* WP-014 requirements Accepted; no preliminary design architecture.
* Fixture NOT IMPLEMENTED; OI-GND-001/PROT/FIX/SC/BI Open.
* No `FX-*` module / `FX-PD-*` decision elements existed.

### Proposed Behaviour

* Proposed functional module decomposition, block design, energy/control architecture with OI-GND-001 option comparison, authorization-vs-physical-state model, fixture state and interlock model, E-stop integrity options, load-bank classes and failure behavior, measurement boundaries and DAQ responsibility split, symbolic interfaces and wiring classes, operator control/indication, `FX-PD-*` decision register, and implementation readiness matrix.
* All new WP-015 elements are `PROPOSED_DESIGN` / `PROPOSED_CONSTRAINT` / `ALTERNATIVE_UNDER_EVALUATION` / `BLOCKED_BY_*`; none self-approved.

### Scope exclusions (mandatory)

```text
No detailed electrical design.
No schematic / PCB / harness / mechanical / manufacturing files.
No MPN or manufacturer selected. No BOM.
No numeric threshold approved.
No ground/reference or isolation topology selected.
No E-stop circuit topology selected.
No procurement / construction / energization / physical fault injection.
No physical verification. No VE created.
```

### Affected Requirements

| ID | Impact |
|----|--------|
| REQ-DCC-V-FX-* (Accepted) | Preliminary design trace consumers — status unchanged (ACCEPTED / NOT VERIFIED) |
| PWR-A-017/018/021…024 | Referenced — ACCEPTED_CONSTRAINT unchanged |
| TBD-DK-001…022 | Remain Open |
| TBD-DK-007 | BLOCKED_BY_EDL_CLARIFICATION retained |

### Affected architectural documents

WP-015 adds nine DevKit preliminary-design documents and updates navigation/status/traceability. WP-014 Accepted content is unchanged.

### Affected safety boundaries

Distinct authorities preserved (E-stop / KILL / nENABLE / AUTH_*); back-feed prevention topology-neutral; EXTERNAL_ENERGY_ARMED authorization-only; simultaneous BASE+EXT blocked while OI-GND-001 Open; authorization ≠ physical energy removal; command OFF ≠ observed safe state; E-stop path integrity deferred (BLOCKED_BY_ARCHITECTURE); load-bank fail-to-remove removes upstream energy.

### Open-issue impact

OI-GND-001, OI-PROT-001/002, OI-FIX-001/002, OI-SC-001, OI-BI-001, OI-SENSE-001, OI-CONFIG-001, ADR-DK-011/012 remain **Open**; WP-015 compares options (e.g. GND-OPTION-A…D, E-STOP-OPT-1…4) but selects none.

### Traceability impact

`TRACEABILITY_MATRIX.md` gains WP-015 architecture references; requirements remain NOT VERIFIED; cases NOT EXECUTED / BLOCKED; no VE; numeric Open.

### Downstream design impact

Constrains future fixture detailed design, component qualification, protection design, E-stop design, load-bank design, measurement/DAQ design. None authorized by this CIA.

### Verification impact

None. No case executed; no case PASS; no requirement Verified; no VE.

### Non-impact (explicit)

No EDL/ADR content change. No hardware/firmware/config implementation. No schematic/PCB/BOM. No numeric approval. **Procurement and construction remain unauthorized.** No hardware energized.

### Rollback

Revert WP-015 PR; WP-014 Accepted baseline (`bc7c6b6`) preserved.

### Validation performed (WP-015 — reproducible)

#### V1 — Baseline ancestry

```bash
git merge-base --is-ancestor bc7c6b6f302aa8a2e6eccc54284dad6628d7101b HEAD
```

| Field | Value |
|-------|-------|
| stdout | *(empty)* |
| exit status | `0` |
| result | **PASS** — WP-014 acceptance baseline is ancestor |

#### V2 — Forbidden paths

```bash
git diff --name-only main...HEAD -- docs/EDL docs/ADR hardware firmware config
```

| Field | Value |
|-------|-------|
| stdout | *(empty)* |
| exit status | `0` |
| result | **PASS** |

#### V3 — MPN / ratings / numeric approval patterns

```bash
rg -i 'MPN:|preferred manufacturer|BOM entry|approved (current|voltage|timing|temperature)|fuse rating [0-9]|breaker [0-9]' \
  docs/DevKit/DevKit_Fixture_Preliminary_Design_Architecture.md \
  docs/DevKit/DevKit_Fixture_Preliminary_Block_Design.md \
  docs/DevKit/DevKit_Fixture_Energy_Control_Preliminary_Design.md \
  docs/DevKit/DevKit_Fixture_Interlock_and_State_Model.md \
  docs/DevKit/DevKit_Load_Bank_Preliminary_Design.md \
  docs/DevKit/DevKit_Fixture_Measurement_and_DAQ_Architecture.md \
  docs/DevKit/DevKit_Fixture_Interface_and_Wiring_Architecture.md \
  docs/DevKit/DevKit_Fixture_Preliminary_Design_Decision_Register.md \
  docs/DevKit/DevKit_Fixture_Implementation_Readiness_Matrix.md
```

| Field | Value |
|-------|-------|
| stdout | *(empty — rg no-match)* |
| exit status | `1` |
| result | **PASS** |

#### V3b — No active nominal-bound fault-energy approximation

```bash
rg -n 'E_FAULT ≈|≈ V_nom|Conservative approximation permitted|Conservative approximation when justified' \
  docs/DevKit/DevKit_Fixture_*.md docs/DevKit/DevKit_Load_Bank_Preliminary_Design.md
```

| Field | Value |
|-------|-------|
| stdout | *(empty — rg no-match)* |
| exit status | `1` |
| result | **PASS** — integral form + proof-bounded candidate only |

#### V4 — Open decisions retained

```bash
rg 'BLOCKED_BY_EDL_CLARIFICATION' docs/DevKit/DevKit_Sizing_Dependency_and_Closure_Matrix.md docs/DevKit/DevKit_Electrical_Design_Input_Register.md
rg -c 'OI-GND-001' docs/DevKit/DevKit_Fixture_Energy_Control_Preliminary_Design.md
```

| Field | Value |
|-------|-------|
| exit status | `0` / `0` |
| result | **PASS** — TBD-DK-007 BLOCKED and OI-GND-001 Open retained |

#### V5 — Deliverables present

```bash
python3 - <<'PY'
import os, sys
files = [
 "docs/DevKit/DevKit_Fixture_Preliminary_Design_Architecture.md",
 "docs/DevKit/DevKit_Fixture_Preliminary_Block_Design.md",
 "docs/DevKit/DevKit_Fixture_Energy_Control_Preliminary_Design.md",
 "docs/DevKit/DevKit_Fixture_Interlock_and_State_Model.md",
 "docs/DevKit/DevKit_Load_Bank_Preliminary_Design.md",
 "docs/DevKit/DevKit_Fixture_Measurement_and_DAQ_Architecture.md",
 "docs/DevKit/DevKit_Fixture_Interface_and_Wiring_Architecture.md",
 "docs/DevKit/DevKit_Fixture_Preliminary_Design_Decision_Register.md",
 "docs/DevKit/DevKit_Fixture_Implementation_Readiness_Matrix.md",
 "docs/records/change_impact/CIA-2026-010_wp015-fixture-preliminary-design-architecture.md",
 "docs/records/review_handoffs/RHP-2026-009_wp015-fixture-preliminary-design-architecture.md",
]
missing=[f for f in files if not os.path.isfile(f)]
for f in files: print(("PRESENT" if os.path.isfile(f) else "MISSING"), f)
sys.exit(1 if missing else 0)
PY
```

| Field | Value |
|-------|-------|
| stdout | `PRESENT` for all 9 DevKit docs + CIA + RHP (11 paths) |
| exit status | `0` |
| result | **PASS** |

#### V6 — Markdown relative links (WP-015 DevKit set)

```bash
python3 - <<'PY'
import re, os, sys
root="docs/DevKit"
files=[
 "DevKit_Fixture_Preliminary_Design_Architecture.md","DevKit_Fixture_Preliminary_Block_Design.md",
 "DevKit_Fixture_Energy_Control_Preliminary_Design.md","DevKit_Fixture_Interlock_and_State_Model.md",
 "DevKit_Load_Bank_Preliminary_Design.md","DevKit_Fixture_Measurement_and_DAQ_Architecture.md",
 "DevKit_Fixture_Interface_and_Wiring_Architecture.md","DevKit_Fixture_Preliminary_Design_Decision_Register.md",
 "DevKit_Fixture_Implementation_Readiness_Matrix.md"]
errors=[];checked=0
for f in files:
    text=open(os.path.join(root,f),encoding="utf-8").read()
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',text):
        t=m.group(1).split('#')[0]
        if not t or t.startswith('http'): continue
        checked+=1
        if not os.path.exists(os.path.normpath(os.path.join(root,t))): errors.append((f,t))
if errors:
    [print("MISSING",f,"->",t) for f,t in errors]; sys.exit(1)
print(f"OK: {len(files)} files, {checked} relative links verified")
PY
```

| Field | Value |
|-------|-------|
| stdout | `OK: 9 files, 9 relative links verified` |
| exit status | `0` |
| result | **PASS** |

#### V7 — No VE / Verified / case PASS

```bash
git diff --name-only main...HEAD -- docs/records/verification
rg -n '\| PASS \|' docs/DevKit/DevKit_Fixture_*.md docs/DevKit/DevKit_Load_Bank_Preliminary_Design.md
```

| Field | Value |
|-------|-------|
| VE diff | empty; exit `0` |
| PASS cells | none; exit `1` |
| result | **PASS** — no VE, no case PASS; no requirement marked Verified |

### Approvals

| Field | Value |
|-------|-------|
| **ADR Required** | NO (may drive future ADR-DK / decision packages) |
| **Architect Approval Required** | YES |
| **Architect approver** | TBD |
| **Architect approval date** | TBD |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial CIA — Draft; reproducible V1–V7 against the nine required deliverables |
