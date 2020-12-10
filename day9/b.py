def can_find_sum(nums: list, num: int) -> bool:
    for x in nums:
        if (num - x) in nums:
            return True
    return False

def find_sum_seq(nums: list, num: int) -> list:
    for seq_size in range(2, len(nums)):
        for pointer in range(seq_size, len(nums)):
            if sum(nums[pointer-seq_size:pointer+1]) == num:
                return nums[pointer-seq_size:pointer+1]

all_nums = []
with open('input_a.txt') as f:
    for x in f:
        all_nums.append(int(x.strip()))

to_find = 0
for pointer in range(25, len(all_nums)):
    encoders = all_nums[pointer-25:pointer]
    if not can_find_sum(encoders, all_nums[pointer]):
        to_find = all_nums[pointer]
        break

num_seq = find_sum_seq(all_nums, to_find)
sum_small_big = min(num_seq) + max(num_seq)
print(sum_small_big)