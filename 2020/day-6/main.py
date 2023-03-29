with open('input.txt') as file:
    data = [group.split() for group in file.read().split('\n\n')]

# Part 1
totals = []
for group in data:
    yes = ''
    group_total = 0
    for person in group:
        for answer in person:
            if answer not in yes:
                yes += answer
                group_total += 1
    
    totals.append(group_total)

print('part 1:', sum(totals))

# Part 2
total = 0
for group in data:
    all_yes = list(group[0])
    for person in group[1:]:
        i = 0
        while i < len(all_yes):
            answer = all_yes[i]
            if answer not in person:
                all_yes.remove(answer)
            else:
                i += 1
    
    total += len(all_yes)

print('part 2:', total)
