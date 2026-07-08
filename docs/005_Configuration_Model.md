# 005 — Configuration Model

Версия схемы: **config-v0.1** · Профиль E30: [config/vehicles/e30_gen1.yaml](../config/vehicles/e30_gen1.yaml)

> **Hardware is fixed, behavior is fully configurable.**

## 1. Поток данных

```
config/vehicles/*.yaml  (Git, ручное редактирование)
        ↓
   Web UI / REST PUT
        ↓
   ESP32: validate (schema v0.1)
        ↓
   config_compiler → binary blob
        ↓
   SPI CONFIG_LOAD → STM32 → FRAM (active) + Flash (backup)
        ↓
   Runtime: VCM + Power Manager + Rules Engine
```

## 2. Структура YAML (schema v0.1)

```yaml
config_version: "0.1"          # обязательно
vehicle:
  name: string
  profile: string              # e.g. e30_gen1

hardware:                      # описание ёмкости (для валидатора)
  channels:
  hbridges:

modes:                         # VCM — порядок переходов
  - OFF
  - MASTER_ON
  # ...

outputs:                       # логические функции → физические каналы
  <name>:
    channel: int               # 1..22
    type: high_side|pwm|hbridge
    current_limit_a: float
    pwm: bool
    retry: int
    modes:                     # режим → поведение
      IGNITION: off|on|auto|prime
      ENGINE_RUN: ...

inputs:
  <name>:
    source: button_box|can|analog|digital
    control_id: int            # для button_box
    pin: string                # для digital

rules:                         # условная логика
  - name: string
    when: { ... }              # выражение
    then: [ actions ]          # список действий

ecu_bindings:                  # сигналы с CAN ECU
  coolant_temp: ecu.telemetry.coolant_temp
  cooling_request_from: ecu.telemetry.cooling_level
```

## 3. VCM — коды режимов (runtime)

| ID | Имя | Описание |
|----|-----|----------|
| 0 | OFF | |
| 1 | MASTER_ON | |
| 2 | IGNITION | |
| 3 | PRIME | |
| 4 | READY | |
| 5 | ENGINE_RUN | |
| 6 | RACE | |
| 7 | COOL_DOWN | |

Переходы задаются в прошивке VCM; таблица `outputs.*.modes` определяет **что включено** в каждом режиме.

## 4. Поведение выходов в режимах

| Значение | Смысл |
|----------|-------|
| `off` | Выключен |
| `on` | Включен |
| `auto` | По rules / ECU / датчикам |
| `prime` | Импульс прогрева (бензонасос) |

## 5. Rules engine (v0.1)

Минимальный набор условий:

| Условие | Тип |
|---------|-----|
| `vehicle_mode` | enum |
| `ignition_on` | bool |
| `engine_running` | bool |
| `coolant_temp_gt` | °C |
| `oil_pressure_lt` | bar |
| `battery_lt` / `battery_gt` | V |
| `vehicle_speed_lt` | km/h |
| `button_event` | control_id + action |
| `ecu.cooling_level` | int |

Действия:

| Действие | Описание |
|----------|----------|
| `output_on: <name>` | Включить выход |
| `output_off: <name>` | Выключить |
| `set_mode: <mode>` | Смена VCM |
| `log_event: <text>` | Журнал |
| `notify: <level>` | Уведомление UI |

## 6. Бинарный runtime-формат (STM32)

Заголовок blob:

| Offset | Size | Поле |
|--------|------|------|
| 0 | 4 | Magic `DCFG` |
| 4 | 2 | `config_version` |
| 6 | 2 | `crc16` |
| 8 | 2 | `output_count` |
| 10 | 2 | `rule_count` |
| 12 | n | `outputs[]` — фиксированная struct per channel |
| | m | `rules[]` — компактные записи |
| | k | `mode_table[]` — битовая матрица |

Детальные размеры struct — в `agents_stuff/config_binary_v0.1.md`.

## 7. Журнал событий

Записи (FRAM кольцевой буфер + Flash архив):

```text
<unix_ts> <severity> <source> <message>
```

Примеры: `IGN ON`, `Fuel Pump Prime`, `Fan1 Overcurrent`, `Fan1 Recovered`.

Экспорт: `GET /api/events` → JSON / CSV.

## 8. Версионирование и миграция

- `config_version` в YAML обязателен
- Несовпадение версии → отказ `CONFIG_FAIL` + сообщение в UI
- Миграции: `tools/config_migrate/v0.1_to_v0.2.py` (когда появится v0.2)

## 9. Валидация

Правила v0.1:

1. Каждый `outputs.*.channel` уникален и в пределах 1..22
2. `current_limit_a` ≤ аппаратного максимума класса канала
3. H-bridge только на `type: hbridge`
4. `rules` не ссылаются на несуществующие outputs/inputs
5. Критичные выходы (ECU, fuel_pump) имеют `retry ≥ 1`

## 10. Статус

- [x] Схема v0.1 и семантика
- [x] Профиль E30 (`config/vehicles/e30_gen1.yaml`)
- [ ] JSON Schema файл (`config/schema/v0.1.json`)
- [ ] `tools/config_compiler`
- [ ] Редактор в Web UI

## Связанные документы

- [001_System_Architecture.md](001_System_Architecture.md)
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [config/vehicles/e30_gen1.yaml](../config/vehicles/e30_gen1.yaml)
