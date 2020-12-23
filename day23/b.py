cups = []
with open('input_ex.txt') as f:
    cups = [int(x) for x in f.readline().strip()]

from_cup = max(cups)+1
cups.extend([x+from_cup for x in range(1000000-len(cups))])
MIN = min(cups)
MAX = max(cups)

def do_move(all_cups: list, index: int) -> list:
    cur_cup = all_cups[index]
    indices = [(index+x)%len(all_cups) for x in range(1,4)]
    picked = [all_cups[x] for x in indices]
    for cup in picked:
        all_cups.remove(cup)
    dest_cup = cur_cup - 1 if not cur_cup == MIN else MAX
    
    while dest_cup in picked:
        dest_cup -= 1
        if dest_cup < MIN:
            dest_cup = MAX
    
    dest_cup_i = all_cups.index(dest_cup) + 1
    for cup in picked[::-1]:
        all_cups.insert(dest_cup_i, cup)
    return all_cups 

cur_cup_i = 0
for move in range(1, 10000001):
    prev = cups[cur_cup_i]
    cups = do_move(cups, cur_cup_i)
    cur_cup_i = (cups.index(prev)+1)%len(cups)
    if move%10000 == 0:
        print(move)

index1 = cups.index(1)
cup1, cup2 = cups[(index1+1)%len(cups)], cups[(index1+2)%len(cups)]
ans = cup1 * cup2
print()
print(cup1, cup2)
print(ans)