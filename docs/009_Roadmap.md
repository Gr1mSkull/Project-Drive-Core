# 009 — Roadmap

## Фаза 0 — Foundation

- DriveCore DevKit
- Архитектура и документация (этот репозиторий)
- DriveCore Protocol (CAN FD + SPI + REST/WebSocket)
- Модель конфигурации
- Bootloader / OTA pipeline

### WP-007 / WP-008 / WP-009 / WP-010 / WP-011 / WP-012 status (2026-07-20)

| Item | Status |
|------|--------|
| DevKit requirements baseline (`REQ-DCC-V-DK-*`) | **Accepted** (WP-007 / PR #11) — evidence NOT VERIFIED |
| DevKit verification plan (DK-A…DK-D) | **Accepted** structure — cases NOT EXECUTED / BLOCKED |
| DevKit P0 ADRs (ADR-016…023) | **Accepted** (WP-008); ADR-021/022 numerics Open |
| WP-009 threshold analysis | **Accepted** (2026-07-20); numeric values Open; TBD-DK-007 **BLOCKED_BY_EDL_CLARIFICATION** |
| WP-010 functional electrical architecture | **Accepted** (2026-07-20); WP-010-R1 Accepted |
| WP-011 EDL-011 + component-class prep | **Accepted** (2026-07-20); WP-011-R1 Accepted |
| WP-012 electrical sizing architecture framework | **Ready for Final Architecture Acceptance** — WP-012-R2 |
| DevKit hardware design | **NOT IMPLEMENTED** — sizing/schematic/PCB NOT AUTHORIZED |
| DevKit built / verified | **No** — NOT VERIFIED |
| Remaining decisions | ADR-DK-008/009/011/012; TBD-DK-007 BLOCKED (not Resolved); thresholds TBD-DK-001…022 Open |

**Next step:** Final Architecture Acceptance of WP-012 (WP-012-R2 corrections applied).

**Next expected engineering stage:** WP-012 acceptance → component-class qualification / symbolic preliminary calculation → fixture requirements → (only then) schematic/PCB/firmware WPs.

## Фаза 1 — Первый автомобиль (E30)

- DCC Gen1 (Logic + Power + Radio)
- Button Box Gen1
- Web UI (планшет)
- Интеграция с E30
- Стенд + тесты в машине

## Фаза 2 — Силовая установка

- ECU Gen1
- Логгер / калибровка
- Анализ данных

## Фаза 3 — Экосистема

- Датчики
- Беспроводная телеметрия
- Конфигуратор
- Нативное мобильное приложение (если Web UI недостаточно)

## Фаза 4 — Gen2

- DCC Gen2 (больше каналов / другие ключи — только Power Board)
- Собственная приборная панель (Dash)
- Ethernet
- Несколько шин CAN FD

## Порядок разработки Gen1 (из диалога)

1. Архитектура и протокол
2. DevKit
3. DCC Gen1
4. Button Box
5. Web UI
6. Интеграция E30
7. ECU
8. Gen2

## Заполнение документации (по этапам)

| Этап | Документы | Статус |
|------|-----------|--------|
| **1. Архитектура** | 001, 004, 005, EDL 008–010 | ✅ v0.1 |
| **2. Аппаратура** | 002, 007, EDL 011 | ✅ v0.1 |
| **3. ECU + UI** | 003, 006, EDL 012–013 | ✅ v0.1 |
| **4. Валидация** | 008, EDL 014 | ✅ v0.1 |
| **5. Реализация** | firmware/shared, tools/, web/ui, hardware/devkit | ✅ scaffold v0.1 |

Прогресс: `agents_stuff/DOC_PROGRESS.md`

## Документация

| ID | Документ | Статус |
|----|----------|--------|
| 000 | Project Vision | ✅ |
| 001 | System Architecture | ✅ **v0.1** |
| 002 | DCC Hardware | ✅ **v0.1** |
| 003 | ECU Architecture | ✅ **v0.1** |
| 004 | Communication Protocol | ✅ **DCP v0.1** |
| 005 | Configuration Model | ✅ **schema v0.1** + e30_gen1.yaml |
| 006 | Web Interface | ✅ **v0.1** |
| 007 | Component Selection | ✅ **v0.1** |
| 008 | Testing and Validation | ✅ **v0.1** |
| 009 | Roadmap | ✅ |
| EDL | Engineering Decision Log | ✅ 14 записей |
| — | agents_stuff/ | ✅ |
| — | config/vehicles/e30_gen1.yaml | ✅ |

## Будущее: single source of truth для CAN

Описания сообщений → автогенерация структур для STM32, ESP32, TypeScript, документации, тестовых пакетов.
