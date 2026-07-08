# 005 — Configuration Model

> **Hardware is fixed, behavior is fully configurable.**

Поведение автомобиля задаётся конфигурацией, а не перепрошивкой.

## Формат (человекочитаемый)

YAML — единый файл конфигурации, хранимый в Git, с понятными diff.

```yaml
vehicle:
  name: BMW E30

outputs:
  fuel_pump:
    channel: 5
    current_limit: 15
    pwm: false
    retry: 3

  fan1:
    channel: 2
    pwm: true
    temp_on: 92

inputs:
  start_button:
    source: ButtonBox.Start

rules:
  - if: ignition_on
    then: fuel_pump_prime
```

## Поток данных

```
YAML (редактор / Web UI)
    ↓
ESP32: валидация, хранение
    ↓
Бинарный формат → STM32 (через SPI)
    ↓
Runtime: Power Manager, VCM, rules engine
```

## Сущности конфигурации

| Сущность | Описание |
|----------|----------|
| `vehicle` | Имя/профиль машины |
| `outputs` | Каналы: номер, лимиты, PWM, retry |
| `inputs` | Источники: Button Box, CAN, аналог |
| `rules` | Условная логика «если → то» |
| `modes` | Таблица активности выходов по режимам VCM |

## Режимы VCM (привязка к конфигу)

Режимы: OFF → MASTER ON → IGNITION → PRIME → READY → ENGINE RUN → RACE → COOL DOWN.

Каждый output имеет таблицу: в каких режимах активен (и как — ON / AUTO / PRIME).

## Виртуальные выходы и правила

Примеры из концепции:

```yaml
rules:
  - if:
      engine_running: true
      coolant_temp_gt: 95
      battery_gt: 11.8
      vehicle_speed_lt: 30
    then: fan1_on

  - if:
      oil_pressure_lt: 1.2
      rpm_gt: 2500
    then: [buzzer, flash_dash, log_error]
```

## Журнал событий

Не только коды ошибок — история с метками времени:

```text
08:15:11  IGN ON
08:15:12  Fuel Pump Prime
08:28:42  Fan1 Overcurrent
08:28:43  Fan1 Recovered
```

Хранение: FRAM (краткосрочно) + Flash (архив). Экспорт через Web UI.

## Версионирование

- Версия схемы конфига в заголовке файла
- Миграции при смене формата
- Экспорт/импорт через ESP32 (файловая система)

## Статус

- [x] Концепция и примеры YAML
- [ ] JSON Schema / валидатор
- [ ] Бинарный runtime-формат для STM32
- [ ] Редактор в Web UI

## Связанные документы

- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [006_Web_Interface.md](006_Web_Interface.md)
- [001_System_Architecture.md](001_System_Architecture.md) — VCM
