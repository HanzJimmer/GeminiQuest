import pygame
import sys

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