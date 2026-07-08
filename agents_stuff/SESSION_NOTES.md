# Session notes

## 2026-07-07 — Импорт концепции

### Сделано

- Прочитан ChatGPT share (45 сообщений), тема PDM E30 → DriveCore.
- Созданы docs 000, 001, 007, 009, CONCEPT_GEN1_SUMMARY, EDL (7 записей).
- PR #1 открыт.

### Сделано (продолжение)

- Дополнены docs 002–006, 008 (были 🔲 в roadmap).
- Создана `agents_stuff/` для конспектов агента.
- Зафиксирован план модульной структуры кода (`CODE_LAYOUT_PLAN.md`).

### Запомнить

- **Модульно:** архитектура + код по MODULE_MAP; не монолит.
- **DCC** = Logic + Power + Radio; планшет не критичен.
- **ECU** только двигатель; кузов — DCC.
- **DevKit** до DCC Gen1 для автомобиля.
- Следующий тех. шаг из чата: тепловая модель → CAN spec → DevKit.

### Открытые вопросы

- Одна CAN шина vs CAN1(ECU)+CAN2(Body) в Gen1?
- Точный бинарный формат SPI STM32↔ESP32?
- Logic↔Power: только SPI+enable или ещё сигналы?

## 2026-07-08 — Этап 1: Архитектура

### Сделано

- **001** v0.1: одна CAN FD, E30 нагрузки, безопасность, DTM12, VCM
- **004** DCP v0.1: CAN ID layout, сообщения, DCPI/SPI, REST/WS
- **005** schema v0.1 + `config/vehicles/e30_gen1.yaml`
- EDL-008 (одна шина), EDL-009 (DCP), EDL-010 (бинарный SPI)
- Конспекты: `dcpi_structs_v0.1.md`, `config_binary_v0.1.md`

### Закрытые вопросы

- ~~Одна CAN vs две~~ → **одна** (EDL-008)
- SPI формат → **DCPI v0.1** (EDL-010)

### Открытые

- JSON Schema файл — этап 3 или позже

### Следующий этап

**Этап 3:** `003_ECU_Architecture`, `006_Web_Interface` — детализация железа ECU и Web UI.

## 2026-07-08 — Этап 2: Аппаратура DCC

### Сделано

- **002** v0.1: трёхплатная структура, J_LP 30-pin, J_EXP 20-pin, канальная карта PROFET
- **007** v0.1: BOM Logic/Power/Radio, пассивы, разъёмы Deutsch, DevKit subset
- Тепловая модель E30 (worst case RACE ~15 W)
- EDL-011 — Logic↔Power SPI + fail-safe
- `agents_stuff/thermal_notes_v0.1.md`

### Закрытые вопросы

- ~~Logic↔Power интерфейс~~ → **J_LP SPI + enable** (EDL-011)

### Следующий этап

**Этап 3:** ECU architecture + Web Interface.

### Для следующего агента

1. `agents_stuff/DOC_PROGRESS.md` — текущий этап (4)
2. Официальные решения — `docs/`; конспекты — `agents_stuff/`
3. Профиль E30 — `config/vehicles/e30_gen1.yaml`

## 2026-07-08 — Этап 3: ECU + Web UI

### Сделано

- **003** v0.1: CAN ECU messages (ID, payload), hardware outline, sensors E30, cooling request, firmware modules
- **006** v0.1: UIMode screens, PIN+Bearer auth, REST full map, WebSocket formats, Wi-Fi SoftAP
- EDL-012 — симулятор/сторонний ECU до Фазы 2
- EDL-013 — Web UI auth model
- `agents_stuff/ecu_can_messages_v0.1.md`, `web_ui_routes_v0.1.md`

### Следующий этап

**Этап 4:** `008_Testing_and_Validation` — DevKit spec, test procedures, acceptance.

### Для следующего агента

1. `agents_stuff/DOC_PROGRESS.md` — этап 5 (код)
2. `agents_stuff/CODE_LAYOUT_PLAN.md` — структура репо
3. Документация 000–009 + EDL — **закрыта v0.1**

## 2026-07-08 — Этап 4: Валидация

### Сделано

- **008** v0.1: DevKit spec, стенд, фазы A–F, channel tests, integration, DCC/E30 acceptance
- EDL-014 — обязательный DevKit gate перед машиной
- `agents_stuff/devkit_bench_v0.1.md`

### Следующий этап

**Этап 5:** код — `firmware/shared`, `tools/can_sim`, `web/ui`, KiCad DevKit.

## 2026-07-08 — Этап 5: Скелет реализации

### Сделано

- `firmware/shared` — proto/dcpi/config headers, CRC-16, CMake test
- `tools/config_compiler` — e30 + devkit → DCFG, unittest
- `tools/can_sim` — ECU/heartbeat CLI
- `config/vehicles/devkit.yaml`
- `web/ui` — Race/Service/Logger vanilla JS
- `hardware/devkit` — README + devkit.kicad_pro scaffold
- `Makefile` — test-all, build-config

### Следующий шаг

STM32/ESP32 проекты, KiCad Power Rev.DK, SocketCAN в can_sim.
