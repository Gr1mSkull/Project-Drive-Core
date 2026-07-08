# 003 — ECU Architecture

Версия: **Gen1 v0.1** · Статус: **этап 3 — зафиксировано**

**DriveCore ECU** — отдельный модуль платформы. Только силовая установка.

## 1. Принцип

> **ECU управляет двигателем. DCC управляет автомобилем.**

ECU не знает о фарах, дворниках, стеклоподъёмниках. Не коммутирует силовые цепи кузова.

| Модуль | Зона ответственности |
|--------|----------------------|
| **ECU** | Впрыск, зажигание, турбо, антилаг, VVT, детонация, телеметрия двигателя |
| **DCC** | Питание, VCM, кнопки, свет, охлаждение (исполнение), диагностика, журнал, конфиг |

## 2. Взаимодействие ECU ↔ DCC

### 2.1 Принцип «Request, don't control»

ECU **не включает** вентилятор, помпу или бензонасос напрямую. Публикует:

- телеметрию (`rpm`, `coolant_temp`, `oil_pressure`, …)
- **cooling_request** (`cooling_level` 0–3)

DCC применяет правила из `config/vehicles/e30_gen1.yaml` (`rules`, `ecu_bindings`).

```
ECU ──CAN──► cooling_level=2
              │
DCC rules engine ──► fan1 ON, fan2 ON (если temp > 100 °C)
```

ECU может **запросить** режим через COMMAND (опц. Gen1), но VCM остаётся на DCC.

### 2.2 Что DCC делает с данными ECU

| Данные ECU | Использование DCC | Пример правила |
|------------|-------------------|----------------|
| `coolant_temp` | Ступени вентиляторов | `coolant_temp_gt: 92` → fan1 |
| `cooling_level` | Прямое следование запросу ECU | level 2 → оба вентилятора |
| `rpm` + `oil_pressure` | Предупреждения | low oil при rpm > 2500 |
| `engine_running` | VCM переходы | READY → ENGINE_RUN |
| `battery_v` (своя) | Derating EHPS | `battery_lt: 11.0` |

DCC **не вмешивается** в алгоритмы впрыска/зажигания.

### 2.3 Питание ECU

ECU питается от **канала DCC Ch7** (`ecu_power` в e30_gen1.yaml). При OFF / FAULT ECU обесточен — это штатное поведение VCM.

## 3. CAN — сообщения ECU (DCP v0.1)

Узел: **Device Type = 0x2**, Instance = 0, Node base = **0x20**.

Формула ID: `CAN_ID = (MC << 8) | (DT << 4) | DI`

### 3.1 Исходящие (ECU → шина)

| Сообщение | MC | msg_type | CAN ID | Период | Описание |
|-----------|-----|----------|--------|--------|----------|
| HEARTBEAT | 0 | 0x01 | **0x020** | 100 ms | Живость узла |
| ENGINE_TELEM | 1 | 0x20 | **0x120** | 20 ms | RPM, temp, pressure, throttle |
| COOLING_REQ | 1 | 0x21 | **0x120* | 100 ms | `cooling_level` 0–3 |

\* Тот же CAN ID, различие по `msg_type` в payload (multiplex в одном MC).

#### ENGINE_TELEM payload (msg_type 0x20)

| Offset | Size | Поле | Тип | Масштаб |
|--------|------|------|-----|---------|
| 4 | 2 | `rpm` | u16 | 1 |
| 6 | 2 | `coolant_temp` | i16 | 0.1 °C |
| 8 | 2 | `oil_pressure` | u16 | кПа |
| 10 | 1 | `throttle` | u8 | % |
| 11 | 1 | `engine_flags` | u8 | bit0=running, bit1=sync, bit2=warmup |
| 12 | 2 | `map_kpa` | u16 | опц. |
| 14 | 2 | `lambda_x1000` | u16 | опц. |

#### COOLING_REQ payload (msg_type 0x21)

| Offset | Size | Поле | Описание |
|--------|------|------|----------|
| 4 | 1 | `cooling_level` | 0=off, 1=stage1, 2=stage2, 3=max |
| 5 | 1 | `reason` | 0=auto, 1=overtemp, 2=ac, 3=manual |

### 3.2 Входящие (DCC → ECU)

| Сообщение | MC | msg_type | CAN ID | Описание |
|-----------|-----|----------|--------|----------|
| DIAG_REQUEST | 3 | 0x40 | **0x320** | Запрос диагностики |
| VEHICLE_MODE | 3 | 0x44 | **0x320** | Текущий VCM режим (опц.) |
| OTA_MODE | 3 | 0x42 | **0x320** | Переход в bootloader |

Gen1: ECU **слушает** VEHICLE_MODE для логики warmup; не блокирует запуск при потере CAN (fail-safe на стороне DCC).

### 3.3 Кэш ECU на DCC

STM32 хранит последний валидный снимок (см. `dcpi_state_v1_t` в `agents_stuff/dcpi_structs_v0.1.md`). Таймаут ECU HEARTBEAT > 500 ms → `ecu_status = LOST`, правила с `engine_running` не срабатывают.

## 4. Аппаратура ECU Gen1 (outline)

> Полный BOM ECU — **Фаза 2** ([009_Roadmap.md](009_Roadmap.md)). Gen1 E30 может использовать **сторонний ECU** с CAN-адаптером до готовности DriveCore ECU.

### 4.1 Блок-схема

```
┌─────────────────────────────────────────────┐
│              DriveCore ECU Gen1             │
│  ┌─────────┐   ┌──────────┐   ┌───────────┐ │
│  │ STM32   │──►│ Drivers  │──►│ Injectors │ │
│  │ G431    │   │ Ignition │   │ Coils     │ │
│  └────┬────┘   └──────────┘   └───────────┘ │
│       │ CAN FD                                │
│  ┌────┴────┐   ┌──────────┐                  │
│  │ TCAN1042│   │ Sensors  │ ← MAP, CLT, IAT │
│  └─────────┘   │ Crank/Cam│                  │
│                └──────────┘                  │
│  J_PWR (DT)    J_CAN (DTM)    J_SENSOR (DTM) │
└─────────────────────────────────────────────┘
```

### 4.2 Компоненты (ориентир)

| Блок | Компонент | Комментарий |
|------|-----------|-------------|
| MCU | **STM32G431CBT6** или G474 | Достаточно для 4 cyl turbo |
| CAN | **TCAN1042HGVDRBRQ1** | Тот же чип, что DCC |
| FRAM | **FM24CL64B** | Калибровки, логи |
| Watchdog | **TPS3430** | Как на DCC Logic |
| Buck/LDO | TPS54302 + TPS7A1633 | 12 V → 5/3.3 V |
| Reverse protect | LM74700-Q1 | Automotive input |

### 4.3 Разъёмы

| Ref | Тип | Назначение |
|-----|-----|------------|
| J_PWR | **DT04-2P** | +12V / GND от DCC Ch7 |
| J_CAN | **DTM06-4S** | CAN_H, CAN_L, +12V ref, GND |
| J_SENSOR | **DTM12-12SA** | Датчики двигателя |
| J_IGN | **DT04-4P** | Катушки / igniter |
| J_INJ | **DTM06-6S** | Форсунки |
| J_SWD | Tag-Connect | Отладка |

### 4.4 Датчики E30 (гоночный I4 turbo — ориентир)

| Сигнал | Тип | Интерфейс MCU | Примечание |
|--------|-----|---------------|------------|
| Crank | 60-2 VR / Hall | Timer capture | Обязательный |
| Cam | Hall | GPIO / capture | VVT sync |
| CLT | NTC / analog | ADC | Охлаждение |
| IAT | NTC | ADC | Турбо |
| MAP | 0–5 V | ADC | Впуск |
| Oil pressure | 0–5 V | ADC | Предупреждения |
| Oil temp | NTC | ADC | Опц. |
| Lambda | Wideband CAN / 0–5 V | ADC или CAN | Внешний контроллер |
| Knock | Piezo | ADC + DSP | Опц. Gen1 |
| TPS | Pot / DBW | ADC / PWM | DBW — Фаза 2 |
| Fuel pressure | 0–5 V | ADC | Опц. |
| Boost | 0–5 V | ADC | WG control — PWM out |

Точная распиновка — в `config/ecu/e30_m20_turbo.yaml` (TBD, этап 5).

### 4.5 Разработка на DevKit

До собственной платы ECU:

1. **DriveCore DevKit** + CAN к DCC DevKit — тест протокола.
2. **ECU simulator** в `tools/can_sim` — эмуляция ENGINE_TELEM + COOLING_REQ.
3. Сторонний ECU (Megasquirt, EMU, Link) с **CAN mapping** на DCP — допустимо для E30 Gen1.

## 5. Прошивка ECU — архитектура

FreeRTOS, модульная структура (`firmware/ecu/`):

```
firmware/ecu/
├── App/
│   ├── engine_control/    # Fuel, spark, boost (Фаза 2)
│   ├── can_manager/       # DCP encode/decode
│   ├── sensor_manager/    # ADC, crank, cam
│   ├── cooling_request/   # cooling_level algorithm
│   ├── config_manager/    # FRAM calibrations
│   ├── diagnostics/       # DTC, limp mode
│   └── logger/            # High-speed log buffer
├── Core/                  # STM32 HAL, FreeRTOS
└── CMakeLists.txt
```

### 5.1 Задачи FreeRTOS (план)

| Задача | Приоритет | Период | Описание |
|--------|-----------|--------|----------|
| `engine_fast` | Highest | 1 ms | Crank sync, injection (Фаза 2) |
| `can_tx` | High | 20 ms | ENGINE_TELEM |
| `can_rx` | High | event | DCC commands |
| `sensors` | Medium | 10 ms | ADC фильтрация |
| `cooling` | Medium | 100 ms | cooling_level |
| `heartbeat` | Low | 100 ms | HEARTBEAT |
| `diag` | Low | event | По запросу |

Gen1 **на стенде**: только `can_tx` + `cooling` + `heartbeat` (симулятор).

### 5.2 Cooling request — алгоритм v0.1

```text
if CLT < 80°C:  level = 0
elif CLT < 92°C: level = 0 (ECU не запрашивает, DCC rules по temp)
elif CLT < 100°C: level = 1
elif CLT < 108°C: level = 2
else: level = 3
```

DCC **может** игнорировать level и использовать только `coolant_temp` в rules — настраивается в YAML `ecu_bindings.cooling_mode: direct | rules_only | hybrid`.

## 6. Конфигурация ECU

### 6.1 Связь с DCC config

В `e30_gen1.yaml`:

```yaml
ecu_bindings:
  rpm: ecu.telemetry.rpm
  coolant_temp: ecu.telemetry.coolant_temp
  oil_pressure: ecu.telemetry.oil_pressure
  engine_running: ecu.telemetry.engine_running
  cooling_level: ecu.telemetry.cooling_level
```

DCC не хранит калибровки впрыска — только телеметрию и bindings.

### 6.2 ECU profile (будущее)

`config/ecu/e30_m20_turbo.yaml` — цилиндры, датчики, CAN publish rate. Компилируется отдельно от vehicle config.

## 7. Диагностика и limp mode

| Условие | Действие ECU | DCC |
|---------|--------------|-----|
| CLT sensor fail | Limp, fixed fan request level 3 | Лог + notify |
| Oil pressure low | Rev limit / warning flag | `low_oil_warning` rule |
| CAN lost | ECU продолжает (локально) | `ecu_status=LOST`, не менять VCM на ENGINE_RUN без RPM |
| DCC FAULT | ECU работает | Нет cooling execution |

DTC коды ECU — `DIAGNOSTIC` MC, msg_type TBD (Фаза 2).

## 8. OTA ECU

| Путь | Описание |
|------|----------|
| CAN OTA | DCC COMMAND 0x42 → ECU bootloader (Фаза 2) |
| USB-SWD | Прямая прошивка на столе |
| Через DCC Web UI | ESP32 → DCC → CAN → ECU (цепочка, Фаза 2) |

Gen1 E30: прошивка ECU **вне** DriveCore OTA pipeline допустима.

## 9. Статус

- [x] Граница ECU / DCC, request-don't-control
- [x] CAN сообщения v0.1 с ID и payload
- [x] Аппаратный outline, датчики E30, разъёмы
- [x] Архитектура прошивки, cooling algorithm
- [x] Интеграция с e30_gen1.yaml
- [ ] `config/ecu/e30_m20_turbo.yaml`
- [ ] Полный BOM ECU (Фаза 2)
- [ ] Engine control algorithms (Фаза 2)

## Связанные документы

- [001_System_Architecture.md](001_System_Architecture.md)
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
- [config/vehicles/e30_gen1.yaml](../config/vehicles/e30_gen1.yaml)
- [agents_stuff/ecu_can_messages_v0.1.md](../agents_stuff/ecu_can_messages_v0.1.md)
