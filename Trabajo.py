import tkinter as tk

class LineDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.lines = []
        self.current_direction = 'x'  # Alternar entre 'x' y 'y'
        self.last_click = None

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x, y = event.x, event.y
        print(f"Clic en: ({x}, {y})")

        if self.current_direction == 'x':
            self.draw_x_line(x, y)
        else:
            self.draw_y_line(x, y)

        self.current_direction = 'y' if self.current_direction == 'x' else 'x'
        self.last_click = (x, y)

    def draw_x_line(self, x, y):
        start_x, end_x = self.find_intersection(x, y, 'x')
        line = self.canvas.create_line(start_x, y, end_x, y, fill="blue")
        self.lines.append(('x', start_x, y, end_x, y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")
        self.canvas.create_text(x, y-10, text=f"({x}, {y})", anchor=tk.S)

    def draw_y_line(self, x, y):
        start_y, end_y = self.find_intersection(x, y, 'y')
        line = self.canvas.create_line(x, start_y, x, end_y, fill="green")
        self.lines.append(('y', x, start_y, x, end_y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")
        self.canvas.create_text(x, y-10, text=f"({x}, {y})", anchor=tk.S)

    def find_intersection(self, x, y, direction):
        if direction == 'x':
            start_x, end_x = 0, self.canvas.winfo_width()
            for line in self.lines:
                if line[0] == 'y':
                    line_x = line[1]
                    line_start_y = line[2]
                    line_end_y = line[4]
                    if line_start_y <= y <= line_end_y:
                        if line_x < x:
                            start_x = max(start_x, line_x)
                        elif line_x > x:
                            end_x = min(end_x, line_x)
            return start_x, end_x
        elif direction == 'y':
            start_y, end_y = 0, self.canvas.winfo_height()
            for line in self.lines:
                if line[0] == 'x':
                    line_y = line[2]
                    line_start_x = line[1]
                    line_end_x = line[3]
                    if line_start_x <= x <= line_end_x:
                        if line_y < y:
                            start_y = max(start_y, line_y)
                        elif line_y > y:
                            end_y = min(end_y, line_y)
            return start_y, end_y

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dibujador de Líneas")
    app = LineDrawer(root)
    root.mainloop()
