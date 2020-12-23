cups = []
with open('input_ex.txt') as f:
    cups = [int(x) for x in f.readline().strip()]

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

def print_cups(cups: list) -> None:
    index = cups.index(1)
    new_list = [str(x) for x in cups[index+1:]]
    new_list.extend([str(x) for x in cups[:index]])
    print(''.join(new_list))

cur_cup_i = 0
for move in range(1, 101):
    prev = cups[cur_cup_i]
    cups = do_move(cups, cur_cup_i)
    cur_cup_i = (cups.index(prev)+1)%len(cups)

print_cups(cups)