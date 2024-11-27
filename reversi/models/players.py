# reversi/models/players.py
from typing import Dict


class Player:
    def __init__(self, name, representation):
        self.name = name
        self.representation = representation  # Emoji representing the player's pieces

    @staticmethod
    def validate_specs(player_specs: Dict):
        # We validate the specs for a human player
        if player_specs["type"] == "Human":
            if not player_specs["name"]:
                raise ValueError("Player name cannot be empty.")
            if not player_specs["representation"]:
                raise ValueError("Player representation cannot be empty.")
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
            return HumanPlayer(player_specs["name"], player_specs["representation"])
        # We create an AI player
        elif player_specs["type"] == "AI":
            return AIPlayer(player_specs["name"], player_specs["representation"])
        else:
            raise ValueError("Player type must be either 'Human' or 'AI'.")


class HumanPlayer(Player):
    def __init__(self, name, representation):
        super().__init__(name, representation)

    # Add methods for making moves...


class AIPlayer(Player):
    def __init__(self, name, representation, difficulty):
        raise NotImplementedError("AIPlayer class is not implemented yet.")
        super().__init__(name, representation)
        self.difficulty = difficulty

    # Add methods for making moves...
