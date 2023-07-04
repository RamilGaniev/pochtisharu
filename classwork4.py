import matplotlib.pyplot as plt
import random
import numpy as np

data = [0] * 100
for j in range(100000):
    s = 0
    for i in range(100):
        s += random.randint(0, 1)
    data[s-1] += 1
for j in range(100):
    data[j] = data[j] / 100000

x = np.arange(0, np.size(data))
fig, ax = plt.subplots(figsize=(5,7), constrained_layout=True)
ax.plot(x, data)
ax.set_xlabel('x')
ax.set_ylabel('P(x)')
ax.set_title('Normal Distribution')
fig.set_facecolor('lightsteelblue')
plt.show()


