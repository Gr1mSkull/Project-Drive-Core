# config_compiler

YAML vehicle profile → DCFG binary blob v0.1 (см. `agents_stuff/config_binary_v0.1.md`).

## Установка

```bash
pip install -r tools/config_compiler/requirements.txt
```

## Использование

```bash
python tools/config_compiler/drivecore_config_compiler.py \
  config/vehicles/e30_gen1.yaml -o build/e30_gen1.dcfg

python tools/config_compiler/drivecore_config_compiler.py \
  config/vehicles/devkit.yaml -o build/devkit.dcfg --hex
```

## Тест

```bash
python -m unittest tools.config_compiler.test_compiler
```
