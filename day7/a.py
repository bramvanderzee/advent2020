lines = []
with open('input_a.txt') as f:
    for x in f:
        lines.append(x.strip())


bags = {}
for line in lines:
    big_bag, other = line.split(' contain ')
    desc, col, _ = big_bag.split(' ')
    key = desc + col
    small_bags = other.split(', ')
    small_bags_list = {}
    for bag in small_bags:
        num, desc, col, _ = bag.split(' ')
        small_bags_list[desc + col] = int(num)
    
    bags[key] = small_bags_list

print(bags)