with open('input.txt') as file:
    data = [line for line in file.readlines() if len(line) > 0]

AIR = 0
ROCK = 1
SAND = 2

# get the minimum and maximum of the data
xs = []
ys = []

for line in data:
    rocks = line.split()
    for rock in rocks:
        if rock == '->': continue
        rock = rock.split(',')
        xs.append(int(rock[0]))
        ys.append(int(rock[1]))

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

def transform(x, y):
    return x - min_x, y - min_y + 1

# build up the grid
size_x = max_x - min_x
size_y = max_y - min_y
grid = []
for _ in range(size_y):
    grid.append([AIR] * size_x)

# draw the rocks onto the grid
#for line in data:
line = data[0]
if True:
    tokens = [token.split(',') for token in line.split() if token != '->']
    points = [(int(token[0]), int(token[1])) for token in tokens]
    for i in range(len(points) - 1):
        point = points[i]
        if i == 0:
            cur_x, cur_y = point

        # draw from the current point to next
        if points[i+1][0] > point[0]:
            dx = 1
        elif points[i+1][0] < point[0]:
            dx = -1
        else:
            dx = 0
        
        if points[i+1][1] > point[1]:
            dy = 1
        elif points[i+1][1] < point[1]:
            dy = -1
        else:
            dy = 0

        # for 
