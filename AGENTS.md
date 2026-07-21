# AGENTS.md

Engineering policy lives in `.cursor/ENGINEERING_CONSTITUTION.mdc` (authoritative) with wrappers in `.cursor/rules/`. Follow those for design/process rules.

## Cursor Cloud specific instructions

DriveCore is mostly an engineering-docs/hardware repo; the runnable code is small. Standard commands are in the root `Makefile` and per-component READMEs — prefer those instead of duplicating them.

Runnable components:
- `firmware/shared/` — C library + CRC-16 test, built with CMake/ctest. Run via `make test-shared`.
- `tools/config_compiler/` — Python (PyYAML) YAML→DCFG compiler + `unittest`. Run via `make test-config`; produce binaries with `make build-config` (outputs to `build/`).
- `tools/can_sim/` — Python DCP CAN frame simulator (no deps). Run via `make test-can-sim` or directly (see `tools/can_sim/README.md`).
- `web/ui/` — static vanilla-JS dashboard, no build step. Serve with `python3 -m http.server 8080` from `web/ui/`.

Non-obvious notes:
- `make test-config` imports the compiler as a top-level module, so it runs `python3 -m unittest test_compiler` from inside `tools/config_compiler/` (not the dotted path in the README).
- The web UI has no backend in this repo; with no DCC connected it intentionally falls back to demo data (status bar shows "Offline (demo data)"). This is expected, not a failure. The Service PIN login and Logger screens require a real ESP32/DCC backend to return live data.
- `make test-shared` compiles with whatever C compiler CMake finds (Clang here); no toolchain pinning is required for host builds.
- System tooling (Python 3, PyYAML, CMake, a C compiler, make) is already present; the startup update script only refreshes the Python dependency.
