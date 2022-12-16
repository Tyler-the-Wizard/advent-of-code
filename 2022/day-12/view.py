with open('input.txt') as file:
    data = file.readlines()

import os
os.system('color')

def colorize_char(ch):
    i = (ord(ch) - ord('a')) % 8
    return f'\33[4{i}m{ch}\33[0m'

def colorize(s):
    return ''.join(colorize_char(c) for c in s)

for line in data:
    print(colorize(line), end='')
