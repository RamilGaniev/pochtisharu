import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
for i in range(1, 10):
    file = open(f'{i}0 mm.txt', 'r')
    try:
        data = file.readlines()
    finally:
        file.close()
    y = np.array(data[4:], dtype='i')
    x = np.arange(-50, 50)
    ax.plot(x, y)
plt.show()
