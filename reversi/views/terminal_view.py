"""
This module uses the View abstract class to define the TerminalView class. This class
implements the required method in order to :
    - Display the game to the user
    - Gather inputs for initializing the game
    - Display the game board
    - Gather player moves
    - Transmit the moves to the controller: GameEngine
"""

from reversi.views.view import View


class TerminalView(View):
    """TerminalView class is responsible for displaying the game to the user and gathering inputs.

    Attributes:
        None
    """

    def __init__(self):
        self.display_introduction()

    def display_introduction(self):
        """Display the introduction of the game."""
        print("Welcome to Reversi!")
        print("The game is played on an 8x8 board.")
        print("The game ends when no player can make a valid move.")
        print("The player with the most pieces on the board wins.")
        print("Good luck!\n")

    # def display_board(self, board):
    #     """Display the game board.

    #     Args:
    #         board (Board): The game board.
    #     """
    #     print("  a b c d e f g h")
    #     for i in range(8):
    #         print(i + 1, end=" ")
    #         for j in range(8):
    #             if board.get_square(i, j) == 0:
    #                 print(".", end=" ")
    #             elif board.get_square(i, j) == 1:
    #                 print("X", end=" ")
    #             else:
    #                 print("O", end=" ")
    #         print()

    # def get_player_move(self):
    #     """Get the player move.

    #     Returns:
    #         str: The player move.
    #     """
    #     move = input("Enter your move (e.g. a1): ")
    #     return move

    # def display_invalid_move(self):
