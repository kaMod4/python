from tkinter import *

def draw_graph(data_points):
    root = Tk()
    root.title("Graph")

    canvas = Canvas(root, width=600, height=400, bg='white')
    canvas.pack()

    x_scale = 50  # Scale for x-axis
    y_scale = 50  # Scale for y-axis

    # Draw x and y axes
    canvas.create_line(50, 350, 550, 350, width=2)  # x-axis
    canvas.create_line(50, 50, 50, 350, width=2)    # y-axis

    # Draw x-axis labels
    for i in range(len(data_points)):
        canvas.create_text((i + 1) * x_scale, 360, text=str(i + 1))

    # Draw y-axis labels
    for i in range(6):
        canvas.create_text(30, 350 - i * y_scale, text=str(i * 10))

    # Draw x and y coordinate lines
    canvas.create_line(50, 350, 50 + len(data_points) * x_scale, 350, fill='gray')
    canvas.create_line(50, 350, 50, 50, fill='gray')

    # Draw coordinate labels
    for i in range(len(data_points) + 1):
        canvas.create_text(50 + i * x_scale, 360, text=f'X{i + 1}', anchor='n')
    for i in range(7):
        canvas.create_text(40, 350 - i * y_scale, text=f'Y{i * 10}', anchor='e')

    # Draw data points as a line graph
    for i in range(len(data_points) - 1):
        x1 = 50 + (i + 1) * x_scale
        y1 = 350 - data_points[i] * y_scale
        x2 = 50 + (i + 2) * x_scale
        y2 = 350 - data_points[i + 1] * y_scale
        canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)

    root.mainloop()

# Example usage:
# data_points = [5, 10, 15, 20, 25, 20, 15, 10, 5]
# draw_graph(data_points)
