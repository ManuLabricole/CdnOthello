from reversi.views.view import View


class GameEngine:
    """GameEngine class is responsible for handling the game logic.
    Act as a Controller by handling the flow of the game and interfacing the Model and View.

    Attributes:
        board (Board): The game board.
        player1 (Player): The first player.
        player2 (Player): The second player.
        current_player (Player): The current player.
        next_player (Player): The next player.
        is_game_over (bool): Flag to indicate if the game is over.
        winner (Player): The winner of the game.
    """

    def __init__(self, view: View):
        """Initialize the GameEngine with the given board and players.

        Args:
            view (View): The view to display the game.
        """
        self.board = None
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def start_game(self):
        """Start the game by initializing the board and players, then run the game loop."""
        print("Starting the game...")
        print("Game Over!")