"""DriveCore config compiler — YAML vehicle profile to DCFG binary v0.1."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path
from typing import Any

import yaml

from crc16 import crc16_ccitt

DCFG_MAGIC = b"DCFG"
DCFG_VERSION = 0x0001
HEADER_SIZE = 16
OUTPUT_ENTRY_SIZE = 16
RULE_ENTRY_SIZE = 32
MAX_OUTPUTS = 22
MAX_RULES = 16

MODE_ACTION = {"off": 0, "on": 1, "auto": 2, "prime": 3}
OUTPUT_TYPE = {"high_side": 0, "pwm": 1, "hbridge": 2}

COND_MAP = {
    "vehicle_mode": 1,
    "engine_running": 2,
    "coolant_temp_gt": 3,
    "oil_pressure_lt": 4,
    "battery_gt": 5,
    "battery_lt": 6,
    "rpm_gt": 7,
    "button_event": 8,
}

ACTION_MAP = {
    "output_on": 1,
    "log_event": 2,
    "notify": 3,
}

MODE_NAME_TO_ID = {
    "OFF": 0,
    "MASTER_ON": 1,
    "IGNITION": 2,
    "PRIME": 3,
    "READY": 4,
    "ENGINE_RUN": 5,
    "RACE": 6,
    "COOL_DOWN": 7,
}


def encode_mode_mask(modes: dict[str, str], profile_modes: list[str]) -> int:
    mask = 0
    for idx, mode_name in enumerate(profile_modes[:8]):
        action = modes.get(mode_name, "off")
        value = MODE_ACTION.get(action, 0)
        mask |= (value & 0x3) << (idx * 2)
    return mask


def compile_output(name: str, spec: dict[str, Any], profile_modes: list[str]) -> bytes:
    channel = int(spec["channel"])
    out_type = OUTPUT_TYPE[spec["type"]]
    current = int(spec.get("current_limit_a", 10))
    retry = int(spec.get("retry", 1))
    flags = 0x01 if spec.get("pwm", False) else 0x00
    mode_mask = encode_mode_mask(spec.get("modes", {}), profile_modes)
    return struct.pack(
        "<BBBBBBxxQ",
        channel,
        out_type,
        current,
        retry,
        flags,
        0,
        mode_mask,
    )


def _condition_param(when: dict[str, Any]) -> tuple[int, int]:
    if "vehicle_mode" in when:
        mode = when["vehicle_mode"]
        return COND_MAP["vehicle_mode"], MODE_NAME_TO_ID.get(mode, 0)
    if "engine_running" in when:
        return COND_MAP["engine_running"], 1 if when["engine_running"] else 0
    if "coolant_temp_gt" in when:
        return COND_MAP["coolant_temp_gt"], int(when["coolant_temp_gt"])
    if "oil_pressure_lt" in when:
        return COND_MAP["oil_pressure_lt"], int(float(when["oil_pressure_lt"]) * 10)
    if "battery_gt" in when:
        return COND_MAP["battery_gt"], int(float(when["battery_gt"]) * 10)
    if "battery_lt" in when:
        return COND_MAP["battery_lt"], int(float(when["battery_lt"]) * 10)
    if "rpm_gt" in when:
        return COND_MAP["rpm_gt"], int(when["rpm_gt"])
    if "button_event" in when:
        return COND_MAP["button_event"], int(when["button_event"].get("control_id", 0))
    return 0, 0


def _first_action(rule: dict[str, Any], output_index: dict[str, int]) -> tuple[int, int, int]:
    for action in rule.get("then", []):
        if "output_on" in action:
            name = action["output_on"]
            return ACTION_MAP["output_on"], output_index.get(name, 0xFF), 0
        if "log_event" in action:
            return ACTION_MAP["log_event"], 0, 0
        if "notify" in action:
            severity = 1 if action["notify"] == "warning" else 0
            return ACTION_MAP["notify"], 0, severity
    return 0, 0, 0


def compile_rule(rule_id: int, rule: dict[str, Any], output_index: dict[str, int]) -> bytes:
    when = rule.get("when", {})
    cond_type, cond_param = _condition_param(when)
    act_type, act_target, act_param = _first_action(rule, output_index)
    payload = struct.pack("<BBhBBB", rule_id, cond_type, cond_param, act_type, act_target, act_param)
    return payload.ljust(RULE_ENTRY_SIZE, b"\x00")


def compile_config(data: dict[str, Any]) -> bytes:
    profile_modes = list(data.get("modes", []))
    outputs: dict[str, Any] = data.get("outputs", {})
    rules: list[dict[str, Any]] = list(data.get("rules", []))

    output_names = list(outputs.keys())
    output_index = {name: idx for idx, name in enumerate(output_names)}

    if len(outputs) > MAX_OUTPUTS:
        raise ValueError(f"too many outputs: {len(outputs)} > {MAX_OUTPUTS}")
    if len(rules) > MAX_RULES:
        raise ValueError(f"too many rules: {len(rules)} > {MAX_RULES}")

    body = bytearray()
    for name in output_names:
        body.extend(compile_output(name, outputs[name], profile_modes))

    for idx, rule in enumerate(rules):
        body.extend(compile_rule(idx + 1, rule, output_index))

    header = struct.pack(
        "<4sHHHHHH",
        DCFG_MAGIC,
        DCFG_VERSION,
        0,
        len(outputs),
        len(rules),
        len(profile_modes),
        0,
    )
    blob = bytearray(header) + body
    crc = crc16_ccitt(blob[8:])
    blob[6:8] = struct.pack("<H", crc)
    return bytes(blob)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compile DriveCore vehicle YAML to DCFG binary")
    parser.add_argument("input", type=Path, help="YAML config path")
    parser.add_argument("-o", "--output", type=Path, help="Output .dcfg path")
    parser.add_argument("--hex", action="store_true", help="Print hex to stdout")
    args = parser.parse_args(argv)

    data = load_yaml(args.input)
    blob = compile_config(data)

    if args.hex:
        print(blob.hex())
    if args.output:
        args.output.write_bytes(blob)
        print(f"Wrote {len(blob)} bytes to {args.output}", file=sys.stderr)
    elif not args.hex:
        sys.stdout.buffer.write(blob)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
