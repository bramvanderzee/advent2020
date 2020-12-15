nums = [int(x) for x in open('input.txt').readline().strip().split(',')]
prev_spoken = {}

for i, n in enumerate(nums):
    prev_spoken[n] = i + 1

for turn in range(len(nums) - 1,2021):
    turn_1 = turn + 1
    prev = nums[turn]
    if prev in nums[:-1]:
        prev_prev = prev_spoken[prev]
        nums.append(turn_1-prev_prev)
    else:
        nums.append(0)
    prev_spoken[prev] = turn_1
    if turn_1 == 2020:
        print(turn_1, nums[turn])
