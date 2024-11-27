# reversi/models/board.py


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
        self._grid[mid_y][mid_x] = 1         # Player 1
        self._grid[mid_y - 1][mid_x] = 2     # Player 2
        self._grid[mid_y][mid_x - 1] = 2     # Player 2

    def get_available_moves(self, player):
        """Return a list of available moves for the given player."""
        raise NotImplementedError

    def get_score(self):
        """
        Calculate the current score for both players.

        Returns:
            dict: A dictionary with keys 'player_1' and 'player_2', representing their scores.
        """
        player_1_score = sum(row.count(1) for row in self._grid)
        player_2_score = sum(row.count(2) for row in self._grid)
        return {"player_1": player_1_score, "player_2": player_2_score}

    @property
    def state(self):
        """This property returns the current state of the board in a structure that will be parsable and displayable by the view"""
        return self._grid

