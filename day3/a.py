def rep_map(map_, x, y):
    if y >= len(map_):
        return 'X'
    width = len(map_[y])
    corrected_x = x%width
    return map_[y][corrected_x]

def get_num_trees(map_, slope_x, slope_y):
    trees = 0
    bottom = False
    x, y = 0, 0

    while not bottom:
        char = rep_map(map_, x, y)
        if char == 'X':
            bottom = True
            break
        elif char == '#':
            trees += 1
        x += slope_x
        y += slope_y
    return trees

map_ = []

with open('input_a.txt') as f:
    for x in f:
        map_.append(x.strip())

print(get_num_trees(map_, 3, 1))