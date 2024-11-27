import argparse

from reversi.controllers import GameEngine
from reversi.views import PygameView, TerminalView

VIEW_CHOICES = ["terminal_view", "pygame_view"]
VIEW_CHOICE = VIEW_CHOICES[0]


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run the Othello game with the specified view.')
    parser.add_argument(
        'view_choice',
        choices=['terminal', 'pygame'],
        help='Choose which view to use: "terminal" or "pygame".'
    )
    args = parser.parse_args()
    # 1. Instantiate the view according to the argument
    try:
        if args.view_choice == 'terminal':
            view = TerminalView()
        elif args.view_choice == 'pygame':
            view = PygameView()
        else:
            raise ValueError(f"Invalid view_choice: {args.view_choice}. Quitting...")
    except ValueError as e:
        print(e)
        main()

    # # 2. Instanciate the game engine passing the view
    game_engine = GameEngine(view)

    # # 3. Start the game
    game_engine.start_game()


if __name__ == "__main__":
    main()
