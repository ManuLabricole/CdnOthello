"""
This module uses abc library to define an abstract class for the view. This is usefull in order to ensure
that all views have the same methods and attributes. This is a good practice to ensure that the code is
maintainable and scalable.
"""

from abc import ABC, abstractmethod

from reversi.models.board import Board


class View(ABC):
    """View class is an abstract class that defines the interface for the views.
    This class is used to ensure that all views have the same methods and attributes.

    Attributes:
        None
    """

    @abstractmethod
    def display_introduction(self):
        """Display the introduction of the game.
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