import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import KDTree

# Generar puntos aleatorios en un espacio 3D
np.random.seed(42)  # Para reproducibilidad
points = np.random.rand(100, 3) * 100  # 100 puntos en un cubo de 100x100x100

# Construir el KDTree
tree = KDTree(points)

# Punto de consulta
query_point = np.array([50, 50, 50])

# Encontrar el punto más cercano
distance, index = tree.query(query_point)
nearest_point = points[index]

# Visualización
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')
ax.scatter(query_point[0], query_point[1], query_point[2], c='r', marker='x', s=100)
ax.scatter(nearest_point[0], nearest_point[1], nearest_point[2], c='g', marker='x', s=100)

for point in points:
    ax.plot([point[0], nearest_point[0]], [point[1], nearest_point[1]], [point[2], nearest_point[2]], 'gray', linestyle='dashed', linewidth=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print(f"Query Point: {query_point}")
print(f"Nearest Point: {nearest_point}")
print(f"Distance: {distance}")
