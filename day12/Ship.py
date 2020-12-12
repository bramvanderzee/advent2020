class Ship:
    def __init__(self, nav: list):
        self.nav = nav
        self.nav_index = 0
        self.cur_pos = (0, 0)
        self.way_pos = (10, 1)
        self.cur_head = 0
        self.rot_map = 'ENWS'

    def get_position(self):
        return self.cur_pos
    
    def get_manhattan(self) -> int:
        cx, cy = self.cur_pos
        return abs(cx) + abs(cy)

    def has_next(self) -> bool:
        if self.nav_index < len(self.nav):
            return True
        return False

    def next_ship(self):
        action, mod = self.nav[self.nav_index]
        x, y = self.cur_pos
        if action == 'F':
            index = (self.cur_head//90) % 4
            action = self.rot_map[index]
        if action == 'N':
            self.cur_pos = (x, y+mod)
        elif action == 'E':
            self.cur_pos = (x+mod, y)
        elif action == 'S':
            self.cur_pos = (x, y-mod)
        elif action == 'W':
            self.cur_pos = (x-mod, y)
        elif action == 'L':
            self.cur_head += mod
        elif action == 'R':
            self.cur_head -= mod

        self.nav_index += 1

    def next_way(self):
        action, mod = self.nav[self.nav_index]
        sx, sy = self.cur_pos
        wx, wy = self.way_pos
        if action == 'F':
            for _ in range(mod):
                sx, sy = sx+wx, sy+wy
            self.cur_pos = (sx, sy)
        elif action == 'N':
            self.way_pos = (wx, wy+mod)
        elif action == 'E':
            self.way_pos = (wx+mod, wy)
        elif action == 'S':
            self.way_pos = (wx, wy-mod)
        elif action == 'W':
            self.way_pos = (wx-mod, wy)
        elif action == 'L' or action == 'R':
            shift = mod % 360
            if action == 'R':
                shift = -shift
            if shift == 180 or shift == -180:
                self.way_pos = (-wx, -wy)
            elif shift == 90 or shift == -270:
                self.way_pos = (-wy, wx)
            elif shift == -90 or shift == 270:
                self.way_pos = (wy, -wx)
        sx, sy = self.cur_pos
        wx, wy = self.way_pos
        print(action, ' ', mod, ' ', sx, ':', sy, ':',wx,':',wy)
        self.nav_index += 1