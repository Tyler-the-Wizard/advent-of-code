data = ''
with open('input.txt', 'r') as file:
    data = file.read()
data = data.split('\n\n')

import re
pattern = '([^:]+):(.+)'
passports = []
for passport_data in data:
    passport = {}
    for field in passport_data.split():
        matches = re.search(pattern, field)
        if matches:
            passport[matches.group(1)] = matches.group(2)
    passports.append(passport)

fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

def validate(passport):
    '''make this function return True always to get part 1 answer'''
    byr = int(passport['byr'])
    if not (1920 <= byr <= 2002):
        return False
    
    iyr = int(passport['iyr'])
    if not (2010 <= iyr <= 2020):
        return False
    
    eyr = int(passport['eyr'])
    if not (2020 <= eyr <= 2030):
        return False
    
    hgt = passport['hgt']
    if hgt[-2:] == 'cm':
        if not (150 <= int(hgt[:-2]) <= 193):
            return False
    elif hgt[-2:] == 'in':
        if not (59 <= int(hgt[:-2]) <= 76):
            return False
    else:
        return False
    
    hcl = passport['hcl']
    if hcl[0] != '#':
        return False
    if not set(hcl[1:]).issubset(set('0123456789abcdef')):
        return False
    
    ecl = passport['ecl']
    if not (
        ecl == 'amb' or
        ecl == 'blu' or
        ecl == 'brn' or
        ecl == 'gry' or
        ecl == 'grn' or
        ecl == 'hzl' or
        ecl == 'oth'
    ):
        return False
    
    pid = passport['pid']
    if len(pid) != 9:
        return False
    
    return True

valid_passports = 0
for passport in passports:
    for field in fields:
        if field not in passport.keys():
            break
    else:
        if validate(passport):
            valid_passports += 1

print('Number of valid passporrts:', valid_passports)
