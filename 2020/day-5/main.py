with open('input.txt') as file:
    data = [line.strip() for line in file.readlines() if len(line.strip())]

def decode(b_pass):
    row = b_pass[:7]
    seat = b_pass[7:]
    
    # Find the row
    lower_limit = 0
    upper_limit = 127

    for c in row:
        if c == 'F':
            upper_limit = lower_limit + (upper_limit - lower_limit) // 2
        else:
            lower_limit = lower_limit + (upper_limit - lower_limit) // 2 + 1
    
    row_num = lower_limit

    # Find the column
    col_dict = {
        'LLL' : 0,
        'LLR' : 1,
        'LRL' : 2,
        'LRR' : 3,
        'RLL' : 4,
        'RLR' : 5,
        'RRL' : 6,
        'RRR' : 7}
    
    col_num = col_dict[seat]

    return (row_num, col_num)

def get_seat_id(tup):
    return tup[0] * 8 + tup[1]

ids = [get_seat_id(decode(line)) for line in data]
ids.sort()

# Part 1
print('max id:', ids[-1])

# Part 2
for i in range(len(ids)):
    if ids[i+1] != ids[i]+1:
        print('my id:', ids[i]+1)
        break
