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
    ans += calculate(line)

print(ans)