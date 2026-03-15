"""Unit tests for snake game logic."""

from testbed.snake import Direction, Game, OPPOSITE


class TestDirection:
    def test_opposites(self) -> None:
        assert OPPOSITE[Direction.UP] == Direction.DOWN
        assert OPPOSITE[Direction.DOWN] == Direction.UP
        assert OPPOSITE[Direction.LEFT] == Direction.RIGHT
        assert OPPOSITE[Direction.RIGHT] == Direction.LEFT


class TestGame:
    def _make_game(self, height: int = 20, width: int = 40) -> Game:
        return Game(height=height, width=width)

    def test_initial_state(self) -> None:
        game = self._make_game()
        assert len(game.snake) == 3
        assert game.score == 0
        assert not game.game_over
        assert game.food is not None
        assert game.direction == Direction.RIGHT

    def test_snake_starts_in_center(self) -> None:
        game = self._make_game(20, 40)
        head_y, head_x = game.snake[0]
        assert head_y == 10
        assert head_x == 20

    def test_tick_moves_snake(self) -> None:
        game = self._make_game()
        head_before = game.snake[0]
        game.tick()
        head_after = game.snake[0]
        assert head_after[1] == head_before[1] + 1  # moved right
        assert head_after[0] == head_before[0]  # same row
        assert len(game.snake) == 3  # no food eaten

    def test_change_direction(self) -> None:
        game = self._make_game()
        game.change_direction(Direction.UP)
        assert game.direction == Direction.UP

    def test_cannot_reverse(self) -> None:
        game = self._make_game()
        assert game.direction == Direction.RIGHT
        game.change_direction(Direction.LEFT)
        assert game.direction == Direction.RIGHT  # ignored

    def test_wall_collision(self) -> None:
        game = self._make_game(20, 40)
        # Move snake head to right wall
        game.snake[0] = (10, 38)
        game.direction = Direction.RIGHT
        game.tick()
        assert game.game_over

    def test_self_collision(self) -> None:
        game = self._make_game()
        # Create a snake that will collide with itself
        game.snake = [(10, 10), (10, 11), (10, 12), (9, 12), (9, 11), (9, 10)]
        game.direction = Direction.UP
        game.tick()  # head moves to (9, 10) which is already in snake
        assert game.game_over

    def test_eating_food(self) -> None:
        game = self._make_game()
        # Place food right in front of snake
        head_y, head_x = game.snake[0]
        game.food = (head_y, head_x + 1)
        game.tick()
        assert game.score == 1
        assert len(game.snake) == 4  # grew by 1

    def test_no_tick_after_game_over(self) -> None:
        game = self._make_game()
        game.game_over = True
        snake_copy = list(game.snake)
        game.tick()
        assert game.snake == snake_copy

    def test_food_not_on_snake(self) -> None:
        game = self._make_game()
        occupied = set(game.snake)
        assert game.food not in occupied
