data = ''
with open('input.txt', 'r') as file:
    data = file.read().split('\n')
data = [line for line in data if len(line) > 0]

# Part 1
def calc_priority(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1

    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27

priority_sum = 0

for line in data:
    r0 = line[:len(line)//2]
    r1 = line[len(line)//2:]
    
    for letter in r1:
        if letter in r0:
            priority_sum += calc_priority(letter)
            break

print(f'Sum of priorities (part 1): {priority_sum}')

# Part 2
groups = []
i = 0
while i < len(data):
    groups.append([
        data[i],
        data[i+1],
        data[i+2]])
    i += 3

priority_sum = 0

for group in groups:
    candidates = list(group[0])

    for letter in candidates[:]:
        if letter not in group[1] or letter not in group[2]:
            while letter in candidates:
                candidates.remove(letter)

    priority_sum += calc_priority(candidates[0])

print(f'Sum of priorities (part 2): {priority_sum}')
