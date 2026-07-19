# Verification Evidence Template

**Document ID:** TPL-VE-001  
**Version:** 1.1.2  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1 · **ADR:** ADR-015

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6 (Evidence-backed validation), §4 / §13 (verification authority).

**Revision identity (normative field meanings):** [`docs/standards/REVISION_IDENTITY_STANDARD.md`](../standards/REVISION_IDENTITY_STANDARD.md) (ADR-015) — composite system baseline. Do not treat project version, firmware version, protocol version, hardware revision, or configuration identity as interchangeable. Encoded wire values are not semantic `MAJOR.MINOR` unless the interface specification defines the mapping.

**Storage convention (filled records only):**

```text
docs/records/verification/VE-YYYY-NNN_<short-title>.md
```

Templates remain in `docs/templates/`.

**Field marking rules:**

- Use `N/A` only when the field does **not apply**.
- Unknown applicable fields: `TBD`, `UNKNOWN`, or `NOT RECORDED` — never `N/A`.

**Authority:**

- Implementer may record raw test results.
- Independent Reviewer or Test Owner records verification certification for high-impact work.
- System Architect approval is separate from verification outcome.

---

## Verification Evidence

| Field | Value |
|-------|-------|
| **Evidence ID** | VE-YYYY-NNN |
| **Related Requirement IDs** | |
| **Related WP / CR** | |
| **Date** | YYYY-MM-DD |
| **Tester (name/agent)** | |
| **Tester role** | Implementation Engineer \| Test Owner \| other |
| **Commit SHA** | Full repository commit (immutable) |
| **Hardware Revision** | Board ID + HW / BOM / assembly rev (+ serial if available) — STD-REV-001 §6 |
| **Firmware Version** | Per module: SemVer + SHA / cleanliness — STD-REV-001 §4 |
| **Bootloader Version** | Separate from application firmware — STD-REV-001 §5 |
| **Configuration ID** | Stable profile ID (e.g. `e30_gen1`, `devkit`) — STD-REV-001 §8 |
| **Configuration Hash** | Full lowercase SHA-256 hex (not CRC) — STD-REV-001 §8 |
| **Protocol Version** | Each applicable contract `MAJOR.MINOR` — STD-REV-001 §7 |
| **DCFG Format Version** | Compiled format version when config blob used — STD-REV-001 §9 |
| **Test Equipment** | |
| **Test Environment** | |
| **System Baseline Reference** | Embedded fields above and/or controlled baseline reference — STD-REV-001 §10 |

### Procedure

Exact command, procedure, or measurement method:

```text

```

### Inputs

|

### Expected Result

|

### Actual Result

|

### Evidence Files

| Type | Path / location |
|------|-----------------|
| Log | |
| Report | |
| Capture / measurement | |

### Result (raw)

| Field | Value |
|-------|-------|
| **Raw result recorded by tester** | PASS / FAIL / PARTIAL / NOT VERIFIED |
| **Limitations** | |
| **Open Issues** | |

### Verification certification (Independent Reviewer / Test Owner)

| Field | Value |
|-------|-------|
| **Certified result** | PASS / FAIL / PARTIAL / NOT VERIFIED / TBD |
| **Certifier (name/agent)** | |
| **Certifier role** | Independent Reviewer \| Test Owner |
| **Certification date** | YYYY-MM-DD or TBD |
| **Evidence reference reviewed** | this VE ID / path |

> A command without its actual result is not evidence. Unexecuted tests = `NOT VERIFIED`.  
> Implementer shall not independently certify own high-impact work as verified.

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 initial template |
| 1.1 | 2026-07-19 | CR-002-R1 records path; separate tester vs certifier |
| 1.1.1 | 2026-07-19 | Reference revision-identity standard; baseline fields |
| 1.1.2 | 2026-07-19 | ADR-015-R1 — canonical ADR-015; encoded-version caution |
