from src.hello import hello


def test_hello_world() -> None:
    assert hello("World") == "Hello, World!"


def test_hello_empty() -> None:
    assert hello("") == "Hello, !"


def test_hello_alice() -> None:
    assert hello("Alice") == "Hello, Alice!"
