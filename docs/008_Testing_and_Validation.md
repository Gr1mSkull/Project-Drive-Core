# 008 — Testing and Validation

Версия: **Gen1 v0.1** · Статус: **этап 4 — зафиксировано**

> **Test before track.** Ни одна новая функция не попадает в автомобиль без проверки на стенде.

## 1. Стратегия валидации

```
DevKit bring-up → Protocol → Power channels → Integration → DCC Gen1 → E30 vehicle
      │              │            │              │              │           │
   Phase A        Phase B       Phase C        Phase D        Phase E     Phase F
```

| Правило | Описание |
|---------|----------|
| **DevKit first** | DCC Gen1 в машину — только после прохождения Phase A–D на DevKit |
| **No skip** | Новый канал / правило YAML → тест на стенде до трека |
| **Fail operational** | Отказ ESP32 / планшета не должен останавливать силовые функции VCM |
| **Traceable** | Каждый прогон — запись в журнале + составной system baseline |

См. EDL-014 (обязательный DevKit gate).

**Revision identity (normative):** every DevKit, bench, qualification, or vehicle-test record shall identify the tested system per [`docs/standards/REVISION_IDENTITY_STANDARD.md`](standards/REVISION_IDENTITY_STANDARD.md) (ADR-CR002-001 / ADR-015). Do not certify verification against unidentified firmware, hardware, protocol, or configuration. Incomplete identity → certification remains `NOT VERIFIED` or `PARTIAL`.

## 2. DriveCore DevKit — спецификация

Лабораторная платформа **до** DCC Gen1. Та же архитектура Logic + Power Rev.DK + Radio.

### 2.1 Состав

| Плата | Rev | Отличие от DCC Gen1 |
|-------|-----|---------------------|
| Logic | A | **Идентична** DCC Gen1 |
| Power | **DK** | Урезанные каналы, клеммы, LED |
| Radio | A | **Идентична** DCC Gen1 |

### 2.2 Каналы DevKit

| Ch | Класс | Микросхема | Нагрузка на стенде | LED |
|----|-------|------------|-------------------|-----|
| 1 | 30 A | BTS7200 chA | Вентилятор 12 V / лампа 55 W | ✓ |
| 2 | 30 A | BTS6143D | Резистивная нагрузка 10 A | ✓ |
| 3–6 | 15 A | BTS7008 ×2 | Лампы 21 W ×4 | ✓ |
| 7–10 | 5 A | BTS7004 ×4 | LED лента / малые лампы | ✓ |
| HB1 | H-bridge | BTN8982TA | Моторчик 12 V | ✓ |

**Нет HS60** — EHPS тестируется только на DCC Gen1 или внешнем load bank.

### 2.3 Разъёмы и корпус

| Элемент | DevKit |
|---------|--------|
| Выходы | WAGO 2-pin клеммы |
| Питание вход | Винтовая клемма + предохранитель 30 A |
| CAN | DTM06-4S |
| USB-C | Прошивка / питание Logic |
| Корпус | Hammond 1590BB (алюминий) |
| Кнопки на плате | BOOT, USER, KILL test |

### 2.4 Конфигурация DevKit

Профиль: `config/vehicles/devkit.yaml` (TBD, этап 5). Флаг `hardware.profile: devkit` — меньше каналов, те же VCM modes.

Прошивка: **та же** binary, что DCC Gen1; отличие только в config blob.

## 3. Инженерный стенд

### 3.1 Схема подключения

```text
┌─────────────┐     ┌──────────────────────────────────────┐
│ БП 13.8 V   │────►│ DriveCore DevKit / DCC Gen1          │
│ 0–30 A      │     │  OUT1 → нагрузка + амперметр шунт    │
└─────────────┘     │  OUT2 → ...                          │
                    │  CAN ──┬── USB-CAN (опц.)            │
                    └────────┼─────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐  ┌─────┴─────┐  ┌────┴────┐
        │ can_sim   │  │ Button    │  │ Планшет │
        │ ECU emu   │  │ Box mock  │  │ Web UI  │
        └───────────┘  └───────────┘  └─────────┘
```

### 3.2 Оборудование стенда

| Оборудование | Назначение |
|--------------|------------|
| БП 13.8 V, 30 A+ | Питание стенда |
| Мультиметр | Напряжение, continuity |
| Клещи / шунт | Ток каналов |
| Осциллограф | PWM, CAN, inrush |
| USB-CAN adapter | Sniff DCP (опц.) |
| Резистивные нагрузки | 10 A, 20 A банки |
| Лампы 12 V 55 W | Имитация вентилятора |
| Моторчик 12 V | H-bridge stall test |

### 3.3 Безопасность стенда

| Правило | Действие |
|---------|----------|
| Первый power-on | Без нагрузок, только LED |
| Kill switch | Физическая кнопка на стенде, дублирует KILL_IN |
| HS тесты | Не более 30 A continuous на DevKit |
| Пожар | Огнетушитель рядом; не оставлять нагрузки без присмотра |
| Wiring mode | Только на стенде, с `X-DriveCore-Confirm` |

## 4. Уровни тестирования

| Уровень | Что | Где | Автоматизация |
|---------|-----|-----|---------------|
| **Unit** | CRC, state machine, rules parser | Host (`tools/`) | pytest / CTest |
| **Module** | Один канал, CAN node, SPI DCPI | DevKit | `tools/can_sim` |
| **Integration** | DCC + ECU sim + Button Box | Стенд | Скрипты + ручной |
| **System** | DCC Gen1 полный, все каналы | Стенд | Чеклист |
| **Vehicle** | E30 | Гараж / трек | Чеклист + лог |

## 5. Phase A — DevKit bring-up

**Цель:** плата включается, прошивается, базовая диагностика.

| # | Тест | Процедура | Pass |
|---|------|-----------|------|
| A1 | Power input | 13.8 V на вход, измерить 5 V / 3.3 V на Logic | ±5 % |
| A2 | SWD flash | Прошить STM32 через Tag-Connect | OK |
| A3 | USB enumerate | USB-C → COM port / DFU | Виден в ОС |
| A4 | ESP32 flash | Прошить Radio, ping DCPI PING | PONG |
| A5 | SPI link | STATE_PUSH 50 ms на логике | ESP32 получает |
| A6 | Watchdog | Зависание MCU → reset / safe OFF | Выходы OFF < 200 ms |
| A7 | Kill hardware | KILL_IN active → все OFF | Немедленно |
| A8 | LED outputs | Включить ch 7 через Wiring | LED + ток |

**Критичные:** A2, A5, A7 — блокируют Phase B без PASS.

## 6. Phase B — Protocol

**Цель:** DCP CAN, DCPI, REST/WS работают по спеке.

### 6.1 CAN

| # | Тест | Pass |
|---|------|------|
| B1 | DCC HEARTBEAT 0x010 @ 100 ms | Sniffer видит, seq++ |
| B2 | ECU sim ENGINE_TELEM 0x120 @ 20 ms | DCC cache rpm обновляется |
| B3 | Node LOST | Остановить sim > 500 ms | `ecu_status=LOST` в STATE_PUSH |
| B4 | Button Box EVENT | can_sim шлёт control_id | DCC rules реагируют |
| B5 | Termination | 2× 120 Ω, waveform clean | Осциллограф OK |

### 6.2 DCPI (SPI)

| # | Тест | Pass |
|---|------|------|
| B6 | STATE_PUSH 50 ms | 100 байт, CRC OK | |
| B7 | CONFIG_LOAD | Загрузить devkit.yaml binary | CONFIG_APPLY_ACK OK |
| B8 | OUTPUT_TEST | Wiring через SPI | Канал переключается |
| B9 | EVENT_PUSH | Сгенерировать fault | Событие в Web UI logger |

### 6.3 REST / WebSocket

| # | Тест | Pass |
|---|------|------|
| B10 | GET /status | JSON с версиями | 200 |
| B11 | WS telemetry | 20 Hz ≥ 15 s без drop | |
| B12 | PIN auth | POST /auth/login | token valid |
| B13 | POST /outputs без token | | 401 |
| B14 | OTA ESP32 | Upload test .bin | Reboot OK |

## 7. Phase C — Power channels

**Цель:** каждый тип выхода — защита и диагностика.

Для **каждого** канала DevKit (1–10, HB1):

| # | Сценарий | Ожидание |
|---|----------|----------|
| C1 | Normal ON/OFF | Ток в пределах, state ON/OFF в CAN |
| C2 | Overcurrent | Искусственный short → OFF + fault OVERCURRENT |
| C3 | Open load | Обрыв → fault OPEN_LOAD (если детектируется) |
| C4 | Undervoltage | БП < 10.5 V → lockout или fault UNDERVOLT |
| C5 | Retry | Inrush fan sim → RETRY ≤ 3 → ON или FAULT |
| C6 | PWM (ch 1, 2) | Duty 0/50/100 %, осциллограф |
| C7 | Thermal (опц.) | Длительный 15 A → derating / log |

### H-bridge HB1

| # | Сценарий | Ожидание |
|---|----------|----------|
| C8 | Forward / reverse | Мотор вращается |
| C9 | Stall | Ток limit, fault, OFF |
| C10 | Coast / brake | По конфигу |

### Запись результатов

Шаблон: `agents_stuff/devkit_test_log_TEMPLATE.md` (создать при первом прогоне) или таблица:

```text
Ch | C1 | C2 | C3 | C4 | C5 | C6 | Date | FW ver
 1 | OK | OK | —  | OK | OK | OK | ...  | 1.0.0
```

## 8. Phase D — Integration

**Цель:** система как на машине, но на стенде.

| # | Сценарий | Шаги | Pass |
|---|----------|------|------|
| D1 | VCM OFF → MASTER_ON | Kill release, контактор FB | Режим переходит |
| D2 | IGNITION → PRIME | Ключ / button | Fuel pump prime 3 s |
| D3 | READY → ENGINE_RUN | ECU sim rpm > 500 | ECU power ON |
| D4 | Cooling rules | CLT sim 95 °C | fan1 ON |
| D5 | Cooling stage 2 | CLT 102 °C | fan1 + fan2 |
| D6 | Low oil rule | oil < 1.2 bar, rpm > 2500 | warning в WS |
| D7 | Button override | long_press fan_override | fan1 + fan2 |
| D8 | ESP32 reboot | Перезагрузка ESP32 | STM32 продолжает, авто OK |
| D9 | Tablet disconnect | Закрыть браузер | Нагрузки без изменений |
| D10 | Config hot reload | PUT yaml → apply | Новые rules без reflash STM32 |

## 9. Phase E — DCC Gen1 acceptance

**Цель:** полная плата для E30, все 22 канала + 2 HB.

Предусловие: Phase A–D PASS на DevKit с **той же** прошивкой.

| # | Критерий | Метод |
|---|----------|-------|
| E1 | Все 22 ch + 2 HB протестированы | Phase C на каждый |
| E2 | HS60 Ch1 EHPS load bank | 50 A, 10 min, T_pwr < 85 °C |
| E3 | Deutsch разъёмы | Continuity жгут ↔ плата |
| E4 | IP54 корпус | Визуальный осмотр, крышки |
| E5 | Тепловой прогон RACE sim | EHPS + 2 fan + pump, 30 min |
| E6 | J_LP swap test | Power Rev.A идентифицируется BOARD_ID |
| E7 | Полный e30_gen1.yaml | Загружен и apply OK |

**Gate:** E1, E2, E7 — обязательны перед Phase F.

## 10. Phase F — E30 vehicle

**Цель:** первый выезд / трек.

### 10.1 Pre-install (гараж)

| # | Проверка |
|---|----------|
| F1 | Жгуты промаркированы по config outputs |
| F2 | Контактор массы + kill по регламенту |
| F3 | Предохранители / сечения кабеля по току |
| F4 | CAN: DCC — ECU — Button Box, терминаторы |
| F5 | DCC крепление, термоконтакт с корпусом |

### 10.2 First power (машина)

| # | Шаг |
|---|-----|
| F6 | Только MASTER_ON, без ENGINE_RUN — проверить габариты/салон |
| F7 | Wiring mode **выключен** в машине |
| F8 | PRIME — слушать fuel pump |
| F9 | ENGINE_RUN — ECU, вентиляторы по temp |
| F10 | Полный лог 30 min idle — без fault |

### 10.3 Track readiness

| # | Критерий |
|---|----------|
| F11 | RACE mode 20 min на стенде/roll test |
| F12 | COOL_DOWN после остановки — вентиляторы работают |
| F13 | Журнал событий без критических error |
| F14 | Запасной план: откат к штатной проводке документирован |

## 11. Fail operational — обязательные тесты

| Отказ | Тест | Ожидание |
|-------|------|----------|
| ESP32 hang | Отключить питание Radio | STM32 + силовые OK |
| Wi-Fi jam | Помеха 2.4 GHz | Авто работает |
| Tablet off | — | VCM по кнопкам / rules |
| ECU CAN lost | Отключить ECU | DCC не переходит в ENGINE_RUN без rpm |
| STM32 reset | Watchdog | Safe OFF → recovery по VCM |

## 12. Прошивка: модули для тестируемости

| Модуль | Тестируемость |
|--------|---------------|
| Power Manager | Mock PROFET, inject fault |
| VCM | Unit: transitions table |
| CAN Manager | can_sim loopback |
| Rules engine | YAML fixtures |
| Config Manager | Round-trip binary |
| DCPI / Comm | SPI loopback на DevKit |

Каждый модуль — отдельный каталог в `firmware/dcc/logic/App/` с unit tests на host где возможно.

## 13. Регрессия перед релизом

| Триггер | Минимальный набор |
|---------|-------------------|
| Изменение прошивки STM32 | A5, A7, B1–B9, D1–D4 |
| Изменение ESP32 | B10–B14, D8 |
| Изменение YAML schema | B7, D10 |
| Изменение Power PCB | Phase C полный |
| Перед треком | Phase F чеклист |

## 14. Инструменты (план)

| Инструмент | Путь | Назначение |
|------------|------|------------|
| can_sim | `tools/can_sim` | ECU + Button Box эмуляция |
| config_compiler | `tools/config_compiler` | YAML → binary |
| bench_script | `tools/bench/` | Автоматизация REST тестов (TBD) |

## 15. Статус

- [x] DevKit spec, фазы A–F
- [x] Процедуры каналов, protocol, integration
- [x] Acceptance criteria DCC Gen1 + E30
- [x] Fail operational matrix
- [ ] `config/vehicles/devkit.yaml`
- [ ] `tools/can_sim` реализация
- [ ] Первый физический прогон Phase A

## Связанные документы

- [002_DCC_Hardware.md](002_DCC_Hardware.md) — DevKit preview
- [006_Web_Interface.md](006_Web_Interface.md) — Wiring / Service modes
- [003_ECU_Architecture.md](003_ECU_Architecture.md) — ECU sim
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [009_Roadmap.md](009_Roadmap.md)
- [agents_stuff/devkit_bench_v0.1.md](../agents_stuff/devkit_bench_v0.1.md)
