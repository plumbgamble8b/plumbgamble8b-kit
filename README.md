# plumbgamble8b-kit

Validate JSON files and print a normalized form.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m plumbgamble8b_kit.cli --help
```

```python
from plumbgamble8b_kit.core import Plumbgamble8bTool

tool = Plumbgamble8bTool()
print(tool)
```

## Layout

```
plumbgamble8b_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 plumbgamble8b
