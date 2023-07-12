import csv

import matplotlib.pyplot as plt

from homework3 import MNK

T = []
file1 = open("length.txt", 'r')
try:
    data = file1.readlines()
finally:
    file1.close()

L = float(data[0])
file = open('data.csv', newline='')
try:
    reader = csv.reader(file)
    col = 0
    list = []
    v = []
    for row in reader:
        col += 1
        list.append(row)
        v.append([])
    v.remove([])
    for str in range(1, col):
        T.append(float(list[str][0]))
        for elem in range(1, len(list[str])):
            v[str % len(list[str]) - 1].append(int(list[str][elem]))
finally:
    file.close()
c = []  # speed of the sound
for i in range(len(v)):
    fig, ax = plt.subplots()
    x = v[i]
    y = []
    for j in range(len(v[i])):
        y.append(j + 1)
    ax.plot(x, y)
    ax.scatter(x, y, color='purple')
    ax.set_xlabel('n')
    ax.set_ylabel('v')
    ax.set_title('Dependence between n and v')
    fig.set_facecolor('pink')
    location = 0  # For the best location
    legend_drawn_flag = True
    plt.legend(["Line", "Experimental Points"], loc=0, frameon=legend_drawn_flag)
    plt.show()
    c.append(MNK(y, x, 'k') * (2 * L))  # calculation by formulas and the smallest squares method
fig, ax = plt.subplots()
ax.plot(c, T)
ax.scatter(c, T, color='red')
ax.set_xlabel('C')
ax.set_ylabel('T')
ax.set_title('The dependence of the speed of sound on temperature')
fig.set_facecolor('lightsteelblue')
location = 0
legend_drawn_flag = True
plt.legend(["Line", "Experimental Points"], loc=0, frameon=legend_drawn_flag)
plt.show()
