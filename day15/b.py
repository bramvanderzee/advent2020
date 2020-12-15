ex = [0,3,6]
nums = [int(x) for x in open('input.txt').readline().strip().split(',')]
prev_spoken = {}

for i, n in enumerate(nums[:-1]):
    prev_spoken[n] = i + 1

turn = len(nums)
index = len(nums)-1
P = -1
for _ in range(30000000-len(nums)):
    turn += 1
    prev = nums[index]
    nums.remove(nums[index-2])
    if prev in prev_spoken.keys():
        prev_prev = prev_spoken[prev]
        diff = (turn-1-prev_prev) if P != prev else 1
        nums.append(diff)
    else:
        nums.append(0)
    prev_spoken[prev] = turn-1
    print(turn, prev, nums[-1])
    P = prev
print(nums[-1])
