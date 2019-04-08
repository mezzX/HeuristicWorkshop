from tkinter import Label


class Tiles():
    def __init__(self, grid, solver):
        self.tiles = []
        self.grid = grid
        self.solver = solver
        self.gap = None
        self.moves = 0

    def add(self, tile):
        self.tiles.append(tile)

    def shuffle(self, shuffle, seed):
        order = self.solver.shuffle(shuffle, seed)
        i = 0
        for row in range(self.grid):
            for col in range(self.grid):
                self.tiles[order[i] - 1].pos = (row, col)
                i += 1

    def show(self):
        for tile in self.tiles:
            if tile != self.gap:
                tile.show()

    def set_gap(self, index):
        self.gap = self.tiles[index]

    def is_correct(self):
        for tile in self.tiles:
            if not tile.is_correct_pos():
                return False

        return True

    def get_tile(self, *pos):
        for tile in self.tiles:
            if tile.pos == pos:
                return tile

    def get_tiles_by_gap(self):
        gap_r, gap_c = self.gap.pos

        return self.get_tile(gap_r, gap_c-1), self.get_tile(gap_r-1, gap_c), self.get_tile(gap_r, gap_c+1), self.get_tile(gap_r+1, gap_c)

    def move_gap(self, tile):
        try:
            gap_p = self.gap.pos
            self.gap.pos = tile.pos
            tile.pos = gap_p
            self.moves += 1
        except AttributeError:
            pass

    def slide(self, key):
        left, up, right, down = self.get_tiles_by_gap()
        if key == 'Up':
            self.move_gap(down)
        elif key == 'Down':
            self.move_gap(up)
        elif key == 'Right':
            self.move_gap(left)
        elif key == 'Left':
            self.move_gap(right)
        self.show()


class Tile(Label):
    def __init__(self, parent, image, pos):
        Label.__init__(self, parent, image=image)

        self.image = image
        self.pos = pos
        self.cor_pos = pos

    def show(self):
        self.grid(row=self.pos[0], column=self.pos[1])

    def is_correct_pos(self):
        return self.pos == self.cor_pos