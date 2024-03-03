from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=160, height=180)  # Изменил размер Canvas
tk.resizable(0, 0)
tk.title("Компьютер 16 бит на Python")
canvas.pack()

bit_map = [0] * 16  # Инициализация 16 нулями


class Bit:
    def __init__(self, index, row, col):
        self.index = index
        self.row = row
        self.col = col
        self.rect = canvas.create_rectangle(
            col, row, col + 20, row + 20, fill="white", tags=f"rectangle_tag_{index}"
        )

    def update(self):
        canvas.delete(f"rectangle_tag_{self.index}")
        fill_color = "black" if bit_map[self.index] == 1 else "white"
        self.rect = canvas.create_rectangle(
            self.col,
            self.row,
            self.col + 20,
            self.row + 20,
            fill=fill_color,
            tags=f"rectangle_tag_{self.index}",
        )


def update_visual():
    # Обновляем визуальное представление
    for bit in bits:
        bit.update()

    # Проверяем первый бит и освещаем квадратик
    if bit_map[0] == 1:
        bits[0].rect = canvas.create_rectangle(
            bits[0].col,
            bits[0].row,
            bits[0].col + 20,
            bits[0].row + 20,
            fill="black",
            tags=f"rectangle_tag_{0}",
        )


bits = []

# Создание 16 битов
for i in range(16):
    row = i // 4 * 20
    col = i % 4 * 20
    bit = Bit(i, row, col)
    bits.append(bit)

# Строка ввода
entry_text = StringVar()
entry = Entry(tk, textvariable=entry_text, width=16)  # Изменил ширину Entry на 16
entry.pack()


def on_entry_change(event):
    try:
        # Получаем введенное значение
        input_value = entry_text.get()

        # Проверяем, что введено не более 16 символов
        if len(input_value) > 16:
            entry_text.set(input_value[:16])  # Обрезаем строку до первых 16 символов

        # Обновляем bit_map в соответствии с введенными значениями
        input_value = int(entry_text.get(), 2)
        for i in range(16):
            bit_map[i] = (input_value >> (15 - i)) & 1

        # Обновляем визуальное представление
        update_visual()
    except ValueError:  
        pass


entry.bind("<KeyRelease>", on_entry_change)

tk.mainloop()
