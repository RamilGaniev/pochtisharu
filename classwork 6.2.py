import csv
import matplotlib.pyplot as plt
import numpy as np
from homework3 import MNK

file = open('data1.csv', newline='')
x = []
y = []
deltax = []
deltay = []
fig, ax = plt.subplots()
try:
    reader = csv.reader(file)
    s = 0
    list = []
    for row in reader:
        s += 1
        list.append(row)
    for i in range(1, s):
        x.append(float(list[i][0]))
        y.append(float(list[i][2]))
        deltax.append(float(list[i][1]))
        deltay.append(float(list[i][3]))
finally:
    file.close()
x1list = [0, 0.5]
y1list = [MNK(x, y, 'b')]
y1list.append(x1list[1] * MNK(x, y, 'k') + MNK(x, y, 'b'))
x1 = np.array(x1list)
y1 = np.array(y1list)
ax.errorbar(x, y, deltay, deltax, fmt='.')
ax.plot(x1, y1)
plt.show()