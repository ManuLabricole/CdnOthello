from time import sleep
from typing import Dict, List, Tuple

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

    def __init__(self, view: View, debug=True):
        """Initialize the GameEngine with the given board and players.

        Args:
            view (View): The view to display the game.
        """
        self._debug = debug
        self.view: View = view
        self.board: Board = None
        self.player_1: Player = None
        self.player_2: Player = None
        self._current_player: int = 1  # Start with Player 1

    @property
    def current_player(self) -> Player:
        """Getter for the current player."""
        return self._current_player

    @current_player.setter
    def current_player(self, player_number: int):
        """Setter for the current player."""
        if player_number not in (1, 2):
            raise ValueError("Invalid player number. Must be 1 or 2.")

        # Set the internal current player index
        self._current_player = player_number

        # Trigger an animation or print indicating the current player
        sleep(1)  # Simulate a brief animation

    def _is_game_over(self):
        # Here we will call the method from the board class to check if the game is over
        # The reversi game ended when there are no more valid moves for both players
        try:
            available_moves = self.board.get_available_moves(self.current_player)
            if len(available_moves) == 0:
                return True
            return False
        except NotImplementedError:
            return False

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

        if self._debug:
            self.player_1 = Player.create_player(
                {"name": "Player 1", "representation": "⚫", "type": "Human"}
            )
            self.player_2 = Player.create_player(
                {"name": "Player 2", "representation": "⚪", "type": "Human"}
            )
        else:
            player_1_specs: Dict = self.view.get_player_info(1)
            self.player_1 = Player.create_player(player_1_specs)
            player_2_specs: Dict = self.view.get_player_info(2)
            self.player_2 = Player.create_player(player_2_specs)

        # Finally

    def _create_board(self):
        x, y = self.view.get_board_specs()
        self.board = Board(x, y)
        # self.view.display_board(self.board.state, self.player_1, self.player_2)

    def start_game(self):
        """Start the game by initializing the board and players, then run the game loop."""
        self._create_players()
        self._create_board()

        while not self._is_game_over():
            # 1. Get the current score
            score = self.board.get_score()
            # 2. Display the header
            self.view.display_header(
                self.player_1, self.player_2, self.current_player, score
            )
            # 3. Compute available moves
            available_moves: List[Tuple[int, int]] = self.board.get_available_moves(self.current_player)
            # 4. Display the board
            self.view.display_board(
                self.board.state, self.player_1, self.player_2, available_moves
            )
            # 5. Get the player's move
            move: Tuple[int, int] = self.view.get_player_move_choice(
                self.current_player, available_moves
            )
            # 6. Make the move i.e update the board accordingly
            self.board.make_move(self.current_player, move)
            # 6. Switch the current player
            self.current_player = 2 if self._current_player == 1 else 1

        self.view.display_game_over()
