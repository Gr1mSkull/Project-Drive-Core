# Document filling progress

Последовательное заполнение документации по этапам.

## Этапы

| Этап | Фокус | Документы / код | Статус |
|------|-------|-----------------|--------|
| **1** | Архитектура | 001, 004, 005 | ✅ v0.1 |
| **2** | Аппаратура DCC | 002, 007 | ✅ v0.1 |
| **3** | ECU + интерфейсы | 003, 006 | ✅ v0.1 |
| **4** | Валидация + DevKit | 008 | ✅ v0.1 |
| **5** | Скелет реализации | firmware/, tools/, web/, hardware/ | ✅ v0.1 |

## Этап 5 — чеклист

- [x] `firmware/shared` — CRC, DCP/DCPI/config headers, CMake + test
- [x] `tools/config_compiler` — YAML → DCFG, unit tests
- [x] `tools/can_sim` — ECU heartbeat/telemetry CLI
- [x] `config/vehicles/devkit.yaml`
- [x] `web/ui` — Race / Service / Logger (vanilla JS)
- [x] `hardware/devkit` — README + KiCad scaffold
- [x] `Makefile` — test-all, build-config

## Следующий шаг (реализация v0.2)

- [ ] `firmware/dcc/logic` STM32 CubeIDE project
- [ ] `firmware/dcc/radio` ESP-IDF + REST/WS stub
- [ ] KiCad Power Rev.DK полная схема
- [ ] `tools/can_sim` SocketCAN backend
