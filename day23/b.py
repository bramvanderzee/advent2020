cups = []
with open('input_ex.txt') as f:
    cups = [int(x) for x in f.readline().strip()]

from_cup = max(cups)+1
cups.extend([x+from_cup for x in range(1000000-len(cups))])

def do_move(all_cups: list, index: int) -> list:
    new_cups = []
    indices = [(index+x)%len(all_cups) for x in range(1,4)]
    picked = [all_cups[x] for x in indices]
    new_cups = [x for x in all_cups if not x in picked]
    cur_cup = all_cups[index]
    dest_cup = cur_cup - 1 if not cur_cup == min(new_cups) else max(all_cups)

    while dest_cup in picked:
        dest_cup -= 1
        if dest_cup < min(new_cups):
            dest_cup = max(new_cups)
    
    dest_cup_i = new_cups.index(dest_cup) + 1
    for cup in picked[::-1]:
        new_cups.insert(dest_cup_i, cup)
    return list(new_cups)

cur_cup_i = 0
progress_markers = [100000*x for x in range(10)]
for move in range(1, 10000001):
    prev = cups[cur_cup_i]
    cups = do_move(cups, cur_cup_i)
    cur_cup_i = cups.index(prev)
    cur_cup_i += 1
    cur_cup_i = cur_cup_i%len(cups)
    if move%1000000 == 0:
        print(move)

index1 = cups.index(1)
cup1, cup2 = cups[(index1+1)%len(cups)], cups[(index1+2)%len(cups)]
ans = cup1 * cup2
print()
print(cup1, cup2)
print(ans)