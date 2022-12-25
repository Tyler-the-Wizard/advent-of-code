with open('input.txt') as file:
    data = file.readlines()
data = [line for line in data if len(line) > 0]

def to_snafu(num):
    result = ''
    while num > 0:
        r = num % 5
        num //= 5
        if r <= 2: result += str(r)
        else:
            num += 1
            if r == 3: result += '='
            elif r == 4: result += '-'
    return result[::-1]

def from_snafu(num):
    length = len(num)
    total = 0
    for i in range(length):
        ch = num[length - i - 1]
        if ch == '2':
            total += 2 * (5 ** i)
        elif ch == '1':
            total += 5 ** i
        elif ch == '-':
            total += -(5 ** i)
        elif ch == '=':
            total += -2 * (5 ** i)

    return total

print(to_snafu(sum([from_snafu(num) for num in data]))[:-1])