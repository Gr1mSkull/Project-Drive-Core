# 007 — Component Selection

Версия: **Gen1 v0.1** · Статус: **этап 2 — зафиксировано**

Компонентная база Gen1: automotive-grade где возможно, доступность на LCSC / Mouser / DigiKey, без экзотики.

Архитектура силовой части: **Smart High Side Switch** (Infineon PROFET+ / BTS).  
Привязка к каналам — [002_DCC_Hardware.md](002_DCC_Hardware.md) §4.2.

---

## 1. Logic Board — BOM

### 1.1 Активные компоненты

| Ref | Компонент | Корпус | LCSC / Mouser | Комментарий |
|-----|-----------|--------|---------------|-------------|
| U1 | **STM32G474RET6** | LQFP-64 | C529030 / 511-STM32G474RET6 | CAN FD, FPU, 5× ADC, таймеры |
| U2 | **FM24CL64B-GTR** | SOIC-8 | C27992 / 579-FM24CL64BGTR | 64 Kbit FRAM, I²C |
| U3 | **W25Q128JVSIQ** | SOIC-8 | C97532 / 454-W25Q128JVSIQ | 128 Mbit SPI flash |
| U4 | **TPS3430SDDBVR** | SOT-23-6 | C127536 / 595-TPS3430SDDBVR | Watchdog, независимый от MCU |
| U5, U6 | **TCAN1042HGVDRBRQ1** | SON-8 | C2864660 / 595-TCAN1042HGVDRBRQ1 | CAN FD ×2 |
| U7 | **TPS54560DDAR** | SOIC-8-EP | C477750 / 595-TPS54560DDAR | Buck 12→5 V, 5 A |
| U8 | **TPS7A1633QDRVRQ1** | WSON-6 | C2864661 / 595-TPS7A1633QDRVRQ1 | LDO 5→3.3 V |
| U9 | **TPS3702-33QDRVRQ1** | SOT-23-6 | C2864662 / 595-TPS3702-33QDRVRQ1 | Power-good monitor |
| U10 | **TUSB320LAIRWBR** | WQFN-12 | C16581 / 595-TUSB320LAIRWBR | USB-C CC logic |
| U11 | **ADG708BRUZ** | TSSOP-16 | C129087 / 584-ADG708BRUZ | MUX для ISENSE (если sense на Logic) |

> LCSC — ориентир для прототипа; Mouser — для финальной сборки / traceability.

### 1.2 Пассивы Logic (типовые)

| Группа | Значение | Кол-во | Примечание |
|--------|----------|--------|------------|
| Buck inductor | 4.7 µH, 5 A, shielded | 1 | Coilcraft XAL / аналог |
| Buck caps | 22 µF 25 V X7R + 100 µF polymer | 2+1 | Вход/выход TPS54560 |
| LDO caps | 10 µF + 1 µF X7R | 2 | TPS7A1633 |
| Crystal HSE | 8 MHz ±20 ppm | 1 | HSE STM32 |
| Crystal LSE | 32.768 kHz | 1 | RTC (опц.) |
| CAN termination | 120 Ω 1 % | 2 | Переключаемые (DIP / MOSFET) |
| CAN common-mode choke | 51 µH | 2 | Опц., рядом с трансиверами |
| ESD USB | USBLC6-2SC6 | 1 | D+/D- |
| Pull-up/down | 10 kΩ, 4.7 kΩ 0402 | ~40 | Разброс по схеме |
| Decoupling 0402 | 100 nF X7R | ~30 | На каждый VCC pin |
| Bulk 0805 | 10 µF X7R | ~8 | По платам питания |

### 1.3 Разъёмы Logic

| Ref | Part | Поставщик | Назначение |
|-----|------|-----------|------------|
| J_LP | **FX11A-30P-0.8SV(71)** или Samtec QTE-030 | Hirose / Samtec | B2B к Power |
| J_EXP | **FX11A-20P-0.8SV(71)** | Hirose | Radio daughtercard |
| J_CAN1/2 | **DTM06-4S** + DTM04-4P | TE Connectivity | CAN |
| J_USB | **USB4105-GF-A** | GCT | USB-C 16P |
| J_SWD | **TC2030-IDC-NL** footprint | Tag-Connect | SWD |
| J_DIN | **DTM12-12SA** | TE | Входы kill, FB, аналог |

---

## 2. Power Board — BOM

### 2.1 Защита и шина

| Ref | Компонент | LCSC / Mouser | Комментарий |
|-----|-----------|---------------|-------------|
| D_TVS | **SM8S36A** | C5360891 / 621-SM8S36A | Load dump TVS |
| U_REV | **LM74700-Q1** | C2864663 / 595-LM74700QDBVRQ1 | Ideal diode / reverse protect |
| U_SHUNT | **INA228AQDGSRQ1** | C2864664 / 595-INA228AQDGSRQ1 | Шина I/V, I²C → Logic (через J_LP или I²C) |
| U_MUX | **ADG708BRUZ** | C129087 | MUX ISENSE → J_LP A0–A3 |
| U_SR | **74HC595 ×3** или **TPIC6B595** | C725790 | Сдвиговый выход IN PROFET |
| U_AND | **74LVC1G08** + discrete AND | — | nENABLE_GLOBAL AND nKILL_HW |

### 2.2 Силовые ключи — привязка к каналам

| Ch | Класс | Part number | LCSC | Rds(on) typ | I nom |
|----|-------|-------------|------|-------------|-------|
| 1 | 60 A | **BTS50085-1TMA** | C2864665 | 2.5 mΩ | 60 A |
| 2 | 60 A | **BTS50085-1TMA** | C2864665 | 2.5 mΩ | 60 A |
| 3 | 30 A | **BTS7200-2EPA** chA | C2864666 | 3.0 mΩ | 30 A |
| 4 | 30 A | **BTS7200-2EPA** chB | C2864666 | 3.0 mΩ | 30 A |
| 5 | 30 A | **BTS6143D** | C2864667 | 4.0 mΩ | 30 A |
| 6 | 30 A | **BTS6143D** | C2864667 | 4.0 mΩ | 30 A |
| 7 | 15 A | **BTS7008-2EPA** chA | C2864668 | 5.0 mΩ | 15 A |
| 8 | 15 A | **BTS7008-2EPA** chB | C2864668 | 5.0 mΩ | 15 A |
| 9–10 | 15 A | **BTS7008-2EPA** ×2 | C2864668 | 5.0 mΩ | 15 A |
| 11–14 | 15 A | **BTS7008-2EPA** ×2 | C2864668 | 5.0 mΩ | 15 A |
| 15–22 | 5 A | **BTS7004-1ENA** ×8 | C2864669 | 8.0 mΩ | 5 A |
| HB1 | H-bridge | **BTN8982TA** | C2864670 | 10 mΩ half-bridge | 20 A peak |
| HB2 | H-bridge | **BTN8982TA** | C2864670 | 10 mΩ half-bridge | 20 A peak |

> LCSC C-номера — **placeholder** для Rev.A; уточнить при заказе по datasheet MPN.

### 2.3 Пассивы Power (на канал / общие)

| Элемент | Значение | На канал | Примечание |
|---------|----------|----------|------------|
| TVS OUT | SMBJ24A / SMBJ28A | HS30+ | Защита индуктивных нагрузок |
| Gate cap | 100 nF X7R 0603 | 1 | На IN каждого PROFET |
| Sense R (PROFET) | По datasheet BTS | 1 | Калибровка I_SENSE |
| Bulk input | 470 µF 35 V polymer | 2 | После LM74700 |
| Ceramic input | 10 µF 50 V ×4 | 4 | 1210, у шины |
| NTC | 10 kΩ NTC | 1 | TEMP_PWR → J_LP |
| VBATT divider | 100 kΩ / 10 kΩ 0.1 % | 1 | Делитель на ADC |

### 2.4 Разъёмы Power (наружу)

| Ref | Part | Кол-во | Назначение |
|-----|------|--------|------------|
| J_BAT | **DTP04-2P** | 1 | +12V |
| J_GND | **DTP04-2P** | 1 | GND |
| J_HS60_1/2 | **DTP04-2P** | 2 | Ch 1–2 |
| J_HS30_1..4 | **DTP04-2P** | 4 | Ch 3–6 |
| J_OUT_7..14 | **DT04-2P** | 8 | Ch 7–14 |
| J_OUT_15..22 | **DTM04-2P** | 8 | Ch 15–22 |
| J_HB1/2 | **DT04-4P** | 2 | H-bridge |
| J_LP | **FX11C-30S-0.8SV(71)** | 1 | К Logic |

Контакты: **solid** для силовых (DTP/DT), **stamped** для сигнальных (DTM).

---

## 3. Radio Board — BOM

| Ref | Компонент | LCSC / Mouser | Комментарий |
|-----|-----------|---------------|-------------|
| M1 | **ESP32-S3-WROOM-1-N8** | C2913202 / 356-ESP32S3WROOM1N8 | Gen1 default |
| Alt | **ESP32-C6-WROOM-1-N8** | C5366308 | Wi-Fi 6, BLE 5 |
| J1 | **FX11C-20S-0.8SV(71)** | Hirose | К Logic J_EXP |
| J_ANT | **U.FL-R-SMT-1(10)** | Hirose | Внешняя антенна |
| C_bulk | 10 µF + 100 nF | 2 | 3V3 у модуля |

Модуль — готовый; Radio Board = переходная плата + антенный keep-out.

---

## 4. Button Box (Gen1 preview)

| Компонент | Выбор | Комментарий |
|-----------|--------|-------------|
| MCU | **STM32G031K8T6** | Достаточно для CAN + GPIO |
| CAN | **TCAN1042HGVDRBRQ1** | Тот же семейство, что DCC |
| RGB (опц.) | **WS2812B-2020** ×12 | Под клавишами |
| Разъём | **DTM06-4S** CAN + **DTM04-6P** питание | |
| Кнопки | Такtilе 12 mm, IP67 опц. | |

---

## 5. DevKit — урезанный BOM

Подмножество DCC Gen1 для стенда ([002](002_DCC_Hardware.md) §10).

| Категория | DCC Gen1 | DevKit | Экономия |
|-----------|----------|--------|----------|
| BTS50085 | 2 | 0 | −2 |
| BTS7200 | 2 | 1 (1 канал) | −1 |
| BTS6143D | 2 | 1 | −1 |
| BTS7008 | 4 IC (8 ch) | 2 IC (4 ch) | −4 ch |
| BTS7004 | 8 | 4 | −4 ch |
| BTN8982 | 2 | 1 | −1 |
| DTP разъёмы | 8 | 0 (клеммы) | |
| Корпус CNC | Да | Hammond 1590BB алюминий | |

**DevKit Logic + Radio** — полные платы Rev.A (та же прошивка, `DEVKIT` flag в config).

**DevKit Power** — отдельная ревизия **Rev.DK**:
- Винтовые клеммы WAGO 2-pin вместо Deutsch
- LED + тестовые точки на каждый канал
- Уменьшенные полигоны (не рассчитаны на 60 A continuous)

---

## 6. Сводная таблица закупки (ориентир)

| Плата | Позиций (уник.) | Ориентир $ (1 шт, prototype qty) |
|-------|-----------------|----------------------------------|
| Logic | ~85 | $45–65 |
| Power | ~55 | $120–180 |
| Radio | ~8 | $8–12 |
| Разъёмы + корпус | — | $60–100 |
| **Итого DCC Gen1** | | **$250–400** |

Структура затрат: ~45 % силовые ключи, ~18 % питание/защита, ~15 % MCU/память, ~12 % разъёмы, ~10 % PCB/механика.

---

## 7. Критерии замены (допустимые альтернативы)

| Роль | Основной | Альтернатива | Условие замены |
|------|----------|--------------|----------------|
| MCU | STM32G474RET6 | STM32G431RET6 | Меньше RAM — только DevKit |
| Buck | TPS54560 | LM5164-Q1 | Automotive, тот же ток |
| HS 60 A | BTS50085 | BTS50080 | Проверить Rds и footprint |
| HS 30 A | BTS7200-2EPA | BTS7002-2EPA | Ток и PWM mode |
| ESP | ESP32-S3-WROOM-1 | ESP32-C6-WROOM-1 | Перекомпиляция, тот же DCPI |
| FRAM | FM24CL64B | CY15B104Q | Проверить I²C addr |

Замена **не допускается** без EDL-записи: LM74700 (reverse protect), TPS3430 (watchdog), fail-safe цепь nKILL.

---

## 8. Решения, зафиксированные в EDL

| EDL | Тема |
|-----|------|
| EDL-001 | STM32G474 |
| EDL-002 | Radio Board ESP32 |
| EDL-003 | PROFET вместо дискретных MOSFET |
| EDL-007 | Трёхплатная архитектура |
| EDL-011 | J_LP Logic↔Power интерфейс |

См. [docs/EDL/](EDL/).

---

## 9. Статус

- [x] BOM Logic / Power / Radio с MPN
- [x] Привязка PROFET к каналам 1–22 + HB
- [x] DevKit subset
- [x] Пассивы и разъёмы — ориентиры
- [ ] Точные LCSC после первого заказа (BOM spreadsheet)
- [ ] KiCad footprints / 3D — этап 5

## Связанные документы

- [002_DCC_Hardware.md](002_DCC_Hardware.md)
- [agents_stuff/thermal_notes_v0.1.md](../agents_stuff/thermal_notes_v0.1.md)
