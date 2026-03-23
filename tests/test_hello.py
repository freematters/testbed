"""Unit tests for hello module."""

from testbed.hello import hello


class TestHello:
    def test_importable(self) -> None:
        """hello function is importable from testbed.hello."""
        assert callable(hello)

    def test_basic_greeting(self) -> None:
        assert hello("World") == "Hello, World!"

    def test_empty_string(self) -> None:
        assert hello("") == "Hello, !"
