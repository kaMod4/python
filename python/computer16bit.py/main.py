from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=200, height=230)
tk.title("computer 16 bit on python")
tk.resizable(0, 0)
canvas.pack()

bit_map = [0] * 16


class Bit:
    def __init__(self, index, row, col):
        self.index = index
        self.row = row
        self.col = col
        self.rect = canvas.create_rectangle(
            col, row, col + 50, row + 50, fill="white", tags=f"rectangle_tag_{index}"
        )

    def update(self):
        canvas.delete(f"ractangle_tag_{self.index}")
        fill_color = "black" if bit_map[self.index] == 1 else "white"
        self.rect = canvas.create_rectangle(
            self.col,
            self.row,
            self.col + 50,
            self.row + 50,
            fill=fill_color,
            tags=f"rectangle_tag_{self.index}",
        )


def update_visual():
    for bit in bits:
        bit.update()

    if bit_map[0] == 1:
        bits[0].rect = canvas.create_rectangle(
            bits[0].col,
            bits[0].row,
            bits[0].col + 50,
            bits[0].row + 50,
            fill="black",
            tags=f"rectangle_tag_{0}",
        )


bits = []

for i in range(16):
    row = i // 4 * 50
    col = i % 4 * 50
    bit = Bit(i, row, col)
    bits.append(bit)

entry_text = StringVar()
entry = Entry(tk, textvariable=entry_text, width=16)
entry.pack()


def on_entry_change(event):
    try:
        input_value = entry_text.get()

        if len(input_value) > 16:
            entry_text.set(input_value[:16])
        input_value = int(entry_text.get(), 2)
        for i in range(16):
            bit_map[i] = (input_value >> (15 - i)) & 1
        update_visual()

    except ValueError:
        pass


entry.bind("<KeyRelease>", on_entry_change)

tk.mainloop()
