C = {}
def to_dict(cubes):
    dict_ = {}
    for iz,z in enumerate(cubes):
        for iy,y in enumerate(z):
            for ix,x in enumerate(y):
                dict_[(ix, iy, iz)] = x
    return dict_

def get_num_nearby_expanding(coord):
    num = 0
    x, y, z = coord
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                c = C.get((x+dx, y+dy, z+dz))
                if c == '#':
                    num += 1
                elif c == None:
                    C[(x+dx, y+dy, z+dz)] = '.'
    return num

def do_cycle():
    new_cubes = {}
    for k in list(C.keys()):
        num = get_num_nearby_expanding(k)
        v = C[k]
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

cubes = []
with open('input_ex.txt') as f:
    y = []
    for x in f:
        y.append([c for c in x.strip()])
    cubes.append(y)

C = to_dict(cubes)

for cycle in range(6):
    C = do_cycle()
    print(C)

print(count_active())