import re
keys_to_contain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def check_passport(psp: dict, required_keys: list):
    for key in required_keys:
        if not key in psp:
            return False

    if int(psp['byr']) < 1920 or int(psp['byr']) > 2002:
        return False
    if int(psp['iyr']) < 2010 or int(psp['iyr']) > 2020:
        return False
    if int(psp['eyr']) < 2020 or int(psp['eyr']) > 2030:
        return False
    if psp['hgt'][-2:] == 'cm':
        hgt = int(psp['hgt'][:-2])
        if hgt < 150 or hgt > 193:
            return False
    elif psp['hgt'][-2:] == 'in':
        hgt = int(psp['hgt'][:-2])
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False
    if not re.match("^#[a-f0-9]{6}$", psp['hcl']):
        return False
    if not psp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match("^[0-9]{9}$", psp['pid']):
        return False

    return True

raw_lines = []

with open('input_a.txt') as f:
    for x in f:
        raw_lines.append(x.strip())

passports = []
psp = {}
for line in raw_lines:
    if len(line) < 1:
        passports.append({key:psp[key] for key in sorted(psp)})
        psp = {}
    else:
        keyvals = line.split(' ')
        for keyval in keyvals:
            (key, val) = keyval.split(':')
            if not key == "cid":
                psp[key] = val

num_valid = 0
for psp in passports:
    if check_passport(psp, keys_to_contain):
        num_valid += 1
        print(psp)

print(num_valid)