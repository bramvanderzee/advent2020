CUPS = []
with open('input_ex.txt') as f:
    CUPS = [int(x) for x in f.readline().strip()]

MIN = min(CUPS)
MAX = max(CUPS)

def do_move(index: int) -> list:
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

def print_cups() -> None:
    index = CUPS.index(1)
    new_list = [str(x) for x in CUPS[index+1:]]
    new_list.extend([str(x) for x in CUPS[:index]])
    print(''.join(new_list))

cur_cup_i = 0
for move in range(1, 101):
    prev = CUPS[cur_cup_i]
    do_move(cur_cup_i)
    cur_cup_i = (CUPS.index(prev)+1)%len(CUPS)

print_cups()