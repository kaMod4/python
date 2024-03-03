import tkinter as tk

class GraphDrawer:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Drawer")

        self.canvas_width = 800
        self.canvas_height = 600

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.entry_label = tk.Label(self.master, text="Enter data points separated by commas:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.draw_button = tk.Button(self.master, text="Draw Graph", command=self.draw_graph)
        self.draw_button.pack()

    def draw_graph(self):
        self.canvas.delete("all")
        data_points_str = self.entry.get()

        if not data_points_str:
            self.show_message("Please enter data points.")
            return

        try:
            data_points = [int(num.strip()) for num in data_points_str.split(',')]
        except ValueError:
            self.show_message("Invalid input. Please enter valid integers separated by commas.")
            return

        num_points = len(data_points)
        x_unit = self.canvas_width / (num_points - 1) if num_points > 1 else self.canvas_width

        for i in range(num_points - 1):
            x1 = i * x_unit
            y1 = self.canvas_height - data_points[i]
            x2 = (i + 1) * x_unit
            y2 = self.canvas_height - data_points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    def show_message(self, message):
        tk.messagebox.showerror("Error", message)

def main():
    root = tk.Tk()
    app = GraphDrawer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
