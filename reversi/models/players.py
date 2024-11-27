# reversi/models/players.py
from typing import Dict


class Player:
    def __init__(self, name, representation, num):
        self.name = name
        self.representation = representation  # Emoji representing the player's pieces
        self.num = num

    # Class method in order to return the Player corresponding to a specific number
    @classmethod
    def get_player_by_num(cls, num):
        # Loop through all the subclasses of Player
        for subclass in cls.__subclasses__():
            if subclass.num == num:
                return subclass

    @staticmethod
    def validate_specs(player_specs: Dict):
        # We validate the specs for a human player
        if player_specs["type"] == "Human":
            if not player_specs["name"]:
                raise ValueError("Player name cannot be empty.")
            if not player_specs["representation"]:
                raise ValueError("Player representation cannot be empty.")
            if not player_specs["num"]:
                raise ValueError("Player number cannot be empty.")
        # We validate the specs for an AI player
        elif player_specs["type"] == "AI":
            raise NotImplementedError("AIPlayer class is not implemented yet.")

        else:
            raise ValueError("Player type must be either 'Human' or 'AI'.")

    @staticmethod
    def create_player(player_specs: Dict):
        # We create a human player
        Player.validate_specs(player_specs)
        if player_specs["type"] == "Human":
            return HumanPlayer(player_specs["name"], player_specs["representation"], num=player_specs["num"])
        # We create an AI player
        elif player_specs["type"] == "AI":
            return AIPlayer(player_specs["name"], player_specs["representation"], num=player_specs["num"], difficulty=player_specs["difficulty"])
        else:
            raise ValueError("Player type must be either 'Human' or 'AI'.")


class HumanPlayer(Player):
    def __init__(self, name, representation, num):
        super().__init__(name, representation, num)

    # Add methods for making moves...


class AIPlayer(Player):
    def __init__(self, name, representation, num, difficulty):
        raise NotImplementedError("AIPlayer class is not implemented yet.")
        super().__init__(name, representation, num)
        self.difficulty = difficulty

    # Add methods for making moves...
