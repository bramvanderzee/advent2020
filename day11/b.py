def find_num_occ(seats: list, visibility: list) -> int:
    num_occ = 0
    for c in visibility:
        x, y = c
        if seats[y][x] == '#':
            num_occ += 1
    return num_occ

def print_seats(seats: list):
    for y in seats:
        print(*y)
    print()

def find_visible_seats(seats: list, iy: int, ix: int) -> list:
    chairs = []
    for sx in range(-1, 2):
        for sy in range(-1, 2):
            if not (sx == 0 and sy == 0):
                seat = find_single_seat(seats, iy, ix, sy, sx)
                if not seat == None:
                    chairs.append(seat)
    return chairs

def find_single_seat(seats: list, iy: int, ix: int, sy: int, sx: int):
    max_x = len(seats[0]) - 1
    max_y = len(seats) - 1
    cur_x = ix
    cur_y = iy
    looking = True
    while looking:
        cur_x = cur_x + sx
        cur_y = cur_y + sy
        if (0 <= cur_x <= max_x and 0 <= cur_y <= max_y):
            if seats[cur_y][cur_x] in ['L','#']:
                looking = False
                return (cur_x, cur_y)
        else:
            looking = False
            break

current = []
prev = []
with open('input_a.txt') as f:
    for x in f:
        current.append(list(x.strip()))

print('Mapping visibility')
visibility = []
for iy, y in enumerate(current):
    row = []
    for ix, _ in enumerate(y):
        row.append(find_visible_seats(current, iy, ix))
        print('#', end='')
    print()
    visibility.append(row)


print('Looking for stability')
stable = False
while not stable:
    if current == prev:
        stable = True
        break
    prev = list(current) 
    current.clear()
    for iy in range(len(prev)):
        row = []
        for ix in range(len(prev[0])):
            num = find_num_occ(prev, visibility[iy][ix])
            if prev[iy][ix] == 'L' and num == 0:
                row.append('#')
            elif prev[iy][ix] == '#' and num >= 5:
                row.append('L')
            else:
                row.append(prev[iy][ix])
        current.append(row)
            
occ_count = 0
for y in current:
    occ_count += y.count('#')
print(occ_count)