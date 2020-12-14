ts = 0
busses = {}

with open('input_ex.txt') as f:
    _ = int(f.readline().strip())
    tmp = [x for x in f.readline().strip().split(',')]
    to_check = tmp[0]
    for bus in tmp:
        if bus != 'x':
            busses[bus] = ts

print(busses)
to_find = list(busses.keys())
to_check_ts = 0

while len(to_find) > 0:
    ts += 1

print(ts)