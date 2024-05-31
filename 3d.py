import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def build_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return Node(
        points[median],
        axis,
        build_kdtree(points[:median], depth + 1),
        build_kdtree(points[median + 1:], depth + 1)
    )

def plot_tree(ax, tree, xmin, xmax, ymin, ymax, zmin, zmax):
    if tree is None:
        return

    point = tree.point
    axis = tree.axis

    if axis == 0:
        ax.plot([point[0], point[0]], [ymin, ymax], [zmin, zmax], color='black')
    elif axis == 1:
        ax.plot([xmin, xmax], [point[1], point[1]], [zmin, zmax], color='black')
    else:
        ax.plot([xmin, xmax], [ymin, ymax], [point[2], point[2]], color='black')

    plot_tree(ax, tree.left, xmin, point[0], ymin, ymax, zmin, zmax)
    plot_tree(ax, tree.right, point[0], xmax, ymin, ymax, zmin, zmax)

# Ejemplo de uso
points = [(2, 3, 1), (5, 4, 2), (9, 6, 3), (4, 7, 4), (8, 1, 5), (7, 2, 6)]
tree = build_kdtree(points)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xmin, ymin, zmin = min(p[0] for p in points), min(p[1] for p in points), min(p[2] for p in points)
xmax, ymax, zmax = max(p[0] for p in points), max(p[1] for p in points), max(p[2] for p in points)

plot_tree(ax, tree, xmin, xmax, ymin, ymax, zmin, zmax)

for point in points:
    ax.scatter(point[0], point[1], point[2], color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
