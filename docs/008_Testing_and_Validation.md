# 008 — Testing and Validation

**Version:** Gen1 v0.1.3  
**Status:** этап 4 — strategy overview (WP-007 Accepted)  
**Work Package update:** WP-007 (Accepted 2026-07-20)

> **Test before track.** Ни одна новая функция не попадает в автомобиль без проверки на стенде.

## 1. Стратегия валидации

```
DevKit bring-up → Protocol → Power channels → Integration → DCC Gen1 → E30 vehicle
      │              │            │              │              │           │
   Phase A        Phase B       Phase C        Phase D        Phase E     Phase F
   Gate DK-A      Gate DK-B     Gate DK-C      Gate DK-D
```

| Правило | Описание |
|---------|----------|
| **DevKit first** | DCC Gen1 в машину — только после прохождения Phase A–D на DevKit |
| **No skip** | Новый канал / правило YAML → тест на стенде до трека |
| **Fail operational** | Отказ Service domain / планшета не должен останавливать силовые функции VCM |
| **Traceable** | Каждый прогон — запись + составной system baseline (ADR-015 / STD-REV-001) |

См. **EDL-014** (обязательный DevKit gate) — без изменений по смыслу.

### Normative DevKit detail (WP-007)

| Topic | Normative / controlled source |
|-------|-------------------------------|
| DevKit system requirements | [`docs/DevKit/DevKit_System_Requirements.md`](DevKit/DevKit_System_Requirements.md) |
| DevKit verification governance (`DK-GOV-*`) | [`docs/DevKit/DevKit_Verification_Governance.md`](DevKit/DevKit_Verification_Governance.md) |
| DevKit verification plan (Phase A–D / DK-A…DK-D) | [`docs/DevKit/DevKit_Verification_Plan.md`](DevKit/DevKit_Verification_Plan.md) |
| DevKit interfaces | [`docs/DevKit/DevKit_Interface_Matrix.md`](DevKit/DevKit_Interface_Matrix.md) |
| Gap / candidate audit | [`docs/DevKit/DevKit_Current_State_Gap_Assessment.md`](DevKit/DevKit_Current_State_Gap_Assessment.md) |
| Document index | [`docs/DevKit/README.md`](DevKit/README.md) |

`docs/008` is the **system-level validation strategy** and navigation aid. It is **not** the competing normative source for detailed DevKit requirements or Phase A–D pass criteria after WP-007.

## 2. DriveCore DevKit — overview (non-normative summary)

Лабораторная платформа **до** DCC Gen1. Та же **архитектурная семья** Logic + Power + Radio (EDL-007).

```text
The DevKit is a controlled verification platform.
It is not a reduced production DCC and not a substitute for DCC Gen1 acceptance.
```

### 2.1 Composition intent (classification)

| Board | Legacy/candidate statement in prior docs | WP-007 classification |
|-------|------------------------------------------|------------------------|
| Logic | “Identical to DCC Gen1 Rev.A” (`docs/008` historical) | **CANDIDATE / ADR-DK-001** — do not assume same physical board without decision |
| Radio | “Identical to DCC Gen1 Rev.A” | **CANDIDATE / ADR-DK-002** |
| Power | Rev.DK reduced channels, lab terminals, indicators | **CANDIDATE DESIGN** pending ADR-DK-004/005/012 |

Exact channel counts, MPNs, enclosure models, connector families, lamp wattages, and “same binary” claims from historical `docs/008` / `docs/007` tables are **not** normative requirements. See gap assessment and threshold register (`TBD-DK-*`).

### 2.2 Configuration intent

Profile scaffold: `config/vehicles/devkit.yaml` (**PARTIAL** — schema field `hardware.profile` not defined in `docs/005`).  
Firmware equivalence rules: **ADR-DK-003**.

## 3. Инженерный стенд (overview)

Bench topology remains: lab PSU → DevKit/DCC → loads; CAN to ECU sim / Button Box sim; optional Tablet.

Detailed equipment models are **not** mandated here. Capability needs are in DevKit requirements (categories C/J) and verification plan equipment fields.

Safety intent (non-exhaustive): controlled first power; hardware kill path; supervised loaded tests; fire extinguisher available. Measurable limits use `TBD-DK-*` until approved.

## 4. Уровни тестирования

| Уровень | Что | Где | Автоматизация |
|---------|-----|-----|---------------|
| **Unit** | CRC, state machine, rules parser | Host (`tools/`) | pytest / CTest |
| **Module** | Один канал, CAN node, SPI DCPI | DevKit | `tools/can_sim` |
| **Integration** | DCC + ECU sim + Button Box | Стенд | Скрипты + ручной |
| **System** | DCC Gen1 полный, все каналы | Стенд | Phase E |
| **Vehicle** | E30 | Гараж / трек | Phase F |

## 5. Phase A–D — DevKit gates (navigation)

Detailed atomic cases, measurable pass criteria, abort criteria, baseline requirements, and gate exit rules:

**→ [`docs/DevKit/DevKit_Verification_Plan.md`](DevKit/DevKit_Verification_Plan.md)**

| Gate | Phase | Focus |
|------|-------|-------|
| DK-A | A | Bring-up and safety |
| DK-B | B | Communication and service |
| DK-C | C | Representative power capability |
| DK-D | D | Integration and fail-operational behaviour |

Historical Phase A–D procedure tables previously embedded in this file are **superseded as normative detail** by the DevKit verification plan. Git history retains the prior text. Candidate numeric values remain inputs to the threshold register, not automatic PASS criteria.

## 6. Phase E — DCC Gen1 acceptance (overview)

**Цель:** полная плата для E30.

Предусловие: Gates DK-A…DK-D satisfied on DevKit per DevKit verification plan and EDL-014.  
“Same firmware” precondition remains subject to **ADR-DK-003**.

| # | Критерий (overview) | Notes |
|---|---------------------|-------|
| E1 | Full channel population tested | Not a DevKit substitute |
| E2 | High-current class / EHPS class verification | May require load bank; candidates in legacy notes are **NOT** frozen here |
| E3 | Production connector continuity | Production interfaces |
| E4 | Enclosure inspection as required | Production packaging |
| E5 | Thermal run for production population | Gen1 scope |
| E6 | J_LP / BOARD_ID Power identification | Encoding TBD-DK-020 |
| E7 | Full vehicle profile apply | e.g. `e30_gen1` |

**Gate:** E1, E2, E7 — обязательны перед Phase F (EDL-014).

Detailed Gen1 acceptance procedures remain to be formalized in a future Gen1 verification plan WP; values above are overview only.

## 7. Phase F — E30 vehicle (overview)

Pre-install, first power, and track-readiness checklists remain vehicle-level. They do **not** replace DevKit or Phase E evidence.

Wiring mode shall not be used as a track operating mode. Kill/contactor compliance remains regulation-driven (**TBD** in SRS where noted).

## 8. Fail operational — strategy

Loss of Service domain, Wi-Fi, or Tablet shall not stop Real-Time power execution required by active VCM rules (constitution / DevKit requirements).  
Executable cases: DevKit verification plan Phase D (e.g. service restart, tablet disconnect, CAN node loss).

## 9. Testability of firmware modules (future)

When firmware trees exist, modules (Power Manager, VCM, CAN, Rules, Config, DCPI) shall support host or bench testability. This section does not create firmware layout.

## 10. Регрессия перед релизом (strategy)

| Триггер | Минимальный набор (strategy) |
|---------|------------------------------|
| Изменение RT firmware | Re-enter relevant DK-A/B/D cases |
| Изменение Service firmware | Re-enter relevant DK-B/D cases |
| Изменение YAML schema | Config apply/reject cases |
| Изменение Power PCB | DK-C coverage for represented classes |
| Перед треком | Phase F checklist + prior gates |

## 11. Инструменты (план)

| Инструмент | Путь | Назначение | Status |
|------------|------|------------|--------|
| can_sim | `tools/can_sim` | ECU + Button Box эмуляция | PARTIAL scaffold |
| config_compiler | `tools/config_compiler` | YAML → DCFG | PARTIAL |
| bench_script | `tools/bench/` | Автоматизация | NOT PRESENT |

## 12. Статус (WP-007)

- [x] System validation strategy Phase A–F
- [x] EDL-014 gate intent preserved
- [x] DevKit requirements + verification plan (**Accepted** structure)
- [x] Traceability import of `REQ-DCC-V-DK-*` (baseline Accepted; evidence NOT VERIFIED)
- [x] Architecture Review acceptance of DevKit baseline (2026-07-20)
- [ ] DevKit hardware design approved
- [ ] First physical Phase A execution / VE records

## Связанные документы

- [DevKit/README.md](DevKit/README.md) — DevKit document set
- [002_DCC_Hardware.md](002_DCC_Hardware.md) — hardware (incl. DevKit preview)
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
- [006_Web_Interface.md](006_Web_Interface.md)
- [009_Roadmap.md](009_Roadmap.md)
- [ADR-015](ADR/ADR-015-platform-revision-identity.md) / [STD-REV-001](standards/REVISION_IDENTITY_STANDARD.md)
- [EDL](EDL/README.md) — EDL-014
- [agents_stuff/devkit_bench_v0.1.md](../agents_stuff/devkit_bench_v0.1.md) — operational notes (non-normative)

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-07-12 | Initial Phase A–F DevKit-oriented procedures |
| 0.1.1 | 2026-07-19 | WP-007 — strategy/navigation; detailed A–D normative cases moved to DevKit verification plan |
| 0.1.2 | 2026-07-19 | WP-007-R1 — link verification governance document |
| 0.1.3 | 2026-07-20 | WP-007 Architecture Review ACCEPTED — status checklist updated |
