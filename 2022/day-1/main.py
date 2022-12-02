data = ''
with open('input.txt', 'r') as file:
    data = file.read()

calories = []

for elf in data.split('\n\n'):
    foods = [int(x) for x in elf.split('\n') if len(x) > 0]
    calories.append(sum(foods))

calories.sort()

print(sum(calories[-3:]))
