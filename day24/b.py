from collections import defaultdict, deque
MAP = defaultdict(lambda: False)
# Black = True, White = False
dirs = {'e': (2,0), 'ne': (1,1), 'nw': (-1,1), 'w': (-2,0), 'sw': (-1,-1), 'se': (1,-1)}
with open('input.txt') as f:
    for x in f:
        x = x.strip()
        route = deque()
        to_parse = deque([c for c in x])
        while len(to_parse) > 0:
            c = to_parse.popleft()
            if c in ['s', 'n']:
                c += to_parse.popleft()
            route.append(c)
        x, y = 0,0
        for direction in route:
            dx, dy = dirs[direction]
            x, y = x+dx, y+dy
        MAP[(x, y)] = not MAP[(x, y)]

def get_num_neighbours(M, coord):
    global dirs
    num = 0
    for dx, dy in dirs.values():
        x, y = coord
        if M[(x+dx,y+dy)] == True:
            num += 1
    return num

print(list(MAP.values()).count(True))
for day in range(100):
    new_map = {}
    nums = {}

    for key in list(MAP.keys()):
        nums[key] = get_num_neighbours(MAP, key)
        for dx, dy in dirs.values():
            x, y = key
            coord = (x+dx, y+dy)
            if not coord in nums.keys():
                nums[coord] = get_num_neighbours(MAP, coord)

    for key in list(nums.keys()):
        if MAP[key] == True and (nums[key] == 0 or nums[key] > 2):
            new_map[key] = False
        elif MAP[key] == False and nums[key] == 2:
            new_map[key] = True
    for key,value in new_map.items():
        MAP[key] = value 
print(list(MAP.values()).count(True))