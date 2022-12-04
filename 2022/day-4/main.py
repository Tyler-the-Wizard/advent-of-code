data = ''
with open('input.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
data = [line for line in data if len(line) > 0]

pattern = '([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'
import re

class Assignment:
    def __init__(self, data):
        matches = re.search(pattern, data)
        self.a0_min = int(matches.group(1))
        self.a0_max = int(matches.group(2))
        self.a1_min = int(matches.group(3))
        self.a1_max = int(matches.group(4))
    
    def __repr__(self):
        return f'{self.a0_min}-{self.a0_max},{self.a1_min}-{self.a1_max}'
    
    def is_complete_overlap(self):
        # Does a0 overlap a1?
        if (self.a0_min <= self.a1_min <= self.a0_max
        and self.a0_min <= self.a1_max <= self.a0_max):
            return True

        # Does a1 overlap a0?
        if (self.a1_min <= self.a0_min <= self.a1_max
        and self.a1_max >= self.a0_max >= self.a1_min):
            return True

        return False
    
    def is_overlap(self):
        if self.a0_max < self.a1_min:
            return False
        if self.a1_max < self.a0_min:
            return False
        
        return True

assignments = [Assignment(line) for line in data]
complete_overlap = [a for a in assignments if a.is_complete_overlap()]

print('Completely overlapping assignments:', len(complete_overlap))

overlap = [a for a in assignments if a.is_overlap()]
print('Overlapping assignments:', len(overlap))