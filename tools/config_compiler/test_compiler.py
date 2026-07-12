"""Tests for config compiler."""

from __future__ import annotations

import struct
import unittest
from pathlib import Path

from compiler import compile_config, load_yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


class ConfigCompilerTest(unittest.TestCase):
    def test_e30_gen1_compiles(self) -> None:
        path = REPO_ROOT / "config/vehicles/e30_gen1.yaml"
        data = load_yaml(path)
        blob = compile_config(data)
        magic, version, crc, out_count, rule_count, mode_count, _ = struct.unpack(
            "<4sHHHHHH", blob[:16]
        )
        self.assertEqual(magic, b"DCFG")
        self.assertEqual(version, 0x0001)
        self.assertEqual(out_count, len(data["outputs"]))
        self.assertEqual(rule_count, len(data["rules"]))
        self.assertGreater(len(blob), 16)

    def test_devkit_compiles(self) -> None:
        path = REPO_ROOT / "config/vehicles/devkit.yaml"
        data = load_yaml(path)
        blob = compile_config(data)
        self.assertTrue(blob.startswith(b"DCFG"))


if __name__ == "__main__":
    unittest.main()
