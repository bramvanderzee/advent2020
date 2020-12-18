groups = []
cur_group = []
cur_group_count = 0
total_count = 0

with open('input_a.txt') as f:
    for x in f:
        line = x.strip()
        if len(line) < 1:
            total_count += len([x for x in set(cur_group) if cur_group.count(x) == cur_group_count])

            groups.append(cur_group[:])
            cur_group = []
            cur_group_count = 0
        else:
            cur_group_count += 1
            for c in line:
                cur_group.append(c)

print(total_count)