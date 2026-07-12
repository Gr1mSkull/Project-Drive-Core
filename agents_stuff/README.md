# agents_stuff

**Внутренние конспекты для AI-агентов.** Не официальная документация проекта.

Официальные документы — в `docs/`. Здесь: чеклисты, карта модулей, ссылки, заметки сессий, план структуры кода.

**Обязательные правила для агента в Cursor:**

| Файл | Назначение |
|------|------------|
| [`.cursor/rules/drivecore-engineering.mdc`](../.cursor/rules/drivecore-engineering.mdc) | Инженерные правила, границы решений, workflow |
| [`.cursor/rules/drivecore-engineering-skills.mdc`](../.cursor/rules/drivecore-engineering-skills.mdc) | Mindset и профессиональные навыки |
| [`.cursor/rules/task-execution.mdc`](../.cursor/rules/task-execution.mdc) | Read → Implement → Validate → Report → Stop |
| [`.cursor/rules/review-checklist.mdc`](../.cursor/rules/review-checklist.mdc) | Чеклист ревью |
| [`.cursor/rules/component-selection.mdc`](../.cursor/rules/component-selection.mdc) | Квалификация компонентов |
| [`.cursor/rules/documentation-standard.mdc`](../.cursor/rules/documentation-standard.mdc) | Стандарты документации |
| [`.cursor/rules/coding-standard.mdc`](../.cursor/rules/coding-standard.mdc) | Стандарты кода |
| [`.cursor/rules/hardware-design-standard.mdc`](../.cursor/rules/hardware-design-standard.mdc) | Стандарты железа |
| [`.cursor/rules/communication-protocols.mdc`](../.cursor/rules/communication-protocols.mdc) | CAN, DCPI, REST |
| [`.cursor/rules/safety-principles.mdc`](../.cursor/rules/safety-principles.mdc) | Безопасность платформы |

Инженерный handbook: [docs/handbook/README.md](../docs/handbook/README.md).

## Файлы

| Файл | Назначение |
|------|------------|
| [DOC_CHECKLIST.md](DOC_CHECKLIST.md) | Что создано / что ещё TBD |
| [MODULE_MAP.md](MODULE_MAP.md) | Модульная карта архитектуры + ссылки на docs |
| [CODE_LAYOUT_PLAN.md](CODE_LAYOUT_PLAN.md) | Планируемая структура репозитория (код) |
| [LINKS.md](LINKS.md) | Внешние ссылки |
| [SESSION_NOTES.md](SESSION_NOTES.md) | Заметки по сессиям |

## Правило для агентов

1. Собираем **архитектуру и код модульно** — один модуль = одна зона ответственности.
2. Перед правками — сверка с `docs/` и этой папкой.
3. Новые решения — в `docs/EDL/` (официально) + краткая запись в `SESSION_NOTES.md`.
4. Не дублировать длинные тексты: ссылаться на `docs/NNN_*.md`.
