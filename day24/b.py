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
for day in range(1, 101):
    new_M = defaultdict(lambda: False)
    # find adjacents
    for x, y in list(M.keys()):
        num = 0
        for dx, dy in dirs.values():
            if M[(x+dx,y+dy)] == True:
                num += 1
        if M[(x, y)] == True and (num == 0 or num > 2):
            new_M[(x,y)] = False
        elif M[(x, y)] == False and num == 2:
            new_M[(x, y)] = True
    for k,v in new_M.items():
        M[k] = v
    print('Day', day, list(M.values()).count(True))