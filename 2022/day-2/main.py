data = ''
with open('input.txt', 'r') as file:
    data = file.read()

data = [line for line in data.split('\n') if len(line) > 0]

rps_dict = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
}

score = 0
for line in data:
    opponent_move = rps_dict[line[0]]
    outcome = line[2]

    match outcome:
        case 'X':
            # Need to lose this round
            score += (opponent_move - 1) % 3 + 1
        case 'Y':
            # Need to draw this round
            score += opponent_move + 4
        case 'Z':
            # Need to win this round
            score += (opponent_move + 1) % 3 + 7
        case _:
            print('Unknown condition! Line: ', line)

print('Total score: ', score)
