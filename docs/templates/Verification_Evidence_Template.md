# Verification Evidence Template

**Document ID:** TPL-VE-001  
**Version:** 1.1  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6 (Evidence-backed validation), §4 / §13 (verification authority).

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
| **Commit SHA** | |
| **Hardware Revision** | |
| **Firmware Version** | |
| **Bootloader Version** | |
| **Configuration ID** | |
| **Configuration Hash** | |
| **Protocol Version** | |
| **Test Equipment** | |
| **Test Environment** | |

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
