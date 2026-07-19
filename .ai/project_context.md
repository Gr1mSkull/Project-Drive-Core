# DriveCore — AI Project Context

**WP-001** · Operational context for AI assistants. Not an official specification.

## Identity

| Field | Value |
|-------|-------|
| Project | DriveCore (open modular automotive platform) |
| Repository | Project-Drive-Core |
| Gen1 vehicle | BMW E30 race (profile: `config/vehicles/e30_gen1.yaml`) |
| Your role | Implementation Engineer — **not** System Architect |

## Gen1 Test Owner (operational)

Gen1 physical DevKit and vehicle Test Owner:  
**Founder / Chief Engineer — Dmitry Arutyunov.**

- Implementation agents may execute automated checks and record raw results.
- Independent Review Agents may certify reproducible software and documentation verification.
- Physical lab and vehicle-test certification requires the human Test Owner.
- System Architect approves architecture and stage gates but does not claim physical test execution.

This is operational role assignment, not system architecture. Authoritative engineering policy: `.cursor/ENGINEERING_CONSTITUTION.mdc`.

## Modules (fixed boundaries)

| Module | Responsibility |
|--------|----------------|
| **DCC** | PDM + VCM + diagnostics + CAN + logging + config execution |
| **ECU** | Engine only |
| **Button Box** | HMI events → CAN |
| **Tablet** | Web UI client (optional) |

## Non-negotiables

- STM32 works without ESP32/tablet.
- Configuration over code (`config/vehicles/*.yaml`).
- One CAN FD bus Gen1 (DCC — ECU — Button Box).
- Binary DCPI on SPI; JSON for browser only.

## Where to read first

1. Current work package / user task
2. `.ai/architecture_summary.md`
3. `docs/001`, `docs/004`, `docs/005`
4. `docs/ADR/` and `docs/EDL/`
5. `docs/SRS/` (when populated)

## Where agents write notes

`agents_stuff/` — session notes, checklists, cheat-sheets. **Not** official docs.

## Rules

**Authoritative:** `.cursor/ENGINEERING_CONSTITUTION.mdc` (always applied).  
Numbered `.cursor/rules/00`–`10` are wrappers pointing to constitution sections.
