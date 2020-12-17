def to_dict(cubes):
    dict_ = {}
    for iz,z in enumerate(cubes):
        for iy,y in enumerate(z):
            for ix,x in enumerate(y):
                dict_[(ix, iy, iz)] = x
    return dict_

def get_num_nearby(cubes: dict, coord):
    num = 0
    x, y, z = coord
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if cubes.get((x+dx, y+dy, z+dz)) == '#':
                    num += 1
    return num

def expand_cube(cubes: dict):
    max_

def do_cycle(cubes: dict):
    new_cubes = {}
    for k,v in cubes.items():
        num = get_num_nearby(cubes,k)
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

def count_active(cube_dict: dict) -> int:
    num = list(cube_dict.values()).count('#')
    return num

cubes = []
with open('input_ex.txt') as f:
    y = []
    for x in f:
        y.append([c for c in x.strip()])
    cubes.append(y)

cubes = to_dict(cubes)
print(cubes)
for cycle in range(6):
    cubes = do_cycle(expand_cube(cubes))

print(get_num_nearby(cubes, (2, 2, 0)))
print(count_active(cubes))