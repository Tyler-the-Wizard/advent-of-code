with open('input.txt') as file:
    data = file.readlines()
data = [[ord(ch) for ch in line] for line in data if len(line) > 0]

rows = len(data)
cols = len(data[0])

# Pull out S and E
for r in range(rows):
    for c in range(cols):
        if data[r][c] == ord('S'):
            start_pos = (r, c)
            data[r][c] = ord('a')
        elif data[r][c] == ord('E'):
            end_pos = (r, c)
            data[r][c] = ord('z')

from random import choice
LIMIT = 20000
def find_path():
    r, c = start_pos
    num_steps = 0
    while (r, c) != end_pos:
        valid_pos = []
        # up
        if r > 0 and data[r-1][c] <= data[r][c] + 1:
            valid_pos.append((r-1, c))
        # right
        if c < cols - 2 and data[r][c+1] <= data[r][c] + 1:
            valid_pos.append((r, c+1))
        # down
        if r < rows - 2 and data[r+1][c] <= data[r][c] + 1:
            valid_pos.append((r+1, c))
        # left
        if c > 0 and data[r][c-1] <= data[r][c] + 1:
            valid_pos.append((r, c-1))

        r, c = choice(valid_pos)
        num_steps += 1

        if num_steps > LIMIT:
            return -1

    return num_steps

# Find the shortest path
path_lengths = []

for _ in range(100):
    l = find_path()
    if l != -1:
        path_lengths.append(l)

print(path_lengths)
print(min(path_lengths))
