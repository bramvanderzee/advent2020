groups = []
cur_group = set()

with open('input_a.txt') as f:
    for x in f:
        line = x.strip()
        if len(line) < 1:
            groups.append(cur_group.copy())
            cur_group.clear()
        else:
            for c in line:
                cur_group.add(c)

count = 0
for g in groups:
    count += len(g)

print(count)