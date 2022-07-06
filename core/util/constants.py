import pathlib
import os


def is_operator(char):
    return char in OPERATIONS.keys()


PATH = pathlib.Path(os.getcwd()).absolute()

EMPTY_STR = ""
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = ''.join(str(i) for i in range(0, 10))  # '0123456789'
LEFT_PAREN = '('
RIGHT_PAREN = ')'

OPERATIONS = {
    "+": 1,
    "-": 2,
    "*": 3,
    "/": 4,
}

PRECEDENCE = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}

