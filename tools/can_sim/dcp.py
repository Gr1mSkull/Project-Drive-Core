"""DriveCore Protocol (DCP) v0.1 frame helpers."""

from __future__ import annotations

import struct
from dataclasses import dataclass
from enum import IntEnum


class MessageClass(IntEnum):
    HEARTBEAT = 0
    TELEMETRY = 1
    EVENT = 2
    COMMAND = 3


class DeviceType(IntEnum):
    DCC = 0x1
    ECU = 0x2
    BUTTON_BOX = 0x3


DCP_PROTO_VER = 0x01


def can_id(mc: MessageClass, dt: DeviceType, instance: int = 0) -> int:
    return ((int(mc) << 8) | (int(dt) << 4) | (instance & 0x0F)) & 0x7FF


@dataclass
class CanFrame:
    can_id: int
    data: bytes

    def hex_line(self) -> str:
        payload = " ".join(f"{b:02X}" for b in self.data)
        return f"ID=0x{self.can_id:03X} DLC={len(self.data)} {payload}"


def dcp_header(msg_type: int, seq: int, payload: bytes) -> bytes:
    return struct.pack("<BBH", DCP_PROTO_VER, msg_type, seq & 0xFFFF) + payload


def heartbeat(dt: DeviceType, seq: int, node_state: int = 2, fault: int = 0) -> CanFrame:
    body = dcp_header(0x01, seq, struct.pack("<BBHI", node_state, fault, 0x0100, 0))
    return CanFrame(can_id(MessageClass.HEARTBEAT, dt), body)


def ecu_engine_telemetry(
    seq: int,
    rpm: int,
    coolant_c10: int,
    oil_kpa: int,
    throttle: int = 0,
    engine_flags: int = 1,
) -> CanFrame:
    payload = struct.pack("<HhHBB", rpm, coolant_c10, oil_kpa, throttle, engine_flags)
    body = dcp_header(0x20, seq, payload)
    return CanFrame(can_id(MessageClass.TELEMETRY, DeviceType.ECU), body)


def ecu_cooling_request(seq: int, level: int, reason: int = 0) -> CanFrame:
    body = dcp_header(0x21, seq, struct.pack("<BB", level, reason))
    return CanFrame(can_id(MessageClass.TELEMETRY, DeviceType.ECU), body)


def button_event(seq: int, control_id: int, action: int, value: int = 0) -> CanFrame:
    payload = struct.pack("<HBh", control_id, action, value)
    body = dcp_header(0x30, seq, payload)
    return CanFrame(can_id(MessageClass.EVENT, DeviceType.BUTTON_BOX), body)
