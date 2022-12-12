with open('input.txt') as file:
    data = file.readlines()
data = [[ord(ch) for ch in line] for line in data if len(line) > 0]

rows = len(data)
cols = len(data[0])

visited = []

# Pull out S and E
for r in range(rows):
    for c in range(cols):
        if data[r][c] == ord('S'):
            start_pos = (r, c)
            data[r][c] = ord('a')
        elif dara[r][c] == ord('E'):
            end_pos = (r, c)
            data[r][c] = ord('z')

# Find the shortest path
steps = 0
cur_pos = start_pos
stack = [start_pos]
path_lengths = []
while len(visited) > rows * cols:
    r, c = cur_pos
    cur_point = data[r][c]

    if cur_pos == end_pos:
        path_lengths.append()

    # Aggregate the possible next points
    if r > 0 and test_pos(r-1, c):
        continue
    elif r < rows - 1 and test_pos(r+1, c):
        continue
    elif c > 0 and test_pos(r, c-1):
        continue
    elif c < cols - 1 and test_pos(r, c+1):
        continue
    else:
        # Time to pop from the stack
        stack.pop()
        cur_pos = stack[-1]
        steps -= 1

def test_pos(r, c):
    # Probably not the best way to do this?
    global data
    global visited
    global stack
    global cur_pos
    global cur_point
    next_pos = (r, c)
    next_point = data[r, c]
    if next_point <= cur_point + 1 and next_pos not in visited:
        stack.append(next_point)
        visited.append(next_point)
        steps += 1
        cur_pos = next_pos
        return True
    return False