# Doc checklist

Проверка полноты документации Gen1. Обновлено: 2026-07-08.

## Официальные документы (`docs/`)

| ID | Файл | Статус | Примечание |
|----|------|--------|------------|
| — | README.md (root) | ✅ | Обзор + индекс |
| — | docs/handbook/ | ✅ | Engineering Handbook v1.0 |
| — | docs/handbook/DriveCore_Engineering_Handbook_v1.0.zip | ✅ | Оригинальный архив |
| 000 | 000_Project_Vision.md | ✅ | |
| 001 | 001_System_Architecture.md | ✅ | |
| 002 | 002_DCC_Hardware.md | ✅ | **v0.1** — тепловая модель, J_LP/J_EXP |
| 003 | 003_ECU_Architecture.md | ✅ | **v0.1** — CAN, sensors, firmware outline |
| 004 | 004_Communication_Protocol.md | ✅ | **DCP v0.1** |
| 005 | 005_Configuration_Model.md | ✅ | **schema v0.1** |
| 006 | 006_Web_Interface.md | ✅ | **v0.1** — auth, REST, screens |
| 007 | 007_Component_Selection.md | ✅ | **v0.1** — BOM per channel |
| 008 | 008_Testing_and_Validation.md | ✅ | **v0.1** — DevKit, фазы A–F |
| 009 | 009_Roadmap.md | ✅ | |
| — | config/vehicles/e30_gen1.yaml | ✅ | Профиль E30 |
| — | firmware/shared/ | ✅ | DCP headers + CRC |
| — | tools/config_compiler/ | ✅ | YAML → DCFG |
| — | tools/can_sim/ | ✅ | CAN simulator CLI |
| — | web/ui/ | ✅ | Минимальный UI |
| — | hardware/devkit/ | ✅ | KiCad scaffold |
| — | agents_stuff/dcpi_structs_v0.1.md | ✅ | Конспект SPI |
| — | agents_stuff/config_binary_v0.1.md | ✅ | Конспект binary config |
| — | agents_stuff/ecu_can_messages_v0.1.md | ✅ | ECU CAN конспект |
| — | agents_stuff/web_ui_routes_v0.1.md | ✅ | REST/WS конспект |
| — | agents_stuff/devkit_bench_v0.1.md | ✅ | Стенд конспект |
| — | agents_stuff/DOC_PROGRESS.md | ✅ | Этапы заполнения |

## Источник концепции

- ChatGPT share: https://chatgpt.com/share/6a4c9df4-a7b0-83ed-8a7b-1897abf06207
- Тема: «Разработка PDM для E30» → эволюция в DriveCore / DCC

## Ещё не создано (ожидаемо позже)

| Артефакт | Когда |
|----------|-------|
| `firmware/` дерево исходников | ✅ shared; logic/radio — TBD |
| `web/` статика UI | ✅ web/ui минимальный |
| `config/schema/` YAML schema | После 004/005 детализации |
| `hardware/` KiCad | ✅ devkit scaffold; полная схема TBD |
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
