# can_sim

Эмуляция DCP CAN кадров для стенда (Phase B в `docs/008`).

## Запуск

```bash
# ECU telemetry 5 s @ 20 ms
python tools/can_sim/can_sim.py ecu --duration 5

# С ростом RPM и нагревом
python tools/can_sim/can_sim.py ecu --rpm 800 --rpm-ramp 50 --coolant 95 --duration 10

# Heartbeat DCC
python tools/can_sim/can_sim.py heartbeat --device dcc
```

Вывод — hex строки для sniffer / ручной проверки. SocketCAN backend — TBD.

## Формат

См. `tools/can_sim/dcp.py` и `docs/004_Communication_Protocol.md`.
