from random import random, choice
from time import sleep

try:
    from config import *
    
    if not (check1 and check2):
        raise NameError

except (ImportError, NameError, SyntaxError):
    from new_config import new_config
    
    new_config(bool(int(input('config file not found or damaged!\nI will create another one for you\nWould you like to write down all the parameters yourself?\n1 - I can write all parameters myself\n0 - do it without me\n'))))

finally:
    from config import *


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
