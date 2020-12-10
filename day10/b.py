vals = []
with open('input_ex.txt') as f:
    for x in f:
        vals.append(int(x.strip()))

starting_jolts = 0
jolts_needed = max(vals) + 3
vals.extend([starting_jolts, jolts_needed])
sorted_vals = sorted(vals)
max_jolt_jump = 3

shortest = 0
longest = len(sorted_vals)
print(shortest)
print(longest)