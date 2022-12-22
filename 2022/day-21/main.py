class Monkey:
    monkeys = {}
    listeners = {}

    def __init__(self, data):
        data = data.split(': ')
        self.name = data[0]
        self.value = data[1]

        if self.value.isnumeric():
            # This monkey knows its value immediately
            self.value = int(self.value)

        Monkey.monkeys[self.name] = self
        self.evaluate()

    def __repr__(self):
        return f'{self.name}: {self.value}'

    def evaluate(self):
        if isinstance(self.value, int):
            # Evaluate all monkeys who are waiting for this monkey
            if self.name in Monkey.listeners.keys():
                for monkey in Monkey.listeners[self.name]:
                    monkey.evaluate()
                # Remove listeners as they are no longer needed
                del Monkey.listeners[self.name]
        else:
            # Calculate own value
            if self.calculate():
                self.evaluate()

    def calculate(self):
        if not isinstance(self.value, str):
            print('Warning:', self.value, 'not string!')

        mon0 = self.value[:4]
        operand = self.value[5]
        mon1 = self.value[-4:]

        mon0_val = None
        mon1_val = None

        if (mon0 in Monkey.monkeys.keys()
        and Monkey.monkeys[mon0].value
        and isinstance(Monkey.monkeys[mon0].value, int)):
            mon0_val = Monkey.monkeys[mon0].value
        if (mon1 in Monkey.monkeys.keys()
        and Monkey.monkeys[mon1].value
        and isinstance(Monkey.monkeys[mon1].value, int)):
            mon1_val = Monkey.monkeys[mon1].value

        if mon0_val and mon1_val:
            if operand == '+':
                self.value = mon0_val + mon1_val
            elif operand == '-':
                self.value = mon0_val - mon1_val
            elif operand == '*':
                self.value = mon0_val * mon1_val
            elif operand == '/':
                self.value = mon0_val // mon1_val

            else:
                print('Unknown operand:', operand)

            return True
        else:
            # Listen for when these monkeys know their values
            if not mon0_val:
                if mon0 in Monkey.listeners.keys():
                    Monkey.listeners[mon0].append(self)
                else:
                    Monkey.listeners[mon0] = [self]
            if not mon1_val:
                if mon1 in Monkey.listeners.keys():
                    Monkey.listeners[mon1].append(self)
                else:
                    Monkey.listeners[mon1] = [self]
            return False

with open('input.txt') as file:
    data = file.readlines()
for line in data:
    Monkey(line.rstrip())
print('Root monkey has value of:', Monkey.monkeys['root'].value)