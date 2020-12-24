from collections import defaultdict, deque
MAP = defaultdict(lambda: False)
# Black = True, White = False
dirs = {'e': (2,0), 'ne': (1,1), 'nw': (-1,1), 'w': (-2,0), 'sw': (-1,-1), 'se': (1,-1)}
with open('input_ex.txt') as f:
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

print(list(MAP.values()).count(True))
for day in range(100):
    new_map = {}
    nums = defaultdict(int)

    for key in list(MAP.keys()):
        nums[key] = 0
        for dx, dy in dirs.values():
            x, y = key
            if MAP[(x+dx,y+dy)] == True:
                nums[key] += 1

    to_check = deque([x for x in MAP.keys()])
    while len(to_check) > 0:
        key = to_check.popleft()
        if MAP[key] == True and (nums[key] == 0 or nums[key] > 2):
            new_map[key] = False
        elif MAP[key] == False and nums[key] == 2:
            new_map[key] = True
    for key,value in new_map.items():
        MAP[key] = value 
    print(day+1, list(MAP.values()).count(True))