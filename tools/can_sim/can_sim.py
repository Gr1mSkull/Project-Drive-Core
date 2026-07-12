#!/usr/bin/env python3
"""DriveCore CAN bus simulator for bench tests (print or socketcan)."""

from __future__ import annotations

import argparse
import sys
import time

from dcp import DeviceType, ecu_cooling_request, ecu_engine_telemetry, heartbeat


def run_ecu(args: argparse.Namespace) -> int:
    seq = 0
    rpm = args.rpm
    clt = int(args.coolant * 10)
    end = time.time() + args.duration if args.duration > 0 else float("inf")

    while time.time() < end:
        seq = (seq + 1) & 0xFFFF
        if args.rpm_ramp > 0:
            rpm = min(args.rpm_max, rpm + args.rpm_ramp)

        frames = [
            heartbeat(DeviceType.ECU, seq),
            ecu_engine_telemetry(seq, rpm, clt, args.oil_kpa, engine_flags=1 if rpm > 500 else 0),
        ]
        if clt >= 920:
            frames.append(ecu_cooling_request(seq, 1 if clt < 1000 else 2))

        for frame in frames:
            print(frame.hex_line())

        time.sleep(args.period_ms / 1000.0)
    return 0


def run_heartbeat(args: argparse.Namespace) -> int:
    dt = DeviceType[args.device.upper()]
    seq = 0
    end = time.time() + args.duration if args.duration > 0 else float("inf")
    while time.time() < end:
        seq = (seq + 1) & 0xFFFF
        print(heartbeat(dt, seq).hex_line())
        time.sleep(0.1)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="DriveCore CAN simulator")
    sub = parser.add_subparsers(dest="mode", required=True)

    ecu = sub.add_parser("ecu", help="ECU telemetry + cooling request")
    ecu.add_argument("--period-ms", type=int, default=20)
    ecu.add_argument("--duration", type=float, default=5.0, help="0 = forever")
    ecu.add_argument("--rpm", type=int, default=800)
    ecu.add_argument("--rpm-ramp", type=int, default=0)
    ecu.add_argument("--rpm-max", type=int, default=6000)
    ecu.add_argument("--coolant", type=float, default=85.0)
    ecu.add_argument("--oil-kpa", type=int, default=250)
    ecu.set_defaults(func=run_ecu)

    hb = sub.add_parser("heartbeat", help="Single node heartbeat")
    hb.add_argument("--device", choices=["dcc", "ecu", "button_box"], default="ecu")
    hb.add_argument("--duration", type=float, default=2.0)
    hb.set_defaults(func=run_heartbeat)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
