data = ''
with open('input.txt', 'r') as file:
    data = file.read()

# Part 1
import re
pattern = '([0-9]+)-([0-9]+) (.): (.+)'
class Password:
    def __init__(self, data):
        matches = re.search(pattern, data)
        self.min_char = int(matches.group(1))
        self.max_char = int(matches.group(2))
        self.char     = matches.group(3)
        self.password = matches.group(4)
    
    def is_valid_p1(self):
        count = self.password.count(self.char)
        return self.min_char <= count <= self.max_char

    def is_valid_p2(self):
        char0 = self.password[self.min_char-1]
        char1 = self.password[self.max_char-1]
        return (char0 == self.char) != (char1 == self.char)

passwords = [Password(line) for line in data.split('\n') if len(line) > 0]

print(f'(Part 1) Number of valid passwords: {len([x for x in passwords if x.is_valid_p1()])}')
print(f'(Part 2) Number of valid passwords: {len([x for x in passwords if x.is_valid_p2()])}')