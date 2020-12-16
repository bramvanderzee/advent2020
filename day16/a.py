lines = []
with open('input.txt') as f:
    for x in f:
        lines.append(x.strip())

RULES = {}
yours = []
other = []
i = 0
for line in lines:
    if line == '':
        i += 1
        continue
    elif i == 0:
        name, vals = line.split(': ')
        r1, r2 = vals.split(' or ')
        r1 = [int(x) for x in r1.split('-')]
        r2 = [int(x) for x in r2.split('-')]
        RULES[name] = [r1, r2]
    elif i == 1:
        if line.startswith('your'):
            continue
        yours = [int(x) for x in line.split(',')]
    elif i == 2:
        if line.startswith('nearby'):
            continue
        other.append([int(x) for x in line.split(',')])

def is_valid(ticket):
    valid = True
    for val in ticket:
        lst = [((v[0][0] <= val <= v[0][1]) or (v[1][0] <= val <= v[1][1])) for v in RULES.values()]
        valid = any(lst)
        if not valid:
            return valid
    return valid

def get_invalid(ticket):
    invalid = []
    for val in ticket:
        lst = [((v[0][0] <= val <= v[0][1]) or (v[1][0] <= val <= v[1][1])) for v in RULES.values()]
        valid = any(lst)
        if not valid:
            invalid.append(val)
    return invalid

ans = 0
for ticket in other:
    if not is_valid(ticket):
        ans += sum(get_invalid(ticket))

print(ans)
