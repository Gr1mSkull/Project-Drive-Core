# 002 — DCC Hardware

Версия: **Gen1 v0.1** · Статус: **этап 2 — зафиксировано**

Аппаратная часть **DriveCore Controller (DCC)**.

## 1. Механическая сборка

```
         ┌──────────────────────────────────────┐
Корпус   │  Radio Board (ESP32, daughtercard)   │  ← J_EXP (на Logic)
алюминий │  ─────────────────────────────────  │
         │  Logic Board (STM32, CAN, USB)       │
         │  ═════════ J_LP ═══════════════════  │  board-to-board
         │  Power Board (PROFET, H-bridge)    │
         │  ─────────────────────────────────  │
         │  DTP/DT/DTM → жгуты автомобиля      │
         └──────────────────────────────────────┘
              ▲ термопрокладки → корпус = радиатор
```

| Параметр | Gen1 |
|----------|------|
| Корпус | Алюминий, ~200×150×55 mm (ориентир) |
| Крепление плат | M3 standoffs + термопрокладка 1.5 mm к крышке |
| IP | Целевой IP54 (гоночный салон / багажник) |
| Масса | ~1.2–1.8 kg (с жгутными разъёмами) |

## 2. Трёхплатная структура

| Плата | Rev | Меняется в Gen2? | Назначение |
|-------|-----|------------------|------------|
| **Logic** | A | Редко | MCU, CAN, память, USB, watchdog, входы |
| **Power** | A | **Да** | PROFET, H-bridge, силовые шины, TVS входа |
| **Radio** | A | Да | ESP32 модуль, Wi-Fi/BLE антенна |

Gen2 = новая Power Board Rev.B при Logic Rev.A.

## 3. Logic Board

### 3.1 Компоненты

См. [007_Component_Selection.md](007_Component_Selection.md).

### 3.2 Разъёмы Logic Board

| Ref | Тип | Назначение |
|-----|-----|------------|
| J_LP | B2B 30-pin | К Power Board |
| J_EXP | B2B 20-pin | Radio + будущие модули |
| J_CAN1 | DTM06-4S | CAN к ECU (шина) |
| J_CAN2 | DTM06-4S | CAN stub / резерв (Gen1: перемычка или второй отвод) |
| J_USB | USB-C 16P | Прошивка, отладка |
| J_SWD | Tag-Connect TC2030 | Отладка STM32 |
| J_DIN | DTM12 | Входы: kill, масса FB, стартер, аналог |
| J_PWR_LOGIC | От J_LP | 12V / 5V / 3.3V с Power (через DC-DC на Logic или питание с Power) |

**Питание Logic:** 5 V и 3.3 V генерируются **на Logic Board** (TPS54560 + TPS7A1633). Power Board подаёт только защищённый `+12V_SW` после контактора.

### 3.3 Входы Logic

| Сигнал | Тип | Примечание |
|--------|-----|------------|
| KILL_IN | Digital, pull-up | Аппаратный, активный LOW |
| MASTER_FB | Digital | Контактор массы замкнут |
| START_IN | Digital | Опц., дубль с CAN |
| AIN1–4 | 0–5 V | Резерв датчиков |
| FREQ1–2 | Timer capture | Скорость, тахо |

## 4. Power Board

### 4.1 Топология силовой части

```
+12V_BAT (DTP) → TVS → LM74700 → +12V_SW (шина)
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
              HS60 ×2          HS30 ×4          HS15 ×8 + HS05 ×8
              (Ch 1–2)         (Ch 3–6)         (Ch 7–22)
                    │               │               │
              DTP выходы       DTP/DT выходы    DT/DTM выходы
```

Отдельная звёздная земля силовая → одна точка связи с Logic GND у J_LP.

### 4.2 Каналы — аппаратная карта

| Ch | Класс | Микросхема | E30 (config) | Разъём выхода |
|----|-------|------------|--------------|---------------|
| 1 | 60 A | BTS50085-1TMA | EHPS | DTP 2-pin |
| 2 | 60 A | BTS50085-1TMA | резерв | DTP 2-pin |
| 3 | 30 A | BTS7200-2EPA chA | Fan1 | DTP 2-pin |
| 4 | 30 A | BTS7200-2EPA chB | Fan2 | DTP 2-pin |
| 5 | 30 A | BTS6143D | Water pump | DT 2-pin |
| 6 | 30 A | BTS6143D | Fuel pump | DT 2-pin |
| 7 | 15 A | BTS7008-2EPA chA | ECU | DT 2-pin |
| 8–14 | 15 A | BTS7008-2EPA ×4 | Lights, heater, wipers | DT 2-pin |
| 15–22 | 5 A | BTS7004-1ENA ×8 | Parking, салон, резерв | DTM 2-pin |
| HB1 | H-bridge | BTN8982TA | Window FL | DT 4-pin |
| HB2 | H-bridge | BTN8982TA | Window FR | DT 4-pin |

Назначение функций — **только в YAML**, таблица выше — дефолтный BOM Gen1 Rev.A.

### 4.3 PWM (аппаратные линии)

4 канала с ШИМ (от таймеров STM32 через J_LP):

| PWM line | Ch | Нагрузка |
|----------|-----|----------|
| PWM0 | 3 | Fan1 |
| PWM1 | 4 | Fan2 |
| PWM2 | 5 | Water pump |
| PWM3 | 11 | Heater blower |

PROFET включается как high-side; PWM — по линии IN (или enable PROFET PWM mode где поддерживается BTS6143D).

### 4.4 Разъёмы Power Board (наружу)

| Ref | Тип | Назначение |
|-----|-----|------------|
| J_BAT | DTP 2-pin | +12V от контактора массы |
| J_GND | DTP 2-pin | Силовая земля |
| J_HS60_1/2 | DTP | Ch 1–2 |
| J_HS30_1..4 | DTP | Ch 3–6 |
| J_OUT_7..22 | DT / DTM | По таблице каналов |
| J_HB1/2 | DT 4-pin | H-bridge |
| J_LP | B2B 30-pin | К Logic |

## 5. Интерфейс Logic ↔ Power (J_LP)

**Протокол:** SPI (Logic = master) + аппаратные линии безопасности.  
См. DCPI в [004](004_Communication_Protocol.md); здесь — физический уровень.

### 5.1 Распиновка J_LP (30 pin)

| Pin | Сигнал | Направление | Описание |
|-----|--------|-------------|----------|
| 1 | +12V_SW | PWR→LOG | Питание DC-DC Logic (через PFET enable) |
| 2 | GND_PWR | PWR | Силовая земля |
| 3 | GND_LOG | LOG | Логическая земля (звезда у pin 2–3) |
| 4 | SPI_SCK | LOG→PWR | 10 MHz max |
| 5 | SPI_MOSI | LOG→PWR | |
| 6 | SPI_MISO | PWR→LOG | |
| 7 | SPI_CS_PWR | LOG→PWR | |
| 8 | nRESET_PWR | LOG→PWR | Сброс сдвиговых регистров / драйверов |
| 9 | nKILL_HW | IN | Kill switch (аппаратный, активный LOW) |
| 10 | nENABLE_GLOBAL | LOG→PWR | Разрешение всех ключей (AND с nKILL) |
| 11 | FAULT_N | PWR→LOG | Open-drain, OR всех fault |
| 12 | SYNC_1kHz | LOG→PWR | Опц. синхро для ADC |
| 13–16 | PWM0–3 | LOG→PWR | ШИМ каналы |
| 17–20 | ISENSE_A0–A3 | PWR→LOG | Мультиплексированные Current Sense |
| 21 | ISENSE_MUX_S0 | LOG→PWR | Выбор канала sense |
| 22 | ISENSE_MUX_S1 | LOG→PWR | |
| 23 | ISENSE_MUX_S2 | LOG→PWR | |
| 24 | VBATT_SENSE | PWR→LOG | Делитель напряжения АКБ |
| 25 | TEMP_PWR | PWR→LOG | NTC корпуса Power Board |
| 26–27 | BOARD_ID0–1 | PWR→LOG | Ревизия Power Board |
| 28–29 | Reserved | — | |
| 30 | SHIELD | — | Корпус |

### 5.2 Обмен Logic ↔ Power

| Кадр SPI (Power RX) | Содержание |
|---------------------|------------|
| `CMD_SET_OUTPUTS` | Битовая маска 22 ch on/off |
| `CMD_SET_PWM` | 4× duty 0–255 |
| `CMD_READ_DIAG` | Запрос fault bitmap + токи |

Power Board:
- 3× сдвиговый регистр / драйвер для 22 IN PROFET
- Аналоговый MUX (ADG708) + 4 sense линии на Logic ADC
- `nENABLE_GLOBAL` AND `nKILL_HW` → аппаратное отключение всех ключей

**Fail-safe:** при отсутствии SPI > 100 ms или `nENABLE_GLOBAL`=LOW → все выходы OFF.

## 6. Radio Board (J_EXP)

Дочерняя плата на Logic. Не проектируется с нуля — модуль ESP32.

### 6.1 Распиновка J_EXP (20 pin)

| Pin | Сигнал | Описание |
|-----|--------|----------|
| 1 | +3V3 | Питание модуля |
| 2 | GND | |
| 3 | SPI_SCK | Общая шина с Power или отдельный SPI2 |
| 4 | SPI_MOSI | |
| 5 | SPI_MISO | |
| 6 | SPI_CS_RADIO | |
| 7 | ESP_INT | Готовность данных → STM32 |
| 8 | ESP_RST | |
| 9 | ESP_GPIO0 | Boot |
| 10 | UART_TX | Опц. debug |
| 11 | UART_RX | |
| 12–13 | BOARD_ID | |
| 14 | +5V | Опц. для модуля |
| 15–20 | Reserved / GPIO | |

**SPI:** STM32 использует **SPI2** для Radio (отдельно от SPI1 Power). См. [004](004_Communication_Protocol.md) DCPI.

### 6.2 Модуль

- **Gen1 выбор:** ESP32-S3-WROOM-1-N8 (Wi-Fi + BLE, 8 MB flash)
- Альтернатива: ESP32-C6-WROOM-1 (Wi-Fi 6, BLE 5)
- Антенна: внешняя u.FL → площадка на корпусе (не внутри металлического экрана без окна)

## 7. Тепловая модель (E30)

### 7.1 Допущения

| Параметр | Значение |
|----------|----------|
| T_amb max | 45 °C (жаркий паддок) |
| T_junction max | 150 °C (PROFET) |
| Rth_junction-case | ~0.5 °C/W (типично BTS7200) |
| Rth_case-heatsink | 0.3 °C/W (термопрокладка + крепёж) |
| Rth_heatsink-ambient | 3 °C/W (корпус DCC, ориентир) |
| **Rth total** | **~3.8 °C/W** на канал |

### 7.2 Потери по каналам (непрерывный режим)

Оценка: **P = I² × Rds(on)**. Rds(on) — типичное при T=25 °C, ухудшение при нагреве учтено запасом ×1.3.

| Нагрузка | Ch | I cont | Rds | P loss | T rise | T_j est |
|--------|-----|--------|-----|--------|--------|---------|
| EHPS | 1 | 50 A | 2.5 mΩ | 6.3 W | +24 °C | ~69 °C |
| Fan1 | 3 | 25 A | 3 mΩ | 1.9 W | +7 °C | ~52 °C |
| Fan2 | 4 | 25 A | 3 mΩ | 1.9 W | +7 °C | ~52 °C |
| Pump | 5 | 15 A | 4 mΩ | 0.9 W | +3 °C | ~48 °C |
| Fuel | 6 | 12 A | 4 mΩ | 0.6 W | +2 °C | ~47 °C |
| ECU | 7 | 5 A | 5 mΩ | 0.13 W | <1 °C | ~46 °C |
| Lights | 9–10 | 12 A | 5 mΩ | 0.7 W | +3 °C | ~48 °C |

### 7.3 Худший сценарий (одновременно)

**RACE:** EHPS 50 A + Fan1 25 A + Fan2 25 A + Pump 15 A + ECU 5 A

| Зона Power Board | ΣP loss | Комментарий |
|------------------|---------|-------------|
| HS60 zone (Ch1) | 6.3 W | Критично — максимум меди, прямой контакт с корпусом |
| HS30 zone (Ch3–5) | 4.7 W | Разнести ключи по плате |
| Остальное | <2 W | Стандартное охлаждение |

**Суммарно на Power Board:** до **~15 W** непрерывно в худшем случае.

### 7.4 Требования к охлаждению

| Требование | Реализация |
|------------|------------|
| HS60 ключи | Прямой контакт с корпусом через термопрокладка 1.5 mm, 3 W/m·K |
| HS30 ключи | Полигон 70 µm меди min, переходные vias к нижнему слою |
| Корпус | Алюминий 4–5 mm стенка под Power Board |
| Derating | Firmware: при T_pwr > 85 °C → снижение duty вентиляторов/EHPS limit |
| Тепловой расчёт Rev.B | Уточнить после KiCad по реальным Rds и полигонам |

### 7.5 Пусковые токи (пиковые)

| Нагрузка | I peak | Длительность | Действие PROFET |
|----------|--------|--------------|---------------|
| EHPS | 80–100 A | <500 ms | Current limit + retry |
| Fan | 50–70 A | <300 ms | Inrush tolerant, retry 3× |
| Fuel pump | 20 A | <200 ms | Штатно |

PROFET ограничивает ток; пиковая мощность — кратковременная, не определяет постоянное охлаждение.

## 8. PCB — требования Gen1

| Плата | Слои | Медь | Примечание |
|-------|------|------|------------|
| Logic | 4 | 2 oz сигналы | Impedance CAN 120 Ω |
| Power | 4–6 | **6 oz** силовые шины | HS60: 8 oz или busbar |
| Radio | 2 | 1 oz | Keep-out под антенну |

## 9. Безопасность (аппаратура)

```
KILL switch ──► nKILL_HW (J_LP pin 9) ──► AND ──► PROFET enable chain
                      ▲
nENABLE_GLOBAL (MCU) ─┘

MCU завис / SPI timeout → nENABLE_GLOBAL = LOW → все OFF
```

Контактор массы — **вне** DCC, в силовой цепи АКБ. DCC не заменяет kill switch.

## 10. DriveCore DevKit (превью)

Урезанная Power Board + полная Logic + Radio:

| Параметр | DevKit | DCC Gen1 |
|----------|--------|----------|
| HS60 | 0 | 2 |
| HS30 | 2 | 4 |
| HS15 | 4 | 8 |
| HS05 | 4 | 8 |
| H-bridge | 1 | 2 |
| Нагрузки | Винтовые клеммы + LED | Deutsch |

Подробнее: [008_Testing_and_Validation.md](008_Testing_and_Validation.md).

## 11. Статус

- [x] Трёхплатная структура, разъёмы J_LP / J_EXP
- [x] Канальная карта + привязка микросхем
- [x] Тепловая модель v0.1 (E30)
- [ ] KiCad схема Rev.A
- [ ] Теплосимуляция по готовой плате

## Связанные документы

- [007_Component_Selection.md](007_Component_Selection.md)
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [001_System_Architecture.md](001_System_Architecture.md)
- [agents_stuff/thermal_notes_v0.1.md](../agents_stuff/thermal_notes_v0.1.md)
