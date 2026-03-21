import sys


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """CLI entry point: parse argv, call greet(), print result."""
    if len(sys.argv) < 2:
        print("Usage: python src/greet.py <name>", file=sys.stderr)
        sys.exit(1)
    print(greet(sys.argv[1]))


if __name__ == "__main__":
    main()
