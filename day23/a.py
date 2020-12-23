cups = []
with open('input.txt') as f:
    cups = [int(x) for x in f.readline().strip()]

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

def print_cups(cups: list) -> None:
    index = cups.index(1)
    new_list = [str(x) for x in cups[index+1:]]
    new_list.extend([str(x) for x in cups[:index]])
    print(''.join(new_list))

cur_cup_i = 0
for move in range(1, 101):
    prev = cups[cur_cup_i]
    cups = do_move(cups, cur_cup_i)
    cur_cup_i = cups.index(prev)
    cur_cup_i += 1
    cur_cup_i = cur_cup_i%len(cups)

print_cups(cups)