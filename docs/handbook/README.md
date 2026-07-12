# DriveCore Engineering Handbook v1.0

Официальный инженерный справочник проекта. Дополняет нумерованную документацию `docs/000–009` и EDL.

| Документ | Содержание |
|----------|------------|
| [PROJECT_PHILOSOPHY.md](PROJECT_PHILOSOPHY.md) | Философия платформы |
| [ENGINEERING_VALUES.md](ENGINEERING_VALUES.md) | Инженерные ценности |
| [ENGINEERING_WORKFLOW.md](ENGINEERING_WORKFLOW.md) | Жизненный цикл работ |
| [REVIEW_PROCESS.md](REVIEW_PROCESS.md) | Процесс ревью |
| [COMPONENT_QUALIFICATION_PROCESS.md](COMPONENT_QUALIFICATION_PROCESS.md) | Квалификация компонентов |

## Cursor rules (из handbook)

Полные правила агента:

| Файл | Уровень |
|------|---------|
| [`.cursor/rules/drivecore-engineering.mdc`](../../.cursor/rules/drivecore-engineering.mdc) | Полный — mandatory instructions |
| [`.cursor/rules/drivecore-engineering-skills.mdc`](../../.cursor/rules/drivecore-engineering-skills.mdc) | Полный — engineering skills |

Краткие rule-индексы v1.0 (из handbook):

| Файл | Тема |
|------|------|
| `task-execution.mdc` | Read → Implement → Validate → Report → Stop |
| `review-checklist.mdc` | Requirements, Architecture, Tests, Docs, Risks |
| `component-selection.mdc` | Datasheet, Lifecycle, Thermal, Alternatives, Qualification |
| `documentation-standard.mdc` | IDs, ADR/EDL, статусы |
| `coding-standard.mdc` | Readable, deterministic, no magic numbers |
| `hardware-design-standard.mdc` | Diagnostics, serviceability |
| `communication-protocols.mdc` | Versioned binary protocols |
| `safety-principles.mdc` | ESP32 never safety-critical |

## Архив

Оригинальный пакет: [DriveCore_Engineering_Handbook_v1.0.zip](DriveCore_Engineering_Handbook_v1.0.zip)

## Статус

**v1.0** — каркас handbook + rule-индексы. Развёрнутые тексты — в `.cursor/rules/drivecore-engineering*.mdc` и `docs/000+`.
