# DriveCore Cursor Rules

**WP-006** — Engineering Constitution integration.

## Authoritative source

| File | Role |
|------|------|
| **[`.cursor/ENGINEERING_CONSTITUTION.mdc`](../ENGINEERING_CONSTITUTION.mdc)** | **Single source of truth** for all engineering policy (`alwaysApply: true`) |

## Numbered wrappers (WP-001 → WP-006)

Files `00`–`10` remain for Cursor path compatibility. Each is a **pointer** to constitution sections — not independent policy.

| File | Constitution sections |
|------|------------------------|
| `00_project_role.mdc` | §4, §5, §8, §11 |
| `01_engineering_rules.mdc` | §6, §9, §21 |
| `02_engineering_skills.mdc` | §3, §7 |
| `03_task_execution.mdc` | §12, §19, §20 |
| `04_review_process.mdc` | §18 |
| `05_component_selection.mdc` | §10, §11, §15, §21 |
| `06_documentation_standard.mdc` | §13 |
| `07_firmware_standard.mdc` | §14, §16 |
| `08_hardware_standard.mdc` | §9, §15 |
| `09_protocol_standard.mdc` | §9, §16 |
| `10_safety_standard.mdc` | §17 |

## Extended narrative (reference docs)

- `docs/PROJECT_PHILOSOPHY.md`, `docs/ENGINEERING_VALUES.md`, `docs/ENGINEERING_WORKFLOW.md`, `docs/REVIEW_PROCESS.md`
- Architecture: `docs/001`, `docs/004`, `docs/005`, `docs/EDL/`
- Agent context: `.ai/project_context.md`

## Migration history

| Version | Change |
|---------|--------|
| WP-001 | Foundation Pack v1.0 — rules 00–10 |
| WP-006 | Consolidated into `ENGINEERING_CONSTITUTION.mdc`; rules become wrappers |

Historical rule text is preserved in constitution sections and WP-001 git history — not deleted.
