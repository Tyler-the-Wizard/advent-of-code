with open('input.txt') as file:
    data = file.readlines()

# for part 1, set to 2
# for part 2, set to 10
NUM_KNOTS = 10

knots = [(0, 0)] * NUM_KNOTS
t_visited = [(0, 0)]

def dist(p0, p1):
    return max(abs(v1-v0) for v0, v1 in zip(p0, p1))

def move_knot(i):
    global knots
    h = knots[i - 1]
    t = knots[i]

    if dist(knots[i-1], knots[i]) > 1:
        if t[0] < h[0]:
            t = (t[0] + 1, t[1])
        elif t[0] > h[0]:
            t = (t[0] - 1, t[1])

        if t[1] < h[1]:
            t = (t[0], t[1] + 1)
        elif t[1] > h[1]:
            t = (t[0], t[1] - 1)

        if i == NUM_KNOTS - 1:
            if t not in t_visited:
                t_visited.append(t)

        knots[i] = t

for line in data:
    if len(line) == 0:
        continue
    
    num_steps = int(line[2:])
    while num_steps > 0:
        match line[0]:
            case 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            case 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            case 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            case 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])

        # move each next piece of the knot
        for i in range(NUM_KNOTS - 1):
            move_knot(i + 1)

        num_steps -= 1

print(f'Visited {len(t_visited)} unique spots')
