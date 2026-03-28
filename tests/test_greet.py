"""Unit tests for greet module."""

from testbed.greet import greet


class TestGreet:
    def test_importable(self) -> None:
        """greet function is importable from testbed.greet."""
        assert callable(greet)

    def test_basic_greeting(self) -> None:
        assert greet("World") == "Hello, World!"

    def test_empty_string(self) -> None:
        assert greet("") == "Hello, !"
