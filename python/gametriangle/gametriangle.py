from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=600)
tk.title("game")
tk.resizable(0, 0)

X = 300
Y = 500

playercoords = []

def start_game():
    btn.destroy()
    canvas.pack()
    time.sleep(0.5)

    class Player:
        def __init__(self, canvas):
            self.x = X
            self.y = Y
            self.canvas = canvas
            self.id = canvas.create_polygon(
                300, 500, 250, 600, 350, 600, fill="blue"
            )
            self.canvas.move(self.id, 0, 0)
            self.x = 0
            self.y = 0
            tk.bind("<Left>", self.move_left)
            tk.bind("<Right>", self.move_right)

        def move_left(self, event):
            canvas.move(self.id, -2, 0)

        def move_right(self, event):
            canvas.move(self.id, 2, 0)

        def check_collision(self, adversary):
            player_coords = self.canvas.coords(self.id)
            adversary_coords = self.canvas.coords(adversary.id)
            if (
                player_coords[2] >= adversary_coords[0]
                and player_coords[0] <= adversary_coords[2]
                and player_coords[3] >= adversary_coords[1]
                and player_coords[1] <= adversary_coords[3]
            ):
                return True
            return False
        

    player = Player(canvas)

    class Adversary:
        def __init__(self, canvas):
            self.canvas = canvas
            self.id = canvas.create_rectangle(
                random.randint(10, 590),
                random.randint(10, 50),
                20,
                20,
                fill="red",
            )
            self.canvas.move(self.id, 0, 0)

        def move_down(self):
            self.canvas.move(self.id, 0, 5)

    adversaries = []

    while True:
        time.sleep(0.1)
        tk.update_idletasks()
        tk.update()

        for adversary in adversaries:
            adversary.move_down()

        if random.randint(1, 10) == 1:
            adversaries.append(Adversary(canvas))

        if any(player.check_collision(adversary) for adversary in adversaries):
            canvas.create_text(
                250, 250, text="You Lose", fill="green", font=("Helvetica", 30)
            )
            break


btn = Button(tk, text="start", command=start_game)
btn.pack()

tk.mainloop()
