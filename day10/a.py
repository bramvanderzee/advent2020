vals = []
with open('input_a.txt') as f:
    for x in f:
        vals.append(int(x.strip()))

starting_jolts = 0
jolts_needed = max(vals) + 3
vals.extend([starting_jolts, jolts_needed])
sorted_vals = sorted(vals)
max_jolt_jump = 3

num_1 = 0
num_3 = 0
for index, val in enumerate(sorted_vals[1:]):
    diff = val - sorted_vals[index]
    print(diff)
    if diff == 1:
        num_1 += 1
    elif diff == 3:
        num_3 += 1

print(num_1*num_3)