import json
from collections import deque

lines = [] 
with open('input.txt') as f:
    for op in f:
        op = op.strip()
        op = op.replace(' ', ',')
        op = op.replace('(', '[')
        op = op.replace(')', ']')
        op = op.replace('*', '"*"')
        op = op.replace('+', '"+"')
        op = '[' + op + ']'

        jsonline = json.loads(str(op))
        lines.append(deque(jsonline))

def parse(c: deque) -> deque:
    cur = c.popleft()
    if type(cur) == type([]):
        cur = list(parse(deque(cur)))
    new_sum = [cur]
    while len(c) >= 2:
        op = c.popleft()
        y = c.popleft()
        if type(y) == type([]):
            y = list(parse(deque(y)))
        if op == '+':
            new_sum.append([new_sum.pop(), op, y])
        else:
            new_sum.extend([op, y])
    return deque(new_sum)

def calculate(c: deque) -> int:
    tot = c.popleft()
    if type(tot) == type([]):
        tot = calculate(deque(tot))
    while len(c) >= 2:
        op = c.popleft()
        y = c.popleft()
        if type(y) == type([]):
            y = calculate(deque(y))
        if op == '+':
            tot += y
        elif op == '*':
            tot *= y
        else:
            print(op)
            assert False
    return tot

ans = 0
for line in lines:
    x = calculate(parse(line))
    ans += x 

print(ans)