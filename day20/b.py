import numpy as np
import math
from collections import defaultdict, deque

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

def check_border(map1: list, map2: list, side: str):
    to_match = get_sides(map1)
    to_match = to_match[side]

    for x in range(4):
        rot_map = rotate(map2, x)
        sides = get_sides(rot_map)
        for k,v in sides.items():
            if to_match in v:
                return True, rot_map
            elif to_match[::-1] in v:
                if k in ['R', 'L']:
                    return True, flip_hor(rot_map)
                else:
                    return True, flip_ver(rot_map)
    return False

def check_borders(map1: list, map2: list):
    for s in ['U', 'D', 'L', 'R']:
        if check_border(map1, map2, s):
            return True,s
    return False

maps = {}
cur_id = 0
cur_map = []
next_ = False
with open('input_ex.txt') as f:
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
while not found:
    dirs = []
    maps[startpoint_id] = rotate(maps[startpoint_id], 1)
    for nb in matches[startpoint_id]:
        nb_map = maps[nb]
        _, d = check_borders(maps[startpoint_id], nb_map)
        dirs.append(d)
    if dirs.count('D') > 0 and dirs.count('R') > 0:
        found = True

print(maps[startpoint_id])
size = int(math.sqrt(len(matches)))
full_map = np.array(np.array([]))
for y in range(size):
    row = np.array(maps[startpoint_id])
    prev_id = startpoint_id
    for x in range(size):
        matched = {k:maps[k] for k in matches[prev_id]}
        id_to_bottom = 0
        for k,v in matched.items():
            _, d = check_borders(maps[prev_id], v)
            if d == 'R':
                id_to_bottom = k
                continue
        map_to_right = maps[id_to_bottom]
        print(map_to_right)
        row = np.append(row, map_to_right, 1)
    full_map = np.append(full_map, row, 0)

    matched = {k:maps[k] for k in matches[startpoint_id]}
    id_to_bottom = 0
    for k,v in matched.items():
        _, d = check_borders(maps[startpoint_id], v)
        if d == 'D':
            id_to_bottom = k
            continue
    startpoint_id = id_to_bottom

print(full_map)