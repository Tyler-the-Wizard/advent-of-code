with open('input.txt') as file:
    data = [int(x) for x in file.readlines() if len(x.strip())]

PREAMBLE_LEN = 25

def is_sum_of_2(num, sublist):
    for x in sublist:
        if num - x in sublist:
            return True
    return False

# Part 1
i = PREAMBLE_LEN
while is_sum_of_2(data[i], data[i-PREAMBLE_LEN:i]):
    i += 1

invalid_number = data[i]

print('(part 1) num:', invalid_number)
