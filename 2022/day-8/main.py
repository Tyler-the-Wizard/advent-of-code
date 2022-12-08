with open('input.txt') as file:
    data = [line for line in file.readlines() if len(line) > 0]

# Part 1
# assume the data is always 99x99
visible = []
for r in range(99):
    visible.append([False] * 99)

def check_tree(r, c, height):
    tree = int(data[r][c])
    if tree > height:
        visible[r][c] = True
        height = tree
    return height

# go from the left
for r in range(99):
    height = -1
    for c in range(99):
        height = check_tree(r, c, height)

# go from the right
for r in range(99):
    height = -1
    for c in reversed(range(99)):
        height = check_tree(r, c, height)

# go from the top
for c in range(99):
    height = -1
    for r in range(99):
        height = check_tree(r, c, height)

# go from the bottom
for c in range(99):
    height = -1
    for r in reversed(range(99)):
        height = check_tree(r, c, height)

# sum all trees that are visible
num_visible = 0
for row in visible:
    num_visible += len([v for v in row if v])
print('(Part 1) Total visible trees:', num_visible)

# Part 2
def calc_scenic_score(r, c):
    tree = int(data[r][c])

    u = 0
    tmp_r = r - 1
    while tmp_r >= 0:
        u += 1
        if int(data[tmp_r][c]) >= tree:
            break
        tmp_r -= 1

    l = 0
    tmp_c = c - 1
    while tmp_c >= 0:
        l += 1
        if int(data[r][tmp_c]) >= tree:
            break
        tmp_c -= 1

    d = 0
    tmp_r = r + 1
    while tmp_r < 99:
        d += 1
        if int(data[tmp_r][c]) >= tree:
            break
        tmp_r += 1

    ri = 0
    tmp_c = c + 1
    while tmp_c < 99:
        ri += 1
        if int(data[r][tmp_c]) >= tree:
            break
        tmp_c += 1

    return u * l * d * ri

max_score = 0
for r in range(99):
    for c in range(99):
        score = calc_scenic_score(r, c)
        if score > max_score:
            max_score = score
print('Highest scenic score:', max_score)
