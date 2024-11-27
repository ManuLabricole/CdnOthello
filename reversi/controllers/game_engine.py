from typing import Dict

from reversi.models import Board, Player
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
        self.view: View = view
        self.board: Board = None
        self.player_1: Player = None
        self.player_2: Player = None
        self.current_player: int = None  # 0 or 1
    
    def _create_players(self):
        """Take input from the user to create two players.

        Expects the following dictionary structure:
        {
            'name': 'Player 1',
            'representation': '⚫',
            'type': 'H'
        }

        Args:
            None

        Returns:
            None
        """
        player_1_specs: Dict = self.view.get_player_info(1)
        self.player_1 = Player.create_player(player_1_specs)
        player_2_specs: Dict = self.view.get_player_info(2)
        self.player_2 = Player.create_player(player_2_specs)

        # Finally



    def start_game(self):
        """Start the game by initializing the board and players, then run the game loop."""
        self._create_players()
