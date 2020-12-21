import numpy as np
from collections import defaultdict

def rotate(map_: list, num: int) -> list:
    return np.rot90(map_, num)

def flip_hor(map_: list) -> list:
    return np.fliplr(map_)

def flip_ver(map_: list) -> list:
    return np.flipud(map_)

def get_sides(map_: list) -> dict:
    sides = {}
    sides['U'] = ''.join([x for x in map_[0]])
    sides['D'] = ''.join([x for x in map_[-1]])
    sides['L'] = ''.join([y[0] for y in map_])
    sides['R'] = ''.join([y[-1] for y in map_])
    return sides

def check_border(map1: list, map2: list, side: str) -> bool:
    to_match = get_sides(map1)
    to_match = to_match[side]

    for x in range(4):
        sides = list(get_sides(rotate(map2, x)).values())
        if to_match in sides or to_match[::-1] in sides:
            return True
    return False

def check_borders(map1: list, map2: list) -> bool:
    for s in ['U', 'D', 'L', 'R']:
        if check_border(map1, map2, s):
            return True
    return False

maps = {}
cur_id = 0
cur_map = []
next = False
with open('input_ex.txt') as f:
    for x in f:
        x = x.strip()
        if x == '':
            next = True
            continue

        if next:
            maps[cur_id] = np.array(cur_map)
            cur_id = 0
            cur_map = []
            next = False
        
        if x.startswith('Tile '):
            _, t = x.split()
            t = t[:-1]
            cur_id = int(t)
        else:
            cur_map.append([y for y in x])
    maps[cur_id] = np.array(cur_map)

matches = defaultdict(lambda: []) 
ans = 1
for id1,map1 in maps.items():
    for id2, map2 in maps.items():
        if id1 != id2 and check_borders(map1, map2):
            matches[id1].append(id2)
print(dict(matches))

ans = 1
for i in [k for k,v in matches.items() if len(v) == 2]:
    ans *= i
print(ans)
