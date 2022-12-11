with open('input.txt') as file:
    data = file.readlines()
data = [line for line in data if len(line) > 0]

X = 1
cycle = 1
result = 0 # part 1

def clock_cycle():
    global X
    global cycle
    global result
    if (cycle - 20) % 40 == 0:
        result += cycle * X

    # part 2
    if (cycle-1)%40 == 0:
        print()

    if X - 1 <= (cycle-1)%40 + 1 <= X + 1:
        print('#', end='')
    else:
        print('.', end='')
    
    
    cycle += 1

for line in data:
    cmd = line[:4]
    if cmd == 'noop':
        clock_cycle()
    elif cmd == 'addx':
        clock_cycle()
        clock_cycle()
        X += int(line[5:])

# print(result) # part 1
