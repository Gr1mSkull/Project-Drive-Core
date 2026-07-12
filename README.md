# Project-Drive-Core

**DriveCore** — открытая модульная автомобильная платформа. Gen1 разрабатывается под BMW E30 (гоночная конфигурация).

Центральный узел — **DCC (DriveCore Controller)**: PDM + VCM + диагностика + CAN gateway + data logging. Вместе с **Button Box** и **Web UI на планшете** заменяет штатные блоки и реле.

## Документация (`docs/`)

| ID | Документ | Описание |
|----|----------|----------|
| — | [CONCEPT_GEN1_SUMMARY.md](docs/CONCEPT_GEN1_SUMMARY.md) | Сжатое ТЗ Gen1 |
| 000 | [Project Vision](docs/000_Project_Vision.md) | Философия, принципы, цели |
| 001 | [System Architecture](docs/001_System_Architecture.md) | Архитектура системы и модулей |
| 002 | [DCC Hardware](docs/002_DCC_Hardware.md) | Платы Logic / Power / Radio |
| 003 | [ECU Architecture](docs/003_ECU_Architecture.md) | ECU — только двигатель |
| 004 | [Communication Protocol](docs/004_Communication_Protocol.md) | CAN FD, SPI, REST/WS |
| 005 | [Configuration Model](docs/005_Configuration_Model.md) | YAML, rules, VCM |
| 006 | [Web Interface](docs/006_Web_Interface.md) | Web UI на планшете |
| 007 | [Component Selection](docs/007_Component_Selection.md) | Компонентная база |
| 008 | [Testing and Validation](docs/008_Testing_and_Validation.md) | DevKit, стенд, чеклисты |
| 009 | [Roadmap](docs/009_Roadmap.md) | Дорожная карта |
| EDL | [Engineering Decision Log](docs/EDL/README.md) | Ключевые решения |
| HB | [Engineering foundation](docs/PROJECT_PHILOSOPHY.md) | Philosophy, workflow, SRS, ADR |
| SRS | [System Requirements](docs/SRS/README.md) | Volumes 1–3 (structure) |
| ADR | [Architecture decisions](docs/ADR/README.md) | ADR + EDL index |
| CQ | [Component Qualification](docs/Component_Qualification/README.md) | WP-002 qualification framework |

## AI context

- [`.ai/`](.ai/) — operational context for assistants
- [`.cursor/rules/`](.cursor/rules/) — WP-001 engineering rules (`00`–`10`)

## Ключевой принцип

> **Hardware is fixed, behavior is fully configurable.**

> **Мы не делаем устройство. Мы создаём платформу.**

## Конфигурация

- [config/vehicles/e30_gen1.yaml](config/vehicles/e30_gen1.yaml) — профиль BMW E30 Gen1
- [config/vehicles/devkit.yaml](config/vehicles/devkit.yaml) — профиль DevKit стенда

## Код (этап 5)

| Путь | Описание |
|------|----------|
| [firmware/shared/](firmware/shared/) | DCP/DCPI structs, CRC-16 |
| [tools/config_compiler/](tools/config_compiler/) | YAML → DCFG binary |
| [tools/can_sim/](tools/can_sim/) | CAN ECU/heartbeat simulator |
| [web/ui/](web/ui/) | Минимальный Web UI |
| [hardware/devkit/](hardware/devkit/) | KiCad scaffold Rev.DK |

```bash
make test-all
make build-config
```

## Статус

- **Этап 1 (архитектура):** ✅ docs 001, 004, 005 v0.1
- **Этап 2 (аппаратура):** ✅ docs 002, 007 v0.1
- **Этап 3 (ECU + UI):** ✅ docs 003, 006 v0.1
- **Этап 4 (валидация):** ✅ doc 008 v0.1
- **Этап 5 (реализация):** ✅ scaffold — `firmware/shared`, `tools/`, `web/ui`, `hardware/devkit`
- Сборка/тесты: `make test-all`
- Прогресс: [agents_stuff/DOC_PROGRESS.md](agents_stuff/DOC_PROGRESS.md)
