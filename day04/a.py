keys_to_contain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def check_passport(passport: dict, required_keys: list):
    for key in required_keys:
        if not key in passport:
            return False
    return True

raw_lines = []

with open('input_a.txt') as f:
    for x in f:
        raw_lines.append(x.strip())

passports = []
passport = {}
for line in raw_lines:
    if len(line) < 1:
        passports.append(passport.copy())
        passport = {}
    else:
        keyvals = line.split(' ')
        for keyval in keyvals:
            (key, val) = keyval.split(':')
            passport[key] = val

num_valid = 0
for passport in passports:
    if check_passport(passport, keys_to_contain):
        num_valid += 1
    else:
        print(passport)

print(num_valid)