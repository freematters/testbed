from greet import greet


def test_greet_returns_hello_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


def test_greet_special_characters():
    assert greet("O'Brien") == "Hello, O'Brien!"
