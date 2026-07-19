# Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-2026-001 |
| **Impact Level** | 2 — Full CIA |
| **Title** | DriveCore Platform Revision Identity and System Baseline |
| **Author** | Implementation Engineer (cloud agent) |
| **Author role** | Implementation Engineer |
| **Date** | 2026-07-19 |
| **Status** | Accepted |
| **Related WP / CR** | ADR-015 (Originating Decision Request: ADR-CR002-001; Originating Change Request: CR-002 / CR-002-R1 / CR-002-R2) |

### Reason for Change

Constitution §6 requires uniquely identifiable testable system states and flags an undefined project-wide versioning scheme as **ARCHITECTURAL DECISION REQUIRED**. CR-002 evidence templates reference identity fields without a coherent composite model. The System Architect approved the direction: independent artifact identities with a composite system baseline. This change formalizes that direction as ADR + normative standard and records compatibility / migration gaps.

### Current Behaviour

* Partial identity fragments exist (protocol constants, HEARTBEAT `fw_version`, YAML `config_version` / profile, hardware prose revisions, `BOARD_ID` pins, VE template fields).
* Prior to this change: no accepted revision-identity ADR or normative standard (now ADR-015 Accepted; STD-REV-001 Approved — documentation only).
* No firmware/bootloader build-metadata generation.
* No configuration SHA-256 content identity.
* DCFG CRC-16/CCITT-FALSE exists; coverage inconsistent across sources.
* Filled verification baselines with complete identity: none (**NOT VERIFIED**).

### Proposed Behaviour

* ADR-015 records the decision: composite baseline of independent artifact identities (`ADR-CR002-001` retained only as originating decision request / legacy alias).
* `docs/standards/REVISION_IDENTITY_STANDARD.md` is the normative source for fields, formats, compatibility, and evidence rules.
* Supporting docs reference the standard without duplicating full rules.
* Implementation of build metadata, hashing, and wire/format changes is **out of scope** for this change.

### Affected Requirements

| Requirement ID | Source | Impact |
|----------------|--------|--------|
| Constitution §6 Baseline and revision identity | `.cursor/ENGINEERING_CONSTITUTION.mdc` | Satisfies ADR-required gap at documentation level; runtime compliance later |
| Traceability / evidence completeness | CR-002 scaffold | Evidence fields map to standard; statuses remain NOT VERIFIED until implemented |
| Atomic SRS IDs | `docs/SRS/`, matrix families | No atomic IDs invented; families unchanged |

### Affected Modules

Documentation and process: ADR, standards, CIA, verification evidence guidance, testing docs, indexes.

Runtime modules (future impact when implemented): DCC-LOGIC, DCC-RADIO, DCC-POWER, ECU, BUTTON-BOX, DEVKIT, config compiler, qualification / VE records.

### Affected Interfaces

| Interface | Current version | Proposed version | Breaking? |
|-----------|-----------------|------------------|-----------|
| DCP | `proto_ver` 0x01 / doc v0.1 | Unchanged by this CIA | NO |
| DCPI | `proto_ver` 0x01 | Unchanged | NO |
| DCFG binary | `DCFG_VERSION` 0x0001 | Unchanged; CRC coverage TBD remains | NO (doc TBD only) |
| YAML schema | `config_version` "0.1" | Unchanged; SHA-256 rule for future | NO |
| REST `/api/v1/` | Path-level | Unchanged | NO |
| WebSocket telemetry | No schema version field | Unchanged | NO |
| BOARD_ID hardware | Pins defined; encoding TBD | Unchanged (no new HW mechanism) | NO |

### Affected Files

Created/updated in this task only:

* `docs/ADR/ADR-015-platform-revision-identity.md`
* `docs/standards/README.md`
* `docs/standards/REVISION_IDENTITY_STANDARD.md`
* `docs/records/change_impact/CIA-2026-001_revision-identity-baseline.md`
* Index / reference updates listed in the ADR task (ADR README, root README, `docs/008`, traceability README, VE/RHP templates)

No firmware, hardware, protocol, configuration payload, or build-script files.

### Affected Tests

* DevKit / vehicle test recording rules gain composite baseline requirements (documentation).
* Existing Phase A–F procedures in `docs/008` are not rewritten as new test methods; they shall reference the standard for identity recording.
* No automated tests added or executed for runtime identity (**NOT VERIFIED** for runtime).

### Affected Documentation

ADR index, standards folder, testing doc cross-reference, traceability related links, VE/RHP templates (pointer to standard), root README standards row.

### Compatibility Assessment

| Aspect | Assessment |
|--------|------------|
| Backward compatibility | Compatible — no wire/format change in this task |
| Forward compatibility | Compatible — defines rules for future additive identity metadata |
| Silent field reinterpretation risk | None in this task — prohibited by decision; existing CRC coverage CONFLICT noted as TBD |

### Migration Requirements

See ADR §13 and compliance matrix in the completion report. Summary:

1. Architect accepts ADR + standard.
2. Build metadata WP.
3. Hardware identity recording / BOARD_ID encoding map WP.
4. Protocol/schema mismatch-reaction completeness per interface.
5. Config canonicalization + SHA-256 WP.
6. DCFG CRC coverage interface decision + metadata linkage.
7. VE / DevKit baseline integration.

### Rollback Method

Revert the documentation PR that introduces ADR-015, STD-REV-001, and CIA-2026-001. No runtime rollback required (no implementation shipped).

### Safety Impact

| Area | Impact |
|------|--------|
| Safe states | None |
| Kill / isolation | None |
| Fail-operational behaviour | None |

Indirect safety benefit later: prevents certification of unidentified hardware/firmware/config states.

### Validation Required

* PR #9 merged before start — executed
* Branch from updated `main` — executed
* ADR ID uniqueness — executed
* Links resolve — executed
* No implementation file changes — executed
* No fabricated current-state version values — executed
* Runtime identity generation — **NOT VERIFIED** (out of scope)

### Open Questions

See ADR-015 §15 (OQ-1 … OQ-6). Encoded-version mappings and DCFG CRC coverage remain separate interface decisions. Not reopened beyond task scope.

### Approvals (architecture / policy)

| Field | Value |
|-------|-------|
| **ADR Required** | YES |
| **Architect Approval Required** | YES |
| **ADR / EDL reference** | ADR-015; related EDL-007, EDL-009, EDL-010, EDL-011, EDL-014 |
| **Architect approver (name/agent)** | System Architect |
| **Architect role** | System Architect |
| **Architect approval date** | 2026-07-19 |
| **Architecture review date** | 2026-07-19 |
| **Conditions** | Encoded-version mappings and DCFG CRC coverage remain separate interface decisions. Approval is not implementation verification. |

### Review acknowledgment (not architecture approval)

| Field | Value |
|-------|-------|
| **Reviewer (name/agent)** | TBD |
| **Reviewer role** | Independent Reviewer |
| **Review date** | TBD |
| **Evidence / CIA review note** | Documentation-only CIA for ADR formalization |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | Initial CIA for ADR-015 formalization |
| 1.0.1 | 2026-07-19 | ADR-015-R1 — Status Accepted; canonical ADR-015 |
