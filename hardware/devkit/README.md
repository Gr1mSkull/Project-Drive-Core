# DriveCore DevKit — hardware

Rev.DK: урезанная Power Board + Logic Rev.A + Radio Rev.A.

## Статус

🔲 KiCad проект — scaffold. Схема и разводка после review документации 002/007/008.

## Структура (план)

```
hardware/devkit/
├── README.md                 # этот файл
├── devkit.kicad_pro          # корневой проект (hierarchical)
├── logic/                    # → reuse dcc/logic Rev.A
├── power/
│   ├── devkit.kicad_sch      # Rev.DK — 10 HS + 1 HB
│   └── devkit.kicad_pcb
└── radio/                    # → reuse dcc/radio Rev.A
```

## Power Rev.DK — отличия от DCC Gen1

| Параметр | DevKit Rev.DK |
|----------|----------------|
| HS60 | нет |
| HS30 | 2 (BTS7200 ×1 + BTS6143D ×1) |
| HS15 | 4 (BTS7008 ×2) |
| HS05 | 4 (BTS7004 ×4) |
| H-bridge | 1 (BTN8982TA) |
| Выходы | WAGO клеммы |
| Корпус | Hammond 1590BB |

## Каналы → разъёмы (план)

| Ch | Ref | Клемма |
|----|-----|--------|
| 1 | FAN1 | OUT1 |
| 2 | PUMP | OUT2 |
| 3–6 | TEST | OUT3–6 |
| 7–8 | LED | OUT7–8 |
| HB1 | MOTOR | M1A/M1B |

## Следующие шаги

1. Импорт footprint Logic/Radio из `hardware/dcc/` (когда появится)
2. Схема Power Rev.DK по `docs/007` BOM
3. DRC: 6 oz силовые зоны не требуются (max 30 A)
4. ORDER PCB + стенд Phase A (`docs/008`)

## Ссылки

- `docs/002_DCC_Hardware.md` §10
- `docs/008_Testing_and_Validation.md` §2
- `config/vehicles/devkit.yaml`
