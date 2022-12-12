with open('input.txt') as file:
    data = file.read().split('\n\n')

monkeys = []

class Monkey:
    mod_base = 1

    def __init__(self, data):
        data = data.split('\n')
        self.id = int(data[0][7:-1])
        self.items = [int(x) for x in data[1][18:].strip().split(',')]
        self.op = operation(data[2][19:])
        self.test_val = int(data[3][21:])
        Monkey.mod_base *= self.test_val
        self.if_true = int(data[4][29:])
        self.if_false = int(data[5][30:])

        self.num_inspections = 0

    def inspect(self):
        global monkeys
        item = self.items[0]
        item = self.op(item) % Monkey.mod_base
        # item //= 3
        if item % self.test_val == 0:
            pass_to = self.if_true
        else:
            pass_to = self.if_false
        monkeys[pass_to].items.append(item)
        self.items.pop(0)
        self.num_inspections += 1
    
    def __gt__(self, other):
        return self.num_inspections < other.num_inspections

def operation(data):
    def func(old):
        operand = data[6:]
        if operand == 'old':
            operand = old
        else:
            operand = int(operand)
        
        operator = data[4]
        if operator == '+':
            return old + operand
        elif operator == '*':
            return old * operand

    return func

def round():
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.inspect()

# Parse the input
for m in data:
    monkeys.append(Monkey(m))

# Perform 10000 rounds
for _ in range(10000):
    round()

# Find the 2 most active monkeys
monkeys.sort()
for m in monkeys:
    print(f'Monkey {m.id} inspected {m.num_inspections} times')
monkey_business = monkeys[0].num_inspections * monkeys[1].num_inspections
print('Level of monkey business:', monkey_business)