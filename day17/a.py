def to_dict(cubes):
    dict_ = {}
    for iz,z in enumerate(cubes):
        for iy,y in enumerate(z):
            for ix,x in enumerate(y):
                dict_[(ix, iy, iz)] = x
    return dict_

def get_num_nearby_expanding(C: dict,coord):
    num = 0
    x, y, z = coord
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if not (dx == 0 and dy == 0 and dz == 0):
                    c = C.get((x+dx, y+dy, z+dz))
                    if c == '#':
                        num += 1
                    elif c == None:
                        C.update({(x+dx, y+dy, z+dz):'.'})
    return C,num

def do_cycle(C: dict):
    new_cubes = {}
    print(len(C.keys()))
    for k in list(C.keys()):
        nC,num = get_num_nearby_expanding(C,k)
        new_cubes.update(nC)
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
print(list(C.values()))
for cycle in range(3):
    C = do_cycle(C)
    print(len(C))

print(count_active())