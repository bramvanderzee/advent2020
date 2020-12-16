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

def find_valid_locations(res, index_list):
    min1, max1, min2, max2 = res[0][0], res[0][1], res[1][0], res[1][1]
    i = []
    for val in index_list:
        i.append(True if min1 <= val <= max1 or min2 <= val <= max2 else False)
    return i

v_t = [t for t in other if is_valid(t)]
per_index = list(map(list, zip(*v_t)))
rule_pos_index = {rule:set() for rule in RULES.keys()}
key = {}
found = False
while not found:
    for rule, res in RULES.items():
        rule_pos_index = {rule:set() for rule in RULES.keys()}
        if not rule in key.keys():
            for ticketI,index in enumerate(per_index):
                if index != None:
                    if all(find_valid_locations(res, index)):
                        rule_pos_index[rule].add(ticketI)
            if len(rule_pos_index[rule]) == 1:
                key[rule] = list(rule_pos_index[rule])[0]
                per_index[key[rule]] = None
    print('#', end='')
    if len(key) == len(RULES):
        found = True
print()
print(key)
ans = 1
for k,v in key.items():
    if k.startswith('departure'):
        ans *= yours[v]
print(ans)