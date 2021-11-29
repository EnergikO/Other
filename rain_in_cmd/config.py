from os import get_terminal_size

LENGTH, HEIGHT = get_terminal_size()

SPEED = 90  # FPS
ALPHABET = list('+--aaa@@@')  # in the terminal in the opposite direction
COUNT_OF_DROPS = 0.35  # float between 0 and 1

# WINDOWS ONLY
TEXT_COLOR = '3'
BACK_COLOR = '0'
