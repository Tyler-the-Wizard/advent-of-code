with open('input.txt') as file:
    data = file.read()

# Part 1
CONTINUE = 2
pairs = [pair.split() for pair in data.split('\n\n')]

def compare(item0, item1, i=0):
    # Case 1: both integers
    if isinstance(item0, int) and isinstance(item1, int):
        if item0 == item1:
            return CONTINUE
        else:
            return item0 < item1

    # Case 2: both lists
    if isinstance(item0, list) and isinstance(item1, list):
        # Bounds check
        if i >= len(item0) and i >= len(item1):
            return CONTINUE
        elif i >= len(item0):
            return True
        elif i >= len(item1):
            return False

        rval = CONTINUE
        i = -1
        while rval == CONTINUE and i < len(item0) - 1 and i < len(item1) - 1:
            i += 1
            rval = compare(item0[i], item1[i])
        
        i += 1
        if rval == CONTINUE:
            if i >= len(item0) and i >= len(item1):
                return CONTINUE
            elif i >= len(item0):
                return True
            elif i >= len(item1):
                return False
        
        return rval
    
    # Case 3: mixed
    if isinstance(item0, int) and isinstance(item1, list):
        return compare([item0], item1, i)
    elif isinstance(item0, list) and isinstance(item1, int):
        return compare(item0, [item1], i)

running_sum = 0
import json
for i, pair in enumerate(pairs):
    packet0 = json.loads(pair[0])
    packet1 = json.loads(pair[1])

    if compare(packet0, packet1):
        running_sum += i + 1

print(f'Part 1: {running_sum}')

# Part 2: Sort the packets
div_0 = [[2]]
div_1 = [[6]]

packets = []
for pair in pairs:
    packets.append(json.loads(pair[0]))
    packets.append(json.loads(pair[1]))
packets.append(div_0)
packets.append(div_1)

def make_comparator(func):
    def comparator(x, y):
        if func(x, y): return -1
        else: return 1
    return comparator

from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(make_comparator(compare)))

i_div_0 = packets.index(div_0) + 1
i_div_1 = packets.index(div_1) + 1

print(f'Part 2: {i_div_0} * {i_div_1} = {i_div_0 * i_div_1}')
