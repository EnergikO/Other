def new_config(manual_input: bool):  
    speed = 90
    alphabet = '..--++@@'

    count_of_drops = 0.5

    text_color = '3'
    back_color = '0' 

    if manual_input:
        speed = float(input('Input new value of SPEED\n'))
        alphabet = input('Input new ALPHABET (don\'t forget what in the terminal in the opposite direction)\n')
        
        count_of_drops = float(input('Input new value of COUNT_OF_DROPS (float between 0 and 1)\n'))
        
        text_color = input('Input new value of TEXT_COLOR\n')
        back_color = input('Input new value of BACK_COLOR\n')
        
    open('config.py', 'w').write(
f'''
check1 = True

from os import get_terminal_size

try:
    LENGTH, HEIGHT = get_terminal_size()

except OSError:
    LENGTH, HEIGHT = 120, 30

SPEED = {speed}  # FPS
ALPHABET = list('{alphabet}')  # in the terminal in the opposite direction
COUNT_OF_DROPS = {count_of_drops}  # float between 0 and 1

# WINDOWS ONLY
TEXT_COLOR = {text_color}
BACK_COLOR = {back_color}
check2 = True'''
    )
