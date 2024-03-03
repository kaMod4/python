from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=150, height=180)
tk.title("test")
tk.resizable(0, 0)
canvas.pack()

bitmap = [0] * 2
bits = []
x1 = None
y1 = None


class Bit:
    def __init__(self, x1, y1, index):
        self.index = index
        self.x1 = x1
        self.y1 = y1

        self.rect = canvas.create_rectangle(
            tk,
            {x1},
            {x1 + 40},
            {y1},
            {y1 + 40},
            fill="white",
            tags=f"rectangle_tag_{index}",
        )

    def update(self):
        fill_color = "black" if bitmap[self.index] == 1 else "white"
        canvas.delete(f"rectangle_tag_{self.index}")
        self.rect = canvas.create_rectangle(
            tk,
            {x1},
            {x1 + 40},
            {y1},
            {y1 + 40},
            fill="black",
            tags=f"rectangle_tag_{self.index}",
        )



