# Progress

## Step 1: Greet function with unit tests
- **Files changed**: `src/greet.py` (new), `tests/test_greet.py` (new), `pyproject.toml` (updated pytest config)
- **What was built**: Core `greet(name: str) -> str` function returning `"Hello, {name}!"`
- **Tests**: 3 unit tests added, all passing
- **Notes**: Added `pythonpath = ["src"]` to pyproject.toml for pytest imports

## Step 2: CLI entry point with subprocess tests
- **Files changed**: `src/greet.py` (modified), `tests/test_greet.py` (modified)
- **What was built**: `main()` function and `if __name__ == "__main__"` block for CLI usage
- **Tests**: 3 subprocess-based CLI tests added (6 total), all passing
- **Notes**: None
