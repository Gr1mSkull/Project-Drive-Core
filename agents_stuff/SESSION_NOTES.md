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

- Logic↔Power: SPI + enable (детализация на этапе 2)
- JSON Schema файл — этап 2 или позже

### Следующий этап

**Этап 2:** `002_DCC_Hardware` — тепловая модель, Logic↔Power, pinout expansion.

### Для следующего агента

1. `agents_stuff/DOC_PROGRESS.md` — текущий этап
2. Официальные решения — `docs/`; конспекты — `agents_stuff/`
3. Профиль E30 — `config/vehicles/e30_gen1.yaml`
