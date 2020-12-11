def find_num_occ(seats: list, iy: int, ix: int) -> int:
    max_x = len(seats[0]) - 1
    max_y = len(seats) - 1
    num_occ = 0
    start_y, end_y, start_x, end_x = -1, 2, -1, 2
    if seats[iy][ix] == '#':
        num_occ = -1
    if iy == 0:
        start_y = 0
    elif iy == max_y:
        end_y = 1
    if ix == 0:
        start_x = 0
    elif ix == max_x:
        end_x = 1

    for dy in range(start_y, end_y):
        for dx in range(start_x, end_x):
            if seats[iy + dy][ix + dx] == '#':
                num_occ += 1
    return num_occ

def print_seats(seats: list):
    for y in seats:
        print(*y)
    print()

current = []
prev = []
with open('input_a.txt') as f:
    for x in f:
        current.append(list(x.strip()))

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
            num = find_num_occ(prev, iy, ix)
            if prev[iy][ix] == 'L' and num == 0:
                row.append('#')
            elif prev[iy][ix] == '#' and num >= 4:
                row.append('L')
            else:
                row.append(prev[iy][ix])
        current.append(row)
            
occ_count = 0
for y in current:
    occ_count += y.count('#')
print(occ_count)