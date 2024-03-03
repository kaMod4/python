#!/usr/bin/env python3


from tkinter import *


def create_text():
    canvas.delete("text_tag")
    user_text = entry.get()
    canvas.create_text(200, 200, text=user_text, tags="text_tag")


def on_entry_change(event):
    create_text()


tk = Tk()
canvas = Canvas(tk, height=400, width=400)
tk.resizable(0, 0)
canvas.pack()
tk.title("python text in-, output")

entry = Entry(tk)
entry.pack()
entry.bind("<Return>", on_entry_change)

canvas.create_text(200, 390, text="Type text here")


tk.mainloop()
