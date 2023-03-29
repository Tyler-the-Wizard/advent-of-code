import copy

with open('input.txt') as file:
    prog = [line.strip() for line in file.readlines() if len(line.strip())]

acc = 0
ip = 0

halted = False

def execute(program):
    global acc
    global ip
    global halted

    if ip >= len(program):
        halted = True
        return

    inst = program[ip]
    arg = int(inst[4:])

    if inst.startswith('jmp'):
        ip += arg
    else:
        if inst.startswith('acc'):
            acc += arg
        
        ip += 1

visited = set()
while ip not in visited:
    visited.add(ip)
    execute(prog)

# Part 1
print('(part 1) acc:', acc)

# Part 2
corrupt = 0
while True:
    # Run the current modified program
    new_prog = copy.deepcopy(prog)

    if new_prog[corrupt].startswith('acc'):
        corrupt += 1
        continue

    elif new_prog[corrupt].startswith('nop'):
        new_prog[corrupt] = 'jmp' + new_prog[corrupt][3:]
    elif new_prog[corrupt].startswith('jmp'):
        new_prog[corrupt] = 'nop' + new_prog[corrupt][3:]
    
    acc = 0
    ip = 0
    visited = set()
    while ip not in visited:
        visited.add(ip)
        execute(new_prog)

    if halted:
        break

    corrupt += 1

print('(part 2) acc:', acc)
