import sys
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.prompt import Prompt
from constants import *
from ship import *
from person import *

# the eventual goal is to create a game that is similar to Oregon Trail
# I used Gemini to see the basics of what might be a general path; answer is below

# The Core (Hours 1–15): Build a text-based loop where you command a ship. 
# Program basic systems: fuel management, hull integrity, and a crew roster (dictionaries inside lists). 
# Implement random text encounters using the random module (e.g., "You encounter a space anomaly. Do you risk shielding to study it?").

# The Stretch (Hours 16–30): Add a turn-based combat system using bitwise flags or state machines for status effects 
# (e.g., EMP disabled shields, plasma fire deals damage over time). Write a save/load system 
# using Python's json or pickle modules so you can resume your voyage.

# The Polish (Hours 31–40): Use the argparse module to let users launch the game 
# with specific custom parameters via the command line (e.g., --difficulty hard --ship dreadnought). 
# Clean up the interface using basic ANSI escape codes for colored text.


#upon creating a new game, we need to initialize the crew (minimum 1 - captain)
def main(): 
    game_ship = Ship(new_crew())
    console = Console(style = "white on black", width=80, height=24)
    game_running = True
    layout = Layout()
    layout.split_column(
        Layout(name = "game_view", ratio=1),
        Layout(name = "input_buffer", size=3)
    )

    layout["game_view"].split_column(
        Layout(name="upper", ratio=1),
        Layout(name="lower", ratio=1)
    )

    layout["upper"].split_row(
        Layout(Panel(str(game_ship), title="Ship Statistics"), name = "upperleft"),
        Layout(Panel("Map goes here?", title="Navigation"), name = "upperright")
    )
    with console.screen() as screen:
        while game_running:
            console.clear()
            console.print(layout)
            action = Prompt.ask("What is your command Captain?")
            if action.lower() == "quit":
                break
#use rich.layout to create boxes and only update each part as needed


if __name__ == "__main__":
    main()