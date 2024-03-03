from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, 500, 500)
tk.title = "game: random number"

random_number = random.randint(1, 100)
number_guess = int(input("tipe a number from 1 to 100: "))
tries = 0

numbers = [range(1, 100)]


def play():
    global number_guess, tries

    while True:
        tries += 1
        if random_number > number_guess:
            print("my number is bigger")
            number_guess = int(input("try again: "))
        if number_guess > random_number:
            print("my number is smaller")
            number_guess = int(input("try again: "))
        else:
            print("""you won, and you needed """, tries, """tries""")
            return True


if number_guess not in numbers:
    print("you have to enter a number")
    play()
else:
    play()
