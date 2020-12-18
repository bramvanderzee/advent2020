from collections import defaultdict

def to_ddict(cubes):
    dict_ = defaultdict(lambda: '.')
    for iz,z in enumerate(cubes):
        for iy,y in enumerate(z):
            for ix,x in enumerate(y):
                dict_[(ix, iy, iz)] = x
    return dict_

def get_num_nearby_expanding(cubes: dict, coord):
    num = 0
    x, y, z = coord
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if not (dx == 0 and dy == 0 and dz == 0):
                    c_coord = (x+dx, y+dy, z+dz)
                    c = cubes.get(c_coord)
                    if c == '#':
                        num += 1
    return num

def expand(cubes: dict):
    new_cubes = {}
    for k in cubes.keys():
        x, y, z = k
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0 and dz == 0):
                        c_coord = (x+dx, y+dy, z+dz)
                        c = cubes.get(c_coord)
                        if c == None:
                            new_cubes[c_coord] = '.'
    return new_cubes

def do_cycle(cubes: dict):
    new_cubes = defaultdict(lambda: '.')
    cubes.update(expand(cubes))
    for k in cubes.keys():
        num = get_num_nearby_expanding(cubes,k)
        v = cubes[k]
        if v == '#':
            if 2 <= num <= 3:
                new_cubes[k] = '#'
            else:
                new_cubes[k] = '.'
        elif v == '.':
            if num == 3:
                new_cubes[k] = '#'
            else:
                new_cubes[k] = '.'
    return new_cubes

def count_active() -> int:
    num = list(C.values()).count('#')
    return num

cubelist = []
with open('input.txt') as f:
    y = []
    for x in f:
        y.append([c for c in x.strip()])
    cubelist.append(y)

C = to_ddict(cubelist)
print(list(C.values()))
for cycle in range(6):
    C = do_cycle(C)
    print('#',end='')
print()
print(count_active())