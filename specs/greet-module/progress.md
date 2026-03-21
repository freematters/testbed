# Progress

## Step 1: Greet function with unit tests
- **Files changed**: `src/greet.py` (new), `tests/test_greet.py` (new), `pyproject.toml` (updated pytest config)
- **What was built**: Core `greet(name: str) -> str` function returning `"Hello, {name}!"`
- **Tests**: 3 unit tests added, all passing
- **Notes**: Added `pythonpath = ["src"]` to pyproject.toml for pytest imports
