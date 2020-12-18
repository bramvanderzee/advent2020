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

max_seat_id = 0
for pos in positions:
    s_id = get_seat_id(get_coord(pos))
    if s_id > max_seat_id:
        max_seat_id = s_id


print(max_seat_id)