# Thermal notes v0.1 — DCC Power Board (E30)

Конспект для агента. Официальная версия — `docs/002_DCC_Hardware.md` §7.

## Модель

```
T_junction = T_amb + P_loss × (Rth_j-c + Rth_c-hs + Rth_hs-amb)
```

| Параметр | Значение | Источник |
|----------|----------|----------|
| T_amb | 45 °C | Паддок, жара |
| T_j max PROFET | 150 °C | Datasheet BTS family |
| Rth_j-c | 0.5 °C/W | Типично BTS7200 |
| Rth_c-hs | 0.3 °C/W | Термопрокладка 1.5 mm, 3 W/m·K |
| Rth_hs-amb | 3.0 °C/W | Корпус DCC ~200×150×55 mm Al |
| **Σ Rth** | **3.8 °C/W** | На один ключ |

Запас на деградацию Rds: **×1.3** к расчёту P = I² × Rds.

## Worst case E30 — RACE mode

Одновременно ON:

| Ch | Load | I (A) | P (W) |
|----|------|-------|-------|
| 1 | EHPS | 50 | 6.3 |
| 3 | Fan1 | 25 | 1.9 |
| 4 | Fan2 | 25 | 1.9 |
| 5 | Pump | 15 | 0.9 |
| 7 | ECU | 5 | 0.13 |

**Σ ≈ 11 W** на ключевых зонах; с запасом **~15 W** на плату.

## Зоны Power Board

```
┌─────────────────────────────────────┐
│  HS60 zone (Ch1-2)  → корпус direct │  ← критично
│  ─────────────────────────────────  │
│  HS30 zone (Ch3-6)  → 70µm + vias   │
│  ─────────────────────────────────  │
│  HS15/05 (Ch7-22)   → standard poly │
│  HB (corner)        → отдельный радиатор опц. │
└─────────────────────────────────────┘
```

## Firmware derating (план)

| T_pwr (NTC) | Действие |
|-------------|----------|
| < 70 °C | Норма |
| 70–85 °C | Ограничить PWM duty вентиляторов max 80 % |
| 85–95 °C | EHPS limit 40 A equivalent |
| > 95 °C | Принудительный COOL_DOWN, отключение EHPS |

Реализация — этап firmware, правила в YAML `thermal:` (TBD).

## Inrush (не для steady-state cooling)

| Load | I_peak | t |
|------|--------|---|
| EHPS | 80–100 A | <500 ms |
| Fan | 50–70 A | <300 ms |
| Fuel pump | 20 A | <200 ms |

PROFET current limit + retry 3× — см. config `retry`.

## Следующие шаги

1. KiCad: полигоны 6 oz / 8 oz HS60
2. Sim (опц.): Fusion 360 / Icepak по готовой плате
3. Стенд: термопара на case tab BTS50085 при 50 A load

## Ссылки

- `docs/002_DCC_Hardware.md` §7
- `docs/007_Component_Selection.md` §2.2
- Infineon PROFET+ thermal application notes
