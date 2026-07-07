# Project-Drive-Core

**DriveCore** — открытая модульная автомобильная платформа. Gen1 разрабатывается под BMW E30 (гоночная конфигурация).

Центральный узел — **DCC (DriveCore Controller)**: PDM + VCM + диагностика + CAN gateway + data logging. Вместе с **Button Box** и **Web UI на планшете** заменяет штатную проводку и реле.

## Документация

| Документ | Описание |
|----------|----------|
| [docs/000_Project_Vision.md](docs/000_Project_Vision.md) | Философия, принципы, цели |
| [docs/001_System_Architecture.md](docs/001_System_Architecture.md) | Архитектура системы и модулей |
| [docs/CONCEPT_GEN1_SUMMARY.md](docs/CONCEPT_GEN1_SUMMARY.md) | Сжатый итог концепции Gen1 (E30) |
| [docs/007_Component_Selection.md](docs/007_Component_Selection.md) | Компонентная база |
| [docs/009_Roadmap.md](docs/009_Roadmap.md) | Дорожная карта |
| [docs/EDL/](docs/EDL/) | Engineering Decision Log |

## Ключевой принцип

> **Hardware is fixed, behavior is fully configurable.**

Мы не делаем устройство — мы создаём платформу.

## Статус

Концепция Gen1 зафиксирована. Следующие шаги: тепловая модель силовой части, CAN message model, DevKit.
