"""
This module uses abc library to define an abstract class for the view. This is usefull in order to ensure
that all views have the same methods and attributes. This is a good practice to ensure that the code is
maintainable and scalable.
"""

from abc import ABC, abstractmethod


class View(ABC):
    """View class is an abstract class that defines the interface for the views.
    This class is used to ensure that all views have the same methods and attributes.

    Attributes:
        None
    """

    @abstractmethod
    def display_introduction(self):
        """Display the introduction of the game."""
        pass

    @abstractmethod
    def display_game_over(self, winner):
        """Display the game over message.

        Args:
            winner (Player): The winner of the game.
        """
        pass

    @abstractmethod
    def get_player_info(self, player_number):
        """Query the user for player type, name, and representation.

        Args:
            player_number (int): The player number (e.g., 1 or 2).

        Returns:
            dict: A dictionary containing player information.
        """
        pass

    @abstractmethod
    def display_board(self, board_state, player_1, player_2):
        """Display the game board.

        Args:
            board (list): The game board.
            player_1 (Player): Player 1.
            player_2 (Player): Player 2.
        """
        pass
    
    @abstractmethod
    def display_header(self, player_1, player_2, current_player, score):
        """Display the header of the game.

        Args:
            player_1 (Player): Player 1.
            player_2 (Player): Player 2.
        """
        pass