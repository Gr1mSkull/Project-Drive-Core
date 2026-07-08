.PHONY: test-shared test-config test-can-sim test-all

test-shared:
	cmake -S firmware/shared -B build/shared
	cmake --build build/shared
	ctest --test-dir build/shared --output-on-failure

test-config:
	pip install -q -r tools/config_compiler/requirements.txt
	cd tools/config_compiler && python3 -m unittest test_compiler

test-can-sim:
	python3 tools/can_sim/can_sim.py heartbeat --device ecu --duration 0.3 | head -5

test-all: test-shared test-config test-can-sim

build-config:
	mkdir -p build
	pip install -q -r tools/config_compiler/requirements.txt
	python3 tools/config_compiler/drivecore_config_compiler.py config/vehicles/e30_gen1.yaml -o build/e30_gen1.dcfg
	python3 tools/config_compiler/drivecore_config_compiler.py config/vehicles/devkit.yaml -o build/devkit.dcfg
