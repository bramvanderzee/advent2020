import numpy as np
import math
from collections import defaultdict

sm = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
sm = list([x.replace(' ', '.') for x in sm.split('\n')])
sm_coords = set()
for y, r in enumerate(sm):
    for x, c in enumerate(r):
        if c == '#':
            sm_coords.add((x, y))

def rotate(map_: list, num: int) -> list:
    return np.rot90(map_, num).tolist()

def flip_hor(map_: list) -> list:
    return np.fliplr(map_).tolist()

def flip_ver(map_: list) -> list:
    return np.flipud(map_).tolist()

def get_sides(map_: list) -> dict:
    sides = {}
    sides['U'] = ''.join([x for x in map_[0]])
    sides['D'] = ''.join([x for x in map_[-1]])
    sides['L'] = ''.join([y[0] for y in map_])
    sides['R'] = ''.join([y[-1] for y in map_])
    return sides

def check_border(map1: list, map2: list, side: str):
    to_match = get_sides(map1)
    to_match = to_match[side]
    other_side = 'DRUL'['ULDR'.index(side)]

    for x in range(4):
        rot_map = rotate(map2, x)
        sides = get_sides(rot_map)

        v = sides[other_side]
        if to_match == v:
            return True, rot_map
        elif to_match[::-1] == v:
            if other_side in ['R', 'L']:
                return True, flip_ver(rot_map)
            else:
                return True, flip_hor(rot_map)
    return False

def check_borders(map1: list, map2: list):
    for side in ['U', 'D', 'L', 'R']:
        if check_border(map1, map2, side):
            return True,side
    return False

def find_num_seamonster(map_: list):
    num = 0
    for y,r in enumerate(map_):
        for x,c in enumerate(r):
            check = []
            for dx, dy in sm_coords:
                if x+dx >= len(map_[0]) or y+dy >= len(map_):
                    check.append(False)
                    break
                check.append(map_[y+dy][x+dx] == '#')
            if all(check):
                print(x, y)
                num += 1
    return num

def calc_roughness(map_: list, num_seamonster: int):
    sm_num = len(sm_coords)
    total = sum([x.count('#') for x in map_])
    return total - (sm_num * num_seamonster)

maps = {}
cur_id = 0
cur_map = []
next_ = False
with open('input.txt') as f:
    for x in f:
        x = x.strip()
        if x == '':
            next_ = True
            continue

        if next_:
            maps[cur_id] = np.array(cur_map)
            cur_id = 0
            cur_map = []
            next_ = False
        
        if x.startswith('Tile '):
            _, t = x.split()
            t = t[:-1]
            cur_id = int(t)
        elif x != '':
            cur_map.append([y for y in x])
    maps[cur_id] = np.array(cur_map)

matches = defaultdict(lambda: []) 
for id1,map1 in maps.items():
    for id2, map2 in maps.items():
        if id1 != id2 and check_borders(map1, map2):
            matches[id1].append(id2)

startpoint_id = [k for k,v in matches.items() if len(v) == 2][0]

#orientation of first corner:
found = False
maps[startpoint_id] = flip_hor(maps[startpoint_id])
while not found:
    dirs = []
    maps[startpoint_id] = rotate(maps[startpoint_id], 1)
    for nb in matches[startpoint_id]:
        nb_map = maps[nb]
        _, d = check_borders(maps[startpoint_id], nb_map)
        dirs.append(d)
    if dirs.count('D') > 0 and dirs.count('R') > 0:
        found = True

size = int(math.sqrt(len(matches)))
full_map = []
seen = set()
for y in range(size):
    row = list([[y for y in x[1:-1]] for x in maps[startpoint_id][1:-1]])
    prev_id = startpoint_id
    seen.add(startpoint_id)
    for x in range(size-1):
        matched = {k:maps[k] for k in matches[prev_id]}
        id_to_right = 0
        for k,v in matched.items():
            _, d = check_borders(maps[prev_id], v)
            if d == 'R':
                id_to_right = k
                break
        seen.add(id_to_right)
        _, maps[id_to_right] = check_border(maps[prev_id], maps[id_to_right], 'R')
        prev_id = id_to_right
        for i, r in enumerate(maps[id_to_right][1:-1]):
            row[i].extend(r[1:-1])

    for i, r in enumerate(row):
        full_map.append(r)

    matched = {k:maps[k] for k in matches[startpoint_id] if not k in seen}
    if not len(matched) == 0:
        id_to_bottom = list(matched.keys())[0]
        assert id_to_bottom != 0
        _, maps[id_to_bottom] = check_border(maps[startpoint_id], maps[id_to_bottom], 'D')
        maps[id_to_bottom] = maps[id_to_bottom]
        startpoint_id = id_to_bottom
    else:
        break

for row in full_map:
    print(''.join(row))

# Search sea monsters, rotate/flip if found none
for f in range(4):
    if f in [1, 2]:
        full_map = flip_hor(full_map)
    if f in [2, 3]:
        full_map = flip_ver(full_map)

    for r in range(4):
        full_map = rotate(full_map, r)
        num_sea_monsters = find_num_seamonster(full_map)
        if num_sea_monsters != 0:
            for row in full_map:
                print(''.join(row))
            print(num_sea_monsters)
            print(calc_roughness(full_map, num_sea_monsters))
            break