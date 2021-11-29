from random import random, choice
from time import sleep

try:    
    from config import *
  
except ImportError:
    open('config.py', 'w').write('''
from os import get_terminal_size

LENGTH, HEIGHT = get_terminal_size()

SPEED = 90  # FPS
ALPHABET = list('+--aaa@@@')  # in the terminal in the opposite direction
COUNT_OF_DROPS = 0.1  # float between 0 and 1

# WINDOWS ONLY
TEXT_COLOR = '3'
BACK_COLOR = '0'
''')

try:
    from os import system
    system(f'color {BACK_COLOR}{TEXT_COLOR}')

except OSError:
    pass


class Drop:
    def __init__(self, pos: int, alphabet: list):
        self.pos = pos
        self.alphabet = alphabet

    def move_down(self):
        self.pos += LENGTH

        if self.pos >= LENGTH * HEIGHT:
            self.alphabet.remove(self.alphabet[-1])
            self.pos -= LENGTH

            if len(self.alphabet) == 0:
                self.delete_drop()

        self.print_drop()

    def delete_drop(self):
        drops[drops.index(self)] = None

    @staticmethod
    def new_drop():
        if random() < COUNT_OF_DROPS:
            drops.append(Drop(choice(all_x), ALPHABET.copy()))

    def print_drop(self):
        count = 0
        for i in range(len(self.alphabet) - 1, -1, -1):
            if self.pos - LENGTH * count < 0:
                break

            picture[self.pos - count * LENGTH] = ALPHABET[i]
            count += 1

        picture[self.pos - count * LENGTH] = ' '


drops = list()
all_x = [i for i in range(LENGTH)]
picture = list(' ' * LENGTH * HEIGHT)

while True:
    Drop.new_drop()

    for drop in drops:
        drop.move_down()

    screen = ''
    for _ in picture:
        screen += _

    print(screen, end='')

    sleep(1 / SPEED)

    for i in range(len(drops) - 1, -1, -1):
        if drops[i] is None:
            drops.pop(i)
