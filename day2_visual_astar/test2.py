import matplotlib
matplotlib.use('TkAgg')  # 또는 'Qt5Agg'
import matplotlib.pyplot as plt
import numpy as np

print("backend:", matplotlib.get_backend())

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

for i in range(10):
    line.set_data(np.arange(i+1), np.random.rand(i+1)*10)
    fig.canvas.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()
