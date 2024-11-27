from time import sleep
from typing import Dict, List, Tuple

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from reversi.views.view import View

# Get player representation (emoji)
EMOJI_CHOICES = {
    "1": "⚫",
    "2": "⚪",
    "3": "🔴",
    "4": "🔵",
    "5": "🟢",
    "6": "🟡",
    "7": "🟣",
    "8": "🟤",
}

X_Y_BOARD_CHOICES = {4, 6, 8, 10, 12}


class TerminalView(View):
    """TerminalView class is responsible for displaying the game to the user and gathering inputs.

    Attributes:
        console (Console): Rich Console object for rendering rich text.
    """

    def __init__(self, debug=True):
        self.console = Console()
        self._debug = debug
        self._emoji_chosen = []
        self.display_introduction()

    # ---------------
    # Display Methods
    # ---------------
    def display_introduction(self):
        """Display the introduction of the game with rich formatting and animations."""
        self.console.clear()

        # Title Panel
        title = Text("🎉 Welcome to Reversi! 🎉", style="bold magenta")
        if not self._debug:
            title_panel = Panel(
                Align.center(title),
                border_style="bright_green",
                padding=(1, 2),
            )
            self.console.print(title_panel)
            sleep(1)

            # Instructions
            instructions = (
                "📜 The game is played on an 8x8 board.\n"
                "🕹️ The game ends when no player can make a valid move.\n"
                "🏆 The player with the most pieces on the board wins.\n"
                "✨ Good luck!\n"
            )

            # Print instructions with animation
            for line in instructions.strip().split("\n"):
                self.console.print(line, style="cyan")
                sleep(0.5)

            # Stunning Loading Animation
            self.console.print("\n")
            with Progress(
                SpinnerColumn(spinner_name="earth"),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                expand=True,
                transient=True,
            ) as progress:
                task = progress.add_task("[green]Loading Game Components...", total=100)
                for i in range(100):
                    sleep(0.02)  # Simulate work being done
                    progress.update(task, advance=1)
            self.console.print(
                "[bold green]All set! Let's start the game![/bold green]\n"
            )

    def display_game_over(self, winner: str = None):
        """Display the game over message with the winner's name."""
        self.console.print("\n[bold magenta]🎉 Game Over! 🎉[/bold magenta]")
        if winner:
            self.console.print(f"[bold cyan]{winner}[/bold cyan] wins!")
        else:
            self.console.print("[bold yellow]It's a tie![/bold yellow]")

    def display_header(self, player_1, player_2, current_player, score):
        """
        Display the header with player specs, current turn, and live score.

        Args:
            player_1 (Player): Player 1 object.
            player_2 (Player): Player 2 object.
            current_player (Player): The current player object.
            score (dict): The current scores for both players.
        """
        self.console.print("\n[bold magenta]🎮 Reversi Game Status 🎮[/bold magenta]\n")

        # Determine which player is the current player to add the pointing emoji
        player_1_indicator = "🫵🏻" if current_player == player_1 else ""
        player_2_indicator = "🫵🏻" if current_player == player_2 else ""

        # Create a table for player specs and scores
        header = Table(show_header=False, box=None, padding=(0, 2))
        header.add_row(
            f"[green]Name:[/green][bold yellow][/bold yellow] {player_1.name} {player_1.representation} {player_1_indicator}",
            f"[green]Name:[/green][bold cyan][/bold cyan] {player_2.name} {player_2.representation} {player_2_indicator}",
        )
        header.add_row(
            f"[green]Type:[/green] {player_1.__class__.__name__}",
            f"[green]Type:[/green] {player_2.__class__.__name__}",
        )
        header.add_row(
            f"[green]Score:[/green] {score['player_1']}",
            f"[green]Score:[/green] {score['player_2']}",
        )

        self.console.print(header)

    def display_board(
        self, board_state: List[List[int]], player_1, player_2, current_player
    ):
        """
        Render the board state in the terminal with proper alignment and style.

        Args:
            board_state (list[list[int]]): The current board state.
            player_1 (Player): Player 1 object.
            player_2 (Player): Player 2 object.
        """
        self.console.print("\n[bold magenta]🌟 Reversi Board 🌟[/bold magenta]\n")

        board_state = board.state
        board_available_moves = board.get_available_moves(player=current_player)
        # Dynamically generate column labels with correct spacing
        num_columns = len(board_state[0])
        header = "      " + "  ".join(
            f"[bold green]{chr(ord('A') + i)}[/bold green]  "
            for i in range(num_columns)
        )
        self.console.print(header)

        # Top border
        top_border = "   ╔" + "════╤" * (num_columns - 1) + "════╗"
        self.console.print(f"[bright_blue]{top_border}[/bright_blue]")

        # Rows with board state and row numbers
        for y, row in enumerate(board_state):
            row_display = (
                f"[bold yellow]{y + 1:<2}[/bold yellow] │"  # Row label (1, 2, ...)
            )
            for x, cell in enumerate(row):
                if cell == 1:
                    row_display += f" {player_1.representation} │"
                elif cell == 2:
                    row_display += f" {player_2.representation} │"
                else:
                    if (x, y) in board_available_moves:
                        # Highlight available moves with a blue circle
                        row_display += " ♦️  │"
                    else:
                        row_display += " 🟩 │"  # Green square for empty cells
            self.console.print(f"[bright_blue]{row_display}[/bright_blue]")
            # self.console.print(f"[bright_blue]{row_display}[/bright_blue]")

            # Add a separator between rows (except the last row)
            if y < len(board_state) - 1:
                separator = "   ╟" + "────┼" * (num_columns - 1) + "────╢"
                self.console.print(f"[bright_blue]{separator}[/bright_blue]")

        # Bottom border
        bottom_border = "   ╚" + "════╧" * (num_columns - 1) + "════╝"
        self.console.print(f"[bright_blue]{bottom_border}[/bright_blue]")

        self.console.print("\n")

    # # -------------
    # Input Methods
    # -------------

    def get_player_info(self, player_number: int) -> Dict:
        """Query the user for player type, name, and representation."""
        self.console.print(
            f"\n[bold cyan]🎮 Configuring Player {player_number}[/bold cyan]"
        )

        # Get player type
        while True:
            player_type = (
                self.console.input(
                    "[magenta]🤖 Is this player a Human or AI? (H/A): [/magenta]"
                )
                .strip()
                .upper()
            )
            if player_type in ("H", "A"):
                break
            else:
                self.console.print(
                    "[red]❌ Invalid input. Please enter 'H' for Human or 'A' for AI.[/red]"
                )

        # Get player name
        name = self.console.input("[magenta]📝 Enter player name: [/magenta]").strip()
        if not name:
            name = f"Player {player_number}"

        while True:
            self.console.print(
                "[magenta]🎨 Choose a representation for your pieces:[/magenta]"
            )
            emoji_table = Table(show_header=False, show_edge=False, padding=(0, 1))
            for key, emoji in EMOJI_CHOICES.items():
                if key not in self._emoji_chosen:
                    emoji_table.add_row(f"{key}. {emoji}")
            self.console.print(emoji_table)
            choice = self.console.input(
                "Enter the number corresponding to your choice: "
            ).strip()
            if choice in EMOJI_CHOICES:
                representation = EMOJI_CHOICES[choice]
                self._emoji_chosen.append(choice)
                break
            else:
                self.console.print(
                    "[red]❌ Invalid choice. Please select a number from the list.[/red]"
                )

        # If AI, get difficulty level (optional)
        difficulty = None
        if player_type == "A":
            while True:
                difficulty = (
                    self.console.input(
                        "[magenta]🎯 Enter AI difficulty (Easy/Medium/Hard): [/magenta]"
                    )
                    .strip()
                    .lower()
                )
                if difficulty in ("easy", "medium", "hard"):
                    break
                else:
                    self.console.print(
                        "[red]❌ Invalid difficulty. Please enter 'Easy', 'Medium', or 'Hard'.[/red]"
                    )

        # Compile player info into a dictionary
        player_info = {
            "type": "AI" if player_type == "A" else "Human",
            "name": name,
            "representation": representation,
            "difficulty": difficulty or None,
        }
        return player_info

    def get_board_specs(self) -> Tuple[int, int]:
        """Thios method query the user to define the board x, y values
        In a first approximation we will fix the available values for x and y to be
        among X_Y_CHOICES = {4, 6, 8, 10, 12}
        """

        if self._debug:
            return 8, 8

        while True:
            x = int(
                self.console.input(
                    "[magenta]🎨 Enter the x value for the board (4, 6, 8, 10, 12): [/magenta]"
                )
            )
            if x in X_Y_BOARD_CHOICES:
                break
            else:
                self.console.print(
                    "[red]❌ Invalid choice. Please select a number from the list.[/red]"
                )

        while True:
            y = int(
                self.console.input(
                    "[magenta]🎨 Enter the y value for the board (4, 6, 8, 10, 12): [/magenta]"
                )
            )
            if y in X_Y_BOARD_CHOICES:
                break
            else:
                self.console.print(
                    "[red]❌ Invalid choice. Please select a number from the list.[/red]"
                )

        return x, y
