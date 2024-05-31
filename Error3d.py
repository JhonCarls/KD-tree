import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LineDrawer3D:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlim([0, 10])
        self.ax.set_ylim([0, 10])
        self.ax.set_zlim([0, 10])

        self.lines = []
        self.current_direction = 'xy'  # Alternar entre 'xy', 'xz' y 'yz'
        self.last_click = None

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.inaxes != self.ax:
            return

        x, y = event.xdata, event.ydata
        z = 0  # Para XY
        if self.current_direction == 'xy':
            self.draw_line(x, y, z, self.current_direction)
            self.current_direction = 'xz'
        elif self.current_direction == 'xz':
            y = self.last_click[1] if self.last_click else 0
            self.draw_line(x, y, event.zdata, self.current_direction)
            self.current_direction = 'yz'
        elif self.current_direction == 'yz':
            x = self.last_click[0] if self.last_click else 0
            self.draw_line(x, y, event.zdata, self.current_direction)
            self.current_direction = 'xy'

        self.last_click = (x, y, event.zdata)

    def draw_line(self, x, y, z, direction):
        if direction == 'xy':
            line = self.ax.plot([0, x], [0, y], [z, z], color='blue')
        elif direction == 'xz':
            line = self.ax.plot([0, x], [y, y], [0, z], color='green')
        elif direction == 'yz':
            line = self.ax.plot([x, x], [0, y], [0, z], color='red')

        self.lines.append((x, y, z, direction))
        plt.draw()

if __name__ == "__main__":
    drawer = LineDrawer3D()
    plt.show()
