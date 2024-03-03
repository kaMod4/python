import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.root.geometry("400x400")
        
        self.rows = 10
        self.cols = 10
        
        self.num_mines = 10
        
        self.grid = []
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                self.grid[i].append(0)
                
        mine_coords = random.sample(range(self.rows * self.cols), self.num_mines)
        for coord in mine_coords:
            row = coord // self.cols
            col = coord % self.cols
            self.grid[row][col] = -1
                
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] != -1:
                    count = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            if i+dx >= 0 and i+dx < self.rows and j+dy >= 0 and j+dy < self.cols:
                                if self.grid[i+dx][j+dy] == -1:
                                    count += 1
                    self.grid[i][j] = count
        
        self.buttons = []
        for i in range(self.rows):
            self.buttons.append([])
            for j in range(self.cols):
                button = tk.Button(root, width=4, height=2, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i].append(button)
        
    def click(self, i, j):
        if self.grid[i][j] == -1:
            self.buttons[i][j].config(text="X", bg="red", state="disabled")
        else:
            self.buttons[i][j].config(text=self.grid[i][j], state="disabled")
        

root = tk.Tk()
game = Minesweeper(root)
root.mainloop()
