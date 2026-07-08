# Doc checklist

Проверка полноты документации Gen1. Обновлено: 2026-07-07.

## Официальные документы (`docs/`)

| ID | Файл | Статус | Примечание |
|----|------|--------|------------|
| — | README.md (root) | ✅ | Обзор + индекс |
| — | CONCEPT_GEN1_SUMMARY.md | ✅ | Сжатое ТЗ |
| 000 | 000_Project_Vision.md | ✅ | |
| 001 | 001_System_Architecture.md | ✅ | |
| 002 | 002_DCC_Hardware.md | ✅ | Тепловая модель — TBD |
| 003 | 003_ECU_Architecture.md | ✅ | Детали железа ECU — Фаза 2 |
| 004 | 004_Communication_Protocol.md | ✅ | CAN ID / бинарный SPI — TBD |
| 005 | 005_Configuration_Model.md | ✅ | Schema / бинарный runtime — TBD |
| 006 | 006_Web_Interface.md | ✅ | Auth, макеты UI — TBD |
| 007 | 007_Component_Selection.md | ✅ | |
| 008 | 008_Testing_and_Validation.md | ✅ | |
| 009 | 009_Roadmap.md | ✅ | |
| — | config/vehicles/e30_gen1.yaml | ✅ | Профиль E30 |
| — | agents_stuff/dcpi_structs_v0.1.md | ✅ | Конспект SPI |
| — | agents_stuff/config_binary_v0.1.md | ✅ | Конспект binary config |
| — | agents_stuff/DOC_PROGRESS.md | ✅ | Этапы заполнения |

## Источник концепции

- ChatGPT share: https://chatgpt.com/share/6a4c9df4-a7b0-83ed-8a7b-1897abf06207
- Тема: «Разработка PDM для E30» → эволюция в DriveCore / DCC

## Ещё не создано (ожидаемо позже)

| Артефакт | Когда |
|----------|-------|
| `firmware/` дерево исходников | Фаза 0, после протокола |
| `web/` статика UI | После DevKit |
| `config/schema/` YAML schema | После 004/005 детализации |
| `hardware/` KiCad | После тепловой модели |
| CAN DBC / `.dcmsg` spec | Этап протокола |

## Быстрая проверка «всё на месте»

```bash
ls docs/000_Project_Vision.md docs/001_System_Architecture.md \
   docs/002_DCC_Hardware.md docs/003_ECU_Architecture.md \
   docs/004_Communication_Protocol.md docs/005_Configuration_Model.md \
   docs/006_Web_Interface.md docs/007_Component_Selection.md \
   docs/008_Testing_and_Validation.md docs/009_Roadmap.md \
   docs/CONCEPT_GEN1_SUMMARY.md docs/EDL/README.md
```

Все 12 путей должны существовать.
