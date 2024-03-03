from tkinter import *

my_list = ['Friesen!']*20

tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg='white')
canvas.pack()

y = 50

for item in my_list:
    canvas.create_text(250, y, text=item, fill="black", font=('Arial', 20))
    y += 20

tk.mainloop()
