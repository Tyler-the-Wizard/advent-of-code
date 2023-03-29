import re

bag_pattern = re.compile(r'^(.+) bags contain (.+)\.$')
contain_pattern = re.compile(r'^(\d+) (.+) bag[s]?$')

class Bag:
    index = {}

    def __init__(self, line):
        match = bag_pattern.match(line)
        if match is None:
            print(f"Unable to parse data '{line}'")
            return
        
        self.color = match.group(1)
        contains = match.group(2)

        __class__.index[self.color] = self

        self.children = []

        if contains == 'no other bags':
            return
        
        for bag in contains.split(', '):
            match = contain_pattern.match(bag)            
            if match is None:
                print(f"Unable to parse bag '{bag}'")
                continue

            num = int(match.group(1))
            color = match.group(2)

            self.children.append((color, num))
    
    def search(self, color_name):
        if color_name in [c[0] for c in self.children]:
            return True

        for child_col, _ in self.children:
            child = __class__.index[child_col]
            if child.search(color_name):
                return True

        return False
    
    @classmethod
    def count(cls, color_name):
        bag = cls.index[color_name]
        total = sum([c[1] for c in bag.children])

        for child_col, amount in bag.children:
            total += amount * cls.count(child_col)
        
        return total


with open('input.txt') as file:
    data = file.readlines()

for line in data:
    Bag(line)

# Part 1
num_valid = 0
for color, bag in Bag.index.items():
    if bag.search('shiny gold'):
        num_valid += 1

print('part 1:', num_valid)

# Part 2
print('part 2:', Bag.count('shiny gold'))
