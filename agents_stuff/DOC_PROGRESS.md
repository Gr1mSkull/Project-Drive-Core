# Document filling progress

Последовательное заполнение документации по этапам.

## Этапы

| Этап | Фокус | Документы | Статус |
|------|-------|-----------|--------|
| **1** | Архитектура | 001, 004, 005 | ✅ v0.1 |
| **2** | Аппаратура DCC | 002, 007 | ✅ v0.1 |
| **3** | ECU + интерфейсы | 003, 006 | 🔲 |
| **4** | Валидация + DevKit | 008 | 🔲 |
| **5** | Схемы / код | hardware/, firmware/ | 🔲 |

## Этап 1 — чеклист

- [x] 001 — системная архитектура, E30, безопасность, CAN (одна шина)
- [x] 004 — DriveCore Protocol v0.1 (CAN, SPI, REST/WS)
- [x] 005 — модель конфигурации + `config/vehicles/e30_gen1.yaml`
- [x] EDL-008..010 — решения этапа 1
- [x] 009 — статусы обновлены
- [x] `agents_stuff/dcpi_structs_v0.1.md`, `config_binary_v0.1.md`

## Этап 2 — чеклист

- [x] 002 — тепловая модель v0.1, J_LP / J_EXP pinout, канальная карта, DevKit preview
- [x] 007 — BOM Logic/Power/Radio, PROFET per channel, DevKit subset, разъёмы
- [x] EDL-011 — Logic↔Power J_LP интерфейс
- [x] `agents_stuff/thermal_notes_v0.1.md`

## Следующий этап (3)

- [ ] 003 — ECU hardware sketch, CAN messages к DCC, сенсоры
- [ ] 006 — Web UI screens, auth, REST endpoints mapping

## Правило

Один этап = один PR/commit блок. Не переходить к KiCad, пока не закрыт этап 1–2.
