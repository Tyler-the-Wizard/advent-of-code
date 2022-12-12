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
        elif data[r][c] == ord('E'):
            end_pos = (r, c)
            data[r][c] = ord('z')

def test_pos(cur_point, r, c):
    # Probably not the best way to do this?
    global data
    global visited
    next_pos = (r, c)
    if data[r][c] <= cur_point + 1 and next_pos not in visited:
        visited.append(next_pos)
        return True
    return False

# Find the shortest path
steps = 0
path_lengths = []

def step(cur_pos, steps):
    global path_lengths
    if cur_pos == end_pos:
        path_lengths.append(steps)
    
    r, c = cur_pos
    cur_point = data[r][c]

    # Aggregate the possible next points
    if r > 0 and test_pos(cur_point, r-1, c):
        step((r-1, c), steps+1)
    if r < rows - 1 and test_pos(cur_point, r+1, c):
        step((r+1, c), steps+1)
    if c > 0 and test_pos(cur_point, r, c-1):
        step((r, c-1), steps+1)
    if c < cols - 1 and test_pos(cur_point, r, c+1):
        step((r, c+1), steps+1)

step(start_pos, 0)

print(path_lengths)
print(max(path_lengths))
