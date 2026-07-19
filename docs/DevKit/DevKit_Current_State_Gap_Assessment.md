# DevKit Current-State Gap Assessment — Gen1

**Document ID:** DOC-DK-GAP-001  
**Version:** 1.0.2  
**Status:** Proposed  
**Work Package:** WP-007 / WP-007-R2  
**Date:** 2026-07-19

Audit of existing DevKit-related claims against WP-007 authority rules. Classifications:

`COMPLIANT` · `PARTIAL` · `NOT IMPLEMENTED` · `NOT VERIFIED` · `CONFLICT` · `TBD`

## Assessment table

| Existing claim or artifact | Source | Classification | Supported by | Conflict | Required action | Suggested WP / CR | Priority |
|----------------------------|--------|----------------|--------------|----------|-----------------|-------------------|----------|
| EDL-014 DevKit gate before vehicle | docs/EDL/README.md | COMPLIANT | Accepted EDL | — | Preserve; map to DK-A…D | WP-007 (done) | P0 |
| Three-board DCC / Gen2 Power swap | EDL-007 | COMPLIANT | Accepted EDL | — | Preserve | — | P0 |
| J_LP + kill/enable + BOARD_ID pins | EDL-011; docs/002 | PARTIAL | Accepted EDL | Encoding map missing | Define BOARD_ID map without new HW | Hardware identity WP | P0 |
| Logic identical to Gen1 Rev.A | docs/008 §2.1 | CONFLICT / TBD | Candidate only | docs/007 allows STM32G431 DevKit-only | ADR-DK-001 | Architecture decision | P0 |
| Radio identical to Gen1 Rev.A | docs/008 §2.1 | TBD | Candidate only | Physical vs interface equivalence undefined | ADR-DK-002 | Architecture decision | P0 |
| Same firmware binary as Gen1 | docs/008 §2.4 | CONFLICT | Candidate | MCU alt + no FW projects | ADR-DK-003 | Architecture decision | P0 |
| Power Rev.DK reduced channels | docs/008; docs/002 §10 | PARTIAL | Consistent candidate counts | Connector wording conflict | Freeze representative classes ADR-DK-004 | DevKit electrical architecture WP | P0 |
| Channel counts HS30×2 / HS15×4 / HS05×4 / HB×1 / no HS60 | docs/002/008/yaml/hardware README | PARTIAL | Internally consistent counts | HS* vs WP-004 HC* taxonomy; yaml missing ch9–10 outputs | Map classes; complete profile after ADR | Config + architecture | P1 |
| Exact smart-switch MPNs (BTS*/BTN*) | docs/008 §2.2; docs/007 | CANDIDATE → not normative | EDL-003 technology only | Remap vs Gen1 channel↔MPN | Keep as candidates; qualify later | Component qualification | P1 |
| H-bridge present on DevKit | docs/008 | PARTIAL | Capability required by REQ-DCC-V-DK-042 | MPN candidate only | Verify by capability | Power architecture WP | P1 |
| Absence of HS60 on DevKit | docs/008 | PARTIAL | Consistent statement | Whether any high-current class mandatory | ADR-DK-005 | Architecture decision | P0 |
| WAGO output terminals | docs/008; docs/007 | CONFLICT | Candidate | docs/002 §10 “винтовые” | ADR-DK-012 | Architecture decision | P1 |
| DTM CAN connector | docs/008 | CANDIDATE | — | Not mandated by Accepted ADR | Keep candidate | Connector policy WP | P2 |
| USB-C role | docs/008 | CANDIDATE | Gen1 Logic intent | — | Keep candidate | Electrical architecture WP | P2 |
| Hammond enclosure | docs/008; docs/007 | CANDIDATE | — | — | ADR-DK-012 | Architecture decision | P2 |
| BOOT/USER/KILL buttons | docs/008 | CANDIDATE | Kill testability required | Button implementation not frozen | Require kill testability; UI buttons candidate | Electrical architecture WP | P1 |
| 13.8 V / 30 A bench limits | docs/008 | TBD | Candidates only | Not authoritative freeze | TBD-DK-001, TBD-DK-002, TBD-DK-003 (register §4); ADR-DK-006 | Threshold CR | P0 |
| Exact lamp wattages / loads | docs/008 | CANDIDATE | — | hardware README / yaml partial mismatch | Treat as example loads | Fixture WP | P2 |
| `hardware.profile: devkit` | docs/008; devkit.yaml | CONFLICT / PARTIAL | File present | Not in docs/005 schema | Schema decision | Config schema CR | P1 |
| Phase A–D procedures in docs/008 | docs/008 §5–8 | PARTIAL | Strategy accepted via EDL-014 | Vague pass criteria; duplicate vs WP-007 plan | Navigate to DevKit_Verification_Plan | WP-007 (done) | P0 |
| Existing pass thresholds (±5%, 200 ms, 10.5 V, …) | docs/008 | TBD | Candidates | Vague terms (“immediately”, “waveform clean”) | Threshold register | Threshold CR | P0 |
| OTA in DevKit gate | docs/008 B14 | TBD | Protocol exists in docs | Mandatory? | ADR-DK-008 | Architecture decision | P1 |
| Configuration hot reload | docs/008 D10 | TBD / CONFLICT | Config model intent | Mode auth / Service Mode rules | ADR-DK-009 | Architecture decision | P1 |
| Physical fault injection | docs/008 §12; DC-DCC-PWR-089 | PARTIAL / TBD | Proposed power reqs | Safe methods undefined | ADR-DK-010 | Fixture + ADR | P0 |
| Representative class coverage vs Gen1 | DC-DCC-PWR-108 Proposed | PARTIAL | Count differences allowed | Class set not frozen | ADR-DK-004/005 | Architecture decision | P0 |
| `hardware/devkit/` KiCad | hardware/devkit | NOT IMPLEMENTED | README + `.kicad_pro` only | — | Design after requirements acceptance | PCB WP | P1 |
| `firmware/dcc/logic` / `radio` | firmware/ | NOT PRESENT | shared headers only | — | Bring-up after ADR-DK-003 | Firmware WP | P1 |
| `config/vehicles/devkit.yaml` | config/ | PARTIAL | Present scaffold | Cooling thresholds vs docs/008 D4/D5; incomplete channels | Align after ADR; do not invent in WP-007 | Config WP | P1 |
| `tools/can_sim` | tools/ | PARTIAL | Scaffold present | Not verified | Use in Phase B/D when ready | Bench tooling WP | P2 |
| `tools/bench` automation | docs/008 TBD | NOT PRESENT | — | — | Future tooling | Bench tooling WP | P2 |
| Test equipment list | docs/008 §3.2 | PARTIAL | Candidate equipment | Models not mandated | Keep capability-based | Fixture WP | P2 |
| Safety procedures | docs/008 §3.3 | PARTIAL | Intent useful | Vague continuous limit | Normalize via requirements C/D | WP-007 (done) + thresholds | P0 |
| Revision identity on DevKit tests | ADR-015 / STD-REV-001 | PARTIAL | Normative standard Approved | Runtime metadata NOT IMPLEMENTED | Use VE template fields | Evidence integration | P0 |
| Traceability for DevKit | matrix pre-WP-007 empty | PARTIAL → importing | WP-007 rows | Evidence still TBD | Keep NOT VERIFIED | WP-007 (done) | P0 |
| Threshold authority | docs/008 numerics | TBD | Candidates | vs WP-004 TBD amperes | Do not freeze without evidence | Threshold CR | P0 |
| Evidence templates | docs/templates VE | COMPLIANT (scaffold) | CR-002 | No filled VE | Create VE when tests run | Execution WP | P2 |
| Physical fixtures / load bank | — | NOT IMPLEMENTED | — | Short fixture undefined | Fixture WP + ADR-DK-010 | Fixture WP | P0 |
| Automated-test coverage | — | NOT VERIFIED / NOT IMPLEMENTED | — | — | After bring-up | Bench tooling WP | P2 |
| SRS §8.1 DevKit | Volume_2 placeholder | NOT IMPLEMENTED → pointer added | WP-007 | — | Keep pointer; no text duplication | WP-007 (done) | P0 |

## Classification counts

| Classification | Count (rows above) |
|----------------|--------------------|
| COMPLIANT | 3 |
| PARTIAL | 18 |
| NOT IMPLEMENTED | 5 |
| NOT PRESENT | 2 |
| NOT VERIFIED | 2 |
| CONFLICT | 5 |
| TBD | 10 |
| CANDIDATE (explicit) | 8 |

Note: some rows carry dual tags (e.g. CONFLICT/TBD); counts reflect primary severity tag used in the Classification column.

## Conflicts detail

1. **Identical Logic / same binary vs G431 DevKit MCU** — docs/008 vs docs/007.  
2. **Output connector family** — WAGO (008/007) vs screw terminals (002 §10).  
3. **Channel index↔MPN remap** undocumented relative to Gen1 tables.  
4. **HS* ampere taxonomy vs WP-004 abstract classes with TBD amperes.**  
5. **Phase D cooling thresholds** — docs/008 95/102 °C vs `devkit.yaml` 92/100 °C.  
6. **`hardware.profile`** present in yaml/008 but absent from docs/005 schema.

## Paths NOT PRESENT

| Path | Status |
|------|--------|
| `firmware/dcc/logic/` | NOT PRESENT |
| `firmware/dcc/radio/` | NOT PRESENT |
| `hardware/devkit` schematics/PCB beyond `.kicad_pro` | NOT PRESENT |
| `hardware/dcc/` reuse tree | NOT PRESENT |
| `tools/bench/` | NOT PRESENT |
| Filled `docs/records/verification/VE-*` for DevKit | NOT PRESENT |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 initial gap assessment |
| 1.0.1 | 2026-07-19 | WP-007-R1 — note governance split; no ADR/TBD resolutions |
| 1.0.2 | 2026-07-19 | WP-007-R2 — TBD references point to restored register (no value closures) |
