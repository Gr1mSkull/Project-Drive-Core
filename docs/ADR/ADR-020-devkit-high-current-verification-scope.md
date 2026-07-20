# ADR-020: DevKit Highest-Current Verification Scope

| Field | Value |
|-------|-------|
| **Canonical ADR ID** | `ADR-020` |
| **Originating decision request** | `ADR-DK-005` |
| **Title** | DevKit Highest-Current Verification Scope |
| **Status** | Proposed |
| **Date** | 2026-07-20 |
| **Decision owner** | System Architect |
| **Work Package** | WP-008 |
| **Deliverable status** | Proposed — requires Architecture Review |

> This ADR is **Proposed**. Recommendations are not Accepted. Implementation Engineer cannot approve.


### Context

E30-class loads (e.g. EHPS) may require highest-tier channel class (HC-A). DevKit candidate documents historically omit HS60-class on the DevKit Power PCB. Operator safety, bench input limits (ADR-021), and EDL-014 Phase E all affect where continuous high-current verification occurs.

### Problem statement

Where shall the highest-current channel class be verified, and which verification types remain DevKit versus Phase E only?

### Existing authoritative constraints

| Source | Constraint |
|--------|------------|
| EDL-014 | Phase E critical items on full DCC Gen1; DevKit does not replace Phase E |
| REQ-DCC-V-DK-005 | Not full production population by default |
| ADR-019 (Proposed) | High-current continuous classified EXTERNAL_FIXTURE / deferred |
| Constitution | High-current copper/thermal must be verified — not headline ratings |
| Candidate docs/008 | no-HS60 on DevKit — candidate only |

### Decision drivers

Operator safety; fire risk; PCB copper/thermal; connector burden; early fault discovery value; representativeness; repeatability; E30 relevance; distinguish control vs full-power evidence.

### Verification type separation

| Type | Meaning |
|------|---------|
| logic/control verification | Commands, interlocks, state machine without full HC continuous current |
| diagnostic verification | Sense/flags/paths at bounded current |
| protection verification | OC/SC reaction at controlled limited energy |
| continuous-current verification | Sustained HC-A continuous rating evidence |
| thermal verification | Temperature rise at sustained load |
| vehicle-load verification | Real vehicle actuators / track loads |

### Options considered

#### Option A — High-current channel directly on DevKit Power Board
#### Option B — External high-current load-bank module controlled through production interfaces
#### Option C — Highest-current class only on DCC Gen1 Phase E hardware
#### Option D — Staged: external module for early bounded discovery + Phase E confirmation on production Power

### Comparative decision matrix

| Criterion | Option A | Option B | Option C | Option D |
|-----------|----------|----------|----------|----------|
| Safety | Weak | Acceptable | Strong | Acceptable |
| Architecture consistency | Weak | Acceptable | Acceptable | Strong |
| Reuse toward DCC Gen1 | Acceptable | Acceptable | Strong | Strong |
| Representativeness | Strong | Acceptable | Strong (late) | Strong |
| Verification coverage | Strong | Acceptable | Weak (late discovery) | Strong |
| Development cost | Weak | Acceptable | Strong | Acceptable |
| Hardware cost | Weak | Acceptable | Strong | Acceptable |
| Schedule | Weak | Acceptable | Strong early / Weak late risk | Acceptable |
| Complexity | Weak | Acceptable | Strong | Acceptable |
| Debuggability | Acceptable | Strong | Weak early | Strong |
| Future migration | Acceptable | Acceptable | Strong | Strong |
| Risk | Unacceptable without heavy lab controls | Acceptable | Weak (late) | Acceptable |

Ratings: **Strong** · **Acceptable** · **Weak** · **Unacceptable**.

### Recommended option

**Recommended option: Option D.**

**Reason:** Places continuous highest-current and vehicle-load evidence on Phase E production Power (EDL-014), while allowing an external load-bank/module—controlled via production-intent interfaces—to discover control/protection issues earlier under bounded energy. Option A concentrates fire/thermal hazard on the DevKit PCB. Option C alone delays discovery. DevKit evidence **shall not** replace Phase E continuous/thermal/vehicle-load evidence for the highest class.

**Residual risks:** External module interface mismatch vs production Power; false confidence from bounded-energy protection tests.

**Evidence still required:** Module/fixture safety limits (ADR-023); numeric current envelope (ADR-021 / threshold WP); HC-A qualification records before claiming ratings.

**Decision that remains open:** Exact HC continuous amperes; whether any reduced high-current on-board channel is ever added (would need superseding ADR).

### Proposed mapping of verification types

| Type | DevKit (with external module as needed) | Phase E |
|------|-------------------------------------------|---------|
| logic/control | **Yes** | Confirm |
| diagnostic | **Yes** (bounded) | Confirm on production |
| protection (energy-limited) | **Yes** via fixture policy | Confirm |
| continuous-current HC | External module optional discovery only; **not** DevKit PCB mandate | **Required** |
| thermal HC sustained | Not DevKit PCB mandate | **Required** |
| vehicle-load | Out of DevKit | **Required** (as applicable) |

### Proposed decision text

```text
PROPOSED: Highest-current class verification follows Option D.
DevKit Power Board is not required to implement a production highest-current channel.
Early bounded high-current discovery may use an external load-bank/module driven through production-intent control/diagnostic interfaces.
Continuous-current, sustained thermal, and vehicle-load verification for the highest class remain mandatory on DCC Gen1 Phase E hardware and are not replaced by DevKit evidence.
Protection and diagnostic tests at controlled limited energy remain in DevKit scope per ADR-023.
No channel MPN or ampere rating is approved by this ADR.
```

### Consequences

Couples to ADR-021 envelope and fixture WP; electrical architecture omits mandatory on-board HC-A.

### Safety impact

Reduces on-board DevKit fire/thermal burden; shifts high energy to supervised external/Phase E contexts.

### Verification impact

Unblocks writing HC scope into `C-001` declarations; continuous HC cases stay Phase E / external; NOT VERIFIED.

### Firmware / Hardware / Configuration / Migration

Firmware may include HC control paths tested at bounded current; hardware DevKit omits mandatory HC power stage; config should not claim HC continuous capability on DevKit inventory.

### Rejected alternatives

Option A as default; Option C as sole strategy without early external discovery path.

### Open dependencies

ADR-019, ADR-021, ADR-023; threshold WP; Phase E plan.

### Requirements affected

`REQ-DCC-V-DK-005`, `014`, `041`; EHPS-related future vehicle reqs (external docs).

### Verification cases affected

`VER-DCC-DK-C-001`, energy-related C-005/C-006 scope notes; Phase E (outside DevKit plan).

### TBDs affected

Constrains `TBD-DK-002/003`; does not close them.

### Follow-up Work Packages

Fixture/load-bank requirements; threshold analysis; Phase E planning.

### Rollback or supersession path

Superseding ADR.

### Architecture Review section

| Field | Value |
|-------|-------|
| **Review status** | Pending Architecture Review |
| **Architect decision** | TBD |
| **Acceptance conditions** | TBD |
| **Rejection / correction notes** | TBD |

### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-20 | Implementation Engineer (WP-008) | Proposed package |

