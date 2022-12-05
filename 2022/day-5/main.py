data = ''
with open('input.txt', 'r') as file:
    data = file.read()

# Input Processing
data = data.split('\n\n')
init = data[0].split('\n')
moves = data[1].split('\n')

init.reverse()
num_stacks = int(init[0][-2])

stacks = []
for i in range(num_stacks):
    stacks.append([])

for line in init[1:]:
    for stack_i in range(num_stacks):
        item_i = 1 + 4 * stack_i
        if line[item_i] != ' ':
            stacks[stack_i].append(line[item_i])

# Perform the moves
import re
pattern = 'move ([0-9]+) from ([0-9]+) to ([0-9]+)'
for line in [x for x in moves if len(x) > 0]:
    matches = re.search(pattern, line)
    num_to_move = int(matches.group(1))
    from_stack  = int(matches.group(2)) - 1
    to_stack    = int(matches.group(3)) - 1

    tmp = []
    for _ in range(num_to_move):
        tmp.append(stacks[from_stack].pop())

    while len(tmp) > 0:
        stacks[to_stack].append(tmp.pop())

# Print the output
for stack in stacks:
    print(stack[-1], end='')
print()
