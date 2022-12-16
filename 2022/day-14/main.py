with open('input.txt') as file:
    data = [line for line in file.readlines() if len(line) > 0]

# get the minimum and maximum of the data
xs = []
ys = []

for line in data:
    rocks = line.split()
    for rock in rocks:
        if rock == '->':
            continue
        rock = rock.split(',')
        xs.append(int(rock[0]))
        ys.append(int(rock[1]))

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)
print(min_x, '-', max_x, ';', min_y, '-', max_y)