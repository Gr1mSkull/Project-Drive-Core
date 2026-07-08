# 004 — Communication Protocol

Версия: **DriveCore Protocol (DCP) v0.1** · Gen1

Единый стандарт обмена для всех модулей платформы. Именованные сообщения, не «магические» CAN ID без документации.

## 1. Уровни стека

| Уровень | Имя | Носитель |
|---------|-----|----------|
| L3 | DCP Application | Семантика сообщений |
| L2 | DCP Framing | CAN FD / SPI / HTTP |
| L1 | Physical | TCAN1042, SPI, Wi-Fi |

## 2. CAN FD — транспорт

### 2.1 Параметры шины

| Параметр | Gen1 |
|----------|------|
| Режим | CAN FD, BRS on |
| Nominal | 500 kbit/s |
| Data | 2 Mbit/s |
| ID | 11-bit standard |
| DLC | до 64 байт (FD) |
| Топология | Линейная, 2× 120 Ω |

### 2.2 Адресация узлов

| Device Type | Code | Gen1 Instance | Node |
|-------------|------|---------------|------|
| DCC | `0x1` | `0` | `0x10` |
| ECU | `0x2` | `0` | `0x20` |
| Button Box | `0x3` | `0` | `0x30` |
| Dash | `0x4` | — | резерв Gen2 |
| Expansion | `0x5` | `0–F` | `0x50+` |

Node ID = уникальный адрес на шине. При замене модуля Node ID сохраняется; Device Type определяет парсер.

### 2.3 Формат CAN ID (11 bit)

```
Bit 10..8   Message Class (MC)
Bit  7..4   Device Type (DT)
Bit  3..0   Device Instance (DI)
```

**Message Class (MC):**

| MC | Имя | Направление | Период |
|----|-----|-------------|--------|
| `0` | HEARTBEAT | Все → broadcast | 100 ms |
| `1` | TELEMETRY | Узел → bus | 10–100 ms |
| `2` | EVENT | Узел → bus | по событию |
| `3` | COMMAND | DCC → узел / узел → DCC | по запросу |
| `4` | DIAGNOSTIC | Узел → bus | по запросу / fault |
| `5` | CONFIG | DCC ↔ узел | при старте / OTA |

**Пример:** DCC Heartbeat = MC=0, DT=1, DI=0 → `0x010` = **0x008**  
Формула: `CAN_ID = (MC << 8) | (DT << 4) | DI`

### 2.4 Общий заголовок payload (CAN)

Все DCP-CAN кадры начинаются с:

| Offset | Size | Поле | Описание |
|--------|------|------|----------|
| 0 | 1 | `proto_ver` | `0x01` |
| 1 | 1 | `msg_type` | Тип внутри класса (см. ниже) |
| 2 | 2 | `seq` | Счётчик последовательности |
| 4 | n | `payload` | Тело сообщения |

## 3. Сообщения по классам

### 3.1 HEARTBEAT (`msg_type = 0x01`)

Период **100 ms**. Отсутствие > 500 ms → узел `LOST`.

| Offset | Size | Поле |
|--------|------|------|
| 4 | 1 | `node_state` — см. NodeState |
| 5 | 1 | `fault_flags` — битовая маска |
| 6 | 2 | `fw_version` — BCD major.minor |
| 8 | 4 | `uptime_ms` |

**NodeState:** `0`=BOOT, `1`=INIT, `2`=RUN, `3`=DEGRADED, `4`=FAULT, `5`=OTA

### 3.2 DCC TELEMETRY (`MC=1`, DT=1)

`msg_type = 0x10` — сводка системы, **50 ms**

| Поле | Тип | Описание |
|------|-----|----------|
| `vehicle_mode` | u8 | VCM режим (см. 005) |
| `battery_v` | u16 | мВ |
| `total_current` | u16 | мА (INA228) |
| `output_count` | u8 | активных каналов |
| `fault_summary` | u32 | битовая маска каналов |

`msg_type = 0x11` — пакет каналов (4 канала на кадр)

| Поле | Тип | Описание |
|------|-----|----------|
| `base_channel` | u8 | первый канал в пакете |
| `ch[n].state` | u8 | OutputState |
| `ch[n].current_ma` | u16 | |
| `ch[n].fault` | u8 | FaultReason |

**OutputState:** OFF=0, STARTING=1, ON=2, OVERCURRENT=3, RETRY=4, FAULT=5

**FaultReason:** NONE=0, OVERCURRENT=1, SHORT_GND=2, OPEN_LOAD=3, THERMAL=4, UNDERVOLT=5, CMD_OFF=6

### 3.3 ECU TELEMETRY (`MC=1`, DT=2)

`msg_type = 0x20` — **20 ms** (с движком)

| Поле | Тип | Масштаб |
|------|-----|---------|
| `rpm` | u16 | 1 |
| `coolant_temp` | i16 | 0.1 °C |
| `oil_pressure` | u16 | кПа |
| `throttle` | u8 | % |
| `engine_flags` | u8 | bit0=running, bit1=sync |

`msg_type = 0x21` — запрос охлаждения

| Поле | Тип | Описание |
|------|-----|----------|
| `cooling_level` | u8 | 0=off, 1–3 ступени |

### 3.4 Button Box EVENT (`MC=2`, DT=3)

`msg_type = 0x30` — по событию

| Поле | Тип | Описание |
|------|-----|----------|
| `control_id` | u16 | ID органа (HEADLIGHT, WIPER, …) |
| `action` | u8 | см. ButtonAction |
| `value` | i16 | для энкодера: delta |

**ButtonAction:** PRESS=1, RELEASE=2, LONG_PRESS=3, HOLD=4, ROTATE=5, DOUBLE=6

DCC не знает физику кнопки — только `control_id` + `action`.

### 3.5 COMMAND

| msg_type | От | Кому | Описание |
|----------|-----|------|----------|
| `0x40` | DCC | любой | Запрос диагностики |
| `0x41` | DCC | output | Вкл/выкл канал (тест Wiring) |
| `0x42` | DCC | любой | Переход в OTA mode |
| `0x43` | любой | DCC | ACK/NACK |

### 3.6 CONFIG (при старте)

| msg_type | Описание |
|----------|----------|
| `0x50` | DISCOVER — узел объявляет Type, FW, serial |
| `0x51` | ASSIGN — DCC назначает Node ID (если динамика) |
| `0x52` | CONFIG_OK / CONFIG_FAIL |

Gen1: Node ID **фиксированы** прошивкой; DISCOVER для мониторинга и Web UI.

## 4. SPI — DCPI (DriveCore Peripheral Interface)

Logic (STM32) ↔ Radio (ESP32). **Не JSON.**

### 4.1 Кадр

| Offset | Size | Поле |
|--------|------|------|
| 0 | 2 | Magic `0xDC 0x01` |
| 2 | 1 | `proto_ver` = `0x01` |
| 3 | 1 | `flags` — bit0=req, bit1=resp |
| 4 | 2 | `command` |
| 6 | 2 | `length` |
| 8 | n | `payload` |
| 8+n | 2 | CRC-16/CCITT |

SPI: **20 MHz**, Mode 0, STM32 = master. ESP32 сигнализирует `INT` при готовности.

### 4.2 Команды SPI

| Code | Имя | Направление | Описание |
|------|-----|-------------|----------|
| `0x0001` | STATE_PUSH | STM32→ESP32 | Полное состояние (50 ms) |
| `0x0002` | EVENT_PUSH | STM32→ESP32 | Запись журнала |
| `0x0010` | CONFIG_LOAD | ESP32→STM32 | Бинарный конфиг |
| `0x0011` | CONFIG_APPLY_ACK | STM32→ESP32 | OK / error code |
| `0x0020` | OUTPUT_TEST | ESP32→STM32 | Тест канала (Wiring) |
| `0x0030` | OTA_BEGIN | ESP32→STM32 | Начало прошивки STM32 |
| `0x0031` | OTA_CHUNK | ESP32→STM32 | Блок прошивки |
| `0x00FF` | PING/PONG | оба | Проверка связи |

`STATE_PUSH` payload = снимок VCM + все каналы + ECU cache (бинарная структура v0.1, см. `agents_stuff/dcpi_structs_v0.1.md`).

## 5. REST API (ESP32 → клиент)

Base: `http://192.168.4.1/api/v1/`

| Method | Path | Описание |
|--------|------|----------|
| GET | `/status` | Версии, uptime, режим |
| GET | `/telemetry` | Снимок (REST fallback) |
| GET | `/outputs` | Все каналы |
| GET | `/outputs/{id}` | Один канал |
| POST | `/outputs/{id}` | `{"state":"on"}` — только Service mode |
| GET | `/config` | YAML как JSON |
| PUT | `/config` | Загрузка конфига |
| POST | `/config/apply` | YAML → validate → SPI → STM32 |
| GET | `/events` | Журнал |
| POST | `/ota/esp` | OTA ESP32 |
| POST | `/ota/stm32` | OTA STM32 |

## 6. WebSocket

`ws://192.168.4.1/ws/telemetry` — push **20 Hz**, JSON:

```json
{
  "ts": 1719876543210,
  "mode": "ENGINE_RUN",
  "battery": 13.82,
  "rpm": 4120,
  "outputs": {
    "fuel_pump": {"state": "ON", "a": 9.1, "fault": null}
  }
}
```

ESP32 собирает JSON из `STATE_PUSH` — STM32 JSON не формирует.

## 7. OTA

| Цель | Путь | Примечание |
|------|------|------------|
| ESP32 | HTTP upload → esp_ota | Автономно |
| STM32 | ESP32 OTA_BEGIN/CHUNK → SPI | Bootloader на STM32 |
| Recovery | USB-C + SWD | Аварийное восстановление |

## 8. Обнаружение узлов при старте

1. DCC выходит в RUN, шлёт HEARTBEAT.
2. Узлы отвечают HEARTBEAT + DISCOVER в течение 2 с.
3. DCC помечает узел `PRESENT` / `LOST`.
4. Button Box заменён → тот же Node ID, DISCOVER с новым serial → запись в журнал.

## 9. Версионирование

| Поле | Правило |
|------|---------|
| `proto_ver` | Инкремент при несовместимых изменениях |
| `msg_type` | Новые типы добавляются, старые не переиспользуются |
| CAN ID layout | Фиксирован в v0.1 |

## 10. Статус реализации

- [x] Архитектура и таблицы v0.1
- [ ] `.dcmsg` / codegen (будущее)
- [ ] Референсная реализация в `firmware/shared`
- [ ] CAN симулятор в `tools/can_sim`

## Связанные документы

- [001_System_Architecture.md](001_System_Architecture.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
- [006_Web_Interface.md](006_Web_Interface.md)
- [agents_stuff/dcpi_structs_v0.1.md](../agents_stuff/dcpi_structs_v0.1.md)
