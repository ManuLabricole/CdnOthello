from time import sleep
from typing import Dict

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

class TerminalView(View):
    """TerminalView class is responsible for displaying the game to the user and gathering inputs.

    Attributes:
        console (Console): Rich Console object for rendering rich text.
    """

    def __init__(self, debug=True):
        self.console = Console()
        self.debug = debug
        self._emoji_chosen = []
        self.display_introduction()

    def display_introduction(self):
        """Display the introduction of the game with rich formatting and animations."""
        self.console.clear()

        # Title Panel
        title = Text("🎉 Welcome to Reversi! 🎉", style="bold magenta")
        if not self.debug:
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
            self.console.print("[bold green]All set! Let's start the game![/bold green]\n")

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

    # Add other methods as needed
