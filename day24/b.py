from collections import defaultdict, deque
M = defaultdict(lambda: False)
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
        M[(x, y)] = not M[(x, y)]

print(list(M.values()).count(True))
for day in range(100):
    new_M = {}
    nums = defaultdict(int)

    for key in list(M.keys()):
        nums[key] = 0
        for dx, dy in dirs.values():
            x, y = key
            if M[(x+dx,y+dy)] == True:
                nums[key] += 1

    to_check = deque([x for x in M.keys()])
    while len(to_check) > 0:
        key = to_check.popleft()
        if M[key] == True and (nums[key] == 0 or nums[key] > 2):
            new_M[key] = False
        elif M[key] == False and nums[key] == 2:
            new_M[key] = True
    for k,v in new_M.items():
        M[k] = v 
    print(day+1, list(M.values()).count(True))