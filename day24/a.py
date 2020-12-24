from collections import defaultdict, deque
M = defaultdict(lambda: False)
# Black = True, White = False
dirs = {'e':(2,0), 'ne': (1,1), 'nw': (-1,1), 'w': (-2,0), 'sw': (-1,-1), 'se': (1,-1)}
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
        M[(x, y)] = not M[(x, y)]

print(list(M.values()).count(True))