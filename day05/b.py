max_row_index = 127
max_col_index = 7

def get_coord(position):
    rows, cols = position
    min_row, max_row = 0, max_row_index
    min_col, max_col = 0, max_col_index
    for row in rows:
        up = True if row == 'B' else False
        min_row, max_row = get_range(min_row, max_row, up)
    for col in cols:
        up = True if col == 'R' else False
        min_col, max_col = get_range(min_col, max_col, up)

    return (min_row, min_col)

def get_range(mini, maxi, up):
    middle = ((maxi-mini)//2)+mini
    if up:
        return (middle+1, maxi)
    else:
        return (mini, middle)

def get_seat_id(coord):
    x, y = coord
    return ((x * 8) + y)

positions = []

with open('input_a.txt') as f:
    for x in f:
        line = x.strip()
        row_id = line[:-3]
        col_id = line[-3:]
        positions.append((row_id, col_id))

missing_seats = []
boarded_seats = []
# excluding front and back seats
for x in range(1, max_row_index):
    for y in range(max_col_index+1): 
        missing_seats.append((x, y, get_seat_id((x, y))))

# remove all boarded passes
for pos in positions:
    x, y = get_coord(pos)
    s_id = get_seat_id((x, y))
    boarded_seats.append((x, y, s_id))
    try:
        missing_seats.remove((x, y, s_id))
    except:
        pass

for seat in missing_seats:
    x, y, seat_id = seat
    if len([f[2] for f in boarded_seats if f[2] == (seat_id - 1) or f[2] == (seat_id + 1)]) == 2:
        print(seat)

