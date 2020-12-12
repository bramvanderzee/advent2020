import Ship as s

nav = []
with open('input_a.txt') as f:
    for x in f:
        ins = x.strip()
        nav.append((ins[0], int(ins[1:])))

ship = s.Ship(nav)
while ship.has_next():
    ship.next_way()
print(ship.get_manhattan())