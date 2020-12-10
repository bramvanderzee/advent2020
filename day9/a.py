def can_find_sum(nums: list, num: int) -> bool:
    for x in nums:
        if (num - x) in nums:
            return True
    return False

lines = []
with open('input_a.txt') as f:
    for x in f:
        lines.append(int(x.strip()))

for pointer in range(25, len(lines)):
    encoders = lines[pointer-25:pointer]
    if not can_find_sum(encoders, lines[pointer]):
        print(lines[pointer])