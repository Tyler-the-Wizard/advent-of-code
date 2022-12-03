data = ''
with open('input.txt', 'r') as file:
    data = file.read()
data = [line for line in data.split('\n') if len(line) > 0]
num_rows = len(data)
num_cols = len(data[0])

def check_slope(dc, dr):
    num_trees = 0
    r = 0
    c = 0
    while r < num_rows:
        if data[r][c % num_cols] == '#':
            num_trees += 1
        r += dr
        c += dc
    return num_trees

# Part 1
num_trees = check_slope(3, 1)
print(f'There are {num_trees} trees in the slope.')

# Part 2
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

slopes = [check_slope(dc, dr) for dc, dr in slopes]
product = 1
for slope in slopes:
    product *= slope
print('Total product:', product)