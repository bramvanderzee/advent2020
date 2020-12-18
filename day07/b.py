def find_parent_bags(bags: dict, bag_name: str) -> set:
    containers = set()
    for key, val in bags.items():
        if bag_name in val.keys():
            containers.add(key)
    return containers

lines = []
with open('input_a.txt') as f:
    for x in f:
        lines.append(x.strip())


bags = {}
for line in lines:
    big_bag, other = line.split(' contain ')
    desc, col, _ = big_bag.split(' ')
    key = desc + '_' + col
    small_bags = other.split(', ')
    small_bags_list = {}
    for bag in small_bags:
        num, other = bag.split(' ', 1)
        if num == 'no':
            break
        desc, col, _ = other.split(' ')
        small_bags_list[desc + '_' + col] = int(num)
    
    bags[key] = small_bags_list.copy()

containers = []
working_list = ['shiny_gold'] 
while not len(working_list) == 0:
    cur = working_list.pop()
    res = bags[cur]
    for key, val in res.items():
        for _ in range(val):
            containers.append(key)
            working_list.append(key)

print(len(containers))