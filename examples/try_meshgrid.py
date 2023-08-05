import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 绘制散点图
x1 = np.arange(-4, 4, 0.25)
x2 = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(x1, x2)

r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)

# 添加坐标轴(顺序是x, y, z)
ax.set_xlabel('x', fontdict={'size': 10, 'color': 'red'})
ax.set_ylabel('y', fontdict={'size': 10, 'color': 'green'})
ax.set_zlabel('z', fontdict={'size': 10, 'color': 'blue'})

plt.show()
