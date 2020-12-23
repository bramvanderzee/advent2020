CUPS = [] 
with open('input.txt') as f:
    CUPS = [int(x) for x in f.readline().strip()]

from_cup = max(CUPS)+1
CUPS.extend([x+from_cup for x in range(1000000-len(CUPS))])
MIN = min(CUPS)
MAX = max(CUPS)

def do_move(index: int):
    cur_cup = CUPS[index]
    indices = [(index+x)%len(CUPS) for x in range(1,4)]
    picked = [CUPS[x] for x in indices]
    for cup in picked:
        CUPS.remove(cup)
    dest_cup = cur_cup - 1 if not cur_cup == MIN else MAX
    
    while dest_cup in picked:
        dest_cup -= 1
        if dest_cup < MIN:
            dest_cup = MAX
    
    dest_cup_i = CUPS.index(dest_cup) + 1
    for cup in picked[::-1]:
        CUPS.insert(dest_cup_i, cup)

cur_cup_i = 0
for move in range(1, 10000001):
    prev = CUPS[cur_cup_i]
    do_move(cur_cup_i)
    cur_cup_i = (CUPS.index(prev)+1)%len(CUPS)
    if move%10000 == 0:
        print(move)

index1 = CUPS.index(1)
cup1, cup2 = CUPS[(index1+1)%len(CUPS)], CUPS[(index1+2)%len(CUPS)]
ans = cup1 * cup2
print()
print(cup1, cup2)
print(ans)