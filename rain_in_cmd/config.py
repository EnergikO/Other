
check1 = True

from os import get_terminal_size

try:
    LENGTH, HEIGHT = get_terminal_size()

except OSError:
    LENGTH, HEIGHT = 120, 30

SPEED = 110.0  # FPS
ALPHABET = list('..--++@@')  # in the terminal in the opposite direction
COUNT_OF_DROPS = 0.7  # float between 0 and 1

# WINDOWS ONLY
TEXT_COLOR = 3
BACK_COLOR = 0
check2 = True