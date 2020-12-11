def find_num_paths(adapters: list, index: int) -> int:
    depth = 3
    if index + depth > len(adapters) - 1:
        depth = len(adapters) - 1 - index
    cur_adapter = adapters[index]
    for i in range(depth, 0, -1):
        if adapters[index + i] - cur_adapter <= 3:
            return i
    return 1

vals = []
with open('input_a.txt') as f:
    for x in f:
        vals.append(int(x.strip()))

starting_jolts = 0
jolts_needed = max(vals) + 3
vals.extend([starting_jolts, jolts_needed])
sorted_vals = sorted(vals)

num_paths = [1] + [0] * (len(sorted_vals) - 1)
for index, item in enumerate(sorted_vals):
    depth = 3
    if index + depth > len(sorted_vals) - 1:
        depth = len(sorted_vals) - 1 - index
    for i in range(depth, 0, -1):
        if sorted_vals[index + i] - item <= 3:
            num_paths[index + i] += num_paths[index]

print(num_paths[-1])