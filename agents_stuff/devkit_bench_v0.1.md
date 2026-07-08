# DevKit bench cheat sheet v0.1

Конспект. Официально: `docs/008_Testing_and_Validation.md`.

## DevKit channels

| Ch | Class | Bench load |
|----|-------|------------|
| 1 | 30A | 55W lamp / fan |
| 2 | 30A | 10A resistor bank |
| 3–6 | 15A | 21W lamps |
| 7–10 | 5A | LED strip |
| HB1 | H-bridge | 12V motor |

## Phase order

```
A bring-up → B protocol → C power → D integration → E DCC Gen1 → F E30
```

## Critical gates (must PASS)

- A7 Kill hardware
- A5 SPI STATE_PUSH
- B7 CONFIG_LOAD
- D8 ESP32 reboot (fail operational)
- E1 All 22 ch (DCC Gen1 only)
- E2 EHPS 50A 10min

## Bench wiring

```
PSU 13.8V → DevKit BAT+
Loads → OUTn+
CAN: DevKit ↔ can_sim (or USB-CAN sniffer)
Tablet → Wi-Fi DriveCore-XXXX
```

## Quick REST smoke test

```bash
curl http://192.168.4.1/api/v1/status
curl -X POST http://192.168.4.1/api/v1/auth/login -d '{"pin":"123456"}'
# use token for /outputs tests
```

## Safety

- Kill switch on bench always reachable
- No Wiring mode in vehicle
- Max 30A continuous on DevKit Power Rev.DK
