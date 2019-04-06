import pieces
import solver
import time
from PIL import Image, ImageTk
from tkinter import Frame


class Board(Frame):   
    MAX_BOARD_SIZE = 512

    def __init__(self, parent, image, grid, shuffle, win, restart, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.grid = grid
        self.win = win
        self.restart = restart
        self.solver = solver.PuzzleSolver(grid)
        self.image = self.open_image(image)
        self.tile_size = self.image.size[0] / self.grid
        self.tiles = self.create_tiles()
        self.tiles.shuffle(shuffle)
        self.bind_keys()
        self.tiles.show()

    def open_image(self, image):
        image = Image.open(image)
        if min(image.size) > self.MAX_BOARD_SIZE:
            image = image.resize((self.MAX_BOARD_SIZE, self.MAX_BOARD_SIZE), Image.ANTIALIAS)
        if image.size[0] != image.size[1]:
            image = image.crop((0, 0, image.size[0], image.size[0]))

        return image

    def create_tiles(self):
        tiles = pieces.Tiles(self.grid, self.solver)
        for row in range(self.grid):
            for col in range(self.grid):
                x0 = col * self.tile_size
                y0 = row * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size
                tile_image = ImageTk.PhotoImage(self.image.crop((x0, y0, x1, y1)))
                tile = pieces.Tile(self, tile_image, (row, col))
                tiles.add(tile)
        tiles.set_gap(-1)

        return tiles

    def bind_keys(self):
        # Move the piece below the gap up
        self.bind_all('<Key-Up>', self.slide)
        # Move the piece above the gap down
        self.bind_all('<Key-Down>', self.slide)
        # Move the piece to the left of the gap right
        self.bind_all('<Key-Right>', self.slide)
        # Move the piece to the right of the gap left
        self.bind_all('<Key-Left>', self.slide)
        # return to the main screen
        self.bind_all('<Key-r>', self.restart)
        # run solver.py
        self.bind_all('<Key-s>', self.solve)

    def solve(self, event):
        actions = self.solver.solve(self.tiles)
        for action in actions:
            #print(action)
            self.tiles.slide(action)
            self.parent.update()
            time.sleep(0.25)
        if self.tiles.is_correct():
            time.sleep(1.5)
            self.win(self.tiles.moves)

    def slide(self, event):
        self.tiles.slide(event.keysym)
        if self.tiles.is_correct():
            self.win(self.tiles.moves)