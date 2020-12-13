ts = 0
busses = []

with open('input.txt') as f:
    ts = int(f.readline().strip())
    busses = [x for x in f.readline().strip().split(',')]

closest = busses[0]
diff = 0
for bus in busses:
    if not bus == 'x':
        if ts%int(bus) > diff:
            diff = ts%int(bus)
            closest = bus

wait = int(closest)-diff
print(int(closest)*wait)