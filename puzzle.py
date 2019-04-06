from tkinter import filedialog
from tkinter import Label, Frame, Tk, StringVar, IntVar, W
from tkinter.ttk import Entry, Button, OptionMenu
import os
import board


class Puzzle():
    def __init__(self, parent):
        self.parent = parent
        self.image = StringVar()
        self.win_text = StringVar()
        self.grid = IntVar()
        self.shuffle = IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.mainFrame = Frame(self.parent)
        Label(self.mainFrame, text='Sliding Puzzle', font=('',50)).pack(padx=10, pady=10)
        frame = Frame(self.mainFrame)
        # Element for selecting Image for the sliding puzzle
        Label(frame, text='Image').grid(sticky=W)
        Entry(frame, textvariable=self.image, width=50).grid(row=0, column=1, padx=10, pady=10)
        Button(frame, text='Browse', command=self.browse).grid(row=0, column=2, pady=10)
        # Size of the grid for the puzzle. Number of pieces = grid**2
        Label(frame, text='Grid').grid(sticky=W)
        OptionMenu(frame, self.grid, *[3,3,4,5]).grid(row=1, column=1, padx=10, pady=10, sticky=W)
        # Number of random moves generated to shuffle the puzzle
        Label(frame, text='Shuffle').grid(sticky=W)
        OptionMenu(frame, self.shuffle, *[200,100,200,300,400,500]).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        frame.pack()
        Button(self.mainFrame, text='Start', command=self.start).pack(padx=10, pady=10)
        self.mainFrame.pack()
        self.board = Frame(self.parent)
        self.winFrame = Frame(self.parent)
        Label(self.winFrame, textvariable=self.win_text, font=('', 50)).pack(padx=10, pady=10)
        Button(self.winFrame, text='Play Again', command=self.play_again).pack(padx=10, pady=10)

    def start(self):
        image = self.image.get()
        grid = self.grid.get()
        shuffle = self.shuffle.get()
        if os.path.exists(image):
            self.board = board.Board(self.parent, image, grid, shuffle, self.win, self.restart)
            self.mainFrame.pack_forget()
            self.board.pack()

    def restart(self, event):
        self.board.pack_forget()
        self.mainFrame.pack()

    def browse(self):
        self.image.set(filedialog.askopenfilename(title='Select Image', filetypes=(('png File','*.png'),('jpg File','*.jpg'),)))

    def win(self, moves):
        self.board.pack_forget()
        self.win_text.set('Puzzle Solved in {} moves'.format(moves))
        self.winFrame.pack()

    def play_again(self):
        self.winFrame.pack_forget()
        self.mainFrame.pack()


if __name__ == '__main__':
    root = Tk()
    Puzzle(root)
    root.mainloop()