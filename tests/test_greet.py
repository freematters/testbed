import subprocess
import sys
from pathlib import Path

from greet import greet

VENV_PYTHON = str(Path(__file__).resolve().parent.parent / ".venv" / "bin" / "python")
GREET_SCRIPT = str(Path(__file__).resolve().parent.parent / "src" / "greet.py")


def test_greet_returns_hello_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


def test_greet_special_characters():
    assert greet("O'Brien") == "Hello, O'Brien!"


def test_cli_prints_greeting():
    result = subprocess.run(
        [VENV_PYTHON, GREET_SCRIPT, "Alice"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "Hello, Alice!\n"


def test_cli_missing_arg_exits_1():
    result = subprocess.run(
        [VENV_PYTHON, GREET_SCRIPT],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Usage: python src/greet.py <name>" in result.stderr


def test_cli_extra_args_ignored():
    result = subprocess.run(
        [VENV_PYTHON, GREET_SCRIPT, "Alice", "Bob"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "Hello, Alice!\n"
