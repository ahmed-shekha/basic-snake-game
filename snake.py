import tkinter
import random

ROWS = 25
COLUMNS = 25
TILE_SIZE = 25

WINDOW_WIDTH =  TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLUMNS

#game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

window.mainloop()



