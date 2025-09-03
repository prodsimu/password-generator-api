# password_generator/generator.py
from string import ascii_letters
from math import floor
from random import choice, shuffle

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def _get_symbols(self):
        safe_symbols = "!@#$%&*?-_"
        return "".join(choice(safe_symbols) for _ in range(floor(self.length / 2)))

    def _get_letters(self):
        all_letters = ascii_letters
        symbols_quantity = len(self._get_symbols())
        return "".join(choice(all_letters) for _ in range(self.length - symbols_quantity))

    def generate(self):
        passwd = list(self._get_symbols() + self._get_letters())
        shuffle(passwd)
        return "".join(passwd)
