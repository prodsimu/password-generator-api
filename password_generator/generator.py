from string import ascii_letters, ascii_lowercase
from math import floor
from random import choice, shuffle


class PasswordGenerator:
    def __init__(self, length=12, use_symbols=True, use_uppercase=True):
        self.length = length
        self.use_symbols = use_symbols
        self.use_uppercase = use_uppercase

    def _get_symbols(self):
        safe_symbols = list("!@#$%&*?-_")
        symbols_choice = ""

        if not self.use_symbols:
            return ""

        for _ in range(0, floor(self.length / 2)):
            symbols_choice += choice(safe_symbols)

        return symbols_choice

    def _get_letters(self, symbols_count):
        if self.use_uppercase:
            all_letters = list(ascii_letters)  # a-z + A-Z
        else:
            all_letters = list(ascii_lowercase)  # apenas a-z

        letters_choice = ""

        for _ in range(0, self.length - symbols_count):
            letters_choice += choice(all_letters)

        return letters_choice

    def generate(self):
        symbols_part = self._get_symbols()
        letters_part = self._get_letters(len(symbols_part))

        passwd = list(symbols_part + letters_part)
        shuffle(passwd)

        return "".join(passwd)
