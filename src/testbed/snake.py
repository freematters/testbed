"""TUI Snake game using curses."""

from __future__ import annotations

import curses
import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


OPPOSITE = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}

KEY_MAP = {
    curses.KEY_UP: Direction.UP,
    curses.KEY_DOWN: Direction.DOWN,
    curses.KEY_LEFT: Direction.LEFT,
    curses.KEY_RIGHT: Direction.RIGHT,
    ord("w"): Direction.UP,
    ord("s"): Direction.DOWN,
    ord("a"): Direction.LEFT,
    ord("d"): Direction.RIGHT,
}


@dataclass
class Game:
    """Core snake game logic, independent of rendering."""

    height: int
    width: int
    snake: list[tuple[int, int]] = field(default_factory=list)
    direction: Direction = Direction.RIGHT
    food: Optional[tuple[int, int]] = None
    score: int = 0
    game_over: bool = False

    def __post_init__(self) -> None:
        mid_y, mid_x = self.height // 2, self.width // 2
        self.snake = [(mid_y, mid_x - i) for i in range(3)]
        self.place_food()

    def place_food(self) -> None:
        """Place food on a random empty cell."""
        occupied = set(self.snake)
        free = [
            (r, c)
            for r in range(1, self.height - 1)
            for c in range(1, self.width - 1)
            if (r, c) not in occupied
        ]
        if free:
            self.food = random.choice(free)

    def change_direction(self, new_dir: Direction) -> None:
        """Change direction, ignoring reversal."""
        if new_dir != OPPOSITE[self.direction]:
            self.direction = new_dir

    def tick(self) -> None:
        """Advance the game by one step."""
        if self.game_over:
            return

        head_y, head_x = self.snake[0]
        dy, dx = self.direction.value
        new_head = (head_y + dy, head_x + dx)

        # Wall collision
        if (
            new_head[0] <= 0
            or new_head[0] >= self.height - 1
            or new_head[1] <= 0
            or new_head[1] >= self.width - 1
        ):
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()


def run(stdscr: curses.window) -> int:
    """Run the snake game in a curses window. Returns final score."""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(120)

    max_y, max_x = stdscr.getmaxyx()
    game = Game(height=max_y, width=max_x)

    while not game.game_over:
        stdscr.erase()

        # Draw border
        for x in range(game.width):
            stdscr.addch(0, x, "#")
            if game.height - 1 < max_y:
                stdscr.addch(game.height - 1, min(x, max_x - 1), "#")
        for y in range(game.height):
            stdscr.addch(y, 0, "#")
            stdscr.addch(y, min(game.width - 1, max_x - 1), "#")

        # Draw food
        if game.food:
            fy, fx = game.food
            if 0 <= fy < max_y and 0 <= fx < max_x:
                stdscr.addch(fy, fx, "*")

        # Draw snake
        for i, (sy, sx) in enumerate(game.snake):
            if 0 <= sy < max_y and 0 <= sx < max_x:
                ch = "O" if i == 0 else "o"
                stdscr.addch(sy, sx, ch)

        # Score
        score_text = f" Score: {game.score} "
        stdscr.addstr(0, 2, score_text)

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            break
        if key in KEY_MAP:
            game.change_direction(KEY_MAP[key])

        game.tick()

    # Game over screen
    stdscr.erase()
    msg = f"Game Over! Score: {game.score}"
    stdscr.addstr(max_y // 2, max(0, (max_x - len(msg)) // 2), msg)
    stdscr.addstr(max_y // 2 + 1, max(0, (max_x - 14) // 2), "Press any key...")
    stdscr.nodelay(False)
    stdscr.refresh()
    stdscr.getch()

    return game.score


def main() -> None:
    curses.wrapper(run)


if __name__ == "__main__":
    main()
