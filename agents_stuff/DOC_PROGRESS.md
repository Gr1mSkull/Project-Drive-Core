# Document filling progress

Последовательное заполнение документации по этапам.

## Этапы

| Этап | Фокус | Документы | Статус |
|------|-------|-----------|--------|
| **1** | Архитектура | 001, 004, 005 | ✅ v0.1 |
| **2** | Аппаратура DCC | 002, 007 | ✅ v0.1 |
| **3** | ECU + интерфейсы | 003, 006 | ✅ v0.1 |
| **4** | Валидация + DevKit | 008 | ✅ v0.1 |
| **5** | Схемы / код | hardware/, firmware/ | 🔲 |

## Этап 4 — чеклист

- [x] 008 — DevKit spec, стенд, фазы A–F, acceptance, fail operational
- [x] EDL-014 — DevKit gate перед машиной
- [x] `agents_stuff/devkit_bench_v0.1.md`

## Следующий этап (5)

- [ ] `firmware/shared`, `tools/can_sim`, `tools/config_compiler`
- [ ] `config/vehicles/devkit.yaml`
- [ ] `hardware/devkit` KiCad Rev.DK
- [ ] `web/ui` минимальный UI

## Правило

Документация этапов 1–4 закрыта. Этап 5 — реализация по `CODE_LAYOUT_PLAN.md`.
