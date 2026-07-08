# Code layout plan

Планируемая **модульная** структура репозитория. Папки создаются по мере начала реализации.

```
Project-Drive-Core/
├── docs/                    # Официальная документация (есть)
├── agents_stuff/            # Конспекты агентов (есть)
├── config/
│   ├── schema/              # JSON Schema / YAML schema
│   └── vehicles/
│       └── e30_gen1.yaml    # Профиль E30
├── firmware/
│   ├── shared/              # CRC, protocol structs, drivecore_proto
│   │   ├── include/
│   │   └── src/
│   ├── dcc/
│   │   ├── logic/           # STM32 — FreeRTOS app
│   │   │   ├── Core/
│   │   │   ├── App/         # power_manager, vcm, can, ...
│   │   │   └── CMakeLists.txt
│   │   └── radio/           # ESP32 — IDF / Arduino
│   │       ├── main/
│   │       └── components/
│   ├── button_box/
│   ├── ecu/                 # Фаза 2
│   └── devkit/              # Общая DevKit прошивка (или alias dcc)
├── hardware/
│   ├── dcc/
│   │   ├── logic/
│   │   ├── power/
│   │   └── radio/
│   ├── button_box/
│   ├── devkit/
│   └── ecu/
├── web/
│   └── ui/                  # Статика → прошивается в ESP32
│       ├── index.html
│       ├── main.js
│       └── style.css
└── tools/
    ├── config_compiler/     # YAML → binary for STM32
    └── can_sim/             # Тестовые пакеты
```

## Принципы модульности

1. **`firmware/shared`** — единственный источник структур протокола (пока нет codegen).
2. **Каждый продукт** (dcc/logic, button_box, ecu) — отдельный CMake/IDF проект.
3. **DevKit** — супerset или отдельная target-плата с меньшим числом каналов.
4. **Web UI** — не зависит от STM32; только REST/WS контракт из `docs/004`, `docs/006`.
5. **Config** — YAML в Git; бинарник генерируется `tools/config_compiler`.

## Порядок появления кода

1. `firmware/shared` + `tools/can_sim` (протокол)
2. `firmware/dcc/logic` + `firmware/dcc/radio` на DevKit
3. `web/ui` минимальная таблица
4. `config/vehicles/e30_gen1.yaml`
5. `hardware/devkit` (KiCad)
6. Остальное по roadmap

## Статус

✅ Скелет этапа 5 создан — см. `firmware/`, `tools/`, `web/`, `hardware/devkit/`.

```bash
make test-all      # CRC + config compiler + can_sim smoke
make build-config  # build/*.dcfg
```
