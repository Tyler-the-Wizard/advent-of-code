data = ''
with open('input.txt', 'r') as file:
    data = file.read()
data = [int(x) for x in data.split('\n') if len(x) > 0]

# Part 1
for num in data:
    if 2020 - num in data:
        print(f'{num} * {2020 - num} = {num * (2020 - num)}')
        break

# Part 2
for num0 in data:
    sum12 = 2020 - num0
    for num1 in data:
        num2 = sum12 - num1
        if num2 in data:
            print(f'{num0} * {num1} * {num2} = {num0 * num1 * num2}')
            break
    else:
        continue
    break
