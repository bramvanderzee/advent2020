nums = []
with open('input.txt') as f:
    for x in f:
        nums.append(int(x.strip()))

def transform(sub_num: int, loop_size: int):
    return pow(sub_num, loop_size, 20201227)

card_pub_key = nums[0]
door_pub_key = nums[1]

found = False
loops_card = 0
while not found:
    pub_card = transform(7, loops_card)
    if loops_card%10000 == 0:
        print(loops_card)
    if pub_card == card_pub_key:
        found = True
        break
    loops_card += 1

found = False
loops_door = 0
while not found:
    pub_door = transform(7, loops_door)
    if pub_door == door_pub_key:
        found = True
        break
    loops_door += 1

print(loops_card)
print(loops_door)
enc_key = transform(card_pub_key, loops_door)
enc_key_2 = transform(door_pub_key, loops_card)
assert enc_key == enc_key_2
print(enc_key)