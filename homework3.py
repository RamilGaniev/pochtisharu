import matplotlib.pyplot as plt
import random
import numpy as np


def averpower(list, n):
    output = 0
    for i in list:
        output += i ** n
    return output / len(list)


def MNK(xlist, ylist, j):
    xylist = []
    for i in range(len(xlist)):
        xylist.append(xlist[i] * ylist[i])
    k = (averpower(xylist, 1) - averpower(xlist, 1) * averpower(ylist, 1)) / (
            averpower(xlist, 2) - averpower(xlist, 1) ** 2)
    b = averpower(ylist, 1) - averpower(xlist, 1) * k
    deltak = (((averpower(ylist, 2) - averpower(ylist, 1) ** 2) / (
            averpower(xlist, 2) - averpower(xlist, 1) ** 2) - k) ** 0.5) * (
                     1 / (len(xlist) ** 0.5))
    deltab = deltak * ((averpower(xlist, 2) - averpower(xlist, 1) ** 2) ** 0.5)
    if j == 'k':
        return k
    if j == 'b':
        return b
    if j == 'deltak':
        return deltak
    if j == 'deltab':
        return deltab


xlist = []
ylist = []
k1 = random.random() * 5
b1 = random.random() * 50
lgh = 200
for i in range(lgh):
    rdxpoint = random.random() * 100
    rdypoint = rdxpoint * k1 + random.random() * 50 - 25 + b1
    xlist.append(rdxpoint)
    ylist.append(rdypoint)
x = np.array(xlist)
y = np.array(ylist)
x1list = [0, 100]
y1list = [MNK(xlist, ylist, 'b')]
y1list.append(x1list[1] * MNK(xlist, ylist, 'k') + MNK(xlist, ylist, 'b'))
x1 = np.array(x1list)
y1 = np.array(y1list)
x2list = [0, 100]
y2list = [b1]
y2list.append(x2list[1] * k1 + b1)
x2 = np.array(x2list)
y2 = np.array(y2list)
fig, ax = plt.subplots(figsize=(5, 7))
ax.scatter(x, y, s=2)
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('MNK')
fig.set_facecolor('lightsteelblue')
plt.show()
