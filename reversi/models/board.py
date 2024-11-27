# reversi/models/board.py
from typing import List, Tuple

DIRECTIONS = [
    (-1, -1),  # Top-left
    (-1, 0),  # Up
    (-1, 1),  # Top-right
    (0, -1),  # Left
    (0, 1),  # Right
    (1, -1),  # Bottom-left
    (1, 0),  # Down
    (1, 1),  # Bottom-right
]


class Board:
    """Class to track the state of the game board."""

    def __init__(self, x=8, y=8):
        """
        Initialize the game board.

        Args:
            size (int): Size of the board (default is 8x8).
        """
        self.x = x
        self.y = y
        self._grid = [[0 for _ in range(x)] for _ in range(y)]
        self._initialize()

    def _initialize(self):
        """Set up the initial board state with starting pieces."""
        mid_x, mid_y = self.x // 2, self.y // 2
        self._grid[mid_y - 1][mid_x - 1] = 1  # Player 1
        self._grid[mid_y][mid_x] = 1  # Player 1
        self._grid[mid_y - 1][mid_x] = 2  # Player 2
        self._grid[mid_y][mid_x - 1] = 2  # Player 2

    def get_score(self):
        """
        Calculate the current score for both players.

        Returns:
            dict: A dictionary with keys 'player_1' and 'player_2', representing their scores.
        """
        player_1_score = sum(row.count(1) for row in self._grid)
        player_2_score = sum(row.count(2) for row in self._grid)
        return {"player_1": player_1_score, "player_2": player_2_score}

    def get_available_moves(self, player: int) -> List[Tuple[int, int]]:
        """
        Return a list of available moves for the given player.

        Args:
            player (int): The player number (1 or 2).

        Returns:
            list of tuples: A list of (x, y) coordinates for valid moves.
        """
        opponent = 2 if player == 1 else 1
        valid_moves = []

        for y in range(self.y):
            for x in range(self.x):
                if self._grid[y][x] != 0:
                    continue  # Skip occupied cells

                # Check all directions from the empty cell
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy

                    # Step 1: Check if adjacent square is on the board
                    if not (0 <= nx < self.x and 0 <= ny < self.y):
                        continue  # Skip if out of bounds

                    # Step 2: Check if adjacent square has opponent's piece
                    if self._grid[ny][nx] != opponent:
                        continue  # No opponent piece next to this square

                    # Step 3: Move along the direction to find player's own piece
                    while True:
                        nx += dx
                        ny += dy

                        if not (0 <= nx < self.x and 0 <= ny < self.y):
                            break  # Out of bounds

                        if self._grid[ny][nx] == opponent:
                            continue  # Continue searching

                        elif self._grid[ny][nx] == player:
                            # Found player's own piece, so the move is valid
                            valid_moves.append((x, y))
                            break

                        else:
                            # Empty square or other, not valid in this direction
                            break

        # Remove duplicates and return the list of valid moves
        return list(set(valid_moves))

    @property
    def state(self) -> List[List[int]]:
        """This property returns the current state of the board in a structure that will be parsable and displayable by the view"""
        return self._grid
