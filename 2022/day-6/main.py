data = ''
with open('input.txt') as f:
    data = f.read()

NUM_UNIQUE = 14

for i in range(len(data)):
    recent_chars = data[i:i+NUM_UNIQUE]

    # Count unique characters
    if len(set(recent_chars)) == NUM_UNIQUE:
        print(i + NUM_UNIQUE, 'was the first character!')
        break
